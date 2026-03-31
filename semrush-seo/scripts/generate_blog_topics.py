#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
博客选题矩阵生成器
基于竞对博客关键词数据生成选题矩阵
"""

import pandas as pd
import shutil
from pathlib import Path
import json
from datetime import datetime

# ==================== 配置区域 ====================
DATA_DIR = Path(__file__).parent.parent / "output" / "analysis_results"
OUTPUT_DIR = Path(__file__).parent.parent / "output" / "blog_topics"
ARCHIVE_DIR = OUTPUT_DIR / "archived"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)

# 主题关键词模式
TOPIC_PATTERNS = {
    "steel_types": ["steel", "cr13", "cr17", "vg10", "s30v", "s90v", "m390", "d2", "damascus", "n690", "aus8"],
    "knife_laws": ["law", "legal", "illegal", "code", "california", "texas", "carry", "ban", "permit"],
    "knife_types": ["knife", "blade", "dagger", "karambit", "cleaver", "kiritsuke", "gyuto", "santoku", "sword"],
    "maintenance": ["sharpen", "stone", "whetstone", "maintain", "care", "grit", "polish", "clean", "rust"],
    "comparison": ["vs", "versus", "compare", "better", "difference", "or", "which"],
    "cooking": ["chef", "kitchen", "cooking", "meat", "fish", "cutting", "food"],
    "outdoor": ["tactical", "survival", "hunting", "camping", "pocket", "edc", "outdoor"],
    "historical": ["viking", "medieval", "ancient", "samurai", "katana", "historical", "ww1", "ww2"],
}

CONTENT_TYPE_RULES = {
    "Ultimate Guide": ["guide", "complete", "ultimate", "everything", "comprehensive"],
    "How-to Tutorial": ["how to", "tutorial", "steps", "way", "make", "do", "tie", "sharpen"],
    "Comparison": ["vs", "versus", "compare", "difference", "better", "or"],
    "List Post": ["types", "best", "top", "list", "ideas", "examples"],
    "Review": ["review", "test", "analysis"],
    "News/Update": ["2024", "2025", "2026", "new", "latest"],
}


def load_blog_keywords() -> pd.DataFrame:
    """加载博客关键词数据"""
    filepath = DATA_DIR / "ai_ref_blog_keywords.csv"
    df = pd.read_csv(filepath)
    for col in ["Search Volume", "Keyword Difficulty", "Traffic"]:
        df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)
    return df


def load_archived_keywords() -> tuple:
    """从存档 CSV 和最新选题矩阵中加载已标记的关键词
    
    返回：(archived_set, archived_df)
    - archived_set: 已存档关键词集合（用于排除）
    - archived_df: 用户标记的完整数据（用于存档）
    """
    archived_set = set()
    archived_dfs = []
    
    # 1. 从合并的存档文件加载
    merged_file = ARCHIVE_DIR / "all_archived_keywords.csv"
    if merged_file.exists():
        try:
            df = pd.read_csv(merged_file)
            for kw in df["Keyword"].str.lower().dropna():
                archived_set.add(kw)
            print(f"  从 all_archived_keywords.csv 加载 {len(df)} 个已存档选题")
        except Exception as e:
            print(f"  读取 all_archived_keywords.csv 失败：{e}")
    
    # 2. 从最新的选题矩阵中读取用户标记的 archive=1
    latest_matrix = get_latest_matrix_file()
    if latest_matrix:
        try:
            df = pd.read_csv(latest_matrix)
            if "archive" in df.columns:
                # 使用 1 来判断（而不是 True）
                marked_df = df[df["archive"] == 1].copy()
                for kw in marked_df["Keyword"].str.lower().dropna():
                    # 只添加新的，不重复加载已存档的
                    if kw not in archived_set:
                        archived_dfs.append(pd.DataFrame([df[df["Keyword"].str.lower() == kw].iloc[0].to_dict()]))
                        archived_set.add(kw)
                if len(marked_df) > 0:
                    print(f"  从 {latest_matrix.name} 读取 {len(marked_df)} 个新标记选题")
        except Exception as e:
            print(f"  读取 {latest_matrix.name} 失败：{e}")
    
    return archived_set, archived_dfs


def get_latest_matrix_file() -> Path:
    """获取最新的选题矩阵文件"""
    files = sorted(OUTPUT_DIR.glob("blog_topic_matrix_*.csv"), reverse=True)
    return files[0] if files else None


def classify_topic(keyword: str) -> str:
    """分类主题"""
    kw_lower = str(keyword).lower()
    for topic, patterns in TOPIC_PATTERNS.items():
        for pattern in patterns:
            if pattern in kw_lower:
                return topic
    return "other"


def classify_content_type(keyword: str) -> str:
    """分类内容类型"""
    kw_lower = str(keyword).lower()
    for content_type, patterns in CONTENT_TYPE_RULES.items():
        for pattern in patterns:
            if pattern in kw_lower:
                return content_type
    return "Informational Post"


def calculate_priority_score(row: pd.Series) -> float:
    """计算优先级分数"""
    sv = row["Search Volume"]
    kd = row["Keyword Difficulty"]
    pos = row["Position"]
    traffic = row["Traffic"]

    if pos <= 3:
        factor = 1.5
    elif pos <= 10:
        factor = 1.2
    elif pos <= 20:
        factor = 1.0
    else:
        factor = 0.8

    priority = (sv * factor * (1 + traffic/100)) / (kd + 10)
    return round(priority, 2)


def generate_topic_matrix(df: pd.DataFrame, archived_keywords: set) -> pd.DataFrame:
    """生成选题矩阵（排除已标记存档的关键词）"""
    df = df.copy()
    df["topic"] = df["Keyword"].apply(classify_topic)
    df["content_type"] = df["Keyword"].apply(classify_content_type)
    df["priority_score"] = df.apply(calculate_priority_score, axis=1)
    df["archive"] = 0  # 默认不存档（使用 0 而不是 False）

    # 排除已标记存档的关键词
    df["is_archived"] = df["Keyword"].str.lower().isin(archived_keywords)
    df = df[~df["is_archived"]]

    matrix_df = df[[
        "Keyword", "Search Volume", "Keyword Difficulty",
        "Position", "Traffic", "topic", "content_type",
        "priority_score", "competitor", "archive"
    ]].copy()

    matrix_df = matrix_df.sort_values("priority_score", ascending=False)
    return matrix_df


def generate_topic_suggestions(matrix_df: pd.DataFrame) -> list:
    """生成选题建议（每个主题 Top 10）"""
    suggestions = []
    for topic in matrix_df["topic"].unique():
        topic_df = matrix_df[matrix_df["topic"] == topic].head(10)
        for _, row in topic_df.iterrows():
            suggestions.append({
                "topic": topic,
                "keyword": row["Keyword"],
                "search_volume": int(row["Search Volume"]),
                "difficulty": float(row["Keyword Difficulty"]),
                "priority_score": float(row["priority_score"]),
                "content_type": row["content_type"],
                "competitor": row["competitor"],
            })
    return suggestions


def archive_selected_topics(archived_dfs: list):
    """将用户标记的选题保存到存档，并合并所有 archive 词"""
    if not archived_dfs:
        return
    
    # 合并所有新标记的 DataFrame
    new_archived = pd.concat(archived_dfs, ignore_index=True) if len(archived_dfs) > 1 else archived_dfs[0]
    
    if len(new_archived) > 0:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # 添加存档时间列
        new_archived["archived_at"] = timestamp
        
        # 加载所有已存档的文件，合并为一个完整的存档
        all_archived = []
        for filepath in ARCHIVE_DIR.glob("archived_*.csv"):
            if filepath.name == "all_archived_keywords.csv":
                continue  # 跳过合并文件，避免重复
            try:
                df = pd.read_csv(filepath)
                all_archived.append(df)
            except Exception as e:
                print(f"  跳过 {filepath.name}: {e}")
        
        # 加载合并文件
        merged_file = ARCHIVE_DIR / "all_archived_keywords.csv"
        if merged_file.exists():
            try:
                df = pd.read_csv(merged_file)
                all_archived.insert(0, df)  # 放在最前面
            except Exception as e:
                print(f"  读取 all_archived_keywords.csv 失败：{e}")
        
        # 合并新旧存档
        if all_archived:
            combined_df = pd.concat(all_archived + [new_archived], ignore_index=True)
            # 去重（保留最新的）
            combined_df = combined_df.drop_duplicates(subset=["Keyword"], keep="last")
        else:
            combined_df = new_archived
        
        # 按优先级排序
        if "priority_score" in combined_df.columns:
            combined_df = combined_df.sort_values("priority_score", ascending=False)
        
        # 保存合并后的完整存档
        combined_df.to_csv(
            ARCHIVE_DIR / "all_archived_keywords.csv",
            index=False,
            encoding="utf-8-sig"
        )
        print(f"✓ 存档 {len(combined_df)} 个选题到 all_archived_keywords.csv")
        
        # 同时保存对应的 JSON
        suggestions = []
        for _, row in combined_df.iterrows():
            suggestions.append({
                "topic": row.get("topic", "unknown"),
                "keyword": row["Keyword"],
                "search_volume": int(row.get("Search Volume", 0)),
                "difficulty": float(row.get("Keyword Difficulty", 0)),
                "priority_score": float(row.get("priority_score", 0)),
                "content_type": row.get("content_type", "Informational Post"),
                "competitor": row.get("competitor", ""),
                "archived_at": row.get("archived_at", timestamp)
            })
        
        with open(ARCHIVE_DIR / "all_archived_keywords.json", "w", encoding="utf-8") as f:
            json.dump(suggestions, f, ensure_ascii=False, indent=2)
        print(f"✓ 存档 {len(suggestions)} 个选题到 all_archived_keywords.json")


def cleanup_old_files():
    """清理所有旧的输出文件（保留最新）"""
    # 清理 blog_topics 目录下的所有旧文件（CSV/JSON/MD）
    for ext in ["*.csv", "*.json", "*.md"]:
        for f in OUTPUT_DIR.glob(ext):
            if f.is_file():
                try:
                    f.unlink()
                    print(f"✓ 删除旧文件：{f.name}")
                except Exception as e:
                    print(f"✗ 删除失败 {f.name}: {e}")


def get_latest_matrix_file() -> Path:
    """获取最新的选题矩阵文件"""
    files = sorted(OUTPUT_DIR.glob("blog_topic_matrix_*.csv"), reverse=True)
    return files[0] if files else None


def generate_markdown_report(matrix_df: pd.DataFrame, suggestions: list):
    """生成 Markdown 报告"""
    topic_stats = matrix_df.groupby("topic").agg({
        "Keyword": "count",
        "Search Volume": "sum",
        "Traffic": "sum",
    })

    report = f"""# 博客选题矩阵报告

**生成时间**: {datetime.now().strftime("%Y-%m-%d %H:%M")}
**总选题数**: {len(matrix_df):,}

---

## 📊 主题分布

| 主题 | 关键词数 | 总搜索量 | 总流量 | 平均优先级 |
|------|----------|----------|--------|-----------|
"""
    for topic in topic_stats.index:
        stats = topic_stats.loc[topic]
        avg_priority = matrix_df[matrix_df["topic"] == topic]["priority_score"].mean()
        report += f"| {topic.replace('_', ' ').title()} | {int(stats['Keyword']):,} | {int(stats['Search Volume']):,} | {int(stats['Traffic']):,} | {avg_priority:.2f} |\n"

    report += """
---

## 🎯 高优先级选题推荐（Top 50）

| # | 主题 | 关键词 | 搜索量 | 难度 | 内容类型 | 竞对 |
|---|------|--------|--------|------|----------|------|
"""
    for i, sug in enumerate(suggestions[:50], 1):
        report += f"| {i} | {sug['topic'].replace('_', ' ').title()} | **{sug['keyword']}** | {sug['search_volume']:,} | {sug['difficulty']:.1f} | {sug['content_type']} | {sug['competitor']} |\n"

    report += """
---

## 📝 按主题分类选题

"""
    for topic in matrix_df["topic"].unique():
        topic_df = matrix_df[matrix_df["topic"] == topic].head(15)
        report += f"""### {topic.replace('_', ' ').title()}
| 关键词 | 搜索量 | 难度 | 优先级 | 类型 |
|--------|--------|------|--------|------|
"""
        for _, row in topic_df.iterrows():
            report += f"| {row['Keyword']} | {row['Search Volume']:,.0f} | {row['Keyword Difficulty']:.1f} | {row['priority_score']:.2f} | {row['content_type']} |\n"
        report += "\n"

    report += """
---

## 📅 内容日历建议

- **第 1-2 周**: 优先级>100 的选题，聚焦搜索量>1000
- **第 3-4 周**: 优先级 50-100，长尾关键词
- **第 5-8 周**: 覆盖各主题，建立内容集群

---

## ✏️ 如何标记选题

1. 打开 `blog_topic_matrix_*.csv`
2. 将已完成或不需要的选题 `archive` 列改为 `TRUE`
3. 重新运行脚本，标记的选题会被移动到 `archived/` 文件夹
4. 下次运行时，已存档的选题会自动排除
"""

    return report


def export_results(matrix_df: pd.DataFrame, suggestions: list):
    """导出结果"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # CSV - 包含 archive 列
    matrix_df.to_csv(OUTPUT_DIR / f"blog_topic_matrix_{timestamp}.csv", index=False, encoding="utf-8-sig")
    
    # JSON
    with open(OUTPUT_DIR / f"blog_suggestions_{timestamp}.json", "w", encoding="utf-8") as f:
        json.dump(suggestions, f, ensure_ascii=False, indent=2)
    
    # MD
    report = generate_markdown_report(matrix_df, suggestions)
    with open(OUTPUT_DIR / f"blog_topic_report_{timestamp}.md", "w", encoding="utf-8") as f:
        f.write(report)

    print(f"✓ blog_topic_matrix_{timestamp}.csv")
    print(f"✓ blog_suggestions_{timestamp}.json")
    print(f"✓ blog_topic_report_{timestamp}.md")


def main():
    print("🚀 开始生成博客选题...")
    print("=" * 50)

    # 先读取已存档关键词（在清理之前）
    print("\n🗄️ 加载已存档关键词...")
    archived_set, archived_dfs = load_archived_keywords()
    print(f"   已存档：{len(archived_set)} 个")

    # 清理旧文件
    print("\n🧹 清理旧文件...")
    cleanup_old_files()

    # 加载数据
    print("\n📂 加载博客关键词...")
    df = load_blog_keywords()
    print(f"   总数：{len(df)}")

    # 生成矩阵
    print("\n📐 生成选题矩阵...")
    matrix_df = generate_topic_matrix(df, archived_set)
    print(f"   新选题：{len(matrix_df)}")

    # 生成建议
    print("\n💡 生成选题建议...")
    suggestions = generate_topic_suggestions(matrix_df)

    # 导出
    print("\n💾 导出结果...")
    export_results(matrix_df, suggestions)

    # 存档标记的选题
    print("\n📁 处理存档选题...")
    archive_selected_topics(archived_dfs)

    # 摘要
    print("\n" + "=" * 50)
    print("📊 选题摘要")
    print("=" * 50)
    for topic in matrix_df["topic"].unique():
        count = len(matrix_df[matrix_df["topic"] == topic])
        print(f"  - {topic}: {count} 个")

    high_priority = len(matrix_df[matrix_df['priority_score'] > 100])
    print(f"\n高优先级 (priority>100): {high_priority}")
    print("\n✅ 完成!")


if __name__ == "__main__":
    main()

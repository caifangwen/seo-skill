#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
竞对关键词数据精简工具
输出简化核心列数据，生成 MD 洞察报告
"""

import pandas as pd
from pathlib import Path
import json
from datetime import datetime

# ==================== 配置区域 ====================
DATA_DIR = Path(__file__).parent.parent / "data"
OUTPUT_DIR = Path(__file__).parent.parent / "output" / "analysis_results"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# 简化核心列（输出 CSV 只保留这些列）
CORE_COLUMNS = [
    "Keyword",
    "Search Volume",
    "Keyword Difficulty",
    "Position",
    "Traffic",
    "URL",
    "competitor",
    "category",
]


def load_data():
    """加载所有竞对数据"""
    data_files = {
        "shieldon": DATA_DIR / "shieldon.net-organic.Positions-us-20260329-2026-03-31T02_22_30Z.csv",
        "noblie": DATA_DIR / "https___nobliecustomknives.com-organic.Positions-us-20260329-2026-03-31T02_25_00Z.csv",
        "koi": DATA_DIR / "https___www.koiknives.com_-organic.Positions-us-20260329-2026-03-31T02_46_50Z.csv",
        "zhangxiaoquan": DATA_DIR / "https___zhangxiaoquan.au_-organic.Positions-us-20260329-2026-03-31T02_44_43Z.xlsx",
        "insight": DATA_DIR / "https___www.insight-kitchenkni-organic.Positions-us-20260329-2026-03-31T02_24_01Z.csv",
        "xinzuo": DATA_DIR / "xinzuocutlery.com-organic.Positions-us-20260329-2026-03-31T02_43_00Z.csv",
    }

    all_data = []
    for name, filepath in data_files.items():
        try:
            df = pd.read_csv(filepath) if filepath.suffix == ".csv" else pd.read_excel(filepath)
            df["competitor"] = name
            all_data.append(df)
            print(f"✓ {name}: {len(df)} 条")
        except Exception as e:
            print(f"✗ {name}: {e}")

    return pd.concat(all_data, ignore_index=True)


def classify_category(url: str, intent: str) -> str:
    """分类：blog / product / page"""
    url_lower = str(url).lower() if pd.notna(url) else ""
    intent_lower = str(intent).lower() if pd.notna(intent) else ""

    if any(p in url_lower for p in ["/blog/", "/blogs/", "/news/"]):
        return "blog"
    if any(p in url_lower for p in ["/products/", "/product/", "/shop/"]):
        return "product"
    if "transactional" in intent_lower:
        return "product"
    if "navigational" in intent_lower:
        return "page"
    return "blog"


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """清洗数据"""
    for col in ["Search Volume", "Keyword Difficulty", "Position", "Traffic"]:
        df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)
    
    df["category"] = df.apply(lambda r: classify_category(r.get("URL"), r.get("Keyword Intents")), axis=1)
    
    # 去重：保留每个 Keyword+competitor 组合中流量最高的
    df = df.sort_values("Traffic", ascending=False).drop_duplicates(subset=["Keyword", "competitor"], keep="first")
    
    return df[CORE_COLUMNS]


def export_simplified_csvs(df: pd.DataFrame):
    """导出简化版 CSV 文件（完整行数，简化列）"""
    # 清理旧的输出文件
    for pattern in ["ai_ref_*.csv", "seo_insights_*.md"]:
        for f in OUTPUT_DIR.glob(pattern):
            f.unlink()
    print(f"✓ 清理旧文件")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # 1. 博客关键词
    blog_df = df[df["category"] == "blog"].sort_values("Traffic", ascending=False)
    blog_df.to_csv(OUTPUT_DIR / f"ai_ref_blog_keywords.csv", index=False, encoding="utf-8-sig")
    print(f"✓ ai_ref_blog_keywords.csv: {len(blog_df)} 条")

    # 2. 产品关键词
    product_df = df[df["category"] == "product"].sort_values("Traffic", ascending=False)
    product_df.to_csv(OUTPUT_DIR / f"ai_ref_product_keywords.csv", index=False, encoding="utf-8-sig")
    print(f"✓ ai_ref_product_keywords.csv: {len(product_df)} 条")

    # 3. 页面关键词
    page_df = df[df["category"] == "page"].sort_values("Traffic", ascending=False)
    page_df.to_csv(OUTPUT_DIR / f"ai_ref_page_keywords.csv", index=False, encoding="utf-8-sig")
    print(f"✓ ai_ref_page_keywords.csv: {len(page_df)} 条")

    # 4. 可竞争关键词（放宽筛选条件）
    competable = df[
        (df["Keyword Difficulty"] <= 40) &
        (df["Search Volume"] >= 30) &
        (df["Position"] <= 20)
    ].copy()
    competable["opportunity_score"] = (
        (competable["Search Volume"] * (100 - competable["Keyword Difficulty"])) /
        competable["Position"].replace(0, 1)
    ).round(0)
    competable = competable.sort_values("opportunity_score", ascending=False)
    competable.to_csv(OUTPUT_DIR / f"ai_ref_competable_keywords.csv", index=False, encoding="utf-8-sig")
    print(f"✓ ai_ref_competable_keywords.csv: {len(competable)} 条")

    return blog_df


def generate_insights_md(df: pd.DataFrame, blog_df: pd.DataFrame):
    """生成简化版 MD 洞察报告"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # 基础统计
    total_kw = len(df)
    total_traffic = df["Traffic"].sum()
    blog_count = len(blog_df)
    
    # 竞对统计
    competitor_stats = df.groupby("competitor").agg({
        "Keyword": "count",
        "Traffic": "sum"
    }).sort_values("Traffic", ascending=False)
    
    # 主题聚类
    topic_patterns = {
        "钢材": ["steel", "cr13", "cr17", "vg10", "s30v", "m390", "d2", "damascus"],
        "刀具类型": ["knife", "blade", "dagger", "karambit", "sword"],
        "法律法规": ["law", "legal", "illegal", "ban", "california", "texas"],
        "维护打磨": ["sharpen", "stone", "whetstone", "maintain", "clean"],
        "对比": ["vs", "versus", "compare", "better", "difference"],
        "厨房烹饪": ["chef", "kitchen", "cooking", "meat", "fish"],
        "户外战术": ["tactical", "survival", "hunting", "camping", "pocket", "edc"],
        "历史文化": ["viking", "medieval", "ancient", "samurai", "katana", "ww1"],
    }
    
    topic_keywords = {}
    for topic, patterns in topic_patterns.items():
        matches = df[df["Keyword"].str.lower().str.contains("|".join(patterns), na=False)]
        topic_keywords[topic] = {
            "count": len(matches),
            "traffic": matches["Traffic"].sum(),
            "top_keywords": matches.nlargest(10, "Traffic")["Keyword"].tolist()
        }
    
    # 高价值机会（低难度高流量）
    opportunities = df[
        (df["Keyword Difficulty"] <= 25) &
        (df["Search Volume"] >= 500) &
        (df["Position"] <= 10)
    ].nlargest(30, "Traffic")
    
    # 生成报告
    report = f"""# SEO 关键词洞察报告

**生成时间**: {datetime.now().strftime("%Y-%m-%d %H:%M")}
**数据来源**: 7 个竞对网站关键词数据

---

## 📊 核心数据

| 指标 | 数值 |
|------|------|
| 总关键词数 | {total_kw:,} |
| 博客关键词 | {blog_count:,} |
| 总流量 | {total_traffic:,.0f} |
| 平均难度 | {df["Keyword Difficulty"].mean():.1f} |

---

## 🏆 竞对流量排名

| 竞对 | 关键词数 | 总流量 |
|------|----------|--------|
"""
    for comp, row in competitor_stats.iterrows():
        report += f"| {comp} | {int(row['Keyword']):,} | {int(row['Traffic']):,.0f} |\n"
    
    report += """
---

## 🎯 高流量关键词 Top 50

| 关键词 | 搜索量 | 难度 | 排名 | 流量 | 竞对 |
|--------|--------|------|------|------|------|
"""
    top50 = df.nlargest(50, "Traffic")
    for _, row in top50.iterrows():
        report += f"| {row['Keyword']} | {int(row['Search Volume']):,} | {row['Keyword Difficulty']:.0f} | {int(row['Position'])} | {int(row['Traffic']):,.0f} | {row['competitor']} |\n"
    
    report += """
---

## 📈 主题领域分析

"""
    for topic, data in topic_keywords.items():
        report += f"""### {topic}
- 关键词数：{data['count']}
- 总流量：{data['traffic']:,.0f}
- 核心词：{', '.join(data['top_keywords'][:8])}

"""
    
    report += """---

## 💡 低难度高流量机会 (KD≤25, Vol≥500)

| 关键词 | 搜索量 | 难度 | 排名 | 流量 | 竞对 |
|--------|--------|------|------|------|------|
"""
    for _, row in opportunities.iterrows():
        report += f"| **{row['Keyword']}** | {int(row['Search Volume']):,} | {row['Keyword Difficulty']:.0f} | {int(row['Position'])} | {int(row['Traffic']):,.0f} | {row['competitor']} |\n"
    
    report += """
---

## 📝 内容建议

1. **优先覆盖**：搜索量>1000 且难度<30 的关键词
2. **博客选题**：参考 ai_ref_blog_keywords.csv 按流量排序
3. **产品优化**：参考 ai_ref_product_keywords.csv 优化产品页
4. **机会词**：关注 ai_ref_competable_keywords.csv 中的低竞争词

---
*完整数据见 analysis_results 目录下的 CSV 文件*
"""
    
    # 保存报告
    report_path = OUTPUT_DIR / f"seo_insights_{timestamp}.md"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"✓ 洞察报告：{report_path.name}")
    
    return report_path


def main():
    print("🚀 开始生成简化关键词数据...")
    print("=" * 50)
    
    print("\n📂 加载数据...")
    df = load_data()
    
    print("\n🧹 清洗数据...")
    clean_df = clean_data(df.copy())
    print(f"   去重后：{len(clean_df)} 条")
    
    print("\n📥 导出简化 CSV...")
    blog_df = export_simplified_csvs(clean_df)
    
    print("\n📊 生成洞察报告...")
    generate_insights_md(clean_df, blog_df)
    
    print("\n✅ 完成!")
    print(f"📁 输出目录：{OUTPUT_DIR}")


if __name__ == "__main__":
    main()

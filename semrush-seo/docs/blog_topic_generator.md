# 博客选题矩阵生成器 Skill

## 📋 Skill 描述

基于竞对关键词数据，自动生成博客选题矩阵，帮助内容团队规划高价值博客文章。

**核心功能：**
- 从 `ai_ref_blog_keywords.csv` 加载博客关键词
- 按主题聚类生成选题
- 评估每个选题的商业价值
- 输出优先级排序的选题矩阵

---

## 🎯 输入数据

### 必需文件
```
analysis_results/
├── ai_ref_blog_keywords.csv    # 博客关键词数据
├── ai_ref_topic_clusters.json  # 主题聚类
└── AI_KEYWORD_REFERENCE.md     # 参考文档
```

### 关键词数据格式
| Keyword | Search Volume | Keyword Difficulty | Position | Traffic | URL | Keyword Intents | competitor | category |
|---------|---------------|-------------------|----------|---------|-----|-----------------|------------|----------|
| seax | 6600 | 20.0 | 1 | 401 | ... | informational | noblie | blog |

---

## 📐 选题矩阵维度

### 1. 主题分类（Topic Cluster）
```
- Steel Types（钢材类型）
- Knife Laws（刀具法律）
- Knife Types（刀具类型）
- Maintenance（维护/磨刀）
- Comparison（对比评测）
- Cooking（烹饪技巧）
- Outdoor（户外/战术）
- Historical（历史/文化）
- Other（其他）
```

### 2. 搜索意图（Intent）
```
- Informational（信息类）- 教程、指南、知识
- Commercial（商业类）- 对比、评测、推荐
- Transactional（交易类）- 购买指南、价格分析
```

### 3. 优先级评分（Priority Score）
```
优先级 = (搜索量 × 流量潜力) / (难度 + 10)

流量潜力系数:
- 竞对排名 1-3: 1.5
- 竞对排名 4-10: 1.2
- 竞对排名 11-20: 1.0
- 竞对排名 20+: 0.8
```

### 4. 内容类型（Content Type）
```
- Ultimate Guide（终极指南）
- How-to Tutorial（教程）
- Comparison（对比）
- List Post（清单）
- Case Study（案例）
- News/Update（资讯）
```

---

## 🔧 使用脚本

### `generate_blog_topics.py`

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
博客选题矩阵生成器
基于竞对博客关键词数据生成选题矩阵
"""

import pandas as pd
import numpy as np
from pathlib import Path
import json
from datetime import datetime
from typing import Dict, List

# ==================== 配置区域 ====================
DATA_DIR = Path(__file__).parent.parent / "analysis_results"
OUTPUT_DIR = Path(__file__).parent.parent / "blog_topics"
OUTPUT_DIR.mkdir(exist_ok=True)

# 主题关键词模式
TOPIC_PATTERNS = {
    "steel_types": ["steel", "cr13", "cr17", "vg10", "s30v", "s90v", "m390", "d2", "damascus", "n690", "aus8"],
    "knife_laws": ["law", "legal", "illegal", "code", "california", "texas", "carry", "ban", "permit", "license"],
    "knife_types": ["knife", "blade", "dagger", "karambit", "cleaver", "kiritsuke", "gyuto", "santoku", "dagger", "sword"],
    "maintenance": ["sharpen", "stone", "whetstone", "maintain", "care", "grit", "polish", "clean", "rust"],
    "comparison": ["vs", "versus", "compare", "better", "difference", "or", "which"],
    "cooking": ["chef", "kitchen", "cooking", "meat", "fish", "cutting", "food", "recipe", "culinary"],
    "outdoor": ["tactical", "survival", "hunting", "camping", "pocket", "edc", "outdoor", "hiking"],
    "historical": ["viking", "medieval", "ancient", "samurai", "ninjato", "katana", "historical", "antique"],
}

# 内容类型判断规则
CONTENT_TYPE_RULES = {
    "Ultimate Guide": ["guide", "complete", "ultimate", "everything", "comprehensive"],
    "How-to Tutorial": ["how to", "tutorial", "steps", "way", "make", "do", "tie", "sharpen"],
    "Comparison": ["vs", "versus", "compare", "difference", "better", "or"],
    "List Post": ["types", "best", "top", "list", "ideas", "examples"],
    "Case Study": ["review", "test", "case", "analysis", "study"],
    "News/Update": ["2024", "2025", "2026", "new", "update", "latest"],
}


def load_blog_keywords() -> pd.DataFrame:
    """加载博客关键词数据"""
    filepath = DATA_DIR / "ai_ref_blog_keywords.csv"
    df = pd.read_csv(filepath)
    
    # 数据清洗
    for col in ["Search Volume", "Keyword Difficulty", "Traffic"]:
        df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)
    
    return df


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
    search_volume = row["Search Volume"]
    difficulty = row["Keyword Difficulty"]
    position = row["Position"]
    traffic = row["Traffic"]
    
    # 流量潜力系数
    if position <= 3:
        traffic_factor = 1.5
    elif position <= 10:
        traffic_factor = 1.2
    elif position <= 20:
        traffic_factor = 1.0
    else:
        traffic_factor = 0.8
    
    # 优先级公式
    priority = (search_volume * traffic_factor * (1 + traffic/100)) / (difficulty + 10)
    
    return round(priority, 2)


def generate_topic_matrix(df: pd.DataFrame) -> pd.DataFrame:
    """生成选题矩阵"""
    # 添加分类列
    df["topic"] = df["Keyword"].apply(classify_topic)
    df["content_type"] = df["Keyword"].apply(classify_content_type)
    df["priority_score"] = df.apply(calculate_priority_score, axis=1)
    
    # 提取核心列
    matrix_df = df[[
        "Keyword", "Search Volume", "Keyword Difficulty", 
        "Position", "Traffic", "topic", "content_type",
        "priority_score", "competitor"
    ]].copy()
    
    # 按优先级排序
    matrix_df = matrix_df.sort_values("priority_score", ascending=False)
    
    return matrix_df


def aggregate_by_topic(matrix_df: pd.DataFrame) -> Dict:
    """按主题聚合统计"""
    topic_stats = matrix_df.groupby("topic").agg({
        "Keyword": "count",
        "Search Volume": "sum",
        "Traffic": "sum",
        "priority_score": "mean",
    }).round(2)
    
    return topic_stats.to_dict()


def generate_topic_suggestions(matrix_df: pd.DataFrame) -> List[Dict]:
    """生成选题建议（每个主题 Top 5）"""
    suggestions = []
    
    for topic in matrix_df["topic"].unique():
        topic_df = matrix_df[matrix_df["topic"] == topic].head(5)
        
        for _, row in topic_df.iterrows():
            suggestions.append({
                "topic": topic,
                "keyword": row["Keyword"],
                "search_volume": int(row["Search Volume"]),
                "difficulty": float(row["Keyword Difficulty"]),
                "priority_score": float(row["priority_score"]),
                "content_type": row["content_type"],
                "competitor": row["competitor"],
                "reference_url": f"参考竞对：{row['competitor']}",
            })
    
    return suggestions


def export_results(matrix_df: pd.DataFrame, suggestions: List[Dict]):
    """导出结果"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # 1. 完整选题矩阵 CSV
    matrix_df.to_csv(
        OUTPUT_DIR / f"blog_topic_matrix_{timestamp}.csv",
        index=False,
        encoding="utf-8-sig"
    )
    
    # 2. 选题建议 JSON
    with open(OUTPUT_DIR / f"blog_suggestions_{timestamp}.json", "w", encoding="utf-8") as f:
        json.dump(suggestions, f, ensure_ascii=False, indent=2)
    
    # 3. Markdown 格式选题报告
    generate_markdown_report(matrix_df, suggestions, timestamp)
    
    print(f"✓ 结果已保存到：{OUTPUT_DIR}")


def generate_markdown_report(matrix_df: pd.DataFrame, suggestions: List[Dict], timestamp: str):
    """生成 Markdown 报告"""
    # 按主题统计
    topic_stats = matrix_df.groupby("topic").agg({
        "Keyword": "count",
        "Search Volume": "sum",
        "Traffic": "sum",
    }).round(0)
    
    report = f"""# 博客选题矩阵报告

**生成时间**: {datetime.now().strftime("%Y-%m-%d %H:%M")}
**数据来源**: 竞对博客关键词分析
**总关键词数**: {len(matrix_df):,}

---

## 📊 主题分布概览

| 主题 | 关键词数 | 总搜索量 | 总流量 | 平均优先级 |
|------|----------|----------|--------|-----------|
"""
    
    for topic in topic_stats.index:
        stats = topic_stats.loc[topic]
        avg_priority = matrix_df[matrix_df["topic"] == topic]["priority_score"].mean()
        report += f"| {topic.replace('_', ' ').title()} | {int(stats['Keyword']):,} | {int(stats['Search Volume']):,} | {int(stats['Traffic']):,} | {avg_priority:.2f} |\n"
    
    report += """
---

## 🎯 高优先级选题推荐（Top 30）

| 优先级 | 主题 | 关键词 | 搜索量 | 难度 | 内容类型 | 参考竞对 |
|--------|------|--------|--------|------|----------|----------|
"""
    
    for i, sug in enumerate(suggestions[:30], 1):
        report += f"| {i} | {sug['topic'].replace('_', ' ').title()} | **{sug['keyword']}** | {sug['search_volume']:,} | {sug['difficulty']:.1f} | {sug['content_type']} | {sug['competitor']} |\n"
    
    report += """
---

## 📝 按主题分类的选题建议

"""
    
    for topic in matrix_df["topic"].unique():
        topic_df = matrix_df[matrix_df["topic"] == topic].head(10)
        
        report += f"""### {topic.replace('_', ' ').title()}

**关键词数量**: {len(topic_df):,} | **总搜索量**: {topic_df['Search Volume'].sum():,.0f}

| 关键词 | 搜索量 | 难度 | 优先级 | 内容类型 |
|--------|--------|------|--------|----------|
"""
        
        for _, row in topic_df.iterrows():
            report += f"| {row['Keyword']} | {row['Search Volume']:,.0f} | {row['Keyword Difficulty']:.1f} | {row['priority_score']:.2f} | {row['content_type']} |\n"
        
        report += "\n"
    
    report += """
---

## 📅 内容日历建议

### 第 1-2 周（高优先级）
- 选择优先级 > 100 的选题
- 聚焦搜索量 > 1000 的关键词
- 内容类型：Ultimate Guide / How-to

### 第 3-4 周（中优先级）
- 选择优先级 50-100 的选题
- 聚焦长尾关键词
- 内容类型：Comparison / List Post

### 第 5-8 周（持续输出）
- 覆盖各主题领域
- 建立内容集群
- 内部链接互联

---

## 💡 内容优化建议

1. **关键词布局**: 每个选题的主关键词应出现在标题、H1、前 100 字
2. **内容长度**: 指南类 2000+ 词，教程类 1500+ 词，对比类 1200+ 词
3. **SERP 特征**: 针对有图片/视频 SERP 特征的关键词，添加对应媒体内容
4. **内部链接**: 同一主题的文章互相链接，形成内容集群
5. **更新频率**: 高优先级选题优先发布，保持每周 2-3 篇

---

## 📁 输出文件

| 文件名 | 说明 |
|--------|------|
| `blog_topic_matrix_{timestamp}.csv` | 完整选题矩阵 |
| `blog_suggestions_{timestamp}.json` | 结构化选题建议 |
| `blog_topic_report_{timestamp}.md` | 本报告 |

"""
    
    with open(OUTPUT_DIR / f"blog_topic_report_{timestamp}.md", "w", encoding="utf-8") as f:
        f.write(report)
    
    print(f"✓ 生成 Markdown 报告：blog_topic_report_{timestamp}.md")


# ==================== 主程序 ====================
def main():
    print("🚀 开始生成博客选题矩阵...")
    print("="*60)
    
    # 1. 加载数据
    print("\n📂 加载博客关键词数据...")
    df = load_blog_keywords()
    print(f"   总关键词数：{len(df)}")
    
    # 2. 生成选题矩阵
    print("\n📐 生成选题矩阵...")
    matrix_df = generate_topic_matrix(df)
    
    # 3. 按主题聚合
    print("\n📊 按主题聚合统计...")
    topic_stats = aggregate_by_topic(matrix_df)
    
    # 4. 生成选题建议
    print("\n💡 生成选题建议...")
    suggestions = generate_topic_suggestions(matrix_df)
    
    # 5. 导出结果
    print("\n💾 导出结果...")
    export_results(matrix_df, suggestions)
    
    # 6. 打印摘要
    print("\n" + "="*60)
    print("📊 选题矩阵摘要")
    print("="*60)
    print(f"\n总选题数：{len(matrix_df)}")
    print(f"\n主题分布:")
    for topic in matrix_df["topic"].unique():
        count = len(matrix_df[matrix_df["topic"] == topic])
        print(f"  - {topic}: {count} 个选题")
    
    print(f"\n高优先级选题（priority > 100）: {len(matrix_df[matrix_df['priority_score'] > 100])}")
    print(f"中优先级选题（50 < priority ≤ 100）: {len(matrix_df[(matrix_df['priority_score'] > 50) & (matrix_df['priority_score'] <= 100)])}")
    print(f"低优先级选题（priority ≤ 50）: {len(matrix_df[matrix_df['priority_score'] <= 50])}")
    
    print("\n✅ 完成!")


if __name__ == "__main__":
    main()

```

---

## 🚀 使用方法

### 1. 运行脚本
```bash
cd scripts
python generate_blog_topics.py
```

### 2. 查看输出
```
blog_topics/
├── blog_topic_matrix_20260331_120824.csv    # 完整选题矩阵 (24,076 条)
├── blog_suggestions_20260331_120824.json    # 结构化建议 (45 条)
└── blog_topic_report_20260331_120824.md     # Markdown 报告
```

### 3. 运行结果摘要
```
总选题数：24,076

主题分布:
  - knife_types: 9,536 个选题 (总搜索量 2,503,670)
  - other: 4,907 个选题
  - knife_laws: 3,586 个选题
  - steel_types: 3,080 个选题
  - comparison: 1,498 个选题
  - cooking: 731 个选题
  - maintenance: 548 个选题
  - outdoor: 136 个选题
  - historical: 54 个选题

高优先级选题（priority > 100）: 216
中优先级选题（50 < priority ≤ 100）: 349
低优先级选题（priority ≤ 50）: 23,511
```

---

## 📊 输出示例

### 选题矩阵 CSV 格式
```csv
Keyword,Search Volume,Keyword Difficulty,Position,Traffic,topic,content_type,priority_score,competitor
seax,6600,20.0,1,401,other,Informational Post,1653.30,noblie
kangaroo,110000,61.0,1,0,other,Informational Post,1239.44,koi
dagger,60500,36.0,2,45,knife_types,Informational Post,1105.36,noblie
pocket knife,49500,41.0,3,24,knife_types,Informational Post,849.51,koi
```

### 选题建议 JSON 格式
```json
[
  {
    "topic": "other",
    "keyword": "seax",
    "search_volume": 6600,
    "difficulty": 20.0,
    "priority_score": 1653.3,
    "content_type": "Informational Post",
    "competitor": "noblie"
  },
  {
    "topic": "knife_types",
    "keyword": "dagger",
    "search_volume": 60500,
    "difficulty": 36.0,
    "priority_score": 1105.36,
    "content_type": "Informational Post",
    "competitor": "noblie"
  }
]
```

---

## 📐 优先级评分说明

### 计算公式
```
优先级 = (搜索量 × 流量系数 × 难度系数) / (难度 + 10)

流量系数:
- 排名 1-3: 1.5（竞对已验证高流量）
- 排名 4-10: 1.2
- 排名 11-20: 1.0
- 排名 20+: 0.8

难度系数 = 1 + (流量/100)
```

### 优先级分级
| 优先级分数 | 级别 | 建议 |
|-----------|------|------|
| > 100 | 高 | 优先创作，第 1-2 周发布 |
| 50-100 | 中 | 常规创作，第 3-4 周发布 |
| < 50 | 低 | 补充内容，第 5-8 周发布 |

---

## 💡 内容类型说明

| 类型 | 适用场景 | 建议字数 |
|------|----------|----------|
| Ultimate Guide | 全面介绍某主题 | 2500+ |
| How-to Tutorial | 步骤教程 | 1500-2000 |
| Comparison | 产品/概念对比 | 1200-1800 |
| List Post | 清单/合集 | 1000-1500 |
| Case Study | 案例分析/评测 | 1500-2000 |
| News/Update | 资讯/更新 | 800-1200 |

---

## 📅 内容日历模板

### 周计划示例
```
第 1 周:
- 周一：[Historical] "seax" - Ultimate Guide (2500 词)
- 周三：[Knife Types] "knife types" - List Post (1500 词)
- 周五：[Maintenance] "sharpening angle" - How-to (1800 词)

第 2 周:
- 周一：[Comparison] "vg10 vs s30v" - Comparison (1500 词)
- 周三：[Outdoor] "karambit" - Ultimate Guide (2000 词)
- 周五：[Cooking] "kiritsuke knife uses" - How-to (1200 词)
```

---

## 🔗 与其他文件联动

1. **参考 `ai_ref_competable_keywords.csv`**: 找出竞对未充分覆盖的机会词
2. **参考 `ai_ref_topic_clusters.json`**: 确保内容覆盖面
3. **参考 `AI_KEYWORD_REFERENCE.md`**: 获取宏观数据支持

---

## 📝 Skill 使用提示词

```
请根据博客选题矩阵，为我的刀具电商网站规划一个月的内容日历。

要求：
1. 每周发布 3 篇文章
2. 覆盖至少 4 个不同主题
3. 优先选择优先级 > 50 的选题
4. 包含 1 篇 Ultimate Guide、2 篇 How-to、1 篇 Comparison

请参考 blog_topic_matrix.csv 和 blog_topic_report.md 中的数据。
```

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
技能 1: 内容大纲生成器
基于 core_insights.json 生成 SEO 优化的内容大纲
"""

import json
import pandas as pd
from pathlib import Path
from datetime import datetime
from typing import Dict, List

# ==================== 配置区域 ====================
DATA_DIR = Path(__file__).parent.parent / "analysis_results"
OUTPUT_DIR = Path(__file__).parent.parent / "content_outlines"
OUTPUT_DIR.mkdir(exist_ok=True)

# 内容模板
CONTENT_TEMPLATES = {
    "Ultimate Guide": {
        "structure": [
            "Introduction (What is X)",
            "Key Features/Benefits",
            "Types/Categories",
            "Comparison Table",
            "How to Choose",
            "How to Use/Maintain",
            "FAQ",
            "Conclusion"
        ],
        "word_count": "3000+",
        "elements": ["comparison table", "images", "FAQ schema"]
    },
    "How-to Tutorial": {
        "structure": [
            "Introduction (What you'll learn)",
            "Tools/Materials Needed",
            "Step-by-Step Instructions",
            "Tips and Best Practices",
            "Common Mistakes to Avoid",
            "FAQ",
            "Conclusion"
        ],
        "word_count": "1500-2500",
        "elements": ["step images", "video", "numbered list"]
    },
    "Comparison": {
        "structure": [
            "Introduction (What we're comparing)",
            "Overview of Each Option",
            "Head-to-Head Comparison",
            "Pros and Cons",
            "Which One to Choose",
            "FAQ",
            "Conclusion"
        ],
        "word_count": "2000-3000",
        "elements": ["comparison table", "pros/cons list", "verdict box"]
    },
    "List Post": {
        "structure": [
            "Introduction (Why this list matters)",
            "Item 1: Name + Description + Pros/Cons",
            "Item 2: Name + Description + Pros/Cons",
            "...",
            "Comparison Summary",
            "FAQ",
            "Conclusion"
        ],
        "word_count": "2000-3500",
        "elements": ["product images", "buy buttons", "rating stars"]
    }
}

# 主题到内容类型的映射
TOPIC_CONTENT_MAPPING = {
    "steel_types": ["Ultimate Guide", "Comparison", "List Post"],
    "knife_laws": ["Ultimate Guide", "How-to Tutorial"],
    "knife_types": ["Ultimate Guide", "List Post"],
    "maintenance": ["How-to Tutorial", "Ultimate Guide"],
    "comparison": ["Comparison", "List Post"],
    "cooking": ["How-to Tutorial", "List Post"],
    "outdoor": ["List Post", "Ultimate Guide"],
    "historical": ["Ultimate Guide", "List Post"],
}


def load_core_insights() -> Dict:
    """加载核心洞察数据"""
    files = list(DATA_DIR.glob("core_insights_*.json"))
    if not files:
        raise FileNotFoundError("未找到 core_insights.json 文件")
    
    with open(files[0], "r", encoding="utf-8") as f:
        return json.load(f)


def load_topic_clusters() -> Dict:
    """加载主题聚类"""
    files = list(DATA_DIR.glob("ai_ref_topic_clusters.json"))
    if not files:
        raise FileNotFoundError("未找到 ai_ref_topic_clusters.json 文件")
    
    with open(files[0], "r", encoding="utf-8") as f:
        return json.load(f)


def generate_outline_for_topic(topic: str, keywords: List[str], insights: Dict) -> List[Dict]:
    """为单个主题生成内容大纲"""
    outlines = []
    content_types = TOPIC_CONTENT_MAPPING.get(topic, ["Ultimate Guide"])
    
    for content_type in content_types:
        template = CONTENT_TEMPLATES.get(content_type, CONTENT_TEMPLATES["Ultimate Guide"])
        
        # 主关键词（搜索量最高）
        main_keyword = keywords[0] if keywords else topic
        
        # 生成大纲
        outline = {
            "topic": topic,
            "content_type": content_type,
            "main_keyword": main_keyword,
            "title_suggestions": generate_titles(main_keyword, content_type),
            "structure": [],
            "word_count": template["word_count"],
            "recommended_elements": template["elements"],
            "keyword_distribution": {}
        }
        
        # 生成结构
        for i, section in enumerate(template["structure"]):
            section_keywords = get_section_keywords(section, keywords, i)
            outline["structure"].append({
                "section": section,
                "heading_level": "H2" if i < 5 else "H3",
                "suggested_keywords": section_keywords[:3]
            })
            outline["keyword_distribution"][section] = section_keywords[:2]
        
        outlines.append(outline)
    
    return outlines


def generate_titles(keyword: str, content_type: str) -> List[str]:
    """生成标题建议"""
    templates = {
        "Ultimate Guide": [
            f"The Complete Guide to {keyword.title()} (2026)",
            f"{keyword.title()}: Everything You Need to Know",
            f"Ultimate {keyword.title()} Guide for Beginners & Pros"
        ],
        "How-to Tutorial": [
            f"How to {keyword.title()}: Step-by-Step Guide",
            f"{keyword.title()}: A Beginner's Tutorial",
            f"Master {keyword.title()} in 5 Easy Steps"
        ],
        "Comparison": [
            f"{keyword.title()}: Head-to-Head Comparison",
            f"Best {keyword.title()}: Tested & Compared",
            f"{keyword.title()} Showdown: Which One Wins?"
        ],
        "List Post": [
            f"Top 10 {keyword.title()} for 2026",
            f"Best {keyword.title()}: Expert Picks",
            f"15 {keyword.title()} You Need to Know"
        ]
    }
    
    return templates.get(content_type, templates["Ultimate Guide"])


def get_section_keywords(section: str, keywords: List[str], index: int) -> List[str]:
    """为章节分配关键词"""
    # 简单分配：前 3 个给引言，接下来每 2-3 个给一个章节
    start_idx = index * 2
    end_idx = start_idx + 3
    
    related = keywords[start_idx:end_idx] if start_idx < len(keywords) else []
    
    # 如果没有足够关键词，使用主题相关词
    if not related:
        related = [f"{section.lower()} tips", f"{section.lower()} guide"]
    
    return related


def generate_outlines_report(outlines: List[Dict]) -> str:
    """生成 Markdown 报告"""
    report = """# SEO 内容大纲报告

**生成时间**: {timestamp}
**数据来源**: core_insights.json + topic_clusters
**总大纲数**: {count}

---

""".format(
        timestamp=datetime.now().strftime("%Y-%m-%d %H:%M"),
        count=len(outlines)
    )
    
    for outline in outlines:
        report += f"""## 主题：{outline['topic'].replace('_', ' ').title()}

### 内容类型：{outline['content_type']}

**目标关键词**: {outline['main_keyword']}
**建议字数**: {outline['word_count']}

#### 标题建议
"""
        for i, title in enumerate(outline['title_suggestions'], 1):
            report += f"{i}. **{title}**\n"
        
        report += "\n#### 内容结构\n\n"
        
        for section in outline['structure']:
            keywords_str = ", ".join(section['suggested_keywords'])
            report += f"- **{section['heading_level]}**: {section['section']}\n"
            report += f"  - 关键词：{keywords_str}\n"
        
        report += f"\n#### 推荐元素\n"
        for element in outline['recommended_elements']:
            report += f"- [ ] {element}\n"
        
        report += "\n---\n\n"
    
    return report


def main():
    print("🚀 开始生成内容大纲...")
    print("="*60)
    
    # 1. 加载数据
    print("\n📂 加载数据...")
    try:
        insights = load_core_insights()
        topics = load_topic_clusters()
        print(f"   加载 {len(topics)} 个主题")
    except FileNotFoundError as e:
        print(f"❌ {e}")
        return
    
    # 2. 为每个主题生成大纲
    print("\n📝 生成内容大纲...")
    all_outlines = []
    
    for topic, keywords in topics.items():
        outlines = generate_outline_for_topic(topic, keywords, insights)
        all_outlines.extend(outlines)
        print(f"   ✓ {topic}: {len(outlines)} 个大纲")
    
    # 3. 导出结果
    print("\n💾 导出结果...")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Markdown 报告
    report = generate_outlines_report(all_outlines)
    with open(OUTPUT_DIR / f"content_outlines_{timestamp}.md", "w", encoding="utf-8") as f:
        f.write(report)
    
    # JSON 数据
    with open(OUTPUT_DIR / f"content_outlines_{timestamp}.json", "w", encoding="utf-8") as f:
        json.dump(all_outlines, f, ensure_ascii=False, indent=2)
    
    print(f"✓ 结果已保存到：{OUTPUT_DIR}")
    print(f"\n📊 摘要：共生成 {len(all_outlines)} 个内容大纲")
    print("\n✅ 完成!")


if __name__ == "__main__":
    main()

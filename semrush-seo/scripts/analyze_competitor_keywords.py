#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
竞对关键词分析工具
功能：
1. 找能竞争的关键词（低难度、高搜索量、竞对排名靠前）
2. 产品/博客/页面关键词分类
3. 核心数据拆分供 AI 调用
"""

import pandas as pd
import numpy as np
from pathlib import Path
import json
from datetime import datetime
from typing import Dict, List, Tuple
import re

# ==================== 配置区域 ====================
DATA_DIR = Path(__file__).parent.parent / "data"
OUTPUT_DIR = Path(__file__).parent.parent / "analysis_results"
OUTPUT_DIR.mkdir(exist_ok=True)

# 竞争关键词筛选条件
MIN_SEARCH_VOLUME = 50      # 最小搜索量
MAX_DIFFICULTY = 30         # 最大难度（越低越容易竞争）
MAX_POSITION = 10           # 竞对排名上限（前 10 名）
MIN_TRAFFIC = 5             # 最小流量贡献

# 关键词分类规则（URL 模式匹配）
URL_PATTERNS = {
    "product": [
        r"/products/",
        r"/product/",
        r"/shop/",
        r"/item/",
        r"/collections/",
        r"product.*html",
    ],
    "blog": [
        r"/blog/",
        r"/blogs/",
        r"/news/",
        r"/article/",
        r"/guide/",
        r"/tips/",
        r"blog.*html",
    ],
    "category": [
        r"/category/",
        r"/categories/",
        r"/collections/",
        r"/type/",
    ],
    "informational": [
        r"/guide/",
        r"/how-to/",
        r"/what-is/",
        r"/vs/",
        r"/compare/",
        r"/review/",
        r"/law/",
        r"/legal/",
    ],
}

# 关键词意图映射
INTENT_MAPPING = {
    "transactional": "product",      # 交易意图 -> 产品页
    "commercial": "product",         # 商业意图 -> 产品/对比页
    "informational": "blog",         # 信息意图 -> 博客/文章
    "navigational": "page",          # 导航意图 -> 首页/品牌页
}


# ==================== 数据加载 ====================
def load_all_data() -> Dict[str, pd.DataFrame]:
    """加载所有竞对数据"""
    data_files = {
        "shieldon": DATA_DIR / "shieldon.net-organic.Positions-us-20260329-2026-03-31T02_22_30Z.csv",
        "noblie": DATA_DIR / "https___nobliecustomknives.com-organic.Positions-us-20260329-2026-03-31T02_25_00Z.csv",
        "koi": DATA_DIR / "https___www.koiknives.com_-organic.Positions-us-20260329-2026-03-31T02_46_50Z.csv",
        "rtkitchen": DATA_DIR / "https___www.rtkitchenknife.com-organic.Positions-us-20260329-2026-03-31T02_43_41Z.xlsx",
        "zhangxiaoquan": DATA_DIR / "https___zhangxiaoquan.au_-organic.Positions-us-20260329-2026-03-31T02_44_43Z.xlsx",
        "biliknife": DATA_DIR / "data/https___biliknife.com-organic.Positions-us-20260329-2026-03-31T02_28_09Z.xlsx",
        "insight": DATA_DIR / "https___www.insight-kitchenkni-organic.Positions-us-20260329-2026-03-31T02_24_01Z.csv",
        "xinzuo": DATA_DIR / "xinzuocutlery.com-organic.Positions-us-20260329-2026-03-31T02_43_00Z.csv",
    }
    
    dataframes = {}
    for name, filepath in data_files.items():
        try:
            if filepath.suffix == ".csv":
                df = pd.read_csv(filepath)
            else:
                df = pd.read_excel(filepath)
            df["competitor"] = name
            dataframes[name] = df
            print(f"✓ 加载 {name}: {len(df)} 条记录")
        except Exception as e:
            print(f"✗ 加载失败 {name}: {e}")
    
    return dataframes


def combine_data(dataframes: Dict[str, pd.DataFrame]) -> pd.DataFrame:
    """合并所有数据"""
    return pd.concat(dataframes.values(), ignore_index=True)


# ==================== 功能 1: 找能竞争的关键词 ====================
def find_competable_keywords(df: pd.DataFrame) -> pd.DataFrame:
    """
    找出可以竞争的关键词
    策略：
    - 低难度 (KD < 30)
    - 有一定搜索量 (SV > 50)
    - 竞对排名靠前但非绝对垄断
    - 有流量潜力
    """
    # 数据清洗
    df_clean = df.copy()
    df_clean["Search Volume"] = pd.to_numeric(df_clean["Search Volume"], errors="coerce").fillna(0)
    df_clean["Keyword Difficulty"] = pd.to_numeric(df_clean["Keyword Difficulty"], errors="coerce").fillna(50)
    df_clean["Position"] = pd.to_numeric(df_clean["Position"], errors="coerce").fillna(100)
    df_clean["Traffic"] = pd.to_numeric(df_clean["Traffic"], errors="coerce").fillna(0)
    
    # 筛选条件
    mask = (
        (df_clean["Keyword Difficulty"] <= MAX_DIFFICULTY) &
        (df_clean["Search Volume"] >= MIN_SEARCH_VOLUME) &
        (df_clean["Position"] <= MAX_POSITION) &
        (df_clean["Traffic"] >= MIN_TRAFFIC)
    )
    
    result = df_clean[mask].copy()
    
    # 计算竞争指数 (机会分数)
    # 机会分数 = (搜索量 * (100 - 难度)) / 位置
    result["opportunity_score"] = (
        (result["Search Volume"] * (100 - result["Keyword Difficulty"])) / result["Position"]
    ).round(2)
    
    # 按机会分数排序
    result = result.sort_values("opportunity_score", ascending=False)
    
    return result


def analyze_keyword_gaps(dataframes: Dict[str, pd.DataFrame]) -> pd.DataFrame:
    """
    分析关键词差距
    找出多个竞对都排名但你的网站没有的关键词
    """
    # 统计每个关键词被多少竞对覆盖
    keyword_competitors = {}
    
    for name, df in dataframes.items():
        for keyword in df["Keyword"].unique():
            if keyword not in keyword_competitors:
                keyword_competitors[keyword] = []
            keyword_competitors[keyword].append(name)
    
    # 创建差距分析表
    gap_data = []
    for keyword, competitors in keyword_competitors.items():
        # 找出所有竞对该关键词的最佳数据
        best_position = 100
        best_traffic = 0
        best_competitor = None
        
        for comp in competitors:
            comp_df = dataframes[comp]
            keyword_data = comp_df[comp_df["Keyword"] == keyword]
            if len(keyword_data) > 0:
                min_pos = keyword_data["Position"].min()
                total_traffic = keyword_data["Traffic"].sum()
                if min_pos < best_position:
                    best_position = min_pos
                    best_traffic = total_traffic
                    best_competitor = comp
        
        gap_data.append({
            "keyword": keyword,
            "competitor_count": len(competitors),
            "competitors": competitors,
            "best_position": best_position,
            "best_traffic": best_traffic,
            "dominant_competitor": best_competitor,
        })
    
    gap_df = pd.DataFrame(gap_data)
    gap_df = gap_df.sort_values(["competitor_count", "best_traffic"], ascending=[False, False])
    
    return gap_df


# ==================== 功能 2: 关键词分类 ====================
def classify_keyword_by_url(url: str) -> str:
    """根据 URL 分类关键词"""
    if pd.isna(url):
        return "unknown"
    
    url_lower = url.lower()
    
    # 按优先级匹配
    for category, patterns in URL_PATTERNS.items():
        for pattern in patterns:
            if re.search(pattern, url_lower):
                return category
    
    # 默认根据域名判断
    return "page"


def classify_by_intent(intent: str) -> str:
    """根据搜索意图分类"""
    if pd.isna(intent):
        return "unknown"
    
    intent_lower = intent.lower()
    
    if "transactional" in intent_lower:
        return "product"
    elif "commercial" in intent_lower:
        return "product"
    elif "informational" in intent_lower:
        return "blog"
    elif "navigational" in intent_lower:
        return "page"
    
    return "blog"  # 默认归为博客


def classify_keywords(df: pd.DataFrame) -> pd.DataFrame:
    """
    对关键词进行分类
    返回：产品关键词、博客关键词、页面关键词
    """
    df_classified = df.copy()
    
    # 基于 URL 分类
    df_classified["url_category"] = df_classified["URL"].apply(classify_keyword_by_url)
    
    # 基于意图分类
    df_classified["intent_category"] = df_classified["Keyword Intents"].apply(classify_by_intent)
    
    # 综合分类（意图优先）
    def final_category(row):
        if row["intent_category"] != "unknown":
            return row["intent_category"]
        if row["url_category"] != "unknown":
            return row["url_category"]
        return "blog"  # 默认
    
    df_classified["final_category"] = df_classified.apply(final_category, axis=1)
    
    return df_classified


def get_category_summary(df_classified: pd.DataFrame) -> Dict:
    """获取分类汇总统计"""
    summary = {
        "by_intent": df_classified.groupby("intent_category").agg({
            "Keyword": "count",
            "Search Volume": "sum",
            "Traffic": "sum",
        }).to_dict(),
        "by_url": df_classified.groupby("url_category").agg({
            "Keyword": "count",
            "Search Volume": "sum",
            "Traffic": "sum",
        }).to_dict(),
        "by_final": df_classified.groupby("final_category").agg({
            "Keyword": "count",
            "Search Volume": "sum",
            "Traffic": "sum",
        }).to_dict(),
    }
    return summary


# ==================== 功能 3: 核心数据拆分（AI 调用依据） ====================
def extract_core_insights(df: pd.DataFrame) -> Dict:
    """
    提取核心洞察，作为 AI 下一步调用的依据
    包含：
    - 高价值关键词列表
    - 内容主题聚类
    - 竞争对手策略分析
    - SERP 特征分析
    """
    
    # 1. 高价值关键词（Top 100 by traffic）
    df_sorted = df.sort_values("Traffic", ascending=False)
    top_keywords = df_sorted.head(100)[["Keyword", "Position", "Search Volume", 
                                         "Keyword Difficulty", "Traffic", "URL", 
                                         "competitor"]].to_dict("records")
    
    # 2. 主题聚类（基于关键词提取）
    topic_keywords = extract_topics(df)
    
    # 3. 竞争对手策略
    competitor_strategy = analyze_competitor_strategy(df)
    
    # 4. SERP 特征分析
    serp_analysis = analyze_serp_features(df)
    
    # 5. 搜索意图分布
    intent_distribution = df.groupby("Keyword Intents").size().to_dict()
    
    # 6. 难度分布
    difficulty_levels = {
        "easy (0-15)": len(df[df["Keyword Difficulty"] <= 15]),
        "medium (16-30)": len(df[(df["Keyword Difficulty"] > 15) & (df["Keyword Difficulty"] <= 30)]),
        "hard (31-50)": len(df[(df["Keyword Difficulty"] > 30) & (df["Keyword Difficulty"] <= 50)]),
        "very_hard (51+)": len(df[df["Keyword Difficulty"] > 50]),
    }
    
    return {
        "generated_at": datetime.now().isoformat(),
        "total_keywords": len(df),
        "high_value_keywords": top_keywords,
        "topic_clusters": topic_keywords,
        "competitor_strategy": competitor_strategy,
        "serp_features": serp_analysis,
        "intent_distribution": intent_distribution,
        "difficulty_distribution": difficulty_levels,
    }


def extract_topics(df: pd.DataFrame) -> Dict:
    """提取关键词主题聚类"""
    # 基于关键词前缀/后缀聚类
    topics = {
        "steel_types": [],      # 钢材类型
        "knife_laws": [],       # 刀具法律
        "knife_types": [],      # 刀具类型
        "maintenance": [],      # 维护/磨刀
        "comparison": [],       # 对比类
        "brand_terms": [],      # 品牌词
        "cooking": [],          # 烹饪相关
        "other": [],
    }
    
    # 主题关键词模式
    patterns = {
        "steel_types": ["steel", "cr13", "cr17", "vg10", "s30v", "s90v", "m390", "d2", "damascus"],
        "knife_laws": ["law", "legal", "illegal", "code", "california", "texas", "carry"],
        "knife_types": ["knife", "blade", "dagger", "karambit", "cleaver", "kiritsuke", "gyuto"],
        "maintenance": ["sharpen", "stone", "whetstone", "maintain", "care", "grit"],
        "comparison": ["vs", "versus", "compare", "better", "difference"],
        "brand_terms": ["shieldon", "noblie", "koi", "custom", "japanese"],
        "cooking": ["chef", "kitchen", "cooking", "meat", "fish", "cutting"],
    }
    
    for keyword in df["Keyword"].unique():
        if pd.isna(keyword):
            continue
        kw_lower = keyword.lower()
        matched = False
        for topic, keywords_list in patterns.items():
            for pattern in keywords_list:
                if pattern in kw_lower:
                    topics[topic].append(keyword)
                    matched = True
                    break
            if matched:
                break
        if not matched:
            topics["other"].append(keyword)
    
    # 返回每个主题的前 20 个关键词
    return {topic: kw[:20] for topic, kw in topics.items()}


def analyze_competitor_strategy(df: pd.DataFrame) -> Dict:
    """分析竞争对手策略"""
    strategies = {}
    
    for competitor in df["competitor"].unique():
        comp_df = df[df["competitor"] == competitor]
        
        # 计算关键指标
        total_keywords = len(comp_df)
        total_traffic = comp_df["Traffic"].sum() if "Traffic" in comp_df.columns else 0
        avg_position = comp_df["Position"].mean() if "Position" in comp_df.columns else 0
        top_pages = comp_df.groupby("URL")["Traffic"].sum().nlargest(5).to_dict()
        
        strategies[competitor] = {
            "total_keywords": int(total_keywords),
            "total_traffic": float(total_traffic) if not pd.isna(total_traffic) else 0,
            "avg_position": float(avg_position) if not pd.isna(avg_position) else 0,
            "top_performing_pages": top_pages,
        }
    
    return strategies


def analyze_serp_features(df: pd.DataFrame) -> Dict:
    """分析 SERP 特征"""
    if "SERP Features by Keyword" not in df.columns:
        return {}
    
    feature_counts = {}
    for features in df["SERP Features by Keyword"].dropna():
        for feature in str(features).split(", "):
            feature = feature.strip()
            if feature:
                feature_counts[feature] = feature_counts.get(feature, 0) + 1
    
    # 按频率排序
    sorted_features = dict(sorted(feature_counts.items(), key=lambda x: x[1], reverse=True))
    
    return sorted_features


# ==================== 输出结果 ====================
def save_results(competable_keywords: pd.DataFrame, 
                 classified_keywords: pd.DataFrame,
                 core_insights: Dict,
                 category_summary: Dict):
    """保存分析结果"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # 1. 可竞争关键词
    competable_keywords.to_csv(
        OUTPUT_DIR / f"competable_keywords_{timestamp}.csv", 
        index=False,
        encoding="utf-8-sig"
    )
    
    # 2. 分类后的关键词
    classified_keywords.to_csv(
        OUTPUT_DIR / f"classified_keywords_{timestamp}.csv",
        index=False,
        encoding="utf-8-sig"
    )
    
    # 3. 核心洞察（JSON 格式供 AI 调用）
    with open(OUTPUT_DIR / f"core_insights_{timestamp}.json", "w", encoding="utf-8") as f:
        json.dump(core_insights, f, ensure_ascii=False, indent=2, default=str)
    
    # 4. 分类汇总
    with open(OUTPUT_DIR / f"category_summary_{timestamp}.json", "w", encoding="utf-8") as f:
        json.dump(category_summary, f, ensure_ascii=False, indent=2, default=str)
    
    # 5. 按类别导出
    for category in classified_keywords["final_category"].unique():
        cat_df = classified_keywords[classified_keywords["final_category"] == category]
        cat_df.to_csv(
            OUTPUT_DIR / f"keywords_{category}_{timestamp}.csv",
            index=False,
            encoding="utf-8-sig"
        )
    
    print(f"\n✓ 结果已保存到：{OUTPUT_DIR}")


def print_summary(competable_keywords: pd.DataFrame, 
                  classified_keywords: pd.DataFrame,
                  core_insights: Dict):
    """打印分析摘要"""
    print("\n" + "="*60)
    print("📊 竞对关键词分析摘要")
    print("="*60)
    
    print(f"\n📈 总关键词数量：{core_insights['total_keywords']}")
    
    print("\n🎯 可竞争关键词数量:", len(competable_keywords))
    if len(competable_keywords) > 0:
        print("   Top 5 机会关键词:")
        for i, row in competable_keywords.head(5).iterrows():
            print(f"   - {row['Keyword']}: 搜索量={row['Search Volume']}, 难度={row['Keyword Difficulty']}, 机会分={row['opportunity_score']}")
    
    print("\n📁 关键词分类统计:")
    for cat in classified_keywords["final_category"].unique():
        count = len(classified_keywords[classified_keywords["final_category"] == cat])
        print(f"   - {cat}: {count} 个关键词")
    
    print("\n🧠 搜索意图分布:")
    for intent, count in core_insights["intent_distribution"].items():
        print(f"   - {intent}: {count}")
    
    print("\n💪 难度分布:")
    for level, count in core_insights["difficulty_distribution"].items():
        print(f"   - {level}: {count}")


# ==================== 主程序 ====================
def main():
    print("🚀 开始竞对关键词分析...")
    print("="*60)
    
    # 1. 加载数据
    print("\n📂 加载数据...")
    dataframes = load_all_data()
    
    if not dataframes:
        print("❌ 未找到任何数据文件")
        return
    
    # 2. 合并数据
    print("\n🔗 合并数据...")
    combined_df = combine_data(dataframes)
    print(f"   总记录数：{len(combined_df)}")
    
    # 3. 找可竞争关键词
    print("\n🎯 分析可竞争关键词...")
    competable_keywords = find_competable_keywords(combined_df)
    
    # 4. 关键词分类
    print("\n📁 关键词分类...")
    classified_keywords = classify_keywords(combined_df)
    category_summary = get_category_summary(classified_keywords)
    
    # 5. 提取核心洞察
    print("\n🧠 提取核心洞察...")
    core_insights = extract_core_insights(combined_df)
    
    # 6. 保存结果
    print("\n💾 保存结果...")
    save_results(competable_keywords, classified_keywords, core_insights, category_summary)
    
    # 7. 打印摘要
    print_summary(competable_keywords, classified_keywords, core_insights)
    
    print("\n✅ 分析完成!")


if __name__ == "__main__":
    main()

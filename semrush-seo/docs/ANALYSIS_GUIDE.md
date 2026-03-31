# 分析指南

## 快速开始

```bash
# 一键运行完整流程
python scripts/run_all.py

# 或分步运行
python scripts/generate_ai_reference.py    # Step 1: 处理关键词数据
python scripts/generate_blog_topics.py     # Step 2: 生成博客选题
```

---

## 工具关系

```
data/ (原始竞对数据)
  │
  ▼
generate_ai_reference.py
  │
  ├──→ output/analysis_results/ai_ref_blog_keywords.csv
  ├──→ output/analysis_results/ai_ref_product_keywords.csv
  ├──→ output/analysis_results/ai_ref_page_keywords.csv
  ├──→ output/analysis_results/ai_ref_competable_keywords.csv
  └──→ output/analysis_results/seo_insights_*.md
         │
         ▼
generate_blog_topics.py
  │
  ├──→ output/blog_topics/blog_topic_matrix_*.csv
  ├──→ output/blog_topics/blog_suggestions_*.json
  └──→ output/blog_topics/blog_topic_report_*.md
```

---

## 项目结构

```
semrush-seo-analyst/
├── data/              # 原始竞对数据（输入）
├── scripts/           # Python 脚本
├── output/            # 所有输出文件
│   ├── analysis_results/
│   └── blog_topics/
└── docs/              # 文档
    ├── ANALYSIS_GUIDE.md
    └── blog_topic_generator.md
```

---

## 输出文件说明

### output/analysis_results/

| 文件 | 列数 | 说明 |
|------|------|------|
| `ai_ref_blog_keywords.csv` | 8 | 博客关键词数据 |
| `ai_ref_product_keywords.csv` | 8 | 产品关键词数据 |
| `ai_ref_page_keywords.csv` | 8 | 页面关键词数据 |
| `ai_ref_competable_keywords.csv` | 9 | 可竞争关键词（含机会分数） |
| `seo_insights_*.md` | - | SEO 洞察报告 |

**CSV 列说明**:
```
Keyword, Search Volume, Keyword Difficulty, Position, Traffic, URL, competitor, category
```

### blog_topics/

| 文件 | 说明 |
|------|------|
| `blog_topic_matrix_*.csv` | 完整选题矩阵（含优先级评分） |
| `blog_suggestions_*.json` | 选题建议（JSON 格式） |
| `blog_topic_report_*.md` | 选题报告（含内容日历） |
| `archived/` | 历史选题存档（自动管理） |

---

## 筛选规则

### 可竞争关键词
- Keyword Difficulty ≤ 40
- Search Volume ≥ 30
- Position ≤ 20

### 低难度高流量机会
- Keyword Difficulty ≤ 25
- Search Volume ≥ 500
- Position ≤ 10

### 优先级评分公式
```
priority = (搜索量 × 排名系数 × (1+流量/100)) / (难度 + 10)

排名系数:
- Position ≤ 3:  1.5
- Position ≤ 10: 1.2
- Position ≤ 20: 1.0
- 其他：0.8
```

---

## 主题分类

| 主题 | 关键词模式 |
|------|-----------|
| steel_types | steel, cr13, vg10, s30v, damascus |
| knife_laws | law, legal, illegal, california |
| knife_types | knife, blade, dagger, karambit |
| maintenance | sharpen, stone, whetstone, clean |
| comparison | vs, versus, compare, better |
| cooking | chef, kitchen, cooking, meat |
| outdoor | tactical, survival, hunting, edc |
| historical | viking, medieval, samurai, katana |

---

## 内容类型识别

| 类型 | 识别模式 |
|------|---------|
| Ultimate Guide | guide, complete, ultimate |
| How-to Tutorial | how to, tutorial, steps |
| Comparison | vs, versus, compare |
| List Post | types, best, top, list |
| Review | review, test, analysis |

---

## 使用建议

1. **新站启动**: 优先选择 `ai_ref_competable_keywords.csv` 中的词
2. **博客规划**: 参考 `blog_topic_report_*.md` 按优先级创作
3. **产品优化**: 使用 `ai_ref_product_keywords.csv` 优化标题/描述
4. **标记已完成**: 在 `blog_topic_matrix_*.csv` 中将 `archive` 列改为 `TRUE`
5. **重新运行**: 标记的选题会被移动到 `archived/` 并自动排除

---

## Archive 机制说明

### CSV 中的 archive 列

`blog_topic_matrix_*.csv` 包含 `archive` 列，默认值为 `0`：

| Keyword | Search Volume | ... | archive |
|---------|---------------|-----|---------|
| seax | 6600 | ... | 0 |
| dagger | 60500 | ... | 0 |

### 如何标记选题

1. **打开 CSV 文件** - `output/blog_topics/blog_topic_matrix_*.csv`
2. **标记已完成** - 将写过的选题 `archive` 改为 `1`
3. **标记不需要** - 将不想要的选题 `archive` 改为 `1`
4. **重新运行脚本** - `python scripts/run_all.py`
5. **自动合并** - 标记的选题会被保存到 `archived/all_archived_keywords.csv`

### 存档目录结构

```
output/blog_topics/archived/
├── all_archived_keywords.csv    ← 所有已存档选题（合并）
└── all_archived_keywords.json   ← JSON 格式
```

### 存档文件格式

| Keyword | Search Volume | ... | archive | archived_at |
|---------|---------------|-----|---------|-------------|
| seax | 6600 | ... | 1 | 20260331_142810 |
| dagger | 60500 | ... | 1 | 20260331_142810 |
| big knife | 3600 | ... | 1 | 20260331_142810 |

- `archived_at`: 存档时间戳
- 自动去重，保留最新数据
- 按优先级分数排序

## 数据更新流程

1. 从 Semrush 导出新的竞对数据
2. 替换 `data/` 目录中的旧文件
3. 运行 `python scripts/run_all.py`
4. 查看新生成的报告

---

## 依赖

```bash
pip install pandas openpyxl
```

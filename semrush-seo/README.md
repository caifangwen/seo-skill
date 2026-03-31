# SEO 关键词分析工具集

## 📋 工具关系图

```
原始数据 (data/)
     │
     ▼
┌─────────────────────────────────────────────────┐
│  Step 1: generate_ai_reference.py              │
│  - 加载 6 个竞对原始数据                         │
│  - 清洗、分类 (blog/product/page)               │
│  - 输出简化 CSV + MD 洞察报告                    │
└─────────────────────────────────────────────────┘
     │
     └───► output/analysis_results/ai_ref_blog_keywords.csv
           │
           ▼
     ┌─────────────────────────────────────────────┐
     │  Step 2: generate_blog_topics.py           │
     │  - 读取博客关键词                           │
     │  - 排除已存档选题                           │
     │  - 生成选题矩阵 + 优先级排序                 │
     └─────────────────────────────────────────────┘
           │
           └───► output/blog_topics/
```

---

## 🛠️ 脚本说明

### Step 1: `generate_ai_reference.py` - 关键词数据处理

**功能**: 原始数据 → 简化分类数据

**输入**: `data/*.csv` 和 `data/*.xlsx` (6 个竞对数据)

**输出**:
| 文件 | 说明 |
|------|------|
| `output/analysis_results/ai_ref_blog_keywords.csv` | 博客关键词 (15,548 条) |
| `output/analysis_results/ai_ref_product_keywords.csv` | 产品关键词 (1,210 条) |
| `output/analysis_results/ai_ref_page_keywords.csv` | 页面关键词 (167 条) |
| `output/analysis_results/ai_ref_competable_keywords.csv` | 可竞争关键词 (6,980 条) |
| `output/analysis_results/seo_insights_*.md` | SEO 洞察报告 |

**运行**:
```bash
python scripts/generate_ai_reference.py
```

---

### Step 2: `generate_blog_topics.py` - 博客选题生成

**功能**: 博客关键词 → 选题建议

**输入**: `output/analysis_results/ai_ref_blog_keywords.csv`

**输出**:
| 文件 | 说明 |
|------|------|
| `output/blog_topics/blog_topic_matrix_*.csv` | 完整选题矩阵 |
| `output/blog_topics/blog_suggestions_*.json` | 选题建议 (JSON 格式) |
| `output/blog_topics/blog_topic_report_*.md` | 选题报告 |

**特性**:
- 自动存档旧选题到 `output/blog_topics/archived/`
- 排除已选题，避免重复
- 按优先级排序

**运行**:
```bash
python scripts/generate_blog_topics.py
```

---

## 🚀 一键运行（推荐）

### Windows
```batch
cd scripts
python run_all.py
```

### Linux/Mac
```bash
cd scripts
python run_all.py
```

---

## 📚 文档

| 文档 | 说明 |
|------|------|
| `docs/ANALYSIS_GUIDE.md` | 分析指南 - 工具使用、筛选规则、主题分类 |
| `docs/blog_topic_generator.md` | 选题生成器 - Skill 详细描述、输出格式、使用示例 |

---

## 📁 项目结构

```
semrush-seo-analyst/
├── README.md                    # 主文档（工具关系说明）
├── data/                        # 原始竞对数据（输入）
├── scripts/                     # Python 脚本
│   ├── run_all.py              # 一键运行（推荐）
│   ├── generate_ai_reference.py # Step 1: 关键词处理
│   └── generate_blog_topics.py  # Step 2: 选题生成
├── output/                      # 所有输出文件
│   ├── analysis_results/       # 关键词数据
│   └── blog_topics/            # 博客选题
│       └── archived/           # 历史选题存档
└── docs/                        # 文档
    ├── ANALYSIS_GUIDE.md        # 分析指南
    └── blog_topic_generator.md  # 选题生成器 Skill 描述
```

---

## 📊 输出文件说明

### output/analysis_results/
```
ai_ref_blog_keywords.csv       # 博客关键词（完整数据）
ai_ref_product_keywords.csv    # 产品关键词
ai_ref_page_keywords.csv       # 页面关键词
ai_ref_competable_keywords.csv # 低难度高流量机会词
seo_insights_YYYYMMDD_HHMMSS.md # SEO 洞察报告
```

### output/blog_topics/
```
blog_topic_matrix_YYYYMMDD_HHMMSS.csv  # 选题矩阵
blog_suggestions_YYYYMMDD_HHMMSS.json  # 选题建议
blog_topic_report_YYYYMMDD_HHMMSS.md   # 选题报告
archived/                              # 历史选题存档
```

---

## ⚙️ 配置说明

### generate_ai_reference.py
```python
# 筛选条件
CORE_COLUMNS = ["Keyword", "Search Volume", "Keyword Difficulty", 
                "Position", "Traffic", "URL", "competitor", "category"]

# 可竞争词筛选
Keyword Difficulty <= 40
Search Volume >= 30
Position <= 20
```

### generate_blog_topics.py
```python
# 主题分类
TOPIC_PATTERNS = {
    "steel_types": [...],
    "knife_laws": [...],
    ...
}

# 优先级公式
priority = (搜索量 × 排名系数 × (1+流量/100)) / (难度 + 10)
```

---

## 📈 工作流程

1. **获取竞对数据** → 放入 `data/` 目录
2. **运行 Step 1** → 生成简化分类数据
3. **运行 Step 2** → 生成博客选题
4. **查看报告** → `blog_topics/blog_topic_report_*.md`
5. **内容创作** → 按优先级选择选题

---

## 🔧 依赖

```bash
pip install pandas openpyxl
```

---

## ❓ 常见问题

### Q: 如何更新数据？
A: 将新的 Semrush 导出文件放入 `data/`，覆盖旧文件，重新运行两个脚本。

### Q: 如何避免选题重复？
A: `generate_blog_topics.py` 会自动读取 `blog_topics/archived/` 中的历史选题并排除。

### Q: 如何调整筛选条件？
A: 编辑对应脚本的配置区域，修改阈值后重新运行。

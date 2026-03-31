# 法兰阀门管件博客文章写作流程

**版本**: 1.0 | **更新**: 2026-03

本文档提供从零开始撰写一篇完整博客文章的**分步骤执行指南**。

---

## 📋 完整流程概览

```
阶段 1: 准备 → ① 确定主题 → ② 关键词调研 → ③ 竞对分析
                    ↓
阶段 2: 规划 → ④ 确认文章类型 → ⑤ 获取技能组合 → ⑥ 准备图片资源
                    ↓
阶段 3: 写作 → ⑦ Front Matter → ⑧ 开篇引言 → ⑨ 正文模块 → ⑩ 结论 CTA
                    ↓
阶段 4: 优化 → ⑪ 植入内部链接 → ⑫ 插入图片 → ⑬ SEO 检查
                    ↓
阶段 5: 发布 → ⑭ 完整检查 → ⑮ 发布上线
```

---

## 阶段 1: 准备阶段

### 步骤 ① 确定文章主题

**输入**: 产品目录、客户需求、行业热点

**操作**:
1. 从以下类别中选择主题：
   - **法兰**: 类型、压力等级、材质、标准解读
   - **阀门**: 球阀、闸阀、截止阀、蝶阀、选型指南
   - **管件**: 弯头、三通、异径管、连接方式
   - **管道**: 无缝钢管、焊接钢管、材质对比

2. 确认文章角度：
   - 产品详解（单一产品深度介绍）
   - 对比分析（A vs B）
   - 选型指南（如何选择合适的 X）
   - 安装教程（如何安装 X）
   - 行业应用（X 在 Y 行业的应用）

**输出**: 明确的文章主题和角度

**示例**:
```
主题：Class 150 vs Class 300 Flanges
角度：对比分析 + 选型指南
目标受众：管道工程师、采购经理
```

---

### 步骤 ② 关键词调研

**读取**: `research/keyword-research.md`

**操作**:
1. 确定核心关键词（1-2 个）
2. 扩展长尾关键词（5-10 个）
3. 分析问题型关键词（3-5 个）
4. 确认商业意图关键词（2-3 个）

**工具**: Google Keyword Planner, Ahrefs, SEMrush

**输出模板**:
```markdown
## 目标关键词报告

**核心关键词**: class 150 vs class 300 flanges
**搜索意图**: 商业调查 + 信息型
**目标受众**: 管道工程师、采购经理

### 主要关键词列表
| 关键词 | 类型 | 难度 | 优先级 |
|-------|------|-----|-------|
| class 150 vs class 300 flanges | 对比 | 中 | P0 |
| flange pressure rating chart | 信息 | 中 | P0 |
| ASME B16.5 flange dimensions | 信息 | 中 | P1 |
```

---

### 步骤 ③ 竞对分析

**读取**: `research/competitor-research.md`

**操作**:
1. 搜索核心关键词，记录前 5 名结果
2. 分析每篇文章：
   - 字数、章节数、图片数
   - 内容结构、优缺点
   - 缺失的主题/信息
3. 找出内容差距（Content Gap）
4. 确定差异化策略

**输出**: 竞对分析报告（见 competitor-research.md 模板）

---

## 阶段 2: 规划阶段

### 步骤 ④ 确认文章类型

**读取**: `workflows/article-types.md`

**操作**: 根据主题选择文章类型

| 你的主题 | 选择类型 |
|---------|---------|
| 单一产品详解 | 类型 1: 产品详解文章 |
| A vs B 对比 | 类型 2: 产品对比文章 |
| 如何安装/选型 | 类型 3: 安装/选型指南 |
| 材料介绍 | 类型 4: 材料介绍文章 |
| 价格/成本分析 | 类型 5: 价格分析文章 |
| 行业知识科普 | 类型 6: 知识科普文章 |
| 行业应用案例 | 类型 7: 行业应用文章 |
| 标准解读 | 类型 8: 标准解读文章 |

---

### 步骤 ⑤ 获取技能组合

根据文章类型，从 `workflows/article-types.md` 获取技能链：

**示例**（对比文章）:
```
技能链：keyword-research → competitor-research → frontmatter → intro 
       → comparison-table → material-specs → material-comparison 
       → conclusion-cta
```

**对应文件**:
```
research/keyword-research.md
research/competitor-research.md
writing/frontmatter.md
writing/intro.md
writing/comparison-table.md
writing/material-specs.md
writing/material-comparison.md
writing/conclusion-cta.md
```

---

### 步骤 ⑥ 准备图片资源

**读取**: `assets/image-guidelines.md`

**操作**:
1. 根据主题确定图片关键词（参考第 3 节表格）
2. 在 Unsplash/Pexels/Pixabay 搜索图片
3. 使用脚本批量下载：

```bash
# 下载 8 张关于法兰的图片
python scripts/download_images.py \
  --query "industrial flanges pipeline" \
  --output output/images/[文章主题]/ \
  --count 8 \
  --size large
```

4. 重命名图片文件（描述性 + 连字符）
5. 上传到 WordPress 媒体库

**输出**: 8-12 张相关图片，存储在 `output/images/[文章主题]/`

---

## 阶段 3: 写作阶段

### 步骤 ⑦ 生成 Front Matter

**读取**: `writing/frontmatter.md`

**操作**: 在文章开头添加 YAML Front Matter

```markdown
---
title: "Class 150 vs Class 300 Flanges: Key Differences Explained"
date: 2026-03-27
categories:
  - "flanges"
coverImage: "class-150-vs-class-300-flanges.jpg"
---
```

**注意**:
- Title 包含核心关键词，50-60 字符
- date 使用当前日期（2026 年）
- categories 选择正确分类

---

### 步骤 ⑧ 撰写开篇引言

**读取**: `writing/intro.md`

**操作**: 写 2-3 段引言

**结构**:
```
第 1 段：主题引入 + 行业地位（2-3 句）
第 2 段：背景信息 + 内部链接（2-3 句）
第 3 段：悬念引导 + 文章预告（1-2 句）
```

**示例**:
```markdown
Among all the pipe components used in industrial piping systems, flanges are 
critical for creating secure, leak-free connections. Class 150 and Class 300 
flanges are the most commonly used pressure ratings in oil and gas, chemical 
processing, and water treatment applications.

Understanding the differences between these two pressure classes is essential 
for engineers and procurement managers. The [pressure rating](link-to-pressure-chart) 
and [material selection](link-to-materials) directly impact system safety and cost.

Wondering which flange class is right for your project? Read on to find out 
the key differences between Class 150 and Class 300 flanges, including pressure 
ratings, dimensions, and ideal applications.
```

---

### 步骤 ⑨ 撰写正文模块

根据技能链中的模块，依次撰写正文：

#### 9.1 对比表格（如适用）

**读取**: `writing/comparison-table.md`

```markdown
## Comparison Table: Class 150 vs Class 300 Flanges

![Flange comparison chart](image-url)

|  | **Class 150** | **Class 300** |
| --- | --- | --- |
| **Pressure Rating** | 285 psi @ 100°F | 740 psi @ 100°F |
| **Wall Thickness** | Standard | Heavier |
| **Weight** | Lighter | ~40% heavier |
| **Cost** | Lower | Higher |
| **Applications** | Low pressure, water, air | Medium pressure, oil, gas |
```

#### 9.2 材料规格详解

**读取**: `writing/material-specs.md`

```markdown
## Material Specifications

### ASTM A105 Carbon Steel

**Chemical Composition**:
- Carbon (C): 0.35% max
- Manganese (Mn): 0.60-1.05%
- ...

**Mechanical Properties**:
- Tensile Strength: 485 MPa min
- Yield Strength: 250 MPa min
- ...
```

#### 9.3 其他模块

按技能链顺序撰写：
- `material-comparison.md` → 材料对比分析
- `pros-cons.md` → 优缺点分析
- `use-cases.md` → 使用场景
- `installation.md` → 安装指南
- `history.md` → 历史背景
- `price-analysis.md` → 价格分析
- `faq.md` → 常见问题

**每节结构**:
```markdown
## [章节标题]

![相关图片](image-url)

[引入句]. [详细说明 2-3 句].

### [子章节]

[内容 3-5 句].

- 要点 1: 说明
- 要点 2: 说明
- 要点 3: 说明
```

---

### 步骤 ⑩ 撰写结论与 CTA

**读取**: `writing/conclusion-cta.md`

**操作**:

#### 10.1 结论总结
```markdown
## Conclusion: Choosing the Right Flange Class

The pressure rating and operating conditions are where flange selection proves 
most critical. For most low-pressure water and air applications, Class 150 
flanges provide adequate performance at the lowest cost.

However, the higher pressure capacity of Class 300 flanges makes them essential 
for oil and gas, chemical processing, and high-temperature steam applications.
```

#### 10.2 CTA 行动号召
```markdown
## Get a Free Quote for Your Piping Project

Looking for certified flange suppliers? Our team supplies ASME B16.5 flanges 
from Class 150 to Class 2500 in carbon steel, stainless steel, and alloy materials.

[Request a Free Quote](https://example.com/request-a-quote/)
```

---

## 阶段 4: 优化阶段

### 步骤 ⑪ 植入内部链接

**读取**: `assets/internal-links.md`

**操作**:
1. 每 300-400 字添加 1 个内部链接
2. 开篇 2 段必须有 1-2 个链接
3. 使用描述性锚文本（非"click here"）

**检查清单**:
```markdown
- [ ] 开篇有 1-2 个内部链接
- [ ] 每节至少 1 个链接
- [ ] 结尾有 /request-a-quote/ 链接
- [ ] 锚文本为描述性关键词
- [ ] 链接到相关产品/知识页面
```

---

### 步骤 ⑫ 插入图片

**读取**: `assets/image-guidelines.md`

**操作**:

#### 方法 1: 手动插入
```markdown
![图片描述](https://img.example.com/wp-content/uploads/2026/03/flange-comparison.jpg)
```

#### 方法 2: 使用脚本自动插入
```bash
python scripts/update_article_images.py \
  --article output/posts/[文章主题]/index.md \
  --images-dir output/images/[文章主题]/ \
  --keyword "industrial flanges" \
  --pattern after-headings
```

**检查清单**:
```markdown
- [ ] 每 500 字至少 1 张图片
- [ ] 每个 H2 章节至少 1 张
- [ ] 图片与内容高度相关
- [ ] Alt 描述包含关键词
- [ ] 图片大小 < 200KB
```

---

### 步骤 ⑬ SEO 检查

**读取**: `qa/seo-checklist.md`

**操作**: 逐项检查

```markdown
## SEO 检查清单

- [ ] 核心关键词在 Title 中
- [ ] 核心关键词在开篇 100 词内
- [ ] 核心关键词在至少 1 个 H2 中
- [ ] 长尾关键词自然分布
- [ ] 图片 Alt 包含关键词
- [ ] Title 长度 50-60 字符
- [ ] 内部链接密度适当
- [ ] FAQ 章节格式规范（可触发精选摘要）
- [ ] 标准号正确引用（ASME/API/ASTM）
```

---

## 阶段 5: 发布阶段

### 步骤 ⑭ 完整检查

**读取**: `qa/publish-checklist.md`

**操作**: 逐项检查

```markdown
## 发布前检查清单

### 内容完整性
- [ ] Front Matter 完整
- [ ] 开篇 2-3 段，含内部链接
- [ ] 每个章节有图片
- [ ] 优缺点平衡分析
- [ ] 结论含 CTA

### 图片验证
- [ ] 所有图片真实存在
- [ ] 图片与内容相关
- [ ] 文件名规范
- [ ] 已上传到正确路径

### 技术准确性
- [ ] 压力等级数据准确
- [ ] 材质标准正确
- [ ] 单位换算正确
- [ ] 无拼写/语法错误

### B2B 元素
- [ ] 目标受众明确
- [ ] OEM/批发服务提及
- [ ] 认证信息展示
```

---

### 步骤 ⑮ 发布上线

**操作**:
1. 在 WordPress 后台创建新文章
2. 粘贴 Markdown 内容（或导入文件）
3. 设置 Featured Image（coverImage）
4. 设置 Categories/Tags
5. 设置 SEO Title/Meta Description
6. 预览检查
7. 发布

**发布后**:
- 提交 Google Search Console
- 分享到社交媒体
- 添加到相关内部链接页面

---

## 📎 快速参考卡

### 文章结构模板

```markdown
---
title: "文章标题"
date: 2026-03-27
categories: ["分类"]
---

[开篇引言 2-3 段，含内部链接]

## [主要章节 1]
[内容 + 图片]

## [主要章节 2]
[内容 + 图片]

## [对比表格/规格表]
[表格]

## [优缺点/应用场景]
[列表]

## FAQ
### 问题 1？
回答

### 问题 2？
回答

## Conclusion
[总结 + CTA]
```

### 常用链接

| 页面 | 路径 |
|-----|------|
| 询价页面 | `/request-a-quote/` |
| 法兰分类 | `/flanges/` |
| 阀门分类 | `/valves/` |
| 管件分类 | `/pipe-fittings/` |

### 图片密度

```
每 500 字 = 1 张图片
每 H2 章节 = 至少 1 张
开篇后第 1 节 = 必须有图
对比表格前后 = 各 1 张
```

---

**下一步**: 开始步骤 ①，确定你的文章主题！

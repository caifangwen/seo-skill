---
name: steel-keyword-research
version: "1.0.0"
description: |
  钢铁外贸 B2B 关键词研究专用 Skill
  触发场景：
  - 用户需要挖掘钢铁产品关键词（如"rebar keywords", "HRC 关键词研究"）
  - 分析买家国家搜索意图（如"中东客户搜索习惯", "东南亚钢铁关键词"）
  - 竞品关键词分析（如"分析印度钢厂关键词", "Baosteel 关键词策略"）
  - 产品规格词提取（如"ASTM A615 rebar specs", "SS400 steel plate keywords"）
  - 长尾词挖掘（如"steel pipe price per ton", "galvanized coil supplier China"）
compatibility:
  tools: [web_search, web_fetch, bash]
---

# Steel Keyword Research

## 概述

专为钢铁外贸 B2B 业务设计的关键词研究 Skill。基于**Triad 模型**（产品类型 + 规格标准 + 使用场景）挖掘高转化意图关键词，聚焦中东、东南亚、非洲、南美等核心买家市场，帮助从产品规格关键词到买家询盘的完整转化链路。

## 核心逻辑

> **"从产品规格关键词到买家询盘"**

所有关键词研究都围绕这一核心链条展开，流量本身无意义，询盘转化是唯一目标。

## 前置条件

开始前必须获取的信息：
- [ ] **目标产品**：具体钢铁产品类型（如 Rebar, HRC, CRC, Galvanized Coil, Steel Pipe 等）
- [ ] **目标市场**：买家国家/地区（如 Saudi Arabia, Vietnam, Nigeria 等）
- [ ] **产品类型**：长材/板材/管材/型材分类
- [ ] **可选信息**：竞品网站、现有关键词列表、目标客户类型（进口商/分销商/终端用户）

如信息不完整，必须先向用户询问，不得跳过。

## 核心工作流

### 步骤 1：产品分类与 Triad 模型构建

根据用户提供的产品，构建完整的 Triad 模型：

**Triad 模型 = [Product Type] + [Spec/Standard] + [Usage/Scenario]**

| 维度 | 示例 |
|------|------|
| Product Type | Rebar, Wire Rod, HRC, CRC, PPGI, Seamless Pipe |
| Spec/Standard | ASTM A615 Gr40/60, SS400, Q235B, SPHC, DX51D |
| Usage/Scenario | construction, infrastructure, automotive, roofing |

**关键点：**
- 产品规格是钢铁外贸关键词的核心，必须精确到标准号和等级
- 不同买家市场对规格标准偏好不同（中东偏好 SASO/ASTM，东南亚偏好 JIS/GB）
- 使用场景词决定搜索意图的商业价值

### 步骤 2：搜索意图分类与优先级

根据钢铁外贸 B2B 特点，对关键词进行意图分类：

| 意图类型 | 优先级 | 示例关键词 | 特征 |
|----------|--------|------------|------|
| Transactional | ⭐⭐⭐⭐⭐ | "buy rebar Saudi Arabia", "steel pipe supplier China", "HRC price per ton" | 包含 buy/supplier/price/manufacturer |
| Commercial | ⭐⭐⭐⭐ | "steel coil manufacturers", "galvanized sheet specifications", "seamless pipe grades" | 产品 + 商业属性词 |
| Specification | ⭐⭐⭐ | "ASTM A615 rebar specs", "SS400 equivalent", "DX51D zinc coating" | 规格/标准/等价查询 |
| Informational | ⭐⭐ | "what is rebar", "steel grades explained", "how to choose steel pipe" | 知识性查询，转化率低 |

**输出要求：**
- 优先挖掘 Transactional 和 Commercial 意图关键词
- Specification 词用于内容优化和内部链接
- Informational 词仅用于博客/指南内容

### 步骤 3：买家国家特定规则应用

根据不同买家市场特点调整关键词策略：

#### 中东市场（Middle East）
- **核心国家**：Saudi Arabia, UAE, Qatar, Kuwait
- **标准偏好**：SASO, ASTM, BS
- **语言特点**：英语 + 阿拉伯语混合搜索
- **热门产品**：Rebar（Vision 2030 基建）, Steel Pipe（油气项目）
- **关键词示例**：
  - "rebar price Saudi Arabia SASO"
  - "steel pipe supplier Dubai"
  - "ASTM A615 rebar Qatar"

#### 东南亚市场（Southeast Asia）
- **核心国家**：Vietnam, Philippines, Indonesia, Thailand
- **标准偏好**：JIS, GB, TIS
- **语言特点**：本地语言 + 英语（如越南语"thép xây dựng"）
- **热门产品**：HRC/CRC（制造业）, Rebar（基建）
- **关键词示例**：
  - "thép cuộn nóng Việt Nam" (Vietnamese)
  - "HRC price Philippines"
  - "steel plate supplier Thailand"

#### 非洲市场（Africa）
- **核心国家**：Nigeria, Kenya, Ethiopia, Ghana
- **标准偏好**：BS, ASTM, 价格敏感
- **语言特点**：英语/法语
- **热门产品**：Rebar（基建）, Galvanized Coil（建筑）
- **关键词示例**：
  - "cheap rebar Nigeria"
  - "galvanized iron sheet price Kenya"
  - "steel supplier Lagos"

#### 南美市场（South America）
- **核心国家**：Brazil, Chile, Peru, Colombia
- **标准偏好**：ASTM, ABNT (Brazil)
- **语言特点**：西班牙语/葡萄牙语
- **热门产品**：Wire Rod, HRC, Steel Plate
- **关键词示例**：
  - "alambrón precio Chile"
  - "chapa de aço Brasil"
  - "steel plate supplier Peru"

### 步骤 4：竞品关键词分析

分析主要竞争对手的关键词策略：

**核心竞品：**
- 印度钢厂：SAIL, Tata Steel, JSW Steel
- 韩国钢厂：POSCO, Hyundai Steel
- 中国钢厂：Baosteel, Ansteel, HBIS
- 土耳其钢厂：Ereğli, İÇDAŞ

**分析方法：**
1. 使用 `web_search` 搜索竞品网站 + 产品词
2. 分析竞品页面 Title/Meta/Heading 中的关键词
3. 识别竞品覆盖但用户未覆盖的规格词
4. 找出竞品未覆盖的长尾机会词

### 步骤 5：关键词矩阵输出

生成完整的关键词研究报告，包含以下维度：

| 维度 | 内容 |
|------|------|
| 核心词 | 产品类型 + 标准词（10-20 个） |
| 长尾词 | 产品 + 规格 + 用途 + 国家（30-50 个） |
| 国家优先级 | 按市场潜力排序的目标国家 |
| 规格词 | 必须覆盖的标准号和等级 |
| 竞品差距 | 竞品覆盖但用户未覆盖的词 |
| 落地页分配 | 每个关键词组对应的页面类型 |

### 步骤 6：输出结果

输出格式：

```markdown
# Steel Keyword Research Report: [Product Name]

## Executive Summary
- 核心产品：[Product]
- 目标市场：[Countries]
- 关键词总数：[Count]
- 高转化词占比：[Percentage]

## Keyword Matrix

### Transactional Keywords (⭐⭐⭐⭐⭐)
| Keyword | Volume | Intent | Priority | Landing Page |
|---------|--------|--------|----------|--------------|
| | | | | |

### Commercial Keywords (⭐⭐⭐⭐)
| Keyword | Volume | Intent | Priority | Landing Page |
|---------|--------|--------|----------|--------------|
| | | | | |

### Specification Keywords (⭐⭐⭐)
| Keyword | Volume | Intent | Priority | Landing Page |
|---------|--------|--------|----------|--------------|
| | | | | |

## Country-Specific Priorities

### [Country 1]
- Top Keywords: [...]
- Standard Preference: [...]
- Content Gap: [...]

### [Country 2]
- Top Keywords: [...]
- Standard Preference: [...]
- Content Gap: [...]

## Spec Terms Coverage
- Must-have Standards: [ASTM, JIS, GB, EN, etc.]
- Grade Equivalents: [Mapping table]
- Missing Specs: [Gap analysis]

## Competitor Gap Analysis
| Competitor | Covered Keywords | Our Gap | Opportunity |
|------------|------------------|---------|-------------|
| | | | |

## Recommended Actions
1. [Action 1]
2. [Action 2]
3. [Action 3]
```

## 输出规范

- 关键词必须包含 Triad 模型的完整维度
- 必须标注每个关键词的意图类型和优先级
- 必须提供国家特定的关键词变体
- 必须包含竞品差距分析
- 必须提供落地页分配建议
- 所有规格词必须精确到标准号和等级

## 错误处理

- **产品信息不完整** → 必须先询问用户具体产品类型、规格、目标市场
- **无法获取搜索量数据** → 使用定性分析（高/中/低）替代具体数字
- **竞品网站无法访问** → 使用 web_search 结果中的 snippet 分析
- **小语种关键词不确定** → 标注需要本地化验证

## 注意事项

- 钢铁外贸关键词的核心是规格，不是泛泛的产品词
- 买家国家决定搜索意图和标准偏好，必须针对性分析
- 询盘转化是唯一目标，优先 Transactional 和 Commercial 意图
- 竞品分析聚焦印度、土耳其、韩国钢厂，找出差异化机会
- 关键词研究结果必须可执行，直接指导落地页优化

## 参考文档

- `references/product-specs-taxonomy.md` - 钢铁产品分类与规格体系
- `references/buyer-country-intent.md` - 买家国家搜索意图地图
- `references/competitor-domains.md` - 竞品网站列表

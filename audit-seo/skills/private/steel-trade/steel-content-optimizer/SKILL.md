---
name: steel-content-optimizer
version: "1.0.0"
description: |
  钢铁外贸 B2B 产品页面 SEO 优化专用 Skill
  触发场景：
  - 用户需要优化钢铁产品页面（如"optimize rebar product page", "HRC 页面 SEO"）
  - 撰写产品描述和规格表（如"write steel product description", "规格表优化"）
  - 优化 Title Tag 和 Meta Description（如"改写 title tag", "meta description 优化"）
  - 生成产品 FAQ（如"generate FAQ for steel pipe", "产品常见问题"）
  - 询盘转化优化（如"improve inquiry conversion", "RFQ 表单优化"）
  - 15 点诊断检查（如"audit product page", "页面诊断"）
compatibility:
  tools: [web_search, web_fetch, bash]
---

# Steel Content Optimizer

## 概述

专为钢铁外贸 B2B 产品页面设计的 SEO 优化 Skill。基于**15 点诊断框架**（12 个通用 SEO 点 + 3 个钢铁行业特殊点），聚焦规格表完整性和询盘转化路径优化，帮助将产品页面流量转化为实际买家询盘。

## 核心逻辑

> **"规格表结构 + 询盘转化诊断 = B2B 产品页面 SEO"**

## 前置条件

开始前必须获取的信息：
- [ ] **目标页面 URL** 或 **产品类型**（如 Rebar, HRC, Steel Pipe）
- [ ] **目标市场**：买家国家/地区（如 Saudi Arabia, Vietnam）
- [ ] **当前页面内容**（如有 URL 则抓取，如无则用户提供）
- [ ] **可选信息**：目标关键词、竞品页面、现有关键词排名

如信息不完整，必须先向用户询问，不得跳过。

## 核心工作流

### 步骤 1:15 点诊断检查

对钢铁产品页面进行完整的 15 点诊断：

#### 通用 SEO 检查点 (1-12)

| # | 检查项 | 检查内容 | 钢铁行业特殊要求 |
|---|--------|----------|------------------|
| 1 | Title Tag | 长度 50-60 字符，包含核心关键词 | 必须包含产品 + 规格范围 + 标准 |
| 2 | Meta Description | 长度 150-160 字符，包含 CTA | 必须包含 MOQ、交期、认证 |
| 3 | H1 Heading | 唯一 H1，包含核心关键词 | 产品全称 + 核心规格 |
| 4 | H2/H3 Structure | 逻辑清晰，覆盖主要话题 | 规格、应用、认证、FAQ |
| 5 | Keyword Density | 核心词密度 1-3% | 规格词自然分布 |
| 6 | Internal Links | 链接到相关产品/分类页 | 规格对比页、应用案例页 |
| 7 | Image Alt Tags | 所有图片有描述性 alt | 包含产品名 + 规格 |
| 8 | URL Structure | 简洁、包含关键词 | /product/rebar-astm-a615/ |
| 9 | Mobile Friendliness | 移动端显示正常 | 询盘按钮可见 |
| 10 | Page Speed | 加载时间<3 秒 | 规格表不拖慢加载 |
| 11 | Schema Markup | Product/Organization 标记 | 必须包含规格属性 |
| 12 | Content Length | 产品页≥800 词 | 规格表 + FAQ 不计入 |

#### 钢铁行业特殊检查点 (13-15)

| # | 检查项 | 检查内容 | 重要性 |
|---|--------|----------|--------|
| 13 | **规格表完整性** | 包含完整技术参数、公差范围、等价等级对照 | ⭐⭐⭐⭐⭐ |
| 14 | **询盘路径诊断** | RFQ 表单可见性、WhatsApp/WeChat 按钮、响应时间承诺 | ⭐⭐⭐⭐⭐ (最关键) |
| 15 | **B2B 信任元素** | ISO/CE 认证、Mill Certificate 样本、工厂图片、项目案例 | ⭐⭐⭐⭐ |

### 步骤 2:Title Tag 优化

**钢铁产品 Title Tag 公式**：

```
[Product] [Spec Range] - [Standard/Grade] | [Company/China Factory]
```

**示例**：
```
Rebar ASTM A615 Gr40/60 10-50mm - Deformed Steel Bar | [Company Name]
HRC Hot Rolled Coil SPHC SS400 1.5-25mm | China Steel Factory
Seamless Pipe ASTM A106 Gr.B 1/2"-48" - SMLS Steel Tube Supplier
```

**优化要点**：
- 核心关键词前置（产品名 + 规格）
- 包含标准号和等级（ASTM A615 Gr40/60）
- 规格范围用数字表示（10-50mm, 1.5-25mm）
- 结尾加公司名或"China Factory/Supplier"
- 长度控制在 50-60 字符

### 步骤 3:Meta Description 优化

**钢铁产品 Meta Description 公式**：

```
[Product] [Core Spec] for [Application]. [Certifications]. MOQ [Quantity], [Lead Time] delivery. [CTA with urgency].
```

**示例**：
```
ASTM A615 Gr40/60 Rebar 10-50mm for construction & infrastructure. 
ISO9001, CE, Mill Certificate. MOQ 25MT, 15-20 days delivery. 
Get best price - Contact us now for fast quote!
```

**必须包含元素**：
- **MOQ**：最小起订量（如 25MT, 100MT）
- **时效性 CTA**：Get best price, Fast quote, Contact now
- **认证**：ISO9001, CE, Mill Certificate, SASO (针对中东)

### 步骤 4:规格表 HTML 优化

**钢铁产品规格表标准 HTML 结构**：

```html
<table class="spec-table">
  <thead>
    <tr>
      <th>Specification</th>
      <th>Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Product Name</td>
      <td>Deformed Steel Bar (Rebar)</td>
    </tr>
    <tr>
      <td>Standard</td>
      <td>ASTM A615 Gr40/60</td>
    </tr>
    <tr>
      <td>Grade</td>
      <td>Grade 40 (280MPa), Grade 60 (420MPa)</td>
    </tr>
    <tr>
      <td>Diameter</td>
      <td>10mm, 12mm, 16mm, 20mm, 25mm, 32mm, 40mm, 50mm</td>
    </tr>
    <tr>
      <td>Length</td>
      <td>6m, 9m, 12m or as per requirement</td>
    </tr>
    <tr>
      <td>Yield Strength</td>
      <td>Gr40: ≥280MPa, Gr60: ≥420MPa</td>
    </tr>
    <tr>
      <td>Tensile Strength</td>
      <td>Gr40: ≥420MPa, Gr60: ≥620MPa</td>
    </tr>
    <tr>
      <td>Elongation</td>
      <td>≥12%</td>
    </tr>
    <tr>
      <td>Surface</td>
      <td>Ribbed/Deformed for better bonding</td>
    </tr>
    <tr>
      <td>Certification</td>
      <td>ISO9001, CE, Mill Test Certificate</td>
    </tr>
    <tr>
      <td>MOQ</td>
      <td>25MT</td>
    </tr>
    <tr>
      <td>Delivery Time</td>
      <td>15-20 days after deposit</td>
    </tr>
  </tbody>
</table>
```

**等级等价对照表**（必须包含）：

```html
<h3>Grade Equivalents</h3>
<table class="equivalent-table">
  <thead>
    <tr>
      <th>Standard</th>
      <th>Grade</th>
      <th>Yield Strength</th>
      <th>Tensile Strength</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>ASTM A615 (USA)</td>
      <td>Gr40</td>
      <td>280 MPa</td>
      <td>420 MPa</td>
    </tr>
    <tr>
      <td>ASTM A615 (USA)</td>
      <td>Gr60</td>
      <td>420 MPa</td>
      <td>620 MPa</td>
    </tr>
    <tr>
      <td>BS4449 (UK)</td>
      <td>Gr460</td>
      <td>460 MPa</td>
      <td>550 MPa</td>
    </tr>
    <tr>
      <td>GB/T 1499 (China)</td>
      <td>HRB400</td>
      <td>400 MPa</td>
      <td>540 MPa</td>
    </tr>
    <tr>
      <td>GB/T 1499 (China)</td>
      <td>HRB500</td>
      <td>500 MPa</td>
      <td>630 MPa</td>
    </tr>
    <tr>
      <td>JIS G3112 (Japan)</td>
      <td>SD390</td>
      <td>390 MPa</td>
      <td>540 MPa</td>
    </tr>
  </tbody>
</table>
```

### 步骤 5:FAQ 生成

**钢铁产品页面必备的 6 类 FAQ**：

#### 1. 价格相关 (Price)
```
Q: What is the price of [Product]?
A: Price varies based on specification, quantity, and market conditions. 
   Please contact us with your requirements for the latest quotation. 
   We offer competitive factory-direct pricing with [lead time] delivery.
```

#### 2. 规格相关 (Specification)
```
Q: What specifications do you supply?
A: We supply [Product] in [spec range]. Common specifications include 
   [list 3-5 popular specs]. Custom specifications are available upon request.
```

#### 3. 订单相关 (Order)
```
Q: What is the minimum order quantity (MOQ)?
A: Our MOQ is [quantity, e.g., 25MT] for [Product]. For trial orders, 
   we may accept smaller quantities. Please contact us for details.
```

#### 4. 认证相关 (Certification)
```
Q: What certifications do you have?
A: Our [Product] is certified with ISO9001, CE, and Mill Test Certificate. 
   For specific markets (e.g., Saudi Arabia), we can provide SASO certification.
```

#### 5. 交货相关 (Delivery)
```
Q: What is the delivery time?
A: Standard delivery time is [15-20] days after receiving deposit. 
   For urgent orders, please contact us for expedited production options.
```

#### 6. 对比相关 (Comparison)
```
Q: What is the difference between [Grade A] and [Grade B]?
A: [Grade A] has [yield strength] yield strength, while [Grade B] has 
   [yield strength]. [Grade A] is suitable for [application], 
   while [Grade B] is used for [application].
```

**FAQ Schema 标记**：
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is the minimum order quantity?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Our MOQ is 25MT for standard specifications."
      }
    }
  ]
}
</script>
```

### 步骤 6:内部链接优化

**钢铁产品页面内部链接策略**：

| 链接类型 | 目标页面 | 锚文本示例 |
|----------|----------|------------|
| 规格对比 | /comparison/rebar-grades/ | "Compare ASTM A615 Gr40 vs Gr60" |
| 应用案例 | /applications/construction-rebar/ | "Rebar for construction projects" |
| 认证页面 | /certifications/iso-ce/ | "View our ISO and CE certificates" |
| 相关产品 | /product/wire-rod/ | "Related: Wire Rod for drawing" |
| 价格页面 | /price/rebar-price-today/ | "Today's rebar price" |

### 步骤 7:询盘转化优化

**询盘路径诊断清单**：

| 检查项 | 要求 | 状态 |
|--------|------|------|
| RFQ 表单位置 | 首屏可见或 1 次滚动内 | ☐ |
| RFQ 表单字段 | ≤5 个必填字段（姓名、邮箱、产品、规格、数量） | ☐ |
| WhatsApp 按钮 | 页面右下角悬浮，响应时间承诺 | ☐ |
| WeChat 二维码 | 针对中国买家，可扫码添加 | ☐ |
| 响应时间承诺 | "Reply within 2 hours" 或类似承诺 | ☐ |
| 信任元素 | ISO/CE 认证图标、Mill Certificate 样本 | ☐ |
| 工厂图片 | 真实工厂/仓库照片（非图库） | ☐ |
| 项目案例 | 已供货项目列表或图片 | ☐ |

**询盘表单最佳实践**：
```html
<form action="/rfq" method="POST">
  <h3>Request a Quote</h3>
  <p>Get best price within 2 hours</p>
  
  <input type="text" name="name" placeholder="Your Name *" required>
  <input type="email" name="email" placeholder="Your Email *" required>
  <input type="text" name="product" placeholder="Product (e.g., Rebar)" required>
  <input type="text" name="specification" placeholder="Specification (e.g., ASTM A615 Gr60)" required>
  <input type="text" name="quantity" placeholder="Quantity (MT)" required>
  <input type="tel" name="phone" placeholder="Phone/WhatsApp (optional)">
  <textarea name="message" placeholder="Additional requirements..."></textarea>
  
  <button type="submit">Get Best Price</button>
  <p class="trust-text">We respect your privacy. No spam.</p>
</form>
```

### 步骤 8:输出结果

输出格式：

```markdown
# Steel Product Page Optimization Report

## Page URL
[URL]

## Overall Score
[Score]/100

## 15-Point Diagnosis

### Critical Issues (P0)
| # | Issue | Impact | Recommendation |
|---|-------|--------|----------------|
| 14 | No visible RFQ form | High | Add inquiry form above the fold |
| 13 | Specification table incomplete | High | Add complete spec with tolerances |

### Important Issues (P1)
| # | Issue | Impact | Recommendation |
|---|-------|--------|----------------|
| 1 | Title tag too short | Medium | Expand to include spec range |
| 2 | Meta description missing CTA | Medium | Add MOQ and lead time |

### Suggestions (P2)
| # | Issue | Impact | Recommendation |
|---|-------|--------|----------------|
| 6 | Limited internal links | Low | Add links to spec comparison page |

## Optimized Elements

### Title Tag (Before/After)
**Before:** [Original title]
**After:** [Optimized title]

### Meta Description (Before/After)
**Before:** [Original or "Missing"]
**After:** [Optimized description]

### Specification Table
[Complete HTML table with all specs]

### Grade Equivalents
[Equivalents table for GB/ASTM/EN/JIS]

### FAQ (6 Questions Minimum)
1. **Q:** [Price question]
   **A:** [Answer]

2. **Q:** [Specification question]
   **A:** [Answer]

3. **Q:** [Order question]
   **A:** [Answer]

4. **Q:** [Certification question]
   **A:** [Answer]

5. **Q:** [Delivery question]
   **A:** [Answer]

6. **Q:** [Comparison question]
   **A:** [Answer]

## Internal Linking Recommendations
- Link to: [Page] with anchor "[Anchor text]"
- Link to: [Page] with anchor "[Anchor text]"

## Inquiry Conversion Improvements
1. [Specific improvement 1]
2. [Specific improvement 2]
3. [Specific improvement 3]

## Implementation Priority
1. **P0 (Critical)**: Fix immediately
2. **P1 (Important)**: Fix within 1 week
3. **P2 (Suggestions)**: Fix within 1 month
```

## 输出规范

- 15 点诊断必须完整，不得跳过任何检查点
- Title/Meta 必须提供优化前后对比
- 规格表必须包含完整 HTML 代码
- FAQ 必须包含至少 6 个问题（价格、规格、订单、认证、交货、对比）
- 必须提供内部链接建议
- 必须提供询盘转化改进建议
- 所有建议必须按优先级排序（P0/P1/P2）

## 错误处理

- **页面无法访问** → 要求用户提供页面内容或截图
- **产品信息不完整** → 必须先询问用户具体产品、规格、目标市场
- **无法确定规格参数** → 参考 `references/product-specs-taxonomy.md`
- **竞品页面无法访问** → 使用 web_search 结果中的 snippet 分析

## 注意事项

- 规格表完整性是钢铁产品页面 SEO 的核心
- 询盘转化路径诊断是最关键的检查点（#14）
- B2B 信任元素（ISO/CE/Mill Certificate）必须展示
- FAQ 必须覆盖买家最关心的 6 类问题
- 内部链接要导向规格对比页、应用案例页、认证页
- 所有优化建议必须可执行，直接提供 HTML 代码

## 参考文档

- `references/product-page-checklist.md` - 产品页面完整检查清单
- `references/steel-grade-glossary.md` - 钢铁等级术语对照表
- `references/inquiry-cta-templates.md` - 询盘 CTA 模板

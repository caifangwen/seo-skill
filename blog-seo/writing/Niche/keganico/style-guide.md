# Keganico 写作风格指南

> 基于 keganico.com 现有 100+ 篇文章总结的写作规范

---

## 🎯 品牌声音

### 核心特质

```
✅ 专业 (Professional): 展示行业知识
✅ 友好 (Friendly): 平易近人，不傲慢
✅ 实用 (Practical): 注重可操作性
✅ B2B 导向 (Business-focused): 强调批发/OEM 服务
✅ 可信 (Trustworthy): 数据支撑，诚实客观
```

### 避免的特质

```
❌ 过于技术化：避免行话堆砌
❌ 销售导向：不要硬推销
❌ 模糊笼统：提供具体信息
❌ 傲慢自大：尊重读者智商
❌ 纯 B2C 视角：始终记得 B2B 受众
```

---

## 📝 人称使用

### 第二人称 (主要)

```
✅ 使用 you/your:
- "You'll find that..."
- "Your knife should..."
- "Whether you're a collector..."
- "For your business..."

❌ 避免:
- "One will find..." (太正式)
- "The user should..." (太疏远)
- "Customers may want..." (太疏远)
```

### 第一人称复数 (适度)

```
✅ 使用 we/us 代表品牌:
- "We recommend..."
- "Our testing shows..."
- "At Keganico, we specialize in..."
- "We supply countless North American knife stores..."

❌ 避免:
- "I think..." (太个人)
- "In my opinion..." (不专业)
```

### B2B 视角

```
✅ 适当提及商业场景:
- "For sourcing managers..."
- "For your business..."
- "If you're looking to stock knives..."
- "For OEM projects..."

❌ 避免:
- 纯消费者视角
- 忽略批发/OEM 机会
```

---

## 📏 句子长度

### 建议长度

```
短句：10-15 字 (25%)
中等句：15-25 字 (50%)
长句：25-35 字 (25%)

避免：>40 字的句子
```

### 示例

```
✅ 好:
"Fixed blade knives are stronger. They have no moving parts. 
This makes them reliable for heavy use."

❌ 差:
"Fixed blade knives, which are characterized by their lack of 
moving parts and full tang construction that extends into the 
handle, are generally considered to be stronger and more reliable 
than their folding counterparts, especially when it comes to 
heavy-duty applications."
```

---

## 📐 段落结构

### 段落长度

```
✅ 理想：2-4 句
✅ 最大：5 句
❌ 避免：>6 句的段落
```

### 段落模式

```
主题句 → 支持句 → 示例/细节 → (可选) 过渡句

示例:
Blade length affects legal compliance. (主题句)
Many jurisdictions limit carry length to 3-4 inches. (支持)
For example, New York City restricts blades to under 4 inches. 
(示例) Always check local laws before purchasing. (过渡/建议)
```

### Keganico 特色段落

```
数据支撑型:
According to Knife Steel Nerds testing, 14C28N scores 9.0 in 
toughness. This is 2.25 times that of S30V, which scores only 4.0. 
In practical applications, this exceptional toughness brings 
revolutionary advantages.

B2B 导向型:
Many OEM knife manufacturers praise 14C28N's "forgiving heat 
treatment." This makes it suitable for mass production without 
quality concerns. For knife sellers, this provides a reliable 
option to capture market share in the $30-100 price range.
```

---

## 🎨 格式规范

### 标题层级

```markdown
# H1: 文章标题 (只用一次)

## H2: 主要章节

### H3: 子章节

#### H4: 细分内容 (如需要)
```

### 粗体使用

```
✅ 强调关键信息:
- 开篇核心定义/定位
- 重要结论
- 数据/统计
- 列表小标题

❌ 避免:
- 整句粗体
- 连续粗体
- 无意义粗体
```

### 列表使用

```
✅ 适用场景:
- 3+ 个并列项
- 步骤说明
- 特点列举
- 优缺点列表

❌ 避免:
- 只有 1-2 项
- 嵌套过深 (>3 层)
- 混合类型
```

### 表格使用

```
✅ 适用:
- 产品对比
- 规格参数
- 性能评分
- 价格比较

❌ 避免:
- 简单数据用段落即可
- 超过 7 列
- 无表头
```

---

## 🔗 链接规范

### 内部链接

```markdown
✅ 描述性锚文本:
- [hunting knives](/hunting-knives/)
- [learn more about blade steel](/knife-steel-types/)
- [OEM knife manufacturers](/oem-knife-manufacturer/)

❌ 通用锚文本:
- [click here](/...)
- [read this](/...)
- [here](/...)
```

### 链接密度

```
每 300-400 字：1 个内链
整篇文章：10-20 个内链
每段：最多 2 个链接
```

### Keganico 常用链接

```
钢材页面:
- /14c28n-steel/
- /s30v-steel/
- /magnacut-steel/

分类页面:
- /product-category/knives/edc-knives/
- /product-category/knives/fixed-blade-knives/

服务页面:
- /oem-service/
- /private-label-service/
- /wholesale-service/
- /contact/
- /get-your-quote-2/

知识页面:
- /what-is-an-edc-knife/
- /knife-blade-shapes/
- /g10-handle/
```

---

## 🖼️ 图片规范

### 图片位置

```
开篇后：封面图
每 400-500 字：章节配图
表格/对比前：对比图
产品评测：产品图 (Figure 格式)
```

### Alt 文本

```
公式：[主体] + [动作/状态] + [场景]

✅ 好:
"tactical knives arranged on yellow bag"
"performance scorecard MagnaCut vs S30V"

❌ 差:
"image of knives" (太短)
"a picture showing various tactical knives that are arranged 
neatly on a bright yellow bag in a well-lit studio setting" (太长)
```

### Figure 格式 (产品图)

```markdown
<figure>

[![产品图片](链接)](产品链接/)

<figcaption>

[产品名称](产品链接/)

</figcaption>

</figure>
```

---

## 📊 数据使用规范

### 数据来源

```
✅ 权威来源:
- Knife Steel Nerds
- zknives.com
- CATRA 测试
- 钢厂官方数据表 (Alleima, Böhler 等)

❌ 避免:
- 无来源数据
- 论坛传言
- 过时数据
```

### 数据呈现

```markdown
✅ 正确格式:
| Element | % | Role |
| --- | --- | --- |
| Carbon (C) | 0.62% | Base hardness contributor |

<figcaption>
_Data source: [Alleima technical datasheet](链接)_
</figcaption>

✅ 评分格式:
| Performance | Score |
| --- | --- |
| Toughness | 9.0/10 ★★★★★ |
| Edge Retention | 3.0/10 ★★☆☆☆ |
```

### 数据解读

```
数据 + 解读 + 实际意义

示例:
14C28N's toughness score is 9.0. This is 2.25 times that of S30V 
(4.0). In practical applications, manufacturers can confidently 
use sharp 15-17 degree edge angles without worrying about chipping.
```

---

## ✍️ 语法规范

### 时态使用

```
✅ 一般现在时 (主要):
- "Fixed blade knives are..."
- "We recommend..."
- "14C28N offers..."

✅ 一般过去时 (历史/测试):
- "The brand was founded in 2018..."
- "Our testing showed..."

✅ 将来时 (建议/预测):
- "You'll find..."
- "This will last..."
```

### 语态使用

```
✅ 主动语态 (优先):
- "We tested the knives."
- "Users prefer this design."

⚠️ 被动语态 (适度):
- "The knives were tested." (可接受)
- "This design is preferred." (可接受)
```

### 标点符号

```
✅ 正确:
- 逗号后加空格
- 冒号后首字母小写 (除非完整句子)
- 引号内标点

❌ 错误:
- 逗号后无空格
- 多个感叹号!!!
- 滥用省略号...
```

---

## 🚫 禁用词汇

### 避免过度使用的词

```
❌ very, really, extremely (空洞强调)
❌ amazing, incredible, awesome (过度夸张)
❌ basically, essentially, actually (填充词)
❌ thing, stuff, things (模糊名词)
❌ game-changer, revolutionary (过度营销)
```

### 替代表达

```
❌ "very sharp" → ✅ "razor-sharp"
❌ "really good" → ✅ "excellent"
❌ "amazing quality" → ✅ "premium quality"
❌ "this thing" → ✅ "this feature/design/tool"
❌ "game-changer" → ✅ "significant improvement"
```

### Keganico 推荐表达

```
✅ 专业表达:
- "outstanding performance"
- "exceptional toughness"
- "excellent value proposition"
- "proven track record"
- "industry-leading"

✅ B2B 表达:
- "cost-effective solution"
- "reliable supply chain"
- "consistent quality control"
- "competitive pricing"
- "scalable production"
```

---

## 📋 文章结构规范

### 开篇公式

```
第 1 段 (80-120 字):
**粗体核心答案/定位** + 扩展说明 1-2 句

第 2 段 (80-150 字):
背景信息 + 数据支撑 + 内部链接

第 3 段 (可选，50-80 字):
内容预告 + 引导语
```

### 主体章节

```
每个 H2 章节:
- 开篇句 (引入主题)
- 详细内容 (2-4 段)
- 图片/表格
- 内部链接
- 小结/过渡 (可选)
```

### FAQ 章节

```
- 3-8 个问题
- 每个 2-4 句回答
- 直接回答问题
- 包含数据支撑
- 可含内部链接
```

### CTA 章节

```
- 总结价值
- 行动动词开头
- 提供选项 (OEM/Private Label/Wholesale)
- 明确链接
- 低门槛表达 (free quote)
```

---

## 🎯 内容深度

### 文章长度建议

| 类型 | 字数 | 深度 |
|------|------|------|
| 钢材评测 | 2500-3500 | 全面深入 |
| 钢材对比 | 3000-4000 | 详细对比 |
| 刀具知识 | 2000-3000 | 全面介绍 |
| 品牌评测 | 3500-5000 | 深度分析 |
| 材料对比 | 2000-3000 | 详细对比 |
| OEM 指南 | 3000-5000 | 专业深入 |

### 信息密度

```
每 500 字应包含:
✅ 1 个核心观点
✅ 1-2 个支撑论据
✅ 1 个示例/数据
✅ 1 张图片/表格
```

---

## 💼 B2B 写作特色

### OEM 服务植入

```
自然植入方式:
- "Many OEM knife manufacturers praise..."
- "For sourcing managers, the choice is..."
- "If you're looking to stock knives..."
- "At Keganico, we specialize in OEM..."

避免:
- 硬插入广告
- 过度推销
- 与服务无关的植入
```

### 价格/成本信息

```
✅ 提供价格区间:
- "typically range from $60 to $80"
- "priced around $40-$60"
- "Target MSRP: $120-$200"

✅ 提供成本分析:
- "Material cost is significantly higher..."
- "For mass production, this reduces unit cost..."

❌ 避免:
- 具体定价 (除非公开)
- 过于详细的成本拆解
```

### 供应链能力展示

```
✅ 展示实力:
- "WE Knife Company created Civivi after spending twenty years 
   building high-end cutlery products."
- "Yangjiang accounts for approximately 70% of China's total 
   knife and scissors production."
- "We supply countless North American knife stores and wholesalers."

❌ 避免:
- 空洞的自夸
- 无数据支撑的声明
```

---

## ✅ 检查清单

### 风格检查

```
□ 语气专业友好
□ 第二人称为主
□ 句子长度多样
□ 段落 2-4 句
□ 无拼写/语法错误
```

### 格式检查

```
□ 标题层级正确
□ 粗体使用恰当
□ 列表格式统一
□ 表格清晰
□ 图片规范
```

### 内容检查

```
□ 开篇有粗体核心
□ 每 400 字有图片
□ 内链 10-20 个
□ FAQ 3-8 个
□ CTA 明确
□ B2B 元素完整
```

### 数据检查

```
□ 所有数据有来源
□ 数据准确最新
□ 解读清晰
□ 年份正确 (2026)
```

---

*Keganico Skills v1.0 | Style Guide | 最后更新：2026-03-26*

# Steel Product Page Checklist

## 概述

钢铁外贸 B2B 产品页面完整检查清单，包含 15 点诊断的详细说明和最佳实践。

## 通用 SEO 检查点 (1-12)

### 1. Title Tag

**检查标准**：
- [ ] 长度 50-60 字符（含空格）
- [ ] 核心关键词前置
- [ ] 包含产品名 + 规格范围 + 标准
- [ ] 结尾加公司名或"China Factory/Supplier"
- [ ] 无堆砌关键词

**钢铁行业公式**：
```
[Product] [Spec Range] - [Standard/Grade] | [Company/China Factory]
```

**评分标准**：
- ✅ 优秀：包含完整 Triad 模型，长度适中
- ⚠️ 一般：缺少规格范围或标准号
- ❌ 差：过短/过长/关键词堆砌

---

### 2. Meta Description

**检查标准**：
- [ ] 长度 150-160 字符（含空格）
- [ ] 包含核心关键词
- [ ] 包含 MOQ（最小起订量）
- [ ] 包含交期（Lead Time）
- [ ] 包含认证信息
- [ ] 包含时效性 CTA

**钢铁行业公式**：
```
[Product] [Core Spec] for [Application]. [Certifications]. 
MOQ [Quantity], [Lead Time] delivery. [CTA with urgency].
```

**评分标准**：
- ✅ 优秀：包含所有必须元素，CTA 清晰
- ⚠️ 一般：缺少 MOQ 或交期
- ❌ 差：缺失或过长/过短

---

### 3. H1 Heading

**检查标准**：
- [ ] 页面唯一 H1
- [ ] 包含产品全称
- [ ] 包含核心规格
- [ ] 长度 20-70 字符
- [ ] 无多个 H1 标签

**示例**：
```html
<!-- ✅ 优秀 -->
<h1>ASTM A615 Gr40/60 Rebar 10-50mm - Deformed Steel Bar for Construction</h1>

<!-- ⚠️ 一般 -->
<h1>Rebar - Steel Bar</h1>

<!-- ❌ 差 -->
<h1>Products</h1>
```

---

### 4. H2/H3 Structure

**检查标准**：
- [ ] H2 覆盖主要话题（规格、应用、认证、FAQ）
- [ ] H3 用于子话题
- [ ] 逻辑层级清晰
- [ ] 包含关键词变体

**推荐结构**：
```html
<h1>Product Name</h1>
<h2>Specifications</h2>
<h3>Technical Parameters</h3>
<h3>Grade Equivalents</h3>
<h2>Applications</h2>
<h2>Certifications</h2>
<h2>Packaging & Delivery</h2>
<h2>FAQ</h2>
```

---

### 5. Keyword Density

**检查标准**：
- [ ] 核心关键词密度 1-3%
- [ ] 规格词自然分布
- [ ] 无关键词堆砌
- [ ] 同义词/变体词使用合理

**工具检查**：
- 使用 `web_fetch` 抓取页面后统计词频
- 核心词出现 5-15 次为宜（800 词内容）

---

### 6. Internal Links

**检查标准**：
- [ ] 链接到相关产品页
- [ ] 链接到规格对比页
- [ ] 链接到应用案例页
- [ ] 链接到认证页面
- [ ] 锚文本描述性

**钢铁行业推荐链接**：
| 目标页面 | 锚文本示例 |
|----------|------------|
| 规格对比页 | "Compare ASTM A615 Gr40 vs Gr60" |
| 应用案例页 | "Rebar for construction projects" |
| 认证页面 | "View our ISO and CE certificates" |
| 价格页面 | "Today's rebar price" |

---

### 7. Image Alt Tags

**检查标准**：
- [ ] 所有图片有 alt 属性
- [ ] alt 包含产品名 + 规格
- [ ] 无空 alt 或堆砌关键词
- [ ] 主产品图 alt 包含核心关键词

**示例**：
```html
<!-- ✅ 优秀 -->
<img src="rebar-astm-a615.jpg" alt="ASTM A615 Gr60 Rebar 12mm deformed steel bar">

<!-- ⚠️ 一般 -->
<img src="rebar.jpg" alt="Rebar">

<!-- ❌ 差 -->
<img src="img001.jpg" alt="">
```

---

### 8. URL Structure

**检查标准**：
- [ ] 简洁清晰
- [ ] 包含核心关键词
- [ ] 无过长参数
- [ ] 使用连字符分隔单词

**示例**：
```
✅ /product/rebar-astm-a615-gr40-gr60/
✅ /steel-products/hot-rolled-coil-hrc/
⚠️ /product.php?id=123&cat=456
❌ /p/rb_stl_br_a615/
```

---

### 9. Mobile Friendliness

**检查标准**：
- [ ] 移动端显示正常
- [ ] 文字无需缩放即可阅读
- [ ] 询盘按钮可见
- [ ] 规格表可横向滚动
- [ ] 图片自适应

**测试方法**：
- 使用 Google Mobile-Friendly Test
- 实际手机测试

---

### 10. Page Speed

**检查标准**：
- [ ] 加载时间 <3 秒
- [ ] 规格表不拖慢加载
- [ ] 图片压缩优化
- [ ] 无过多外部资源

**测试工具**：
- Google PageSpeed Insights
- GTmetrix

---

### 11. Schema Markup

**检查标准**：
- [ ] Product Schema 存在
- [ ] 包含价格范围
- [ ] 包含库存状态
- [ ] 包含规格属性
- [ ] Organization Schema 存在
- [ ] FAQPage Schema（如有 FAQ）

**Product Schema 示例**：
```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "ASTM A615 Gr40/60 Rebar",
  "description": "Deformed steel bar for construction",
  "brand": {
    "@type": "Brand",
    "name": "Company Name"
  },
  "offers": {
    "@type": "Offer",
    "priceCurrency": "USD",
    "minPrice": "500",
    "maxPrice": "700",
    "availability": "https://schema.org/InStock"
  }
}
```

---

### 12. Content Length

**检查标准**：
- [ ] 产品描述 ≥800 词
- [ ] 规格表不计入字数
- [ ] FAQ 不计入字数
- [ ] 覆盖产品、应用、认证、交货

**内容结构建议**：
| 部分 | 建议字数 |
|------|----------|
| 产品简介 | 150-200 词 |
| 详细描述 | 400-500 词 |
| 应用场景 | 150-200 词 |
| 认证/质检 | 100-150 词 |

---

## 钢铁行业特殊检查点 (13-15)

### 13. 规格表完整性 ⭐⭐⭐⭐⭐

**检查标准**：
- [ ] 包含完整技术参数
- [ ] 包含公差范围
- [ ] 包含等级等价对照（GB/ASTM/EN/JIS）
- [ ] 包含 MOQ
- [ ] 包含交期
- [ ] HTML 表格结构清晰
- [ ] 移动端可滚动查看

**必须包含的参数**：
| 参数类型 | 示例 |
|----------|------|
| 产品名 | Deformed Steel Bar (Rebar) |
| 标准 | ASTM A615 Gr40/60 |
| 等级 | Grade 40 (280MPa), Grade 60 (420MPa) |
| 直径 | 10mm, 12mm, 16mm, 20mm, 25mm, 32mm, 40mm, 50mm |
| 长度 | 6m, 9m, 12m or as per requirement |
| 屈服强度 | Gr40: ≥280MPa, Gr60: ≥420MPa |
| 抗拉强度 | Gr40: ≥420MPa, Gr60: ≥620MPa |
| 延伸率 | ≥12% |
| 表面 | Ribbed/Deformed |
| 认证 | ISO9001, CE, Mill Test Certificate |
| MOQ | 25MT |
| 交期 | 15-20 days after deposit |

---

### 14. 询盘路径诊断 ⭐⭐⭐⭐⭐ (最关键)

**检查标准**：
- [ ] RFQ 表单首屏可见或 1 次滚动内
- [ ] RFQ 表单字段 ≤5 个必填
- [ ] WhatsApp 按钮悬浮
- [ ] WeChat 二维码（针对中国买家）
- [ ] 响应时间承诺（"Reply within 2 hours"）
- [ ] 隐私保护声明

**RFQ 表单最佳实践**：
| 字段 | 必填 | 说明 |
|------|------|------|
| 姓名 | ✅ | Your Name |
| 邮箱 | ✅ | Your Email |
| 产品 | ✅ | Product Name |
| 规格 | ✅ | Specification |
| 数量 | ✅ | Quantity (MT) |
| 电话 | ❌ | Phone/WhatsApp (optional) |
| 留言 | ❌ | Additional requirements |

**转化元素检查**：
- [ ] CTA 按钮文字清晰（"Get Best Price", "Request Quote"）
- [ ] 信任文字（"No spam", "We respect your privacy"）
- [ ] 响应时间承诺
- [ ] 多种联系方式（表单、WhatsApp、Email）

---

### 15. B2B 信任元素 ⭐⭐⭐⭐

**检查标准**：
- [ ] ISO9001 认证展示
- [ ] CE 认证展示
- [ ] Mill Test Certificate 样本
- [ ] 真实工厂图片
- [ ] 仓库/库存图片
- [ ] 项目案例
- [ ] 客户评价（如有）

**信任元素优先级**：
| 元素 | 重要性 | 位置建议 |
|------|--------|----------|
| ISO/CE 认证图标 | ⭐⭐⭐⭐⭐ | 产品描述下方 |
| Mill Certificate 样本 | ⭐⭐⭐⭐⭐ | 规格表下方 |
| 工厂图片 | ⭐⭐⭐⭐ | 页面中部 |
| 项目案例 | ⭐⭐⭐⭐ | 页面底部 |
| 客户评价 | ⭐⭐⭐ | 页面底部 |

---

## 评分标准

### 总体评分

| 分数 | 等级 | 说明 |
|------|------|------|
| 90-100 | A+ | 优秀，无需大改 |
| 80-89 | A | 良好，少量优化 |
| 70-79 | B | 中等，需要改进 |
| 60-69 | C | 及格，多处需优化 |
| <60 | D | 差，需要全面重构 |

### 优先级分类

| 优先级 | 检查点 | 要求 |
|--------|--------|------|
| P0 (Critical) | #13, #14 | 必须立即修复 |
| P1 (Important) | #1, #2, #3, #15 | 1 周内修复 |
| P2 (Suggestions) | 其他 | 1 月内修复 |

---

## 使用指南

### 诊断流程

1. 使用 `web_fetch` 抓取目标页面
2. 逐项检查 15 个检查点
3. 记录每个检查点的状态（✅/⚠️/❌）
4. 计算总体评分
5. 按优先级输出改进建议

### 输出模板

```markdown
## Page Audit Summary
- URL: [URL]
- Score: [XX]/100
- Grade: [A+/A/B/C/D]

## Critical Issues (P0)
- #14: [Issue description]
- #13: [Issue description]

## Important Issues (P1)
- #1: [Issue description]
- #2: [Issue description]

## Suggestions (P2)
- #6: [Issue description]
```

## 参考链接

- [Google SEO Starter Guide](https://developers.google.com/search/docs/beginner/seo-starter-guide)
- [Schema.org Product](https://schema.org/Product)

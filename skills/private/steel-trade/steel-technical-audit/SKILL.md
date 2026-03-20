---
name: steel-technical-audit
version: "1.0.0"
description: |
  钢铁外贸 B2B 网站技术 SEO 审计专用 Skill
  触发场景：
  - 用户需要技术 SEO 诊断（如"technical SEO audit", "网站技术诊断"）
  - 多语言/多地区配置检查（如"hreflang 检查", "多语言 SEO"）
  - 询盘表单功能排查（如"RFQ form not working", "询盘表单问题"）
  - 移动端询盘流程优化（如"mobile inquiry optimization"）
  - 产品目录结构优化（如"product URL structure", "catalog SEO"）
  - Schema 标记检查（如"schema markup check", "structured data"）
  - 网站速度优化（如"page speed optimization", "网站加速"）
compatibility:
  tools: [web_search, web_fetch, bash]
---

# Steel Technical Audit

## 概述

专为钢铁外贸 B2B 网站设计的技术 SEO 审计 Skill。除了通用技术 SEO 检查外，特别关注**多语言/多地区配置**、**询盘转化路径**和**产品目录结构**三大钢铁外贸网站特殊需求，帮助确保网站技术基础设施支持询盘转化目标。

## 核心逻辑

> **"技术 SEO 为询盘转化服务"**

所有技术优化都围绕确保买家能够顺利找到产品、理解规格、发送询盘。

## 前置条件

开始前必须获取的信息：
- [ ] **网站 URL**：需要审计的网站地址
- [ ] **目标市场**：主要买家国家/地区（如 Saudi Arabia, Vietnam）
- [ ] **网站类型**：企业官网 / B2B 平台店铺 / 独立站
- [ ] **可选信息**：Google Analytics/Search Console 访问权限、现有关于询盘转化的问题反馈

如信息不完整，必须先向用户询问，不得跳过。

## 核心工作流

### 步骤 1: 通用技术 SEO 检查

首先进行标准技术 SEO 审计：

| 检查项 | 检查内容 | 工具/方法 |
|--------|----------|-----------|
| 爬取可访问性 | robots.txt 不 blocking 重要页面 | `web_fetch` robots.txt |
| XML Sitemap | 存在且包含所有产品页 | 检查 /sitemap.xml |
| HTTPS | 全站 HTTPS，无混合内容 | 检查 URL 协议 |
| 404 错误 | 无重要页面 404 | `web_search` site:domain |
| 重定向 | 301 正确配置，无重定向链 | 手动测试关键 URL |
| 规范标签 | canonical 正确设置 | 检查页面 HTML |
| 网站速度 | 加载时间<3 秒，Core Web Vitals 达标 | PageSpeed Insights |
| 移动端友好 | 响应式设计，移动端可用 | Mobile-Friendly Test |
| 结构化数据 | Product/Organization Schema | Rich Results Test |

---

### 步骤 2: 特殊审计 A - 多语言/多地区配置

针对钢铁外贸网站的多买家市场特点进行审计：

#### A1. hreflang 标签检查

**检查标准**：
- [ ] 所有语言版本页面有 hreflang 标签
- [ ] 包含 x-default 标签
- [ ] hreflang 双向对应（A 指向 B，B 指向 A）
- [ ] 语言和地区代码正确（ar-SA, es-ES, vi-VN）

**钢铁外贸常见语言配置**：
| 语言 | 代码 | 目标市场 |
|------|------|----------|
| 英语（默认） | en, en-US | 全球 |
| 阿拉伯语 | ar, ar-SA | 沙特、中东 |
| 西班牙语 | es, es-ES | 南美、墨西哥 |
| 葡萄牙语 | pt, pt-BR | 巴西 |
| 越南语 | vi, vi-VN | 越南 |
| 印尼语 | id, id-ID | 印尼 |
| 泰语 | th, th-TH | 泰国 |

**正确示例**：
```html
<link rel="alternate" hreflang="en" href="https://example.com/en/rebar/" />
<link rel="alternate" hreflang="ar" href="https://example.com/ar/rebar/" />
<link rel="alternate" hreflang="es" href="https://example.com/es/rebar/" />
<link rel="alternate" hreflang="x-default" href="https://example.com/en/rebar/" />
```

**常见错误**：
- ❌ 只有英语版本，无其他语言
- ❌ hreflang 代码错误（如用"arabic"而非"ar"）
- ❌ 缺少 x-default
- ❌ 单向引用（A 指向 B，但 B 不指向 A）

#### A2. 内容质量检查（非机器翻译）

**检查标准**：
- [ ] 非 Google 翻译直出内容
- [ ] 专业术语准确（钢号、标准号）
- [ ] 本地化表达（而非直译）
- [ ] 联系方式本地化（本地电话、WhatsApp）

**机器翻译识别标志**：
- 钢号错误（如将"Grade 60"翻译成"60 级"）
- 标准号格式错误
- 语句不通顺
- 行业术语不统一

#### A3. CDN 和地区覆盖

**检查标准**：
- [ ] CDN 覆盖目标市场（中东、东南亚、非洲）
- [ ] 目标地区加载速度<3 秒
- [ ] 使用地区特定 CDN 节点

**推荐 CDN**：
| CDN | 优势地区 | 适用场景 |
|-----|----------|----------|
| Cloudflare | 全球 | 通用 |
| AWS CloudFront | 全球 | 大型网站 |
| 阿里云 CDN | 东南亚、中东 | 专注新兴市场 |
| 腾讯云 CDN | 东南亚 | 专注新兴市场 |

---

### 步骤 3: 特殊审计 B - 询盘转化路径

针对钢铁外贸 B2B 询盘转化进行技术审计：

#### B1. RFQ 表单功能检查

**检查清单**：
- [ ] 表单可正常提交
- [ ] 提交后有成功提示
- [ ] 表单数据正确发送到邮箱/CRM
- [ ] 表单字段验证合理（不过严也不过松）
- [ ] 有防垃圾措施（honeypot/reCAPTCHA）
- [ ] 移动端表单易用

**测试流程**：
1. 实际提交测试表单
2. 检查是否收到邮件
3. 检查 CRM 是否创建记录
4. 检查成功提示页面

#### B2. 表单 SEO 可见性

**检查标准**：
- [ ] 表单页面不被 robots.txt blocking
- [ ] 表单页面有独立 URL
- [ ] 表单页面有 Title/Meta
- [ ] 表单内容可被搜索引擎理解

**常见错误**：
```
❌ robots.txt:
Disallow: /rfq/
Disallow: /inquiry/
Disallow: /contact/

✅ 应该允许爬取：
Allow: /rfq/
Allow: /inquiry/
```

#### B3. 移动端询盘流程

**检查清单**：
- [ ] WhatsApp 按钮悬浮且可点击
- [ ] WeChat 二维码可扫描
- [ ] 电话链接可拨打（tel:）
- [ ] 邮件链接可发送（mailto:）
- [ ] 表单在移动端易填写
- [ ] CTA 按钮在拇指热区

**移动端最佳实践**：
```html
<!-- 电话链接 -->
<a href="tel:+861234567890" class="cta-button">📞 Call Now</a>

<!-- WhatsApp 链接 -->
<a href="https://wa.me/861234567890" class="whatsapp-button">💬 WhatsApp</a>

<!-- 邮件链接 -->
<a href="mailto:sales@example.com" class="email-button">✉️ Email</a>
```

---

### 步骤 4: 特殊审计 C - 产品目录配置

针对钢铁产品目录进行技术审计：

#### C1. URL 结构检查

**推荐结构**：
```
✅ /product/rebar-astm-a615/
✅ /product/hot-rolled-coil-hrc/
✅ /product/seamless-pipe-astm-a106/
✅ /category/long-products/rebar/
✅ /category/flat-products/hrc/

❌ /product.php?id=123
❌ /p/rb_a615/
❌ /products/category/1/2/
```

**URL 最佳实践**：
- 包含核心关键词（产品名 + 标准）
- 使用连字符分隔单词
- 长度适中（<60 字符）
- 层级不超过 3 层

#### C2. 图片 Alt 标签

**检查标准**：
- [ ] 所有产品图片有 alt
- [ ] alt 包含产品名 + 规格
- [ ] 无空 alt 或堆砌关键词

**示例**：
```html
<!-- ✅ 优秀 -->
<img src="rebar-astm-a615.jpg" alt="ASTM A615 Gr60 Rebar 12mm deformed steel bar for construction">

<!-- ❌ 差 -->
<img src="img001.jpg" alt="">
<img src="rebar.jpg" alt="rebar steel bar iron metal construction">
```

#### C3. Schema Markup

**必须包含的 Schema 类型**：

**Product Schema**：
```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "ASTM A615 Gr40/60 Rebar",
  "description": "Deformed steel bar for construction and infrastructure",
  "brand": {
    "@type": "Brand",
    "name": "Your Company"
  },
  "offers": {
    "@type": "Offer",
    "priceCurrency": "USD",
    "minPrice": "500",
    "maxPrice": "700",
    "availability": "https://schema.org/InStock",
    "seller": {
      "@type": "Organization",
      "name": "Your Company"
    }
  },
  "additionalProperty": [
    {
      "@type": "PropertyValue",
      "name": "Standard",
      "value": "ASTM A615 Gr40/60"
    },
    {
      "@type": "PropertyValue",
      "name": "Diameter",
      "value": "10-50mm"
    },
    {
      "@type": "PropertyValue",
      "name": "Certification",
      "value": "ISO9001, CE, Mill Certificate"
    }
  ]
}
```

**Organization Schema**：
```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Your Company",
  "url": "https://example.com",
  "logo": "https://example.com/logo.png",
  "description": "Professional steel manufacturer and exporter",
  "address": {
    "@type": "PostalAddress",
    "addressCountry": "CN"
  },
  "contactPoint": {
    "@type": "ContactPoint",
    "contactType": "sales",
    "email": "sales@example.com",
    "telephone": "+86-123-4567-890"
  },
  "sameAs": [
    "https://www.linkedin.com/company/your-company",
    "https://www.facebook.com/your-company"
  ]
}
```

**FAQPage Schema**（如有 FAQ）：
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is your MOQ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Our MOQ is 25MT for standard specifications."
      }
    }
  ]
}
```

---

### 步骤 5: 优先级排序

将发现的问题按优先级排序：

| 优先级 | 类型 | 响应时间要求 | 示例 |
|--------|------|--------------|------|
| P0 (Critical) | 阻塞询盘、搜索引擎无法爬取 | 立即修复 | RFQ 表单不工作、robots.txt blocking 产品页 |
| P1 (Important) | 影响转化、用户体验 | 1 周内修复 | 移动端表单难用、缺少 hreflang |
| P2 (Suggestions) | 优化建议 | 1 月内修复 | URL 结构优化、Schema 增强 |

---

### 步骤 6: 输出结果

输出格式：

```markdown
# Steel Technical Audit Report

## Website
[URL]

## Audit Date
[Date]

## Executive Summary
- Total Issues Found: [Count]
- Critical (P0): [Count]
- Important (P1): [Count]
- Suggestions (P2): [Count]
- Overall Health Score: [Score]/100

## General Technical SEO

### Crawling & Indexing
| Status | Issue | Impact | Recommendation |
|--------|-------|--------|----------------|
| ✅/⚠️/❌ | [Issue] | High/Med/Low | [Fix] |

### Site Performance
| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Page Load Time | [X]s | <3s | ✅/⚠️/❌ |
| Core Web Vitals | [Score] | >90 | ✅/⚠️/❌ |

## Special Audit A: Multi-language/Region

### hreflang Implementation
| Status | Issue | Impact | Recommendation |
|--------|-------|--------|----------------|
| ✅/⚠️/❌ | [Issue] | High/Med/Low | [Fix] |

### Content Localization
| Language | Status | Issues | Recommendation |
|----------|--------|--------|----------------|
| Arabic | ✅/⚠️/❌ | [Issues] | [Fix] |
| Spanish | ✅/⚠️/❌ | [Issues] | [Fix] |
| Vietnamese | ✅/⚠️/❌ | [Issues] | [Fix] |

## Special Audit B: Inquiry Conversion Path

### RFQ Form Functionality
| Test | Result | Issue | Fix |
|------|--------|-------|-----|
| Form Submission | Pass/Fail | [Issue] | [Fix] |
| Email Notification | Pass/Fail | [Issue] | [Fix] |
| Mobile Usability | Pass/Fail | [Issue] | [Fix] |

### Mobile Inquiry Flow
| Element | Status | Issue | Fix |
|---------|--------|-------|-----|
| WhatsApp Button | ✅/⚠️/❌ | [Issue] | [Fix] |
| Click-to-Call | ✅/⚠️/❌ | [Issue] | [Fix] |
| Form Mobile UX | ✅/⚠️/❌ | [Issue] | [Fix] |

## Special Audit C: Product Catalog

### URL Structure
| Page Type | Current | Recommended | Priority |
|-----------|---------|-------------|----------|
| Product Pages | [URL pattern] | [Suggested] | P0/P1/P2 |
| Category Pages | [URL pattern] | [Suggested] | P0/P1/P2 |

### Schema Markup
| Schema Type | Present | Valid | Recommendation |
|-------------|---------|-------|----------------|
| Product | ✅/❌ | ✅/❌ | [Fix] |
| Organization | ✅/❌ | ✅/❌ | [Fix] |
| FAQPage | ✅/❌ | ✅/❌ | [Fix] |

## Priority Roadmap

### P0 (Critical) - Fix Immediately
1. [Issue + Fix]
2. [Issue + Fix]

### P1 (Important) - Fix Within 1 Week
1. [Issue + Fix]
2. [Issue + Fix]

### P2 (Suggestions) - Fix Within 1 Month
1. [Issue + Fix]
2. [Issue + Fix]

## Implementation Guide

### [Issue 1]
**Problem:** [Description]
**Impact:** [Business impact]
**Solution:** [Step-by-step fix]
**Code/Config:** [If applicable]

### [Issue 2]
...
```

## 输出规范

- 必须覆盖通用技术 SEO + 3 个特殊审计维度
- 必须提供优先级排序（P0/P1/P2）
- 必须提供实施指南和代码示例
- 必须提供整体健康评分
- 所有问题必须附带修复建议

## 错误处理

- **网站无法访问** → 告知用户并提供自查清单
- **无法测试表单** → 提供表单测试指南让用户自行测试
- **无 Analytics 权限** → 基于可见数据推断，标注需要验证
- **多语言页面不存在** → 建议添加，提供实施方案

## 注意事项

- 技术 SEO 的最终目标是支持询盘转化
- 多语言配置对钢铁外贸至关重要（中东、东南亚、南美）
- RFQ 表单功能必须 100% 可靠，定期测试
- 移动端询盘流程必须流畅（WhatsApp/WeChat 集成）
- Schema 标记有助于搜索结果展示（富媒体片段）

## 参考文档

- `references/b2b-ux-checklist.md` - B2B 网站用户体验检查清单

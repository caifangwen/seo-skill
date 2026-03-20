---
name: steel-report-generator
version: "1.0.0"
description: |
  钢铁外贸 B2B SEO 报告生成专用 Skill
  触发场景：
  - 用户需要生成 SEO 月报（如"generate SEO monthly report", "SEO 月报"）
  - 询盘转化分析报告（如"inquiry conversion report", "询盘分析"）
  - 关键词排名报告（如"keyword ranking report", "关键词排名"）
  - 网站流量分析（如"traffic analysis report", "流量报告"）
  - 竞品对比报告（如"competitor analysis report", "竞品对比"）
  - 季度/年度总结（如"quarterly SEO review", "年度 SEO 总结"）
  - 绩效汇报（如"SEO performance report", "SEO 汇报"）
compatibility:
  tools: [web_search, web_fetch, bash]
---

# Steel Report Generator

## 概述

专为钢铁外贸 B2B 设计的 SEO 报告生成 Skill。基于**询盘为核心**的 KPI 体系（而非流量），生成包含询盘分析、关键词排名、流量分析、内容/外链进展、技术 SEO 状态的完整报告，帮助展示 SEO 工作对业务的实际价值。

## 核心逻辑

> **"询盘而非流量是核心指标"**

钢铁外贸 B2B SEO 的所有报告都围绕询盘转化展开，流量只是过程指标，询盘才是结果指标。

## 前置条件

开始前必须获取的信息：
- [ ] **报告周期**：月度/季度/年度
- [ ] **网站 URL**：需要报告的网站
- [ ] **目标市场**：主要买家国家/地区
- [ ] **数据来源**：Google Analytics/Search Console 访问权限或导出数据
- [ ] **可选信息**：CRM 询盘数据、竞品列表、历史报告

如信息不完整，必须先向用户询问，不得跳过。

## 核心工作流

### 步骤 1: KPI 体系定义

钢铁外贸 B2B SEO 的 KPI 分为三个层级：

#### Level 1 - 核心指标（询盘相关）

| 指标 | 定义 | 目标值 | 数据来源 |
|------|------|--------|----------|
| 自然搜索询盘数 | 来自有机搜索的询盘数量 | 月增长 10-20% | Google Analytics + CRM |
| 询盘转化率 | 询盘数/自然搜索会话数 | 1-3% | GA4 Conversions |
| 询盘关键词分布 | 带来询盘的关键词列表 | Top 20 覆盖核心产品 | GSC + CRM |
| 高价值询盘占比 | Transactional 意图询盘比例 | >50% | 手动分类 |

#### Level 2 - 过程指标（流量相关）

| 指标 | 定义 | 目标值 | 数据来源 |
|------|------|--------|----------|
| 自然搜索会话数 | 来自有机搜索的访问 | 月增长 5-10% | Google Analytics |
| 国家流量分布 | 各目标市场流量占比 | 中东/东南亚/非洲 >70% | GA Geo Report |
| 关键词排名 | 核心关键词排名位置 | Top 10 关键词数增长 | GSC/Rank Tracker |
| 新收录页面 | 新增索引页面数 | 月增 10-20 页 | GSC Indexing |
| 新增外链 | 新增反向链接域名数 | 月增 5-10 个 | Ahrefs/Semrush |

#### Level 3 - 辅助指标（内容/技术）

| 指标 | 定义 | 目标值 | 数据来源 |
|------|------|--------|----------|
| 产品页流量 | 产品页面访问量 | 占总流量>50% | GA Page Report |
| 热门产品页 | Top 10 产品页面 | 覆盖核心产品 | GA Page Report |
| 内容更新数 | 新增/更新内容数量 | 月增 4-8 篇 | CMS |
| 技术 SEO 健康度 | 技术审计得分 | >85/100 | Audit Tool |
| 页面速度 | 平均加载时间 | <3 秒 | PageSpeed |

---

### 步骤 2: 数据收集

#### 数据来源清单

| 数据类别 | 具体数据 | 来源 | 获取方式 |
|----------|----------|------|----------|
| 询盘数据 | 询盘总数、来源、关键词 | CRM + GA4 | 导出 CSV |
| 流量数据 | 会话数、页面浏览、跳出率 | GA4 | 导出 CSV |
| 排名数据 | 关键词排名、曝光、点击 | GSC | 导出 CSV |
| 外链数据 | 新增外链、域名权威 | Ahrefs/Semrush | 导出 CSV |
| 内容数据 | 新页面、更新页面 | CMS | 手动统计 |
| 技术数据 | 健康度、错误数 | Audit Tool | 运行审计 |

#### 数据收集模板

```markdown
## Data Collection Checklist

### Google Analytics 4
- [ ] Acquisition > Traffic Acquisition (Organic Search)
- [ ] Engagement > Pages and Screens (Product Pages)
- [ ] Engagement > Events (Inquiry Submissions)
- [ ] Monetization > Conversions (RFQ Form)
- [ ] Demographics > User Demographics (by Country)

### Google Search Console
- [ ] Performance > Search Results (Total Clicks, Impressions, CTR, Position)
- [ ] Performance > Queries (Top Keywords)
- [ ] Performance > Pages (Top Landing Pages)
- [ ] Performance > Countries (by Target Market)
- [ ] Indexing > Pages (Indexed vs Non-Indexed)

### CRM/Email
- [ ] Total Inquiries (by Source: Organic Search)
- [ ] Inquiry Details (Product, Specification, Country)
- [ ] Conversion Status (Quoted, Negotiating, Closed)

### Backlink Tool (Ahrefs/Semrush)
- [ ] Total Backlinks
- [ ] Referring Domains
- [ ] New Backlinks (This Period)
- [ ] Lost Backlinks (This Period)
- [ ] Top Anchor Texts
```

---

### 步骤 3: 报告结构

钢铁外贸 B2B SEO 报告的标准结构：

#### 1. Executive Summary（执行摘要）

**内容**：
- 报告周期
- 核心指标概览（询盘数、转化率、流量）
- 关键成就（Top 3）
- 主要问题（Top 3）
- 下月优先级

**模板**：
```markdown
## Executive Summary

**Report Period:** [Month Year]

**Key Metrics:**
| Metric | This Month | Last Month | Change |
|--------|------------|------------|--------|
| Organic Inquiries | [X] | [Y] | [+Z%] |
| Inquiry Rate | [X%] | [Y%] | [+/-Z%] |
| Organic Sessions | [X] | [Y] | [+Z%] |
| Avg. Position | [X] | [Y] | [+/-Z] |

**Key Achievements:**
1. [Achievement 1]
2. [Achievement 2]
3. [Achievement 3]

**Main Issues:**
1. [Issue 1]
2. [Issue 2]
3. [Issue 3]

**Next Month Priorities:**
1. [Priority 1]
2. [Priority 2]
3. [Priority 3]
```

---

#### 2. Inquiry Analysis（询盘分析）

**内容**：
- 询盘总数及趋势
- 询盘来源分布
- 询盘产品分布
- 询盘国家分布
- 高价值询盘分析

**模板**：
```markdown
## Inquiry Analysis

### Total Inquiries from Organic Search
| Period | Inquiries | Change |
|--------|-----------|--------|
| This Month | [X] | [+Y%] |
| Last Month | [Y] | - |
| Same Month Last Year | [Z] | [+/-W%] |

### Inquiry Trend (Last 6 Months)
[Chart: Monthly inquiries trend]

### Inquiry by Product
| Product | Inquiries | % | Change |
|---------|-----------|---|--------|
| Rebar | [X] | [X%] | [+Y%] |
| HRC | [X] | [X%] | [+Y%] |
| Steel Pipe | [X] | [X%] | [+Y%] |
| Other | [X] | [X%] | [+Y%] |

### Inquiry by Country
| Country | Inquiries | % | Change |
|---------|-----------|---|--------|
| Saudi Arabia | [X] | [X%] | [+Y%] |
| Vietnam | [X] | [X%] | [+Y%] |
| Philippines | [X] | [X%] | [+Y%] |
| Other | [X] | [X%] | [+Y%] |

### Top Inquiry Keywords
| Keyword | Inquiries | Intent | Landing Page |
|---------|-----------|--------|--------------|
| [Keyword 1] | [X] | Transactional | [URL] |
| [Keyword 2] | [X] | Transactional | [URL] |
| [Keyword 3] | [X] | Commercial | [URL] |

### Inquiry Quality Analysis
| Intent Type | Inquiries | % | Conversion Rate |
|-------------|-----------|---|-----------------|
| Transactional | [X] | [X%] | [X%] |
| Commercial | [X] | [X%] | [X%] |
| Specification | [X] | [X%] | [X%] |
| Informational | [X] | [X%] | [X%] |
```

---

#### 3. Keyword Rankings（关键词排名）

**内容**：
- 核心关键词排名变化
- 排名提升/下降关键词
- 新进入 Top 10/20 关键词
- 各目标市场排名情况

**模板**：
```markdown
## Keyword Rankings

### Overall Ranking Performance
| Metric | This Month | Last Month | Change |
|--------|------------|------------|--------|
| Avg. Position | [X] | [Y] | [+/-Z] |
| Top 3 Keywords | [X] | [Y] | [+/-Z] |
| Top 10 Keywords | [X] | [Y] | [+/-Z] |
| Top 20 Keywords | [X] | [Y] | [+/-Z] |

### Core Product Keywords
| Keyword | Current | Last Month | Change | Intent |
|---------|---------|------------|--------|--------|
| ASTM A615 rebar | [X] | [Y] | [+/-Z] | Transactional |
| HRC supplier China | [X] | [Y] | [+/-Z] | Transactional |
| seamless pipe ASTM A106 | [X] | [Y] | [+/-Z] | Transactional |

### Ranking Improvements (Top 10)
| Keyword | Current | Last Month | Improvement |
|---------|---------|------------|-------------|
| [Keyword 1] | [X] | [Y] | [+Z] |
| [Keyword 2] | [X] | [Y] | [+Z] |
| [Keyword 3] | [X] | [Y] | [+Z] |

### New Entries (Top 20)
| Keyword | Current | Previous | Landing Page |
|---------|---------|----------|--------------|
| [Keyword 1] | [X] | >50 | [URL] |
| [Keyword 2] | [X] | >50 | [URL] |

### Rankings by Country
| Country | Avg. Position | Top 10 Count | Change |
|---------|---------------|--------------|--------|
| Saudi Arabia | [X] | [Y] | [+/-Z] |
| Vietnam | [X] | [Y] | [+/-Z] |
| Philippines | [X] | [Y] | [+/-Z] |
```

---

#### 4. Traffic Analysis（流量分析）

**内容**：
- 自然搜索流量趋势
- 流量国家分布
- 热门产品页面
- 用户行为指标

**模板**：
```markdown
## Traffic Analysis

### Organic Search Traffic
| Metric | This Month | Last Month | Change |
|--------|------------|------------|--------|
| Sessions | [X] | [Y] | [+Z%] |
| Users | [X] | [Y] | [+Z%] |
| Pageviews | [X] | [Y] | [+Z%] |
| Bounce Rate | [X%] | [Y%] | [+/-Z%] |
| Avg. Session | [X] | [Y] | [+/-Z%] |

### Traffic Trend (Last 6 Months)
[Chart: Monthly sessions trend]

### Traffic by Country
| Country | Sessions | % | Change |
|---------|----------|---|--------|
| Saudi Arabia | [X] | [X%] | [+Y%] |
| Vietnam | [X] | [X%] | [+Y%] |
| Philippines | [X] | [X%] | [+Y%] |
| UAE | [X] | [X%] | [+Y%] |
| Other | [X] | [X%] | [+Y%] |

### Top Product Pages
| Page | Sessions | % of Total | Change | Inquiry Rate |
|------|----------|------------|--------|--------------|
| /product/rebar-astm-a615/ | [X] | [X%] | [+Y%] | [Z%] |
| /product/hrc-hot-rolled-coil/ | [X] | [X%] | [+Y%] | [Z%] |
| /product/seamless-pipe/ | [X] | [X%] | [+Y%] | [Z%] |

### User Behavior Metrics
| Metric | Value | Benchmark | Status |
|--------|-------|-----------|--------|
| Bounce Rate | [X%] | <60% | ✅/⚠️/❌ |
| Avg. Session Duration | [X] | >2:00 | ✅/⚠️/❌ |
| Pages/Session | [X] | >3 | ✅/⚠️/❌ |
| Mobile Traffic % | [X%] | >40% | ✅/⚠️/❌ |
```

---

#### 5. Content & Backlink Progress（内容/外链进展）

**内容**：
- 新增/更新内容
- 内容表现
- 新增外链
- 外链质量

**模板**：
```markdown
## Content & Backlink Progress

### New Content (This Period)
| Type | Title/URL | Publish Date | Sessions | Inquiries |
|------|-----------|--------------|----------|-----------|
| Product Page | [URL] | [Date] | [X] | [Y] |
| Blog Post | [URL] | [Date] | [X] | [Y] |
| Guide | [URL] | [Date] | [X] | [Y] |

### Updated Content
| Page | Update Type | Before Sessions | After Sessions | Change |
|------|-------------|-----------------|----------------|--------|
| [URL] | Spec Update | [X] | [Y] | [+Z%] |
| [URL] | SEO Optimization | [X] | [Y] | [+Z%] |

### Backlink Summary
| Metric | This Month | Last Month | Change |
|--------|------------|------------|--------|
| Total Backlinks | [X] | [Y] | [+Z%] |
| Referring Domains | [X] | [Y] | [+Z%] |
| New Backlinks | [X] | [Y] | [+/-Z] |
| Lost Backlinks | [X] | [Y] | [+/-Z] |

### New Backlinks (Top 10)
| Source | DA | Type | Anchor | URL |
|--------|----|------|--------|-----|
| [Domain 1] | [X] | Directory | [Anchor] | [URL] |
| [Domain 2] | [X] | Guest Post | [Anchor] | [URL] |
| [Domain 3] | [X] | Mention | [Anchor] | [URL] |

### Backlink Quality
| Tier | Count | % | Target |
|------|-------|---|--------|
| Tier 1 (High Value) | [X] | [X%] | >20% |
| Tier 2 (Medium Value) | [X] | [X%] | >50% |
| Tier 3 (Foundation) | [X] | [X%] | <30% |
```

---

#### 6. Technical SEO Status（技术 SEO 状态）

**内容**：
- 技术健康度
- 爬取/索引状态
- 页面速度
- 核心问题

**模板**：
```markdown
## Technical SEO Status

### Overall Health Score
| Metric | Score | Last Month | Change |
|--------|-------|------------|--------|
| Health Score | [X]/100 | [Y] | [+/-Z] |
| Crawl Errors | [X] | [Y] | [+/-Z] |
| Indexed Pages | [X] | [Y] | [+/-Z] |

### Indexing Status
| Status | Count | Change |
|--------|-------|--------|
| Indexed | [X] | [+Y] |
| Excluded | [X] | [+/-Y] |
| Errors | [X] | [+/-Y] |

### Core Web Vitals
| Metric | Mobile | Desktop | Target |
|--------|--------|---------|--------|
| LCP | [X]s | [Y]s | <2.5s |
| FID | [X]ms | [Y]ms | <100ms |
| CLS | [X] | [Y] | <0.1 |

### Page Speed
| Page Type | Avg. Load Time | Target | Status |
|-----------|----------------|--------|--------|
| Homepage | [X]s | <3s | ✅/⚠️/❌ |
| Product Pages | [X]s | <3s | ✅/⚠️/❌ |
| Blog Posts | [X]s | <3s | ✅/⚠️/❌ |

### Critical Issues
| Issue | Severity | Pages Affected | Status |
|-------|----------|----------------|--------|
| [Issue 1] | High/Med/Low | [X] | Open/Fixed |
| [Issue 2] | High/Med/Low | [X] | Open/Fixed |
```

---

#### 7. Next Month Priorities（下月优先级）

**模板**：
```markdown
## Next Month Priorities

### P0 (Critical)
1. **[Task]**: [Description]
   - Impact: [Business impact]
   - Effort: [High/Med/Low]
   - Owner: [Person]
   - Deadline: [Date]

### P1 (Important)
1. **[Task]**: [Description]
   - Impact: [Business impact]
   - Effort: [High/Med/Low]
   - Owner: [Person]
   - Deadline: [Date]

### P2 (Suggestions)
1. **[Task]**: [Description]
   - Impact: [Business impact]
   - Effort: [High/Med/Low]
   - Owner: [Person]
   - Deadline: [Date]

### Content Calendar
| Week | Content Type | Topic | Target Keyword |
|------|--------------|-------|----------------|
| Week 1 | Product Page | [Product] | [Keyword] |
| Week 2 | Blog Post | [Topic] | [Keyword] |
| Week 3 | Guide | [Topic] | [Keyword] |
| Week 4 | Update | [Page] | [Keyword] |
```

---

### 步骤 4: 输出结果

输出格式：

```markdown
# Steel Export SEO Monthly Report

## [Month Year]

---

## Executive Summary

[Summary content as per template above]

---

## 1. Inquiry Analysis

[Inquiry analysis content]

---

## 2. Keyword Rankings

[Keyword rankings content]

---

## 3. Traffic Analysis

[Traffic analysis content]

---

## 4. Content & Backlink Progress

[Content and backlink content]

---

## 5. Technical SEO Status

[Technical SEO content]

---

## 6. Next Month Priorities

[Priorities content]

---

## Appendix

### Data Sources
- Google Analytics 4: [Date Range]
- Google Search Console: [Date Range]
- CRM: [Date Range]
- Ahrefs/Semrush: [Date Range]

### Notes
- [Any specific notes about data quality, methodology, etc.]

---

**Report Generated:** [Date]
**Prepared by:** [Name]
**Next Report:** [Date]
```

## 输出规范

- 必须包含 7 个标准章节
- 核心指标（询盘）必须放在最前面
- 所有数据必须标注来源和周期
- 必须提供同比/环比对比
- 必须提供下月优先级
- 报告必须可执行（有明确行动项）

## 错误处理

- **数据不完整** → 标注缺失数据，使用估算或注明"Data Unavailable"
- **无法访问 Analytics** → 要求用户提供导出数据或使用替代数据源
- **询盘来源无法追踪** → 使用表单提交来源、邮件主题等间接数据
- **历史数据缺失** → 从当前月份开始，建立基线后逐月对比

## 注意事项

- 询盘是核心指标，所有分析围绕询盘展开
- 国家分布必须聚焦目标买家市场（中东/东南亚/非洲/南美）
- 产品页面流量和转化是分析重点
- 技术 SEO 问题必须按优先级排序
- 报告必须可执行，有明确的行动项和负责人
- 报告语言简洁，避免 SEO 术语堆砌

## 参考文档

- `references/kpi-definitions.md` - KPI 定义和计算方法

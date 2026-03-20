# KPI Definitions

## 概述

钢铁外贸 B2B SEO 核心 KPI 定义和计算方法。

---

## Level 1: 核心指标（询盘相关）

### 1. 自然搜索询盘数 (Organic Inquiries)

**定义**：来自有机搜索的询盘数量。

**计算公式**：
```
Organic Inquiries = Count(Conversions where Source = "organic" AND Action = "inquiry")
```

**数据来源**：
- Google Analytics 4: Events > Conversions
- CRM: Inquiry Source = "Organic Search"
- 表单系统: Referrer contains Google/Bing

**目标值**：月增长 10-20%

**注意事项**：
- 需要正确设置转化追踪
- 排除付费搜索（SEM）流量
- 排除直接访问和社交媒体

---

### 2. 询盘转化率 (Inquiry Rate)

**定义**：自然搜索访客中发送询盘的比例。

**计算公式**：
```
Inquiry Rate = (Organic Inquiries / Organic Sessions) × 100%
```

**示例**：
```
Organic Inquiries = 50
Organic Sessions = 2500
Inquiry Rate = (50 / 2500) × 100% = 2%
```

**基准值**：
| 行业 | 平均转化率 | 优秀转化率 |
|------|------------|------------|
| B2B 钢铁 | 0.5-1% | 1-3% |
| B2B 机械 | 0.3-0.8% | 1-2% |
| B2B 化工 | 0.5-1.2% | 1.5-3% |

**优化方向**：
- 优化产品页面规格表
- 改进询盘表单 UX
- 增加信任元素
- 优化 CTA 位置和文案

---

### 3. 询盘关键词分布 (Inquiry Keyword Distribution)

**定义**：带来询盘的关键词列表及其贡献。

**计算方法**：
1. 从 GSC 导出带来转化的查询
2. 从 GA4 查看转化路径中的关键词
3. 从 CRM 追踪询盘来源关键词（如有）

**分析维度**：
| 维度 | 说明 |
|------|------|
| 关键词 | 具体搜索词 |
| 询盘数 | 该关键词带来的询盘数量 |
| 意图类型 | Transactional/Commercial/Specification/Informational |
| 落地页 | 用户访问的页面 |
| 转化率 | 该关键词的询盘转化率 |

**目标**：Top 20 关键词覆盖核心产品

---

### 4. 高价值询盘占比 (High-Value Inquiry Rate)

**定义**：Transactional 意图询盘占总询盘的比例。

**计算公式**：
```
High-Value Rate = (Transactional Inquiries / Total Inquiries) × 100%
```

**意图分类**：
| 意图 | 特征 | 示例关键词 |
|------|------|------------|
| Transactional | 包含 buy/price/supplier/manufacturer | "buy rebar", "steel pipe price" |
| Commercial | 包含 supplier/manufacturer/factory | "steel coil supplier", "HRC manufacturer" |
| Specification | 包含规格/标准/等价 | "ASTM A615 specs", "rebar grades" |
| Informational | 知识性查询 | "what is rebar", "steel types" |

**目标值**：Transactional + Commercial > 70%

---

## Level 2: 过程指标（流量相关）

### 5. 自然搜索会话数 (Organic Sessions)

**定义**：来自有机搜索的网站访问量。

**计算公式**：
```
Organic Sessions = Count(Sessions where Source/Medium = "google / organic")
```

**数据来源**：Google Analytics 4 > Acquisition > Traffic Acquisition

**目标值**：月增长 5-10%

**细分维度**：
- 按国家
- 按设备（桌面/移动）
- 按页面类型
- 按新用户/回访用户

---

### 6. 国家流量分布 (Traffic by Country)

**定义**：各目标市场的流量占比。

**计算公式**：
```
Country % = (Sessions from Country / Total Organic Sessions) × 100%
```

**目标市场优先级**：
| 市场 | 目标占比 | 说明 |
|------|----------|------|
| 中东（沙特、阿联酋） | 25-35% | 核心买家市场 |
| 东南亚（越南、菲律宾、印尼） | 25-35% | 核心买家市场 |
| 非洲（尼日利亚、肯尼亚） | 10-20% | 增长市场 |
| 南美（巴西、智利） | 5-15% | 潜力市场 |
| 其他 | <15% | 非核心市场 |

---

### 7. 关键词排名 (Keyword Rankings)

**定义**：核心关键词在搜索结果中的位置。

**计算方法**：
- 使用 Rank Tracker 工具（Ahrefs, Semrush, SERPWatcher）
- 或使用 GSC 平均排名数据

**关键指标**：
| 指标 | 定义 | 目标 |
|------|------|------|
| Avg. Position | 所有追踪关键词的平均排名 | <15 |
| Top 3 Count | 排名前 3 的关键词数量 | 增长 |
| Top 10 Count | 排名前 10 的关键词数量 | 增长 |
| Top 20 Count | 排名前 20 的关键词数量 | 增长 |

**核心关键词分类**：
| 类别 | 示例 | 优先级 |
|------|------|--------|
| 产品词 | "rebar", "HRC", "seamless pipe" | P0 |
| 产品 + 标准 | "ASTM A615 rebar", "SPHC HRC" | P0 |
| 产品 + 国家 | "rebar Saudi Arabia", "steel pipe Philippines" | P1 |
| 长尾词 | "ASTM A615 Gr60 rebar 12mm price" | P2 |

---

### 8. 新收录页面 (New Indexed Pages)

**定义**：新增被搜索引擎索引的页面数量。

**计算公式**：
```
New Indexed = Indexed Pages (This Month) - Indexed Pages (Last Month)
```

**数据来源**：Google Search Console > Indexing > Pages

**目标值**：月增 10-20 页（产品页 + 内容页）

**页面类型建议**：
| 类型 | 月目标 | 说明 |
|------|--------|------|
| 产品页面 | 5-10 | 核心产品规格页 |
| 分类页面 | 2-5 | 产品类别页 |
| 内容页面 | 3-5 | 博客、指南 |
| 其他 | 0-5 | 应用案例、认证页 |

---

### 9. 新增外链 (New Backlinks)

**定义**：新增的反向链接域名数量。

**计算公式**：
```
New Backlinks = Referring Domains (This Month) - Referring Domains (Last Month)
```

**数据来源**：Ahrefs / Semrush / Moz

**目标值**：月增 5-10 个域名

**外链质量分类**：
| Tier | 目标占比 | 说明 |
|------|----------|------|
| Tier 1 | >20% | 行业权威媒体、协会 |
| Tier 2 | >50% | 行业平台、B2B 目录 |
| Tier 3 | <30% | 论坛、社交媒体 |

---

## Level 3: 辅助指标（内容/技术）

### 10. 产品页流量 (Product Page Traffic)

**定义**：产品页面的访问量占总流量的比例。

**计算公式**：
```
Product Page % = (Product Page Sessions / Total Sessions) × 100%
```

**目标值**：>50%

**优化方向**：
- 增加产品页面数量
- 优化产品页 SEO
- 内部链接导向产品页

---

### 11. 热门产品页 (Top Product Pages)

**定义**：流量最高的产品页面列表。

**分析方法**：
1. GA4 > Pages and Screens
2. 过滤 URL 包含 "/product/"
3. 按 Sessions 排序
4. 取 Top 10-20

**目标**：Top 10 页面覆盖核心产品

---

### 12. 内容更新数 (Content Updates)

**定义**：新增或更新的内容数量。

**分类**：
| 类型 | 月目标 | 说明 |
|------|--------|------|
| 新产品页 | 5-10 | 新增产品规格页 |
| 更新产品页 | 5-10 | 更新现有产品页 |
| 博客文章 | 2-4 | 行业内容 |
| 指南/资源 | 1-2 | 深度内容 |

---

### 13. 技术 SEO 健康度 (Technical Health Score)

**定义**：技术审计的综合得分。

**计算方法**：
- 使用 Audit Tool（Sitebulb, Screaming Frog, Ahrefs Audit）
- 基于错误数量、严重程度计算

**目标值**：>85/100

**关键检查项**：
| 检查项 | 权重 | 目标 |
|--------|------|------|
| 爬取错误 | 30% | 0 错误 |
| 索引问题 | 25% | <5% 页面 |
| 页面速度 | 20% | >80 分 |
| 移动端 | 15% | 100% 友好 |
| 结构化数据 | 10% | 核心页面覆盖 |

---

### 14. 页面速度 (Page Speed)

**定义**：页面加载时间。

**指标**：
| 指标 | 定义 | 目标 |
|------|------|------|
| LCP (Largest Contentful Paint) | 最大内容绘制时间 | <2.5s |
| FID (First Input Delay) | 首次输入延迟 | <100ms |
| CLS (Cumulative Layout Shift) | 累计布局偏移 | <0.1 |

**数据来源**：Google PageSpeed Insights, Chrome UX Report

---

## 报告模板

### 月度 KPI 追踪表

```markdown
## Monthly KPI Dashboard

| KPI | This Month | Last Month | Change | Target | Status |
|-----|------------|------------|--------|--------|--------|
| **Level 1: Inquiry** |
| Organic Inquiries | [X] | [Y] | [+Z%] | [Target] | ✅/⚠️/❌ |
| Inquiry Rate | [X%] | [Y%] | [+/-Z%] | [Target] | ✅/⚠️/❌ |
| High-Value % | [X%] | [Y%] | [+/-Z%] | [Target] | ✅/⚠️/❌ |
| **Level 2: Traffic** |
| Organic Sessions | [X] | [Y] | [+Z%] | [Target] | ✅/⚠️/❌ |
| Top 10 Keywords | [X] | [Y] | [+Z] | [Target] | ✅/⚠️/❌ |
| New Indexed Pages | [X] | [Y] | [+Z] | [Target] | ✅/⚠️/❌ |
| New Backlinks | [X] | [Y] | [+Z] | [Target] | ✅/⚠️/❌ |
| **Level 3: Content/Tech** |
| Product Page % | [X%] | [Y%] | [+/-Z%] | [Target] | ✅/⚠️/❌ |
| Health Score | [X]/100 | [Y]/100 | [+/-Z] | [Target] | ✅/⚠️/❌ |
| Page Speed | [X]s | [Y]s | [+/-Z] | [Target] | ✅/⚠️/❌ |
```

---

## 参考链接

- [Google Analytics 4 Documentation](https://support.google.com/analytics/answer/10089681)
- [Google Search Console Help](https://support.google.com/webmasters/)
- [Core Web Vitals Guide](https://web.dev/vitals/)

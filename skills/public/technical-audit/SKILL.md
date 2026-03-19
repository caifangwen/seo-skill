---
name: technical-audit
version: "1.1.0"
description: |
  执行网站技术 SEO 全面审计。当用户提到技术 SEO 检查、网站爬取问题、
  Core Web Vitals、页面速度、robots.txt、sitemap 配置、
  canonical 标签、结构化数据、移动端适配、HTTPS 问题、
  重定向链、404 错误时必须触发此技能。
  用户说"帮我查一下网站技术问题"或"为什么我的页面没有被收录"也应触发。
compatibility:
  tools: [web_search, web_fetch, bash]
---

# 技术 SEO 审计 Skill

## 概述

对目标网站执行系统化技术 SEO 健康检查，输出按严重程度分级的问题清单
和附带代码示例的修复方案，以及 30/60/90 天修复路线图。

## 前置条件

- [ ] 目标网站 URL（必须）
- [ ] 网站类型（企业官网/电商/博客/SaaS）
- [ ] 当前问题描述或审计目的（可选）
- [ ] 重点审计范围（全面/爬取专项/速度专项）

## 审计深度路由

根据 `SEO_AUDIT_DEPTH` 环境变量或用户指定选择：

- `quick`：仅检查可索引性（robots/sitemap/HTTPS），5 分钟内完成
- `standard`：可索引性 + 技术健康 + 结构化数据
- `full`：全部审计项 + 竞品对比 + 修复路线图

## 核心审计项（按优先级排序）

### P0 — 可索引性（阻断排名的问题）

使用 `scripts/check_robots.py` 和 `scripts/validate_sitemap.py` 执行后，再手动检查：

1. **robots.txt 状态**
   - 是否存在：`GET /robots.txt`
   - 是否误封重要目录（如 `/product/`, `/blog/`）
   - Sitemap 路径是否在 robots.txt 中声明

2. **XML Sitemap**
   - 格式是否有效（`<urlset>` 标签完整）
   - 最后更新时间是否在 7 天内
   - 是否包含所有重要页面

3. **Noindex 使用**
   - 重要页面是否被误加 `noindex`
   - 分页页面的处理是否合理

4. **Canonical 标签**
   - 是否存在自引用 canonical
   - 跨域 canonical 是否正确

### P1 — 技术健康（影响排名和体验）

5. **HTTPS 完整性**（混合内容检查）
6. **移动端适配**（`<meta name="viewport">` / 响应式）
7. **重定向链**（超过 2 跳标记为问题）
8. **Core Web Vitals 参考值**（读取 `references/cwv-thresholds.md`）
   - LCP < 2.5s ✅ / 2.5-4s ⚠️ / >4s ❌
   - CLS < 0.1 ✅ / 0.1-0.25 ⚠️ / >0.25 ❌
   - INP < 200ms ✅ / 200-500ms ⚠️ / >500ms ❌

### P2 — 结构化数据

9. 检查现有 Schema 类型和 JSON-LD 格式
10. 根据网站类型推荐适合的 Schema（参考下表）

| 网站类型 | 推荐 Schema |
|----------|-------------|
| 博客/媒体 | Article, BreadcrumbList, FAQPage |
| 电商 | Product, Review, BreadcrumbList |
| SaaS | SoftwareApplication, FAQPage, HowTo |
| 本地商户 | LocalBusiness, Review |

## 输出格式

```
## 技术 SEO 审计报告：[网站 URL]

**审计时间**：[日期]
**审计深度**：[quick/standard/full]

### 执行摘要
发现 🔴X 个紧急问题 / 🟡X 个优化建议 / 🟢X 项最佳实践

---

### 🔴 紧急修复（影响索引或排名）

#### 问题 1：[问题名称]
- **影响**：[对 SEO 的具体影响]
- **发现**：[具体的问题现象]
- **修复方案**：
  ```[代码或配置示例]```
- **预估工时**：[X 小时]

### 🟡 优化建议

[同上格式]

### 🟢 最佳实践（已通过）

[简单列举通过的检查项]

---

### 修复优先级路线图

| 阶段 | 时间 | 行动项 | 预期收益 |
|------|------|--------|----------|
| 第一阶段 | 第 1-30 天 | [P0 问题] | 恢复索引/排名 |
| 第二阶段 | 第 31-60 天 | [P1 问题] | 提升 CWV 评分 |
| 第三阶段 | 第 61-90 天 | [P2 问题] | 丰富富媒体结果 |
```

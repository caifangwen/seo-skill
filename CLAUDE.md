# SEO Skills 项目

## 项目简介

这是一个专为 SEO 工作流设计的 Claude Code Skill 体系，包含 5 个核心 SEO Skill，
覆盖关键词研究、内容优化、技术审计、外链建设和报告生成的完整工作流。

## 可用 Skill 列表

| Skill 名称 | 路径 | 触发场景 |
|------------|------|----------|
| keyword-research | skills/public/keyword-research/ | 关键词挖掘、搜索意图分析 |
| content-optimizer | skills/public/content-optimizer/ | 文章 SEO 优化、标题改写 |
| technical-audit | skills/public/technical-audit/ | 技术 SEO 诊断、爬取问题排查 |
| link-building | skills/public/link-building/ | 外链策略、竞品外链分析 |
| report-generator | skills/public/report-generator/ | SEO 月报、绩效汇报 |

## 使用规则

1. 执行任何 SEO 相关任务前，**必须先读取对应 SKILL.md**
2. 如果任务涉及多个 Skill，按以下顺序串联：
   - 内容策略类：keyword-research → content-optimizer → report-generator
   - 站点诊断类：technical-audit → report-generator
   - 全站优化类：technical-audit → keyword-research → content-optimizer → report-generator
3. 每次执行完毕，如有明显问题或改进建议，请在对话末尾标注 `[SKILL-FEEDBACK]`

## Skill 冲突处理规则

- 同时匹配 content-optimizer 和 report-generator → 优先 content-optimizer
- 用户明确说"生成报告" → 强制触发 report-generator

## 环境变量（可选）

```bash
SEO_DEFAULT_LOCALE=zh-CN          # 默认语言和地区
SEO_REPORT_FORMAT=markdown         # 报告输出格式：markdown / docx
SEO_AUDIT_DEPTH=full               # 审计深度：quick / standard / full
```

## 版本信息

- 当前版本：v1.2.0
- 最后更新：2026-03-18
- 维护团队：SEO Engineering Team

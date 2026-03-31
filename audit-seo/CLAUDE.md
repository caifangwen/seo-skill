# SEO Skills 项目

## 项目简介

这是一个专为 SEO 工作流设计的 Claude Code Skill 体系，包含：
- **5 个通用 SEO Skill**：适用于一般网站 SEO
- **5 个钢铁外贸专用 Skill**：专为钢铁外贸 B2B 网站设计

覆盖关键词研究、内容优化、技术审计、外链建设和报告生成的完整工作流。

## 可用 Skill 列表

### 通用 SEO Skill

| Skill 名称 | 路径 | 触发场景 |
|------------|------|----------|
| keyword-research | skills/public/keyword-research/ | 关键词挖掘、搜索意图分析（非钢铁行业） |
| content-optimizer | skills/public/content-optimizer/ | 文章 SEO 优化、标题改写（非钢铁行业） |
| technical-audit | skills/public/technical-audit/ | 技术 SEO 诊断、爬取问题排查（非钢铁行业） |
| link-building | skills/public/link-building/ | 外链策略、竞品外链分析（非钢铁行业） |
| report-generator | skills/public/report-generator/ | SEO 月报、绩效汇报（非钢铁行业） |

### 钢铁外贸专用 Skill

| Skill 名称 | 路径 | 触发场景 |
|------------|------|----------|
| steel-keyword-research | skills/private/steel-trade/steel-keyword-research/ | 钢铁产品关键词挖掘、买家国家意图分析、竞品关键词分析 |
| steel-content-optimizer | skills/private/steel-trade/steel-content-optimizer/ | 钢铁产品页面 SEO 优化、规格表优化、询盘转化优化 |
| steel-technical-audit | skills/private/steel-trade/steel-technical-audit/ | 钢铁网站技术 SEO 诊断、多语言配置检查、询盘表单排查 |
| steel-link-building | skills/private/steel-trade/steel-link-building/ | 钢铁行业外链建设、目录提交、外链内容创作 |
| steel-report-generator | skills/private/steel-trade/steel-report-generator/ | 钢铁外贸 SEO 报告生成、询盘分析报告、绩效汇报 |

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
- **钢铁外贸相关查询优先触发 steel-* Skill 而非通用 Skill**

## 优先触发规则（钢铁外贸）

当用户输入包含以下关键词时，**优先触发 steel-* Skill**：

| 关键词类型 | 示例关键词 | 触发 Skill |
|------------|------------|------------|
| 钢铁产品 | rebar, HRC, CRC, steel pipe, galvanized coil, wire rod, I-beam, steel plate | steel-* |
| 钢铁标准 | ASTM A615, SS400, SPHC, DX51D, Q235B, API 5L, GB/T | steel-* |
| 询盘相关 | inquiry, RFQ, quote, buyer, 询盘 | steel-* |
| 买家国家 | Saudi Arabia, Vietnam, Nigeria, Brazil, Middle East, Southeast Asia | steel-* |
| 钢铁行业 | steel industry, B2B steel, steel export, 钢铁，钢材，外贸 | steel-* |

### 触发判断流程

```
1. 用户输入是否包含钢铁产品/标准/行业关键词？
   → 是：触发 steel-* Skill
   → 否：继续判断

2. 用户输入是否包含通用 SEO 关键词？
   → 是：触发通用 Skill
   → 否：询问用户具体需求

3. 用户是否明确指定 Skill 名称？
   → 是：触发指定 Skill
   → 否：根据上下文推断
```

## 环境变量（可选）

```bash
SEO_DEFAULT_LOCALE=zh-CN          # 默认语言和地区
SEO_REPORT_FORMAT=markdown         # 报告输出格式：markdown / docx
SEO_AUDIT_DEPTH=full               # 审计深度：quick / standard / full
```

## 钢铁外贸工作流串联

### 新产品上线工作流

```
steel-keyword-research → steel-content-optimizer → steel-report-generator
```

1. **steel-keyword-research**: 挖掘新产品关键词，分析目标市场
2. **steel-content-optimizer**: 优化产品页面，确保询盘转化
3. **steel-report-generator**: 追踪新产品页面的询盘表现

### 网站优化工作流

```
steel-technical-audit → steel-keyword-research → steel-content-optimizer → steel-link-building → steel-report-generator
```

1. **steel-technical-audit**: 诊断网站技术问题
2. **steel-keyword-research**: 分析关键词机会
3. **steel-content-optimizer**: 优化核心页面
4. **steel-link-building**: 建设行业外链
5. **steel-report-generator**: 生成优化效果报告

### 询盘下降排查工作流

```
steel-technical-audit → steel-content-optimizer → steel-report-generator
```

1. **steel-technical-audit**: 检查询盘表单功能、技术配置
2. **steel-content-optimizer**: 优化询盘转化路径
3. **steel-report-generator**: 分析询盘数据，找出下降原因

## 版本信息

- 当前版本：v1.3.0
- 最后更新：2026-03-20
- 维护团队：SEO Engineering Team
- 新增：钢铁外贸专用 Skill 体系（5 个 Skill）

# SEO Skills

这是一个专为 SEO 工作流设计的 Claude Code Skill 体系，包含 5 个核心 SEO Skill，覆盖关键词研究、内容优化、技术审计、外链建设和报告生成的完整工作流。

---

## 快速开始

### 1. 初始化项目

```bash
# 克隆项目
git clone https://github.com/your-org/seo-skills.git
cd seo-skills

# 或使用初始化脚本
bash scripts/init_project.sh
```

### 2. 在 Claude Code 中打开

```bash
cd seo-skills
claude
```

Claude Code 会自动读取根目录的 `CLAUDE.md`，加载 Skill 注册信息。

### 3. 执行 SEO 任务

在 Claude Code 中输入：

```
请帮我分析以下文章并进行 SEO 优化。
主关键词：[你的关键词]
[粘贴文章内容]
```

Claude Code 会自动：
1. 识别这是内容优化任务
2. 读取 `skills/public/content-optimizer/SKILL.md`
3. 按照 12 项诊断 → 优化输出的流程执行

---

## 可用 Skill 列表

| Skill 名称 | 路径 | 触发场景 |
|------------|------|----------|
| keyword-research | skills/public/keyword-research/ | 关键词挖掘、搜索意图分析 |
| content-optimizer | skills/public/content-optimizer/ | 文章 SEO 优化、标题改写 |
| technical-audit | skills/public/technical-audit/ | 技术 SEO 诊断、爬取问题排查 |
| link-building | skills/public/link-building/ | 外链策略、竞品外链分析 |
| report-generator | skills/public/report-generator/ | SEO 月报、绩效汇报 |

---

## 项目结构

```
seo-skill/
│
├── CLAUDE.md                          ← 项目入口
│
├── skills/
│   ├── public/                        ← 可公开分享的通用 Skill
│   │   ├── keyword-research/
│   │   ├── content-optimizer/
│   │   ├── technical-audit/
│   │   ├── link-building/
│   │   └── report-generator/
│   │
│   └── private/                       ← 团队内部专属 Skill
│       └── brand-guidelines/
│
├── scripts/
│   ├── init_project.sh                ← 一键初始化脚本
│   ├── run_eval.py                    ← 执行单个 Skill 测试
│   ├── run_all_evals.py               ← 执行全套测试
│   └── package_skill.py               ← 打包分发 Skill
│
├── docs/
│   ├── CONTRIBUTING.md                ← 贡献指南
│   ├── SKILL-TEMPLATE.md              ← 新 Skill 模板
│   └── CHANGELOG.md                   ← 版本记录
│
└── .github/workflows/
    └── eval-ci.yml                    ← CI 自动测试
```

---

## 测试

### 运行单个 Skill 测试

```bash
python scripts/run_eval.py \
  --skill content-optimizer \
  --eval-file skills/public/content-optimizer/evals/evals.json
```

### 运行全套测试

```bash
python scripts/run_all_evals.py --verbose
```

### 打包 Skill

```bash
python scripts/package_skill.py --skill keyword-research
```

---

## 文档

- [贡献指南](docs/CONTRIBUTING.md) - 如何新增 Skill
- [Skill 模板](docs/SKILL-TEMPLATE.md) - 创建新 Skill 的模板
- [变更日志](docs/CHANGELOG.md) - 版本历史记录

---

## 环境变量

可选配置：

```bash
SEO_DEFAULT_LOCALE=zh-CN          # 默认语言和地区
SEO_REPORT_FORMAT=markdown         # 报告输出格式：markdown / docx
SEO_AUDIT_DEPTH=full               # 审计深度：quick / standard / full
```

---

## 版本

当前版本：v1.2.0

遵循语义化版本（SemVer）：
- **Patch** (x.x.1): Bug 修复
- **Minor** (x.1.0): 新增功能
- **Major** (2.0.0): 重大变更

---

## 许可证

MIT License

---

## 相关文章

- [项目级 SEO Skill 体系构建指南](../seo-skill-collection/)
- [如何构建 AI Skill 体系](../how-to-build-skill-system/)
- [Anthropic Claude Code 官方文档](https://docs.claude.com)

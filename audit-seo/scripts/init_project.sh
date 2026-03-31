#!/bin/bash

# SEO Skills 项目初始化脚本
# 使用方法：bash scripts/init_project.sh [项目名称]

set -e

PROJECT_NAME=${1:-"seo-skills"}
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PARENT_DIR="$(dirname "$SCRIPT_DIR")"
TARGET_PATH="$PARENT_DIR/$PROJECT_NAME"

echo "🚀 初始化 SEO Skill 项目：$PROJECT_NAME"
echo "📁 目标路径：$TARGET_PATH"
echo ""

# 创建完整目录结构
echo "📂 创建目录结构..."
mkdir -p "$TARGET_PATH"/{skills/public/{keyword-research,content-optimizer,technical-audit,link-building,report-generator}/{references,evals/files,scripts,assets},skills/private/brand-guidelines/references,scripts,docs,.github/workflows}

# 创建占位文件
SKILLS=("keyword-research" "content-optimizer" "technical-audit" "link-building" "report-generator")

for skill in "${SKILLS[@]}"; do
  touch "$TARGET_PATH/skills/public/$skill/SKILL.md"
  touch "$TARGET_PATH/skills/public/$skill/evals/evals.json"
  touch "$TARGET_PATH/skills/public/$skill/evals/trigger_evals.json"
  echo "  ✅ 创建 $skill Skill 目录"
done

# 创建 private skills
touch "$TARGET_PATH/skills/private/brand-guidelines/SKILL.md"
echo "  ✅ 创建 brand-guidelines Skill (private)"

# 创建 CLAUDE.md
cat > "$TARGET_PATH/CLAUDE.md" << 'EOF'
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
EOF

echo "  ✅ 创建 CLAUDE.md"

# 创建 .gitignore
cat > "$TARGET_PATH/.gitignore" << 'EOF'
# 私人 Skill（不公开）
skills/private/

# 环境配置
*.env
.env.local

# 系统文件
.DS_Store
Thumbs.db

# Python
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
pip-log.txt
pip-delete-this-directory.txt

# 测试结果
grading_results/
eval_results/
*.log

# IDE
.vscode/
.idea/
*.swp
*.swo
*~
EOF

echo "  ✅ 创建 .gitignore"

# 创建 README.md
cat > "$TARGET_PATH/README.md" << 'EOF'
# SEO Skills

这是一个专为 SEO 工作流设计的 Claude Code Skill 体系。

## 快速开始

1. 在 Claude Code 中打开此项目
2. Claude Code 会自动读取 CLAUDE.md
3. 执行 SEO 任务时会自动触发对应 Skill

## 文档

- [贡献指南](docs/CONTRIBUTING.md)
- [Skill 模板](docs/SKILL-TEMPLATE.md)
- [变更日志](docs/CHANGELOG.md)

## 许可证

MIT
EOF

echo "  ✅ 创建 README.md"

echo ""
echo "✅ 项目初始化完成！"
echo ""
echo "📂 目录结构："
find "$TARGET_PATH" -type f | sort | head -30
echo ""
echo "📝 下一步："
echo "  1. 将各 SKILL.md 模板内容填入对应文件"
echo "  2. 配置 CLAUDE.md 项目入口"
echo "  3. 编写 evals/evals.json 测试用例"
echo "  4. 运行 python scripts/run_all_evals.py 验证"
echo ""

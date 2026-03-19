# 变更日志

本文档记录 SEO Skills 项目的所有重要变更。

---

## [1.2.0] - 2026-03-18

### Added

- **新项目初始化**
  - 完整的 SEO Skill 体系目录结构
  - CLAUDE.md 项目入口配置
  - 5 个核心 SEO Skill（keyword-research, content-optimizer, technical-audit, link-building, report-generator）
  - 1 个内部 Skill（brand-guidelines）

- **参考文档**
  - keyword-research: intent-taxonomy.md, keyword-difficulty-guide.md
  - content-optimizer: on-page-checklist.md, title-tag-formulas.md
  - technical-audit: cwv-thresholds.md, redirect-rules.md
  - link-building: outreach-templates.md, link-quality-criteria.md
  - report-generator: report-template.md
  - brand-guidelines: brand-seo-rules.md

- **脚本工具**
  - scripts/init_project.sh - 项目初始化脚本
  - scripts/run_eval.py - 单个 Skill 测试执行
  - scripts/run_all_evals.py - 全套测试执行
  - scripts/package_skill.py - Skill 打包分发

- **文档**
  - docs/CONTRIBUTING.md - 贡献指南
  - docs/SKILL-TEMPLATE.md - Skill 模板
  - docs/CHANGELOG.md - 变更日志（本文档）

- **测试体系**
  - 每个 Skill 包含 evals/evals.json（功能测试）
  - 每个 Skill 包含 evals/trigger_evals.json（触发准确性测试）
  - 测试样本文件（sample-article-1.md, sample-article-2.md）

- **CI/CD**
  - .github/workflows/eval-ci.yml - GitHub Actions 自动测试配置

### Changed

- 无（初始版本）

### Fixed

- 无（初始版本）

---

## 版本说明

### 语义化版本规则

| 版本类型 | 格式 | 说明 |
|----------|------|------|
| Major | X.0.0 | 重大变更，可能不向后兼容 |
| Minor | 1.X.0 | 新增功能，向后兼容 |
| Patch | 1.0.X | Bug 修复，向后兼容 |

### 发布周期

- **Patch**: 随时发布（Bug 修复）
- **Minor**: 每月发布（新功能）
- **Major**: 按需发布（重大重构）

---

## 历史版本

### [1.0.0] - 2026-03-01

- 项目启动
- 设计 Skill 体系架构
- 确定目录结构和文件规范

---

## 贡献者

感谢所有为这个项目做出贡献的人！

- [你的名字] - 初始工作

---

**格式参考：** [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)

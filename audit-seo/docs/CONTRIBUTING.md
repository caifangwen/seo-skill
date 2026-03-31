# 贡献指南

欢迎为 SEO Skills 项目做出贡献！本文档将指导您完成贡献流程。

---

## 目录

1. [新增 Skill 流程](#新增-skill-流程)
2. [Skill 版本管理](#skill-版本管理)
3. [PR 检查清单](#pr-检查清单)
4. [测试规范](#测试规范)
5. [代码风格](#代码风格)

---

## 新增 Skill 流程

### 步骤 1：复制模板

```bash
cp docs/SKILL-TEMPLATE.md skills/public/<新 skill 名>/SKILL.md
```

### 步骤 2：填写 SKILL.md

必须填写的字段：
- `name`: Skill 名称（英文，小写，连字符分隔）
- `version`: 版本号（语义化版本，如 "1.0.0"）
- `description`: 触发描述（**重要**，决定 AI 何时触发此 Skill）
- `compatibility.tools`: 需要的工具权限

### 步骤 3：创建参考文档

在 `references/` 目录下创建 Skill 所需的参考文档：
- 行业标准/规范
- 检查清单
- 模板/公式
- 最佳实践

### 步骤 4：编写测试用例

创建 `evals/evals.json`：
- 至少 5 个功能测试用例
- 覆盖正常场景和边界情况
- 包含触发准确性测试

创建 `evals/trigger_evals.json`：
- 正例（应触发）≥ 6 个
- 负例（不应触发）≥ 4 个

### 步骤 5：本地测试

```bash
# 测试单个 Skill
python scripts/run_eval.py --skill <skill 名> --eval-file skills/public/<skill 名>/evals/evals.json

# 测试全部 Skill
python scripts/run_all_evals.py --verbose
```

### 步骤 6：提交 PR

确认以下项目后提交：
- [ ] SKILL.md 内容完整
- [ ] 测试用例覆盖充分
- [ ] 本地测试通过率 ≥ 80%
- [ ] 文档无敏感信息

---

## Skill 版本管理

遵循语义化版本（SemVer）：`MAJOR.MINOR.PATCH`

### 版本升级规则

| 变更类型 | 版本升级 | 示例 |
|----------|----------|------|
| 修复错误/措辞优化 | Patch | 1.0.0 → 1.0.1 |
| 新增步骤/功能 | Minor | 1.0.0 → 1.1.0 |
| 重构工作流/输出格式 | Major | 1.0.0 → 2.0.0 |

### 更新 CHANGELOG.md

每次 PR 必须更新 `docs/CHANGELOG.md`：

```markdown
## [1.1.0] - 2026-03-18

### Added
- content-optimizer: 新增 FAQ Schema 建议功能

### Changed
- keyword-research: 优化意图分类流程

### Fixed
- technical-audit: 修复 sitemap 验证脚本的日期解析问题
```

---

## PR 检查清单

提交 PR 前请确认：

### 文档
- [ ] SKILL.md 的 `version` 字段已更新
- [ ] CHANGELOG.md 已记录变更内容
- [ ] description 中无敏感信息或内部业务细节

### 测试
- [ ] evals.json 覆盖新功能的测试用例
- [ ] 本地 `pass_rate` ≥ 0.80
- [ ] 触发测试准确率 ≥ 0.85

### 代码（如有脚本）
- [ ] 脚本有 shebang (`#!/usr/bin/env python3`)
- [ ] 脚本有使用说明
- [ ] 错误处理完善

---

## 测试规范

### 功能测试用例格式

```json
{
  "id": 1,
  "description": "测试描述",
  "prompt": "用户输入",
  "files": ["evals/files/sample.md"],
  "expectations": [
    "期望 1",
    "期望 2",
    "期望 3"
  ]
}
```

### 触发测试用例格式

```json
{
  "prompt": "用户输入",
  "should_trigger": true
}
```

### 通过率计算

```
通过率 = 通过的测试用例数 / 总测试用例数

目标：≥ 0.80 (80%)
```

### Benchmark 测试

对比有 Skill vs 无 Skill 的输出质量：

```bash
python scripts/run_all_evals.py --benchmark --verbose
```

---

## 代码风格

### Python 脚本

- 使用 `black` 格式化代码
- 遵循 PEP 8 规范
- 函数/类必须有 docstring

### Markdown 文档

- 标题使用 ATX 风格（`#`）
- 列表使用 `-` 而非 `*`
- 代码块指定语言

### 命名规范

- 目录/文件：小写，连字符分隔（`keyword-research`）
- Python 变量：蛇形命名（`skill_name`）
- 常量：大写蛇形命名（`SEO_DEFAULT_LOCALE`）

---

## 发布流程

### 准备发布

1. 更新所有 Skill 的版本号
2. 更新 CLAUDE.md 中的版本信息
3. 更新 README.md
4. 运行完整测试套件

### 打标签

```bash
git tag -a v1.2.0 -m "Release v1.2.0"
git push origin v1.2.0
```

### 打包分发

```bash
# 打包所有 public skills
for skill in skills/public/*/; do
  python scripts/package_skill.py --skill $(basename $skill)
done
```

---

## 问题反馈

如发现问题或有改进建议，请：
1. 搜索现有 issue，避免重复
2. 创建新 issue，详细描述问题
3. 如可能，提供复现步骤

---

## 联系方式

- 项目维护者：[联系方式]
- 讨论区：[链接]

---

感谢你的贡献！🎉

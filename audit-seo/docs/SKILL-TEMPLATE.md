# Skill 模板

复制此模板作为新 Skill 的起点。

---

## SKILL.md 模板

```markdown
---
name: <skill-name>
version: "1.0.0"
description: |
  <触发描述：详细说明何时应触发此 Skill>
  <包括用户可能使用的关键词和场景>
  <这是最重要的部分，决定 AI 是否正确触发>
compatibility:
  tools: [web_search, web_fetch, bash]  # 根据需要的工具权限选择
---

# <Skill 名称>

## 概述

<用 2-3 句话描述此 Skill 的用途和价值>

## 前置条件

开始前必须获取的信息：
- [ ] <必需信息 1>
- [ ] <必需信息 2>
- [ ] <可选信息>

如信息不完整，必须先向用户询问，不得跳过。

## 核心工作流

### 步骤 1：<步骤名称>

<详细描述此步骤的操作>

**关键点：**
- <要点 1>
- <要点 2>

### 步骤 2：<步骤名称>

<详细描述此步骤的操作>

### 步骤 3：<步骤名称>

<详细描述此步骤的操作>

### 步骤 N：输出结果

输出格式：

```
<输出模板>
```

## 输出规范

- <规范 1>
- <规范 2>
- <规范 3>

## 错误处理

- <错误场景 1> → <处理方式>
- <错误场景 2> → <处理方式>

## 注意事项

- <注意 1>
- <注意 2>
- <注意 3>
```

---

## 参考文档模板

### references/<主题>.md

```markdown
# <主题>

## 概述

<简要介绍>

## 标准/规范

| 项目 | 标准 | 说明 |
|------|------|------|
| | | |

## 最佳实践

- <实践 1>
- <实践 2>

## 示例

<代码示例或案例>

## 参考链接

- [链接 1](url)
- [链接 2](url)
```

---

## 测试用例模板

### evals/evals.json

```json
{
  "skill_name": "<skill-name>",
  "version": "1.0.0",
  "evals": [
    {
      "id": 1,
      "description": "测试描述",
      "prompt": "用户输入",
      "files": ["evals/files/sample.md"],
      "expectations": [
        "期望检查点 1",
        "期望检查点 2",
        "期望检查点 3"
      ]
    }
  ]
}
```

### evals/trigger_evals.json

```json
{
  "skill_name": "<skill-name>",
  "description": "测试触发描述的准确性",
  "evals": [
    { "prompt": "应触发的用户输入 1", "should_trigger": true },
    { "prompt": "应触发的用户输入 2", "should_trigger": true },
    { "prompt": "应触发的用户输入 3", "should_trigger": true },
    { "prompt": "不应触发的用户输入 1", "should_trigger": false },
    { "prompt": "不应触发的用户输入 2", "should_trigger": false }
  ]
}
```

---

## 检查清单

创建新 Skill 时请确认：

- [ ] SKILL.md 包含完整的 frontmatter（name, version, description, compatibility）
- [ ] description 详细描述了触发场景
- [ ] 核心工作流包含至少 3 个步骤
- [ ] 有明确的输出格式模板
- [ ] 包含错误处理说明
- [ ] 创建了必要的参考文档
- [ ] 编写了至少 5 个功能测试用例
- [ ] 编写了触发准确性测试（正例≥6，负例≥4）
- [ ] 本地测试通过率 ≥ 80%

---

## 示例参考

参考以下已完成的 Skill 作为示例：
- `skills/public/keyword-research/SKILL.md`
- `skills/public/content-optimizer/SKILL.md`
- `skills/public/technical-audit/SKILL.md`

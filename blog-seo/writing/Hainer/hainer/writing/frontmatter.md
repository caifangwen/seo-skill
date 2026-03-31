# SKILL-01: Front Matter 生成器

**用途**: 生成文章开头的 YAML Front Matter
**输入**: 文章标题、日期、分类

---

## 输出格式

```markdown
---
title: "文章标题"
date: YYYY-MM-DD
categories:
  - "分类名称"
coverImage: "文章标题.jpg"
---
```

---

## 分类选项

| 分类名 | 适用内容 |
|-------|---------|
| `flanges` | 法兰产品、法兰类型、法兰标准 |
| `valves` | 阀门产品、阀门类型、阀门应用 |
| `pipe-fittings` | 管件产品、管件类型、管件连接 |
| `pipes` | 管道产品、管道规格、管道标准 |
| `industry-knowledge` | 行业知识、标准解读、选型指南 |
| `other` | 其他内容 |

---

## 日期规范

```
✅ 正确：date: 2026-03-23（使用当前年份）
❌ 错误：date: 2024-03-23（过时）
```

Title 中如包含年份，应使用 **2026**。

---

## 标题转换规则（coverImage 文件名）

- 空格 → `-`
- 特殊字符删除
- 首字母大写

```
输入标题：How to Choose the Right Flange Class for Your Pipeline
输出 coverImage: How-to-Choose-the-Right-Flange-Class-for-Your-Pipeline.jpg
```

---

**下一步** → `writing/intro.md`

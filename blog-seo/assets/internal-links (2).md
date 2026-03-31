# SKILL-07: 内部链接植入

**用途**: 在文章中自然植入内部链接  
**适用**: 所有文章类型（横切关注点）

---

## 链接密度规则

- 每 300-400 字至少 1 个内部链接
- 开篇 2 段必须有 1-2 个链接
- 每个主要章节至少 1 个链接

---

## 链接格式

```markdown
[链接文字](https://leeknives.com/页面路径/)
```

---

## 常用链接类型

| 类型 | 示例 URL |
|-----|---------|
| 钢材页面 | `https://leeknives.com/d2-steel/` |
| 分类页面 | `https://leeknives.com/best-steel-for-kitchen-knives/` |
| 知识页面 | `https://leeknives.com/rockwell-hardness-scale/` |
| 联系页面 | `https://leeknives.com/request-a-quote/` |
| 产品页面 | `https://leeknives.com/folding-knife-lkfdk10015/` |

---

## 锚文本规范

```
✅ 正确: [VG-10 is better suited for home cooks](https://leeknives.com/vg-10-steel/)
❌ 错误: [点击这里](https://leeknives.com/vg-10-steel/)
❌ 错误: [here](https://leeknives.com/vg-10-steel/)
```

规则：锚文本必须是描述性关键词，不使用"click here"或"here"之类的无意义文字。

---

## 自然植入示例

```markdown
Among the stainless steel used for making kitchen knives, ZDP-189 has one of the worst
[corrosion resistance](https://leeknives.com/best-stainless-steel-for-knives/).

Japanese chefs that utilize [these types of knives](https://leeknives.com/japanese-kitchen-knives/)
are familiar with carbon steels.

The knives made from this steel can last for years without showing imminent signs of aging,
making them a great choice for [wholesale buyers](https://leeknives.com/request-a-quote/).
```

---

## 内部链接网络建议

在文章中优先链接以下高价值页面：

1. `/request-a-quote/` — 每篇文章结尾必须出现
2. 相关钢材对比页面 — 同类文章互链
3. 同一类别的最佳推荐页面 — 引导深度浏览
4. 产品分类页面 — 导流到商品

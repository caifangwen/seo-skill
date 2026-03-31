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
[链接文字](https://example.com/页面路径/)
```

---

## 链接类型

| 类型 | 示例 URL |
|-----|---------|
| 产品页面 | `https://example.com/stainless-steel-flanges/` |
| 分类页面 | `https://example.com/flange-types/` |
| 知识页面 | `https://example.com/asme-b16-5-standard/` |
| 联系页面 | `https://example.com/request-a-quote/` |
| 选型指南 | `https://example.com/valve-selection-guide/` |

---

## 锚文本规范

```
✅ 正确：[316 stainless steel flanges](https://example.com/316-stainless-flanges/)
❌ 错误：[点击这里](https://example.com/316-stainless-flanges/)
❌ 错误：[here](https://example.com/316-stainless-flanges/)
```

规则：锚文本必须是描述性关键词，不使用"click here"或"here"之类的无意义文字。

---

## 自然植入示例

```markdown
Among the various flange materials available, [stainless steel 316](https://example.com/316-stainless-flanges/) offers superior corrosion resistance in chloride environments.

The [ASME B16.5 standard](https://example.com/asme-b16-5-guide/) defines pressure-temperature ratings for steel flanges from Class 150 to Class 2500.

For projects requiring certified components, [API 6D valves](https://example.com/api-6d-valves/) provide reliable performance in pipeline applications.

When selecting flanges for high-pressure systems, consider the [pressure rating chart](https://example.com/flange-pressure-ratings/) to ensure safe operation.

For bulk orders and OEM requirements, [request a quote](https://example.com/request-a-quote/) from our sales team.
```

---

## 内部链接网络建议

在文章中优先链接以下高价值页面：

1. `/request-a-quote/` — 每篇文章结尾必须出现
2. 相关产品分类页面 — 法兰/阀门/管件分类页
3. 技术标准解读页面 — ASME/API/ASTM 标准说明
4. 选型指南页面 — 帮助客户选择合适产品
5. 材质说明页面 — 不锈钢/碳钢/合金钢对比

---

## 法兰/阀门/管件文章链接策略

| 文章主题 | 应链接的相关页面 |
|---------|-----------------|
| 法兰压力等级 | 法兰类型、材质选择、尺寸表 |
| 阀门选型指南 | 阀门类型对比、执行器选型、应用案例 |
| 不锈钢管件 | 304 vs 316 对比、耐腐蚀性说明、行业应用 |
| 安装指南 | 工具推荐、质检流程、常见问题 |
| 材质对比 | 各材质详情页、价格分析、应用建议 |

---

## CTA 链接位置

```markdown
## 文中 CTA（长文章插入）

Looking for reliable [产品] suppliers? [Request a free quote](https://example.com/request-a-quote/) for your project.

## 结尾 CTA

[公司名] supplies certified [产品类别] to industries worldwide. [Contact us today](https://example.com/request-a-quote/) for competitive pricing and fast delivery.
```

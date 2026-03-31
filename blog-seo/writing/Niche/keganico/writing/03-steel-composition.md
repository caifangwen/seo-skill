# SKILL-03: 钢材成分列表生成

**用途**: 生成钢材化学成分列表

---

## 结构模板

```markdown
## Chemical Composition of [钢材名]

<figure>

| Element | % | Role |
| --- | --- | --- |
| Carbon (C) | X% | Base hardness contributor |
| Chromium (Cr) | X% | Forms passive oxide layer; exceeds 13% stainless threshold |
| **Nitrogen (N)** | **X%** | **Core innovation: refines grains, boosts corrosion resistance** |
| Manganese (Mn) | X% | Stabilizes smelting process |
| Vanadium (V) | X% | Wear resistance and tool life |
| Molybdenum (Mo) | X% | Enhances toughness and strength |

<figcaption>

_Data source: [来源名称](链接)_

</figcaption>

</figure>

[钢材名] doesn't chase "ultra-high hardness" but instead "**[核心理念].**"
This [关键元素] not only [作用 1] but also [作用 2]. This sophisticated formula
allows [钢材名] to achieve better overall performance while maintaining [优势].
```

---

## 常见元素顺序 (按重要性)

1. Carbon (C) - 硬度基础
2. Chromium (Cr) - 耐腐蚀性
3. Vanadium (V) - 耐磨性
4. Nitrogen (N) - 晶粒细化
5. Molybdenum (Mo) - 韧性
6. Manganese (Mn) - 稳定性
7. Silicon (Si) - 脱氧
8. 其他 (Nickel, Cobalt, Niobium 等)

---

## 示例 (14C28N)

```markdown
## Chemical Composition of 14C28N

<figure>

| Element | % | Role |
| --- | --- | --- |
| Carbon (C) | 0.62% | Base hardness contributor |
| Chromium (Cr) | 14.00% | Forms passive oxide layer; exceeds 13% stainless threshold |
| **Nitrogen (N)** | **0.11%** | **Core innovation: refines grains, boosts corrosion resistance** |
| Manganese (Mn) | 0.6% | Stabilizes smelting process |
| Silicon (Si) | 0.2% | Deoxidization |

<figcaption>

_Data source: [Alleima technical datasheet](https://www.alleima.com/en/technical-center/material-datasheets/strip-steel/alleima-14c28n/)_

</figcaption>

</figure>

14C28N doesn't chase "ultra-high hardness" but instead "**substitutes nitrogen
for some carbon.**" This 0.11% nitrogen not only refines the grain structure
(making edges easier to sharpen) but also forms nitrides, further enhancing
hardness and corrosion resistance.
```

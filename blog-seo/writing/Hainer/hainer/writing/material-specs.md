# SKILL-03 + SKILL-04: 材料规格与属性详解

**用途**: 生成材料化学成分/机械性能列表（SKILL-03）及各项属性详解（SKILL-04）
**适用**: 产品评测文章、材料对比文章、法兰/阀门/管件详解文章

---

## SKILL-03: 材料规格列表

### 结构模板（法兰/阀门 - 材质标准）

```markdown
## [产品名] Material Specifications

### Material Grade

- **Standard**: ASTM / ASME / DIN / JIS
- **Grade**: [等级，如 A105, F304, F316]
- **Type**: [类型，如 Carbon Steel, Stainless Steel, Alloy Steel]

### Chemical Composition

- **Carbon (C)**: X%
- **Manganese (Mn)**: X%
- **Silicon (Si)**: X%
- **Chromium (Cr)**: X%
- **Nickel (Ni)**: X%
- **Molybdenum (Mo)**: X%
- **Phosphorus (P)**: X% max
- **Sulfur (S)**: X% max

### Mechanical Properties

- **Tensile Strength**: XXX MPa (XX ksi) min
- **Yield Strength**: XXX MPa (XX ksi) min
- **Elongation**: XX% min
- **Hardness**: XXX HB max
```

### 常见材质标准

| 标准号 | 材料类型 | 典型应用 |
|-------|---------|---------|
| ASTM A105 | 碳钢锻件 | 常温法兰、阀门 |
| ASTM A182 F304 | 304 不锈钢 | 腐蚀性介质 |
| ASTM A182 F316 | 316 不锈钢 | 海洋环境、化工 |
| ASTM A234 WPB | 碳钢对焊管件 | 一般管道连接 |
| ASTM A403 WP304 | 不锈钢对焊管件 | 食品级管道 |
| ASTM A350 LF2 | 低温碳钢 | 低温工况 |

### 示例（A105 法兰）

```markdown
## ASTM A105 Flange Material Specifications

### Chemical Composition

- **Carbon (C)**: 0.35% max
- **Manganese (Mn)**: 0.60-1.05%
- **Silicon (Si)**: 0.10-0.35%
- **Phosphorus (P)**: 0.035% max
- **Sulfur (S)**: 0.040% max
- **Copper (Cu)**: 0.40% max
- **Nickel (Ni)**: 0.40% max
- **Chromium (Cr)**: 0.30% max
- **Molybdenum (Mo)**: 0.12% max

### Mechanical Properties

- **Tensile Strength**: 485 MPa (70 ksi) min
- **Yield Strength**: 250 MPa (36 ksi) min
- **Elongation**: 22% min
- **Reduction of Area**: 35% min
- **Hardness**: 187 HB max
```

---

## SKILL-04: 产品属性详解

### 标准章节顺序（法兰）

```markdown
## [产品名] Key Properties

### Pressure Rating
### Temperature Range
### Corrosion Resistance
### Weldability
### Machinability
### Dimensional Standards
```

### 标准章节顺序（阀门）

```markdown
## [产品名] Key Properties

### Pressure Class
### Temperature Range
### Flow Characteristics
### Leakage Rate
### Actuation Options
### Material Compatibility
```

### 每节结构

```markdown
### [属性名]

![相关图片](https://img.example.com/wp-content/uploads/YYYY/MM/图片名.jpg)

[属性定义/说明]（1 句）

[具体数值/表现]（1-2 句）

[适用标准]（1 句）

[与同类对比]（1-2 句）

[使用建议]（1 句）
```

---

## 各属性常用表达

**压力等级（Pressure Rating）**:
```
- "The [产品] is available in pressure classes ranging from Class 150 to Class 2500."
- "According to ASME B16.5, the maximum working pressure for Class 150 at ambient temperature is 285 psi."
- "PN16 flanges are rated for 16 bar working pressure at temperatures up to 120°C."
```

**温度范围（Temperature Range）**:
```
- "[产品] can operate in temperatures ranging from -20°F to 800°F (-29°C to 427°C)."
- "For low-temperature applications down to -50°F, ASTM A350 LF2 material is recommended."
- "High-temperature service requires materials like ASTM A182 F11 or F22."
```

**耐腐蚀性（Corrosion Resistance）**:
```
- "[产品] performs well in corrosive environments due to the chromium content."
- "316 stainless steel offers superior corrosion resistance compared to 304, especially in chloride environments."
- "Carbon steel flanges should be coated or painted for outdoor applications."
```

**连接方式（Connection Type）**:
```
- "Weld Neck flanges provide the strongest connection for high-pressure applications."
- "Threaded flanges are ideal for low-pressure systems where welding is not feasible."
- "Slip-On flanges offer easier alignment and lower installation costs."
```

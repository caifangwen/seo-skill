# SKILL-06: 图片插入规范

**用途**: 规范图片插入位置和格式

---

## 图片密度规则

```
✅ 每 400-500 字至少 1 张图片
✅ 每个主要章节 (##) 至少 1 张
✅ 开篇后第 1 个章节必须有图片
✅ 对比表格前后各 1 张
✅ 结论前可有 1 张总结性图片
```

---

## 图片格式

### 基础格式

```markdown
![描述文字](https://keganico.com/wp-content/uploads/YYYY/MM/图片名称.jpg)
```

### Figure 格式 (用于产品展示)

```markdown
<figure>

[![产品图片](https://keganico.com/wp-content/uploads/YYYY/MM/图片.jpg)](https://keganico.com/产品链接/)

<figcaption>

[产品名称](https://keganico.com/产品链接/)

</figcaption>

</figure>
```

### 带数据来源的图片说明

```markdown
<figure>

![图片](https://keganico.com/wp-content/uploads/YYYY/MM/图片.jpg)

<figcaption>

_Data source: [来源名称](链接)_

</figcaption>

</figure>
```

---

## 图片命名规范

```
✅ 正确:
- performance-scorecard-magnacut-vs-s30v.jpg
- chemical-comparison-14c28n-vs-d2.jpg
- civivi-knives-overview.jpg
- oem-fixed-blade-knife-g10-handle.jpg

❌ 错误:
- DSC_2847.JPG (无意义)
- 图片 1.jpg (无描述)
- magnacut-vs-s30v-performance-scorecard-head-to-head-ratings-comparison-chart-final.jpg (过长)
```

---

## 图片来源优先级

```
第 1 优先：网站现有本地资源 (output/images/[文章目录]/ 中已使用的图片)
第 2 优先：从网络获取并下载到本地 (Unsplash, Pexels 等)
第 3 优先：外部可信赖来源 (Wikimedia, 品牌官网)
```

---

## 文章与图片目录结构

```
output/
├── posts/                    # 文章文件目录
│   └── [文章名称].md         # 文章 Markdown 文件
│
└── images/                   # 图片文件目录
    └── [文章名称]/
        ├── image-1.jpg       # 图片 1
        ├── image-2.jpg       # 图片 2
        └── image-3.jpg       # 图片 3

示例:
output/
├── posts/
│   └── s30v-steel-review.md
│
└── images/
    └── s30v/
        ├── steel-metal-texture-1.jpg
        ├── knife-sharpening-whetstone-1.jpg
        └── outdoor-camping-knife-1.jpg
```

---

## 图片路径引用

```markdown
# 文章中的图片引用格式（相对路径）
# 从 posts/ 引用 images/ 中的图片

![描述文字](../images/[文章简称]/图片名.jpg)

示例:
![CPM S30V Steel Microstructure](../images/s30v/steel-metal-texture-1.jpg)
![Knife Sharpening](../images/s30v/knife-sharpening-whetstone-1.jpg)
```

---

## 图片使用示例

### 钢材性能图

```markdown
![Performance Scorecard MagnaCut vs S30V](https://keganico.com/wp-content/uploads/2026/01/Performance-Scorecard-MagnaCut-vs-S30V.jpg)
```

### 产品展示图

```markdown
<figure>

![OEM Fixed Blade Knife G10 Handle](https://keganico.com/wp-content/uploads/2025/10/OEM-Fixed-Blade-Knife-G10-Handle-3.74-Inch-S30V-Blade-KKFB00012.jpg)

<figcaption>

[OEM Fixed Blade Knife G10 Handle (3.74 Inch S30V Blade) KKFB00012](https://keganico.com/product/fixed-blade-kkfb00012/)

</figcaption>

</figure>
```

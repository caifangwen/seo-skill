# Keganico 图片资源使用规范

> 基于 keganico.com 现有文章图片使用习惯制定的规范

---

## 📊 图片使用概览

### 图片密度标准

| 文章类型 | 字数范围 | 图片数量 | 密度 |
|---------|---------|---------|------|
| 钢材评测 | 2500-3500 | 6-8 张 | 每 400 字 1 张 |
| 钢材对比 | 3000-4000 | 8-10 张 | 每 400 字 1 张 |
| 刀具知识 | 2000-3000 | 5-7 张 | 每 400 字 1 张 |
| 品牌评测 | 3500-5000 | 10-15 张 | 每 350 字 1 张 |
| 材料对比 | 2000-3000 | 5-8 张 | 每 400 字 1 张 |

### 图片位置规范

```
文章结构图片分布:

开篇后 → 第 1 个 H2 章节 (必须有图)
每 2-3 个 H2 → 1 张配图
对比表格 → 前后各 1 张
产品展示 → Figure 格式带链接
结论前 → 1 张总结性图片 (可选)
```

---

## 🖼️ 图片格式规范

### 基础图片格式

```markdown
![描述文字](https://keganico.com/wp-content/uploads/YYYY/MM/图片名称.jpg)
```

**示例**:
```markdown
![Performance Scorecard MagnaCut vs S30V](https://keganico.com/wp-content/uploads/2026/01/Performance-Scorecard-MagnaCut-vs-S30V.jpg)
```

### Figure 格式 (产品展示)

```markdown
<figure>

[![产品图片](https://keganico.com/wp-content/uploads/YYYY/MM/图片.jpg)](https://keganico.com/产品链接/)

<figcaption>

[产品名称](https://keganico.com/产品链接/)

</figcaption>

</figure>
```

**示例**:
```markdown
<figure>

![OEM Fixed Blade Knife G10 Handle](https://keganico.com/wp-content/uploads/2025/10/OEM-Fixed-Blade-Knife-G10-Handle-3.74-Inch-S30V-Blade-KKFB00012.jpg)

<figcaption>

[OEM Fixed Blade Knife G10 Handle (3.74 Inch S30V Blade) KKFB00012](https://keganico.com/product/fixed-blade-kkfb00012/)

</figcaption>

</figure>
```

### 带数据来源的图片

```markdown
<figure>

![图片](https://keganico.com/wp-content/uploads/YYYY/MM/图片.jpg)

<figcaption>

_Data source: [来源名称](链接)_

</figcaption>

</figure>
```

---

## 📁 图片命名规范

### 命名规则

```
格式：[主题]-[描述]-[可选细节].jpg

规则:
✅ 全部小写字母
✅ 单词间用连字符 - 连接
✅ 避免特殊字符和空格
✅ 保持描述性但简洁 (3-5 个关键词)
✅ 长度不超过 50 字符
```

### 命名示例

**钢材类图片**:
```
✅ performance-scorecard-magnacut-vs-s30v.jpg
✅ chemical-comparison-14c28n-vs-d2.jpg
✅ steel-hardness-testing.jpg
✅ corrosion-resistance-comparison.jpg

❌ DSC_2847.JPG (无意义)
❌ Performance Scorecard MagnaCut vs S30V.jpg (空格)
❌ magnacut-vs-s30v-performance-scorecard-head-to-head-ratings-comparison-chart-final.jpg (过长)
```

**产品类图片**:
```
✅ oem-fixed-blade-knife-g10-handle.jpg
✅ civivi-knives-overview.jpg
✅ folding-knife-blade-closeup.jpg

❌ 产品图片 1.jpg (无描述)
❌ IMG_12345.png (无意义)
```

**场景类图片**:
```
✅ knife-sharpening-whetstone.jpg
✅ chef-knife-cutting-vegetables.jpg
✅ edc-pocket-knife-lifestyle.jpg
✅ outdoor-survival-knife-use.jpg
```

---

## 📷 图片来源优先级

### 来源优先级

```
第 1 优先：网站现有本地资源
  - output/posts 中已使用的图片
  - 现有产品图片
  - 历史文章图片

第 2 优先：从网络获取并下载
  - Unsplash (免费商用)
  - Pexels (免费商用)
  - Pixabay (免费商用)

第 3 优先：外部可信赖来源
  - Wikimedia Commons
  - 品牌官网 (需确认权限)
  - 客户提供的图片
```

### 网络图片下载流程

**步骤 1: 搜索关键词**
```
钢材性能类:
- "knife steel hardness"
- "metal hardness testing"
- "steel material texture"
- "spark test steel"

使用场景类:
- "chef knife cutting"
- "knife sharpening"
- "outdoor knife use"
- "edc pocket knife"

制造/工厂类:
- "knife manufacturing"
- "steel factory"
- "cnc machining"
- "yangjiang knives"
```

**步骤 2: 下载与记录**
```
1. 右键点击图片 → 另存为
2. 保存到临时文件夹
3. 记录原始 URL 和来源
4. 记录搜索关键词
```

**步骤 3: 重命名**
```
原始：DSC_2847.JPG
重命名：steel-hardness-testing.jpg

原始：unsplash-photo-123456.png
重命名：knife-sharpness-closeup.jpg
```

**步骤 4: 优化压缩**
```
推荐工具:
- TinyPNG (https://tinypng.com)
- Squoosh (https://squoosh.app)
- ImageOptim (Mac)

目标:
- 文件大小 < 200KB
- 宽度 1200-1920px
- JPG 格式 (照片类)
- PNG 格式 (图表/截图)
```

**步骤 5: 上传**
```
WordPress 媒体库
路径：/wp-content/uploads/YYYY/MM/
月份：使用当前月份或内容主题月份
```

---

## 🗂️ 图片分类体系

### 按内容类型分类

**1. 钢材性能类**
```
用途：钢材评测/对比文章
常见图片:
- 硬度测试场景
- 耐腐蚀对比
- 耐磨性展示
- 金相组织图
- 火花测试

命名示例:
- steel-hardness-testing.jpg
- corrosion-resistance-comparison.jpg
- wear-resistance-demo.jpg
- steel-microstructure.jpg
- spark-test-high-carbon.jpg
```

**2. 产品展示类**
```
用途：品牌评测/产品推荐
常见图片:
- 产品整体图
- 刀片特写
- 手柄细节
- 锁定机制
- 尺寸对比

命名示例:
- civivi-elementum-overview.jpg
- folding-knife-blade-closeup.jpg
- knife-handle-g10-texture.jpg
- liner-lock-mechanism.jpg
- knife-size-comparison.jpg
```

**3. 使用场景类**
```
用途：知识科普/指南文章
常见图片:
- 厨房切割
- 户外使用
- EDC 携带
- 磨刀场景
- 维护清洁

命名示例:
- chef-knife-cutting-vegetables.jpg
- outdoor-survival-knife-use.jpg
- edc-pocket-knife-carry.jpg
- knife-sharpening-whetstone.jpg
- knife-maintenance-cleaning.jpg
```

**4. 制造/工厂类**
```
用途：OEM 指南/产地文章
常见图片:
- 工厂外观
- CNC 加工
- 热处理炉
- 质检流程
- 包装发货

命名示例:
- knife-factory-exterior.jpg
- cnc-machining-blade.jpg
- heat-treatment-furnace.jpg
- quality-control-inspection.jpg
- knife-packaging-shipping.jpg
```

**5. 对比/图表类**
```
用途：对比文章/数据分析
常见图片:
- 性能评分表
- 成分对比图
- 趋势图表
- 信息图

命名示例:
- performance-scorecard-comparison.jpg
- chemical-composition-chart.jpg
- steel-price-trend-graph.jpg
- knife-steel-selection-guide.jpg
```

---

## 📋 现有图片资源清单

### 2026 年资源

| 文件名 | 描述 | 使用文章 | 上传路径 |
|-------|------|---------|---------|
| MagnaCut-vs.-S30V.jpg | 对比主图 | MagnaCut vs S30V | /2026/01/ |
| Performance-Scorecard-MagnaCut-vs-S30V.jpg | 性能评分 | MagnaCut vs S30V | /2026/01/ |
| S45VN-vs-MagnaCut-featured-image.jpg | 对比配图 | 多篇对比 | /2025/12/ |
| what-does-a-fixed-blade-knife-look-like.jpg | 固定刀外观 | What Is Fixed Blade | /2026/03/ |
| anatomy-of-fixed-blade-knife.jpg | 刀具解剖 | What Is Fixed Blade | /2026/03/ |
| hunting-fixed-blade-knife.jpg | 猎刀 | What Is Fixed Blade | /2026/03/ |
| tactical-military-knives.jpg | 战术刀 | What Is Fixed Blade | /2026/03/ |
| fixed-blade-vs-folding-knife.jpg | 对比图 | What Is Fixed Blade | /2026/03/ |
| choosing-fixed-blade-knife-guide.jpg | 选购指南 | What Is Fixed Blade | /2026/03/ |
| fixed-blade-knife-uses.jpg | 使用场景 | What Is Fixed Blade | /2026/03/ |
| knife-maintenance-care.jpg | 维护保养 | What Is Fixed Blade | /2026/03/ |
| civivi.jpg | Civivi 概览 | Civivi Review | /2026/03/ |
| blade.jpg | 刀片特写 | Civivi Review | /2026/03/ |
| civivi-knives.jpg | Civivi 产品 | Civivi Review | /2026/03/ |
| construction.jpg | 构造展示 | Civivi Review | /2026/03/ |
| popular-civivi-knife.jpg | 热门型号 | Civivi Review | /2026/03/ |
| user-experience.jpg | 用户体验 | Civivi Review | /2026/03/ |
| Pros-and-cons-of-Civivi-knives.jpg | 优缺点 | Civivi Review | /2026/03/ |
| Civivi-knives-vs-other-brands.jpg | 品牌对比 | Civivi Review | /2026/03/ |

### 2025 年资源

| 文件名 | 描述 | 使用文章 | 上传路径 |
|-------|------|---------|---------|
| OEM-Fixed-Blade-Knife-G10-Handle-S30V-Blade.jpg | 产品示例 | 多篇钢材文 | /2025/10/ |
| OEM-Micarta-Carbon-Fiber-Handle-14C28N-Blade.jpg | 产品示例 | 14C28N 评测 | /2025/07/ |
| OEM-Liner-Lock-Fused-Carbon-Fiber-G10.jpg | 产品示例 | 14C28N 评测 | /2024/01/ |
| Figure-5-Steel-Molding-Damascus.jpg | 钢材成型 | 14C28N 评测 | /2025/06/ |

---

## ✅ 图片使用检查清单

### 发布前检查

```
□ 每 400-500 字至少 1 张图片
□ 每个 H2 章节有配图
□ 开篇后第 1 个章节有图
□ 对比表格前后有图
□ 所有图片有 Alt 文本
□ Alt 文本包含关键词
□ 图片文件名描述性
□ Figure 格式正确 (产品图)
□ 图片来源/数据有标注
□ 文件大小已优化 (<200KB)
□ 链接有效 (产品 Figure)
```

### SEO 检查

```
□ Alt 文本 5-15 个单词
□ Alt 文本描述图片内容
□ Alt 文本包含关键词
□ 避免"image of"开头
□ 文件名含关键词
□ 上传路径正确 (YYYY/MM)
```

---

## 🔧 图片处理工具推荐

### 批量重命名
```
- Bulk Rename Utility (Windows) - 免费
- Renamer (Mac) - $20
- Advanced Renamer (跨平台) - 免费
```

### 图片优化
```
- TinyPNG (在线) - https://tinypng.com
- Squoosh (在线) - https://squoosh.app
- ImageOptim (Mac) - 免费
- RIOT (Windows) - 免费
```

### 格式转换
```
- Convertio (在线) - https://convertio.co
- XnConvert (跨平台) - 免费
- IrfanView (Windows) - 免费
```

### 截图/标注
```
- Snagit - 付费，功能全面
- Greenshot - 免费，轻量级
- ShareX - 免费，开源
```

---

## 📊 图片使用统计

### 按年份统计

| 年份 | 图片数量 | 占比 | 说明 |
|-----|---------|------|------|
| 2026 | 20+ | 40% | 最新资源，优先使用 |
| 2025 | 15+ | 30% | 高质量资源 |
| 2024 | 10+ | 20% | 补充资源 |
| 2023 | 5+ | 10% | 经典资源 |

### 按类型统计

| 类型 | 数量 | 常用场景 |
|-----|------|---------|
| 钢材性能 | 15+ | 钢材评测/对比 |
| 产品展示 | 20+ | 品牌评测/推荐 |
| 使用场景 | 10+ | 知识科普 |
| 制造工厂 | 5+ | OEM 指南 |
| 对比图表 | 10+ | 对比文章 |

---

## 🚀 最佳实践

### 图片选择原则

```
1. 相关性优先
   - 图片必须与章节内容相关
   - 避免为配图而配图

2. 质量优先
   - 清晰度高 (最小 800px 宽)
   - 光线充足
   - 焦点清晰

3. 多样性
   - 避免同一篇文章重复使用相似图片
   - 混合使用特写/全景/场景图

4. 品牌一致性
   - 优先使用产品图片
   - 展示 Keganico 产品
   - 链接到产品页面
```

### 避免事项

```
❌ 使用模糊/低质量图片
❌ 使用有版权风险的图片
❌ 使用与内容无关的图片
❌ 图片文件名无意义
❌ Alt 文本缺失或过于简单
❌ 图片文件过大 (>500KB)
❌ 同一图片多次使用
```

---

*Keganico Skills v1.0 | Image Guidelines | 最后更新：2026-03-26*

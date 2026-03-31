# SKILL-06: 图片规范与工具

**用途**: 规范图片插入位置、格式，及使用脚本自动化处理
**适用**: 所有文章类型（横切关注点）

---

## 1. 图片密度规则

- 每 500 字至少 1 张图片
- 每个主要章节（`##`）至少 1 张
- 开篇后第 1 个章节必须有图片
- 对比表格前后各 1 张
- 结论前可有 1 张总结性图片

---

## 2. 图片来源优先级

```
第 1 优先：网站现有本地资源（output/images 中已下载的图片）
第 2 优先：从网络下载并本地化（使用 download_images.py）
第 3 优先：外部可信赖来源（Wikimedia、Unsplash 等）
```

⚠️ **禁止虚构图片链接** — 所有图片必须真实存在于服务器或本地。

**图片存储路径规范**:
```
本地开发：output/images/[文章主题]/图片名.webp
示例：output/images/class-150-vs-300-flanges/image-1.webp

文章引用：../../images/[文章主题]/图片名.webp
示例：../../images/class-150-vs-300-flanges/image-1.webp

服务器路径：/wp-content/uploads/YYYY/MM/图片名.jpg
示例：/wp-content/uploads/2026/03/flange-comparison.jpg
```

---

## 3. 关键词选择策略 ⭐ 重要

**图片必须与文章主题高度相关** — 避免使用通用/随机图片

### 法兰/阀门/管件文章图片关键词

| 章节 | 推荐关键词 | 避免关键词 |
|-----|-----------|-----------|
| 开篇/引言 | `industrial flanges`, `pipe fittings`, `valve assembly`, `steel pipeline` | `random metal`, `abstract texture` |
| 产品规格 | `flange dimensions chart`, `technical drawing`, `engineering blueprint` | `generic factory`, `metal sheet` |
| 材质说明 | `stainless steel material`, `carbon steel`, `metal alloy`, `spectrometer analysis` | `rusty metal`, `scrap steel` |
| 压力等级 | `pressure gauge`, `pressure testing equipment`, `hydrostatic test` | `tire pressure`, `blood pressure` |
| 温度范围 | `industrial thermometer`, `temperature sensor`, `heat treatment furnace` | `weather thermometer`, `kitchen oven` |
| 耐腐蚀性 | `corrosion resistant coating`, `salt spray test`, `chemical tank` | `rusted pipe`, `damaged equipment` |
| 焊接连接 | `pipe welding`, `welded flange`, `welder working`, `TIG welding stainless` | `arc welding sparks`, `construction site` |
| 螺栓紧固 | `bolt torque wrench`, `flange bolt tightening`, `crisscross pattern` | `car mechanic`, `random bolts` |
| 安装场景 | `pipeline installation`, `industrial construction`, `pipe fitter working` | `home plumbing`, `bathroom repair` |
| 应用 - 石化 | `petrochemical plant`, `refinery pipes`, `chemical processing` | `gas station`, `fuel pump` |
| 应用 - 电力 | `power plant pipes`, `steam turbine`, `boiler system` | `electrical substation`, `solar panel` |
| 应用 - 水处理 | `water treatment plant`, `municipal water pipes`, `pump station` | `swimming pool`, `home faucet` |
| 对比表格 | `flange comparison chart`, `valve types diagram`, `material comparison` | `product comparison`, `price table` |

### 关键词选择规则

```
✅ 正确做法:
- 使用具体描述性关键词：`weld neck flange dimensions`, `ball valve cross section`
- 添加材质/场景限定：`stainless steel 316 flange`, `industrial pipeline oil and gas`
- 使用同义词扩展：`flange` / `fitting` / `connection` / `valve` / `pipeline`

❌ 错误做法:
- 过于宽泛：`metal`, `steel`, `pipe`（结果不相关）
- 使用随机种子图片（Picsum 随机图）
- 与主题无关的通用图片：`office desk`, `person working`
```

### 产品类型图片速查表

```
法兰文章:
- 优先：各种法兰类型实物图、尺寸图、安装现场
- 避免：无关的金属片、生锈管道

阀门文章:
- 优先：阀门剖面图、工作原理图、执行器细节
- 避免：家用阀门、塑料阀门

管件文章:
- 优先：弯头/三通/异径管实物、焊接细节
- 避免：家用 plumbing 配件、PVC 管件

材质对比文章:
- 优先：金相组织图、光谱分析、腐蚀测试对比
- 避免：模糊的材质特写、无标注的图表
```

---

## 4. 图片本地化流程（5 步）

**步骤 1**: 在 Unsplash / Pexels / Pixabay / Wikimedia 查找图片

**步骤 2**: 使用 `download_images.py` 批量下载（见第 6 节）

**步骤 3**: 重命名规范：
```
格式：[主题]-[描述]-[可选版本].jpg

✅ weld-neck-flange-dimensions.jpg
✅ ball-valve-cross-section.jpg
✅ flange-bolt-tightening-pattern.jpg

❌ DSC_2847.JPG（无意义）
❌ 法兰图片_2024.jpg（中文 + 特殊字符）
❌ class-150-flange-image-final-v2.jpg（过长）
```

**步骤 4**: 上传到服务器
```
路径：/wp-content/uploads/YYYY/MM/图片名.jpg
示例：/wp-content/uploads/2026/03/weld-neck-flange.jpg
```

**步骤 5**: 使用 `update_article_images.py` 更新文章中的图片引用（见第 7 节）

---

## 5. Markdown 图片格式

**基础格式**:
```markdown
![图片描述](https://img.example.com/wp-content/uploads/年份/月份/图片名称.jpg)
```

**Figure 格式**（产品展示）:
```markdown
<figure>

[![产品图片](https://img.example.com/wp-content/uploads/YYYY/MM/图片.jpg)](https://example.com/产品链接/)

<figcaption>

[产品名称](https://example.com/产品链接/)

</figcaption>

</figure>
```

**图片来源标注**:
```markdown
<figure>

[![图片](https://img.example.com/wp-content/uploads/YYYY/MM/图片.jpg)](https://img.example.com/wp-content/uploads/YYYY/MM/图片.jpg)

<figcaption>

ASME B16.5 Flange Dimensions from [Wikimedia](https://commons.wikimedia.org/wiki/Main_Page)

</figcaption>

</figure>
```

**图片描述命名规则**:
- 使用小写 + 连字符
- 描述性文字，如 `the-pressure-rating-chart-for-class-150-flanges`
- 避免过于简单的描述

---

## 6. 图片下载脚本：`download_images.py`

**脚本位置**: `scripts/download_images.py`

**功能**: 从 Unsplash/Pexels/Picsum 批量下载免版税图片，自动压缩为 WebP/JPG 格式

**安装依赖**:
```bash
pip install requests Pillow
```

**环境变量（可选）**:
```bash
export PEXELS_API_KEY="你的 Pexels 密钥"
export UNSPLASH_ACCESS_KEY="你的 Unsplash 密钥"
```

**使用示例**:

```bash
# 下载 5 张关于法兰的图片到 output/images（默认 medium 尺寸）
python scripts/download_images.py --query "industrial flanges pipeline" --count 5 --output output/images/

# 下载到指定文章目录，使用 large 尺寸
python scripts/download_images.py --query "ball valve industrial" --output output/images/ball-valve-guide/ --count 8 --size large

# 使用 Pexels API（需设置 PEXELS_API_KEY）
python scripts/download_images.py --query "steel pipe fittings" --use-api --count 6 --output output/images/
```

**参数说明**:

| 参数 | 简写 | 说明 | 默认值 |
|-----|------|------|-------|
| `--query` | `-q` | 搜索关键词（中英文均可） | 必填 |
| `--output` | `-o` | 输出目录（建议使用 output/images/[文章主题]/） | `output/images/` |
| `--count` | `-c` | 下载数量（最多 20） | `5` |
| `--size` | `-s` | 图片尺寸：small/medium/large/xlarge | `medium` |
| `--use-api` | — | 启用 Pexels API | 关闭 |

**尺寸参考**:

| 尺寸名 | 分辨率 |
|-------|-------|
| small | 640×480 |
| medium | 1280×720 |
| large | 1920×1080 |
| xlarge | 2560×1440 |

**输出示例**:
```
==================================================
SEO 文章图片下载器
==================================================
关键词：industrial flanges pipeline
输出目录：/project/images
数量：5
尺寸：medium (1280x720)
==================================================

正在从 Picsum 下载图片...
  ✓ 已保存：industrial-flanges-pipeline-1.webp (87KB)
  ✓ 已保存：industrial-flanges-pipeline-2.webp (92KB)
  ...

下载完成！成功：5/5
```

---

## 7. 图片引用更新脚本：`update_article_images.py`

**脚本位置**: `scripts/update_article_images.py`

**功能**: 自动将文章中的占位符图片替换为真实下载的图片，或将新图片插入文章合适位置

**安装依赖**:
```bash
pip install Pillow
```

**使用示例**:

```bash
# 自动替换占位符图片 + 插入新图片
python scripts/update_article_images.py --article output/posts/flange-guide/index.md --images-dir output/images/flange-guide/

# 仅替换占位符图片（不插入新图片）
python scripts/update_article_images.py --article output/posts/flange-guide/index.md --images-dir output/images/flange-guide/ --replace-only

# 在每个 H2 标题后插入图片
python scripts/update_article_images.py --article output/posts/flange-guide/index.md --images-dir output/images/flange-guide/ --pattern after-headings

# 均匀分布图片（每 300 字一张）
python scripts/update_article_images.py --article output/posts/flange-guide/index.md --images-dir output/images/flange-guide/ --pattern evenly

# 查看图片列表和引用示例（不修改文章）
python scripts/update_article_images.py --list --images-dir output/images/flange-guide/ --keyword "industrial flanges"
```

**参数说明**:

| 参数 | 简写 | 说明 |
|-----|------|------|
| `--article` | `-a` | Markdown 文章文件路径 |
| `--images-dir` | `-i` | 图片目录（默认：output/images/）|
| `--keyword` | `-k` | 关键词（用于生成 alt 文本）|
| `--pattern` | `-p` | 插入模式（见下表）|
| `--max-images` | `-m` | 最大图片数量 |
| `--list` | — | 仅列出图片，不修改文章 |
| `--replace-only` | — | 仅替换占位符，不插入新图片 |

**插入模式（--pattern）**:

| 模式 | 说明 |
|-----|------|
| `after-intro`（默认）| 在第一个 H2 标题后插入 |
| `after-headings` | 在每个 H2 标题后插入 |
| `evenly` | 每 300 字均匀插入一张 |

**占位符图片识别**: 脚本自动识别以下格式的占位符并替换：
```
images/featured-image.jpg
images/image-1.jpg
images/placeholder.jpg
images/TODO.jpg
```

**典型工作流**（下载 + 插入一体）:
```bash
# 1. 下载图片到 output/images/[文章主题]/
python scripts/download_images.py --query "ball valve industrial" --output output/images/ball-valve-guide/ --count 8

# 2. 更新文章图片引用
python scripts/update_article_images.py \
  --article output/posts/ball-valve-guide/index.md \
  --images-dir output/images/ball-valve-guide/ \
  --keyword "ball valve" \
  --pattern after-headings
```

---

## 8. 图片优化最佳实践

- JPG 格式用于照片类图片
- PNG 格式用于图表/截图
- WebP 格式用于网页优化（脚本默认输出）
- 图片大小控制在 **200KB 以内**
- 宽度建议 **1200-1920px**

**推荐工具**:
- 批量重命名：Bulk Rename Utility / Advanced Renamer
- 在线压缩：TinyPNG / Squoosh
- 格式转换：Convertio / XnConvert

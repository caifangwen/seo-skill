# SEO Article Skill

SEO 文章写作技能 - 用于创建符合 SEO 优化的文章，包括自动下载和引用图片。

## 文件夹结构

```
seo-article/
├── SKILL.md                    # 技能定义和使用说明
├── example-article.md          # 文章模板示例
└── scripts/
    ├── download_images.py      # 图片下载脚本
    ├── update_article_images.py # 文章图片引用更新脚本
    └── requirements.txt        # Python 依赖
```

## 安装依赖

```bash
cd skills/seo-article/scripts
pip install -r requirements.txt
```

## 使用方法

### 1. 下载图片

```bash
# 基本用法
python scripts/download_images.py --query "人工智能"

# 指定输出目录和数量
python scripts/download_images.py --query "机器学习" --output images/ --count 10

# 指定图片尺寸
python scripts/download_images.py --query "数据科学" --size large --count 5
```

### 2. 在文章中插入图片引用

```bash
# 自动插入图片到文章
python scripts/update_article_images.py --article article.md --images-dir images/

# 列出图片和引用示例
python scripts/update_article_images.py --list images/ --keyword "人工智能"
```

### 3. 在 Claude 中使用

在 Claude 对话中提及：
- "使用 SEO 文章技能帮我写一篇关于 [主题] 的文章"
- "用 seo-article 技能下载关于 [关键词] 的图片"
- "帮我创建符合 SEO 的博客文章"

## 脚本参数

### download_images.py

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `--query`, `-q` | 搜索关键词（必需） | - |
| `--output`, `-o` | 输出目录 | `images/` |
| `--count`, `-c` | 下载数量 | `5` |
| `--size`, `-s` | 图片尺寸 (small/medium/large/xlarge) | `medium` |
| `--use-api` | 使用 Unsplash API（需要密钥） | `false` |

### update_article_images.py

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `--article`, `-a` | Markdown 文章文件路径 | - |
| `--images-dir`, `-i` | 图片目录 | `images/` |
| `--keyword`, `-k` | 关键词（用于生成 alt 文本） | - |
| `--pattern`, `-p` | 插入模式 (after-intro/after-headings/evenly) | `after-intro` |
| `--max-images`, `-m` | 最大图片数量 | - |
| `--list` | 仅列出图片，不修改文章 | `false` |
| `--replace-only` | 仅替换占位符，不插入新图片 | `false` |

**功能**:
- 自动识别并替换占位符图片 (`featured-image.jpg`, `image-1.jpg` 等)
- 根据章节上下文生成准确的 alt 文本
- 添加图片尺寸和文件大小说明

## 环境变量（可选）

设置 Unsplash API 密钥以获得更好的搜索结果：

```bash
export UNSPLASH_ACCESS_KEY=your_access_key_here
```

## 示例工作流程

```bash
# 1. 创建文章目录
mkdir my-seo-article
cd my-seo-article

# 2. 下载图片
python ../skills/seo-article/scripts/download_images.py \
  --query "可再生能源" \
  --output images/ \
  --count 5

# 3. 创建文章
# （使用 SKILL.md 中的模板创建 article.md）

# 4. 插入图片引用
python ../skills/seo-article/scripts/update_article_images.py \
  --article article.md \
  --images-dir images/ \
  --keyword "可再生能源"
```

## 注意事项

1. 图片来自 Unsplash，为免版税图片，可用于商业用途
2. 建议设置 UNSPLASH_ACCESS_KEY 获得更稳定的服务
3. 图片会自动压缩到 200KB 以下
4. 文件名会自动转换为小写和连字符格式

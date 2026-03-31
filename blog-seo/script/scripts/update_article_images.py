#!/usr/bin/env python3
"""
文章图片引用更新脚本
自动匹配并更新 Markdown 文章中的图片引用

使用方法:
    python update_article_images.py --article article.md --images-dir images/
    python update_article_images.py --article article.md --images-dir images/ --pattern "after-intro"

依赖:
    pip install Pillow
"""

import argparse
import re
import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError as e:
    print(f"缺少依赖：{e}")
    print("请运行：pip install Pillow")
    sys.exit(1)


# 常见的占位符图片模式
PLACEHOLDER_PATTERNS = [
    r'!\[([^\]]*)\]\(images/featured-image\.(jpg|jpeg|png|gif|webp)\)',
    r'!\[([^\]]*)\]\(images/image-\d+\.(jpg|jpeg|png|gif|webp)\)',
    r'!\[([^\]]*)\]\(images/placeholder\.(jpg|jpeg|png|gif|webp)\)',
    r'!\[([^\]]*)\]\(images/TODO\.(jpg|jpeg|png|gif|webp)\)',
]


def get_image_metadata(image_path):
    """获取图片元数据"""
    try:
        with Image.open(image_path) as img:
            return {
                'width': img.width,
                'height': img.height,
                'format': img.format,
                'size_kb': image_path.stat().st_size // 1024
            }
    except Exception as e:
        return {'error': str(e)}


def generate_alt_text(filename, keyword=None, context=None):
    """
    根据文件名和上下文生成 alt 文本

    参数:
        filename: 图片文件名
        keyword: 可选的关键词
        context: 可选的上下文描述
    """
    # 移除扩展名和数字后缀
    name = Path(filename).stem
    # 移除数字后缀 (如 -1, -2)
    name = re.sub(r'-\d+$', '', name)
    # 将连字符转换为空格
    name = name.replace('-', ' ')

    if context:
        return f"{context} - {name}"
    elif keyword:
        return f"{name} - {keyword}"
    return name.replace('-', ' ').title()


def create_image_markdown(filename, images_dir, alt_text=None, caption=None):
    """
    创建 Markdown 图片引用

    参数:
        filename: 图片文件名
        images_dir: 图片目录
        alt_text: alt 文本（可选，自动生成）
        caption: 可选的图片说明
    """
    if not alt_text:
        alt_text = generate_alt_text(filename)

    # 使用相对路径
    rel_path = f"{images_dir.rstrip('/')}/{filename}"

    markdown = f"![{alt_text}]({rel_path})"

    if caption:
        markdown += f"\n*{caption}*"

    return markdown


def find_placeholder_images(content):
    """
    查找文章中的占位符图片引用

    返回：[(行号，完整匹配，alt 文本，文件名)]
    """
    placeholders = []
    lines = content.split('\n')

    for line_num, line in enumerate(lines):
        for pattern in PLACEHOLDER_PATTERNS:
            match = re.search(pattern, line)
            if match:
                placeholders.append((line_num, match.group(0), match.group(1), match.group(2)))
                break

    return placeholders


def find_section_context(content, line_num):
    """
    根据行号查找所在章节的上下文

    返回章节标题，用于生成更准确的 alt 文本
    """
    lines = content.split('\n')
    current_section = None

    for i in range(line_num, -1, -1):
        if lines[i].startswith('## '):
            current_section = lines[i][3:].strip()
            break

    return current_section


def replace_placeholders_with_real_images(
    article_path,
    images_dir,
    keyword=None
):
    """
    替换文章中的占位符图片为实际下载的图片

    参数:
        article_path: 文章文件路径
        images_dir: 图片目录
        keyword: 关键词
    """
    article_path = Path(article_path)
    images_path = Path(images_dir)

    if not article_path.exists():
        print(f"错误：文章文件不存在：{article_path}")
        return False

    if not images_path.exists():
        print(f"错误：图片目录不存在：{images_path}")
        return False

    # 获取图片列表
    image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.webp')
    images = [
        f.name for f in images_path.iterdir()
        if f.is_file() and f.suffix.lower() in image_extensions
    ]
    images.sort()

    if not images:
        print(f"警告：图片目录为空：{images_path}")
        return False

    print(f"\n{'='*50}")
    print(f"文章图片引用更新")
    print(f"{'='*50}")
    print(f"文章：{article_path}")
    print(f"图片目录：{images_path}")
    print(f"可用图片：{len(images)}")
    print(f"{'='*50}\n")

    # 读取文章
    content = article_path.read_text(encoding='utf-8')
    lines = content.split('\n')

    # 查找占位符
    placeholders = find_placeholder_images(content)

    if not placeholders:
        print("✓ 未发现占位符图片，检查是否需要插入新图片...")
        # 检查是否有未引用的图片
        existing_refs = re.findall(r'!\[([^\]]*)\]\(images/([^)]+)\)', content)
        existing_files = [ref[1] for ref in existing_refs]

        unreferenced = [img for img in images if img not in existing_files]
        if unreferenced:
            print(f"发现 {len(unreferenced)} 张未引用的图片:")
            for img in unreferenced:
                print(f"  - {img}")
        else:
            print("✓ 所有图片都已正确引用")
        return True

    print(f"发现 {len(placeholders)} 个占位符图片引用:")
    for line_num, full_match, alt, ext in placeholders:
        print(f"  行 {line_num + 1}: {full_match[:60]}...")

    # 为每个占位符分配图片
    # 先按正序分配图片索引，然后倒序处理以避免行号偏移
    image_index = 0
    replacements_made = 0

    # 创建 (行号，图片索引) 的映射
    line_to_image = {}
    for line_num, full_match, old_alt, ext in placeholders:
        if image_index < len(images):
            line_to_image[line_num] = image_index
            image_index += 1

    # 从后往前处理，避免行号偏移
    for line_num in sorted(line_to_image.keys(), reverse=True):
        img_index = line_to_image[line_num]
        img_file = images[img_index]

        # 获取原始匹配
        full_match = None
        old_alt = None
        ext = None
        for ln, fm, oa, ex in placeholders:
            if ln == line_num:
                full_match, old_alt, ext = fm, oa, ex
                break
        metadata = get_image_metadata(images_path / img_file)

        if 'error' in metadata:
            print(f"  ✗ 无法读取：{img_file} - {metadata['error']}")
            continue

        # 获取章节上下文
        section_context = find_section_context(content, line_num)

        # 生成 alt 文本
        alt_text = generate_alt_text(img_file, keyword, section_context)

        # 生成图片说明
        caption = f"图片来源：Unsplash ({metadata['width']}x{metadata['height']}, {metadata['size_kb']}KB)"

        # 创建新的图片引用
        new_markdown = f"![{alt_text}]({images_dir.rstrip('/')}/{img_file})\n*{caption}*"

        # 替换图片行
        lines[line_num] = new_markdown

        # 检查下一行是否是旧的图片说明（以 * 开头且包含"图片来源"）
        if line_num + 1 < len(lines):
            next_line = lines[line_num + 1].strip()
            if next_line.startswith('*') and ('图片来源' in next_line or 'source' in next_line.lower()):
                # 删除旧的图片说明行
                lines.pop(line_num + 1)
                # 由于删除了一行，后续所有行号需要减 1
                # 但因为我们是倒序处理，所以不需要调整

        print(f"  ✓ 已替换：{img_file} -> 行 {line_num + 1}")

        image_index += 1
        replacements_made += 1

    # 写入更新后的文章
    new_content = '\n'.join(lines)
    article_path.write_text(new_content, encoding='utf-8')

    print(f"\n{'='*50}")
    print(f"更新完成！")
    print(f"已替换 {replacements_made} 个占位符图片")
    print(f"{'='*50}\n")

    return True


def insert_images_to_article(
    article_path,
    images_dir,
    keyword=None,
    pattern='after-intro',
    max_images=None
):
    """
    在文章中插入新的图片引用（当没有占位符时使用）

    参数:
        article_path: 文章文件路径
        images_dir: 图片目录
        keyword: 关键词（用于 alt 文本）
        pattern: 插入模式
        max_images: 最大图片数量
    """
    article_path = Path(article_path)
    images_path = Path(images_dir)

    if not article_path.exists():
        print(f"错误：文章文件不存在：{article_path}")
        return False

    if not images_path.exists():
        print(f"错误：图片目录不存在：{images_path}")
        return False

    # 获取图片列表
    image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.webp')
    images = [
        f.name for f in images_path.iterdir()
        if f.is_file() and f.suffix.lower() in image_extensions
    ]
    images.sort()

    if not images:
        print(f"警告：图片目录为空：{images_path}")
        return False

    if max_images:
        images = images[:max_images]

    # 检查是否已有图片引用
    content = article_path.read_text(encoding='utf-8')
    existing_refs = re.findall(r'!\[([^\]]*)\]\(images/([^)]+)\)', content)
    existing_files = [ref[1] for ref in existing_refs]

    # 过滤掉已引用的图片
    new_images = [img for img in images if img not in existing_files]

    if not new_images:
        print("✓ 所有图片都已引用，无需插入")
        return True

    print(f"\n{'='*50}")
    print(f"插入新图片到文章")
    print(f"{'='*50}")
    print(f"文章：{article_path}")
    print(f"新图片：{len(new_images)}")
    print(f"{'='*50}\n")

    # 查找插入点
    insertion_points = find_insertion_points(content, pattern, existing_refs)

    if not insertion_points:
        print("未找到合适的插入位置")
        return False

    # 生成图片引用
    image_markdowns = []
    for img in new_images:
        metadata = get_image_metadata(images_path / img)

        if 'error' in metadata:
            print(f"  ✗ 无法读取：{img} - {metadata['error']}")
            continue

        alt_text = generate_alt_text(img, keyword)
        caption = f"图片来源：Unsplash ({metadata['width']}x{metadata['height']}, {metadata['size_kb']}KB)"
        markdown = create_image_markdown(img, images_dir, alt_text, caption)
        image_markdowns.append(markdown)
        print(f"  ✓ 准备插入：{img}")

    # 插入图片到文章
    lines = content.split('\n')

    # 计算每个插入点应该插入多少图片
    images_per_point = max(1, len(image_markdowns) // max(1, len(insertion_points)))

    # 从后往前插入，避免索引偏移
    insertion_points.sort(reverse=True)

    output_images = []
    for idx, point in enumerate(insertion_points):
        start_idx = idx * images_per_point
        end_idx = min(start_idx + images_per_point, len(image_markdowns))

        if start_idx >= len(image_markdowns):
            break

        images_to_insert = image_markdowns[start_idx:end_idx]
        output_images.extend(images_to_insert)

        # 插入空行和图片
        insert_content = '\n'.join([''] + images_to_insert + [''])
        lines.insert(point, insert_content)

    # 写入更新后的文章
    new_content = '\n'.join(lines)
    article_path.write_text(new_content, encoding='utf-8')

    print(f"\n{'='*50}")
    print(f"插入完成！")
    print(f"已插入 {len(output_images)} 张图片引用")
    print(f"{'='*50}\n")

    return True


def find_insertion_points(content, pattern='after-intro', existing_refs=None):
    """
    查找图片插入位置

    参数:
        content: 文章内容
        pattern: 插入模式
        existing_refs: 已有的图片引用列表
    """
    lines = content.split('\n')
    insertion_points = []

    if pattern == 'after-intro':
        # 在第一个 H2 标题后插入
        for i, line in enumerate(lines):
            if line.startswith('## ') and i > 2:
                insertion_points.append(i)
                break

    elif pattern == 'after-headings':
        # 在每个 H2 标题后插入（跳过已有图片的位置）
        for i, line in enumerate(lines):
            if line.startswith('## '):
                # 检查下一行是否已有图片
                if i + 1 < len(lines) and not lines[i + 1].startswith('!['):
                    insertion_points.append(i + 1)

    elif pattern == 'evenly':
        # 均匀分布：每 300 字左右插入一张
        char_count = 0
        for i, line in enumerate(lines):
            char_count += len(line)
            if char_count >= 300 and not line.startswith('#') and not line.startswith('!['):
                insertion_points.append(i)
                char_count = 0

    return insertion_points


def generate_image_list(images_dir, keyword=None):
    """
    生成图片列表和引用示例

    参数:
        images_dir: 图片目录
        keyword: 关键词
    """
    images_path = Path(images_dir)

    if not images_path.exists():
        print(f"错误：目录不存在：{images_path}")
        return

    image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.webp')
    images = [
        f for f in images_path.iterdir()
        if f.is_file() and f.suffix.lower() in image_extensions
    ]
    images.sort(key=lambda x: x.name)

    print(f"\n{'='*50}")
    print(f"图片列表和引用示例")
    print(f"{'='*50}")
    print(f"目录：{images_path.absolute()}")
    print(f"图片数量：{len(images)}")
    print(f"{'='*50}\n")

    for img in images:
        metadata = get_image_metadata(img)
        alt_text = generate_alt_text(img.name, keyword)

        print(f"文件：{img.name}")
        print(f"  尺寸：{metadata.get('width', 'N/A')}x{metadata.get('height', 'N/A')}")
        print(f"  大小：{metadata.get('size_kb', 'N/A')}KB")
        print(f"  Alt: {alt_text}")
        print(f"  引用：![{alt_text}]({images_dir.rstrip('/')}/{img.name})")
        print()


def main():
    parser = argparse.ArgumentParser(
        description='在 Markdown 文章中插入或更新图片引用',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python update_article_images.py --article article.md --images-dir images/
  python update_article_images.py --article blog/post.md --images-dir images/ --pattern after-headings
  python update_article_images.py --list images/ --keyword "人工智能"

功能:
  1. 自动替换占位符图片 (featured-image.jpg, image-1.jpg 等)
  2. 插入新图片到文章
  3. 列出图片和引用示例
        """
    )

    parser.add_argument(
        '--article', '-a',
        help='Markdown 文章文件路径'
    )

    parser.add_argument(
        '--images-dir', '-i',
        default='images',
        help='图片目录（默认：images/）'
    )

    parser.add_argument(
        '--keyword', '-k',
        help='关键词（用于生成 alt 文本）'
    )

    parser.add_argument(
        '--pattern', '-p',
        choices=['after-intro', 'after-headings', 'evenly'],
        default='after-intro',
        help='图片插入模式（默认：after-intro）'
    )

    parser.add_argument(
        '--max-images', '-m',
        type=int,
        help='最大图片数量'
    )

    parser.add_argument(
        '--list',
        action='store_true',
        dest='list_mode',
        help='仅列出图片和引用示例，不修改文章'
    )

    parser.add_argument(
        '--replace-only',
        action='store_true',
        help='仅替换占位符，不插入新图片'
    )

    args = parser.parse_args()

    if args.list_mode:
        generate_image_list(args.images_dir, args.keyword)
    elif args.article:
        # 首先尝试替换占位符
        if replace_placeholders_with_real_images(
            article_path=args.article,
            images_dir=args.images_dir,
            keyword=args.keyword
        ):
            print("占位符替换完成")

        # 如果不是仅替换模式，继续插入新图片
        if not args.replace_only:
            insert_images_to_article(
                article_path=args.article,
                images_dir=args.images_dir,
                keyword=args.keyword,
                pattern=args.pattern,
                max_images=args.max_images
            )
    else:
        parser.print_help()
        print("\n错误：请指定 --article 或 --list 参数")
        sys.exit(1)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
图片下载脚本 - 用于 SEO 文章
从 Unsplash/Pexels/Pixabay 下载免版税图片

使用方法:
    python download_images.py --query "关键词" --output output/images/ --count 5

依赖:
    pip install requests Pillow

钢材文章推荐关键词:
    - 开篇/引言：knife blade close-up, steel texture
    - 硬度：hardness testing, rockwell hardness test
    - 耐腐蚀：rust resistant steel, stainless steel water
    - 边缘保持：sharp knife edge, knife cutting paper
    - 韧性：toughness test, impact test steel
    - 耐磨性：wear resistance, abrasion test
    - 打磨：knife sharpening, whetstone
    - 厨房场景：chef knife professional, kitchen knife cutting
    - EDC 场景：pocket knife edc, folding knife
    - 户外场景：hunting knife, outdoor knife camping
"""

import argparse
import os
import re
import sys
from pathlib import Path

try:
    import requests
    from PIL import Image
    from io import BytesIO
except ImportError as e:
    print(f"缺少依赖：{e}")
    print("请运行：pip install requests Pillow")
    sys.exit(1)


# 多个图片源，按优先级排列
PEXELS_API_URL = "https://api.pexels.com/v1/search"
UNSPLASH_API_URL = "https://api.unsplash.com/search/photos"
PIXABAY_API_URL = "https://pixabay.com/api/"

# 可选：如果有 API 密钥，可以使用更完整的 API
UNSPLASH_ACCESS_KEY = os.environ.get("UNSPLASH_ACCESS_KEY", "")
PEXELS_API_KEY = os.environ.get("PEXELS_API_KEY", "")
# PIXABAY_API_KEY = os.environ.get("PIXABAY_API_KEY", "")
PIXABAY_API_KEY = "55145593-d3e99049408b5d5e0e0c742e2"  # 硬编码密钥


# ⚠️ 不再使用 Picsum 随机图片 — 图片与文章主题不相关
# PICSUM_URL = "https://picsum.photos"


def sanitize_filename(text):
    """将文本转换为安全的文件名"""
    # 移除特殊字符
    text = re.sub(r'[^\w\s\u4e00-\u9fff\-]', '', text)
    # 替换空格为连字符
    text = re.sub(r'\s+', '-', text)
    # 移除多个连续连字符
    text = re.sub(r'-+', '-', text)
    # 转换为小写
    return text.strip('-').lower()


def get_image_size(size_name):
    """获取图片尺寸配置"""
    sizes = {
        'small': {'width': 640, 'height': 480},
        'medium': {'width': 1280, 'height': 720},
        'large': {'width': 1920, 'height': 1080},
        'xlarge': {'width': 2560, 'height': 1440},
    }
    return sizes.get(size_name, sizes['medium'])


def download_from_pixabay(query, count, size, output_dir):
    """
    从 Pixabay API 下载图片（需要 API 密钥）
    Pixabay 提供大量免版税图片，适合 SEO 文章
    """
    if not PIXABAY_API_KEY:
        return []

    print(f"正在使用 Pixabay API 搜索：{query}")

    size_config = get_image_size(size)
    downloaded = []

    params = {
        'key': PIXABAY_API_KEY,
        'q': query,
        'image_type': 'photo',
        'per_page': min(count, 40),
        'min_width': size_config['width'],
        'min_height': size_config['height'],
    }

    try:
        response = requests.get(PIXABAY_API_URL, params=params, timeout=30)
        response.raise_for_status()

        results = response.json().get('hits', [])

        if not results:
            print(f"  未找到相关图片")
            return downloaded

        for i, hit in enumerate(results[:count]):
            try:
                image_url = hit['largeImageURL']

                print(f"  下载图片 {i + 1}/{min(count, len(results))}...")

                img_response = requests.get(image_url, timeout=30)
                img_response.raise_for_status()

                safe_query = sanitize_filename(query)
                filename = f"{safe_query}-{i + 1}.jpg"
                filepath = output_dir / filename

                img = Image.open(BytesIO(img_response.content))

                if img.mode in ('RGBA', 'P'):
                    img = img.convert('RGB')

                img.save(filepath, 'JPEG', quality=90, optimize=True)

                downloaded.append(filename)
                print(f"  ✓ 已保存：{filename} ({filepath.stat().st_size // 1024}KB)")

            except Exception as e:
                print(f"  ✗ 下载失败：{e}")
                continue

    except Exception as e:
        print(f"Pixabay API 请求失败：{e}")

    return downloaded


def download_from_pexels(query, count, size, output_dir):
    """
    从 Pexels API 下载图片（需要 API 密钥）
    """
    if not PEXELS_API_KEY:
        return []
    
    print(f"正在使用 Pexels API 搜索：{query}")
    
    size_config = get_image_size(size)
    downloaded = []
    
    headers = {'Authorization': PEXELS_API_KEY}
    params = {'query': query, 'per_page': count}
    
    try:
        response = requests.get(PEXELS_API_URL, headers=headers, params=params, timeout=30)
        response.raise_for_status()
        
        results = response.json().get('photos', [])
        
        for i, photo in enumerate(results[:count]):
            try:
                image_url = photo['src']['large']
                
                print(f"  下载图片 {i + 1}/{min(count, len(results))}...")
                
                img_response = requests.get(image_url, timeout=30)
                img_response.raise_for_status()
                
                safe_query = sanitize_filename(query)
                filename = f"{safe_query}-{i + 1}.jpg"
                filepath = output_dir / filename
                
                img = Image.open(BytesIO(img_response.content))
                
                if img.mode in ('RGBA', 'P'):
                    img = img.convert('RGB')
                
                img.save(filepath, 'JPEG', quality=90, optimize=True)
                
                downloaded.append(filename)
                print(f"  ✓ 已保存：{filename} ({filepath.stat().st_size // 1024}KB)")
                
            except Exception as e:
                print(f"  ✗ 下载失败：{e}")
                continue
                
    except Exception as e:
        print(f"Pexels API 请求失败：{e}")
    
    return downloaded


def download_from_unsplash_api(query, count, size, output_dir):
    """
    从 Unsplash API 下载图片（需要 API 密钥）
    提供更精确的搜索结果
    """
    if not UNSPLASH_ACCESS_KEY:
        return []

    print(f"正在使用 Unsplash API 搜索：{query}")
    
    size_config = get_image_size(size)
    downloaded = []
    
    headers = {
        'Authorization': f'Bearer {UNSPLASH_ACCESS_KEY}'
    }
    
    params = {
        'query': query,
        'per_page': min(count, 30),
        'orientation': 'landscape',
    }
    
    try:
        response = requests.get(UNSPLASH_API_URL, headers=headers, params=params, timeout=30)
        response.raise_for_status()
        
        results = response.json().get('results', [])
        
        if not results:
            print(f"  未找到相关图片")
            return downloaded
        
        for i, photo in enumerate(results[:count]):
            try:
                # 获取适合尺寸的图片 URL
                image_url = photo['urls']['regular']
                
                print(f"  下载图片 {i + 1}/{min(count, len(results))}...")
                
                img_response = requests.get(image_url, timeout=30)
                img_response.raise_for_status()
                
                # 生成文件名
                safe_query = sanitize_filename(query)
                filename = f"{safe_query}-{i + 1}.jpg"
                filepath = output_dir / filename
                
                # 保存图片
                img = Image.open(BytesIO(img_response.content))
                
                if img.mode in ('RGBA', 'P'):
                    img = img.convert('RGB')
                
                img.save(filepath, 'JPEG', quality=90, optimize=True)
                
                downloaded.append(filename)
                print(f"  ✓ 已保存：{filename} ({filepath.stat().st_size // 1024}KB)")
                
            except Exception as e:
                print(f"  ✗ 下载失败：{e}")
                continue

    except Exception as e:
        print(f"API 请求失败：{e}")

    return downloaded


def download_images(query, output_dir, count=5, size='medium', use_api=True):
    """
    下载图片的主函数

    参数:
        query: 搜索关键词
        output_dir: 输出目录
        count: 下载数量
        size: 图片尺寸 (small/medium/large/xlarge)
        use_api: 是否使用 API（自动检测已设置的 API 密钥）
    """
    # 创建输出目录
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    print(f"\n{'='*50}")
    print(f"SEO 文章图片下载器")
    print(f"{'='*50}")
    print(f"关键词：{query}")
    print(f"输出目录：{output_path.absolute()}")
    print(f"数量：{count}")
    print(f"尺寸：{size} ({get_image_size(size)['width']}x{get_image_size(size)['height']})")
    print(f"{'='*50}\n")

    downloaded = []

    # 尝试多个图片源，按优先级排列
    # 优先级 1: Pixabay API（免费，无需审核）
    if PIXABAY_API_KEY:
        print("尝试使用 Pixabay API...")
        downloaded = download_from_pixabay(query, count, size, output_path)

    # 优先级 2: Pexels API（需要 API 密钥）
    if len(downloaded) < count and PEXELS_API_KEY:
        remaining = count - len(downloaded)
        print(f"尝试使用 Pexels API 下载剩余 {remaining} 张图片...")
        downloaded += download_from_pexels(query, remaining, size, output_path)

    # 优先级 3: Unsplash API（需要 API 密钥）
    if len(downloaded) < count and UNSPLASH_ACCESS_KEY:
        remaining = count - len(downloaded)
        print(f"尝试使用 Unsplash API 下载剩余 {remaining} 张图片...")
        downloaded += download_from_unsplash_api(query, remaining, size, output_path)

    # 检查是否下载成功
    if not downloaded:
        print(f"\n{'='*50}")
        print(f"⚠️ 警告：未下载任何图片")
        print(f"{'='*50}")
        print(f"\n可能原因:")
        print(f"  1. 未设置 API 密钥（PIXABAY_API_KEY, PEXELS_API_KEY, UNSPLASH_ACCESS_KEY）")
        print(f"  2. 关键词 '{query}' 未找到相关图片")
        print(f"\n建议:")
        print(f"  - 设置至少一个 API 密钥")
        print(f"  - 尝试更具体的关键词，如 'knife blade' 而非 'metal'")
        print(f"  - 参考 assets/image-guidelines.md 中的关键词选择策略")
        print()

    print(f"\n{'='*50}")
    print(f"下载完成！")
    print(f"成功：{len(downloaded)}/{count}")
    print(f"{'='*50}\n")

    if downloaded:
        print("已下载的文件:")
        for f in downloaded:
            print(f"  - {f}")
        print(f"\n在 Markdown 中引用:")
        for f in downloaded:
            alt_text = query
            print(f"  ![{alt_text}]({output_path / f})")

    return downloaded


def main():
    parser = argparse.ArgumentParser(
        description='下载 SEO 文章相关的免版税图片',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 下载钢材相关图片
  python download_images.py --query "knife blade close-up" --output output/images/cpm20cv/

  # 下载厨房场景图片
  python download_images.py --query "chef knife professional" --output output/images/kitchen/ --count 8

  # 下载打磨工具图片
  python download_images.py --query "knife sharpening whetstone" --size large --count 5

推荐关键词（钢材文章）:
  - 开篇：knife blade close-up, steel texture
  - 硬度：hardness testing, rockwell hardness
  - 耐腐蚀：stainless steel water resistant
  - 打磨：knife sharpening whetstone
  - 厨房：chef knife professional kitchen
  - EDC: pocket knife edc folding

需要 API 密钥（至少设置一个）:
  - Pixabay: https://pixabay.com/api/docs/
  - Pexels: https://www.pexels.com/api/
  - Unsplash: https://unsplash.com/developers

设置方法:
  export PIXABAY_API_KEY="your_key_here"
  export PEXELS_API_KEY="your_key_here"
        """
    )
    
    parser.add_argument(
        '--query', '-q',
        required=True,
        help='搜索关键词（中文或英文）'
    )
    
    parser.add_argument(
        '--output', '-o',
        default='output/images',
        help='输出目录（默认：output/images/）'
    )
    
    parser.add_argument(
        '--count', '-c',
        type=int,
        default=5,
        help='下载数量（默认：5，最大：20）'
    )
    
    parser.add_argument(
        '--size', '-s',
        choices=['small', 'medium', 'large', 'xlarge'],
        default='medium',
        help='图片尺寸（默认：medium）'
    )

    args = parser.parse_args()
    
    if args.count > 20:
        print("警告：数量限制为 20")
        args.count = 20
    
    download_images(
        query=args.query,
        output_dir=args.output,
        count=args.count,
        size=args.size
    )


if __name__ == '__main__':
    main()

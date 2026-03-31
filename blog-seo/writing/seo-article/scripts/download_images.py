#!/usr/bin/env python3
"""
图片下载脚本 - 用于 SEO 文章
从 Unsplash/Picsum/Pexels 下载免版税图片

使用方法:
    python download_images.py --query "关键词" --output images/ --count 5

依赖:
    pip install requests Pillow
"""

import argparse
import os
import re
import sys
import random
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
PICSUM_URL = "https://picsum.photos"
PEXELS_API_URL = "https://api.pexels.com/v1/search"
UNSPLASH_API_URL = "https://api.unsplash.com/search/photos"

# 可选：如果有 API 密钥，可以使用更完整的 API
UNSPLASH_ACCESS_KEY = os.environ.get("UNSPLASH_ACCESS_KEY", "")
PEXELS_API_KEY = os.environ.get("PEXELS_API_KEY", "")


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


def download_from_picsum(query, count, size, output_dir):
    """
    从 Picsum 下载随机图片
    这是一个简单的方法，不需要 API 密钥
    """
    print(f"正在从 Picsum 下载图片...")
    
    size_config = get_image_size(size)
    downloaded = []
    
    # 使用随机种子下载图片
    for i in range(count):
        try:
            seed = random.randint(1, 10000)
            url = f"{PICSUM_URL}/{size_config['width']}/{size_config['height']}?random={seed}"
            
            print(f"  下载图片 {i + 1}/{count}...")
            
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            
            # 生成文件名（使用 .webp 格式）
            safe_query = sanitize_filename(query)
            filename = f"{safe_query}-{i + 1}.webp"
            filepath = output_dir / filename
            
            # 保存图片为 WebP 格式
            img = Image.open(BytesIO(response.content))
            
            # 转换为 RGB 模式（如果需要）
            if img.mode in ('RGBA', 'P'):
                img = img.convert('RGB')
            
            # 保存为 WebP 格式，质量 80，文件大小更小
            img.save(filepath, 'WEBP', quality=80, method=6)
            
            # 检查文件大小
            file_size = filepath.stat().st_size
            if file_size > 150 * 1024:  # 大于 150KB，进一步压缩
                img.save(filepath, 'WEBP', quality=65, method=6)
            
            downloaded.append(filename)
            print(f"  ✓ 已保存：{filename} ({filepath.stat().st_size // 1024}KB)")
            
        except Exception as e:
            print(f"  ✗ 下载失败：{e}")
            continue
    
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
        print("未设置 UNSPLASH_ACCESS_KEY，使用备用方法...")
        return download_from_unsplash_source(query, count, size, output_dir)
    
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
        print("回退到 Unsplash Source...")
        return download_from_unsplash_source(query, count, size, output_dir)
    
    return downloaded


def download_images(query, output_dir, count=5, size='medium', use_api=False):
    """
    下载图片的主函数
    
    参数:
        query: 搜索关键词
        output_dir: 输出目录
        count: 下载数量
        size: 图片尺寸 (small/medium/large/xlarge)
        use_api: 是否使用 API（需要密钥）
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
    
    # 尝试多个图片源
    if use_api and PEXELS_API_KEY:
        print("尝试使用 Pexels API...")
        downloaded = download_from_pexels(query, count, size, output_path)
    
    if len(downloaded) < count:
        # 如果 API 下载不足或没有 API 密钥，使用 Picsum
        remaining = count - len(downloaded)
        print(f"尝试使用 Picsum 下载剩余 {remaining} 张图片...")
        downloaded += download_from_picsum(query, remaining, size, output_path)
    
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
  python download_images.py --query "人工智能"
  python download_images.py --query "机器学习" --output article-images/ --count 10
  python download_images.py --query "数据科学" --size large --count 5
        """
    )
    
    parser.add_argument(
        '--query', '-q',
        required=True,
        help='搜索关键词（中文或英文）'
    )
    
    parser.add_argument(
        '--output', '-o',
        default='images',
        help='输出目录（默认：images/）'
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
    
    parser.add_argument(
        '--use-api',
        action='store_true',
        help='使用 Unsplash API（需要设置 UNSPLASH_ACCESS_KEY 环境变量）'
    )
    
    args = parser.parse_args()
    
    if args.count > 20:
        print("警告：数量限制为 20")
        args.count = 20
    
    download_images(
        query=args.query,
        output_dir=args.output,
        count=args.count,
        size=args.size,
        use_api=args.use_api
    )


if __name__ == '__main__':
    main()

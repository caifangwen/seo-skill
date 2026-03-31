#!/usr/bin/env python3
"""
检查 robots.txt 配置
用法：python check_robots.py <url>
"""

import sys
import urllib.request
import urllib.error
from urllib.parse import urlparse, urljoin


def check_robots_txt(url):
    """检查目标网站的 robots.txt 配置"""
    parsed = urlparse(url)
    base_url = f"{parsed.scheme}://{parsed.netloc}"
    robots_url = urljoin(base_url, "/robots.txt")
    
    print(f"检查 robots.txt: {robots_url}\n")
    
    try:
        with urllib.request.urlopen(robots_url, timeout=10) as response:
            content = response.read().decode('utf-8')
            print("✅ robots.txt 存在\n")
            print("=" * 50)
            print(content)
            print("=" * 50)
            
            analyze_robots(content)
            
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print("❌ robots.txt 不存在")
            print("建议：创建 robots.txt 文件并放置在网站根目录")
        else:
            print(f"❌ 请求失败：{e.code}")
    except Exception as e:
        print(f"❌ 错误：{e}")


def analyze_robots(content):
    """分析 robots.txt 内容"""
    lines = content.strip().split('\n')
    
    issues = []
    warnings = []
    sitemaps = []
    
    blocked_dirs = []
    user_agents = []
    
    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
            
        lower_line = line.lower()
        
        if lower_line.startswith('sitemap:'):
            sitemap_url = line.split(':', 1)[1].strip()
            sitemaps.append(sitemap_url)
            
        elif lower_line.startswith('user-agent:'):
            ua = line.split(':', 1)[1].strip()
            user_agents.append(ua)
            
        elif lower_line.startswith('disallow:'):
            path = line.split(':', 1)[1].strip()
            if path:
                blocked_dirs.append(path)
                # 检查是否误封重要目录
                critical_paths = ['/product', '/blog', '/article', '/category']
                for critical in critical_paths:
                    if path.startswith(critical) or critical.startswith(path):
                        warnings.append(f"⚠️ 可能误封重要目录：{path}")
                        
        elif lower_line.startswith('allow:'):
            path = line.split(':', 1)[1].strip()
    
    print("\n📊 分析结果\n")
    
    # User-Agent 统计
    print(f"User-Agent 数量：{len(user_agents)}")
    if '*' in user_agents:
        print("  - 包含通配符规则 (*)")
    
    # Sitemap 检查
    print(f"\nSitemap 声明：{len(sitemaps)} 个")
    if sitemaps:
        for sm in sitemaps:
            print(f"  ✅ {sm}")
    else:
        print("  ⚠️ 未声明 Sitemap（建议添加）")
    
    # 封禁目录检查
    print(f"\n封禁目录：{len(blocked_dirs)} 个")
    if blocked_dirs:
        for d in blocked_dirs[:10]:  # 只显示前 10 个
            print(f"  - {d}")
        if len(blocked_dirs) > 10:
            print(f"  ... 还有 {len(blocked_dirs) - 10} 个")
    
    # 警告
    if warnings:
        print("\n⚠️  警告:")
        for w in warnings:
            print(f"  {w}")
    
    # 建议
    print("\n💡 建议:")
    if not sitemaps:
        print("  1. 添加 Sitemap 声明：Sitemap: https://example.com/sitemap.xml")
    if '/' in blocked_dirs:
        print("  2. 注意：Disallow: / 会封禁整个网站！")
    if len(warnings) == 0 and len(sitemaps) > 0:
        print("  robots.txt 配置良好")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法：python check_robots.py <url>")
        print("示例：python check_robots.py https://example.com")
        sys.exit(1)
    
    url = sys.argv[1]
    if not url.startswith('http'):
        url = 'https://' + url
    
    check_robots_txt(url)

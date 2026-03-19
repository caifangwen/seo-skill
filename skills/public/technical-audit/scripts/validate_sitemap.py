#!/usr/bin/env python3
"""
验证 XML Sitemap 格式和内容
用法：python validate_sitemap.py <sitemap_url>
"""

import sys
import urllib.request
import urllib.error
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
from urllib.parse import urlparse


def validate_sitemap(url):
    """验证 sitemap.xml 文件"""
    print(f"验证 Sitemap: {url}\n")
    
    try:
        with urllib.request.urlopen(url, timeout=30) as response:
            content = response.read()
            
        # 解析 XML
        try:
            root = ET.fromstring(content)
        except ET.ParseError as e:
            print(f"❌ XML 解析失败：{e}")
            return
            
        # 检查命名空间
        ns = {'urlset': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
        
        # 尝试带命名空间和不带命名空间两种方式
        url_elements = root.findall('.//urlset:url', ns)
        if not url_elements:
            url_elements = root.findall('.//url')
        
        print(f"✅ XML 格式有效")
        print(f"📊 URL 数量：{len(url_elements)}\n")
        
        analyze_urls(url_elements, ns)
        
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print("❌ Sitemap 不存在 (404)")
            print("建议：创建 sitemap.xml 并在 robots.txt 中声明")
        else:
            print(f"❌ 请求失败：{e.code}")
    except Exception as e:
        print(f"❌ 错误：{e}")


def analyze_urls(url_elements, ns):
    """分析 URL 列表"""
    issues = []
    warnings = []
    
    urls_data = []
    now = datetime.now()
    seven_days_ago = now - timedelta(days=7)
    
    for url_elem in url_elements:
        # 获取 loc
        loc_elem = url_elem.find('urlset:loc', ns)
        if loc_elem is None:
            loc_elem = url_elem.find('loc')
        
        if loc_elem is None or not loc_elem.text:
            issues.append("❌ 发现 URL 缺少 <loc> 标签")
            continue
            
        loc = loc_elem.text.strip()
        
        # 获取 lastmod
        lastmod_elem = url_elem.find('urlset:lastmod', ns)
        if lastmod_elem is None:
            lastmod_elem = url_elem.find('lastmod')
        
        lastmod = None
        if lastmod_elem is not None and lastmod_elem.text:
            try:
                lastmod = datetime.fromisoformat(lastmod_elem.text[:19])
            except ValueError:
                warnings.append(f"⚠️ 日期格式问题：{loc}")
        
        # 获取 changefreq
        changefreq_elem = url_elem.find('urlset:changefreq', ns)
        if changefreq_elem is None:
            changefreq_elem = url_elem.find('changefreq')
        changefreq = changefreq_elem.text if changefreq_elem is not None else None
        
        # 获取 priority
        priority_elem = url_elem.find('urlset:priority', ns)
        if priority_elem is None:
            priority_elem = url_elem.find('priority')
        priority = priority_elem.text if priority_elem is not None else None
        
        urls_data.append({
            'loc': loc,
            'lastmod': lastmod,
            'changefreq': changefreq,
            'priority': priority
        })
        
        # 检查 lastmod 是否超过 7 天
        if lastmod and lastmod < seven_days_ago:
            warnings.append(f"⚠️ 最后更新超过 7 天：{loc} ({lastmod.date()})")
        
        # 检查 URL 格式
        parsed = urlparse(loc)
        if not parsed.scheme or not parsed.netloc:
            issues.append(f"❌ URL 格式无效：{loc}")
        elif parsed.scheme not in ['http', 'https']:
            issues.append(f"❌ URL 协议问题：{loc}")
    
    # 统计
    print("📈 统计信息\n")
    
    # lastmod 统计
    with_lastmod = sum(1 for u in urls_data if u['lastmod'])
    print(f"包含 lastmod 的 URL: {with_lastmod}/{len(urls_data)} ({with_lastmod/len(urls_data)*100:.1f}%)")
    
    # changefreq 统计
    with_changefreq = sum(1 for u in urls_data if u['changefreq'])
    print(f"包含 changefreq 的 URL: {with_changefreq}/{len(urls_data)} ({with_changefreq/len(urls_data)*100:.1f}%)")
    
    # priority 统计
    with_priority = sum(1 for u in urls_data if u['priority'])
    print(f"包含 priority 的 URL: {with_priority}/{len(urls_data)} ({with_priority/len(urls_data)*100:.1f}%)")
    
    # changefreq 分布
    if with_changefreq > 0:
        freq_dist = {}
        for u in urls_data:
            if u['changefreq']:
                freq_dist[u['changefreq']] = freq_dist.get(u['changefreq'], 0) + 1
        print("\n更新频率分布:")
        for freq, count in sorted(freq_dist.items()):
            print(f"  {freq}: {count}")
    
    # 显示前 10 个 URL
    print(f"\n📋 URL 示例（前 10 个）:")
    for u in urls_data[:10]:
        lastmod_str = u['lastmod'].strftime('%Y-%m-%d') if u['lastmod'] else 'N/A'
        print(f"  {u['loc'][:60]}... (lastmod: {lastmod_str})")
    
    # 问题和警告
    if issues:
        print("\n❌ 问题:")
        for issue in issues[:5]:
            print(f"  {issue}")
        if len(issues) > 5:
            print(f"  ... 还有 {len(issues) - 5} 个问题")
    
    if warnings:
        print("\n⚠️  警告:")
        for warning in warnings[:5]:
            print(f"  {warning}")
        if len(warnings) > 5:
            print(f"  ... 还有 {len(warnings) - 5} 个警告")
    
    # 建议
    print("\n💡 建议:")
    if with_lastmod / len(urls_data) < 0.5:
        print("  1. 为更多 URL 添加 lastmod 标签（当前覆盖率低）")
    if with_priority / len(urls_data) < 0.3:
        print("  2. 考虑添加 priority 标签帮助爬虫识别重要页面")
    if len(issues) == 0 and len(warnings) == 0:
        print("  Sitemap 状态良好")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法：python validate_sitemap.py <sitemap_url>")
        print("示例：python validate_sitemap.py https://example.com/sitemap.xml")
        sys.exit(1)
    
    url = sys.argv[1]
    validate_sitemap(url)

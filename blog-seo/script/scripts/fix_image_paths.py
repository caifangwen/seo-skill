#!/usr/bin/env python3
"""
修复文章中的图片路径 - 将绝对路径转换为相对路径
"""

import re
import sys

if len(sys.argv) < 2:
    print("用法：python fix_image_paths.py <文章路径>")
    sys.exit(1)

file_path = sys.argv[1]

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 替换绝对路径为相对路径
old_pattern = r'C:\\Users\\frida\\Downloads\\Hainer\\Hainer SKILL\\leeknives blog\\output\\images\\([^/]+)/'

def replace_path(match):
    folder_name = match.group(1)
    return f'../../images/{folder_name}/'

content = re.sub(old_pattern, replace_path, content)

# 清理 alt 文本格式：移除 ' - pipe fittings material selection' 后缀
content = re.sub(r'!\[([^\]]+) - pipe fittings material selection\]', r'![\1]', content)

# 移除图片来源说明行（多种格式）
content = re.sub(r'\n\*图片来源：Unsplash \([^)]+\)\*', '', content)
content = re.sub(r'\n\*图片来源：Pexels \([^)]+\)\*', '', content)
content = re.sub(r'\n\*图片来源：Pixabay \([^)]+\)\*', '', content)

# 清理多余的空行
content = re.sub(r'\n{3,}', '\n\n', content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('✓ 图片路径已更新完成！')
print('✓ 已转换为相对路径：../../images/asme-b16-9-guide/')
print('✓ 已清理 alt 文本和图片来源说明')

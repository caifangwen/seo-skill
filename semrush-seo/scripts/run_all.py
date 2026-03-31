#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
主运行脚本 - 一键执行完整分析流程
"""

import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
ROOT_DIR = SCRIPT_DIR.parent

def run_script(script_name: str) -> bool:
    """运行脚本并返回成功状态"""
    print(f"\n{'='*60}")
    print(f"📌 运行：{script_name}")
    print('='*60)
    
    result = subprocess.run(
        [sys.executable, str(SCRIPT_DIR / script_name)],
        cwd=str(ROOT_DIR)
    )
    return result.returncode == 0


def main():
    print("\n" + "="*60)
    print("🚀 SEO 关键词分析工具集 - 一键运行")
    print("="*60)
    
    # Step 1: 生成 AI 参考数据
    if not run_script("generate_ai_reference.py"):
        print("\n❌ Step 1 失败，终止流程")
        return
    
    # Step 2: 生成博客选题
    if not run_script("generate_blog_topics.py"):
        print("\n❌ Step 2 失败")
        return
    
    print("\n" + "="*60)
    print("✅ 全部完成!")
    print("="*60)
    print("\n📁 输出位置:")
    print("   - output/analysis_results/  (关键词数据)")
    print("   - output/blog_topics/       (选题建议)")
    print("\n📄 查看报告:")
    print("   - output/analysis_results/seo_insights_*.md")
    print("   - output/blog_topics/blog_topic_report_*.md")
    print()


if __name__ == "__main__":
    main()

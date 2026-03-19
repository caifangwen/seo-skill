#!/usr/bin/env python3
"""
执行单个 Skill 的测试
用法：python run_eval.py --skill <skill_name> --eval-file <eval_file.json>
"""

import argparse
import json
import sys
import os
from pathlib import Path


def load_evals(eval_file):
    """加载测试用例"""
    with open(eval_file, 'r', encoding='utf-8') as f:
        return json.load(f)


def run_eval(skill_name, eval_data):
    """执行测试"""
    print(f"\n{'='*60}")
    print(f"Skill: {skill_name}")
    print(f"版本：{eval_data.get('version', 'N/A')}")
    print(f"{'='*60}\n")
    
    evals = eval_data.get('evals', [])
    results = []
    
    for i, eval_case in enumerate(evals, 1):
        eval_id = eval_case.get('id', i)
        description = eval_case.get('description', f'测试 {i}')
        prompt = eval_case.get('prompt', '')
        expectations = eval_case.get('expectations', [])
        files = eval_case.get('files', [])
        
        print(f"\n📋 测试 {i}: {description}")
        print(f"   Prompt: {prompt[:80]}..." if len(prompt) > 80 else f"   Prompt: {prompt}")
        
        # 检查文件是否存在
        file_status = "✅"
        for file_path in files:
            if not os.path.exists(file_path):
                file_status = "⚠️ 文件缺失"
                break
        
        print(f"   附件：{file_status if files else '无'}")
        print(f"   期望检查点：{len(expectations)} 项")
        
        # 模拟测试结果（实际需要调用 Claude API）
        # 这里只输出测试框架
        result = {
            'id': eval_id,
            'description': description,
            'status': 'pending',  # pending / passed / failed
            'expectations': expectations,
            'notes': '需要 Claude API 执行实际测试'
        }
        results.append(result)
        
        print(f"   状态：⏳ pending (需要 Claude API)")
    
    # 统计
    print(f"\n{'='*60}")
    print(f"测试完成")
    print(f"总计：{len(results)} 个测试用例")
    print(f"通过：0 (需要实际执行)")
    print(f"待执行：{len(results)}")
    print(f"{'='*60}\n")
    
    return results


def main():
    parser = argparse.ArgumentParser(description='执行单个 Skill 的测试')
    parser.add_argument('--skill', required=True, help='Skill 名称')
    parser.add_argument('--eval-file', required=True, help='测试用例 JSON 文件路径')
    parser.add_argument('--output', help='输出结果文件路径')
    
    args = parser.parse_args()
    
    # 加载测试用例
    try:
        eval_data = load_evals(args.eval_file)
    except FileNotFoundError:
        print(f"❌ 文件不存在：{args.eval_file}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"❌ JSON 解析失败：{e}")
        sys.exit(1)
    
    # 执行测试
    results = run_eval(args.skill, eval_data)
    
    # 输出结果
    if args.output:
        output_data = {
            'skill': args.skill,
            'version': eval_data.get('version', 'N/A'),
            'results': results
        }
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, ensure_ascii=False, indent=2)
        print(f"📄 结果已保存至：{args.output}")


if __name__ == "__main__":
    main()

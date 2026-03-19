#!/usr/bin/env python3
"""
执行所有 Skill 的测试
用法：python run_all_evals.py [--skills-path <path>] [--output <file>] [--benchmark] [--verbose]
"""

import argparse
import json
import sys
from pathlib import Path
from datetime import datetime


def find_skills(skills_path):
    """查找所有 Skill"""
    skills = []
    skills_dir = Path(skills_path)

    if not skills_dir.exists():
        print(f"❌ 目录不存在：{skills_path}")
        return skills

    for skill_dir in skills_dir.iterdir():
        if skill_dir.is_dir():
            skill_file = skill_dir / "SKILL.md"
            eval_file = skill_dir / "evals" / "evals.json"
            trigger_eval_file = skill_dir / "evals" / "trigger_evals.json"

            if skill_file.exists():
                skills.append({
                    'name': skill_dir.name,
                    'path': str(skill_dir),
                    'skill_file': str(skill_file),
                    'eval_file': str(eval_file) if eval_file.exists() else None,
                    'trigger_eval_file': str(trigger_eval_file) if trigger_eval_file.exists() else None
                })

    return skills


def load_evals(eval_file):
    """加载测试用例"""
    try:
        with open(eval_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"⚠️ 加载失败 {eval_file}: {e}")
        return None


def run_trigger_evals(skill_name, eval_data):
    """执行触发准确性测试"""
    evals = eval_data.get('evals', [])
    results = []

    for eval_case in evals:
        prompt = eval_case.get('prompt', '')
        should_trigger = eval_case.get('should_trigger', None)

        # 模拟测试结果
        result = {
            'prompt': prompt,
            'should_trigger': should_trigger,
            'actual_trigger': 'pending',  # 需要实际执行
            'status': 'pending'
        }
        results.append(result)

    return results


def run_all_evals(skills, verbose=False):
    """执行所有测试"""
    all_results = {
        'timestamp': datetime.now().isoformat(),
        'skills': []
    }

    for skill in skills:
        print(f"\n{'='*60}")
        print(f"Skill: {skill['name']}")
        print(f"路径：{skill['path']}")
        print(f"{'='*60}")

        skill_result = {
            'name': skill['name'],
            'path': skill['path'],
            'functional_evals': [],
            'trigger_evals': []
        }

        # 功能测试
        if skill['eval_file']:
            print("\n📋 功能测试:")
            eval_data = load_evals(skill['eval_file'])
            if eval_data:
                evals = eval_data.get('evals', [])
                print(f"   测试用例数：{len(evals)}")
                for eval_case in evals:
                    eval_result = {
                        'id': eval_case.get('id', 0),
                        'description': eval_case.get('description', ''),
                        'status': 'pending'
                    }
                    skill_result['functional_evals'].append(eval_result)
                    if verbose:
                        print(f"   - {eval_case.get('description', 'N/A')}")

        # 触发测试
        if skill['trigger_eval_file']:
            print("\n📋 触发准确性测试:")
            eval_data = load_evals(skill['trigger_eval_file'])
            if eval_data:
                evals = eval_data.get('evals', [])
                print(f"   测试用例数：{len(evals)}")
                trigger_results = run_trigger_evals(skill['name'], eval_data)
                skill_result['trigger_evals'] = trigger_results
                if verbose:
                    for r in trigger_results:
                        trigger_status = "应触发" if r['should_trigger'] else "不应触发"
                        print(f"   - [{trigger_status}] {r['prompt'][:50]}...")

        all_results['skills'].append(skill_result)

    return all_results


def print_summary(results):
    """打印摘要"""
    print("\n" + "="*60)
    print("📊 测试摘要")
    print("="*60)

    total_skills = len(results['skills'])
    total_functional = sum(len(s['functional_evals']) for s in results['skills'])
    total_trigger = sum(len(s['trigger_evals']) for s in results['skills'])

    print(f"Skill 数量：{total_skills}")
    print(f"功能测试用例：{total_functional}")
    print(f"触发测试用例：{total_trigger}")
    print(f"总测试用例：{total_functional + total_trigger}")
    print("状态：待执行 (需要 Claude API)")
    print("="*60 + "\n")


def main():
    parser = argparse.ArgumentParser(description='执行所有 Skill 的测试')
    parser.add_argument('--skills-path', default='skills/public',
                        help='Skill 目录路径 (默认：skills/public)')
    parser.add_argument('--output', help='输出结果文件路径')
    parser.add_argument('--benchmark', action='store_true',
                        help='执行 benchmark 对比')
    parser.add_argument('--verbose', '-v', action='store_true',
                        help='详细输出')
    parser.add_argument('--threshold', type=float, default=0.80,
                        help='通过率阈值 (默认：0.80)')

    args = parser.parse_args()

    # 查找 Skills
    print(f"🔍 查找 Skills: {args.skills_path}")
    skills = find_skills(args.skills_path)

    if not skills:
        print("❌ 未找到任何 Skill")
        sys.exit(1)

    print(f"✅ 找到 {len(skills)} 个 Skill:")
    for skill in skills:
        print(f"   - {skill['name']}")

    # 执行测试
    results = run_all_evals(skills, verbose=args.verbose)

    # 打印摘要
    print_summary(results)

    # 保存结果
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        print(f"📄 结果已保存至：{args.output}")

    # Benchmark 模式
    if args.benchmark:
        print("\n📈 Benchmark 模式")
        print("需要配置无 Skill 对照组进行对比测试")
        print("请参考 docs/CONTRIBUTING.md 中的 Benchmark 配置说明")


if __name__ == "__main__":
    main()

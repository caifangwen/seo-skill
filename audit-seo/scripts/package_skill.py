#!/usr/bin/env python3
"""
打包 Skill 用于分发
用法：python package_skill.py --skill <skill_name> --output <output_dir>
"""

import argparse
import json
import shutil
from pathlib import Path
from datetime import datetime


def load_skill_info(skill_path):
    """加载 Skill 信息"""
    skill_file = Path(skill_path) / "SKILL.md"

    if not skill_file.exists():
        return None

    with open(skill_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 解析 frontmatter
    info = {}
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 2:
            frontmatter = parts[1].strip()
            for line in frontmatter.split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    value = value.strip().strip('"\'')
                    info[key.strip()] = value

    return info


def package_skill(skill_name, skills_path, output_dir):
    """打包单个 Skill"""
    skill_dir = Path(skills_path) / skill_name

    if not skill_dir.exists():
        print(f"❌ Skill 不存在：{skill_dir}")
        return None

    # 创建输出目录
    output_path = Path(output_dir) / f"{skill_name}-skill"
    if output_path.exists():
        shutil.rmtree(output_path)
    output_path.mkdir(parents=True)

    # 复制文件
    print(f"📦 打包 {skill_name}...")

    files_copied = []

    # 复制 SKILL.md
    skill_file = skill_dir / "SKILL.md"
    if skill_file.exists():
        shutil.copy2(skill_file, output_path / "SKILL.md")
        files_copied.append("SKILL.md")

    # 复制 references
    refs_dir = skill_dir / "references"
    if refs_dir.exists():
        output_refs = output_path / "references"
        shutil.copytree(refs_dir, output_refs)
        ref_count = len(list(refs_dir.rglob('*')))
        files_copied.append(f"references/ ({ref_count} 文件)")

    # 复制 scripts
    scripts_dir = skill_dir / "scripts"
    if scripts_dir.exists():
        output_scripts = output_path / "scripts"
        shutil.copytree(scripts_dir, output_scripts)
        script_count = len(list(scripts_dir.rglob('*')))
        files_copied.append(f"scripts/ ({script_count} 文件)")

    # 复制 assets
    assets_dir = skill_dir / "assets"
    if assets_dir.exists():
        output_assets = output_path / "assets"
        shutil.copytree(assets_dir, output_assets)
        asset_count = len(list(assets_dir.rglob('*')))
        files_copied.append(f"assets/ ({asset_count} 文件)")

    # 复制 evals (可选，public skills 才包含)
    evals_dir = skill_dir / "evals"
    if evals_dir.exists() and 'private' not in str(skill_dir):
        output_evals = output_path / "evals"
        shutil.copytree(evals_dir, output_evals)
        eval_count = len(list(evals_dir.rglob('*')))
        files_copied.append(f"evals/ ({eval_count} 文件)")

    # 创建 package.json
    skill_info = load_skill_info(skill_dir)
    package_info = {
        'name': skill_name,
        'version': skill_info.get('version', '1.0.0') if skill_info else '1.0.0',
        'description': skill_info.get('description', '') if skill_info else '',
        'packaged_at': datetime.now().isoformat(),
        'files': files_copied
    }

    with open(output_path / "package.json", 'w', encoding='utf-8') as f:
        json.dump(package_info, f, ensure_ascii=False, indent=2)
    files_copied.append("package.json")

    # 创建 README
    readme_content = f"""# {skill_name} Skill

**版本：** {package_info['version']}
**打包日期：** {package_info['packaged_at']}

## 安装

将此 Skill 复制到您的项目的 `skills/` 目录下。

## 使用

在 Claude Code 中打开项目后，执行相关任务会自动触发此 Skill。

## 文件结构

"""

    for file_info in files_copied:
        readme_content += f"- {file_info}\n"

    readme_content += """
## 许可证

请参考主项目许可证
"""

    with open(output_path / "README.md", 'w', encoding='utf-8') as f:
        f.write(readme_content)
    files_copied.append("README.md")

    # 创建压缩包
    archive_path = shutil.make_archive(str(output_path), 'zip', output_path.parent, output_path.name)

    print(f"✅ 打包完成:")
    for file_info in files_copied:
        print(f"   - {file_info}")
    print(f"\n📦 压缩包：{archive_path}")

    return archive_path


def main():
    parser = argparse.ArgumentParser(description="打包 Skill 用于分发")
    parser.add_argument('--skill', required=True, help='Skill 名称')
    parser.add_argument('--skills-path', default='skills/public',
                        help='Skill 目录路径 (默认：skills/public)')
    parser.add_argument('--output', default='dist',
                        help='输出目录 (默认：dist)')

    args = parser.parse_args()

    # 创建输出目录
    Path(args.output).mkdir(exist_ok=True)

    # 打包
    archive_path = package_skill(args.skill, args.skills_path, args.output)

    if archive_path:
        print("\n💡 提示：将压缩包分发给用户后，解压到项目的 skills/ 目录即可")


if __name__ == "__main__":
    main()

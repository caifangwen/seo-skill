#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
产品 SEO 批量生成工具 v2.5
支持自定义类别文件夹、自定义目标列、Token 优化
"""

import csv
import json
import os
import re
import sys
import time
import requests
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# ==================== 配置区域 ====================

API_KEY_DEFAULT  = os.environ.get("AI_API_KEY", "")
API_URL_DEFAULT  = os.environ.get("AI_API_URL", "https://api.deepseek.com/v1/chat/completions")
MODEL_DEFAULT    = os.environ.get("AI_MODEL", "deepseek-chat")
BATCH_SIZE       = int(os.environ.get("AI_BATCH_SIZE", "5"))
RATE_LIMIT       = float(os.environ.get("AI_RATE_LIMIT", "0.5"))

# 类别配置（硬编码的类别，带中文描述）
CATEGORIES = {
    "1": ("Japanese-Knives",  "日式刀具"),
    "2": ("Chinese-Knives",   "中式刀具"),
    "3": ("Western-Knives",   "西式刀具"),
    "4": ("Cookware",         "厨具"),
    "5": ("Axes-Outdoor",     "户外工具"),
    "6": ("Accessories",      "配件"),
    "7": ("Pocket-Knives",    "口袋刀"),
}

# 目标列定义
ALL_TARGET_COLUMNS = {
    "short_desc":  {"csv_col": "Short description",                "label": "短描述 HTML",      "token_heavy": True},
    "description": {"csv_col": "Description",                      "label": "长描述 HTML",      "token_heavy": True},
    "seo_title":   {"csv_col": "Meta: rank_math_title",            "label": "SEO 标题",         "token_heavy": False},
    "meta_desc":   {"csv_col": "Meta: rank_math_description",      "label": "Meta 描述",        "token_heavy": False},
    "focus_kw":    {"csv_col": "Meta: rank_math_focus_keyword",    "label": "Focus 关键词",     "token_heavy": False},
}

# ==================== 路径 ====================

BASE_DIR        = Path(__file__).parent
CATEGORIES_DIR  = BASE_DIR / "categories"
OUTPUT_DIR      = BASE_DIR / "output"
CONFIG_FILE     = BASE_DIR / ".seo_config.json"
BASE_PROMPT     = BASE_DIR / "prompt_base.md"

# ==================== 配置读写 ====================

def load_config() -> dict:
    if CONFIG_FILE.exists():
        try:
            return json.loads(CONFIG_FILE.read_text("utf-8"))
        except Exception:
            pass
    return {}

def save_config(cfg: dict):
    CONFIG_FILE.write_text(json.dumps(cfg, indent=2, ensure_ascii=False), "utf-8")

def get_api_config() -> Tuple[str, str, str]:
    cfg = load_config()
    return (
        cfg.get("api_key",  API_KEY_DEFAULT),
        cfg.get("api_url",  API_URL_DEFAULT),
        cfg.get("model",    MODEL_DEFAULT),
    )

def save_api_config(api_key: str, api_url: str, model: str):
    cfg = load_config()
    cfg.update({"api_key": api_key, "api_url": api_url, "model": model})
    save_config(cfg)

def get_saved_columns() -> Optional[List[str]]:
    return load_config().get("target_columns", None)

def save_columns(cols: List[str]):
    cfg = load_config()
    cfg["target_columns"] = cols
    save_config(cfg)

# ==================== 列选择 ====================

def select_target_columns(preselected: Optional[List[str]] = None) -> List[str]:
    all_keys = list(ALL_TARGET_COLUMNS.keys())

    if preselected:
        valid = [k for k in preselected if k in ALL_TARGET_COLUMNS]
        if valid:
            return valid
        print(f"[警告] 指定的列无效：{preselected}，将进入交互选择")

    saved = get_saved_columns() or all_keys

    print("\n" + "=" * 50)
    print("请选择要生成的列：")
    print("=" * 50)
    for i, key in enumerate(all_keys, 1):
        info = ALL_TARGET_COLUMNS[key]
        default = "●" if key in saved else "○"
        heavy = " [长文本]" if info["token_heavy"] else ""
        print(f"  {i}. [{default}] {info['label']}{heavy}")
    print()
    print("  输入编号切换选中（空格分隔），回车使用默认")
    print("  all=全选，light=仅短字段")
    print()
    raw = input("你的选择：").strip().lower()

    if raw == "":
        selected = saved
    elif raw == "all":
        selected = all_keys
    elif raw == "light":
        selected = [k for k, v in ALL_TARGET_COLUMNS.items() if not v["token_heavy"]]
    else:
        selected = list(saved)
        for token in raw.split():
            try:
                idx = int(token) - 1
                key = all_keys[idx]
                if key in selected:
                    selected.remove(key)
                else:
                    selected.append(key)
            except (ValueError, IndexError):
                pass

    if not selected:
        print("[警告] 未选择任何列，使用全部列")
        selected = all_keys

    save_columns(selected)

    print("\n已选择：")
    for k in selected:
        print(f"  + {ALL_TARGET_COLUMNS[k]['label']}")
    return selected

# ==================== Prompt 构建 ====================

def load_prompt_template(category_dir: Path) -> str:
    if BASE_PROMPT.exists():
        base_text = BASE_PROMPT.read_text("utf-8").strip()
    else:
        print(f"  [警告] prompt_base.md 不存在")
        base_text = ""

    cat_fp = category_dir / "prompt.md"
    if not cat_fp.exists():
        raise FileNotFoundError(f"类别 prompt 不存在：{cat_fp}")
    cat_text = cat_fp.read_text("utf-8").strip()

    merged = (base_text + "\n\n" + cat_text) if base_text else cat_text

    missing = [p for p in ["{{product_list}}", "{{output_spec}}"] if p not in merged]
    if missing:
        merged += "\n\n{{product_list}}\n\n{{output_spec}}"

    return merged

def extract_product_info(row: Dict[str, str]) -> Dict[str, str]:
    name = row.get("Name", "")
    sku  = row.get("SKU", "")
    cats = row.get("Categories", "")

    def _match(pattern):
        m = re.search(pattern, name, re.IGNORECASE)
        return m.group(1) if m else ""

    material = _match(r'(Damascus|VG-?10|9Cr18MoV|8Cr13MoV|65Mn|4Cr13|1055|10Cr15MoV|SG2|R2|AUS-10|S35VN|M390|ZDP-189|Blue Steel|White Steel|Shirogami|Aogami|Tsuchime|Mirror Finish|Hammered|Stonewash|10Cr15CoMoV|5Cr15MoV)')
    size     = _match(r'(\d{2,3}\s*mm)')
    handle   = _match(r'(Rosewood|African Blackwood|Stabilized Wood|Hickory|Walnut|Oak|Beech|G10|Micarta|Pakka Wood|Ebony)')

    return {
        "name":     name,
        "sku":      sku,
        "cats":     cats,
        "material": material,
        "size":     size,
        "handle":   handle,
        "_row":     row,
    }

def build_output_spec(target_cols: List[str]) -> str:
    lines = ["Output JSON array with these fields only:"]
    for k in target_cols:
        info = ALL_TARGET_COLUMNS[k]
        lines.append(f'  "{k}": {info["label"]}')
    return "\n".join(lines)

def generate_batch_prompt(products: List[Dict], prompt_template: str,
                          target_cols: List[str], variables: dict = None) -> str:
    product_lines = []
    for i, p in enumerate(products, 1):
        parts = [f"{i}. {p['name']}"]
        if p["sku"]:      parts.append(f"   SKU:{p['sku']}")
        if p["material"]: parts.append(f"   Material:{p['material']}")
        if p["size"]:     parts.append(f"   Size:{p['size']}")
        if p["handle"]:   parts.append(f"   Handle:{p['handle']}")
        product_lines.append("\n".join(parts))
    product_list = "\n\n".join(product_lines)

    prompt = prompt_template.replace("{{product_list}}", product_list)

    output_spec = build_output_spec(target_cols)
    if "{{output_spec}}" in prompt:
        prompt = prompt.replace("{{output_spec}}", output_spec)
    else:
        prompt += f"\n\n---\n{output_spec}\nOutput JSON array only, no markdown."

    if variables:
        for k, v in variables.items():
            prompt = prompt.replace(f"{{{{{k}}}}}", v or "")

    return prompt

# ==================== AI 调用 ====================

def call_ai_api(prompt: str, api_key: str, api_url: str, model: str,
                max_retries: int = 3) -> str:
    if not api_key:
        raise ValueError("未设置 API Key")

    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are an SEO copywriting expert for B2B kitchenware wholesale. Return only valid JSON arrays, no explanations."},
            {"role": "user",   "content": prompt},
        ],
        "temperature": 0.5,
        "max_tokens": 4000,
    }

    for attempt in range(max_retries):
        try:
            resp = requests.post(api_url, headers=headers, json=payload, timeout=120)
            resp.raise_for_status()
            return resp.json()["choices"][0]["message"]["content"]
        except (requests.exceptions.Timeout, requests.exceptions.RequestException) as e:
            wait = 3 * (attempt + 1)
            if attempt < max_retries - 1:
                print(f" [重试 {attempt+1}/{max_retries-1} 等待 {wait}s]", end="", flush=True)
                time.sleep(wait)
            else:
                raise
    return ""

# ==================== JSON 解析 ====================

def parse_ai_response(text: str, products: List[Dict], target_cols: List[str]) -> List[Dict]:
    text = text.strip()
    text = re.sub(r"^```(?:json)?\s*", "", text)
    text = re.sub(r"\s*```$", "", text)
    text = text.strip()

    if not text.endswith("]"):
        last_brace = text.rfind("}")
        if last_brace > 0:
            text = text[:last_brace + 1]
        text += "]"

    try:
        results = json.loads(text)
        if isinstance(results, dict):
            results = [results]
    except json.JSONDecodeError as e:
        print(f"\n    [JSON 解析失败] {e}")
        blocks = re.findall(r'\{[^{}]+\}', text, re.DOTALL)
        if blocks:
            try:
                results = [json.loads(b) for b in blocks]
            except Exception:
                results = []
        else:
            results = []

    empty = {k: "" for k in target_cols}
    for i, p in enumerate(products):
        ai = results[i] if i < len(results) else {}
        for k in target_cols:
            p[f"ai_{k}"] = ai.get(k, "")
        if not any(p.get(f"ai_{k}") for k in target_cols):
            p.update({f"ai_{k}": "" for k in target_cols})
    return products

# ==================== CSV 处理 ====================

def skip_row(row: Dict, target_cols: List[str]) -> bool:
    for k in target_cols:
        csv_col = ALL_TARGET_COLUMNS[k]["csv_col"]
        if not row.get(csv_col, "").strip():
            return False
    return True

def process_category(category_dir: Path, api_key: str, api_url: str, model: str,
                     target_cols: List[str], force: bool = False) -> Tuple[int, int]:
    processed = skipped = 0
    use_ai = bool(api_key)

    # 确保输出目录存在
    OUTPUT_DIR.mkdir(exist_ok=True)

    variables: Dict[str, str] = {}
    cfg_file = category_dir / "config.json"
    if cfg_file.exists():
        try:
            cat_cfg = json.loads(cfg_file.read_text("utf-8"))
            for k, v in cat_cfg.get("variables", {}).items():
                variables[k] = v.get("value", v) if isinstance(v, dict) else v
        except Exception:
            pass

    try:
        prompt_template = load_prompt_template(category_dir)
        base_status = "OK" if BASE_PROMPT.exists() else "MISSING"
        print(f"  [{base_status}] {category_dir.name}/prompt.md")
    except FileNotFoundError as e:
        print(f"  [ERROR] {e}")
        prompt_template = ""

    csv_files = sorted(category_dir.glob("products-*.csv"))
    if not csv_files:
        print("  [ERROR] 未找到 CSV 文件")
        return 0, 0

    for csv_file in csv_files:
        print(f"\n  -> {csv_file.name}")

        # 输出文件路径
        output_file = OUTPUT_DIR / csv_file.name

        with open(csv_file, "r", encoding="utf-8-sig") as f:
            reader     = csv.DictReader(f)
            fieldnames = list(reader.fieldnames or [])
            rows       = list(reader)

        for k in target_cols:
            col = ALL_TARGET_COLUMNS[k]["csv_col"]
            if col not in fieldnames:
                fieldnames.append(col)

        if not use_ai or not prompt_template:
            print("    [SKIP] 无 API Key 或 Prompt")
            processed += len(rows)
            continue

        to_process = []
        row_indices = []
        for idx, row in enumerate(rows):
            if not force and skip_row(row, target_cols):
                skipped += 1
            else:
                to_process.append(extract_product_info(row))
                row_indices.append(idx)

        if not to_process:
            print(f"    [SKIP] 全部 {len(rows)} 行已有内容 (--force 强制覆盖)")
            continue

        print(f"    待处理 {len(to_process)} 行 (已跳过 {skipped} 行)")
        print(f"    目标列：{', '.join(ALL_TARGET_COLUMNS[k]['label'] for k in target_cols)}")
        print(f"    批次大小：{BATCH_SIZE}")

        all_results: List[Dict] = []
        total_batches = (len(to_process) + BATCH_SIZE - 1) // BATCH_SIZE

        for batch_idx in range(0, len(to_process), BATCH_SIZE):
            batch     = to_process[batch_idx:batch_idx + BATCH_SIZE]
            batch_num = batch_idx // BATCH_SIZE + 1
            print(f"    批次 {batch_num}/{total_batches} ({len(batch)} 个)...", end=" ", flush=True)

            try:
                prompt   = generate_batch_prompt(batch, prompt_template, target_cols, variables)
                response = call_ai_api(prompt, api_key, api_url, model)
                results  = parse_ai_response(response, batch, target_cols)
                all_results.extend(results)
                print("OK")
            except Exception as e:
                print(f"ERROR: {e}")
                for p in batch:
                    for k in target_cols:
                        p[f"ai_{k}"] = ""
                all_results.extend(batch)

            if batch_idx + BATCH_SIZE < len(to_process):
                time.sleep(max(0.1, 1.0 / RATE_LIMIT))

        for result_idx, row_idx in enumerate(row_indices):
            if result_idx < len(all_results):
                prod = all_results[result_idx]
                for k in target_cols:
                    val = prod.get(f"ai_{k}", "")
                    if val:
                        rows[row_idx][ALL_TARGET_COLUMNS[k]["csv_col"]] = val
            processed += 1

        # 写入到 output 目录
        with open(output_file, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
            writer.writeheader()
            writer.writerows(rows)
        print(f"    [OK] output/{output_file.name}")

    return processed, skipped

# ==================== API 配置交互 ====================

def input_api_config() -> Tuple[str, str, str]:
    cur_key, cur_url, cur_model = get_api_config()
    print("\n" + "=" * 50)
    print("API 配置（回车保留现有值）")
    print("=" * 50)
    display_key = (cur_key[:8] + "...") if len(cur_key) > 8 else (cur_key or "(未设置)")
    print(f"当前 Key: {display_key}  URL: {cur_url}  Model: {cur_model}\n")

    api_key = input(f"API Key [{display_key}]: ").strip() or cur_key
    api_url = input(f"API URL [{cur_url}]: ").strip()     or cur_url
    model   = input(f"Model   [{cur_model}]: ").strip()    or cur_model

    if api_key:
        save_api_config(api_key, api_url, model)
        print("[OK] 配置已保存")
    else:
        print("[ERROR] 未设置 API Key")
    return api_key, api_url, model

# ==================== 菜单 ====================

def show_menu(api_key: str, model: str):
    status = "OK" if api_key else "NOT SET"
    saved  = get_saved_columns() or list(ALL_TARGET_COLUMNS.keys())
    cols   = ", ".join(ALL_TARGET_COLUMNS[k]["label"] for k in saved)
    print("\n" + "=" * 55)
    print("  产品 SEO 批量生成工具 v2.5")
    print("=" * 55)
    print(f"  API: {status}  Model: {model}")
    print(f"  目标列：{cols}")
    print("-" * 55)
    for key, (name, desc) in CATEGORIES.items():
        cat_dir = CATEGORIES_DIR / name
        csv_cnt = len(list(cat_dir.glob("products-*.csv"))) if cat_dir.exists() else 0
        print(f"  {key}. {desc:<15} ({name})  [{csv_cnt} CSV]")
    print("  A. 处理所有类别")
    print("  N. 输入类别文件夹名（新类别）")
    print("  C. 选择目标列")
    print("  S. 设置 API")
    print("  0. 退出")
    print()

# ==================== 主函数 ====================

def main():
    args = sys.argv[1:]

    def pop_flag(*flags) -> bool:
        for f in flags:
            if f in args:
                args.remove(f)
                return True
        return False

    def pop_value(*flags) -> Optional[str]:
        for f in flags:
            if f in args:
                i = args.index(f)
                args.remove(f)
                return args.pop(i) if i < len(args) else None
        return None

    def pop_values(*flags) -> List[str]:
        for f in flags:
            if f in args:
                i = args.index(f)
                args.remove(f)
                vals = []
                while i < len(args) and not args[i].startswith("-"):
                    vals.append(args.pop(i))
                return vals
        return []

    show_help   = pop_flag("--help", "-h")
    do_config   = pop_flag("--config", "-c")
    do_all      = pop_flag("--all", "-a")
    force       = pop_flag("--force", "-f")
    single_key  = pop_value("--single", "-s")
    col_keys    = pop_values("--cols")

    if show_help:
        print("""
用法：python generate_product_seo.py [选项]

模式选项:
  (无参数)            交互菜单
  --all,   -a         处理所有类别
  --single, -s <KEY>  处理单个类别（KEY=1~7 或文件夹名）
  --config, -c        设置 API Key / URL / Model

列选项:
  --cols <k1 k2 ...>  指定生成的列（空格分隔）
      可选值：short_desc  description  seo_title  meta_desc  focus_kw
  示例：--cols focus_kw seo_title meta_desc

其他:
  --force, -f         强制覆盖已有内容
  --help,  -h         显示帮助
        """)
        return

    api_key, api_url, model = get_api_config()

    if do_config:
        api_key, api_url, model = input_api_config()
        return

    if not api_key:
        print("[WARN] 未配置 API Key，AI 功能不可用。使用 --config 设置。")

    if col_keys:
        target_cols = [k for k in col_keys if k in ALL_TARGET_COLUMNS]
        if not target_cols:
            print(f"[ERROR] 无效列名：{col_keys}")
            return
        print(f"目标列（命令行）: {', '.join(ALL_TARGET_COLUMNS[k]['label'] for k in target_cols)}")
    else:
        target_cols = get_saved_columns() or list(ALL_TARGET_COLUMNS.keys())

    # 运行
    if do_all:
        print(f"\n处理所有类别，目标列：{', '.join(ALL_TARGET_COLUMNS[k]['label'] for k in target_cols)}\n")
        total = 0
        for key, (name, desc) in CATEGORIES.items():
            cat_dir = CATEGORIES_DIR / name
            if cat_dir.exists():
                print(f"\n[{desc}]")
                p, _ = process_category(cat_dir, api_key, api_url, model, target_cols, force)
                total += p
        print(f"\n完成！共处理 {total} 个产品")
        return

    if single_key:
        # 支持直接输入文件夹名称
        if single_key in CATEGORIES:
            name, desc = CATEGORIES[single_key]
        else:
            name = single_key
            desc = single_key
        cat_dir = CATEGORIES_DIR / name
        if not cat_dir.exists():
            print(f"类别目录不存在：{cat_dir}")
            return
        print(f"\n处理：{desc}")
        p, s = process_category(cat_dir, api_key, api_url, model, target_cols, force)
        print(f"\n完成！处理 {p} 个，跳过 {s} 个")
        return

    # 交互菜单
    while True:
        show_menu(api_key, model)
        choice = input("输入选项：").strip().upper()

        if choice == "0":
            break
        elif choice == "S":
            api_key, api_url, model = input_api_config()
        elif choice == "C":
            target_cols = select_target_columns()
        elif choice == "A":
            print()
            for key, (name, desc) in CATEGORIES.items():
                cat_dir = CATEGORIES_DIR / name
                if cat_dir.exists():
                    print(f"\n[{desc}]")
                    process_category(cat_dir, api_key, api_url, model, target_cols, force)
        elif choice == "N":
            folder_name = input("请输入类别文件夹名：").strip()
            if folder_name:
                cat_dir = CATEGORIES_DIR / folder_name
                if cat_dir.exists():
                    print(f"\n处理：{folder_name}")
                    process_category(cat_dir, api_key, api_url, model, target_cols, force)
                else:
                    print(f"目录不存在：{cat_dir}")
        elif choice in CATEGORIES:
            name, desc = CATEGORIES[choice]
            cat_dir = CATEGORIES_DIR / name
            if cat_dir.exists():
                print(f"\n处理：{desc}")
                process_category(cat_dir, api_key, api_url, model, target_cols, force)
            else:
                print(f"目录不存在：{cat_dir}")
        else:
            print("无效选项")


if __name__ == "__main__":
    main()

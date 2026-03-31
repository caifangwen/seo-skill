# 产品 SEO 批量生成工具

基于 AI 的产品 SEO 内容批量生成工具，专为 WooCommerce 电商网站设计。

## 📁 项目结构

```
leeknivs-product-seo/
├── run.bat                      # Windows 启动脚本（双击运行）
├── generate_product_seo.py      # 主程序
├── seo_diagnosis_dashboard.html # SEO 诊断面板
├── categories/                  # 产品类别目录
│   ├── prompt_base.md          # 全局通用 Prompt 模板（必须存在）
│   ├── Japanese-Knives/        # 类别文件夹
│   │   ├── prompt.md           # 类别专属 Prompt
│   │   ├── config.json         # 可选：类别变量配置
│   │   └── products-*.csv      # 产品 CSV 文件
│   ├── Chinese-Knives/
│   ├── Western-Knives/
│   ├── Cookware/
│   ├── Axes-Outdoor/
│   ├── Accessories/
│   └── Pocket-Knives/
└── output/                      # 输出目录（处理后文件）
```

## 🚀 BAT 使用说明

### 三步流程

运行 `run.bat` 后按顺序完成三个步骤：

#### Step 1: API 配置
- 已配置：询问是否修改
- 未配置：提示设置 API Key

#### Step 2: 选择处理范围
| 选项 | 说明 |
|------|------|
| `A` | 处理所有类别 |
| `1-7` | 预设类别（1=日式刀具，2=中式刀具...） |
| `N` | 自定义文件夹名（新类别） |

#### Step 3: 选择生成列
| 选项 | 生成列 | 说明 |
|------|--------|------|
| `L` | focus_kw + seo_title + meta_desc | 轻量模式（省 Token） |
| `A` | 全部 5 列 | 完整生成 |
| `C` | 自定义 | 输入列序号，如 `3 4 5` |
| `1-5` | 单列 | 仅生成指定列 |

**列序号对照：**
1. 短描述 HTML (Short description)
2. 长描述 HTML (Description)
3. SEO 标题 (Meta: rank_math_title)
4. Meta 描述 (Meta: rank_math_description)
5. Focus 关键词 (Meta: rank_math_focus_keyword)

### 命令行参数（可选）

```bash
# 查看帮助
run.bat --help

# 设置 API Key
run.bat --config

# 处理所有类别 + 轻量模式
run.bat --all --cols focus_kw seo_title meta_desc

# 处理自定义类别文件夹
run.bat --single My-New-Category --cols seo_title meta_desc

# 强制覆盖已有内容
run.bat --all --force
```

## 📝 Prompt 逻辑说明

### Prompt 拼接规则

系统使用两层 Prompt 结构：

```
最终 Prompt = [prompt_base.md] + [categories/XXX/prompt.md]
```

### 1. 全局模板 `prompt_base.md`

位于根目录 `categories/prompt_base.md`，包含通用规则：
- AI 角色定义
- 输出格式要求
- SEO 写作规范
- 通用约束条件

### 2. 类别模板 `categories/XXX/prompt.md`

每个类别文件夹下的 `prompt.md`，仅写差异部分：
- 类别特定说明
- 产品类型描述
- 目标受众定位
- 特殊要求

### 3. 占位符要求

类别 Prompt 必须包含以下占位符（系统自动注入）：

| 占位符 | 说明 |
|--------|------|
| `{{product_list}}` | 产品列表（自动填充） |
| `{{output_spec}}` | 输出字段规范（根据选择的列生成） |

如果缺失，系统会自动追加到末尾。

### 4. 变量注入（可选）

类别文件夹可包含 `config.json`，定义可注入的变量：

```json
{
  "variables": {
    "brand_name": { "value": "Leeknivs" },
    "target_market": { "value": "B2B Wholesale" }
  }
}
```

在 Prompt 中使用 `{{brand_name}}` 引用。

### Prompt 示例

**prompt_base.md**（全局通用）：
```markdown
You are an SEO copywriting expert for B2B kitchenware wholesale.

Requirements:
- Write in professional English
- Focus on wholesale and bulk order benefits
- Include relevant keywords naturally

{{output_spec}}

Generate content for these products:
{{product_list}}
```

**categories/Japanese-Knives/prompt.md**（类别专属）：
```markdown
Product Category: Japanese Kitchen Knives

Key Features to Highlight:
- Traditional Japanese craftsmanship
- High-quality steel (VG-10, Damascus, etc.)
- Precision cutting for professional chefs

Target Audience: Restaurant owners, kitchen supply wholesalers
```

## ⚙️ 配置说明

### API 配置

存储在 `.seo_config.json` 文件中：
```json
{
  "api_key": "sk-...",
  "api_url": "https://api.deepseek.com/v1/chat/completions",
  "model": "deepseek-chat"
}
```

### 环境变量（可选）

| 变量名 | 默认值 | 说明 |
|--------|--------|------|
| `AI_API_KEY` | (空) | API 密钥 |
| `AI_API_URL` | `https://api.deepseek.com/v1/chat/completions` | API 端点 |
| `AI_MODEL` | `deepseek-chat` | 模型名称 |
| `AI_BATCH_SIZE` | `5` | 每批处理产品数 |
| `AI_RATE_LIMIT` | `0.5` | 每秒请求数限制 |

## 📊 CSV 文件格式

### 输入文件位置
`categories/{类别}/products-{描述}.csv`

### 必需列
| 列名 | 说明 |
|------|------|
| `Name` | 产品名称 |
| `SKU` | 产品 SKU |
| `Categories` | 产品分类 |

### 输出文件位置
`output/products-{描述}.csv`

处理后的文件会添加选择的 SEO 列到 `output/` 目录。

## 💡 使用技巧

1. **首次使用**：建议先用 `L` 轻量模式测试效果
2. **新类别**：在 `categories/` 下创建文件夹，放入 `prompt.md` 和 CSV 文件
3. **断点续跑**：中断后重新运行，自动跳过已完成的行
4. **批量处理**：使用 `A` 全量模式一次性处理所有类别

## 🔧 故障排除

| 问题 | 解决方案 |
|------|----------|
| Python 未找到 | 安装 Python 3.8+ 并添加到 PATH |
| API Key 未配置 | 运行 `run.bat` 按 Step 1 配置 |
| 乱码 | 文件编码需为 UTF-8 |
| JSON 解析失败 | 检查 API Key 和网络连接 |
| 类别目录不存在 | 确认 `categories/` 下有对应文件夹 |

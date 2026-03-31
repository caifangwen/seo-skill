# LeeKnives 文章写作技能入口

> **版本**: 6.0 | **更新**: 2026-03 | **范围**: leeknives.com 所有英文博客文章

这是技能模块的**路由入口**，本文件只做导航，不包含具体规则。  
所有执行细节在下方对应子文件中。

---

## 📂 文件结构

```
leeknives-skills/
├── SKILL.md                        ← 你在这里（入口路由）
│
├── research/
│   ├── keyword-research.md         ← SKILL-00A 关键词调研
│   └── competitor-research.md      ← SKILL-00B + SKILL-18 竞对调研
│
├── writing/
│   ├── frontmatter.md              ← SKILL-01 Front Matter 生成
│   ├── intro.md                    ← SKILL-02 开篇引言
│   ├── steel-specs.md              ← SKILL-03 + 04 钢材成分与属性
│   ├── comparison-table.md         ← SKILL-05 对比表格
│   ├── pros-cons.md                ← SKILL-11 优缺点分析
│   ├── use-cases.md                ← SKILL-12 使用场景
│   ├── history.md                  ← SKILL-10 历史背景
│   ├── maintenance.md              ← SKILL-13 维护保养
│   ├── material-comparison.md      ← SKILL-14 材料对比
│   ├── price-analysis.md           ← SKILL-15 价格因素
│   ├── conclusion-cta.md           ← SKILL-08 + 16 结论与CTA
│   └── faq.md                      ← SKILL-09 FAQ生成
│
├── assets/
│   ├── image-guidelines.md         ← SKILL-06 图片规范 + 脚本说明
│   └── internal-links.md           ← SKILL-07 内部链接
│
├── qa/
│   ├── seo-checklist.md            ← SKILL-17 SEO优化检查
│   └── publish-checklist.md        ← 发布前完整检查清单
│
├── workflows/
│   └── article-types.md            ← 7种文章类型组合流程
│
├── scripts/
│   ├── download_images.py          ← 图片下载脚本
│   └── update_article_images.py    ← 文章图片更新脚本
│
└── style-guide.md                  ← 写作风格规范
```

---

## 🚦 快速路由

| 你要做的事 | 读哪个文件 |
|-----------|-----------|
| 写作前：关键词研究 | `research/keyword-research.md` |
| 写作前：分析竞争对手 | `research/competitor-research.md` |
| 确定文章类型和完整流程 | `workflows/article-types.md` |
| 写 Front Matter | `writing/frontmatter.md` |
| 写开篇引言 | `writing/intro.md` |
| 写钢材成分 + 属性详解 | `writing/steel-specs.md` |
| 写对比表格 | `writing/comparison-table.md` |
| 写优缺点 | `writing/pros-cons.md` |
| 写使用场景 | `writing/use-cases.md` |
| 写历史背景 | `writing/history.md` |
| 写维护保养 | `writing/maintenance.md` |
| 写材料对比 | `writing/material-comparison.md` |
| 写价格分析 | `writing/price-analysis.md` |
| 写结论 + CTA | `writing/conclusion-cta.md` |
| 写 FAQ | `writing/faq.md` |
| 处理图片（规范 + 工具脚本） | `assets/image-guidelines.md` |
| 植入内部链接 | `assets/internal-links.md` |
| 发布前 SEO 检查 | `qa/seo-checklist.md` |
| 发布前完整检查 | `qa/publish-checklist.md` |
| 语气/人称/段落规范 | `style-guide.md` |

---

## ⚡ 标准写作流程（速查）

```
① 调研阶段
   keyword-research.md → competitor-research.md

② 确认类型
   workflows/article-types.md  （选择文章类型，获取技能组合清单）

③ 写作阶段
   frontmatter → intro → [正文模块按类型选择] → conclusion-cta

④ 资产处理
   image-guidelines.md + internal-links.md

⑤ 发布前
   seo-checklist.md → publish-checklist.md
```

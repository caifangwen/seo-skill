# B2B UX Checklist

## 概述

钢铁外贸 B2B 网站用户体验检查清单，聚焦询盘转化和买家体验。

## 信息架构

### 导航设计

**检查标准**：
- [ ] 主导航清晰，不超过 7 个项目
- [ ] 产品分类符合行业习惯（长材/板材/管材）
- [ ] 有搜索功能，支持产品名/规格搜索
- [ ] 面包屑导航正确显示
- [ ] 页脚包含重要链接

**推荐导航结构**：
```
Home | Products | Applications | Certifications | About Us | Contact
                         ↓
                    Products
                         ↓
        Long Products | Flat Products | Tubular | Sections
                         ↓
                   [Specific Products]
```

---

### 产品分类

**钢铁行业推荐分类**：

| 一级分类 | 二级分类 | 示例产品 |
|----------|----------|----------|
| Long Products | Rebar, Wire Rod, Angle, I-Beam | ASTM A615 Rebar |
| Flat Products | HRC, CRC, GI, PPGI, Plate | SPHC Hot Rolled Coil |
| Tubular Products | Seamless Pipe, Welded Pipe, Hollow Section | ASTM A106 SMLS |
| Section Products | Channel, Angle, Rail | U-Channel, Rail Steel |

---

## 产品页面体验

### 首屏设计（Above the Fold）

**必须包含元素**：
- [ ] 产品主图（清晰、专业）
- [ ] 产品标题（包含规格/标准）
- [ ] 核心规格摘要
- [ ] CTA 按钮（Get Best Price / Request Quote）
- [ ] 信任元素（认证图标、响应时间）

**首屏布局示例**：
```
┌─────────────────────────────────────────┐
│  [Product Image]    │  ASTM A615 Rebar  │
│                     │  Gr40/60 10-50mm  │
│                     │                   │
│                     │  ✓ ISO9001        │
│                     │  ✓ Mill Certificate│
│                     │                   │
│                     │  [Get Best Price] │
│                     │  Reply in 2 hours │
└─────────────────────────────────────────┘
```

---

### 规格表展示

**最佳实践**：
- [ ] 表格清晰，行间距适中
- [ ] 关键规格高亮（屈服强度、抗拉强度）
- [ ] 包含等级等价对照表
- [ ] 移动端可横向滚动
- [ ] 支持下载 PDF 规格书

**表格设计**：
```html
<table class="spec-table">
  <thead>
    <tr><th>Specification</th><th>Value</th></tr>
  </thead>
  <tbody>
    <tr class="highlight">
      <td>Yield Strength</td>
      <td>Gr40: ≥280MPa | Gr60: ≥420MPa</td>
    </tr>
    <!-- ... -->
  </tbody>
</table>
```

---

### 图片展示

**检查标准**：
- [ ] 至少 3 张产品图片（整体、细节、应用）
- [ ] 图片清晰，分辨率≥1200px
- [ ] 支持点击放大
- [ ] 有工厂/仓库实拍图
- [ ] 有包装图片

**图片类型优先级**：
| 类型 | 重要性 | 说明 |
|------|--------|------|
| 产品整体图 | ⭐⭐⭐⭐⭐ | 展示产品外观 |
| 细节特写 | ⭐⭐⭐⭐⭐ | 展示螺纹、表面质量 |
| 应用场景 | ⭐⭐⭐⭐ | 展示实际使用 |
| 工厂实拍 | ⭐⭐⭐⭐ | 建立信任 |
| 包装图片 | ⭐⭐⭐ | 展示运输保护 |
| 证书图片 | ⭐⭐⭐⭐ | 建立信任 |

---

## 询盘转化体验

### RFQ 表单体验

**表单设计原则**：
- 字段数量 ≤5 个必填
- 字段标签清晰
- 有输入验证和错误提示
- 提交后有成功确认
- 移动端易填写

**字段优化**：
| 字段 | 类型 | 必填 | 优化建议 |
|------|------|------|----------|
| 姓名 | text | ✅ | placeholder: "Your Name" |
| 邮箱 | email | ✅ | placeholder: "john@company.com" |
| 产品 | text | ✅ | placeholder: "e.g., Rebar ASTM A615" |
| 规格 | text | ✅ | placeholder: "12mm x 12m" |
| 数量 | text | ✅ | placeholder: "100 MT" |
| 电话 | tel | ❌ | placeholder: "+966 5X XXX XXXX" |
| 留言 | textarea | ❌ | placeholder: "Additional requirements" |

---

### 即时通讯集成

**WhatsApp**：
- [ ] 悬浮按钮固定右下角
- [ ] 点击打开 WhatsApp 对话
- [ ] 预设消息包含产品名称
- [ ] 显示在线状态（如可能）

**WeChat**：
- [ ] 二维码清晰可扫描
- [ ] 标注"WeChat ID: xxx"
- [ ] 针对中国买家展示

**其他市场特定**：
| 市场 | 工具 |
|------|------|
| 中东 | WhatsApp, Telegram |
| 东南亚 | WhatsApp, LINE (Thai), Zalo (Vietnam) |
| 南美 | WhatsApp |
| 非洲 | WhatsApp |

---

### 响应时间展示

**信任元素**：
```
✅ "Reply within 2 hours"
✅ "24/7 Support Available"
✅ "Get Quote in 30 Minutes"
✅ "Same Day Response"
```

**展示位置**：
- CTA 按钮下方
- 表单旁边
- 页脚联系信息区

---

## 信任建立

### 认证展示

**必须展示的认证**：
- [ ] ISO9001 证书
- [ ] CE 标志（如适用）
- [ ] Mill Test Certificate 样本
- [ ] SGS/BV 检验报告（如有）
- [ ] 行业会员（钢协等）

**展示位置**：
- 首页底部
- 产品页面规格表下方
- 关于我们页面
- 页脚

---

### 工厂实力展示

**内容建议**：
| 内容类型 | 说明 | 重要性 |
|----------|------|--------|
| 工厂外观 | 航拍/全景图 | ⭐⭐⭐⭐ |
| 生产车间 | 轧钢线、设备 | ⭐⭐⭐⭐⭐ |
| 质检设备 | 拉力试验机、光谱仪 | ⭐⭐⭐⭐ |
| 仓库库存 | 展示现货能力 | ⭐⭐⭐⭐⭐ |
| 装运现场 | 装车/装船 | ⭐⭐⭐ |
| 团队照片 | 销售、质检团队 | ⭐⭐⭐ |

---

### 项目案例

**案例展示要素**：
- [ ] 项目名称
- [ ] 项目地点
- [ ] 供应产品
- [ ] 供应数量
- [ ] 项目图片（如可公开）

**案例格式**：
```
┌─────────────────────────────────────┐
│  [Project Image]                    │
│  Saudi Arabia Vision 2030 Housing   │
│  • Location: Riyadh, Saudi Arabia   │
│  • Product: ASTM A615 Gr60 Rebar    │
│  • Quantity: 50,000 MT              │
│  • Year: 2024                       │
└─────────────────────────────────────┘
```

---

## 移动端体验

### 响应式设计

**检查标准**：
- [ ] 所有页面在手机正常显示
- [ ] 文字无需缩放即可阅读
- [ ] 按钮大小适合拇指点击（≥44px）
- [ ] 表单易填写
- [ ] 图片自适应

**测试设备**：
- iPhone (Safari)
- Android (Chrome)
- 平板 (iPad/Android Tablet)

---

### 移动端特定优化

**必须优化元素**：
| 元素 | 桌面端 | 移动端 |
|------|--------|--------|
| 导航 | 水平菜单 | 汉堡菜单 |
| CTA 按钮 | 正常大小 | 全宽、大尺寸 |
| 表单 | 多列 | 单列、大输入框 |
| 规格表 | 完整显示 | 可横向滚动 |
| WhatsApp | 悬浮按钮 | 悬浮按钮（底部） |
| 电话 | 文字 | 可点击拨打 |

---

## 内容可读性

### 文字排版

**最佳实践**：
- [ ] 正文字号 ≥16px
- [ ] 行高 1.5-1.8
- [ ] 段落长度 ≤5 行
- [ ] 使用小标题分段
- [ ] 使用列表（如本清单）

---

### 语言使用

**检查标准**：
- [ ] 无拼写/语法错误
- [ ] 专业术语准确
- [ ] 避免中式英语
- [ ] 针对目标市场本地化
- [ ] 单位使用正确（mm, MT, MPa）

---

## 页面速度

### 性能指标

**目标值**：
| 指标 | 目标 | 工具 |
|------|------|------|
| 首屏加载 | <1.5s | PageSpeed Insights |
| 完全加载 | <3s | PageSpeed Insights |
| LCP | <2.5s | Core Web Vitals |
| FID | <100ms | Core Web Vitals |
| CLS | <0.1 | Core Web Vitals |

---

### 优化建议

| 优化项 | 影响 | 实施难度 |
|--------|------|----------|
| 图片压缩 | 高 | 低 |
| 启用缓存 | 高 | 中 |
| CDN 部署 | 高 | 中 |
| 减少 JS | 中 | 中 |
| 懒加载 | 中 | 低 |

---

## B2B 特定功能

### 多语言切换

**最佳实践**：
- [ ] 语言切换器在页眉明显位置
- [ ] 使用本地语言名称（English, 中文，Español）
- [ ] 切换后保持当前页面
- [ ] 当前语言高亮显示

---

### 货币显示

**检查标准**：
- [ ] 支持多货币（USD, EUR, SAR 等）
- [ ] 货币符号正确
- [ ] 价格格式正确（$500.00 vs 500,00 €）
- [ ] 注明价格条款（FOB, CIF）

---

### 下载资源

**推荐提供**：
- [ ] 产品目录 PDF
- [ ] 规格书下载
- [ ] 证书下载
- [ ] 价格表（需注册）

---

## 检查清单使用指南

### 审计流程

1. 逐项检查每个检查点
2. 标记状态：✅ 符合 / ⚠️ 部分符合 / ❌ 不符合
3. 记录问题和改进建议
4. 按优先级排序修复

### 评分标准

| 得分率 | 等级 | 说明 |
|--------|------|------|
| 90-100% | A+ | 优秀 |
| 80-89% | A | 良好 |
| 70-79% | B | 中等 |
| 60-69% | C | 及格 |
| <60% | D | 需改进 |

---

## 参考链接

- [Google UX Playbook for B2B](https://think.storage.googleapis.com/docs/b2b-ux-playbook.pdf)
- [Nielsen Norman Group - B2B UX](https://www.nngroup.com/topics/b2b/)

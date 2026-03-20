# Inquiry CTA Templates

## 概述

钢铁外贸 B2B 询盘转化 CTA 模板集合，包含表单设计、按钮文案、信任元素等最佳实践。

## RFQ 表单模板

### 模板 1: 标准 RFQ 表单

```html
<div class="rfq-form-container">
  <h3>Request a Quote</h3>
  <p class="subtitle">Get best price within 2 hours</p>
  
  <form action="/rfq" method="POST">
    <div class="form-group">
      <label for="name">Your Name *</label>
      <input type="text" id="name" name="name" placeholder="John Smith" required>
    </div>
    
    <div class="form-group">
      <label for="email">Your Email *</label>
      <input type="email" id="email" name="email" placeholder="john@company.com" required>
    </div>
    
    <div class="form-group">
      <label for="phone">Phone / WhatsApp</label>
      <input type="tel" id="phone" name="phone" placeholder="+966 5X XXX XXXX">
    </div>
    
    <div class="form-group">
      <label for="product">Product *</label>
      <input type="text" id="product" name="product" placeholder="e.g., Rebar ASTM A615 Gr60" required>
    </div>
    
    <div class="form-group">
      <label for="specification">Specification *</label>
      <input type="text" id="specification" name="specification" placeholder="e.g., 12mm x 12m" required>
    </div>
    
    <div class="form-group">
      <label for="quantity">Quantity (MT) *</label>
      <input type="text" id="quantity" name="quantity" placeholder="e.g., 100" required>
    </div>
    
    <div class="form-group">
      <label for="message">Additional Requirements</label>
      <textarea id="message" name="message" placeholder="Destination port, delivery time, special requirements..."></textarea>
    </div>
    
    <button type="submit" class="cta-button">Get Best Price</button>
    
    <p class="trust-text">
      <svg class="icon">🔒</svg>
      We respect your privacy. No spam. Reply within 2 hours.
    </p>
  </form>
</div>
```

**CSS 样式建议**：
```css
.rfq-form-container {
  background: #f8f9fa;
  padding: 30px;
  border-radius: 8px;
  border: 2px solid #007bff;
}

.rfq-form-container h3 {
  margin-top: 0;
  color: #333;
  font-size: 24px;
}

.rfq-form-container .subtitle {
  color: #666;
  font-size: 14px;
  margin-bottom: 20px;
}

.form-group {
  margin-bottom: 15px;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
  font-weight: 600;
  color: #333;
}

.form-group input,
.form-group textarea {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 14px;
}

.cta-button {
  width: 100%;
  padding: 15px;
  background: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.3s;
}

.cta-button:hover {
  background: #0056b3;
}

.trust-text {
  margin-top: 15px;
  font-size: 12px;
  color: #666;
  text-align: center;
}
```

---

### 模板 2: 简洁 RFQ 表单（移动端优化）

```html
<div class="rfq-form-compact">
  <h4>Quick Quote</h4>
  
  <form action="/rfq" method="POST">
    <input type="text" name="name" placeholder="Your Name *" required>
    <input type="email" name="email" placeholder="Your Email *" required>
    <input type="text" name="product" placeholder="Product & Spec *" required>
    <input type="text" name="quantity" placeholder="Quantity (MT) *" required>
    
    <button type="submit">Get Price Now</button>
  </form>
  
  <p class="micro-copy">Reply within 2 hours. No spam.</p>
</div>
```

---

### 模板 3: 分步 RFQ 表单

```html
<div class="rfq-step-form">
  <!-- Step 1: Contact Info -->
  <div class="step step-1 active">
    <h4>Step 1: Your Contact</h4>
    <input type="text" name="name" placeholder="Your Name *" required>
    <input type="email" name="email" placeholder="Your Email *" required>
    <input type="tel" name="phone" placeholder="Phone / WhatsApp">
    <button class="btn-next">Next →</button>
  </div>
  
  <!-- Step 2: Product Info -->
  <div class="step step-2">
    <h4>Step 2: Product Details</h4>
    <input type="text" name="product" placeholder="Product Name *" required>
    <input type="text" name="specification" placeholder="Specification *" required>
    <input type="text" name="quantity" placeholder="Quantity (MT) *" required>
    <textarea name="message" placeholder="Additional requirements"></textarea>
    <button type="submit">Submit Request</button>
  </div>
</div>
```

---

## CTA 按钮文案

### 高转化按钮文案

| 文案 | 适用场景 | 转化率提升 |
|------|----------|------------|
| Get Best Price | 通用 | 基准 |
| Get Free Quote | 价格敏感市场 | +5-10% |
| Request Quote Now | 紧急需求 | +8-15% |
| Contact Supplier | B2B 平台风格 | 基准 |
| Get Factory Price | 强调工厂直销 | +10-20% |
| Check Price | 轻量级 CTA | +5-8% |
| Get Latest Price | 价格波动产品 | +8-12% |
| Inquire Now | 简洁直接 | 基准 |
| Send Inquiry | 正式商务 | 基准 |
| Get Quick Quote | 强调速度 | +10-15% |

### 针对特定市场的文案

| 市场 | 推荐文案 | 原因 |
|------|----------|------|
| 中东 | Get Best Price, Factory Direct | 价格敏感，重视工厂直销 |
| 东南亚 | Get Quick Quote, Fast Response | 重视响应速度 |
| 非洲 | Best Price, Cheap | 高度价格敏感 |
| 南美 | Cotización Gratis (Free Quote) | 本地化语言 |

---

## 信任元素文案

### 响应时间承诺

| 文案 | 适用场景 |
|------|----------|
| Reply within 2 hours | 标准承诺 |
| Response within 1 hour | 快速响应 |
| 24/7 Support Available | 全天候服务 |
| Get Quote in 30 Minutes | 极速响应（工作时间） |
| Same Day Response | 当日回复 |

### 隐私保护文案

| 文案 | 语气 |
|------|------|
| We respect your privacy. No spam. | 标准 |
| Your information is safe with us. | 温和 |
| 100% Privacy Guaranteed. | 强调 |
| We never share your information. | 承诺 |
| Secure & Confidential. | 正式 |

### 工厂实力展示文案

| 文案 | 适用场景 |
|------|----------|
| Factory Direct Price | 工厂直销 |
| 20+ Years Experience | 资深厂家 |
| ISO9001 Certified Factory | 认证工厂 |
| 5000MT Monthly Capacity | 产能展示 |
| Export to 50+ Countries | 出口经验 |
| Mill Test Certificate Provided | 质量保证 |

---

## WhatsApp/WeChat 集成

### WhatsApp 悬浮按钮

```html
<a href="https://wa.me/861234567890?text=Hi,%20I'm%20interested%20in%20your%20steel%20products" 
   class="whatsapp-float" 
   target="_blank">
  <img src="whatsapp-icon.png" alt="Chat on WhatsApp">
</a>

<style>
.whatsapp-float {
  position: fixed;
  bottom: 20px;
  right: 20px;
  z-index: 1000;
  background: #25D366;
  border-radius: 50%;
  padding: 15px;
  box-shadow: 0 4px 10px rgba(0,0,0,0.3);
  transition: transform 0.3s;
}

.whatsapp-float:hover {
  transform: scale(1.1);
}

.whatsapp-float img {
  width: 40px;
  height: 40px;
}
</style>
```

### WhatsApp 预设消息模板

| 产品 | 预设消息 |
|------|----------|
| Rebar | Hi, I'm interested in ASTM A615 Gr60 Rebar. Please send me your best price. |
| HRC | Hi, I need HRC SPHC 2mm x 1250mm. What's your best price for 100MT? |
| Seamless Pipe | Hi, I'm looking for ASTM A106 Gr.B seamless pipe 2 inch SCH40. Please quote. |

### WeChat 二维码展示

```html
<div class="wechat-qr">
  <h5>Add us on WeChat</h5>
  <img src="wechat-qr.png" alt="WeChat QR Code">
  <p>Scan to chat instantly</p>
</div>
```

---

## 邮件 CTA 模板

### 邮件主题行

| 类型 | 主题行示例 |
|------|------------|
| 报价 | Re: Your Inquiry for [Product] - Best Price from [Company] |
| 跟进 | Following up: [Product] Inquiry from [Date] |
| 促销 | Special Offer: [Product] at Factory Price - Limited Time |
| 新品 | New: [Product] Now Available - Factory Direct |

### 邮件正文 CTA

```
Dear [Name],

Thank you for your inquiry about [Product].

Based on your requirements:
- Product: [Specification]
- Quantity: [Quantity]
- Destination: [Port]

Our best offer:
- Price: USD [Price]/MT FOB [Port]
- Lead Time: [Days] days
- Payment: L/C at sight or T/T 30% deposit

[CTA Button: Accept This Offer]

Or reply to this email for any questions.

Best regards,
[Your Name]
[Company Name]
WhatsApp: +86 XXX
```

---

## 落地页 CTA 最佳实践

### 位置策略

| 位置 | 适用场景 | 转化率 |
|------|----------|--------|
| 首屏（Above the Fold） | 所有页面 | 最高 |
| 规格表下方 | 产品页 | 高 |
| 页面中部 | 长页面 | 中 |
| 页面底部 | 所有页面 | 低（但必要） |
| 侧边栏悬浮 | 桌面端 | 高 |

### A/B 测试建议

| 测试元素 | 变体 A | 变体 B | 衡量指标 |
|----------|--------|--------|----------|
| 按钮颜色 | 蓝色 | 橙色 | 点击率 |
| 按钮文案 | Get Best Price | Get Factory Price | 提交率 |
| 表单长度 | 4 字段 | 7 字段 | 完成率 |
| 信任文案 | Reply within 2 hours | 24/7 Support | 提交率 |
| CTA 位置 | 首屏 | 规格表下方 | 转化率 |

---

## 转化漏斗优化

### 典型转化漏斗

```
访客 → 查看产品页 → 点击 CTA → 填写表单 → 提交 → 询盘
      (100%)      (10%)     (50%)    (80%)   (4% 总转化)
```

### 优化策略

| 环节 | 优化点 | 预期提升 |
|------|--------|----------|
| 查看产品页 → 点击 CTA | 首屏 CTA、悬浮按钮 | +20-50% |
| 点击 CTA → 填写表单 | 简化表单、信任文案 | +10-30% |
| 填写表单 → 提交 | 减少必填字段、进度指示 | +5-20% |

---

## 参考链接

- [HubSpot CTA Best Practices](https://blog.hubspot.com/marketing/cta-examples)
- [Unbounce Landing Page Guide](https://unbounce.com/landing-page-articles/)

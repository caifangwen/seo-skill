# 重定向规则最佳实践

## 重定向类型

### 301 Moved Permanently（永久重定向）

**使用场景：**
- 页面永久迁移
- 域名变更
- HTTP → HTTPS 迁移
- URL 结构重构

**SEO 影响：** 传递 90-99% 的链接权重

```apache
# Apache .htaccess
Redirect 301 /old-page.html https://example.com/new-page.html

# Nginx
rewrite ^/old-page.html$ https://example.com/new-page.html permanent;
```

---

### 302 Found（临时重定向）

**使用场景：**
- 短期促销活动
- A/B 测试
- 临时维护页面

**SEO 影响：** 不传递权重，原页面保留在索引中

```apache
# Apache .htaccess
Redirect 302 /promo https://example.com/summer-sale

# Nginx
rewrite ^/promo$ https://example.com/summer-sale redirect;
```

---

### 307 Temporary Redirect（临时重定向，保持方法）

**使用场景：**
- 需要保持 POST 请求的临时重定向
- 表单提交处理

**与 302 的区别：** 严格保持请求方法不变

---

## 重定向链规则

### 最佳实践

- **最大跳数：** 不超过 2 跳
- **目标：** 直接重定向到最终 URL

### 问题示例

```
❌ 错误：A → B → C → D（3 跳，太慢）
✅ 正确：A → D（1 跳，直接）
```

### 修复方法

1. 使用 Screaming Frog 爬取网站
2. 筛选"Redirect Chains"报告
3. 更新重定向规则，跳过中间跳

---

## 常见重定向场景

### 1. WWW 与非 WWW 统一

```apache
# WWW → 非 WWW
RewriteCond %{HTTP_HOST} ^www\.example\.com [NC]
RewriteRule ^(.*)$ https://example.com/$1 [L,R=301]

# 非 WWW → WWW
RewriteCond %{HTTP_HOST} ^example\.com [NC]
RewriteRule ^(.*)$ https://www.example.com/$1 [L,R=301]
```

---

### 2. HTTP → HTTPS

```apache
RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
```

---

### 3. 尾部斜杠统一

```apache
# 强制添加尾部斜杠
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_URI} !/$
RewriteRule ^(.*)$ https://example.com/$1/ [L,R=301]

# 强制移除尾部斜杠
RewriteCond %{REQUEST_FILENAME} !-d
RewriteCond %{REQUEST_URI} /$
RewriteRule ^(.*)$ https://example.com/$1 [L,R=301]
```

---

### 4. 大写字母 URL → 小写

```apache
RewriteMap lowercase int:tolower
RewriteCond %{REQUEST_URI} [A-Z]
RewriteRule ^(.*)$ ${lowercase:$1} [R=301,L]
```

---

## 重定向检查清单

- [ ] 所有重定向使用正确的状态码（301/302）
- [ ] 无重定向链超过 2 跳
- [ ] 无重定向循环
- [ ] 重要页面重定向到相关页面（非 404）
- [ ] 内部链接更新为直接链接到最终 URL
- [ ] sitemap 中只包含最终 URL
- [ ] canonical 指向最终 URL

---

## 重定向调试工具

| 工具 | 用途 |
|------|------|
| curl -I | 查看响应头 |
| httpstatus.io | 批量检查状态码 |
| Screaming Frog | 爬取重定向链 |
| Redirect Path (Chrome 插件) | 实时查看重定向 |

```bash
# 使用 curl 查看重定向链
curl -I -L https://example.com/old-page
```

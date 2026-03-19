# On-Page SEO 完整检查清单

## Title Tag 最佳实践

- 长度：50-60 字符（中文约 25-30 个汉字）
- 结构模板：`[主关键词] - [修饰词] | [品牌名]`
- 禁止：全大写、堆砌关键词、超过 70 字符
- 主关键词必须出现在前 30 字符内

## Meta Description

- 长度：150-160 字符
- 必须包含：主关键词 + 行动召唤（了解更多/立即体验/免费试用）
- 不影响排名，但影响点击率（CTR）

## H 标签层级规范

```
H1（仅一个）：页面主题，含主关键词
  H2（3-7 个）：主要章节，含相关词
    H3（按需）：子章节，含长尾词和问题词
```

## 关键词分布最佳位置

1. 文章前 100 字内（自然出现）
2. 至少一个 H2 标题中
3. 图片 Alt 标签
4. 文章结尾段落
5. URL slug（拼音或英文）

## 内容深度参考标准

| 内容类型 | 建议字数 |
|----------|----------|
| 信息类博客 | 1500-2500 字 |
| 终极指南 | 3000-5000 字 |
| 产品页 | 800-1200 字 |
| 落地页 | 500-800 字 |

## FAQ Schema 触发条件

当文章中包含以下结构时，建议添加 FAQ Schema：

```html
<div itemscope itemtype="https://schema.org/FAQPage">
  <div itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
    <h3 itemprop="name">问题文本</h3>
    <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
      <p itemprop="text">答案文本</p>
    </div>
  </div>
</div>
```

# SKILL-09: FAQ 问答生成

**用途**: 生成常见问题解答章节
**适用**: 指南/科普文章、产品指南文章、选型指南文章

---

## 结构模板

```markdown
## Frequently Asked Questions

### 问题 1？

回答内容（2-3 句）...

### 问题 2？

回答内容（2-3 句）...

### 问题 3？

回答内容（2-3 句）...
```

---

## 问题类型

1. **定义类**: "What is...?" "What does... mean?"
2. **规格类**: "What is the pressure rating of...?" "What size is available?"
3. **对比类**: "What's the difference between...?" "Which is better...?"
4. **应用类**: "Where is... used?" "Can... be used for...?"
5. **安装类**: "How to install...?" "How to tighten flange bolts?"
6. **维护类**: "How to maintain...?" "How often to inspect...?"
7. **合规类**: "Is... API certified?" "Does... meet ASME standards?"

---

## 回答结构

```
[直接回答]（1 句）

[补充说明/技术细节]（1-2 句）

[相关建议/标准参考]（可选）
```

---

## 示例（法兰 FAQ）

```markdown
## Frequently Asked Questions

### What is the difference between Class 150 and Class 300 flanges?

Class 150 and Class 300 refer to ASME pressure-temperature ratings. Class 300 flanges can withstand higher pressures than Class 150 flanges of the same size. At ambient temperature, Class 150 flanges are rated for 285 psi, while Class 300 flanges are rated for 740 psi. Class 300 flanges also have thicker walls and larger bolt holes, making them heavier and more expensive.

### What is the maximum temperature for carbon steel flanges?

ASTM A105 carbon steel flanges can be used in temperatures ranging from -20°F to 800°F (-29°C to 427°C). For temperatures above 800°F, alloy steel materials like ASTM A182 F11 or F22 are recommended. For low-temperature applications below -20°F, ASTM A350 LF2 low-temperature carbon steel should be used.

### How do you determine the correct flange size?

Flange size is determined by the pipe nominal pipe size (NPS) and the pressure class. The flange bore should match the pipe's inside diameter for smooth flow. Refer to ASME B16.5 for dimensional standards covering NPS 1/2" to 24". For larger sizes, ASME B16.47 covers flanges up to NPS 60".

### What is the difference between weld neck and slip-on flanges?

Weld neck flanges have a long tapered hub that is butt-welded to the pipe, providing superior strength and fatigue resistance. Slip-on flanges slide over the pipe and are welded on both sides, offering easier installation and lower cost. Weld neck flanges are preferred for high-pressure and critical service applications, while slip-on flanges are suitable for low-pressure, non-critical applications.
```

---

## 示例（阀门 FAQ）

```markdown
## Frequently Asked Questions

### What is the difference between a ball valve and a gate valve?

Both ball valves and gate valves are designed for on/off service, but they operate differently. Ball valves use a rotating ball with a bore through the center, providing quarter-turn operation and bubble-tight shutoff. Gate valves use a sliding gate that lifts out of the flow path, offering minimal pressure drop but slower multi-turn operation. Ball valves are generally preferred for most applications due to their reliability and ease of operation.

### Can a ball valve be used for flow control?

Ball valves are not recommended for throttling or flow control applications. When partially open, the high-velocity flow can cause cavitation and erosion of the ball and seats, leading to premature failure. For flow control applications, globe valves, needle valves, or control valves with appropriate trim should be used instead.

### What does "full port" mean in ball valves?

Full port (or full bore) ball valves have a ball bore diameter equal to the pipe's inside diameter, resulting in minimal flow restriction and pressure drop. Standard port ball valves have a smaller bore, which creates some flow restriction but reduces the valve size and cost. Full port valves are preferred for applications requiring pigging or where minimizing pressure drop is critical.

### How often should valves be inspected and maintained?

Valve inspection frequency depends on the service conditions and criticality. For normal service, visual inspection should be conducted annually, with operational testing every 2-3 years. For critical service or harsh environments, inspection intervals should be shortened to 6-12 months. API 570 provides guidelines for piping system inspection including valves. Regular lubrication, seal replacement, and functional testing extend valve service life.
```

---

## 示例（材料选型 FAQ）

```markdown
## Frequently Asked Questions

### What is the difference between 304 and 316 stainless steel?

Both 304 and 316 are austenitic stainless steels with good corrosion resistance. The key difference is that 316 contains 2-3% molybdenum, which significantly improves resistance to pitting and crevice corrosion, especially in chloride environments. For marine applications or systems handling saltwater, 316 is the preferred choice. For general corrosive service, 304 provides adequate performance at a lower cost.

### When should I use duplex stainless steel?

Duplex stainless steel (such as 2205) offers approximately twice the yield strength of austenitic stainless steels and superior resistance to chloride stress corrosion cracking. It is ideal for seawater systems, offshore platforms, and chemical processing equipment handling chlorides. The higher strength allows for thinner wall sections, potentially reducing weight and cost despite the higher material price per pound.

### Is carbon steel suitable for outdoor applications?

Carbon steel can be used outdoors with proper protection. Hot-dip galvanizing, epoxy coating, or paint systems provide corrosion protection for exposed carbon steel components. Without protection, carbon steel will rust when exposed to moisture and oxygen. For maintenance-free outdoor applications, stainless steel or aluminum may be more cost-effective over the lifecycle despite higher initial costs.
```

---

**提示**: FAQ 章节可捕获精选摘要（Featured Snippet），建议每篇指南类文章都加入。使用 Schema 标记可增强 SEO 效果。

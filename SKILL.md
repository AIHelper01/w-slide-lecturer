---
name: w-slide-lecturer
description: Convert PPTX/PDF training slides into a faithful, detailed English lecture script in Markdown. Use when asked for PPT英文授课讲稿、逐页讲解稿、按模块提取原文、讲稿与原图对应、修复PPT断行、speaker notes, or a slide-aligned lecture package. Each visual module gets original text, a mostly source-worded spoken script, and Chinese pointing cues; bundle slide screenshots.
compatibility: "Python 3.9+; python-pptx, PyMuPDF; optional LibreOffice for rendering PPTX. Visual inspection by a capable agent is needed for text inside embedded images."
metadata:
  author: "w"
  version: "2.0.0"
---

# w-slide-lecturer — PPT 逐模块英文授课讲稿

**使命：让讲师能看着当前 PPT 的当前模块，顺着页面原句，用简单英语一口气讲完整，不必在各模块间跳转。**

## Activate for

- 用户上传 PPTX/PDF，让你“做完整英文授课讲稿、逐页 PPT 讲解、写 MD、图中文字也提取、打包原页截图”。
- 用户要求“按模块讲 / 原文优先 / 讲详细一些 / 修复提取文字里的不合理换行”。
- 修改现有讲稿，使 A 原文、B 英文讲解、C 中文提示按照**相同的视觉模块**一一对应。

默认产出：`<course>_逐模块英文授课讲稿.md` + `<course>_逐模块讲稿_含截图.zip`，压缩包里有 MD 和 `slide_images/`。若未要求另做演示文稿，**不要修改原 PPT**。

## 不可违反的七条原则

1. **模块先行**：以 PPT **实际视觉布局**划分模块（列、卡片、流程段、图表块、表格区域）。先完成模块 1 的 A→B→C，再讲模块 2。**任何时候不要跳到模块 B，又回头补模块 A**。
2. **原文优先**：B 部分能直接用 PPT 原句就直接用；原词、专有名词、数字、公式、示例和标题尽可能不改。仅添加易朗读的短连接句和必要解释。杜绝套话式扩写、换掉原句的同义改写。
3. **原文也必须按模块**：不能把整页文本统一堆在 A1、把所有图中文字统一堆在 A2，再单独写 B。每个模块内收集**该模块**的正文和图示文字，紧跟它自己的 B、C。
4. **仅清理排版断行**：修复 PPT/PDF 转换带来的句中换行、多余空格、拆开的英文术语；保留真实段落、条目、表格单元格、代码、公式、数字及页面结构。**修换行不等于改写或校对事实**。
5. **页内单向前进**：按视觉阅读顺序（通常上→下、左→右；流程图严格按箭头），每个模块完整讲完再往下。每页只在**所有模块结束**后写一次页间 Transition。
6. **详细但不游离**：覆盖当页重要句子、表格维度、步骤、图中箭头、数学符号和案例；长短由页面密度决定。讲稿可以详细，但不得擅自补新的理论、案例、数据或时事来凑长度。
7. **没有核对就不称完整**：脚本可抓取可编辑文字，但**不能保证识别图片烘焙文字**。每页必须看原页截图；无法看清则标注，不可猜。完整性验证脚本通过不等于视觉或事实复核通过。

## Workflow (must follow in order)

### 1. 读取源文件与渲染原页

1. 优先使用用户当前上传的原始 PPTX；PDF 仅在本身就是源文件或 PPTX 不可用时使用。**不要依赖前一次文件的文字覆盖新版 PPT**。
2. 确定真实物理页数，包括封面、目录、章节页、THANKS。不要从 `_P43` 等文件名推断页数。检查每页标题和图示，抽样核对复杂页。
3. 可以运行：

   ```bash
   python scripts/prepare_slides.py "course.pptx" --out "./work" --render
   # 若已是 PDF：python scripts/prepare_slides.py "course.pdf" --out "./work" --render
   ```

   输出 `source_manifest.json`（文本 + 位置 + 可选原备注）、`selectable_text.md`、`slide_images/slide_01.png...`。如果缺少 LibreOffice，改用可用的幻灯片预览工具；**未渲染不可宣称完成图中文字提取**。详见 [图文提取规范](references/extraction.md)。
4. `source_manifest.json` 与预览图都只是输入。**不要把脚本生成的机械草稿当成完整讲稿**。

### 2. 每页先确定真实的视觉模块

- 先观察整页：标题、左栏/右栏、上下卡片、流程步骤、图与说明文字、底部结论；按**实际讲解路径**命名 `Module 01 / 02 / 03 ...`。
- 一个完整的流程或对照图可以作为一个模块；不要为了增加模块数，把同一流程每个箭头拆开。也不要把两个独立视觉区强合成一个模块。
- 图文在同一概念区域时，**图中文字和其旁边的解释归入同一模块**；例如“ReAct 解释 + 三步环形图”可归为一个模块。
- 不能仅依 XML 的对象顺序或 PDF 文本读序决定模块；这些常在多栏页面中串行。需用**渲染截图 + 位置信息**重建阅读顺序。
- 对于密集时间线、架构图、数值表格，按实际**图中顺序**讲，不是按提取器输出顺序。

### 3. 在每个模块内部按 A → B → C 写作

严格使用 [交付模板](assets/module-template.md)，每个 `### Module NN — ...` 内：

**A. PPT 原文（按模块，已修复异常换行）**
- 录入**可见原文**：当前模块的标题、正文、子标题、项目符号、表格行/列、数字、引用、图注、公式。
- 同模块嵌入图中的**可辨认**标注列在 A 的“图中文字”里。图中没有额外文字时写“无额外可见文字”；不可辨认时标注 `[图中细字无法可靠辨认，以原页截图为准]`。
- 保持原词、语义、顺序与细节。**仅合并意外软换行与多余空格**；不要换词、补缺的图示细字、改正原数据。保留代码块及公式独立行。
- Speaker Notes 若包含教学备注，可另设**整页末尾**“原备注（非 PPT 可见）”附录，不与 A 混合，也不让备注替代可见原文。

**B. English Teaching Script（可直接朗读）**
- 只讲当前模块；贴着 A 的先后逐句展开，直接复用原文原句。例：`The slide says “Each token can use context from both sides.” This helps the model ...`。原句自然的就直接念，不必每句加引号。
- 先讲**当前模块标题**，再讲对应段落、图、箭头、表格和例子；必要解释写在它的内容旁边，**不提前剧透下个模块，也不回头补上个模块**。
- 用短句和常见词衔接：`First ...`, `Look at ...`, `Next ...`, `For example ...`, `In this figure ...`, `So ...`。避免生硬复述 `Here, the key point is ...` 每段重复。
- 内容足够详细：标题与要点均有对应讲法；数据、对照关系、流程、公式及原案例不能被一句泛泛总结代替。英文句子以可朗读为准，**不用牺牲技术准确性换简单**。
- 禁止在英文可朗读正文中出现中文模块名或中文解释；中文仅放 C 或指图提示。

**C. 中文授课提示（不朗读）**
- 写清**指图路线**（左/右/上/下/箭头/第几行），本模块重点句和易混点。提示尽量短。
- 不借中文提示补充 B 中漏讲的核心英文内容。

### 4. 过渡与内容边界

- 模块之间可使用一句简单的 `Next, let's look at ...`，**只在前一模块结束时引出后一个**；禁止模块中途跨区引用。
- 每页所有模块写完后，再写独立 `**Transition to Next Slide:** ...`；对应真实下一页标题/主题。最后一页改结束语。
- 原 PPT 若有错误、来源争议或过时信息：原文照录，不暗中改；如用户要求审核，再单独标注“补充核验”。
- **不要外部检索来覆盖用户教材**，除非用户明确要求核验、更新或扩展；有外部内容时清楚区分其来源。

### 5. 输出前质量检查与打包

1. 对照原始页数检查 `## Slide 01 ... ## Slide NN` 无缺漏、重复；每页截图与页码对应。
2. 每个 Module 必须完整有 A/B/C；确保 A1 原文与图中文字没有跑到别的模块；检查不合理换行和多栏串行。
3. 验证 B 的**模块顺序、原句重用、覆盖率**；尤其防止文本过短、跨模块跳转、凭空增加示例、机械套话。参见 [人工审校清单](references/quality.md)。
4. 若能运行脚本，执行：

   ```bash
   python scripts/validate_output.py "./work/final.md" --manifest "./work/source_manifest.json" --images-root "./work"
   ```

5. 打包 `final.md` + `slide_images/`；每张截图采用可解析的相对路径 `slide_images/slide_01.png`。保留独立 MD 和 ZIP 下载。**交付前验证 ZIP 内图片路径、页数、文件存在性**。
6. 如遇渲染或视觉读取失败，交付已核实的部分，明确限制；不能输出空白占位的“完整讲稿”。

## Specialized page handling

- **封面 / 目录 / 章节页**：原文精确、B 简短自然；不要虚构后续不存在的章节。
- **流程 / ReAct / Function Calling / MCP**：沿实际箭头逐步讲，循环只在原图有反馈箭头时说循环；案例写在当前模块。
- **3栏比较**：完整讲完左栏 A/B/C，再讲中栏，再讲右栏；底部汇总作为最后一个模块。
- **时间线**：按年份/节点顺序，原数字保留；超密集图不能全部辨认时只讲可见的主节点并声明限制。
- **表格**：按可见行/列阅读，保留数值/单位及对比维度；不得混用来源不明的新数值。
- **公式 / 代码**：原样展示，B 用容易说出口的英语说明变量/步骤；如有代码语法，不能意译修改。
- **图中英文字**：例如 `Input → Encoder → Decoder → Output`，在 A 原样列出；不是直接从图形猜抽象标签。

## Resources

- [阅读与断行修复原则](references/extraction.md)
- [英文讲稿风格与详细示例](references/speaking.md)
- [质量审核清单](references/quality.md)
- [模块化 Markdown 模板](assets/module-template.md)

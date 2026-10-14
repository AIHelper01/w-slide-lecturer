# 讲稿书写风格：贴原文、逐模块、不跳讲

## 讲师定位

用户英语非母语，熟悉专业术语，想要的是能够**看着 PPT 当前区域直接讲出来**的口语稿，不是另一套脱离 PPT 的文章。优先使用原文的完整句子、术语和例子，必要时将长句拆成容易停顿的两句。

## 英文 B 部分的基本顺序

每个模块遵循：

1. 模块开场：`First, look at ...` / `Now, let us move to ...`（只出现一次）
2. 标题和原文第一项：**尽量原句** + 一句简单解释
3. 原文第二项：**尽量原句** + 对应图片/公式位置
4. 原 PPT 中的例子、表格和关键数字：**沿着当前模块顺序完整讲完**
5. 本模块结束：`So ...` / `That is why ...`（确有必要时）
6. **下一模块**：在前模块全部讲完后才开始

## 值得避免的写法

- `Here, the key point is...` 每个模块都出现；机械、空洞。
- 从左栏讲到右栏的结论，再回来讲左栏第二个 bullet。
- 用全新案例替换 PPT 的案例，如原 PPT 讲上海旅行却改用火车票订购。
- PPT 说 `Function Calling`，讲稿却只说 `Tool Use`，让讲师找不到原词。
- 口语稿混入 `模块一` / `指箭头` 的中文；中文提示放到 C。
- 一页只说 3 句大概意思，忽略流程细节；或加入大量教材没有的新知识凑字数。

## 来源优先的示例（合成示例）

原 PPT 左栏：

```text
Encoder-Only: Read and Understand.
Uses encoder layers to read the input.
Each token can use context from both sides.
Example: "This movie is great!" → positive.
Representative models: BERT and RoBERTa.
```

合适的 B：

> First, let's look at **Encoder-Only**. The slide says **Read and Understand**. It uses encoder layers to read the input. Each token can use context from both sides. This helps the model understand the sentence. Let's look at the example: **“This movie is great!”** The result is **positive**. Representative models are **BERT and RoBERTa**.

不合适的 B：

> Before explaining encoder-only models, let's jump to decoder-only. By the way, there are many exciting applications of foundation models ...

**原因**：合适的写法顺序固定、完整使用原文术语和例子；不合适的写法跨模块且引入无关知识。

## 时长控制

- 标题/THANKS 页：2–8 句即可。
- 每页较少内容：几十秒到一两分钟的口语稿。
- 信息量大的图表 / 工作流页：按可见信息详讲，不用追求统一单页字数。
- 如果用户要求某个时间长度，优先裁剪次要解释，**不要删掉原文中的关键技术步骤**。

## 讲稿与备注

A 是绝对忠实原文的独立材料。B 可以复用 A 的完整句子并适当补“because / for example”；C 是教师指图与风险提示。若要引用幻灯片备注，应注明来自备注，不能伪装成 PPT 页面原文。

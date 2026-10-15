# Teaching patterns

## Voice and emphasis

Use common verbs: use, check, choose, keep, change, read, write, run, improve.
Keep standard terms: Function Calling, MCP, Skills, ReAct, context window, pytest.
Prefer “travel plan” to “itinerary” for a general audience, unless retaining the slide’s term helps consistency. Avoid inflated wording and extra jargon.

Keep source wording and explanation distinguishable:

> Step three is where the request becomes an action. **The model generates a structured function call. The host program runs the function and calls the weather API.** Look at the arrow going down from the model to the external function. The model requests the work, and the host performs it.

Bold only the reused source portion. Do not bold the whole paragraph, all new examples, or every transition. Key technical terms may be emphasized separately only when this does not obscure the source distinction. Preserve meaningful punctuation and capitalization. Do not claim revised wording is a verbatim quote from the original deck.

Read bullet fragments naturally: add a short regular-font lead-in or lightly adjust the Part One wording first, then reuse it consistently. Do not bolt a transition onto an incomplete fragment if it creates bad grammar. For an imperative source, use a grammatical frame such as “The first step is this: **Describe the function to the model.**” rather than “First, **Describe...**”. Do not add a sentence that repeats the immediately following source sentence.

## Content preservation

Treat polishing as a faithful language edit, not a rewrite into notes. Preserve every original bullet and its explanation. For example, do not replace three source bullets with “Core characteristics: reactive; text chat; Q&A.” Keep:

- Reactive interaction: it stays silent unless asked.
- Text-based chat: it communicates through a chat window.
- General knowledge Q&A: it generates answers based on its training data.

Keep capability limits, comparison rows, dates, examples, names, exact arguments and units. Shortening a title is acceptable only if meaning and specificity remain intact. Keep added examples and explanations in the teaching script, not as replacements for source paragraphs. When a prior draft compressed content, restore the complete source first, then rebuild the script and bold spans from that restored version.

## Module narration

Use this sequence flexibly, not as visible subheadings for every paragraph:

1. Connect: say why this module follows the previous one.
2. State: use the relevant source wording in bold.
3. Explain: clarify the meaning in one or two short sentences.
4. Ground: follow the original visual or give a short example.
5. Bridge: lead to the next original module when needed.

Add depth where it helps. A simple contents divider needs little explanation. A dense architecture figure may need several paragraphs. Do not enforce a word quota or put a long analogy after every bullet. Generally explain each concept with one concrete example, then move on.

## Contents-page model

Use the actual course titles and number of sections. For a course on agents:

This slide shows the **Contents** of our course. There are six parts, and each part answers one important question about AI agents.

First, **LLM Application Evolution: From Chatbots to Agents**. What is the difference between answering a question, helping a user, and completing a task on its own? We will compare Chatbot, Copilot, and Agent.

Second, **Agent Planning: From ReAct to Reflection**. Once we give an agent a goal, how does it decide what to do? We will compare ReAct, Plan-and-Solve, and Reflection using the same example.

Third, **Agent Action: Function Calling, MCP, and Skills**. We will see how an agent requests tool calls, connects to services, and follows reusable workflows.

Fourth, **Agent Memory: From Short-Term to Long-Term**. How does the agent keep track of its current task and use information across sessions?

Fifth, **Agent Engineering: Evolving Paradigms**. We will look at the instructions, context, and runtime system that help the agent work reliably.

Finally, **Agent Products: Coding Agents and General Agents**. We will connect the ideas with real products and practical tasks.

So, we move from why agents matter to how they plan, act, and remember, then examine how they are built and used.

Use this as a rhetorical pattern, not a fixed six-part syllabus. Bold only text grounded in the chosen source reference. Later chapter dividers should briefly recap what ended and introduce the current question without repeating the whole outline.

## Visual explanation

- Use observed labels and locations: “Start at the User box at the top.”
- Follow visible arrows in the right direction: request, execution, response, feedback.
- Distinguish the model’s decision from the host’s tool execution.
- Read tables row by row or by the slide’s intended comparison, naming the relevant columns.
- Explain a chart’s axes, trend, and teaching implication; do not invent data or causal claims.
- Explain formula symbols before their relationship. Do not read raw LaTeX aloud.
- Treat screenshots as a particular interface version, not a universal current UI.
- If a screenshot is unavailable, report the missing visual and continue only with provided text; do not invent its boxes or arrows.

## Natural transitions

Choose a relationship, not a stock filler:

- Need → mechanism: “How do we provide that missing information?”
- Definition → picture: “Now let’s follow that process in the diagram.”
- Plan → execution: “Once the plan is ready, the agent can carry it out.”
- Result → review: “We have a first result. The next question is whether it meets the requirements.”
- Contrast: “The task stays the same, but the way we connect the tool changes.”
- Summary → next slide: “We have seen how the tool is called. Next, let’s look at the connection.”

Prefer actual classroom wording such as “Let me ask you…” to meta-instructions such as “Ask the class…” inside a directly readable script. Keep directions to the teacher in separate Chinese labels.

---
name: slide-teaching-guide
description: "将 PPT/PPTX、幻灯片截图或已有英文讲稿整理成可直接授课的英文教学讲稿，并按需输出 Word。Use for slide-by-slide English teaching scripts, simple natural English polishing, original slide screenshots, bold source wording, visual explanations, natural transitions, and moderate examples. Preserve slide structure and order."
---

# Slide Teaching Guide

## Default contract

- Use simple, common English and short, natural spoken sentences. Keep accurate technical terms.
- Preserve the original slide count, page order, layout, modules, headings, bullet count, tables, steps, examples, dates, numbers, conditions, qualifications, and content scope. Polish wording and grammar only. NEVER summarize, compress several bullets into one sentence, remove supporting explanations, or replace a paragraph with its main point. Keep the revised text close to the original length. Do not edit the deck unless requested.
- Finish one visual module, including its image, formula, example, and explanation, before moving to the next. Avoid jumping between columns.
- Use the complete optimized PPT wording as the main spoken text; do not narrate a shortened summary instead of the original material. Bold the source sentences reused in the teaching script. Leave transitions, added explanations, and examples in regular type.
- State once that bold text corresponds to the revised wording in Part One, not necessarily a verbatim transcription of the uploaded original. If a user requires strictly original wording, use that as the bold reference instead.
- Add useful classroom explanation rather than merely reading bullets. Explain why, walk through arrows, and use short examples or analogies where they clarify a point. Keep the original material central.
- Default to a complete Word `.docx` for a full-deck guide. For a single screenshot, respond inline unless the user asks for a file. Honor any explicit format.
- Begin each slide with `Slide 21 — Polished Slide Title`, then embed the actual original slide image. Never invent a screenshot or infer a page number from an unrelated example. Use `Slide — Title` when a screenshot has no known page number.

## Workflow

1. Inspect the source. Count actual slides, including contents dividers and closing pages. Read both editable text and rendered visuals. Recursively inspect grouped shapes. Repair artificial line breaks while preserving real paragraphs, formulas, code, and units.
2. Build a visual module map. Use original reading order and spatial groups, not raw shape XML order. Read multi-column slides column by column when each column is a complete concept. Link chart/table/image text to its parent module.
3. Create a source-unit ledger and map every original text box, grouped text, table cell, caption, and visual annotation to a revised location. Account for all source units exactly once in Part One. Preserve original source text in the working data so omission checks are possible. Polish the title and all module wording. Prefer short titles around eight words where natural, but never lose the topic or exact technical distinction. Preserve bullets, steps, comparison dimensions, and numerical conditions. Keep code identifiers and valid syntax.
4. Check Part One against the complete original before drafting the script. Compare every bullet, example, number, date, condition, table row, and clause. Compare word counts by module and by slide; a large reduction (for example over 10%) requires reviewing for omissions, never padding or treating a numeric tolerance as permission to delete content. Update the script from the restored full text after any correction. Write the script using [teaching-patterns.md](references/teaching-patterns.md). For each module, connect the preceding idea to the source wording, explain its visual if present, then add a concise explanation or example. Tailor transitions to the relationship; avoid mechanically repeating “Next, let’s continue.”
5. Treat the first contents page as a course introduction: announce the six (or actual number of) parts, explain the main question for each part, and summarize the learning sequence. Treat later contents pages as short chapter transitions. Match section names to the actual deck, not a memorized course.
6. Check technical meaning. Do not turn illustrative values into universal laws or claim unsupported dates, quotations, product capabilities, or official architectures. For wording-only requests, preserve the source claim and put factual concerns or proposed corrections in separate Chinese instructor notes. Do not silently delete a date, quotation, product, number, or explanation because it is unverified. Make factual changes only when requested or clearly required, and identify them separately. Browse primary sources when needed for a factual correction or verification; a language-polishing task is not permission to rewrite the whole course as new research.
7. For Word, read the available Documents skill and relevant presentation-rendering instructions. Follow [word-workflow.md](references/word-workflow.md). Use bundled scripts if useful, then render and inspect every page. Fix missing Chinese glyphs, blank pages, orphan headings, awkward tail pages, clipped screenshots, and formulas. Deliver only the requested final artifact.
8. Validate coverage and formatting with `scripts/validate_guide.py`. Review language manually: a structural validator cannot assess natural teaching quality. Save using the environment’s durable artifact mechanism. For revisions, replace the same deliverable identity unless a separate version is requested.

## Per-slide output

Use these sections in order:

1. `Slide NN — Title`
2. Original slide image
3. `一、优化后的标题与正文（结构不变）`: revised title and each original module in order, including relevant figure labels and formulas.
4. `二、英文讲稿（按原顺序，串联图片讲解）`: short opening, ordered module narration with **source wording**, regular explanatory text, and a natural closing transition.

Use Chinese module/location labels as non-spoken navigation (e.g. 左侧模块、右图流程、Step 03). Do not read them aloud. Do not append “Thank you” to every slide. Do not promise the next slide covers a topic without checking that next slide.

## Resources

- [teaching-patterns.md](references/teaching-patterns.md): voice, source-bold contract, module narration, contents-page example, figure explanation, transitions.
- [word-workflow.md](references/word-workflow.md): rendering, layout, font checks, dependencies, commands.
- [guide-schema.md](references/guide-schema.md): editable intermediate JSON used by the builder and validator.
- `scripts/extract_pptx.py`: extract editable grouped text, tables, and bounding boxes. Does not replace visual inspection or OCR.
- `scripts/build_guide.py`: build Word from reviewed JSON and original page images using explicit bold source segments.
- `scripts/validate_guide.py`: check coverage, ordering, original images, source matches, and mixed source/explanation formatting in the DOCX.

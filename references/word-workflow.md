# Word workflow

1. Read the environment’s Documents skill before authoring. Use its primary runtime and required operation marker, renderer, typography, and saving conventions. Also read applicable presentation-rendering guidance.
2. Extract editable content with `extract_pptx.py`, render original slides, and inspect them. Use recursive group extraction plus visual inspection. XML text extraction misses raster text and some equations. Reconcile both sources before writing.
3. Build a complete source-unit ledger before polishing. Reconcile all original editable text and raster text. Check complete bullet, row, example, number, date and condition coverage, and near-original word length. Do not replace source material with summaries. Prefer a faithful office renderer for equations and imported objects. If an artifact renderer drops formulas, use another supported renderer and compare the result. Do not silently embed a broken slide preview.
4. Build reviewed intermediate JSON using guide-schema.md. Write the narration yourself; do not transform every bullet into a generic repeated sentence.
5. Run the bundled builder with a configured CJK font when Chinese headings are used:

```bash
python scripts/build_guide.py guide.json output.docx --cjk-font "Noto Sans CJK SC"
python scripts/validate_guide.py guide.json --docx output.docx
```

The builder requires python-docx. Extraction requires python-pptx; validation requires python-docx. Use the environment’s managed runtime when present; otherwise use an available Python environment with these dependencies. The skill does not include these libraries or install them automatically.

6. Render DOCX to page images using the Documents skill. Without that skill, use an available office renderer to PDF, then render PDF pages with an available PDF tool. Do not claim visual verification if rendering is unavailable. Diagnose the blocker instead.
7. Inspect all pages. Verify source bold versus regular explanation, original images, actual page numbering, readable sizes, equations, tables, Chinese glyphs, spacing, and no clipping. Adjust local layout instead of shrinking the entire book to meet a page target. Avoid single closing lines on mostly empty pages. Use Word heading styles for navigation.
8. Save the requested DOCX to durable storage. Preserve identity and version when revising an existing guide. Deliver only Word when Word is requested. Do not add PDFs, screenshots, intermediate JSON, extracted source text, or the original deck unless requested.

## Sample exercise

Make a temporary one-slide original image and a guide.json using the example schema. Build and validate the Word file. Then test failure cases: a missing image, duplicate slide numbers, source text not present in revised wording, and a script with no source segment. Keep generated exercises outside the installed skill and out of the distributable archive.

## Privacy and portability

Do not bundle a user’s source PPT, logos, complete course, API keys, local usernames, Library IDs, absolute workspace paths, fonts, or generated test files. Keep examples short and generic. Resolve skill-relative resources from the installed skill root. No script sends data to external services.

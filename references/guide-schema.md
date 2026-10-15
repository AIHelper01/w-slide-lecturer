# Intermediate guide JSON

Use UTF-8 JSON. This is a content contract, not an instruction to generate narration mechanically.

```json
{
  "title": "From Chatbots to Agents",
  "subtitle": "English Teaching Guide",
  "source_slide_count": 1,
  "slides": [
    {
      "number": 1,
      "title": "Checking the Weather",
      "image": "pages/slide-1.png",
      "intro": "Let’s see how the agent gets weather information.",
      "modules": [
        {
          "label": "Step 01",
          "revised": ["Describe the weather function to the model."],
          "script": [
            [
              {"text": "First, we make the tool available. ", "source": false},
              {"text": "Describe the weather function to the model.", "source": true},
              {"text": " The description explains its purpose and arguments.", "source": false}
            ]
          ]
        }
      ],
      "closing": "Now let’s follow the request through the system.",
      "instructor_notes": []
    }
  ]
}
```

Resolve relative image paths against the JSON file’s parent. Use original page numbers, unique and ascending. For complete decks require exactly 1 through `source_slide_count`. For selected pages omit the count and preserve the chosen numbers. Modules must match visual order, not extraction order.

`revised` is an array of paragraphs. Each `script` paragraph is an array of segments with explicit `source` booleans. The builder makes source segments bold and leaves explanations regular. Set `source: true` only when the segment text appears in that module’s revised wording after whitespace normalization. Split a paragraph into multiple source and regular segments as needed. Do not copy Markdown asterisks into segment text.

Keep code as exact paragraph text or implement code styling in the current Documents workflow. For structured mathematics, use native Word equations or a verified equation renderer; never pass raw LaTeX to this plain-text builder. Supply equation explanation as script text. The original page image alone is not a substitute for missing requested editable content.

## Source fidelity ledger

For language-edit tasks, add `original` (array of complete source strings) and `source_ids` (array of unique source object identifiers) to each module. Record `expected_source_ids` at slide level. This is working provenance, not user-facing content. Preserve bullets, data, conditions, and examples one-to-one. The validator compares identifiers and flags large length changes; semantic omission checks remain mandatory. Never delete source details to make a concise template fit.

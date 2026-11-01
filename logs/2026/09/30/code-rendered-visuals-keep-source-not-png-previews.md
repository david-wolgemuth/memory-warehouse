---
tags:
- visuals
- artifacts
- source-of-truth
visibility: public
related:
- ./visual-artifact-memory-and-tool-cards.md
- ./fine-tuning-break-even-visuals.md
---


# Code-rendered visuals keep source, not PNG previews

David reviewed the fine-tuning visual artifacts created by another agent on
2026-09-30 and clarified the storage preference: PNG is strictly for display
in Paseo and should not be retained in Warehouse for these code-rendered
visuals. Keep the SVG instead, or keep Python code when it can genuinely
regenerate the visual; Python is just as suitable as the SVG as durable source.
This narrows the earlier [visual-artifact guidance](./visual-artifact-memory-and-tool-cards.md), which had allowed durable PNGs
beside a log.

Direct inspection found `fine-tuning-break-even-visuals.md`,
`render-fine-tuning-break-even-charts.py` (unavailable in this public edition), three SVG chart files and three
tracked PNG chart files under this date. The script currently writes both
SVG and PNG beside the log. A fourth chart and concurrent edits to the same
script and log were also observed. Cleanup should retain source and rendering
instructions, send temporary PNGs through `view_image`, and avoid overwriting
the other agent's active chart work.

This preference concerns PNGs derived from editable vector or code source.
It does not decide how to store an original raster image that has no
equivalent SVG or reproducible code.

After the other agent's chart update settled, four tracked PNG chart copies
were removed from Warehouse. The four SVGs and Python renderer remain. The
renderer now writes SVGs beside the log by default and accepts
`--png-dir /tmp/warehouse-finetuning-previews` for temporary Paseo previews.
The chart log links to SVGs and documents both commands. Running the script
with and without `--png-dir` regenerated the SVGs without changes and created
four valid 1100 × 680 PNGs only under `/tmp`.

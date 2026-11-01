---
tags:
- visuals
- artifacts
- image-generation
ledger:
- ../logs/2026/09/30/generated-image-artifacts-belong-with-log.md
- ../logs/2026/09/30/memory-engine-name-and-pulp-visual-exploration.md
related:
- ./visual-artifact-source-and-render-recipes-follow-the-log.md
confidence: high
created: 2026-09-30 00:00:00+00:00
visibility: public
---

> Some links or assets are omitted from this public edition. References to omitted files and commands using them apply to the private source.

# Generated raster originals are copied into dated log artifacts

When the built-in image generator produces an original image worth retaining
for Warehouse work, copy the selected output from its external generation
directory into the relevant `logs/YYYY/MM/DD/` directory. Give the file a
subject-based name and link it from the small log about that exploration.
Record the generator, prompt or concise generation instructions, and whether
the image is an exploratory concept or an approved asset. Commit the image
with its log so future agents can actually retrieve it; an external tool
output path alone is not durable Warehouse memory.

Keep this separate from temporary PNG previews of SVG, Python, or other
retained editable source. Those previews can be regenerated and need not be
stored in Warehouse. See [visual artifact source and render recipes](./visual-artifact-source-and-render-recipes-follow-the-log.md).

---
tags:
- visuals
- artifacts
- logs
- provenance
ledger:
- ../logs/2026/09/30/visual-artifact-memory-and-tool-cards.md
- ../logs/2026/09/30/code-rendered-visuals-keep-source-not-png-previews.md
related:
- ./plantuml-diagram-source-lives-in-logs.md
confidence: high
created: 2026-09-30 12:28:31+00:00
visibility: public
---

> Some links or assets are omitted from this public edition. References to omitted files and commands using them apply to the private source.

# Visual artifact source and render recipes follow the log

For a visual made during Warehouse work, retain editable source and the
command or instructions that render it alongside the artifact. Source may be
an SVG block or file, PlantUML/DOT text, or Python code that genuinely
regenerates the visual. A dated log can carry that material when useful; an
artifact with its own source and provenance does not need a duplicate log.
David's original dated-log default is in the [decision log](../logs/2026/09/30/visual-artifact-memory-and-tool-cards.md); his later
direction favors artifacts where a separate log would duplicate the answer.

For visuals rendered from such source, generate PNGs temporarily for Paseo
display and do not retain those PNG previews in Warehouse. David clarified
this after reviewing the [fine-tuning chart artifacts](../logs/2026/09/30/code-rendered-visuals-keep-source-not-png-previews.md).
This does not decide retention of an original raster image without vector or
code source.

For an ongoing world or project, keep its canonical map source with its world
records and link to it from the Warehouse log. Preserve the tool, settings,
and generation command or steps so the visible result can be reproduced.
Add a separate artifacts directory only when repeated use shows a concrete
need for it.

---
tags:
- communication
- diagrams
- logs
ledger:
- ../logs/2026/09/30/visual-artifact-memory-and-tool-cards.md
related:
- ./agent-replies-use-visuals-when-relationships-or-space-matter.md
- ./visual-artifact-source-and-render-recipes-follow-the-log.md
confidence: high
created: 2026-09-29 00:00:00+00:00
visibility: public
---

> Some links or assets are omitted from this public edition. References to omitted files and commands using them apply to the private source.

# PlantUML diagram source lives in logs and renders to PNG

When a PlantUML visual is part of Warehouse work, put its `@startuml` to
`@enduml` source in the relevant dated Markdown log. Extract and render it to
an image for the Paseo reply. David explicitly requested this workflow in the
source log (unavailable in this public edition).

The rendered image is disposable; the log is the editable, versioned source.
Keep the source block easy to extract, and avoid relying on the image alone to
preserve the meaning of an event or decision.

For linked reference material, David requested that each source be saved as
its own Markdown file for later reference, with one tab per file. Keep the
source URL with the saved content. The current request records this preference
but supplied no URLs to capture; see the workflow log (unavailable in this public edition).

The installed `plantuml` CLI successfully rendered a log block to PNG using
`plantuml -tpng -pipe`; the test log (unavailable in this public edition) has the
exact command. `view_image` displayed that PNG in Paseo. The same tool
rejected direct SVG input in the SVG test (unavailable in this public edition), so render PNG for
image attachments. Use PlantUML for text-authored flows, sequences and
relationships, not precise map geometry.

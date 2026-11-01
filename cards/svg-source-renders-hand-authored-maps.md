---
tags:
- visuals
- svg
- maps
ledger:
- ../logs/2026/09/30/visual-artifact-memory-and-tool-cards.md
related:
- ./visual-artifact-source-and-render-recipes-follow-the-log.md
- ./graphviz-renders-positioned-route-and-relationship-maps.md
confidence: high
created: 2026-09-30 12:28:31+00:00
visibility: public
---

> Some links or assets are omitted from this public edition. References to omitted files and commands using them apply to the private source.

# SVG source renders hand-authored maps

Use SVG paths, shapes and text with deliberate coordinates when geography or
precise spatial placement matters. A hand-authored fantasy map stored in the
map log (unavailable in this public edition) was
rasterized with the installed GdkPixbuf SVG loader and sent through Paseo as
a PNG; David confirmed that SVG-generated image worked for him.

The available `view_image` tool rejected direct SVG input in the
SVG test (unavailable in this public edition). Render SVG
to PNG for image attachments. For a larger world, the map may become a view
of separate canonical place and geometry records.

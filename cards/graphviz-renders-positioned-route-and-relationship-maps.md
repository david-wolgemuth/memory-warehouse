---
tags:
- visuals
- graphviz
- maps
ledger:
- ../logs/2026/09/30/visual-artifact-memory-and-tool-cards.md
related:
- ./visual-artifact-source-and-render-recipes-follow-the-log.md
- ./svg-source-renders-hand-authored-maps.md
confidence: high
created: 2026-09-30 12:28:31+00:00
visibility: public
---

> Some links or assets are omitted from this public edition. References to omitted files and commands using them apply to the private source.

# Graphviz renders positioned route and relationship maps

Use Graphviz `neato` with explicit node positions for small maps where both
connections and rough relative placement matter. A DOT block in the
spatial-map log (unavailable in this public edition)
was extracted and rendered to PNG with `neato -n2 -Tpng` on 2026-09-29.

This is a route or topology sketch. For coastlines, terrain, room outlines,
or precise boundaries, use hand-authored geometry such as SVG. Keep accepted
places and routes in world records rather than relying on the drawing alone.

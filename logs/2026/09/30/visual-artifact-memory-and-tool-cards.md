---
tags:
- visuals
- artifacts
- warehouse
- organization
visibility: public
---


# Visual artifact memory and tool cards

David asked for durable guidance around visuals: where source artifacts and
render instructions should live, whether a dated `artifacts/` directory would
help, whether visualization tools should have individual cards, and whether a
visual index would help. He was undecided between logs and a new artifacts
directory, and chose to start with cards for locally tested tools.

Decision for now: use the relevant dated log as the default home for a modest,
standalone visual's editable source and exact render recipe. This extends
David's earlier explicit PlantUML-in-logs preference (unavailable in this public edition). It makes the provenance and
render instructions travel together, and the existing `logs/YYYY/MM/DD/`
layout supplies the date structure. Do not add a separate `artifacts/`
directory until repeated use shows a concrete need. Generated PNGs used only
to show a reply can remain temporary. If an image itself needs durable storage,
keep it beside and link it from the dated log; if source is too large for the
Markdown body, keep a linked source file there. For an ongoing RPG world, its
canonical editable map and place records belong in that world's workspace;
Warehouse can record the event, selection and rendering recipe with links.

The first tool cards cover what was directly tested on 2026-09-29: Mermaid in
Paseo, PlantUML text to PNG, Graphviz `neato` fixed-position maps, and
hand-authored SVG rasterized through GdkPixbuf. The visuals index (unavailable in this public edition) is a curated entry point, not an exhaustive
tool registry. Watabou and other external generators remain research leads,
without individual tool cards yet.

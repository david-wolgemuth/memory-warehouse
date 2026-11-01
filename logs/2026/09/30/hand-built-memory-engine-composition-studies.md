---
harness: codex
started: 2026-09-30 00:00:00+00:00
tags:
- visuals
- svg
- composition
visibility: public
---

> Some links or assets are omitted from this public edition. References to omitted files and commands using them apply to the private source.

# Hand-built Memory Engine composition studies

David requested a few compositions drawn “by hand” as SVG files that could
later be used as image-generation references. The agent authored three
editable SVGs directly from simple flat shapes. No image-generation model
was used in this step, and none of the earlier generated images was traced.
These are layout proposals, not approved artwork or fixed content for a
publication image.

1. A — close merge (unavailable in this public edition): a large
   human profile and compact machine share one silhouette and a single bright
   seam. Most of the background remains quiet. Landscape 8:5 frame.
2. B — isometric growth (unavailable in this public edition):
   a central human-machine form connects to three isometric modules on a
   small floating footprint, suggesting room to grow. This tests isometric
   as one retro-game composition option, not the only preferred style. 4:3
   frame.
3. C — branching map (unavailable in this public edition): a
   top-down central human-machine form sends four broad paths toward simple
   tile endpoints. The pattern borrows the structure of a game map without
   requiring a literal map in the final artwork. 4:3 frame.

All three use a restrained dark, muted metal, skin, and warm-light palette,
flat color regions, crisp edges, and one focal area. Their broad pixel-like
blocks are intentional guides for scale and visual hierarchy; specific
objects, colors, and anatomy can change after David reviews them. Each SVG
contains no visible labels, so it can be rasterized and used as a reference
without encouraging the image generator to copy text.

## Render and reuse

From the Warehouse root, generate temporary previews with the installed
GdkPixbuf SVG thumbnailer:

> This example refers to files not included in this public edition.

```sh
gdk-pixbuf-thumbnailer -s 800 logs/2026/09/30/memory-engine-composition-a-close-merge.svg /tmp/memory-engine-composition-a.png
gdk-pixbuf-thumbnailer -s 800 logs/2026/09/30/memory-engine-composition-b-isometric-growth.svg /tmp/memory-engine-composition-b.png
gdk-pixbuf-thumbnailer -s 800 logs/2026/09/30/memory-engine-composition-c-branching-map.svg /tmp/memory-engine-composition-c.png
```

To test one design through the built-in image generator later, supply **one**
of the rendered PNGs in `referenced_image_paths` and tell the tool it is a
composition guide: preserve broad masses, relative placement, and quiet
space while adding only selective detail. The editable SVG remains the
source. Temporary PNG previews need not be committed; see the
[visual-artifact rule](../../../../cards/visual-artifact-source-and-render-recipes-follow-the-log.md).

Related: [closest earlier image and excessive-detail feedback](./image-hyperdetail-and-focal-cropping-feedback.md),
retro-game references (unavailable in this public edition), and
[human-machine growth theme](./memory-engine-evolution-and-grown-together-theme.md).

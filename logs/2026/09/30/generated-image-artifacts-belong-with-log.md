---
harness: codex
started: 2026-09-30T00:00:00Z
tags:
  - visuals
  - artifacts
  - image-generation
visibility: public
---

# Generated image originals belong beside their dated log

David explicitly requested a card for the image-generation method used in the
Memory Engine naming exploration, including a reminder to copy generated
images into Warehouse as log artifacts. In that exploration, the built-in
image generator wrote original PNGs outside the repository. The agent copied
both PNGs into `logs/2026/09/30/`, linked them from the subject log, and
recorded the prompts, generator, dimensions, and exploratory status there.

The distinction matters because a generated raster is an original artifact
without a deterministic SVG or code renderer. The existing preference to
discard temporary PNG previews applies to charts and diagrams regenerated
from retained source, not to these original generated images.

Evidence: [Memory Engine visual exploration](./memory-engine-name-and-pulp-visual-exploration.md)
and this user direction.

---
harness: codex
started: 2026-09-30 00:00:00+00:00
tags:
- visuals
- user-preference
- image-generation
visibility: public
---


# Excessive AI image detail can bury the desired focal image

David clarified that close workshop candidate #4 (unavailable in this public edition) was the closest of the new
Memory Engine images, while nocturnal habitat #5 (unavailable in this public edition) had many of the right
themes. The agent had misidentified which image he meant and corrected the
[earlier log](./nocturnal-candidate-and-svg-composition-control.md).

David also described a broader recurring problem with AI images: they are
often hyper-detailed in an interesting way, but the image he wants may be
closer to a crop around the center. This is a preference for visual focus and
appropriate detail in this context, not an instruction to crop every image
or eliminate all texture. He asked whether the density is inherent to the
generator or can be worked around.

The agent's analysis: the last five prompts repeatedly invited intricate
texture with phrases such as “battered future city,” “worn metal,” “wiring,”
“repairs,” and “architecture”; those instructions plausibly contributed to
busy outputs. This is an inference, not a verified causal test. The
[OpenAI image prompting guide](https://developers.openai.com/api/docs/guides/image-prompting) recommends
specifying composition and framing, and its simple-logo example asks for a
clear silhouette and legibility at small size. A proposed next experiment is
to ask for a tight focal crop, one dominant subject, quiet surrounding space,
few large shapes, and a deliberately limited pixel vocabulary. A coarse SVG
composition sketch might help anchor that frame. Low output quality or a
smaller image size, where available through the API, is a different control
and does not by itself specify the desired visual hierarchy. No new image was
made in this turn.

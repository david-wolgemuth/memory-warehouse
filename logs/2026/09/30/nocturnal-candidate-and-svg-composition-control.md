---
harness: codex
started: 2026-09-30 00:00:00+00:00
tags:
- visuals
- image-generation
- user-feedback
visibility: public
---


# Image candidate feedback and composition sketch

## Correction to initial record

This log initially attributed David's “closest” feedback to the
nocturnal habitat candidate (unavailable in this public edition). David later clarified
that he meant the close workshop candidate (unavailable in this public edition), image #4 in the
[candidate set](./independent-memory-engine-image-candidates.md). He said
nocturnal habitat does have many of the right themes. This correction is
relative feedback, not final approval of an image or a request to reuse it
as an input reference.

He observed that three related text-only generations were similar in overall
motif despite having different compositions and people, and compared this
with the many controls he remembers from Stable Diffusion. The three
[recorded calls](./independent-memory-engine-image-candidates.md) actually
used different prompts with overlapping themes; they were not an exact-prompt
repeatability test.

David proposed drawing an SVG outline of the intended composition first and
then supplying it as an image reference to guide generation. This is an open
workflow idea, not yet a chosen composition or completed test. The agent's
proposed implementation is to retain the editable SVG and render a temporary
PNG at the intended aspect ratio for the image tool. Give the PNG the role of
**composition sketch** and ask the generator to preserve large shapes,
relative positions, and the subject boundary while supplying the desired
pulp/pixel-art texture. Because David prioritizes overall vibe over exact
content, the sketch could begin with coarse masses and visual flow before
locking specific objects.

The [OpenAI image prompting guide](https://developers.openai.com/api/docs/guides/image-prompting) explicitly
describes sketch-to-render workflows and prompts to preserve layout and
perspective. The [image generation guide](https://developers.openai.com/api/docs/guides/image-generation) cautions that
precise placement in structured compositions remains imperfect. The
[image input guide](https://developers.openai.com/api/docs/guides/images-vision)
lists PNG, JPEG, WebP, and non-animated GIF as supported image inputs, so a
rasterized SVG is a more dependable reference than submitting SVG directly.
No image or SVG was created in this turn.

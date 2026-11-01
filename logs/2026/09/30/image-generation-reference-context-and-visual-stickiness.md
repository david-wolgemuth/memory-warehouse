---
harness: codex
started: 2026-09-30T00:00:00Z
tags:
  - visuals
  - image-generation
  - research
visibility: public
---

# Image references and visual stickiness in conversational generation

David observed that successive images in ChatGPT and Codex can feel like
variations of one image, where he expected independent and more divergent
generations. He asked how supplying a previous image as a reference actually
appears in a Codex image tool call. This follows the [Memory Engine visual
drafts](./memory-engine-visual-drafts-missed-target.md), none of which David
approved as a target reference.

The built-in Codex `image_gen__imagegen` call accepts a text `prompt` plus
either `referenced_image_paths` (local image paths) or
`num_last_images_to_include` (recent conversation images without paths). For
brand-new images, omit both reference arguments. The earlier Memory Engine
sequence included calls that explicitly supplied the preceding draft as a
reference, as well as calls without image references whose prompts repeated
subjects and motifs. This is a direct observation about the agent's requests;
it does not establish any hidden image-model session state.

OpenAI's [image generation guide](https://developers.openai.com/api/docs/guides/image-generation) distinguishes
generation from scratch and edits. In the Responses API image tool, a
conversation can include earlier images; `action: "auto"` permits the model to
choose generate or edit, while `action: "generate"` explicitly requests a new
image. The built-in Codex tool available in this session does not expose that
`action` parameter. The [tool guide](https://developers.openai.com/api/docs/guides/tools-image-generation) also
describes prompt rewriting by the mainline model. These features make
conversational continuity a plausible contributor, but do not prove how
ChatGPT or this Codex tool internally handled each call.

Other users have described similar style persistence in the
[OpenAI Developer Community](https://community.openai.com/t/image-model-stuck-on-the-same-style/1357399)
and a separate [visual-context bug report](https://community.openai.com/t/bug-report-severe-context-contamination-in-gpt-4o-image-generation-upcoming-api-implications/1164076).
Those are anecdotes, including older model versions, rather than verified
explanations of the current implementation.

For future exploration, generate several independent concepts from distinct
text prompts with no image reference. Use a prior image only when deliberately
refining that image or retaining its composition/style. A fresh conversation
can reduce conversational anchoring, but independent calls can still resemble
one another when their prompts and model defaults are similar.

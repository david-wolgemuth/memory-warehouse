---
tags:
  - llm-models
  - llm-costs
  - model-comparison
  - hermes
  - research
visibility: public
---

# Public model catalogs and comparison sources

## User direction

David asked for good places to find models, compare quality and price, and
programmatically retrieve that information without an API key. The context is
finding a paid Hermes alternative to its bundled free
`upstage/solar-pro4:free` model that might have comparable or better quality
per dollar.

## Direct observations on 2026-09-19

The following unauthenticated HTTP endpoints returned successfully:

| Source | URL | What it exposes | Best use |
| --- | --- | --- | --- |
| OpenRouter model catalog | `https://openrouter.ai/api/v1/models` | Model identifiers, context window, modalities, parameter support, and token prices | Primary data source when buying through OpenRouter |
| OpenRouter model endpoint detail | `https://openrouter.ai/api/v1/models/{model-id}/endpoints` | Route/provider-specific price, context limit, cache price, and supported parameters | Verify the actual route before switching Hermes |
| Models.dev catalog | `https://models.dev/api.json` | Large cross-provider catalog of models and capabilities/pricing metadata | Broad discovery; independently verify a shortlisted provider price |
| Hugging Face Hub models API | `https://huggingface.co/api/models` | Open-model metadata, tags, downloads, licenses, and files | Find self-hostable candidates; not a hosted-price comparison |

OpenRouter's endpoint for `upstage/solar-pro4` returned $0.09/M input,
$0.018/M cached input read, and $0.36/M output. The catalog also contained
lower-price text models with at least 65K context, such as Mistral Nemo,
Qwen 3.7 Flash, OpenAI gpt-oss-20b, and DeepSeek V4 Flash. This establishes
only price and advertised capability; it is not evidence that any is a
quality-equivalent replacement for Hermes.

## Quality sources and limits

LMArena's public website is the strongest broadly useful human-preference
comparison for chat quality, though its attempted anonymous
`https://arena.ai/api/leaderboard` request returned HTTP 403. Treat its site
as a browseable corroborating quality signal rather than a reliable
no-key-API dependency. Artificial Analysis is similarly useful for its public
quality, speed, and price comparisons, but its commercial data should be
checked in the site rather than scraped as a stable interface.

## Recommended workflow

Use OpenRouter as the machine-readable source of truth for price and route
availability. Filter its model catalog for the Hermes requirements (especially
tool calling, structured output, context size, and cache pricing), then use
LMArena or Artificial Analysis to shortlist quality candidates. Finally, run
the same representative Hermes tasks against two or three candidates and
measure success rate, latency, and actual OpenRouter cost from the response
usage. Public leaderboards cannot establish agent/tool-use reliability for a
specific personal workflow.

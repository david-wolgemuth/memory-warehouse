---
harness: codex
session_id: ''
started: 2026-09-11 00:00:00+00:00
tags:
- ai-exports
- projects
- provenance
- lineage
- methodology
visibility: public
---

> Some links or assets are omitted from this public edition. References to omitted files and commands using them apply to the private source.

# AI export review maps project lineage rather than only directory names

## Record

- Old Codex and Claude exports are historical evidence of activity, not a
  ready-made project index. Review them in reverse chronology, beginning with
  lightweight session metadata (date, working directory, first user turn) and
  reading conversation detail only where it can establish a relationship.
- A project link is **direct** when an exported working directory, named
  repository, current README, Git origin, or matching commit history establishes
  the identity. A historical directory can still map to a current repository
  when the implementation history and documentation corroborate a rename or
  move.
- A link is **thematic** when a conversation shares ideas, tools, or subject
  matter with a project but does not establish the same codebase or continuing
  effort. Keep thematic links in a log as leads; do not turn them into project
  cards by default.
- Some sessions happen from a home directory, a shared infrastructure
  repository, or an untracked working directory. Associate them with a project
  only when a configuration path, repository evidence, or explicit discussion
  establishes the connection. Otherwise record the session as an unattributed
  context or shared-infrastructure thread.
- A project line may be a graph, not a one-to-one mapping: infrastructure can
  support several projects, an exploratory project can become a renamed
  implementation, and multiple experiments can share a domain. Cards may link
  such durable relationships, while the dated log preserves the evidence and
  ambiguity behind them.

## Practical output

Historical note: the visibility terminology in item 4 was superseded on
2026-09-30. Current policy uses `public` and `private`; omitted means private.

1. Create a dated batch log with export paths, evidence type, links found, and
   uncertainty.
2. Create or update a project card only for a confirmed, reusable project
   identity; include its current local location, public repository when known,
   and pointers back to relevant export history.
3. Use `related` card links for durable lineage or shared-infrastructure
   relationships. Do not use cards as a transcript index or a task tracker.
4. Apply visibility deliberately: `public` only after review, `restricted` for
   retained private context requiring a fresh sharing review, and `private` or
   no marker for ordinary private-source material.

## Sources

- User conversation, 2026-09-11.
- `logs/2026/09/11/codex-reverse-review-september-project-links.md` (unavailable in this public edition).
- `logs/2026/09/11/codex-reverse-review-august-july-project-links.md` (unavailable in this public edition).
- `logs/2026/09/11/claude-projects-and-local-repositories.md` (unavailable in this public edition).

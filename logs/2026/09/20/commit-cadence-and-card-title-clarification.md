---
harness: codex
tags:
- governance
- git
- user-direction
visibility: public
---


# Commit cadence and card-filename clarification

## User direction

David clarified that card filenames, not display titles, should normally remain
stable: filenames function as references, and a deliberate filename rename
requires updating all references. The `AGENTS.md` (unavailable in this public edition) link text may add operational
nuance without renaming the linked card.

David also clarified the intended commit cadence. Agents should batch related
Warehouse edits into meaningful checkpoints rather than committing after every
file or small change. The practical guardrail is to avoid allowing roughly one
or two hours of substantive work to pass without a commit. A forgotten
uncommitted change is not an emergency; a later agent should review and pick
it up under the existing meaningful-untracked-file presumption.

Source: David's direction in this conversation, 2026-09-20.

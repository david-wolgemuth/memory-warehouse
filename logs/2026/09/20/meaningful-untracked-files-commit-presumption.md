---
harness: codex
started: 2026-09-20 12:27:50+00:00
tags:
- governance
- git
- user-direction
visibility: public
---

> Some links or assets are omitted from this public edition. References to omitted files and commands using them apply to the private source.

# Meaningful untracked files are presumed commit-worthy

## User direction

David asked that the existing Warehouse rule to assume meaningful untracked
files should be committed receive its own card and a direct `AGENTS.md` (unavailable in this public edition) link.
This followed an agent incorrectly deferring to a generic untracked-worktree
precaution instead of applying the Warehouse checkpoint policy.

## Decision

At a natural checkpoint, agents should review meaningful untracked Warehouse
files for generated, temporary, secret, or deliberately deferred material, but
should otherwise stage, commit, and push them. The mere fact that another
session created a file is not a reason to leave it uncommitted or ask the user
to decide.

Source: David's direction in this conversation, 2026-09-20; see also the
earlier checkpoint-policy record.

## Related evidence

- [Checkpoint-policy record](../12/commit-meaningful-uncommitted-warehouse-changes.md).

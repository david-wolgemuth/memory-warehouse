---
date: 2026-09-12
source: user direction in this conversation
visibility: public
---

> Some links or assets are omitted from this public edition. References to omitted files and commands using them apply to the private source.

# Commit meaningful Warehouse changes instead of leaving them uncommitted

David clarified the commit policy after a scoped commit left other meaningful
untracked Warehouse logs in the worktree. At a natural checkpoint, agents
should assume uncommitted tracked and untracked changes are appropriate to
commit and push.

The only exclusions are files that are clearly generated, temporary, secret,
or otherwise intended for `.gitignore`, plus changes that require a separate
deliberate decision. Agents should still review the staged diff, but should not
treat another session's work as unrelated by default or leave useful Warehouse
work uncommitted for that reason.

The policy now has its own card and is linked from the `AGENTS.md` (unavailable in this public edition) reading
index.

## Follow-up: maintain ignore rules

David clarified that a file excluded because it is generated, secret,
temporary, or otherwise not versioned must prompt an update to `.gitignore` or
the appropriate ignore mechanism in the same turn. Agents should not leave it
as recurring worktree noise. Ignore rules must be narrowly scoped; they do not
replace removing a committed secret or addressing an existing exposure.

---
tags:
- communication
- agent-memory
- style-guide
- governance
ledger:
- ../logs/2026/09/16/four-layer-style-guide-design.md
related:
- ./agent-replies-are-mobile-friendly-and-log-linked.md
- ./agent-memory-retains-context-and-scope.md
confidence: medium
created: 2026-09-16 00:00:00+00:00
review_after: 2026-12-16 00:00:00+00:00
visibility: public
---

> Some links or assets are omitted from this public edition. References to omitted files and commands using them apply to the private source.

# Style guidance uses separate defaults, templates, scoped feedback, and evaluations

Keep the always-loaded default style small. Use templates for artifact-specific
structure, provenance-linked records for corrections, and concrete evaluation
cases to test the resulting behavior.

## Why it matters

One long style prompt competes with task instructions and overgeneralizes
formatting or corrections. Separate layers give the agent useful direction at
the right time while retaining the conditions that make a preference true.

## Boundaries

This is a proposed architecture, not proof that every listed default or
template improves agent behavior. Keep individual rules as drafts until actual
work and evaluation cases show that they help. User-specified formats, safety
requirements, exact quotations, and artifact audiences take priority over the
default voice.

## Resources

- [Four-layer style-guide design log](../logs/2026/09/16/four-layer-style-guide-design.md) records the detailed design, initial templates, and proposed evaluation suite.

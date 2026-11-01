---
tags:
- cards
- projects
- metadata
visibility: public
---


# Project-card metadata pattern

On 2026-09-13, David directed that the home-workstation card be aligned with
the established project-card pattern and that this pattern be preserved as a
meta card.

Direct observation of the existing project cards and `indexes/projects.md` (unavailable in this public edition):
each project card records a compact project identity, provenance-linked ledger,
repository URL and visibility, card visibility rationale, and comparable
activity fields. The activity fields are `project_started`, `last_active`,
`activity_basis`, `activity_status`, and `activity_as_of`.

The project index defines the status thresholds as of 2026-09-12: current is
activity within 14 days, recent within 180 days, and dormant otherwise. It also
states that last activity normally means the latest repository commit; a named
project-specific session is used only when it is newer and more direct.

## Sources

- User direction, 2026-09-13.
- `indexes/projects.md` (unavailable in this public edition).
- `logs/2026/09/11/project-cards-and-log-detail-pattern.md`.
- Direct read of all existing `cards/*-project.md` records, 2026-09-13.

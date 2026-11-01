---
tags:
- cards
- projects
- metadata
- provenance
ledger:
- ../logs/2026/09/11/project-cards-and-log-detail-pattern.md
- ../logs/2026/09/13/project-card-metadata-pattern.md
related: []
confidence: high
created: 2026-09-13 00:00:00+00:00
visibility: public
---

> Some links or assets are omitted from this public edition. References to omitted files and commands using them apply to the private source.

# Project cards record compact repository profiles

A project card states a project’s durable identity, local source, repository
metadata, and activity signal. It uses `project_started`, `last_active`,
`activity_basis`, `activity_status`, and `activity_as_of` so project activity
can be compared consistently. It separately records repository visibility and
the reviewed basis for the card’s own visibility.

## Boundaries

Keep the card lean and factual. Put detailed commit history, session evidence,
uncertainty, and import analysis in linked dated logs. Use the latest repository
commit for `last_active` unless a newer, directly relevant named project
session is better evidence. Project cards describe repository profiles; they
do not serve as task trackers.

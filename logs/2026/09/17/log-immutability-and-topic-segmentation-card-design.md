---
date: 2026-09-17
source: user direction and design discussion in this conversation
tags:
- warehouse
- logs
- cards
- agent-behavior
- user-direction
visibility: public
related:
- ./log-topic-drift-and-tangent-boundary.md
---

> Some links or assets are omitted from this public edition. References to omitted files and commands using them apply to the private source.

# Log immutability and topic segmentation are separate card concepts

## User direction

David observed that the existing "Logs are append-only-ish" card could either
be edited to express the new-log boundary or remain focused while a new card
with a distinct title explains it. He noted that the two are slightly different
concepts.

## Design assessment

They should be separate cards. Append-only-ish describes how an established
historical record may be changed: only for an obvious error or omitted fact.
Topic segmentation describes when to create a record: a drift in subject,
tangent, or distinct later development starts another small, subject-named
log. Keeping the claims distinct makes each easier to retrieve and apply.

## Proposed follow-up, not yet applied

Create a focused card such as "Topic shifts and tangents start new logs," link
it to the append-only card, and list both under AGENTS.md's log-recording
section. Align the related communication card with the same wording if needed.

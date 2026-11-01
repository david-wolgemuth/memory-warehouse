---
tags:
- agents
- autonomous-agents
- orchestration
- scheduling
- architecture
ledger: []
related: []
confidence: high
created: 2026-09-19 00:00:00+00:00
visibility: public
---


# A deterministic harness coordinates stateless agent runs

For a long-running autonomous project, scheduling, work selection, exclusion
locks, budgets, output validation, and stop conditions belong in a
deterministic harness and project state, not in a persistent or supervisory
LLM conversation. Each fresh agent run receives one role-specific, bounded
job, reads only the relevant evidence and state, then writes a reviewable
result.

## Why it matters

The harness creates reproducible control flow and makes idle a valid outcome.
It avoids paying for an LLM merely to dispatch another LLM, limits accumulated
context drift, and lets QA reject changes before they become later agents'
assumptions.

## Boundaries

This does not prohibit agents from prioritizing or reflecting within their
assigned work. The project still needs an explicit, inspectable mutable work
ledger distinct from its append-only logs and durable knowledge records.

## Resources

- Staged stateless agent-loop direction (unavailable in this public edition)
  — user direction and proposed research-to-reflection roles.
- Long-running agent experiments need legible artifacts and feedback (unavailable in this public edition)
  — accumulated artifact and feedback requirement.

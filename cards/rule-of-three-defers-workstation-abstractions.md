---
tags:
- workstation
- tooling
- design
- abstraction
ledger:
- ../logs/2026/09/12/rule-of-three-history-and-workstation-application.md
related: []
confidence: high
created: 2026-09-12 00:00:00+00:00
visibility: public
---

> Some links or assets are omitted from this public edition. References to omitted files and commands using them apply to the private source.

# The rule of three defers workstation tooling abstractions

For the workstation setup, retain a direct package list or small explicit step
until three genuine, similar needs show that a shared mechanism is warranted.
Only then introduce an extra package ecosystem, generic bootstrap helper, or
compatibility-shim layer.

## Why it matters

The rule follows the refactoring heuristic “three strikes, then refactor”:
concrete repetition reveals the common shape of a problem and reduces the risk
of creating a wrong abstraction for a one-off need.

## Boundaries

Three is a prompt to evaluate, not an automatic mandate. A material security,
maintenance, or usability concern may justify acting sooner; three superficially
similar cases may still deserve separate solutions. This principle does not
prevent using a well-supported existing package manager where it is already a
clear fit.

## Resources

- [Martin Fowler on the Rule of Three](https://martinfowler.com/articles/practical-test-pyramid.html).
- `logs/2026/09/12/rule-of-three-history-and-workstation-application.md`.

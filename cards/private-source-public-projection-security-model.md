---
tags:
- governance
- security
- privacy
- open-source
ledger:
- ../logs/2026/09/11/visibility-metadata-for-public-projection.md
- ../logs/2026/09/11/restricted-visibility-for-private-context.md
- ../logs/2026/09/12/visibility-annotations-and-reasoned-disagreement.md
- ../logs/2026/09/12/publication-safety-and-visibility-research.md
related:
- ./agent-replies-are-mobile-friendly-and-log-linked.md
confidence: high
created: 2026-09-11 00:00:00+00:00
visibility: public
---

> Some links or assets are omitted from this public edition. References to omitted files and commands using them apply to the private source.

# Warehouse separates private source memory from a public projection

Warehouse is the private source repository. Records have two effective
visibility states: `public` and `private`. An omitted `visibility` field means
private. Use `visibility: private` when an explicit label helps; do not use
`restricted`. A public projection selects only records explicitly marked
`visibility: public` and reviewed in their current form.

Prefer a small public card or log when its useful point can be expressed safely.
Split topic shifts and tangents into separate records so one private detail does
not force an otherwise publishable subject to stay private. A private source
repository, local path, personal preference, or private evidence link alone is
not a reason to classify the current record as private.

Keep a whole record private when its topic is intentionally excluded from the
public projection, or when a safe rewrite would lose its useful point. For a
mixed record, write a public version that omits or replaces sensitive details
with a plain `[redacted]` marker where that helps readers; keep the original
detail only in private source history or a separate private record. A marker
must not reveal the omitted detail through its wording, metadata, links, or
filename. Do not place credentials or recovery material in Warehouse at all.

Publish into a separate public repository. GitHub visibility applies to the
repository, not to individual branches, and the public repository must have
its own history containing only reviewed projected content.

Before every public copy, review the exact projected files and their links,
frontmatter, filenames, and assets. A small model can propose downgrades to
private or public rewrites, but its judgment is not proof of safety. The copy
step must fail closed on unreviewed changes or detected sensitive content and
must never copy the private repository's Git history. Run this same review once
over existing records before first publication, then on each subsequent copy.
Record review outcomes in private source memory so decisions can be revisited.

## Resources

- `AGENTS.md` (unavailable in this public edition) — operating policy and publication rules.
- `logs/2026/09/12/publication-safety-and-visibility-research.md` — sources
  and fuller exclusion guidance.

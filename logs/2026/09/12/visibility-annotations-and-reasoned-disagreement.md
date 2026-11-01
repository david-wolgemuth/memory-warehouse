---
date: 2026-09-12
source: user direction in this conversation
visibility: public
---


# Visibility annotations are deliberate, and agents should reason openly

Historical note: the visibility rules below were superseded on 2026-09-30.
Current policy uses `public` and `private`; omitted visibility means private.

## Visibility correction

David reviewed two visibility decisions made during this conversation and gave
specific corrections:

- `mobile-friendly-agent-communication-preference.md` is appropriate for
  `visibility: public`. It contains general communication and log-maintenance
  guidance that would be safe to publish as a blog post.
- `claude-web-prompt-structure-preference-review.md` (unavailable in this public edition) should omit the
  `visibility` field. It references a private source boundary but does not
  reproduce account data, credentials, or sensitive source contents. Its
  content alone does not warrant an explicit private or restricted label.

The original classifications were too conservative. The communication record
was marked private merely because it expressed a personal preference, although
the preference is non-sensitive. The export-review record was marked restricted
because it cited external private-source paths, even though the log carefully
excluded sensitive contents. Neither reason is sufficient on its own.

## Standing rule

An omitted `visibility` key is not an agent declaration that a record is
private. It receives the repository's normal non-public treatment, while
remaining unclassified. Agents should therefore omit the key unless an
explicit classification adds useful information:

- `public` for records deliberately suitable for a future public projection;
- `private` for personal, work, or operational context where the explicit
  private classification matters; and
- `restricted` for private material that needs a fresh, explicit review before
  sharing beyond the private source repository.

The practical test is whether a record could safely be published as a
high-level blog post without creating a reasonable concern that its information
could be used against David or others. A local path or a private-source citation
alone does not make the record private or restricted.

## Reasoned disagreement

David also directed agents not to become automatic yes-men. Agents should state
the concrete evidence when they disagree with a proposed action or
classification, ask for clarification when it is materially needed, and offer
a safer alternative when available. They should not invent disagreement when
the user's reasoning is supported by the evidence.

This is now recorded in `AGENTS.md` (unavailable in this public edition) as a repeatable operating rule.

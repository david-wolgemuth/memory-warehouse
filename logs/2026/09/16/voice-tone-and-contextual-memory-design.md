---
date: 2026-09-16
source: user statement and supplied examples in this conversation; external style sources reviewed
visibility: public
---

# Voice should be plain, artifact-aware, and conditional

## Direction from David

David asked to examine the ideal voice and tone for Warehouse logs, cards, and
related agent work. He supplied a Claude memory record about not creating
unrequested Jira tickets, a discussion of Claude memory overgeneralizing from
corrections, and a tentative personal Claude output style called "Plainspoken."

The ticket example is useful because it includes the event, the rationale, and
how to apply the instruction. It is also a warning: its use of "only" and
"never" is appropriate only because David explicitly gave that narrow,
behavioral direction. A one-off preference in one context must not silently
become a universal agent rule.

David said that the Plainspoken style is an experiment and that he is not yet
sure it has materially helped. Its detailed rules are therefore a design lead,
not an adopted Warehouse-wide contract. The established preference for short,
plain, mobile-friendly agent replies remains documented in
[the 2026-09-12 communication log](../12/mobile-friendly-agent-communication-preference.md).

## Recommended voice by artifact

| Artifact | Primary job | Voice and structure |
| --- | --- | --- |
| Chat reply | Help David decide or act now | Lead with the outcome or next action. Use direct, plain language. Include the mechanism and risk when they affect the decision. Keep supporting detail in a linked log. |
| Log | Preserve what happened and why | Be concrete, evidence-linked, chronological when useful, and candid about uncertainty. Distinguish David's statements, direct observations, external sources, and agent inferences. Rough prose is acceptable. |
| Card | Give a future agent one reusable belief | State one compact claim. Explain why it matters and define its boundaries. Link the local evidence. Name a condition, counterexample, or review point when a conclusion depends on context. |
| Skill or instruction | Make a repeatable action reliable | State the actor, trigger, action, and exception. Use exact constraints where failure would matter. Do not hide a material judgment inside a broad stylistic rule. |
| Requested outward-facing artifact | Produce text for its intended reader | Follow the requested format and audience. Return the artifact without chat ceremony when David asks for the artifact itself. |

## Memory design conclusions

The main failure mode in agent memory is not confidence alone. It is losing the
scope that made a correction true. A durable preference record should retain:

- the source and wording of the direction;
- the situation that triggered it;
- the actor and object it applies to;
- the rationale or harm avoided;
- exceptions, counterexamples, or unknown scope; and
- a link to the event evidence.

Use a universal verb such as "always" or "never" only when David explicitly
sets a durable, broad rule or when the rule is a verified invariant. Otherwise,
describe the observed context: for example, "For unrequested outward-facing
artifacts, report the finding and wait for explicit authorization." This stays
specific without being timid.

Promote an event log to a card when it contains a reusable rule with stable
scope. Keep a contextual correction in a log when the same request has not
recurred, when its boundaries are unclear, or when it is only an agent's
interpretation. A later event can refine the scope with a new log rather than
rewriting history.

## Assessment of the Plainspoken draft

The strongest parts are answer-first structure, plain and consistent words,
active phrasing with a named actor, concrete mechanisms instead of vague
assurances, and guardrails that preserve exact technical material. They match
David's existing communication preference and Google guidance for clear,
respectful developer writing.

Some rules should remain preferences or checks rather than global prohibitions:

- A strict second-person, present-tense voice does not fit every log, history,
  code review, quotation, or artifact.
- A mandatory gloss for every domain term can obscure writing for an expert
  audience. Define terms when the likely reader needs the definition.
- A ban on every em dash or analogy is an editing preference, not a reliability
  rule. Apply it to agent prose if it helps the voice, but never alter quoted or
  byte-sensitive text.
- A closing sentence that a reader can repeat is useful for a decision or
  explanation, but redundant for a short status update or a requested artifact.
- Exact negative-word lists can turn into prompt noise. Prefer positive,
  observable checks: answer first, name the actor and mechanism, retain the
  necessary conditions, and remove ceremony that adds no meaning.

## Sources

- David's supplied Claude memory example, discussion thread, and Plainspoken
  output-style draft, 2026-09-16.
- [Google developer documentation voice and tone guide](https://developers.google.com/style/tone), reviewed 2026-09-16. It supports conversational, respectful, direct language while warning against jargon, filler, choppy prose, and claims that a procedure is easy.
- [awesome-claude-output-styles](https://github.com/smixs/awesome-claude-output-styles), reviewed 2026-09-16. Its useful general design principles are positive, checkable constraints; preservation of byte-exact technical material; and exceptions for depth, requested artifacts, and safety-critical text. Its implementation and claims about Claude behavior are not evidence for Warehouse behavior.

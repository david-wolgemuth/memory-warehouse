---
date: 2026-09-16
source: user direction and discussion in this conversation
visibility: public
related:
  - ./voice-tone-and-contextual-memory-design.md
  - ../12/mobile-friendly-agent-communication-preference.md
---

# A style guide needs defaults, templates, scoped feedback, and evaluation cases

## The design problem

An agent's underlying training shapes its default register, confidence, and
idea of a complete response. An instruction can steer those habits, but it
cannot reliably replace them while the agent is also handling a difficult task,
tool output, safety constraints, and repository-specific requirements.

A style guide should therefore assign each layer a narrow job:

| Layer | Job | It must not do |
| --- | --- | --- |
| Default style | Set the normal reader-facing voice | Encode every artifact format or every past correction |
| Artifact template | Supply structure for a particular kind of writing | Pretend the structure is the voice |
| Scoped memory | Preserve a real correction with its conditions | Generalize one event into an unconditional rule |
| Evaluation case | Test whether behavior remains useful over time | Become a rhetorical example that nobody checks |

This arrangement is more resilient than a single, long output prompt. It keeps
the always-loaded guidance short and places detail only where it changes the
work.

## 1. The default style is a small, observable contract

Use these five defaults for ordinary agent prose:

1. **Lead with the answer, decision, or next action.** Do not restate the
   request or add a social preamble.
2. **Name the actor and mechanism when they affect the reader's decision.**
   Say who does what and why, rather than offering a vague assurance.
3. **Use direct, consistent, plain words.** Keep necessary technical terms.
   Define one only when the intended reader is unlikely to know it.
4. **Keep the necessary conditions, evidence, numbers, and risks.** Brevity
   removes ceremony, not reasoning. A request for depth increases detail while
   retaining the same discipline.
5. **Preserve exact technical material.** Do not stylistically alter code,
   commands, error messages, file paths, identifiers, quoted text, numbers, or
   order-critical conditions.

The first four rules guide voice. The fifth protects correctness. Together,
they are small enough to remember and concrete enough to evaluate.

### Default-style boundaries

The default yields to a user-specified format, the reader of an external
artifact, a quotation, a security or destructive-action warning, and other
content where exact wording matters. It should also yield to a short factual
answer where an explanation would repeat the answer.

Do not use an exhaustive ban list as the default. Lists of disfavored words,
punctuation, or sentence shapes are useful for an optional editing pass, but
they compete with the task and create false violations. A reader should notice
the positive qualities above, not a model trying to avoid a visible list of
forbidden tokens.

## 2. Templates give each artifact its own job

The following templates define information order. They are not all mandatory
headings. A short answer can use the structure without printing a template.

### Chat reply template

Use chat to make the immediate result easy to scan.

```text
<Answer, decision, or completed action.>

<The reason, mechanism, or evidence that changes the decision.>

<A caveat, risk, or remaining choice, only when it changes what David should do.>

<Link to a detailed log when the work has a durable record.>
```

For a status update, replace the reasoning with what changed and what remains.
For a requested bare artifact, return only the artifact.

### Log template

Historical note: the example below predates the 2026-09-30 visibility change.
Current policy uses only `public` and `private`; omitted visibility is private.

Use a log to preserve the evidence and working context that a short reply
would hide.

```markdown
---
date: YYYY-MM-DD
source: user statement | direct observation | external sources | agent inference
visibility: private | restricted | public
---

# One event, finding, decision, source set, or open question

## What happened or what is known

State the event or observation. Attribute it close to the claim.

## Context and interpretation

Explain the trigger, mechanism, uncertainty, and agent inference. Keep a user
statement separate from an inference about how to apply it.

## Consequence or open question

State what changed, what remains unknown, or why no action follows yet.

## Sources

Link the user statement, direct evidence, commands, files, or external source.
```

Logs can be informal. They do not need a polished conclusion, and later
understanding normally gets a new topic-named log rather than a rewrite of the
event record.

### Card template

Use a card only for a claim that a future agent should retrieve across tasks.
The existing Warehouse card template has the right shape:

```markdown
# One qualified, reusable claim

State the claim in one or two sentences.

## Why it matters

State the action or inference the claim changes.

## Boundaries

State conditions, exceptions, uncertainty, or a review trigger.

## Resources

Link the log, direct observation, user statement, or primary source.
```

Prefer a conditional claim over a broad slogan. "For unrequested
outward-facing artifacts, wait for explicit authorization" is more useful than
"Never create tickets" because it names the situation without extending the
rule to unrelated work.

### External-artifact template

The requested audience and format take priority over the agent's default
voice. A commit message, pull-request description, email, issue, review reply,
or documentation page has different conventions and readers.

Before drafting, identify the artifact's reader, purpose, required format,
facts that must stay exact, and whether David explicitly authorized creating or
sending it. Then produce the artifact without a chat wrapper when he requested
the artifact itself. Do not infer permission to create an outward-facing object
from a discussion of it.

## 3. Feedback becomes memory only with its scope intact

Every correction is evidence. Not every correction is a global instruction.
Record the smallest durable form that preserves the information future agents
need to apply it correctly.

### The record shape

Each feedback record should answer these questions:

| Field | Purpose |
| --- | --- |
| Source | Who said it, when, and where can a future agent verify it? |
| Triggering situation | What was happening when the correction occurred? |
| Direction | What action, decision, or writing behavior changed? |
| Scope | Which actor, object, task type, or condition does it cover? |
| Rationale | What harm, cost, or preference does it address? |
| Boundaries | What does it not establish? What remains uncertain? |
| Evidence link | Where is the original event recorded? |

This is not bureaucratic metadata. It is the information that prevents an
agent from turning a local correction into a false universal rule.

### The promotion rule

| Evidence | Warehouse layer | Example |
| --- | --- | --- |
| One correction with unclear wider scope | Log | "Do not infer that selecting a described option authorizes creating the ticket." |
| Explicit broad direction from David | Card, and possibly operating instructions | "Do not create any outward-facing artifact without explicit authorization." |
| Same preference across several independent situations | Card | "Lead ordinary agent replies with the outcome." |
| Repeatable multi-step method | Skill | A documented review, deployment, or research procedure |
| Agent interpretation without direct confirmation | Log, labeled as inference | "This may reflect a preference for X; confirm before enforcing it broadly." |

When later evidence changes the rule, add a new log that says what changed and
why. Update the card only after the change is durable. This preserves history
and prevents a clean current summary from pretending that it was always known.

## 4. Evaluation cases measure behavior, not resemblance to a prompt

A style guide is useful only if someone can tell whether it improved an answer.
Keep a small suite of real or carefully anonymized examples. Each case should
include the task, the relevant facts, an undesirable response pattern, the
desired response, and explicit acceptance checks.

### Initial evaluation suite

| Case | Prompt situation | Failure to catch | Pass condition |
| --- | --- | --- | --- |
| Local correction | David corrects an action that happened in one context | The agent writes a global "never" rule without the triggering condition | The log names the context and the card is created only if broader scope is explicit or evidenced. |
| Diagnosis | A test fails after a change | The answer says it is "likely" a general issue without naming the failing mechanism | The first sentence states the cause or uncertainty. The explanation names the file, path, or observed behavior that supports it. |
| Deep explanation | David asks why a design behaved unexpectedly | The answer stays short and omits decisions, thresholds, risks, or alternatives | The answer covers the causal chain and material tradeoffs in reader order. |
| Requested artifact | David requests a commit message or email | The agent adds a preamble, explanation, or unsolicited alternatives | The response contains only the requested artifact in the requested form. |
| Exactness | An answer includes a command or condition such as `only after restart` | The style pass paraphrases or widens the instruction | The command, number, path, quote, and condition remain exact. |

### How to use the cases

Run the cases whenever the default style, templates, memory process, or model
changes materially. Evaluate the full response, not isolated sentences. Check
first for factual correctness and authorization, then scope retention and
reader usefulness, and only then surface voice.

Use a short checklist for each result:

- Did the response preserve the requested or observed facts?
- Did it keep conditions and uncertainty instead of widening them?
- Did it identify the answer or next action early?
- Did it give enough mechanism and evidence for the reader's decision?
- Did it match the requested artifact and audience?
- Did its detail level match the task?

Automated checks can flag easy surface regressions, such as an added preamble
around a bare artifact or a changed command string. They cannot reliably judge
whether an explanation is calibrated or whether a correction retained the
right scope. Periodic human review remains necessary, especially for examples
that would affect external actions or durable memory.

## Adoption sequence

1. Treat the five default rules as a draft and use them for ordinary agent
   prose.
2. Use the artifact templates when creating or revising the relevant type of
   record, without forcing their headings into short replies.
3. Record new corrections with source and scope before promoting them to a
   card or instruction.
4. Add a case to the evaluation suite whenever a real failure exposes a gap.
5. Review the suite after enough examples accumulate to determine whether a
   rule improves answers or merely makes them more uniform.

This makes style a maintained system of behavior and evidence, rather than a
single aspirational prompt.

## Sources

- David's direction to develop the four layers for the style guide,
  2026-09-16.
- [Voice, tone, and contextual-memory design log](./voice-tone-and-contextual-memory-design.md), 2026-09-16.
- [Agent replies are mobile-friendly and log-linked](../../../../cards/agent-replies-are-mobile-friendly-and-log-linked.md), Warehouse card.
- [Agent memory retains the context and scope of a correction](../../../../cards/agent-memory-retains-context-and-scope.md), Warehouse card.

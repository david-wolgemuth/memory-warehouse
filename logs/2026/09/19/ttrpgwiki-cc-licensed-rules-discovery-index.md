---
tags:
- tabletop-rpg
- data-curation
- licensing
- autonomous-agents
- source-discovery
visibility: public
related:
- ../../../../cards/dmsim-uses-rule-system-inspirations-without-adopting-their-rules.md
---


# TTRPG Wiki CC-licensed rules discovery index

## Direct observation (2026-09-19)

David supplied <https://ttrpgwiki.com/?tags=CC-Licensed+Rules> as a possible
source for the proposed provenance-first TTRPG procedure/open-rules index.
The public page preloads two no-authentication JSON catalogs:

- <https://ttrpgwiki.com/data/systems.json?v=2>
- <https://ttrpgwiki.com/data/tag-taxonomy.json?v=1>

At retrieval, the systems catalog had 280 records; 44 carried the
`CC-Licensed Rules` tag. The taxonomy defines that tag as complete core rules
released under a Creative Commons license permitting redistribution and
adaptation, including noncommercial variants. It explicitly excludes OGL,
ORC, Year Zero Engine OGL, Forged in the Dark, and similar source-text
licenses.

The full taxonomy has 100 tags in five categories: Play Structure & Table
Format; Mechanics & Character Design; Tone, Premise & Subgenre; Accessibility
& Session Fit; and Product & Licensing Metadata. Each tag has a label and
definition, and some have aliases. It can therefore be retrieved as a
controlled-vocabulary source, not merely an opaque website filter.

The catalog supplies useful candidate metadata including system name and
edition, tags, declared license, official URL where available, core mechanic,
and editorial highlights/considerations. Examples in the tagged subset include
Fate Core, Cairn, Basic Fantasy RPG, Ironsworn, Eclipse Phase, Lasers &
Feelings, Freeform Universal, Wicked Ones, and OpenQuest.

## Collection implication

TTRPG Wiki is a strong no-key discovery index and can seed bounded candidate
selection without downloading rulebooks. It is not primary license evidence:
each included system must preserve and verify its publisher/SRD license URL,
license version and scope, attribution requirements, access date, and any
exceptions before the curator treats text as reusable. The catalog itself
demonstrates this need: its Dungeons & Dragons entry distinguishes the CC BY
4.0 SRD from proprietary core books.

The initial artifact should store provenance and concise original procedure
classification, with links to authorized rules sources; it should not mirror
or redistribute commercial books.

## Design-palette use

David proposed using the tag taxonomy as a list of features that an autonomous
TTRPG game/framework could add. This is a useful alternate use of the source:
the tags' qualifying definitions can become acceptance criteria for a proposed
feature, rather than vague inspiration labels.

The taxonomy should be normalized before entering a game backlog. Its 40
Mechanics & Character Design and 25 Play Structure & Table Format tags are
mostly addable mechanics or procedures (for example, faction play, journey,
map drawing, resource management, random tables, or base-building). The 27
Tone, Premise & Subgenre tags are creative constraints/outcomes that need a
supporting procedure before they can be claimed. The six Accessibility &
Session Fit tags are usability goals. The two Product & Licensing Metadata tags
are release-policy facts, not in-game mechanics.

For each chosen tag, a project should require an original, small feature card:
the intended player-facing behavior, minimal state/procedure, testable
qualification against the taxonomy definition, interactions/conflicts with
existing features, and provenance/attribution to the tag source. Tags can
inspire new original mechanics but do not authorize copying a tagged game's
specific rules text.

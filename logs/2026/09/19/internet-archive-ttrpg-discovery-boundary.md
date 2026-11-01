---
tags:
- tabletop-rpg
- data-curation
- licensing
- internet-archive
- source-discovery
visibility: public
related:
- ./ttrpgwiki-cc-licensed-rules-discovery-index.md
- ../../../../cards/dmsim-uses-rule-system-inspirations-without-adopting-their-rules.md
---

> Some links or assets are omitted from this public edition. References to omitted files and commands using them apply to the private source.

# Internet Archive TTRPG discovery boundary

## User-provided lead and direct observation (2026-09-19)

David supplied <https://archive.org/search?query=subject%3A%22ttrpg%22> as
another potential TTRPG source. Internet Archive offers an unauthenticated,
machine-readable search endpoint:

<https://archive.org/advancedsearch.php?q=subject%3A%22ttrpg%22&fl%5B%5D=identifier&fl%5B%5D=title&fl%5B%5D=licenseurl&fl%5B%5D=rights&fl%5B%5D=mediatype&rows=50&page=1&output=json>

The supplied subject query returned 4,438 results at retrieval. The first 50
were materially heterogeneous: audio episodes, images, fan-wiki mirrors,
unrelated material with a keyword match, and scans of commercial TTRPG books,
alongside some records declaring Creative Commons metadata. Consequently,
Archive search membership, an item's uploader metadata, and mere public
downloadability do not prove authority to copy, redistribute, or train on
rulebook text.

## Safe role in a curator

Internet Archive may be used as a discovery lead, a record for its own
metadata, or a source for material independently verified as public-domain or
publisher-authorized under a suitable license. Do not bulk-download or retain
TTRPG texts from search results. Before any text ingestion, require a primary
publisher/SRD license source, an allowed license/scope decision, and an
explicit collection policy; treat missing or conflicting rights metadata as a
rejection or a human-review proposal.

Useful stored fields for a candidate are the Archive identifier and URL,
search query, retrieval time, `licenseurl`, `rights`, media type, uploader
provenance, and the separate primary-source verification record. This allows
the project to remain a helpful, provenance-first index without endorsing a
possibly unauthorized upload.

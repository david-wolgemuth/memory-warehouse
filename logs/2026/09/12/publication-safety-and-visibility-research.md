---
date: 2026-09-12
source: user-requested research; FTC, CISA, and EFF guidance
visibility: public
---


# Publication safety: what agents should keep out of public-ready records

Historical note: the visibility terminology described below was superseded on
2026-09-30. Current policy uses only `public` and `private`, with an omitted
field treated as private. See [current publication policy](../../../../cards/private-source-public-projection-security-model.md).

## Result

The useful default is simple: if unsure, omit `visibility`; never write
`visibility: private`; and use `visibility: public` liberally for records that
would be safe as a high-level blog post. `visibility: restricted` is reserved
for material that needs a later explicit sharing review.

This does not mean “publish everything.” Public content should be written on
the assumption that it can be copied, indexed, screenshot, and read years later
by a much broader audience than intended. The FTC specifically cautions that
online posts can affect privacy, reputation, and safety now and in the future,
and that deletion does not reliably remove copies:
<https://consumer.ftc.gov/articles/heads-up>.

## Keep out of public-eligible records

The following are practical hard exclusions for public-ready Warehouse records.
They should usually not be written into Warehouse at all when a durable,
non-sensitive summary can serve the same purpose.

- Credentials and recovery material: passwords, API keys, access tokens,
  private keys, recovery codes, session cookies, password-reset answers, and
  account identifiers that could assist account recovery or impersonation.
- Identity and financial data: government identifiers, bank or payment details,
  tax records, credit data, insurance identifiers, scans of identity documents,
  and combinations of name, birth date, address, phone number, or place of
  birth that enable identity theft or security-question guessing.
- Physical-safety data: exact home or work addresses, live or predictable
  location, travel plans, daily routines, floor plans, access methods, vehicle
  details, and device/location metadata that would help someone find a person
  or an unattended home.
- Health and intimate information: medical, mental-health, reproductive,
  genetic, addiction, sexual, or therapy details, unless the person concerned
  has made a deliberate decision to publish a high-level account themselves.
- Other people's private context: names, contact information, photos, messages,
  family details, work details, or identifying narratives about people who have
  not consented; apply extra care to children and vulnerable people.
- Non-public work and security information: employer/client confidential data,
  source material under an obligation of confidence, internal incidents,
  undisclosed vulnerabilities, topology, access procedures, or operational
  details that could make systems or people easier to target.
- Raw personal archives: private journals, intimate relationship conflicts,
  screenshots/transcripts of private conversations, and unverified accusations.
  Preserve only the durable lesson, and remove identifying detail.

CISA specifically recommends limiting public personal details such as address,
location, birthdays, travel, family, workplace, and access-relevant details;
it notes that combinations of ordinary facts can enable targeting or identity
theft. [CISA online-privacy guidance](https://www.cisa.gov/sites/default/files/publications/Online-Privacy-Tip-Sheet-122019-508.pdf)
and its [personal-security guide](https://www.cisa.gov/sites/default/files/2024-06/personal-security-considerations-action-guide-critical-infrastructure-workers_06-07-2024_508.pdf)
support these exclusions. The FTC likewise warns against publishing information
that can answer security questions or enable identity theft. [FTC guidance](https://consumer.ftc.gov/articles/protect-your-personal-information-hackers-and-scammers)

## Contextual, not automatic, exclusions

Personal opinions, professional lessons, project decisions, and high-level
accounts of mistakes can all be reasonable public blog material. They should
not be withheld merely because a future employer, government, former partner,
or stranger might disagree with them.

The agent's job is to avoid publishing the identifying details, confidential
context, or private third-party material that turns a useful public account
into an unnecessary personal or security risk. When a record contains a real
tradeoff, preserve the general principle publicly and retain any sensitive
context only when it is needed and deliberately reviewed.

EFF's blogging guidance makes a similar distinction for work-related writing:
avoid details that identify people or an employer when retaliation or privacy
risk is material, while still allowing meaningful expression.
<https://www.eff.org/wp/blog-safely>

## Operational change

`AGENTS.md` (unavailable in this public edition) now uses the simple default above. Existing `visibility: private`
annotations predate this clarification and should be reconsidered individually,
not mechanically rewritten, because some may properly become `public`, some
may need `restricted`, and some should simply omit the field.

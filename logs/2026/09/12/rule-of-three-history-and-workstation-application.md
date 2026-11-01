---
visibility: public
---

# Rule of three: history and workstation application

User direction (2026-09-12): adopt a rule of three for workstation setup: do
not introduce a general framework, shim layer, or extra package ecosystem for a
single special case. Reconsider it when three genuine recurring cases reveal a
stable shared need.

Research: the software-design heuristic is usually phrased “three strikes, then
you refactor.” Martin Fowler popularized it in *Refactoring* and attributes the
guideline to Don Roberts: first do the thing, tolerate the second similar
occurrence, and refactor on the third. A historical investigation traces a
related “3-system rule” through reuse-pattern work from the late 1980s and
1990s, but concludes that three is a useful heuristic, not a magic inflection
point. The philosophy is to gain enough concrete examples to choose a sound
abstraction, avoiding premature generalization or a wrong abstraction.

Application: retain direct Apt/Homebrew lists plus npm and uv inventories.
Do not add a Go tool list just to acquire Mike Farah yq; Go becomes a justified
third cross-platform source if several desired Go CLIs accumulate. Likewise,
do not add a custom binary-fetch framework or command shims for one exception.

Sources consulted 2026-09-12:

- Martin Fowler, “The Practical Test Pyramid” (Rule of Three; “use before
  reuse”): https://martinfowler.com/articles/practical-test-pyramid.html
- Go/Thoughtworks sample chapter of *Refactoring* (refactoring context):
  https://www.thoughtworks.com/content/dam/thoughtworks/documents/books/bk_Refactoring2-free-chapter_en.pdf
- Eoin Noble, historical research and Roberts attribution:
  https://eoinnoble.com/posts/origins-of-the-rule-of-three/
- Fowler/Roberts attribution summary:
  https://en.wikipedia.org/wiki/Rule_of_three_(computer_programming)

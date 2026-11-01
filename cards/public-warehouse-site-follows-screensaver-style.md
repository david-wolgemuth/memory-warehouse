---
tags:
- warehouse
- public-website
- visual-style
- screensaver
ledger:
- ../logs/2026/10/09/public-warehouse-html-site-screensaver-style.md
- ../logs/2026/10/09/public-warehouse-desktop-six-panel-layout.md
- ../logs/2026/10/09/terminal-screensaver-six-panel-correction.md
- ../logs/2026/10/09/public-warehouse-static-html-rendering-direction.md
- ../logs/2026/10/09/warehouse-tmux-cli-screensaver-and-html-output.md
- ../logs/2026/10/09/warehouse-tmux-pane-textual-tui.md
related:
- ./warehouse-screensaver-is-a-read-only-terminal-view.md
- ./private-source-public-projection-security-model.md
confidence: high
created: 2026-10-10 02:13:40+00:00
visibility: public
---


# Public Warehouse site's intended style follows the screensaver

David directed the public HTML version of Warehouse to follow the terminal
screensaver's visual style. This is [his direct design
direction](../logs/2026/10/09/public-warehouse-html-site-screensaver-style.md),
given after seeing the then-current screensaver still (unavailable in this public edition).

David [clarified](../logs/2026/10/09/terminal-screensaver-six-panel-correction.md)
that the 3×2 desktop arrangement of roughly phone-sized portrait displays,
each changing every 12 seconds, applied to the terminal screensaver at that
stage. He later [changed its architecture](../logs/2026/10/09/warehouse-tmux-cli-screensaver-and-html-output.md)
to independent tmux panes: index, compact cards, and a log stream. He compared
that composition to iframes and asked for `--format=HTML` on the same content
commands. The future site should follow the finished look. He [prefers static HTML pages](../logs/2026/10/09/public-warehouse-static-html-rendering-direction.md)
with minimal JavaScript, while allowing small server-rendered HTML updates or
iframes where useful. Share rendering components with the terminal when
feasible. The current CLI renders each terminal pane with Textual and standalone
static HTML with Pandoc, using the same visibility and selection rules.

## Boundaries

The preview remains a design reference. This does not authorize publication of
Warehouse source records; use the separate public projection review.

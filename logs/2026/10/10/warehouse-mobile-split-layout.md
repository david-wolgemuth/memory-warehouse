---
tags:
- warehouse
- screensaver
- tmux
- mobile
- index
- cards
- logs
visibility: public
---

> Some links or assets are omitted from this public edition. References to omitted files and commands using them apply to the private source.

# Mobile screensaver keeps tmux splits with cards as the main view

## User correction

After seeing the first full-width mobile feed, David clarified that mobile
should still use tmux splits. He suggested a horizontal, cycling index bar at
the top and cards as the main content. Logs could appear at the bottom or as
a hidden list, and should no longer be part of the main rotation. He also
asked whether the launcher calls tmux and saves its configuration. The
launcher creates and configures windows and panes at runtime from
`scripts/screensaver` (unavailable in this public edition); it does not write a
separate tmux configuration file.

## Current layout

At the observed 56×50 mobile window size, the launcher creates two vertical
tmux panes: a 56×4 index bar and a 56×45 card pane, with the tmux border
between them. The index bar is an independent `print.py nav --format=TUI`
view. It shows public or all scope, selected card and log counts, the active
card, and the next card. It refreshes every two seconds and follows the card
pane's selection. The card pane runs `print.py feed --cards-only --format=TUI`;
it rotates only cards at the configured interval, 12 seconds by default.

The card pane's `l` key opens a scrollable list of eligible logs in place.
`i` opens the full index, including the weekly activity chart. These overlays
pause card rotation while open. No log body is inserted into the card cycle.
Public mode still requires explicit `visibility: public`; `--all` must be
chosen to include private records. On very short terminals, the launcher
keeps a single card pane so Textual has room to render.

## Verification

A detached 56×50 tmux window showed the independent 56×4 and 56×45 panes.
Its index bar followed a manual card change after the two-second refresh.
Pressing `l` showed a public-only log title list while the card remained the
main pane. Ten focused tests passed, including mobile card and index stills
from a fixture with public and private cards and logs. Python compilation,
Bash syntax, and staged whitespace checks passed. An earlier attached phone
session was closed to release the user after a separate quit issue was
reported. David restarted the phone screensaver, and the new two-pane layout
appeared in its attached session. The desktop session retained its four-pane
layout.

The phone keyboard exposed a second layout problem: after launching at a
shorter client height, tmux distributed newly available rows to both panes,
growing the index bar to 17 rows in a 50-row window. The launcher now installs
a window-local `window-resized` hook that resizes the index pane back to four
rows after the tmux window changes size. The hook was applied to the already
attached phone window, restoring 56×4 index and 56×45 card panes. A detached
test resized a 56-column window from 23 to 50 rows; the index remained four
rows at both sizes while the card took 18 and then 45 rows.

The index bar still (unavailable in this public edition) and
card pane still (unavailable in this public edition) were generated from the
two actual TUI commands at the live pane dimensions:

> This example refers to files not included in this public edition.

```sh
./scripts/print.py nav --format=TUI --filter-index=screensaver \
  --screenshot logs/2026/10/10/warehouse-mobile-index-bar-preview.svg \
  --screenshot-size 56x4
./scripts/print.py feed --cards-only --format=TUI --filter-index=screensaver \
  --start cards/warehouse-screensaver-is-a-read-only-terminal-view.md \
  --screenshot logs/2026/10/10/warehouse-mobile-card-preview.svg \
  --screenshot-size 56x45
```

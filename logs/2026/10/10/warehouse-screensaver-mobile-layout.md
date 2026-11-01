---
tags:
- warehouse
- screensaver
- tmux
- mobile
- textual
- responsive-layout
visibility: public
---


# Screensaver uses a full-width feed on narrow terminals

## User direction and observed failure

David showed the `screensaver` entry point on a phone and said it was
scrunched and should support mobile. The attached mobile tmux client measured
56×55 cells. Its existing four-pane screensaver window measured 56×50 cells;
the panes were only 1, 4, 4, and 49 columns wide. The index and card panes
were unusable, leaving the log pane as the only readable region. This was a
layout problem, not a Markdown rendering failure.

## Change

`scripts/screensaver` (unavailable in this public edition) now chooses a layout
from the current client width. At 160 columns or more it keeps the four-pane
desktop window. Below that it launches one full-width Textual feed in one tmux
pane. `--layout mobile` and `--layout desktop` override automatic selection.
The mobile feed alternates eligible cards and logs every 12 seconds by default
and uses the same public visibility gate, `--all`, index filter, and starting
record as the desktop views. Its controls are shown at the bottom: `n`/`p`
move through records, `i` toggles a scrollable index with the weekly activity
chart, `c`/`l` jump to a card or log, space pauses, and PgUp/PgDn scroll.
Rotation pauses while the index is open. The narrow view uses a short type
label and record name in the header so Markdown keeps the usable width.

`print.py` (unavailable in this public edition) (unavailable in this public edition) accepts `feed --format=TUI` for the
mobile view. The feed interleaves the existing public-filtered card and log
selectors; it does not create another source inventory. The desktop tmux
layout and `--format=HTML` commands remain available. The same
`watch-scripts` (unavailable in this public edition) wrapper restarts the
mobile view when script files change.

## Verification and live session

A detached 56×50 tmux test window selected the mobile layout automatically
and contained one 56-column pane. The card body wrapped across the full
width. Sending `l` showed a Markdown-rendered log, and `i` showed the index
with selected entries and the eight-week activity chart; `i` returned to the
log. Nine focused screensaver tests passed, including a mobile SVG still
started on a public log beside a private log in the fixture. The attached
phone tmux session was then switched to the new one-pane public feed. Its
captured status read `public`, and its Markdown card occupied the full
56-column pane. The desktop 240-column session was left on its four-pane
layout.

The mobile still (unavailable in this public edition) is generated
by the same Textual feed at 56×50 cells:

> This example refers to files not included in this public edition.

```sh
./scripts/print.py feed --format=TUI --filter-index=screensaver \
  --start cards/warehouse-screensaver-is-a-read-only-terminal-view.md \
  --screenshot logs/2026/10/10/warehouse-mobile-screensaver-preview.svg \
  --screenshot-size 56x50
```

---
tags:
- warehouse
- screensaver
- tmux
- textual
- tui
- markdown
visibility: public
---


# Textual Markdown returns inside independent tmux panes

## User direction

After reviewing the CLI-rendered tmux layout, David said the earlier Textual
TUI rendered content better. He asked for `--format=TUI` on the same content
commands, with each cell rendered like the earlier view while remaining in its
own tmux region. This refines the earlier tmux direction: tmux owns the layout,
and each pane owns one small TUI renderer. The requested `--format=HTML`
continues to emit static pages from the same card, log, and index selectors.

## Implementation

`print.py` (unavailable in this public edition) (unavailable in this public edition) accepts `--format=TUI` (case
insensitive). `warehouse_tui.py` (unavailable in this public edition) (unavailable in this public edition)
implements a separate Textual app for each command. The card pane uses
Textual's Markdown widget, with a readable wrapped body, title bar, status,
keyboard controls, and scrolling. The log pane appends Rich-rendered Markdown
to a scrollable Textual log. The index keeps the live selected-record lists and
colored eight-week activity chart, updating in place. Both card panes advance
every 12 seconds by default; the log appends on the same interval. Each view
rechecks selected paths and enforces the public visibility gate when files
change. `--all` includes private records only when explicitly requested.

`screensaver` (unavailable in this public edition) still creates one tmux window
with a left index, two stacked compact cards, and a right log stream. Each pane
runs its own `print.py --format=TUI` command through
`watch-scripts` (unavailable in this public edition), which restarts that pane
on script edits. The launcher now creates all splits before starting the TUI
processes, so Textual measures each final pane width and wraps Markdown there.
The old plain terminal format remains available for command-line use;
`--format=HTML` still produces standalone static HTML through Pandoc.

## Evidence and still

The detached 240×62 tmux test window started all four views independently:
index 52×61, cards 71×30 each, and log stream 115×61. Captures showed both
cards wrapped within their panes, public-only index counts and colored weekly
bars, and a Markdown-rendered log stream. Focused tests passed, including a
TUI SVG still generated from a fixture with one public and one private card;
only the public card appeared. Python compile and `git diff --check` passed.
The attached desktop tmux session was reloaded in public mode using
`scripts/screensaver public`. Its four live panes were captured at the same
dimensions, and the index reported public scope. The Markdown cards wrapped
within their panes.

The implementation uses Textual 8.2.8. Inspection of the installed Textual and
Rich sources confirmed `Markdown(open_links=False)` and Rich Markdown's
`hyperlinks=False` option for nonopening links; this is version-specific
behavior. No Textual source checkout was present under
(local source omitted) during this work.

The public card still (unavailable in this public edition) is generated
by the actual TUI view, at the live card-pane dimensions:

> This example refers to files not included in this public edition.

```sh
./scripts/print.py card --format=TUI --filter-index=screensaver \
  --start cards/warehouse-screensaver-is-a-read-only-terminal-view.md \
  --screenshot logs/2026/10/09/warehouse-tmux-textual-card-preview.svg \
  --screenshot-size 71x30
```

Textual's SVG screenshot records a single pane. The tmux layout itself remains
the four-pane composition shown by the live desktop session.

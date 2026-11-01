---
tags:
- warehouse
- terminal
- visibility
- retrieval
ledger:
- ../logs/2026/10/09/warehouse-terminal-screensaver.md
- ../logs/2026/10/09/terminal-screensaver-six-panel-correction.md
- ../logs/2026/10/09/warehouse-tmux-cli-screensaver-and-html-output.md
- ../logs/2026/10/09/warehouse-screensaver-flicker-and-script-reload.md
- ../logs/2026/10/09/warehouse-screensaver-color-log-activity-chart.md
- ../logs/2026/10/09/warehouse-tmux-pane-textual-tui.md
- ../logs/2026/10/10/warehouse-screensaver-mobile-layout.md
- ../logs/2026/10/10/warehouse-mobile-split-layout.md
- ../logs/2026/10/10/warehouse-screensaver-quit-closes-tmux-window.md
related:
- ./private-source-public-projection-security-model.md
confidence: high
created: 2026-10-10 01:57:27+00:00
visibility: public
---


# Warehouse screensaver is a read-only terminal view

The Warehouse screensaver cycles through Markdown logs and cards in tmux panes.
Its default and `public` modes select records only when their
frontmatter explicitly says `visibility: public`; `--all` includes private
records too. [David requested these modes](../logs/2026/10/09/warehouse-terminal-screensaver.md#user-direction).

The viewer reads source files live and never changes them. It is a local display
tool, not the reviewed public projection. Its selection policy and controls are
documented in the screensaver index (unavailable in this public edition).

The [desktop tmux layout](../logs/2026/10/09/warehouse-tmux-pane-textual-tui.md)
has a live index at left, two compact cards in the middle, and a log stream at
right. Each pane runs `print.py --format=TUI` as an independent Textual view.
On [narrow terminals](../logs/2026/10/10/warehouse-mobile-split-layout.md),
the launcher splits the tmux window into a short horizontal index bar and a
full-width card pane. Cards rotate every 12 seconds. Logs stay in a hidden
list opened with `l`; `i` opens the full index and weekly log chart. A wrapper
restarts each view when any file in `scripts/` changes. The earlier single-app
Textual layout
and the interim Glow pane rendering remain historical. The same card, log,
and index selectors output static HTML with `--format=HTML`. Pressing `q` or
Ctrl+q closes the screensaver's tmux window and stops its pane watchers.

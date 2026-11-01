---
tags:
- warehouse
- terminal
- screensaver
- desktop
- layout
- correction
visibility: public
---

> Some links or assets are omitted from this public edition. References to omitted files and commands using them apply to the private source.

# Six portrait panels belong in the terminal screensaver

David clarified that his [3×2 desktop layout suggestion](./public-warehouse-desktop-six-panel-layout.md)
applies to the terminal interface already running in tmux. The earlier log
interpreted it as a future web-only suggestion; that scope was wrong. On a
full desktop terminal, he wants six roughly phone-shaped Markdown displays in
three columns and two rows, each changing every 12 seconds. He authorized
inspecting and reloading the existing tmux session after the change. He said a
file-change restart loop may live in the tmux shell instead of the script if
useful; it is optional.

The existing pane was observed at 240×61 cells. The updated Textual app uses
six portrait panels on a terminal of at least 120×59 cells and the original
single-page view on smaller terminals. One panel updates every two seconds in
round-robin order, so each panel gets its own turn every 12 seconds. A long
record scrolls one page on its turn before that panel moves to another record.
The user can select a panel with `1`–`6` and use `n` or `p` on it.

The implementation remains a local, read-only view with the same explicit
public visibility filter. The current six-panel still (unavailable in this public edition)
was generated from the terminal app at 240×61 cells.

Verification: the focused visibility, single-page paging, and independent
six-panel rotation tests passed. The still was rendered by the app, and the
existing 240×61 tmux pane was restarted with `scripts/screensaver public`;
its captured screen showed all six panels. The pane runs the command directly,
without a file watcher.

---
tags:
- warehouse
- screensaver
- tmux
- textual
- quit
- watcher
visibility: public
---

> Some links or assets are omitted from this public edition. References to omitted files and commands using them apply to the private source.

# Quit closes the screensaver window and its watcher

David showed the mobile screensaver after pressing a quit key and reported
that he could not fully leave the session. Textual displayed a confirmation
to press Ctrl+q to quit the app. The pane command was managed by
`watch-scripts` (unavailable in this public edition), which starts a new child
after any app exit, so quitting only Textual returned to the same view.

The launcher now sets `WAREHOUSE_SCREENSAVER=1` only on commands it starts.
Inside that environment, `q` and Ctrl+q in
`warehouse_tui.py` (unavailable in this public edition) (unavailable in this public edition) use the pane's
`TMUX_PANE` identifier to close its entire tmux window. The watcher dies with
the pane. A standalone `print.py --format=TUI` call outside the launcher
exits just its app. Textual's confirmation is bypassed by explicit high
priority bindings for these keys.

David's attached phone session was closed to release him immediately. In a
fresh detached tmux session, `q` removed the screensaver window and left the
shell window; a separate fresh run did the same with Ctrl+q. Neither view
reappeared after the watcher interval. On a dedicated screensaver session
with no other windows, closing the window ends the tmux session and returns
the client to its shell.

While testing, a detached 56-column session unexpectedly inherited a
240-column size from a different attached client when the launcher read
`client_width`. The launcher now reads the current tmux window width for
automatic layout selection. The attached phone session had already used a
separate 56-column window; the new measurement avoids another client's width
changing the layout decision in detached or mixed-client runs. A newly created
window in a detached test session can still inherit the size of an attached
client elsewhere because tmux's `window-size` policy is `latest`.

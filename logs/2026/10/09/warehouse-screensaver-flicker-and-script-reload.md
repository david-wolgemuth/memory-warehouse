---
tags:
- warehouse
- screensaver
- tmux
- reload
- correction
visibility: public
---

> Some links or assets are omitted from this public edition. References to omitted files and commands using them apply to the private source.

# Keep the index visible and restart pane commands on script edits

David observed the left index blinking in the running tmux screensaver. He
also directed that each script command run through a wrapper which watches
for changes to any file in `scripts/` and reloads automatically.

Direct code inspection found that `every` (unavailable in this public edition) cleared
the pane before starting each command. The index repeats every two seconds,
so the pane showed a blank interval while `print.py` (unavailable in this public edition) started and selected
records. `every` now prepares each index or card frame in a temporary file,
then moves the cursor home, writes the completed frame, and clears only the
unused remainder. The log stream still appends directly to tmux scrollback.

The launcher now puts every pane command under
`watch-scripts` (unavailable in this public edition). The wrapper checks the
script directory four times a second for file additions, deletions, and
edits. On a change it stops the current command process group and re-executes
itself, so changes to `watch-scripts`, `every`, or `print.py` (unavailable in this public edition) take effect. It
ignores Python bytecode caches. The wrapper keeps using the launcher options
and pane layout already chosen; those require relaunching the window to
change.

Focused tests verified that a slow frame produces no early clear command,
and that a watched file edit restarts a running child. The previous public
selection and HTML tests also passed.

The existing desktop tmux session was reloaded with the new four-pane layout.
All four pane processes ran `watch-scripts`. Eight index captures across
multiple refreshes retained the `WAREHOUSE / INDEX` heading. Touching
`scripts/every` changed its modification time and all four watcher children
were replaced with new process IDs; the index remained visible afterward.

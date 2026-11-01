---
tags:
- warehouse
- screensaver
- tmux
- chart
- color
- html
visibility: public
---


# Color log activity chart in the screensaver index

David shared a photo of the running desktop tmux screensaver and asked whether
a chart or graph could be rendered there. He then asked to get some color in.
The left index is the natural space for a compact chart without displacing the
card panes or the streaming log.

`print.py` (unavailable in this public edition) (unavailable in this public edition) now counts selected dated logs by
Monday-starting week. It shows the latest eight weeks as horizontal terminal
bars at the bottom of the left index, with cool blue through green to warm
orange colors. The cards and logs headings and active selections get distinct
cool and warm accents. The active tmux pane border is warm orange. The same
weekly counts and palette appear in the static HTML index produced by
`print.py index --format=HTML`; no JavaScript is needed.

The chart receives the already-filtered log paths. Public mode therefore
counts only explicitly public logs; `--all` can include private logs. A named
index filter narrows the chart in the same way it narrows the lists. The chart
is a computed view of Markdown files and stores no generated inventory.

Focused tests verified the visibility boundary and the HTML chart. The live
index displayed the bars within its 52×61 pane. The eight displayed weeks
are anchored to the latest selected dated log, so a narrow historical index
still shows a meaningful period.

The desktop tmux window was reloaded in public mode. A tmux capture of the
index contained the colored weekly bars, including the warm orange current
week, and `pane-active-border-style` reported `fg=#f2b66d`.

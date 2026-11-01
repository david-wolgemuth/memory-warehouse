---
tags:
- warehouse
- screensaver
- tmux
- markdown
- html
- visibility
- correction
visibility: public
---

> Some links or assets are omitted from this public edition. References to omitted files and commands using them apply to the private source.

# Tmux panes and CLI renderers replace the Textual screensaver

David stopped the Textual-based redesign and directed that the terminal
screensaver be composed from independent tmux views running command-line
tools. His example command shape was
`every --seconds=n -- ./scripts/print.py card --filter-index=index-name --offset=o`.
He confirmed tmux panes plus a CLI Markdown renderer, and compared independent
tmux regions to web iframes: each region owns its content and refresh cycle,
while a containing layout arranges them. He then asked for `--format=HTML` at
the end of the same card, log, and index commands so they can emit static HTML.
This supersedes the [Textual six-panel implementation](./terminal-screensaver-six-panel-correction.md)
as the active terminal design; that earlier log remains historical evidence.

The launcher (unavailable in this public edition) creates one tmux window with
four panes at 240×61 cells: a 52×61 live index at left, two 71×30 compact
card panes stacked in the middle, and a 115×61 log stream at right. The index
highlights the two displayed cards and the latest log. The
`every` wrapper (unavailable in this public edition) reruns each independent command,
passing a zero-based tick. The two card panes use offsets 0 and 1 with a
stride of 2; each changes every 12 seconds. Logs append every 12 seconds and
remain in tmux scrollback. Repeating `print.py` (unavailable in this public edition) means edits to its script and
source records appear on the next cycle. Layout changes require relaunching.

`print.py` (unavailable in this public edition) (unavailable in this public edition) is a selector and CLI adapter. It
keeps the prior fail-closed public frontmatter rule, strips frontmatter, and
uses Glow to render Markdown in terminal panes. Pandoc reflows hard-wrapped
prose for the available pane width; if Glow is absent, Pandoc also provides a
plain terminal fallback. `--filter-index` follows links in a named curated
index and evidence logs in its linked cards' `ledger` fields. That filter
never overrides a record's own public visibility. The left index is a computed
view of eligible records, so it does not expose raw private index text in
public mode.

With `--format=HTML`, the same command and record selection produce a
standalone static HTML page. Pandoc supplies HTML markup; the command adds the
screensaver palette and no JavaScript. Raw HTML in Markdown is escaped, and
local `.md` links become `.html` links. This is a local output option, not a
public site deployment. Publication still requires [review of the exact
projection](../../../../cards/private-source-public-projection-security-model.md).

## Verification and dependency

- Focused tests passed for fail-closed visibility, index and ledger filtering,
  successive `every` ticks, and `--format=HTML` output and escaping.
- A detached 240×61 tmux session displayed all four panes; capture confirmed
  a public index, rendered cards, and a growing log stream. The SVG still (unavailable in this public edition)
  and text capture (unavailable in this public edition) preserve one
  public-mode snapshot filtered through `indexes/screensaver.md` (unavailable in this public edition).
- Glow was obtained from Debian's `glow` package version `2.0.0-1+b5` and
  installed in David's local bin. The downloaded package SHA-256 matched the
  value in local Debian package metadata:
  `3e36a1b585d953429b429ec53a51b75ff1e182b7a76f547d5c60014899d08218`.
  The verified CLI accepts stdin, `--style`, and `--width`; this behavior is
  also visible in [Glow's source](https://github.com/charmbracelet/glow/blob/main/main.go).

---
tags:
- warehouse
- terminal
- screensaver
- markdown
- visibility
- textual
visibility: public
---


# Warehouse terminal screensaver

## User direction

On 2026-10-09, David asked for a command inside Warehouse that can be run on a
connected screen or through tmux and continuously cycle through logs and notes
as rendered Markdown. He suggested a Python curses-style app or an existing
open-source Markdown rendering engine. He specified a `public` mode that shows
only public material and a `--all` mode that shows both public and private
material, and later asked for a still shot to preview the screen.

## Implementation

- Added executable scripts/screensaver (unavailable in this public edition), a Python
  script with inline `uv` dependencies pinned to Textual 8.2.8 and PyYAML
  6.0.3. Textual's
  built-in Markdown widget renders headings, lists, links, tables, and code in
  the terminal. Its event loop supplies key handling, scrolling, and a timer.
- Default mode and positional `public` use a fail-closed frontmatter filter:
  only one direct, scalar `visibility: public` field selects a record. Missing,
  malformed, duplicated, or inherited visibility fields do not select it.
  `--all` includes every readable Markdown log and card, including unlabeled
  files. Symlinks are excluded. Frontmatter is removed from rendered pages.
- The catalog is computed from `logs/**/*.md` and `cards/*.md`, with newest log
  paths first and one card after every four logs. Each record is reread before
  display, so a changed public label is rechecked. The catalog is refreshed at
  wraparound or with `r`. No Warehouse source file is modified by the viewer.
- The timer advances one screenful at a time within long notes before changing
  records. `n`/`p` change records, `PgDn`/`PgUp` and arrows scroll, `space`
  pauses, and `q` exits. Link clicks are disabled: a public record may mention
  a private file, but the viewer must not navigate to that target.
- `--interval` changes seconds per screen; `--list` audits selection; `--root`
  supports another checkout or test fixture; `--start` chooses a selected
  first record; `--screenshot FILE.svg` captures that screen. The screen is a
  local reading view, not a substitute for review before publishing a public
  repository.

## Preview

The public-mode still (unavailable in this public edition) is an actual
Textual screenshot at 104 by 32 cells, rendering an explicitly public log. It
was generated from source with:

> This example refers to files not included in this public edition.

```sh
env -u NO_COLOR TERM=xterm-256color COLORTERM=truecolor \
  scripts/screensaver public \
  --start logs/2026/10/02/aws-managed-small-model-training-and-serving.md \
  --screenshot logs/2026/10/09/warehouse-screensaver-preview.svg
```

`NO_COLOR` was unset only for the color preview. The viewer itself honors the
terminal's color setting.

## Verification and limits

- Direct selection check before this log and card were added: 94 public
  records, 532 records with `--all`.
- `unittest` fixtures cover omitted/private labels, malformed YAML, duplicate
  visibility, YAML-merged visibility, symlinks, page scrolling, pause and
  navigation, and a record changing from public to private after startup. Run
  them with `uv run --with textual==8.2.8 --with PyYAML==6.0.3 python -m
  unittest discover -s tests -v` (or set `UV_OFFLINE=1` after dependencies
  have been cached).
- A pseudo-terminal run showed the rendered Markdown and controls; pressing
  `q` restored the terminal and exited with status zero. In this Python 3.13
  sandbox, `asyncio.run()` did not promptly join a thread after Markdown
  rendering, so the runner owns and closes Textual's Markdown parsing executor
  explicitly. The same command then exited promptly.
- This version displays Markdown source from logs and cards. Linked raster
  assets are not shown as terminal images, and it does not visit indexes,
  skills, or non-Markdown log attachments. Public selection relies on the
  record's visibility label; the separate public-projection review remains
  necessary before sharing content outside the private source repository.

## Sources

- [Textual Markdown widget](https://textual.textualize.io/widgets/markdown/) — built-in terminal Markdown rendering.
- [Textual timers](https://textual.textualize.io/api/timer/) — periodic callbacks.
- [Textual testing guide](https://textual.textualize.io/guide/testing/) — headless pilot and screenshot workflow.
- [Warehouse visibility policy](../../../../cards/private-source-public-projection-security-model.md).

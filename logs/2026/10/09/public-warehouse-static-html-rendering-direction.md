---
tags: [warehouse, public-website, html, screensaver, rendering]
visibility: public
---

# Future public Warehouse website should use static HTML

David prefers reusing the same rendering HTML components across the terminal
screensaver and future public web interface if feasible. He clarified that the
web interface should primarily consist of static HTML pages, with minimal
JavaScript. Small JavaScript updates that fetch server-rendered component HTML
are acceptable, as is an iframe approach if it reduces scripting. A custom
renderer is acceptable if it serves this goal. This is design direction for a
future public site, not authorization to publish Warehouse content now.

Textual's official [web application description](https://textual.textualize.io/blog/2024/09/08/towards-textual-web-applications/)
says its browser route sends terminal escape sequences to xterm.js. It can
reuse the Textual widget tree, but that route does not produce native static
HTML pages. The terminal app itself renders Markdown with Textual widgets.
The future web project can share source Markdown, selection rules, layout
decisions, and visual tokens with it, then emit reviewed static HTML. Any
public copy still requires the [separate projection review](../../../../cards/private-source-public-projection-security-model.md).

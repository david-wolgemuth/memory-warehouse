# Memory Warehouse

Memory Warehouse is the name for a public-facing collection of notes and
cards selected from the private Warehouse memory system.

## Build the site

Install Python 3, Pandoc, and the Python dependency, then build and preview:

```sh
python -m pip install -r requirements.txt
python scripts/build_site.py
python -m http.server --directory build 8000
```

The build selects Markdown in `cards/` and `logs/` explicitly marked
`visibility: public`. It produces individual static HTML pages and a
screensaver-inspired home page. `build/` is generated and ignored by Git.
The home page rotates records every 12 seconds, with pause and navigation
controls; the index and record pages also work without JavaScript.

## GitHub Pages

After creating a public GitHub repository and pushing this project, select
**Settings → Pages → Build and deployment → Source → GitHub Actions**.
The included workflow builds the Markdown and deploys the generated Pages
artifact on pushes to `main` or manual dispatch. The generated site is not
committed. No site is published until the repository and Pages are configured.

Warehouse stays private. Before each copy into this repository, review the
exact projected files, including content, names, metadata, links, and assets.
The public repository maintains its own history and never contains Warehouse's
private Git history. Reviewed site assets live in `site/assets/` and are copied
to the build. Assets referenced by synced records need separate review and
handling; the Warehouse projection sync does not copy them automatically.

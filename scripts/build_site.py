#!/usr/bin/env python3
"""Build the reviewed Memory Warehouse Markdown into a static site."""

import html
import json
import re
import shutil
import subprocess
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / 'build'


def public_body(path):
    if path.is_symlink() or any(p.is_symlink() for p in path.parents if p != ROOT and p.is_relative_to(ROOT)):
        return None
    text = path.read_text(encoding='utf-8')
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != '---':
        return None
    try:
        end = next(i for i in range(1, min(len(lines), 201)) if lines[i].strip() == '---')
        header = ''.join(lines[1:end])
        node = yaml.compose(header, Loader=yaml.SafeLoader)
        metadata = yaml.safe_load(header)
        if not isinstance(node, yaml.MappingNode) or not isinstance(metadata, dict):
            return None
        keys = [key.value for key, _ in node.value if isinstance(key, yaml.ScalarNode) and key.value == 'visibility']
        if keys != ['visibility'] or metadata.get('visibility') != 'public':
            return None
        tags = metadata.get('tags', [])
        if isinstance(tags, str):
            tags = [tags]
        if not isinstance(tags, list):
            tags = []
        return ''.join(lines[end + 1:]), [tag for tag in tags if isinstance(tag, str) and tag.strip()]
    except (StopIteration, yaml.YAMLError):
        return None


def page(title, content, prefix=''):
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} · Memory Warehouse</title><link rel="stylesheet" href="{prefix}style.css"><link rel="stylesheet" href="{prefix}tags.css"></head>
<body>{content}</body></html>\n'''


def build():
    if OUTPUT.is_symlink():
        raise ValueError('build must not be a symlink')
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    OUTPUT.mkdir()
    for asset in ('style.css', 'tags.css', 'site.js'):
        shutil.copyfile(ROOT / 'site' / asset, OUTPUT / asset)
    assets = ROOT / 'site' / 'assets'
    if assets.exists():
        if assets.is_symlink() or any(path.is_symlink() for path in assets.rglob('*')):
            raise ValueError('Site assets must not contain symlinks')
        shutil.copytree(assets, OUTPUT / 'assets')
    about = (ROOT / 'site' / 'about.md').read_text(encoding='utf-8')
    about_html = subprocess.run(['pandoc', '--from=markdown-raw_html', '--to=html5'], input=about, text=True, capture_output=True, check=True).stdout
    (OUTPUT / 'about.html').write_text(page('About', f'<header class="record-header"><a href="index.html">← Memory Warehouse</a><span>ABOUT</span></header><main class="record about">{about_html}</main>'), encoding='utf-8')
    records = {'cards': [], 'logs': []}
    for kind in records:
        directory = ROOT / kind
        if not directory.exists():
            continue
        for path in sorted(directory.rglob('*.md'), reverse=(kind == 'logs')):
            record = public_body(path)
            if record is None:
                continue
            body, tags = record
            relative = path.relative_to(ROOT).with_suffix('.html')
            target = OUTPUT / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            heading = re.search(r'^#\s+(.+?)\s*$', body, re.M)
            title = heading.group(1) if heading else path.stem.replace('-', ' ')
            rendered = subprocess.run(['pandoc', '--from=markdown-raw_html', '--to=html5'], input=body, text=True, capture_output=True, check=True).stdout
            rendered = re.sub(r'(href="[^"#?]*?)\.md(?=[#?\"])', r'\1.html', rendered)
            if tags:
                pills = '<div class="record-tags" aria-label="Tags">' + ''.join(
                    f'<span class="tag">{html.escape(tag)}</span>' for tag in tags) + '</div>'
                if '</h1>' in rendered:
                    rendered = rendered.replace('</h1>', '</h1>' + pills, 1)
                else:
                    rendered = pills + rendered
            prefix = '../' * len(relative.parent.parts)
            content = f'<header class="record-header"><a href="{prefix}index.html" target="_top">← Memory Warehouse</a><span>{kind.upper()}</span></header><main class="record">{rendered}</main>'
            target.write_text(page(title, content, prefix), encoding='utf-8')
            records[kind].append({'title': title, 'url': relative.as_posix()})
    def nav(kind):
        return ''.join(f'<li><a href="{html.escape(r["url"], quote=True)}">{html.escape(r["title"])}</a></li>' for r in records[kind]) or '<li class="empty">No records yet</li>'
    def frame(kind, index=0):
        entries = records[kind]
        if not entries:
            return '<p class="empty">No public records yet.</p>'
        record = entries[index % len(entries)]
        return f'<iframe title="{kind} view {index + 1}" src="{html.escape(record["url"], quote=True)}" data-frame="{kind}" data-offset="{index}"></iframe>'
    content = f'''<header class="top"><a class="brand" href="index.html"><span class="brand-mark">✳</span> MEMORY WAREHOUSE</a><span class="top-note">A PUBLIC NOTEBOOK <span> / </span> HUMAN + MACHINE</span></header>
<div class="workspace"><aside class="panel index-panel"><div class="panel-title"><span>INDEX</span><span>01 / NAVIGATE</span></div><div class="index-body"><p class="eyebrow">A living collection</p><h1>Notes from the<br><em>memory warehouse.</em></h1><p class="intro">Ideas, observations, and connections gathered over time.</p><p><a href="about.html">About the Warehouse ↗</a></p><details open><summary>Cards <span>{len(records['cards']):02d}</span></summary><ul>{nav('cards')}</ul></details><details><summary>Logbook <span>{len(records['logs']):02d}</span></summary><ul>{nav('logs')}</ul></details></div><div class="panel-foot">BROWSE THE COLLECTION <span>↗</span></div></aside>
<section class="cards-column" aria-label="Cards"><article class="panel card-panel"><div class="panel-title"><span>CARD 01</span><span>◆ &nbsp; MEMORY</span></div>{frame('cards', 0)}</article><article class="panel card-panel second"><div class="panel-title"><span>CARD 02</span><span>◆ &nbsp; MEMORY</span></div>{frame('cards', 1)}</article></section>
<section class="panel log-panel"><div class="panel-title"><span>LOG STREAM</span><span>02 / OBSERVE</span></div><div class="log-intro"><span class="live-dot"></span> NOTES FROM THE LOGBOOK <span class="log-count">{len(records['logs']):02d} ENTRIES</span></div>{frame('logs')}</section></div>
<footer class="controls"><span><span class="live-dot"></span> <span id="rotation-status">ROTATING EVERY 12 SECONDS</span></span><div><button id="previous" type="button">← PREV</button><button id="pause" type="button">Ⅱ PAUSE</button><button id="next" type="button">NEXT →</button></div><span class="footer-note">MEMORY IS A WORK IN PROGRESS <span>✳</span></span></footer>
<script type="application/json" id="records">{json.dumps(records).replace('<', chr(92) + 'u003c')}</script><script src="site.js" defer></script>'''
    (OUTPUT / 'index.html').write_text(page('Home', content), encoding='utf-8')
    print(f"Built {len(records['cards'])} cards and {len(records['logs'])} logs into {OUTPUT}")


if __name__ == '__main__':
    build()

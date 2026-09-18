"""Structural, reader-facing and local-link checks; no external services."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
from html.parser import HTMLParser
import re

root = Path(__file__).resolve().parents[1]
errors, ids, visible = [], [], []
index = (root / 'index.html').read_text()
for part in range(7):
    path = root / f'slides/part{part}.md'
    text = path.read_text()
    if f'data-markdown="slides/part{part}.md"' not in index:
        errors.append(f'Part {part} missing from deck entry point')
    if re.search(r'<\s*/?section\b', text): errors.append(f'Nested section in {path.name}')
    if 'data-copy=' in text: errors.append(f'Duplicated prompt in {path.name}')
    for chunk in re.split(r'^\s*---\s*$', text, flags=re.M):
        if chunk.count('\nNote:\n') != 1: errors.append(f'Exactly one Note: required in {path.name}')
        found = re.search(r'\.slide: id="([^"]+)"', chunk)
        if not found: errors.append(f'Missing anchor in {path.name}')
        else: ids.append(found[1])
        visible.append(chunk.split('\nNote:\n')[0])
assert len(ids) == 52, len(ids)
assert len(set(ids)) == len(ids)
assert 'Wenxin Jiang' in visible[0]
assert 'PART 0' not in visible[0]
assert 'id="agenda"' in visible[1]
assert ids[-1] == 'questions'
for required in ('part6', 'demo-to-practice', 'deep-research', 'math-frontier', 'future-reflection', 'first-demo', 'exercise1', 'exercise2', 'exercise3'):
    assert required in ids, required
for forbidden in ['The lecturer starts import', 'Importing sources and generating a quiz are different waiting steps', 'A prepared notebook is a backup', 'Illustrative teaching dialogue', 'Scheduled return:', 'Open Canvas', 'A generated world you can navigate', 'not percentage-point changes', 'Short-term results in this setting', 'A citation is a route to evidence, not a verdict', 'Does this source support that claim?']:
    if any(forbidden in text for text in visible): errors.append(f'Reader-facing text regression: {forbidden}')
assert 'world-demo' not in ids
for anchor, seconds in [('first-demo',240), ('exercise1',600), ('exercise2',480), ('exercise3',360), ('break',600), ('future-reflection',60)]:
    page = visible[ids.index(anchor)]
    assert f'data-seconds="{seconds}"' in page, anchor

class Links(HTMLParser):
    def __init__(self): super().__init__(); self.urls = []
    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key in ('href', 'src', 'data-src', 'data-markdown') and value: self.urls.append(value)

for path in root.rglob('*'):
    if not path.is_file() or path.suffix not in ('.md', '.html'): continue
    if any(part in ('.git', 'node_modules', '_site', 'test-results', '.review') for part in path.parts): continue
    parser = Links(); text = path.read_text(); parser.feed(text)
    urls = parser.urls + re.findall(r'\]\(([^\s)]+)\)', text)
    base = root if path.parent.name == 'slides' else path.parent
    for raw in urls:
        url = urlsplit(raw)
        if url.scheme or url.netloc or not url.path: continue
        if not (base / unquote(url.path)).resolve().exists(): errors.append(f'{path.relative_to(root)} -> missing {raw}')
if errors: raise SystemExit('\n'.join(errors))
print('PASS: 52 slides across seven parts, reader-facing checks, anchors, notes, timers and local links.')

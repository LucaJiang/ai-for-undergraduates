"""Structural and local-link checks independent of browser/network services."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
from html.parser import HTMLParser
import re

root = Path(__file__).resolve().parents[1]
errors = []
count = 0
ids = []
for part in range(6):
    path = root / f"slides/part{part}.md"
    text = path.read_text()
    chunks = re.split(r"^\s*---\s*$", text, flags=re.M)
    count += len(chunks)
    if re.search(r"<\s*/?section\b", text):
        errors.append(f"Nested section in {path.name}")
    for chunk in chunks:
        if chunk.count("\nNote:\n") != 1:
            errors.append(f"Exactly one Note: required in {path.name}")
        found = re.search(r'\.slide: id="([^"]+)"', chunk)
        if not found:
            errors.append(f"Missing stable id in {path.name}")
        else:
            ids.append(found[1])
    if "data-copy=" in text:
        errors.append(f"Duplicated copy text in {path.name}")
assert count == 51, count
assert len(set(ids)) == count

class Links(HTMLParser):
    def __init__(self):
        super().__init__(); self.urls = []
    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key in ("href", "src", "data-src", "data-markdown") and value:
                self.urls.append(value)

for path in root.rglob("*"):
    if not path.is_file() or path.suffix not in (".md", ".html"):
        continue
    if any(part in (".git", "node_modules", "_site", "test-results", ".review") for part in path.parts):
        continue
    parser = Links(); text = path.read_text(); parser.feed(text)
    urls = parser.urls + re.findall(r"\]\(([^\s)]+)\)", text)
    base = root if path.parent.name == "slides" else path.parent
    for raw in urls:
        url = urlsplit(raw)
        if url.scheme or url.netloc or not url.path:
            continue
        target = (base / unquote(url.path)).resolve()
        if not target.exists():
            errors.append(f"{path.relative_to(root)} -> missing {raw}")
if errors:
    raise SystemExit("\n".join(errors))
print(f"PASS: {count} slides, unique anchors, notes, no nested sections/duplicated copy data, local links resolve.")

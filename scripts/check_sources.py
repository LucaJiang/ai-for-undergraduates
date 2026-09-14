"""Structural, reader-facing and local-link checks; no external services."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
from html.parser import HTMLParser
import re

root = Path(__file__).resolve().parents[1]
errors, ids = [], []
visible = []
for part in range(6):
    path = root / f"slides/part{part}.md"
    text = path.read_text()
    if re.search(r"<\s*/?section\b", text): errors.append(f"Nested section in {path.name}")
    if "data-copy=" in text: errors.append(f"Duplicated prompt in {path.name}")
    for chunk in re.split(r"^\s*---\s*$", text, flags=re.M):
        if chunk.count("\nNote:\n") != 1: errors.append(f"Exactly one Note: required in {path.name}")
        found = re.search(r'\.slide: id="([^"]+)"', chunk)
        if not found: errors.append(f"Missing anchor in {path.name}")
        else: ids.append(found[1])
        visible.append(chunk.split("\nNote:\n")[0])
assert len(ids) == 52, len(ids)
assert len(set(ids)) == len(ids)
assert "Wenxin Jiang" in visible[0]
assert "PART 0" not in visible[0]
assert 'id="agenda"' in visible[1]
for forbidden in ["The lecturer starts import", "Importing sources and generating a quiz are different waiting steps", "A prepared notebook is a backup", "Illustrative teaching dialogue", "Scheduled return:", "Open Canvas"]:
    if any(forbidden in text for text in visible): errors.append(f"Reader-facing text regression: {forbidden}")

class Links(HTMLParser):
    def __init__(self): super().__init__(); self.urls = []
    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key in ("href", "src", "data-src", "data-markdown") and value: self.urls.append(value)

for path in root.rglob("*"):
    if not path.is_file() or path.suffix not in (".md", ".html"): continue
    if any(part in (".git", "node_modules", "_site", "test-results", ".review") for part in path.parts): continue
    parser = Links(); text = path.read_text(); parser.feed(text)
    urls = parser.urls + re.findall(r"\]\(([^\s)]+)\)", text)
    base = root if path.parent.name == "slides" else path.parent
    for raw in urls:
        url = urlsplit(raw)
        if url.scheme or url.netloc or not url.path: continue
        if not (base / unquote(url.path)).resolve().exists(): errors.append(f"{path.relative_to(root)} -> missing {raw}")
if errors: raise SystemExit("\n".join(errors))
print("PASS: 52 slides, reader-facing checks, unique anchors, notes and local links.")

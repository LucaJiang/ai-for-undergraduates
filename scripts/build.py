"""Build a static site with the pinned Reveal runtime copied locally; no fonts."""
from pathlib import Path
import shutil

root = Path(__file__).resolve().parents[1]
reveal = root / "node_modules/reveal.js"
if not reveal.is_dir():
    raise SystemExit("Run npm install --ignore-scripts --no-audit --no-fund first.")
output = root / "_site"
if output.exists():
    shutil.rmtree(output)
output.mkdir()
for name in ("index.html", "materials.html", "css", "js", "slides", "demo-materials", "prompts", "resources", "references", "examples", "LICENSE"):
    source = root / name
    if source.is_dir():
        shutil.copytree(source, output / name)
    else:
        shutil.copy2(source, output / name)
for rel in ("dist/reveal.js", "dist/reveal.css", "plugin/markdown/markdown.js", "plugin/notes/notes.js", "LICENSE"):
    source = reveal / rel
    if not source.is_file():
        raise SystemExit(f"Pinned dependency missing required file: {rel}")
    target = output / "vendor/reveal" / rel
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)
optional = reveal / "plugin/notes/speaker-view.html"
if optional.exists():
    shutil.copy2(optional, output / "vendor/reveal/plugin/notes/speaker-view.html")
index = output / "index.html"
index.write_text(index.read_text().replace("https://cdn.jsdelivr.net/npm/reveal.js@5.2.1/", "vendor/reveal/"))
(output / ".nojekyll").touch()
print(f"Built {output} with Reveal.js 5.2.1. External videos remain click-to-load.")

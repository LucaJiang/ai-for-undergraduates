"""Add reading-page i18n to the built site; original teaching sources stay intact.

Uses only the Python standard library. Chinese Notebook source pages are also
rendered statically so an importer does not need to execute JavaScript.
"""
from html import escape
from html.parser import HTMLParser
from pathlib import Path
import json
import re


def normalize(value):
    return " ".join(value.split())


class ChineseHTML(HTMLParser):
    def __init__(self, dictionary):
        super().__init__(convert_charrefs=True)
        self.dictionary = dictionary
        self.output = []
        self.raw = False

    def handle_starttag(self, tag, attrs):
        self.output.append(self.get_starttag_text())
        if tag in ("script", "style"):
            self.raw = True

    def handle_startendtag(self, tag, attrs):
        self.output.append(self.get_starttag_text())

    def handle_endtag(self, tag):
        self.output.append(f"</{tag}>")
        if tag in ("script", "style"):
            self.raw = False

    def handle_data(self, text):
        if self.raw:
            self.output.append(text)
            return
        translated = self.dictionary.get(normalize(text))
        value = text.replace(text.strip(), translated) if translated and text.strip() else text
        self.output.append(escape(value, quote=False))

    def handle_decl(self, decl):
        self.output.append(f"<!{decl}>")

    def handle_comment(self, text):
        self.output.append(f"<!--{text}-->")


def localize(site):
    site = Path(site)
    deck_dictionary = (site / "js/translations-zh.js").read_text(encoding="utf-8")
    deck = json.loads(deck_dictionary[deck_dictionary.index("({") + 1:deck_dictionary.rindex("});") + 1])
    additional = json.loads((site / "js/materials-zh.json").read_text(encoding="utf-8"))
    dictionary = {normalize(k): v for k, v in {**deck, **additional}.items()}
    (site / "js/materials-zh.js").write_text(
        "/* Generated from materials-zh.json. No external translation service. */\n"
        "window.WorkshopChinese = Object.freeze(Object.assign({}, window.WorkshopChinese, "
        + json.dumps(additional, ensure_ascii=False) + "));\n", encoding="utf-8")
    index = (site / "index.html").read_text(encoding="utf-8")
    controls = index[index.index('<div class="deck-preferences"'):index.index('<noscript>')]
    pages = [p for p in sorted(site.rglob("*.html")) if "vendor" not in p.parts and '.zh.' not in p.name]
    count = 0

    def enhance(text, prefix):
        assets = (f'<script src="{prefix}js/preferences.js"></script>'
                  f'<link rel="stylesheet" href="{prefix}css/preferences.css">'
                  f'<link rel="stylesheet" href="{prefix}css/materials.css">')
        text = text.replace('</head>', assets + '</head>', 1)
        text = text.replace('<body class="source-page">', '<body class="source-page">' + controls, 1)
        # Stable select values must not change when visible labels are translated.
        for mode in ('Explain', 'Practice', 'Any'):
            text = text.replace(f'<option>{mode}</option>', f'<option value="{mode}">{mode}</option>')
        # Give wide teaching tables their own scroll container on small screens.
        text = re.sub(r'(<table\b[\s\S]*?</table>)', r'<div class="table-scroll" tabindex="0" role="region" aria-label="Scrollable table">\1</div>', text)

        def source_link(match):
            href = match.group(1)
            chinese = None
            if 'demo-materials/notebook/' in href and href.endswith('.html'):
                chinese = href[:-5] + '.zh.html'
            elif any(href.endswith(name) for name in (
                'undergraduate-study-prompts.md',
                'answer-keys.md',
                'part0-evidence.md',
                'part0-media.md',
            )):
                chinese = href[:-3] + '.zh.md'
            if not chinese:
                return match.group(0)
            return f'href="{href}" data-source-en="{href}" data-source-zh="{chinese}"'

        text = re.sub(r'href="([^"]+)"', source_link, text)
        # A single renderer owns both language versions of the searchable library.
        if 'id="library"' in text:
            text = re.sub(r"<script>\s*'use strict';[\s\S]*?</script>",
                          f'<script src="{prefix}js/prompt-library.js"></script>', text, count=1)
        runtime = (f'<script src="{prefix}js/translations-zh.js"></script>'
                   f'<script src="{prefix}js/materials-zh.js"></script>'
                   f'<script src="{prefix}js/materials.js"></script>')
        return text.replace('</body>', runtime + '</body>', 1)

    for page in pages:
        original = page.read_text(encoding="utf-8")
        if '<body class="source-page">' not in original:
            continue
        prefix = '../' * (len(page.relative_to(site).parts) - 1)
        page.write_text(enhance(original, prefix), encoding="utf-8")
        count += 1
        if page.parent == site / 'demo-materials/notebook':
            renderer = ChineseHTML(dictionary)
            renderer.feed(original)
            translated = ''.join(renderer.output).replace('<html lang="en">', '<html lang="zh-CN" data-default-language="zh">', 1)
            page.with_suffix('.zh.html').write_text(enhance(translated, prefix), encoding="utf-8")

    # A Chinese downloadable answer key accompanies the in-place bilingual page.
    answers = (site / 'resources/answer-keys.html').read_text(encoding='utf-8')
    renderer = ChineseHTML(dictionary)
    renderer.feed(answers)
    translated = ''.join(renderer.output)
    from html import unescape
    paragraphs = re.findall(r'<(h1|h2|p)\b[^>]*>([\s\S]*?)</\1>', translated)
    markdown = []
    for tag, content in paragraphs:
        text = unescape(re.sub(r'<[^>]+>', '', content)).strip()
        if text:
            markdown.append(('# ' if tag == 'h1' else '## ' if tag == 'h2' else '') + text)
    (site / 'resources/answer-keys.zh.md').write_text('\n\n'.join(markdown) + '\n', encoding='utf-8')
    print(f'Localized {count} student pages; built 3 static Chinese Notebook sources.')

# Presentation language and theme

The two controls in the upper-right corner switch between **中文 / EN** and **light / dark**. The first visit opens in English with the projector-friendly light palette. A browser remembers choices locally; no preference is sent to an external service.

Language changes update the current slide in place. Slide IDs, expanded fragments, speaker notes, running timers, video elements and lab inputs are retained. Prompt copying always copies the text currently displayed. Chinese covers the slide copy, prompt examples, navigation, presenter controls and the embedded teaching labs. The 16 linked student pages now have Chinese/English and light/dark controls too. External websites and original papers retain their original language.

## Open a particular combination

Append options before the slide hash:

- `?lang=zh&theme=light#/start` — Chinese, light.
- `?lang=en&theme=light#/start` — English, light.
- `?lang=zh&theme=dark#/start` — Chinese, dark.
- `?lang=en&theme=dark#/start` — English, dark.

Explicit URL options take priority over saved choices. Buttons work even when browser storage is blocked. Use Tab and Enter/Space to operate them with a keyboard. Presentation controls are hidden when printing or exporting a PDF.

## Editing

The original `slides/part*.md` files remain the single source of slide structure. Reviewed Chinese copy lives in `js/translations-zh.js`; keys match complete English text nodes with normalized whitespace, not arbitrary substrings. Add or update a translation whenever slide text changes. Keep formulas, product names, source URLs, IDs and data attributes intact.

`js/preferences.js` reads preferences before the first paint and handles in-place translation. `css/preferences.css` defines the light palette, corner controls and Chinese typography. The original dark colors remain in `css/workshop.css`. Dynamic timer/copy text uses `WorkshopPreferences.t()`.

## Checks

After installing the existing pinned dependencies and building the site:

```sh
npm run build
python scripts/browser_check.py
python scripts/browser_visual_check.py
python scripts/browser_preferences_check.py
python scripts/browser_materials_check.py
```

The original browser regression explicitly opens the dark theme. The preferences suite checks all 54 slides in all four combinations, translation coverage, text contrast, bounds, exact clipboard text, timers, fragments, media, embedded labs, responsive controls, URL precedence and unavailable storage. CI retains the tested site, screenshots and JSON reports in the `workshop-qa` artifact for seven days.

## Student materials

Build with `npm run build` and serve `_site` to preview the complete bilingual site. `scripts/localize_materials.py` adds the shared controls and reading-page styles during the build, without duplicating the original teaching HTML. `js/materials-zh.json` contains reviewed translations of complete text nodes; update a key when the English source changes. `js/materials-zh.js` is generated, not hand-edited.

The 20 prompt translations live in `prompts/undergraduate-study-prompts.zh.md`. The renderer joins the English/Chinese records by stable prompt number, keeps open cards and filter values, searches both languages, and copies the currently displayed prompt. Both Markdown versions remain directly accessible.

Language and theme parameters travel through local HTML links, including when browser storage is blocked. Selecting Chinese on Materials also selects the three `demo-materials/notebook/*.zh.html` source pages, whose Chinese text is rendered at build time so an importer does not need JavaScript. The answer-key page also offers a Chinese Markdown download. External sources are not translated or rehosted.

The materials suite checks all 16 pages in four language/theme combinations, all 20 Chinese prompts, copy/search/filter behavior, static source import text, retained lab inputs, mobile/tablet overflow, unavailable storage and print-hidden controls.

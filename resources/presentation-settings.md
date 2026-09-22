# Presentation language and theme

The two controls in the upper-right corner switch between **中文 / EN** and **light / dark**. The first visit opens in English with the projector-friendly light palette. A browser remembers choices locally; no preference is sent to an external service.

Language changes update the current slide in place. Slide IDs, expanded fragments, speaker notes, running timers, video elements and lab inputs are retained. Prompt copying always copies the text currently displayed. Chinese covers the slide copy, prompt examples, navigation, presenter controls and the embedded teaching labs. Linked student materials and external references retain their original language.

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
```

The original browser regression explicitly opens the dark theme. The preferences suite checks all 52 slides in all four combinations, translation coverage, text contrast, bounds, exact clipboard text, timers, fragments, media, embedded labs, responsive controls, URL precedence and unavailable storage. CI retains the tested site, screenshots and JSON reports in the `workshop-qa` artifact for seven days.

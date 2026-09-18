# Boost Your Study Skills with AI

A practical workshop for undergraduate students. **Wenxin Jiang · 23 September 2026 · 14:30–16:30 HKT.**

[Open the slides](https://lucajiang.github.io/ai-for-undergraduates/) · [Student materials](https://lucajiang.github.io/ai-for-undergraduates/materials.html) · [Prompt library](https://lucajiang.github.io/ai-for-undergraduates/prompts/index.html)

## Workshop route

The 52-slide deck has an opening and six parts: **Choose, Ask, Understand, Explore, Verify, and AI past & future**. Slides are in English; presenter notes are in Mandarin.

The opening connects two research examples and two short capability demos to a familiar assignment question. Part 1 includes NotebookLM and Gemini Deep Research. The later sections move through concept explanations, interactive prediction, feedback and source checking. Part 6 closes with mathematical AI and a personal learning reflection.

Four exercises run for 4, 10, 8 and 6 minutes. The ten-minute break is after Part 2. Teaching and practice total 90 minutes, followed by 20 minutes of Q&A. See the [clock schedule](schedule.md).

## Teaching resources

- [Presenter guide](resources/presenter-guide.md), [video setup](resources/part0-media.md), and [opening-study Q&A](references/part0-evidence.md).
- [NotebookLM and Deep Research official guides](resources/google-study-tools.html), [in-chat interactive guide](resources/interactive-guide.html), and [AI future reading](references/future.html).
- [Materials](materials.html), [20 prompt templates](prompts/index.html), [eigenvector lab](demo-materials/stem/eigenvectors.html), and [PPV lab](demo-materials/medicine/ppv-lab.html).

## Edit the workshop

Edit `slides/part0.md` through `slides/part6.md`. Each slide has an ID, an English body, and one `Note:` block. Slide breaks use `---`. `index.html` loads all seven files through Reveal.js 5.2.1.

The existing theme is in `css/workshop.css` and `css/reader.css`. The visual layouts and small local SVG icons are in `css/visuals.css` and `js/visuals.js`. No external icon library, image service or font download is needed. Keep explanatory labels alongside decorative icons.

Prompts copy their visible text. Timers start manually. The four exercise anchors remain `first-demo`, `exercise1`, `exercise2` and `exercise3`; the displayed exercise numbers are 1–4. Press **S** or use **Notes** for presenter view. Press **V** for local-video setup. Source clips are linked, not distributed.

## Build and test

```sh
npm install --ignore-scripts --no-audit --no-fund
python scripts/check_sources.py
npm run build
python -m pip install playwright==1.55.0
python -m playwright install chromium
python scripts/browser_check.py
python scripts/browser_visual_check.py
```

The build places the pinned Reveal runtime in `_site/vendor/reveal/`. GitHub Actions runs structural/link checks, browser regression checks and visual-feature checks before publishing. QA screenshots and reports are saved as the `workshop-qa` workflow artifact.

For a quick development preview, serve the repository with `python -m http.server 8000` and open `http://localhost:8000`. The source entry point uses a CDN for Reveal; the built site uses its local bundled copy.

Before delivery, rehearse sign-in, AI generation, video playback and the venue's display/audio setup in the teaching account. The archived original outline is retained under `archive/`; it is not the current delivery plan.

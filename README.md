# AI for undergraduates

A public workshop by **Wenxin Jiang** for undergraduate students in Hong Kong. English slides, Mandarin presenter notes. **Use AI to think better — not to stop thinking.**

## Open the workshop

- [Slides](https://lucajiang.github.io/ai-for-undergraduates/)
- [Student materials](https://lucajiang.github.io/ai-for-undergraduates/materials.html)
- [Searchable prompt library](https://lucajiang.github.io/ai-for-undergraduates/prompts/)
- [Interactive visualizations in Gemini chat](https://lucajiang.github.io/ai-for-undergraduates/resources/interactive-guide.html)
- [Sources](https://lucajiang.github.io/ai-for-undergraduates/references/)

## Current teaching version

52 projected pages, with a standalone cover and outline. The schedule remains 90 minutes of teaching/practice, a 10-minute break after Part 2 and 20 minutes of Q&A. Four exercises now begin with a familiar assignment question and the student's own solution. See [schedule](schedule.md) and the detailed [presenter guide](resources/presenter-guide.md).

Student slides explain what to learn and try. Setup, generation waits, backup results and example provenance belong in presenter notes. Notebook import and quiz-generation waits have separate presenter checkpoints. The interactive-visualization request uses ordinary Gemini chat rather than requiring Canvas. Availability and generated output must be checked in the actual account; the prepared browser labs remain usable without an AI account.

All parts use external Markdown without nested sections. Copy buttons read the visible prompt. Eigenvector and PPV labs use original fictional teaching examples. The original outline remains labelled archived.

## Editing and local preview

Content: `slides/part0.md` through `slides/part5.md`. Styles: `css/workshop.css` and `css/reader.css`. Use `---` for slide breaks, `Note:` for Mandarin notes and `<!-- .slide: id="..." -->` for stable anchors. Do not wrap Markdown pages in `<section>`.

Quick Internet-connected preview:

```bash
python -m http.server 8000
```

Bundled build:

```bash
npm install --ignore-scripts --no-audit --no-fund
npm run build
python -m http.server 8000 --directory _site
```

Open localhost:8000. Reveal.js 5.2.1 is bundled locally by the build; external AI tools and YouTube still need Internet access. No font files or third-party videos are redistributed.

## Teaching material

- [Prompt templates](prompts/undergraduate-study-prompts.md)
- [First assignment conversation](demo-materials/assignment-warmup.html)
- [Eigenvector lab](demo-materials/stem/eigenvectors.html)
- [PPV lab](demo-materials/medicine/ppv-lab.html)
- [Interactive prompts and troubleshooting](resources/interactive-guide.html)
- [Answer keys](resources/answer-keys.md)
- [Evidence notes](references/part0-evidence.md)
- [Video runbook](resources/part0-media.md)
- [QA scope](resources/qa.md)

Press S or Notes for speaker view, Esc for overview. Timers are manual. Press V before class to select video files you have permission to use, or open `?presenter=1` for the Video setup button. Files stay on the device and must be reselected after reload. External source-video links locate only the start; stop those manually at the listed end.

## Before delivery

Rehearse with the actual school account, venue network and audio setup. A successful website test does not verify authenticated Gemini/Notebook or YouTube playback. Current host policy must be supplied by the organizer; do not invent permission to use AI on an assignment. No private student, patient or research data belongs in this repository.

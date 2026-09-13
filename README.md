# AI for undergraduates

A public workshop for undergraduate students in Hong Kong. English slides, Mandarin presenter notes. **Use AI to think better — not to stop thinking.**

## Open the workshop

- [Slides](https://lucajiang.github.io/ai-for-undergraduates/)
- [Student materials and four subject tracks](https://lucajiang.github.io/ai-for-undergraduates/materials.html)
- [Searchable, copyable prompt library](https://lucajiang.github.io/ai-for-undergraduates/prompts/)
- [Sources](https://lucajiang.github.io/ai-for-undergraduates/references/)

## Current version

Second-pass revision: 51 projected pages across Parts 0–5. The agreed schedule is 90 minutes of teaching/practice, a 10-minute break and 20 minutes of Q&A. See [schedule](schedule.md) and the detailed [presenter guide](resources/presenter-guide.md).

All parts now use external Markdown without nested slide sections. Copy buttons read the displayed code. The two Notebook processing stages have explicit fallbacks. Exercises separately assess prompt improvement, independent explanation and judgment of feedback. The eigenvector and PPV labs run locally in the browser on fictional teaching data.

The original outline is retained and labelled archived. Git history contains the first-pass deck. Current university policy and actual school-account screenshots have not been supplied; these are rehearsal checks, not fabricated content.

## Edit and preview

Content lives in `slides/part0.md` through `slides/part5.md`; shared styles in `css/workshop.css`. Use `---` for page breaks, `Note:` for Mandarin notes and `<!-- .slide: id="..." -->` for stable links. Do not wrap each Markdown page in `<section>`.

For a quick preview with Internet access:

```bash
python -m http.server 8000
```

For a bundled build (Node.js and Python required):

```bash
npm install --ignore-scripts --no-audit --no-fund
npm run build
python -m http.server 8000 --directory _site
```

Open localhost:8000. The bundled build includes Reveal.js locally; only external links and YouTube playback need the Internet. No font files or video files are copied from the development environment. Reveal.js is pinned to 5.2.1.

## Teaching materials

- [Prompt source of truth](prompts/undergraduate-study-prompts.md)
- [Difficult-concept prompts](prompts/part3-hard-concepts.md)
- [Critique and verification](prompts/critique-and-verification-prompts.md)
- [Eigenvector lab](demo-materials/stem/eigenvectors.html)
- [PPV lab](demo-materials/medicine/ppv-lab.html)
- [Answer keys](resources/answer-keys.md)
- [Evidence interpretation](references/part0-evidence.md)
- [Media notes](resources/part0-media.md)
- [QA scope and commands](resources/qa.md)

Press `S` or Notes for speaker view, `Esc` for overview. Chapter links are at the top. Timers start manually; pause/reset when required. Click a video to load its bounded excerpt; leaving the slide unloads it.

## Before delivery

Rehearse Notebook import and artifact generation with the actual school account. Confirm the host's academic-integrity policy, projected text size and video/audio playback on the venue network. Automated checks do not certify those external services. No private student, patient or research data belongs in this public repository.

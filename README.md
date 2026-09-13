# ai-for-undergraduates

A practical public workshop website for undergraduate students in Hong Kong on studying with Generative AI.

**Core message:** use AI to think better — not to stop thinking.

## View the slides

- Slide deck: `index.html`
- GitHub Pages: `https://lucajiang.github.io/ai-for-undergraduates/`

## Current status

### Part 0 — implemented

- evidence-based opening warning about AI and learning;
- frontier multimodal capability montage with short timestamped video excerpts;
- crutch-vs-scaffold framing;
- multimodal learning demo;
- four demo tracks for STEM, medicine, business, and humanities/social science;
- speaker notes, prompt cards, evidence and media notes.

### Part 1 — implemented

- task-first tool selection rather than a model leaderboard;
- Gemini / DeepSeek / Gemini Notebook positioning;
- reasoning-effort framework (routine → standard → extended/deep);
- quota-aware model use;
- live Gemini Notebook demo with processing time filled by reasoning slides;
- public Notebook demo source pack;
- backup/fallback presenter workflow;
- verification rubric and final decision tree.

### Part 2 — implemented

- Q&A prompt structure: **Role + Context + Constraints + Format**;
- distinction between study conversation prompts and action / agentic workflow prompts;
- bad-prompt-to-study-prompt examples;
- before-class, after-class, and exam-prep study workflows;
- active recall and AI-as-examiner workflow;
- Exercise 1: students build their own study loop;
- public undergraduate prompt template library.

### Part 3 — implemented

- difficult-concept learning framework: intuition → formalism → example → self-check;
- eigenvector demo connecting formula, geometry, and computation;
- Socratic one-hint-at-a-time tutoring pattern;
- multi-representation learning: words, symbols, diagrams, numbers, and code;
- coding-assisted concept visualization with a minimal Python example;
- discipline-specific concept options for STEM, medicine, business, and humanities/social science;
- Exercise 2: students choose a hard concept and make AI test their understanding.

## Workshop structure

See [`schedule.md`](schedule.md) for the 90-minute formal session plus Q&A structure.

## Part 0 materials

- [`prompts/part0-learning-prompt.md`](prompts/part0-learning-prompt.md)
- [`references/part0-evidence.md`](references/part0-evidence.md)
- [`resources/part0-media.md`](resources/part0-media.md)
- [`demo-materials/stem/eigenvectors.html`](demo-materials/stem/eigenvectors.html)
- [`demo-materials/medicine/diagnostic-testing.html`](demo-materials/medicine/diagnostic-testing.html)
- [`demo-materials/business/price-elasticity.html`](demo-materials/business/price-elasticity.html)
- [`demo-materials/humanities/argument-structure.html`](demo-materials/humanities/argument-structure.html)

## Part 1 materials

- [`slides/part1.md`](slides/part1.md)
- [`resources/part1-runbook.md`](resources/part1-runbook.md)
- [`demo-materials/notebook/lecture-diagnostic-testing.html`](demo-materials/notebook/lecture-diagnostic-testing.html)
- [`demo-materials/notebook/screening-reading.html`](demo-materials/notebook/screening-reading.html)
- [`demo-materials/notebook/common-misconceptions.html`](demo-materials/notebook/common-misconceptions.html)

## Part 2 materials

- [`slides/part2.md`](slides/part2.md)
- [`css/part2.css`](css/part2.css)
- [`resources/part2-runbook.md`](resources/part2-runbook.md)
- [`prompts/undergraduate-study-prompts.md`](prompts/undergraduate-study-prompts.md)

## Part 3 materials

- [`slides/part3.md`](slides/part3.md)
- [`css/part3.css`](css/part3.css)
- [`resources/part3-runbook.md`](resources/part3-runbook.md)
- [`prompts/part3-hard-concepts.md`](prompts/part3-hard-concepts.md)
- [`examples/linear-transform-visualization.py`](examples/linear-transform-visualization.py)

## Local preview

```bash
python -m http.server 8000
```

Then open <http://localhost:8000>.

## Presenter notes

Press `S` in Reveal.js to open speaker view.

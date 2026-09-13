# Part 1 presenter runbook

Target duration: **10 minutes**.

Part 1 teaches two transferable decisions:

1. **Where should the answer come from?** — a defined set of course sources vs an open-ended assistant.
2. **How much reasoning does this task deserve?** — fast/routine vs extended/deep reasoning.

The three products used in the workshop are examples, not a ranking:

- **Gemini** — broad multimodal assistant and default workshop tool.
- **DeepSeek** — alternative model, useful for comparison, a second opinion, and as a backup when usage limits matter.
- **Gemini Notebook (formerly NotebookLM)** — source-grounded study workflow over a defined set of materials.

## Timing

| Time | Action |
|---|---|
| 0:00–0:45 | Part 1 title + two decisions |
| 0:45–1:45 | Gemini / DeepSeek / Gemini Notebook positioning |
| 1:45–3:00 | **Start the live Gemini Notebook demo** |
| 3:00–5:45 | While Notebook is processing: reasoning effort + quota + “more thinking ≠ truth” |
| 5:45–7:45 | Return to Notebook: source grounding + quiz + optional slide deck |
| 7:45–9:00 | Model comparison / verification rubric |
| 9:00–10:00 | Decision tree + transition to Part 2 |

Do **not** wait on stage for generation. If the artifact is not ready when you return, use the backup notebook immediately or continue one more slide and return once.

## Before the workshop

1. Sign in to Gemini Notebook using the university account.
2. Create a **backup notebook** using the three demo sources below.
3. Pre-generate at least:
   - one Quiz;
   - one Slide Deck (or another current study artifact worth showing);
   - one source-grounded answer with citations.
4. Keep the backup notebook open in a second browser tab.
5. Also prepare a fresh empty notebook for the live demonstration.
6. Test the campus network and the university account in the actual presentation browser.

## Public demo sources

After GitHub Pages deploys, the sample sources are available at:

- `https://lucajiang.github.io/ai-for-undergraduates/demo-materials/notebook/lecture-diagnostic-testing.html`
- `https://lucajiang.github.io/ai-for-undergraduates/demo-materials/notebook/screening-reading.html`
- `https://lucajiang.github.io/ai-for-undergraduates/demo-materials/notebook/common-misconceptions.html`

They intentionally overlap but have different roles: lecture definition, conceptual reading, and misconceptions/self-test. This makes source citations easy to demonstrate.

## Live Notebook prompt

Use this after the sources finish importing:

```text
Based only on these sources, explain why sensitivity is not the same as
P(disease | positive).

Cite the supporting source passage and explain the distinction in language
suitable for a first-year undergraduate.

Then ask me one question that tests whether I actually understand the
conditional probabilities. Do not answer that question until I respond.
```

Then start a **Quiz** from the Studio panel. If appropriate, also show that Gemini Notebook can create other study artifacts such as flashcards, slide decks and audio/video overviews. Do not spend time demonstrating every artifact.

## What to point out when returning to Notebook

### 1. Source grounding

Click a citation and show the supporting passage. Say explicitly:

> “The value here is not that the AI sounds confident. The value is that I can inspect what source it used.”

### 2. Quiz as active recall

Ask students to answer before revealing feedback. Do not turn the demo into passive consumption of an automatically generated quiz.

### 3. Generated slides are orientation, not replacement

If you show a generated Slide Deck, frame it as a map of the material. Students should still return to the lecture/readings for detail and verification.

## Processing-time fallback

Notebook source ingestion and artifact generation can vary in duration. The workshop should never stop to wait.

Fallback order:

1. Continue the reasoning-effort slides while the live notebook runs.
2. Return once after ~3 minutes.
3. If still processing, open the pre-generated backup notebook.
4. If the account or network fails entirely, describe the workflow using the Part 1 slide and continue. Do not troubleshoot on stage.

## Reasoning-effort message

Avoid teaching model-version names as permanent categories. Use the stable concept:

- **Fast / low effort:** translation, extraction, formatting, short summaries.
- **Standard:** explaining, comparing, tutoring, organizing.
- **Extended / deep:** proofs, debugging, causal reasoning, multi-step mathematics.

Higher reasoning effort often costs more time and more usage quota. Students should spend it where reasoning is the bottleneck.

## Verification message

“Thinking mode” is not a truth mode. A model can still misunderstand the question, reason from a bad assumption, hallucinate a citation, or make a calculation error. For important answers, use a source, a calculation, or another model as an independent check.

When comparing Gemini and DeepSeek, use this rubric rather than output length or confidence:

1. Is it correct?
2. Is it clear enough to learn from?
3. Are important assumptions visible?
4. Can I verify it?

Disagreement between models is a reason to investigate, not a majority vote.

## Current product notes (verified September 2026)

- Google renamed **NotebookLM to Gemini Notebook** on July 16, 2026. It remains a standalone product focused on research and learning.
- Google documents compute-based Gemini usage limits and notes that more advanced models / higher thinking levels consume more usage. Avoid putting fixed daily numbers in the slides because limits can change.
- Gemini currently exposes multiple reasoning levels where available (for example Standard and Extended, with Deep Think on higher tiers).
- DeepSeek V4 supports both thinking and non-thinking modes and supports reasoning-effort controls. The slides intentionally avoid tying the teaching framework to a specific model version.

Official references:

- Google, “NotebookLM is now Gemini Notebook” (2026-07-16): https://blog.google/innovation-and-ai/products/gemini-notebook/notebooklm-gemini-notebook/
- Gemini Apps Help, usage limits and thinking levels: https://support.google.com/gemini/answer/16275805
- Gemini Notebook Help, usage limits: https://support.google.com/gemininotebook/answer/17670842
- DeepSeek API Docs, Thinking Mode: https://api-docs.deepseek.com/guides/thinking_mode/

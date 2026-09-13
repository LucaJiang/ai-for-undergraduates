# Part 3 runbook: learning difficult concepts with AI

## Timing target

Part 3 is scheduled after the 10-minute break.

| Time | Content | Presenter action |
|---:|---|---|
| 15:25–15:27 | Re-enter: difficult concepts | Reset attention after the break; remind students not to outsource the struggle |
| 15:27–15:30 | Why concepts are hard | Explain prerequisite gaps, representation gaps, and missing feedback loops |
| 15:30–15:34 | Eigenvector demo | Use Gemini or DeepSeek with the hard-concept prompt; emphasize intuition → formalism |
| 15:34–15:37 | Socratic mode | Show why one-hint-at-a-time is safer than direct solution mode |
| 15:37–15:40 | Multiple representations + coding | Mention words/symbols/diagram/numbers/code; optionally open the Python script |
| 15:40–15:48 | Exercise 2 | Students choose a concept and run the prompt themselves |

## Presenter framing

Part 3 should sound like this:

> “When a concept is hard, do not ask AI to explain everything. Ask it to identify the layer you are missing.”

The central distinction:

- bad use: `Explain this concept completely.`
- better use: `Start from what I already know. Build intuition first. Connect it to the formal definition. Then test me.`

## Live demo option A: eigenvectors

Use either Gemini or DeepSeek.

Recommended prompt:

```text
Role: Act as a patient linear algebra tutor.

Context: I know matrix-vector multiplication, but I do not understand the geometric meaning of eigenvectors.

Constraints: Do not start with a formal proof. Explain the intuition first, then connect it to A v = λ v. Use one 2D example.

Format: Give me a short explanation, one diagram description, and one self-check question. Do not reveal the answer until I try.
```

Expected output qualities:

- starts with direction-preserving transformation;
- explains λ as stretch/shrink/flip factor;
- does not jump immediately into characteristic polynomials;
- asks a check question.

If the model jumps too formal, follow up:

```text
This is too formal. Re-explain it using only geometry first. Use a grid transformation analogy and avoid determinant / characteristic polynomial until the end.
```

## Live demo option B: medical statistics

Useful if the audience looks less STEM-heavy.

Prompt:

```text
Role: Act as a medical statistics tutor.

Context: I know that sensitivity means P(test positive | disease), but I do not understand why a positive result may still have low positive predictive value.

Constraints: Do not start with Bayes' theorem. Use a population of 1,000 people and a 2x2 table first.

Format: Explain the intuition, show the table, connect it to the formula, and ask me one clinical interpretation question.
```

## Optional coding demo

Use `examples/linear-transform-visualization.py`.

Presenter line:

> “Here code is not doing my homework. It is letting me manipulate the concept and observe what changes.”

Recommended AI prompt if generating the code live:

```text
Role: Act as a coding tutor, not a homework solver.

Context: I want to understand eigenvectors by visualizing how a 2D matrix transforms several vectors.

Constraints: Write the smallest useful Python script using NumPy and Matplotlib. Add comments explaining what each part teaches conceptually. After the code, give me two parameter changes I can try myself.

Format: short explanation, minimal code, what to observe, two experiments.
```

Do not spend more than 90 seconds on code unless the audience is highly technical. Part 3 is about concept learning, not coding proficiency.

## Exercise 2 instructions

Students choose one difficult concept from their own course or from the slide menu.

### Suggested concepts

- STEM: eigenvector, entropy, Fourier transform, recursion, derivative as local linear approximation
- Medicine: sensitivity vs PPV, action potential, receptor affinity, odds ratio vs risk ratio
- Business / economics: marginal effect, elasticity, opportunity cost, net present value
- Humanities / social science: argument structure, causality, interpretation, counterargument

### Student workflow

1. Choose a concept.
2. Fill the hard-concept prompt.
3. Ask for intuition → formal definition → worked example.
4. Ask one self-check question.
5. Answer the question yourself.
6. Ask AI to critique your reasoning.

## What to watch for while walking around

Common failure modes:

- Student leaves placeholders blank.
- AI gives a long textbook answer.
- Student reads passively and does not answer the self-check question.
- AI solves an assignment-style question directly.
- Student does not specify what they already know.

Quick interventions:

- “Tell AI what you already understand.”
- “Ask for one hint, not the solution.”
- “Make AI ask you a question.”
- “Explain it back in your own words.”
- “Ask it what is wrong or imprecise in your explanation.”

## Debrief prompt

Ask the room:

> “What changed when you told AI not just what to explain, but how to teach you?”

Then transition to Part 4:

> “Now that we have used AI as a tutor, we can look at more advanced workflows: notebooks, data, code, and larger projects. The same rule still applies: do not outsource the part where learning happens.”

# Part 4 Presenter Runbook — Beyond Chat

Target time: **8 minutes** for Part 4, followed by **6 minutes** for Exercise 3.

## Purpose

Part 4 shows students that AI is not limited to a chat box. It can support source-grounded notebooks, executable examples, code visualizations, and multi-step workflows. The pedagogical boundary is strict:

> Advanced AI should make reasoning more traceable, not more hidden.

## Timing

| Time | Slide focus | Presenter action |
|---:|---|---|
| 0:00–0:45 | Beyond chat | Transition from Part 3: once AI can tutor and visualize, it can also become a larger learning environment. |
| 0:45–1:45 | Chat / Notebook / Code / Agent | Explain each interface in one sentence. Avoid product details. |
| 1:45–2:45 | Notebook | Refer back to the earlier Gemini Notebook demo. Emphasize source-grounded answers and source checking. |
| 2:45–4:00 | Code | Use one example: PPV table, logistic curve, price elasticity, or eigenvector transform. The point is toy simulation, not assignment automation. |
| 4:00–5:15 | Concept-to-code prompt | Show Role + Context + Constraints + Format in an advanced but still learning-safe prompt. |
| 5:15–6:20 | Agents carefully | Explain the delegation ladder: low-risk / reversible / high-risk. |
| 6:20–7:30 | Advanced workflow | Walk through Question → Sources → Notebook → Toy model → My explanation → AI critique. |
| 7:30–8:00 | Exercise transition | Tell students to write their own explanation first. |
| 8:00–14:00 | Exercise 3 | Students use the critique prompt. Walk around and inspect whether they are asking for critique rather than rewritten answers. |

## Recommended live example

Use the diagnostic-testing example from earlier materials:

1. Question: Why can a test with high sensitivity still have low positive predictive value?
2. Sources: lecture note + screening reading in Notebook.
3. Toy code: compute a 2×2 table for disease prevalence = 1%, sensitivity = 90%, specificity = 90%.
4. Student explanation: “A positive test is not always likely to mean disease because false positives can outnumber true positives when the disease is rare.”
5. AI critique: ask whether the student distinguished sensitivity from PPV.

This example works for medicine, statistics, public health, and business students.

## Exercise 3 instructions

Students should choose one concept from their own course or from the provided tracks:

- STEM: eigenvectors, entropy, recursion, Fourier transform
- Medicine: sensitivity vs PPV, action potential, odds ratio vs risk ratio
- Business: price elasticity, marginal cost, NPV
- Humanities / social science: causality, utilitarianism, argument structure

They should write 4–6 sentences first. Then they paste the critique prompt.

## Watch for failure modes

If students ask AI to rewrite immediately, redirect them:

> First ask for diagnosis, then revise yourself.

If students ask AI to solve an assessed problem:

> Convert it into a toy example or ask for one hint at a time.

If students paste real data:

> Stop and ask whether the data is allowed to be uploaded.

## Transition to Part 5

Use this bridge:

> Once AI can read sources, write code, and coordinate steps, the question becomes more serious: how do we verify it, protect data, and stay academically honest?

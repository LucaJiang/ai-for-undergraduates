# Critique and Verification Prompts

These prompts are designed for undergraduate study. Use them to make AI diagnose your understanding and make its own answer easier to check.

## 1. Critique my explanation

```text
Here is my explanation of [concept]:

[Paste my explanation]

Do not rewrite it yet.

1. Identify anything incorrect or imprecise.
2. Identify one important idea I missed.
3. Ask me one question that would reveal whether I truly understand it.
4. After I answer, help me revise my explanation.
```

## 2. Check whether I really understand

```text
I think I understand [concept].

Ask me three questions:
1. One basic definition question.
2. One application question.
3. One question about a common misconception.

Ask one question at a time. Do not show the answer until I try.
```

## 3. Make your answer checkable

```text
Before I rely on this answer:

1. List your key assumptions.
2. Mark which claims come directly from my provided material.
3. Mark which claims are your own inference.
4. Tell me what I should verify in the original source.
5. Give one simple test case or counterexample.
```

## 4. Find weak points in my solution

```text
Here is my attempted solution:

[Paste attempt]

Do not solve the whole problem for me.

1. Identify the first step where my reasoning becomes incorrect or unsupported.
2. Explain why that step fails.
3. Give me one hint for how to fix it.
4. Wait for my revised attempt.
```

## 5. Source-grounded verification

```text
Using only the materials I provided:

1. Which parts of your answer are directly supported?
2. Which parts are not explicitly supported?
3. Quote or point to the relevant section for each supported claim.
4. Tell me which claims I should not use unless I verify them elsewhere.
```

## 6. Academic integrity self-check

```text
I want to use AI for this course task:

[Describe the task]

Help me classify my intended AI use into one of three categories:
1. Learning support
2. Needs course-policy check
3. Likely inappropriate outsourcing

Ask me for missing information if the boundary depends on course instructions.
```

## 7. AI-use disclosure draft

```text
Draft a concise AI-use disclosure based on this information:

Tool used: [tool/model]
Purpose: [explanation / brainstorming / editing / code debugging / feedback]
My own contribution: [what I wrote, checked, changed, or rejected]
Verification: [course materials / original sources / tests / instructor guidance]

Keep it factual. Do not exaggerate or minimize the AI contribution.
```

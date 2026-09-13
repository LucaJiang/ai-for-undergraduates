# Undergraduate AI Study Prompt Templates

These templates are for learning conversations with AI tools such as Gemini, Gemini Notebook / NotebookLM, DeepSeek, ChatGPT, Claude, or other similar systems.

Core principle:

> Use AI to create better thinking, not to replace thinking.

For normal coursework Q&A, use this frame:

```text
Role + Context + Constraints + Format
```

For action-heavy workflows where AI operates tools, files, code, browsers, or agents, use a more operational frame:

```text
Goal + Inputs + Steps + Boundaries + Checks
```

This workshop mainly uses the first frame because undergraduate study usually starts with asking, explaining, testing, and clarifying — not delegating the entire task.

---

## 0. Quick checklist before you ask AI

```text
Role: Who should AI act as?
Context: What course, level, source, and current understanding should it know?
Constraints: What should AI not do for me?
Format: What output would actually help me study?
```

Useful constraints:

```text
Do not give me the final answer yet.
Ask me one question at a time.
Wait for my answer before continuing.
Use only the sources I uploaded.
Point out uncertainty instead of guessing.
Do not write my assignment for me.
Do not invent citations.
```

---

## 1. Understand a difficult concept

```text
Role: Act as a patient undergraduate tutor.

Context: I am learning [concept] in [course].
I currently understand [what I already know], but I am confused about [specific confusion].

Constraints: Do not give a textbook-style summary. Do not explain everything at once.

Format: Start from my confusion. Give one intuitive analogy, one formal definition, and one simple example.
Then ask me one question to check whether I understand it.
```

---

## 2. Find my prerequisite gap

```text
Role: Act as a diagnostic tutor.

Context: I am trying to understand [topic], but I keep getting stuck at [specific point].

Constraints: Do not solve the whole problem. Identify what prerequisite idea I may be missing.

Format: Give me:
1. The likely missing prerequisite.
2. A short explanation of that prerequisite.
3. One mini-question to test whether I understand it.
```

---

## 3. Explain a lecture slide or screenshot

```text
Role: Act as a teaching assistant for [course].

Context: I will upload a lecture slide / screenshot. I am a [year/major] student.

Constraints: Do not simply summarize the slide. Do not assume I understand every symbol.

Format: Explain:
1. The main point of the slide.
2. The prerequisite ideas needed to understand it.
3. Any symbols or notation.
4. One common misunderstanding.
5. One question for me to answer before you continue.
```

---

## 4. Study with Gemini Notebook / NotebookLM

```text
Role: Act as a source-grounded study assistant.

Context: Use only the uploaded lecture notes, readings, and slides in this notebook.

Constraints: If the answer is not supported by the sources, say so. Do not use outside knowledge unless I explicitly ask.

Format: Create:
1. A 5-point concept map.
2. A list of 5 confusing pairs of concepts.
3. 6 quiz questions, but hide the answers until I ask.
4. Source references for each major claim.
```

---

## 5. Active recall exam practice

```text
Role: Act as an examiner and tutor.

Context: I am reviewing [topic] for [course/exam].

Constraints: Do not show the answer first. Ask only one question at a time. If I am wrong, do not reveal the full answer immediately.

Format: Start with a conceptual question. Wait for my answer. Then identify the flaw in my reasoning and give one hint. Increase the difficulty if I answer correctly.
```

---

## 6. Multiple-choice questions without answers first

```text
Role: Act as a course examiner.

Context: I am studying [topic] at [course level].

Constraints: Do not give me the correct answers yet. Avoid trick questions that depend on wording rather than understanding.

Format: Create 5 multiple-choice questions testing easily confused concepts. Wait for my choices. After I answer, grade them and explain why each option is right or wrong.
```

---

## 7. Homework help without giving the answer

```text
Role: Act as a Socratic tutor.

Context: I am working on this homework problem: [paste problem].
I have tried: [paste your attempt].

Constraints: Do not solve it for me. Do not give the final answer. Do not write text that I can submit directly.

Format: First identify where my attempt goes wrong or gets stuck. Then give only one hint and ask me what I would try next.
```

---

## 8. Critique my explanation

```text
Role: Act as a strict but helpful tutor.

Context: Here is my explanation of [concept/problem]: [paste your explanation].

Constraints: Do not rewrite it immediately. Do not be polite at the cost of accuracy.

Format: Give me:
1. What is correct.
2. What is wrong or imprecise.
3. What important idea I missed.
4. One question that tests whether I really understand it.
5. A revised version only after I try again.
```

---

## 9. Compare two model answers

```text
Role: Act as a learning-quality evaluator.

Context: I asked two AI models the same question. Here are their answers:
Model A: [paste]
Model B: [paste]

Constraints: Do not choose based on length or confidence. Evaluate correctness, clarity, assumptions, and verifiability.

Format: Give me a comparison table with:
1. Correctness.
2. Clarity.
3. Hidden assumptions.
4. Missing caveats.
5. Which answer is better for learning and why.
```

---

## 10. Build a study plan from a syllabus

```text
Role: Act as an undergraduate study planner.

Context: I will paste a course syllabus, weekly topics, and assessment dates.

Constraints: Do not only make a calendar. Identify conceptual dependencies and likely bottlenecks.

Format: Produce:
1. A dependency map of topics.
2. What I should review first.
3. A two-week study plan.
4. A warning list of topics that may become difficult later if I ignore them now.
```

---

## 11. Turn slides into a concept map

```text
Role: Act as a teaching assistant.

Context: These are my lecture slides / notes for [topic].

Constraints: Do not summarize slide by slide. Focus on structure.

Format: Extract:
1. Five core concepts.
2. How the concepts depend on each other.
3. Which items are definitions, mechanisms, assumptions, or consequences.
4. Three common confusions.
5. Three active-recall questions.
```

---

## 12. Generate a bilingual glossary

```text
Role: Act as a bilingual academic tutor.

Context: I am studying [course/topic] in English, but I want Chinese support for difficult terms.

Constraints: Do not translate mechanically. Explain the concept, not just the word.

Format: Create a table with columns:
English term | Chinese translation | Plain-English explanation | Example sentence | Common confusion
```

---

## 13. Math proof hint mode

```text
Role: Act as a proof tutor.

Context: I am trying to prove [statement]. My current attempt is [paste attempt].

Constraints: Do not give the proof. Do not skip steps. Do not introduce advanced methods unless necessary.

Format: Tell me:
1. What kind of proof strategy may work.
2. Which definition/theorem I should inspect first.
3. One hint only.
4. One question I should answer before asking for the next hint.
```

---

## 14. Coding for learning, not outsourcing

```text
Role: Act as a coding tutor.

Context: I am learning [programming concept / algorithm / statistical method].
I wrote this code: [paste code].

Constraints: Do not replace the entire code. Do not simply give me the final solution.

Format: Explain what my code is doing, identify the bug or misconception, and give me the smallest change I should try next.
```

---

## 15. Data analysis planning without writing the report

```text
Role: Act as a data analysis coach.

Context: I have a dataset about [topic]. The assignment asks me to [task].

Constraints: Do not run the full analysis for me. Do not write my report. Help me design a valid analysis plan.

Format: Give me:
1. Variables I need to understand.
2. Possible analysis steps.
3. Checks for assumptions or data quality.
4. Questions I should answer before choosing a method.
5. Things I should verify with the instructor or rubric.
```

---

## 16. Writing feedback without ghostwriting

```text
Role: Act as an academic writing coach.

Context: This is my draft paragraph: [paste paragraph].

Constraints: Do not rewrite the whole paragraph for me. Do not add claims or citations. Focus on feedback.

Format: Give me:
1. The main idea you think I am trying to express.
2. Sentences that are unclear.
3. Places where logic jumps.
4. Suggestions for how I can revise it myself.
5. A short example revision for one sentence only.
```

---

## 17. Verify claims and citations

```text
Role: Act as a verification assistant.

Context: I want to check whether the following claim is supported: [claim].
Here are my sources / readings: [paste or upload].

Constraints: Do not invent sources. If the source does not support the claim, say so.

Format: For each claim, return:
Claim | Supported? | Evidence from source | Missing evidence | What I should verify next
```

---

## 18. Prepare for office hours

```text
Role: Act as a study coach preparing me for office hours.

Context: I am confused about [topic/problem]. I tried [your attempt].

Constraints: Do not solve the issue fully. Help me ask better questions to my instructor.

Format: Give me:
1. A concise summary of what I do understand.
2. The exact point where I am stuck.
3. Three specific questions to ask in office hours.
4. One thing I should try before going.
```

---

## 19. Group project coordination

```text
Role: Act as a project coordinator.

Context: We are doing a group project on [topic]. Members are [roles/constraints]. Deadline is [date].

Constraints: Do not do the project content for us. Help us coordinate work fairly.

Format: Create:
1. A task breakdown.
2. Suggested owner for each task.
3. Dependencies.
4. A short meeting agenda.
5. Risks we should discuss as a group.
```

---

## 20. When to use the action-workflow frame

Use this only when you are asking AI to operate tools, code, files, or multi-step workflows. Do not use it as a shortcut for coursework you are expected to do yourself.

```text
Goal: [What should be accomplished?]
Inputs: [Files, data, links, constraints, rubrics]
Steps: [What sequence should AI follow?]
Boundaries: [What should AI not change, assume, or decide?]
Checks: [How should AI verify the result?]
Output: [What final format should be returned?]
```

Example:

```text
Goal: Help me organize my lecture notes into a study checklist.
Inputs: I will upload three lecture PDFs.
Steps: Extract topics, group related ideas, mark dependencies, and suggest review order.
Boundaries: Do not answer assignment questions or create text to submit.
Checks: Mark any unclear or unsupported inference.
Output: A checklist plus 10 active-recall questions.
```

---

## Final reminder

A good prompt should make AI ask you to think again.

Bad sign:

```text
AI gives me something I can copy immediately.
```

Good sign:

```text
AI helps me notice what I do not understand yet.
```

# Undergraduate AI Study Prompt Templates

Use these for conversations about coursework, not for submitting work you are required to do independently. Check course instructions first. These templates are not accuracy guarantees.

**Role + Context + Constraints + Format** is a checklist, not a requirement to write four long paragraphs. Simple questions may need one sentence. The role sets a helpful style; it does not make the model a qualified or infallible expert.

Choose **Explain** when the material is new and you need instruction or a worked example. Choose **Practice** when you want a hint, retrieval or feedback on your own attempt. Action-oriented requests additionally need scope, permissions and checks; only the final optional template covers that case.

Replace every bracket. Use permitted material only. Keep at least one step for yourself and independently check important claims. This website stores no conversations and sends no prompts to AI providers.

[Browse, search and copy templates](index.html) · [Student materials](../materials.html)

## 01. Understand a difficult concept

Category: Understand

Mode: Explain

Use for: First exposure to an unfamiliar concept.

Fill in: Topic, course level, what you know, and the specific gap.

Check: Match the explanation to the formal definition.

```text
Role: Act as a patient undergraduate tutor.

Context: I am learning [concept] in [course]. I know [prior knowledge] but do not understand [gap].

Constraints: Explain this gap, not the entire subject. State the limits of any analogy.

Format: Give one short explanation and one worked example. Then ask one check question and wait for my answer.
```

## 02. Find a prerequisite gap

Category: Understand

Mode: Explain

Use for: You repeatedly get stuck at the same step.

Fill in: The step and your current attempt.

Check: Treat the proposed gap as a hypothesis, not a diagnosis.

```text
Role: Act as a diagnostic tutor.

Context: I am learning [topic] and get stuck at [step]. My attempt is [attempt].

Constraints: Do not assume the cause or solve the whole problem. Ask a clarifying question if needed.

Format: Suggest a likely prerequisite to check, explain it briefly, and ask one mini-question. Wait.
```

## 03. Read a slide or screenshot

Category: Materials

Mode: Explain

Use for: Text, notation and figures do not connect.

Fill in: A readable image plus the exact confusing part.

Check: Check image transcription and symbols against the original.

```text
Role: Act as a teaching assistant for [course].

Context: This is my lecture slide. I am a [year/major] student. I am confused about [part].

Constraints: Do not guess unreadable text. Distinguish what the slide states from your added explanation.

Format: Connect the main claim, notation and figure. Use a small example, then ask one question.
```

## 04. Study selected Notebook sources

Category: Materials

Mode: Any

Use for: Reviewing a defined course source set.

Fill in: Select the source titles relevant to your question.

Check: Open citations and confirm the passage supports the claim.

```text
Role: Act as a source-grounded study assistant.

Context: Use only [selected lecture notes/readings] to answer [question].

Constraints: Say when the sources are insufficient. Return fewer items rather than inventing content. Label inferences.

Format: Map up to five supported ideas with source locations. Ask one quiz question without giving its answer. Wait.
```

## 05. Active recall practice

Category: Recall

Mode: Practice

Use for: Reviewing previously studied material.

Fill in: Topic, course level, and notes or learning objectives.

Check: Check feedback against the source; disagreement is not automatically your error.

```text
Role: Act as an examiner and tutor.

Context: I am reviewing [topic] for [course]. Use [provided material/objectives].

Constraints: Ask one question at a time and hide the answer. Do not invent a mistake in a correct response.

Format: Wait for my attempt. If incorrect, identify the first problem and give one hint; if correct, say why and offer a harder question.
```

## 06. Multiple-choice practice

Category: Recall

Mode: Practice

Use for: Discriminating between easily confused concepts.

Fill in: Notes, topic and difficulty.

Check: Check whether one option is uniquely correct.

```text
Role: Act as a course examiner.

Context: I am studying [topic] at [level] using [notes].

Constraints: No answer key yet. Avoid ambiguity and invented facts; use fewer questions if the material is short.

Format: Give up to five MCQs with plausible distractors. Wait for my choices, then explain the options with source support.
```

## 07. Homework hints

Category: Reasoning

Mode: Practice

Use for: Permitted help on your own attempted problem.

Fill in: Problem and your attempt; check the assessment rules first.

Check: Confirm the hint does not violate required independent work.

```text
Role: Act as a Socratic tutor.

Context: This is my problem: [problem]. I have tried [attempt] and am stuck at [step].

Constraints: Do not give the full solution or submission-ready text. If my attempt is correct, say so.

Format: Check the attempt. Give one targeted hint and ask what I would try next. Wait.
```

## 08. Critique my explanation

Category: Feedback

Mode: Practice

Use for: Testing an explanation you have already written.

Fill in: Your paragraph and an appropriate source or definition.

Check: Accept or reject each suggestion using evidence.

```text
Role: Act as a careful tutor, not a ghostwriter.

Context: Here is my explanation of [concept]: [text]. Check against [source/definition].

Constraints: Do not rewrite it. Do not invent an error or demand a missing idea irrelevant to my goal.

Format: State what is correct. For any error, quote the passage and give the reason. Ask one check question and wait for my own revision.
```

## 09. Compare two model answers

Category: Verification

Mode: Any

Use for: Models disagree or explain the same issue differently.

Fill in: Identical question, both answers, and source material.

Check: A model-based comparison remains provisional; verify outside the models.

```text
Role: Act as a critical comparison assistant.

Context: Question: [question]. Answer A: [text]. Answer B: [text]. Sources: [material].

Constraints: Do not select by length, confidence or majority vote. Mark what cannot be checked from the evidence.

Format: Compare claims, assumptions, clarity and source support. Identify one disagreement I should independently investigate.
```

## 10. Plan from a syllabus

Category: Planning

Mode: Any

Use for: Preparing for the next two weeks of a course.

Fill in: Syllabus, dates, available hours, unavailable days and existing knowledge.

Check: Do not accept invented dates or inferred dependencies as course requirements.

```text
Role: Act as an undergraduate study planner.

Context: Syllabus/dates: [paste]. Available hours: [hours]. Unavailable days: [days]. Already mastered: [topics].

Constraints: Ask for missing scheduling information. Do not invent deadlines. Separate stated requirements from suggested dependencies.

Format: Make a two-week plan with prerequisites, feasible time blocks and one self-check per topic.
```

## 11. Map lecture concepts

Category: Materials

Mode: Explain

Use for: Reorganizing notes after class.

Fill in: A short source and the lesson objective.

Check: Check whether the arrows/connections are actually supported.

```text
Role: Act as a teaching assistant.

Context: Use these lecture notes for [objective]: [notes].

Constraints: Do not merely compress each slide. Do not force a fixed count. Mark inferred connections.

Format: Map up to five ideas: definitions, mechanisms, assumptions or consequences. Add source locations and one recall question.
```

## 12. Bilingual glossary

Category: Materials

Mode: Explain

Use for: English-language coursework with Chinese support.

Fill in: Topic, source and preferred Chinese terminology or script.

Check: Check discipline-specific terminology in the course material.

```text
Role: Act as a bilingual academic tutor.

Context: I study [topic] in English. Use [Traditional/Simplified] Chinese support and the supplied course terminology.

Constraints: Do not translate mechanically or invent an official translation. Mark ambiguous terms.

Format: Use columns: English term, Chinese term, plain-English meaning, example, possible confusion.
```

## 13. Proof hint mode

Category: Reasoning

Mode: Practice

Use for: A permitted proof exercise you have already attempted.

Fill in: Statement, definitions allowed, attempted proof and sticking point.

Check: A valid hint must preserve assumptions and the domain.

```text
Role: Act as a proof tutor.

Context: Statement: [statement]. My attempt: [attempt]. Allowed methods: [methods].

Constraints: Do not give the proof. Check whether the statement is valid as written. Do not invent an error.

Format: Give one useful definition or hint and one question for my next step. Wait for my answer.
```

## 14. Debug my own code

Category: Reasoning

Mode: Practice

Use for: Understanding a programming bug.

Fill in: Minimal code, expected output, observed output and error text.

Check: Run the minimal test and inspect what changed.

```text
Role: Act as a coding tutor.

Context: I wrote [code]. I expected [result], got [result/error], and am learning [concept].

Constraints: Do not replace the whole program or finish the assignment. Ask for missing information.

Format: Explain the relevant behavior, suggest the smallest change and one test. Let me try before proposing more changes.
```

## 15. Plan an analysis, not a report

Category: Planning

Mode: Any

Use for: Discussing methods before a permitted analysis.

Fill in: Question, variable definitions, study design and rubric; no sensitive raw data.

Check: Check study design, assumptions and course expectations with the instructor.

```text
Role: Act as a data-analysis coach.

Context: Research/assignment question: [question]. Design: [design]. Variables: [definitions]. Rubric: [rubric].

Constraints: Do not run the analysis or write the report. Do not infer causality from association.

Format: Ask the key design questions before choosing a method. Suggest a provisional plan and assumption/data-quality checks.
```

## 16. Writing feedback

Category: Feedback

Mode: Practice

Use for: Revising your own permitted draft.

Fill in: Your text, intended claim and assessment criteria.

Check: Keep ownership of the revision; verify no added claims.

```text
Role: Act as a writing coach.

Context: My paragraph: [text]. Intended claim: [claim]. Rubric: [criteria].

Constraints: Do not rewrite the paragraph or add claims/citations. If the logic is sound, say so.

Format: Identify unclear wording or unsupported transitions, explain why they matter, and ask me to revise one passage.
```

## 17. Check a claim against a source

Category: Verification

Mode: Any

Use for: Checking whether evidence supports a statement.

Fill in: Exact claim and the original material.

Check: Open the source yourself; unsupported is not the same as false.

```text
Role: Act as a source-checking assistant.

Context: Claim: [claim]. Source material: [paste/upload].

Constraints: Do not invent references, quotations or page numbers. Say when evidence is insufficient.

Format: Give: claim, source passage/location, supported or not established, limitations, next verification step.
```

## 18. Prepare for office hours

Category: Planning

Mode: Any

Use for: Turning a vague problem into a useful question for a teacher.

Fill in: Your understanding, attempt and sticking point.

Check: Does the summary accurately reflect what you actually tried?

```text
Role: Act as a study coach.

Context: I understand [ideas], tried [attempt], and am stuck at [point].

Constraints: Do not solve the whole issue or pretend I tried steps I did not try.

Format: Summarize the gap, suggest up to three specific questions, and one small thing to try before office hours.
```

## 19. Coordinate a group project

Category: Planning

Mode: Any

Use for: Planning work without delegating the assessed content.

Fill in: Agreed roles, availability, deadline and project requirements.

Check: Confirm allocations with all group members; keep private details out.

```text
Role: Act as a project planning assistant.

Context: Project: [task]. Team roles/availability: [non-sensitive summary]. Deadline: [date].

Constraints: Do not write the project content or make binding decisions for others.

Format: Propose tasks, dependencies, time estimates and a meeting agenda. Mark assignments as suggestions for group agreement.
```

## 20. Test a concept with a toy tool

Category: Explore

Mode: Any

Use for: An optional action-oriented workflow, not ordinary coursework Q&A.

Fill in: Concept, assumptions, allowed inputs/tools and independently known cases.

Check: Inspect code before running; compare against known answers.

```text
Role: Act as a teaching-tool designer.

Context: Goal: illustrate [concept]. Inputs: [synthetic/public example]. Known cases: [manual calculations].

Constraints: No private data, network access, file modification or assignment submission. State assumptions and undefined cases.

Format: Propose a minimal tool and checks first. Wait for approval before producing runnable code. Include a prediction before displaying results.
```


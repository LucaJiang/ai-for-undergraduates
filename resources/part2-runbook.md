# Part 2 presenter runbook

## Part 2 goal

Help students move from casual AI chat to deliberate learning conversations.

Core distinction requested by the presenter:

- For ordinary study Q&A: **Role + Context + Constraints + Format**.
- For action-heavy AI workflows: **Goal + Inputs + Steps + Boundaries + Checks**.

Part 2 should focus on the first pattern because the workshop is teaching students how to communicate with AI about coursework without outsourcing the work.

---

## Target timing

Part 2 formal content: **15 minutes**

| Time | Segment | Slide intent |
|---:|---|---|
| 0:00–1:00 | Transition | From tool selection to learning conversations |
| 1:00–3:00 | Two prompt modes | Q&A vs action workflows |
| 3:00–5:00 | RCCF formula | Role, Context, Constraints, Format |
| 5:00–7:00 | Bad → better prompt | Logistic regression example |
| 7:00–10:00 | Three workflows | Before class, after class, exam review |
| 10:00–12:00 | Active recall | AI as examiner, not answer machine |
| 12:00–13:30 | AI roles | Explainer, tutor, examiner, critic, organizer |
| 13:30–15:00 | Exercise setup | Students choose a track and copy scaffold |

Exercise 1: **10 minutes**

| Time | Activity |
|---:|---|
| 0:00–2:00 | Students choose a track and material |
| 2:00–6:00 | First prompt attempt |
| 6:00 | Presenter reminder: add constraints and make AI wait |
| 6:00–9:00 | Students revise prompt and try again |
| 9:00–10:00 | Quick reflection: what changed? |

Then break: **10 minutes**.

---

## Opening line

> In Part 1, we chose the tool and the reasoning effort. Now we design the conversation. For study Q&A, the simplest reliable structure is Role, Context, Constraints, and Format.

---

## Key teaching point

A prompt is not a spell. It is a contract for the learning interaction.

For undergraduate learning, the most important parts are usually:

- **Context**: the AI needs to know your level and current confusion.
- **Constraints**: the AI should not solve, reveal, or write everything for you.
- **Format**: the AI should make you do the next cognitive step.

---

## Exercise 1 tracks

### Track A — Understand

Use when a student has one lecture slide, paragraph, diagram, or formula they do not understand.

Recommended starting prompt:

```text
Role: Act as a patient undergraduate tutor.
Context: I am learning [topic] in [course]. I understand [X], but I am confused about [Y].
Constraints: Do not summarize everything. Do not solve a related assignment for me.
Format: Start from my confusion, explain one prerequisite idea, then ask me one question.
```

### Track B — Recall

Use when a student has already studied something but wants to test memory.

Recommended starting prompt:

```text
Role: Act as an examiner and tutor.
Context: I am reviewing [topic] for [course/exam].
Constraints: Do not show the answer first. Ask one question at a time.
Format: Wait for my answer, identify the flaw, give one hint, then ask me to try again.
```

### Track C — Plan

Use when a student has a syllabus or course outline.

Recommended starting prompt:

```text
Role: Act as an undergraduate study planner.
Context: I will paste my syllabus and assessment schedule.
Constraints: Do not only make a calendar. Identify dependencies between topics.
Format: Give me a two-week plan, what to review first, and likely bottlenecks.
```

### Track D — Bring your own

Students use their own course material. Encourage this when possible.

---

## Instructor patrol checklist

When looking at student outputs, ask:

1. Did the prompt include the student's current understanding?
2. Did the student tell AI what not to do?
3. Did the AI ask the student to think next, or did it just produce an answer?
4. Did the student verify source-dependent claims?

---

## Common student problems and fixes

### Problem: AI gives a long summary

Fix:

```text
Do not summarize the whole topic. Start with only the prerequisite concept I am missing.
```

### Problem: AI reveals answers immediately

Fix:

```text
Do not show the answer first. Ask me one question and wait.
```

### Problem: AI writes something that could be submitted

Fix:

```text
Do not write my assignment. Give feedback, questions, or revision suggestions only.
```

### Problem: AI hallucinates details from a source

Fix:

```text
Use only the uploaded source. For each claim, quote or cite the source location. If unsupported, say unsupported.
```

---

## Link to prompt library

Public template file:

```text
prompts/undergraduate-study-prompts.md
```

Use it as a handout, not as a rigid script. Students should replace placeholders with their real course, topic, level, attempt, and constraints.

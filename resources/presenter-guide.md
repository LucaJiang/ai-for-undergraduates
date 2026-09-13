# Presenter guide — second-pass revision

English slides, Mandarin delivery. Six parts, 51 projected pages including exercise/debrief/break/Q&A pages. The source packs, prompt library and evidence notes are companion material, not additional lecture pages. Keep the agreed 90 minutes of content/practice, a 10-minute break, and 20 minutes of Q&A. The original outline is archived, not the current run-of-show.

## Clock schedule

| Time (HKT) | Segment | Content / output |
|---|---|---|
| 14:30–14:40 | Part 0 | Learning evidence, 74 seconds of video, brief educational demo |
| 14:40–14:50 | Part 1 | Tool choice + two-stage Notebook preparation/demonstration |
| 14:50–15:05 | Part 2 | Role + Context + Constraints + Format; useful follow-up questions |
| 15:05–15:15 | Exercise 1 | Before/after prompts and one observable improvement |
| 15:15–15:25 | Break | 10 minutes, not another exercise |
| 15:25–15:40 | Part 3 | Predict → reveal → connect geometry and definition |
| 15:40–15:48 | Exercise 2 | Own explanation or attempt with AI answer hidden |
| 15:48–15:56 | Part 4 | One complete PPV toy-tool demonstration and independent checks |
| 15:56–16:02 | Exercise 3 | Accept/reject AI feedback with a reason, then revise |
| 16:02–16:10 | Part 5 | Source verification, course policy, privacy, disclosure, closing |
| 16:10–16:30 | Q&A | Questions and unresolved concerns |

Exercise debriefs are included in the exercise minutes. Do not add extra discussion blocks after each one. All slides have Mandarin notes; press S or Notes. Timers are manual and continue across slide navigation; pause/reset explicitly.

## Part 0 — 10 minutes

0:00–0:40 opening; 0:40–2:00 negative and guarded-tutor comparison; 2:00–2:45 positive study; 2:45–5:00 capability setup and three excerpts; 5:00–7:40 one source-image learning conversation; 7:40–10:00 agreement, student response and transition buffer.

The video player is click-to-load with start/end bounds, not a local video edit. Leaving a slide unloads it. Check audio, ads, captions, embedding permission, selected scene and the venue network. No actual third-party playback or best-frame selection is certified by the automated browser tests. Skip a failed video immediately; use the on-screen capability and original link. Do not claim that all clips show the newest model version.

For the learning-image demo open the eigenvector lab, reveal the first vector, then screenshot the matrix selector and graph. The page now supplies a matrix, coordinates and input/output labels. A general explanation is not wrong; the improved prompt supplies the student's actual gap. Use a prepared example when generation is slow and label it as prepared.

## Part 1 — two waiting stages, not one

Prepare three tabs on the instructor's school account:

- A: a fresh notebook for importing sources live.
- B: the same sources already imported, for import failure/latency.
- C: one pre-generated Quiz, one source-linked answer and optionally one Slide Deck.

| Elapsed | Action |
|---|---|
| 0:00–1:00 | Start import in A, then immediately return to slides. Do not wait to ask a question. |
| 1:00–3:30 | Explain tool choice and source-grounded vs open questions. |
| 3:30–4:00 | Check once: if A is ready start Quiz; otherwise use B. |
| 4:00–6:30 | Explain reasoning effort, show the real account's menu, discuss checks. |
| 6:30–9:15 | Return: inspect a citation, answer one quiz item, optionally preview prepared slides. If still generating use C. |
| 9:15–10:00 | Recap and transition. |

When using B/C say it was prepared in advance. Import latency and artifact latency are variable; the schedule is not a service-time guarantee. A Quiz is started from the actual Studio control after source import, not assumed to start from an ordinary chat prompt. Do not display a fabricated product screenshot. Student access is reported by the organizer; it has not been tested from this development environment.

Public source pack: [materials.html#notebook](../materials.html#notebook). If account/network access fails, work through the original table and questions with [the answer key](answer-keys.html), not a fake Notebook result. Sources this short may yield a whole-source citation rather than a pinpoint citation. Check it before presenting.

## Part 2 — study conversation, not task delegation

Use RCCF as a context checklist. Short questions remain valid. Show the prepared three-turn example, explicitly labelled illustrative, to teach follow-up rather than “rewrite a longer prompt”. Explain and Practice modes serve different stages: beginners may need a worked example before retrieval. Study plans must include available hours and distinguish inferred dependencies from the syllabus.

During Exercise 1: 2 minutes choose material; 4 minutes test and inspect; 3 minutes refine/follow up; 1 minute record. Keep one topic for the next exercises. Use the searchable [prompt library](../prompts/index.html); students replace brackets rather than submitting blank templates.

## Part 3 — 15 minutes + 8-minute exercise

2 minutes frame the obstacle, 2 minutes connect representations, 4 minutes predict/reveal the eigenvector lab, 2 minutes connect to Av=λv and edge cases, 2 minutes one-hint dialogue, 1 minute analogy limits, 2 minutes explain track choice/exercise.

Use A=diag(2,1). Compare (1,0) with (1,1), asking for a prediction first. Then show reflection or projection as time permits. Nonzero input is required; λ=0 is allowed; “same direction” needs a sign/zero caveat. The labelled interactive tool is prepared and numerically tested, not a live model transcript. Keep code generation for Part 4.

Exercise 2: 1 minute choose, 3 minutes learn, 2 minutes hide the answer and explain/apply, 2 minutes independently check a source/key. Keep the student's paragraph for Exercise 3. A new example and a limit of the analogy matter more than fluent wording.

## Part 4 — one complete demo / 8 minutes

1 minute frame the question; 1 minute show the action-oriented build request; 3 minutes operate the PPV lab; 1 minute check arithmetic independently; 2 minutes explain boundaries and hand off to Exercise 3.

Open [the PPV lab](../demo-materials/medicine/ppv-lab.html). Change only prevalence first. Se=Sp=90%, N=10,000: p=10% gives 900/(900+900)=50%; p=1% gives 90/(90+990)≈8.3%. Then use the no-positive preset: PPV is undefined, not zero. Counts are expected values, not sampled people; fixed test performance across populations is a deliberate simplification. This is not clinical advice.

The safe default is to show the prepared implementation and its request. Live code generation is optional, requires review, and must not consume the demonstration slot. Do not require student installations or let an agent submit assessed work.

Exercise 3: 1 minute prepare own text, 3 minutes inspect feedback, 2 minutes revise. A correct explanation need not change. Students may reject an unsupported criticism, with evidence. Do not accept feedback merely because it is confident or long.

## Part 5 — 8 minutes + Q&A

Use the original humanities passage for a one-minute claim/source check. It supplies an argument, not a controlled study. “Unsupported by this passage” is not “proved false”. Show the source, ask students, then reveal the answer. Follow with exact-source checks, course-policy priority, privacy and an honest disclosure example. Keep the final THINK / VERIFY / INTEGRITY checklist visible before Q&A.

## Final rehearsal still required

The school/account menus, Notebook imports/generation, venue network/audio, third-party videos, and host policy cannot be validated by local automated tests. Prepare the actual school policy URL before delivery. Under-18 availability and Workspace sharing rules may constrain some optional artifacts; no student is required to create a slide deck. Do not promise a public Notebook share link from an Education account.

## Sources and status

[Evidence notes](../references/part0-evidence.md) distinguish study results from teaching recommendations. [Official product references](../references/index.html#products) were checked on 13 September 2026. [QA documentation](qa.md) explains what automated checks cover and what they do not.

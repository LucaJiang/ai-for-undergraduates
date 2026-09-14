# Presenter guide — reader-focused revision

**Wenxin Jiang · 23 September 2026 · Hong Kong**

English slides and Mandarin delivery. The deck has 52 pages. Presenter logistics belong here and in `Note:` blocks, not on student slides. Four exercises now run in chronological order; existing fragment IDs remain stable for old links.

## Clock schedule

| Time | Segment | Student activity |
|---|---|---|
| 14:30–14:40 | Opening / Part 0 | Evidence, short demos and Exercise 1 (four minutes on a familiar assignment question) |
| 14:40–14:50 | Part 1 | Tool and thinking choices; Notebook demonstration |
| 14:50–15:05 | Part 2 | Role + Context + Constraints + Format; follow-up questions |
| 15:05–15:15 | Exercise 2 | Improve the first conversation |
| 15:15–15:25 | Break | Ten-minute break after Part 2, before Part 3 |
| 15:25–15:40 | Part 3 | Difficult concepts and multiple representations |
| 15:40–15:48 | Exercise 3 | Explain without looking at the AI answer |
| 15:48–15:56 | Part 4 | In-chat interactive visualization, prediction and independent checks |
| 15:56–16:02 | Exercise 4 | Accept or reject AI feedback with a reason |
| 16:02–16:10 | Part 5 | Sources, course rules, privacy and closing |
| 16:10–16:30 | Q&A | Questions and unresolved concerns |

90 minutes teaching/practice + 10-minute break + 20-minute Q&A. Debriefs stay inside exercise slots. Do not let a generation delay consume an exercise or the break.

Ask students to bring an assignment and their own solutions before arrival. They must check whether discussing the question with AI is allowed. Share one question, not a whole document with names or student IDs. Use the [public warm-up](../demo-materials/assignment-warmup.html) when an assignment cannot be used.

## Part 0 — exact Gemini conversation

Suggested timing: cover and outline 40 seconds; mathematics study 70 seconds; positive study 35 seconds; capabilities 15 seconds; videos and transitions 90 seconds; instructor demonstration 40 seconds; student exercise four minutes; debrief and transition about one minute. Simplify commentary rather than rushing student work.

开场：“我是 Wenxin Jiang。今天我们练习怎样和 AI 讨论功课、核对解释，再用它帮助自己学会。”目录明确休息在Part 2及练习之后。研究数值是相对对照组的变化，不是百分点变化；不把短期研究结果推广成普遍的学期成绩保证。

### 讲者第一条消息

打开Gemini普通聊天，不需要Canvas。直接粘贴：

```text
I am studying introductory quantitative reasoning.
A price rises from HK$100 to HK$120. What is the percentage increase?
My solution is (120 - 100) / 100 × 100% = 20%, because the original price is the reference value.
Check my reasoning without rewriting my solution. If it is correct, say so.
Ask me one question about why I used 100 in the denominator, then wait.
```

若问为什么分母是100，回答：

```text
My denominator is the original price because percentage change compares the change with the starting value.
Is that explanation precise? Please check it, then ask one related question without giving the answer.
```

若问从120降回100，先请学生预测，再回答：

```text
I would use (120 - 100) / 120 × 100%, about 16.7%, because 120 is now the starting price. Check my explanation.
```

若直接给完答案：

```text
Pause. Do not give another solution. Ask me one check question and wait for my response.
```

若它错误否定20%：

```text
Check which value is the starting price. It is HK$100.
Please recompute the percentage change and identify the exact step you think is wrong.
```

独立核验：涨幅20%；反向跌幅约16.7%。不要为了演示制造虚假的模型错误。回应慢时让学生开始自己的交流，不等讲者示范完成。

### 学生四分钟

1分钟选择会做的一题、贴题及自己的解法；2分钟阅读反馈并回答一次追问；1分钟判断反馈是否正确并保存。巡视问：“它检查的是同一道题吗？你能判断它哪句话是对的吗？”这里不让AI先解一道学生完全不会做的题。后面Exercise 2继续改进这段交流。

### Video playback

See [media runbook](part0-media.md). Press **V** before class, or open the deck with `?presenter=1`, to select video files you have permission to use. Full source videos use the saved source times; already-trimmed excerpts begin at zero. Files remain local, survive slide navigation, and must be selected again after reload. Leaving a slide stops its player. No video files are committed or uploaded.

Standard YouTube embeds are an alternative, not a promised fix for login/anti-bot restrictions. Watch on YouTube opens the source in the signed-in browser at the start time; manually stop at the listed end. Do not imply that changing the embed domain bypasses authentication. Failed playback should not become an on-stage debugging session.

## Part 1 — two waiting stages, only in the presenter workflow

Prepare A: empty Notebook, B: sources already imported, C: quiz and optional study slides already generated. Use the actual school account.

| Elapsed | Presenter action | Student-facing topic |
|---|---|---|
| 0:00–1:00 | Start import in A, return to slides | What a course notebook helps you do |
| 1:00–3:30 | Leave import running | Tool choice; notes versus wider knowledge |
| 3:30–4:00 | Check A once; use B if needed; start Quiz | Quiz, flashcards and study slides |
| 4:00–6:30 | Leave generation running | Thinking modes and checking answers |
| 6:30–9:15 | Show an answer/citation, one quiz question and optional slides; use C if needed | Read the source and answer before feedback |
| 9:15–10:00 | Return to slides | Source, effort and verification |

具体提问：

```text
Use the selected course notes to explain the difference between sensitivity and the chance of disease after a positive test.
Show the passage that supports your explanation.
```

点击引用让学生看到原文。Quiz可以用确定问题：“Among the 180 people with positive tests, 90 have the disease. What fraction is that?” 答案50%。这里是1000人的source表，不要与Part 4的10000人表混淆。

使用预生成结果时，口头如实说明“这份是我提前生成的”。学生不需要看备课标记。等待时间不作保证。导入网页文字不代表已经读到全部图片或视频画面。

## Part 2 — improve the first conversation

Retain RCCF. It is a checklist, not four mandatory paragraphs. Simple questions may be short. The teaching dialogue is illustrative; do not call it a recorded Gemini run. Its provenance belongs in notes, not as a caption interrupting the student conversation.

Exercise 2: reopen Exercise 1, identify missing context or an unhelpful response, then revise and ask again. Suggested split: two minutes inspect, four minutes test, three minutes follow up, one minute record. Keep before/after prompts and a specific difference. Debrief inside the last minute.

Break: 15:15–15:25. Show a ten-minute timer; the outline already establishes its position. Do not add work to the break.

## Part 3 — understand and explain

Use the student's own course where possible. Eigenvectors are the demonstration, not a requirement for every discipline. Let students predict what happens to (1,0) and (1,1) under a matrix doubling x and keeping y fixed. Connect the picture to Av = λv. Require nonzero input; negative λ can reverse orientation, and zero λ can collapse the vector.

Exercise 3: one minute choose, three minutes explanation/example, two minutes hide the answer and write independently, two minutes check against the material. Keep the paragraph for Exercise 4. Ask where an analogy fails, not only where it sounds appealing.

## Part 4 — interactive visualization directly in chat

**Canvas is not required.** Use the [student guide](interactive-guide.html). Google documents an in-chat visualization feature distinct from writing code in Canvas. In a new ordinary Gemini chat select Pro if offered; start from “help me visualize” plus the concept and one control. Do not begin by requesting HTML, JavaScript, a downloadable file or Canvas Preview: the objective is a usable learning visualization, not a code listing.

```text
Help me visualize how disease prevalence changes the meaning
of a positive test. Show an interactive visualization in this chat,
with a prevalence slider, not an HTML code block.
Use 10,000 fictional people. Keep sensitivity and specificity at 90%.
Show true positives, false positives and PPV as I move the slider.
Ask me to predict what changes from 10% to 1% prevalence.
```

If only text/code appears, try once:

```text
Please show an interactive visualization directly in this conversation.
I want to move a prevalence slider and see the counts change.
Do not give me code or instructions for building an app.
If this chat cannot display an interactive visualization, tell me plainly.
```

For a simpler pre-class capability check:

```text
Help me visualize a pendulum. Show an interactive simulation here with a length slider and a play/pause button.
```

A successful pendulum demo does not guarantee the PPV request will work. A failed request does not by itself identify an account restriction. The prompts are proposed workshop requests; they have not been tested in the lecturer's authenticated account. No prompt can guarantee enabling a feature.

Use the [prepared PPV lab](../demo-materials/medicine/ppv-lab.html) if no usable result appears. Say it is a prepared tool, not a newly generated Gemini result. Students can still predict, change parameters and verify. Do not require buying a plan or moving restricted materials to a private account.

Timing: one minute show how to ask, one minute send request, three minutes operate the available visualization or prepared lab, one minute manual checks, two minutes boundaries/transition. With N=10000 and sensitivity=specificity=90%, prevalence 10% gives 900/(900+900)=50%; prevalence 1% gives 90/(90+990)=8.33%. In the prepared lab, prevalence 0% and specificity 100% gives no positives and PPV undefined. These are expected-count calculations, not patient data or clinical recommendations.

Exercise 4: one minute reopen own paragraph, three minutes evaluate feedback, two minutes revise or reject a suggestion with a reason. Correct work need not be changed.

## Part 5 — check claims

Show the source passage and let students choose A/B before revealing the explanation. The source contains an argument, not a controlled experiment. Distinguish unsupported from false. Check course rules before assessed use. Disclosure must describe the help and checks actually performed.

## Sources and rehearsal boundaries

- [Google, 9 April 2026: interactive simulations directly in Gemini chat](https://blog.google/innovation-and-ai/products/gemini-app/3d-models-charts/): Pro and “show me”/“help me visualize” guidance.
- [Google, 19 August 2026: student tools](https://blog.google/innovation-and-ai/products/gemini-app/student-offer-google-ai/), section 4 and footnote 8: consumer and school-issued accounts. This supersedes the narrower education exclusion in the April launch note; actual availability and limits still require checking.
- [YouTube player parameters](https://developers.google.com/youtube/player_parameters): start/end are playback settings, not authentication workarounds.

Official feature descriptions checked 14 September 2026. Local/CI tests cover the website, layout, copy buttons, timers and numerical examples, not authenticated Gemini/Notebook, YouTube login or campus audio/network. Host policy and school-account behavior must be rehearsed; do not present them as verified by a successful CI run.

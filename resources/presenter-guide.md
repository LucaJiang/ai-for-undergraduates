# Presenter guide

**Wenxin Jiang · 23 September 2026 · Hong Kong**

English/Chinese slides, conversational Mandarin notes, 54 pages. Use the [clock schedule](../schedule.md): the break stays at 15:15, teaching ends at 16:10, and Q&A runs until 16:30.

## Before the room opens

Open the slides, Gemini, the teaching Notebook account, and the two prepared interactive labs. Check the projector and sound. Students should have a computer, a Google account, and relevant course materials, preferably a completed assignment with their own solution. The [public warm-up](../demo-materials/assignment-warmup.html) is available when they need a question.

Prepare three notebooks: A is empty for the import demonstration; B already contains the sources; C has a quiz and a short study-slide output ready. Use the [course-source pack](../materials.html#notebook). Review the actual menus in the account you will use.

Press **V** to set up locally available video files you have permission to use, or rehearse the YouTube links. There are now two clips, 50 seconds in total. See the [media runbook](part0-media.md).

## Opening: from a demo to a familiar question

14:30–14:41, including the four-minute exercise. The first study is a quick contrast; the physics example now has two slides, showing the learning comparison and the tutoring design. The optional GPT Tutor explanation is in [presenter Q&A](../references/part0-evidence.md).

After the two clips, pause on “Impressive demos. What about your next exam?” Say:

“这些演示很精彩，但今天更重要的问题是：它能不能帮你学会明天要考的内容？我们先从一道已经会做的题开始。”

### Demonstration conversation

Open ordinary Gemini chat and paste:

```text
I am studying introductory quantitative reasoning.
A price rises from HK$100 to HK$120. What is the percentage increase?
My solution is (120 - 100) / 100 × 100% = 20%, because the original price is the reference value.
Check my reasoning. If it is correct, say so.
Ask one question to test my understanding, then wait.
```

When asked about the denominator:

```text
I used 100 because percentage change compares the change with the starting price.
Is that explanation clear? Ask me a related question.
```

For the reverse change, from HK$120 to HK$100, let students predict first. The decrease is 20/120, approximately 16.7%.

If the response runs ahead, ask: “Pause here. Ask one question and let me answer.” If its feedback seems wrong, return to the given starting price and calculate together.

Exercise 1, **14:36–14:40**: one minute to choose and paste, two minutes to discuss, one minute to decide whether the feedback makes sense and save the conversation. Debrief at 14:40, then move to tools.

## Part 1: NotebookLM and Deep Research

14:41–14:53. [Official feature guides and prompts](google-study-tools.html).

| Time | Presenter action |
|---|---|
| 14:41 | Start importing sources into A; return to the slides |
| 14:42 | Compare the uses of Gemini, DeepSeek and NotebookLM |
| 14:43 | Show revision formats, check import once, and start a quiz in A or B |
| 14:44 | Demonstrate the available thinking-mode menu |
| 14:45 | Open Google's Deep Research feature tour; explain question, plan, search and report |
| 14:46:30 | Walk through the focused final-project prompt |
| 14:48 | Return to the notebook and open a citation in an answer |
| 14:50 | Let students answer the fixed teaching question, then show the prepared quiz |
| 14:52 | Summarize exam revision versus a final-project search |

Use C whenever it is the most convenient demonstration, saying “这份是我提前准备的。” A full Deep Research run belongs in preparation or follow-up work; a prepared report is useful for showing its structure and source links.

The notebook question asks about sensitivity versus the probability of disease after a positive result. In our teaching source, 90 of 180 positive tests are true positives, giving 50%. This is the 1,000-person source table; Part 4 uses a separate 10,000-person visualization.

## Part 2: improve the first conversation

14:53–15:15. Introduce Role, Context, Constraints and Format as a practical way to explain what help you need. Move between “teach me” and “let me practise”. Connect the examples to current revision and final projects.

Exercise 2, **15:05–15:15**: two minutes to inspect the earlier conversation, four to try an improved request, three to follow up, one to record the difference. Share one example inside the final minute.

Break: **15:15–15:25**. Start the ten-minute timer.

## Part 3: understand, predict, explain

15:25–15:45. Use the eigenvector lab to compare (1,0) and (1,1) when the matrix doubles x and keeps y unchanged. Ask for a prediction before revealing the output. Connect the picture to Av = λv with v nonzero. A negative λ reverses the vector; zero λ sends the output to zero.

Exercise 3, **15:37–15:45**: one minute to choose a concept, three for an explanation and example, two to hide the answer and write independently, two to check and try another case. The final debrief is part of these eight minutes. Students keep their own paragraph for Exercise 4.

## Part 4: interactive exploration and feedback

15:45–15:58. Use ordinary Gemini chat for the visualization request; Canvas is not required. The [interactive guide](interactive-guide.html) contains the request and account-rehearsal details. Ask for a prevalence slider and visible counts. If a usable visualization does not appear after one follow-up, open the [prepared PPV lab](../demo-materials/medicine/ppv-lab.html) and say it is the prepared example.

Have students predict before changing prevalence from 10% to 1%. With 10,000 fictional people and sensitivity = specificity = 90%, the independent calculations are 900/1,800 = 50% and 90/1,080 ≈ 8.3%. The prepared lab also supports the zero-positive-result case, where PPV is undefined.

Exercise 4, **15:52–15:58**: one minute to reopen the paragraph, three to examine feedback alongside the source, two to revise or retain the wording with a reason.

## Part 5: check a concrete claim

15:58–16:03. Reuse the Harvard study rather than introducing a new source. The deliberately overstated sentence is “AI doubles students’ final exam scores.” Ask students which words should change. Then show the routine: open the paper, locate what was measured, and rewrite the summary.

Close with three practical coursework habits: check the assignment instructions, choose suitable materials, and describe the help you received. Use public examples instead of patient, company or classmates' private material.

## Part 6: three questions about AI and opportunity

16:03–16:10. [Evidence and discussion sources](../references/future.html). Keep the seven-minute slot and the full minute of quiet writing. Let students answer before using the right arrow to reveal the prompts. Longer exchanges continue in Q&A.

| Time | Page and facilitation |
|---|---|
| 16:03–16:04 | Timeline, then mathematics: 30 seconds each. Plant the future question about learning mathematics alongside stronger AI. |
| 16:04–16:05:30 | Capabilities: ask what coding, maths and games share; hear one idea; reveal goals, feedback and repeated attempts. |
| 16:05:30–16:07 | Access: ask what a student would need to reproduce a research result; distinguish access, run budget and tools. |
| 16:07–16:09 | Opportunity: invite narrow/widen/both and one reason from two students; reveal both possible mechanisms; ask whether equal accounts mean equal opportunities. |
| 16:09–16:10 | Start the 60-second timer and leave it quiet. Three lines: one learning goal, one AI-assisted task, one needed resource or kind of support. |

### 讲者提问与接话

**能力：**“数学和编程都很难，为什么 AI 在这些地方进步很快？”接住学生的例子，再讲目标、反馈和反复尝试。追加一句：“解出一道题，和选择值得研究的问题，是一回事吗？”不必把任务类型讲成 AI 与人类的永久分界。

**获取：**“新闻里的那个系统，你觉得自己能不能用？”用资料页的 First Proof 实例解释：模型公开，仍要考虑运行费用、时间和配套程序。Google 的个人账号文档则提供一个额度和思考级别的实例。这里讨论门槛，不做套餐推销。

**机会：**“AI 会缩小差距、扩大差距，还是两者都有？”不要预先规定答案。客服研究提供了帮助初学者的实例；经济研究讨论收益如何分配。追问：“学校给大家同样的账号，机会就完全一样了吗？除了账号，还需要什么？”学生可以讨论假设情形，不需要透露家庭收入或个人订阅。

**反思：**“即使 AI 有一天比所有数学家都强，你仍想学懂什么？又需要什么支持？”把专业理解、AI 使用和判断力带回学生自己的目标。喜欢一门学科，也是继续学习的理由。资源差异不全是个人努力的问题；把所需支持写下来，与目标并列。

16:10 进入 Q&A，可邀请学生分享三行中的任意一行。原来的数学学习、优势组合与个人反思已合并进这一收尾，而不是另加三页讲解。

## Q&A and rehearsal record

16:10–16:30 is reserved for questions. Website tests cover layout, links, notes, prompts, timers and the prepared labs. Sign-in, actual AI generation, streamed video, projector sound and venue connectivity are checked during the live rehearsal.

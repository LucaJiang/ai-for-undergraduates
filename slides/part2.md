<!-- .slide: id="part2" class="" -->
<p class="eyebrow">PART 2 · ASK</p>

## Ask clearly about the thing you are learning.

<div class="cards"><div><h3>Role</h3><p>What kind of help? Tutor, examiner, critic, organizer.</p></div><div><h3>Context</h3><p>Course level, source, what you know and where you are stuck.</p></div><div><h3>Constraints</h3><p>What should AI avoid or leave for you to do?</p></div><div><h3>Format</h3><p>A short explanation, table, one hint or one question at a time.</p></div></div><p class="takeaway">Role + Context + Constraints + Format</p><p class="footer">A checklist for useful context — not four mandatory paragraphs.</p>

Note:
0:00–2:00。保留用户原来的RCCF框架。普通问答不是指挥agent操作电脑。简单问题一句话可以问清；Role帮助约定教学姿态，不是准确性保证。

---

<!-- .slide: id="specific-question" class="" -->
<p class="eyebrow">PART 2 · ASK</p>

## Give the missing context, not magic words.

<p class="sub">“Explain logistic regression” is broad. This question names a specific gap.</p><div class="prompt"><pre><code>Role: Act as an introductory statistics tutor.
Context: I know linear regression, but not why logistic
regression uses log-odds.
Constraints: Explain just this connection, not the whole topic.
Format: Use one small numerical example, then ask one
check question. Wait for my answer.</code></pre><button class="copy" type="button">Copy prompt</button></div><p class="footer">Change the subject and your actual knowledge — do not leave the placeholders.</p>

Note:
2:00–3:30。示例不是说短prompt错误。这里只是学习目标更具体。不把log-odds说成二元回归唯一可能link；需要进一步追问时提及probit等可作课后内容。

---

<!-- .slide: id="follow-up" class="" -->
<p class="eyebrow">PART 2 · ASK</p>

## A useful answer can start another question.

<p class="footer">Illustrative teaching dialogue — not a recorded model output</p><div class="dialogue"><p><b>Student:</b> I know sensitivity is 90%. Why is PPV not 90%?</p><p><b>Tutor:</b> In this example, 90 positive tests come from people with disease and 90 from people without it. Which group belongs in the PPV denominator?</p><p><b>Student:</b> Everyone with a positive result: 180 people. So PPV is 90/180 = 50%?</p><p><b>Tutor:</b> Correct for this table. Sensitivity instead uses everyone with disease as the denominator.</p></div><p class="takeaway">“Here is my understanding. Is it correct for this example?”</p>

Note:
3:30–5:30。这是备课对话，不冒充Gemini实测结果。来源为我们提供的1000人教学表。强调不用每次重写整段prompt，告诉AI具体卡在哪儿，再复述自己的理解。也可现场用同一问题，但不要预设它必出错。

---

<!-- .slide: id="two-modes" class="" -->
<p class="eyebrow">PART 2 · ASK</p>

## Choose explanation or practice.

<div class="cards"><div><h3>Explain mode</h3><p>“This is new to me. Explain it and show one worked example.”</p></div><div><h3>Practice mode</h3><p>“Here is my attempt. Give one hint and wait before showing the solution.”</p></div></div><p class="takeaway">First exposure may need teaching.<br>Practice should leave a meaningful step for you.</p>

Note:
5:30–7:00。不要把“保留思考”变成不准学生看完整解释。尚未学习时可以先示范；已经练习时逐步撤掉支持。两种模式都用RCCF。

---

<!-- .slide: id="before-class" class="" -->
<p class="eyebrow">PART 2 · ASK</p>

## Before class: plan from the syllabus.

<div class="sequence"><div><b>Inputs</b><p>Topics, deadlines, current knowledge and available hours.</p></div><div><b>Ask</b><p>What should I review first? Which dependencies are inferred?</p></div><div><b>Check</b><p>Do the dates match? Does the plan fit my actual week?</p></div></div><p class="links"><a href="prompts/index.html" target="_blank" rel="noopener">Prompt library ↗</a></p>

Note:
7:00–9:00。两周计划必须有可用时间和已有基础，缺信息先问，不编造deadline。知识依赖图是建议，课程安排是来源事实，分开标。

---

<!-- .slide: id="after-class" class="" -->
<p class="eyebrow">PART 2 · ASK</p>

## After class: map the ideas, not every slide.

<div class="chips"><span>Definitions</span><span>Mechanisms</span><span>Assumptions</span><span>Consequences</span></div><div class="prompt"><pre><code>Role: Act as a teaching assistant.
Context: Use these lecture notes.
Constraints: Include only supported content; return fewer
items if the notes are short. Label your own suggestions.
Format: Map up to five connected ideas, add source locations,
and ask about one possible confusion.</code></pre><button class="copy" type="button">Copy prompt</button></div><p class="caution">A neat concept map can still contain an unsupported connection.</p>

Note:
9:00–11:00。这里演示材料重组，Notebook也可以做。不强制必须五条，避免AI凑数。学生可沿用之前同一材料。

---

<!-- .slide: id="exam-practice" class="" -->
<p class="eyebrow">PART 2 · ASK</p>

## Before exams: retrieve, then review.

<div class="sequence"><div><b>Close the explanation</b><p>Try a question or explain from memory.</p></div><div><b>Get feedback</b><p>Ask whether the reasoning is correct. Do not demand an error.</p></div><div><b>Re-open the source</b><p>Check the gap, revise, then try again later.</p></div></div><p class="takeaway">Familiarity is not the same test as independent explanation.</p><p class="footer">This is a practice routine, not a promise of a particular grade improvement.</p>

Note:
11:00–13:00。回忆练习适用于已经接触的内容，不能替代初次学习。提醒AI反馈也会错，不能让它必须找错。可用Part1已生成Quiz，但目的不同：Part1展示功能，这里解释如何学习。

---

<!-- .slide: id="exercise1" class="" -->
<p class="eyebrow">PART 2 · ASK</p>

## Exercise 1 · improve one study question.

<p class="sub">Choose: understand · recall · plan · your own course.</p><div class="cards"><div><h3>First</h3><p>Ask with your current prompt. Inspect what is missing.</p></div><div><h3>Then</h3><p>Add useful context or constraints. Ask again.</p></div><div><h3>Leave with</h3><p>Your before/after prompts and one specific change in the answer.</p></div></div><div class="timer" data-seconds="600"><output aria-live="off">10:00</output><button type="button" data-timer="toggle">Start</button><button type="button" data-timer="reset">Reset</button></div><p class="links"><a href="materials.html" target="_blank" rel="noopener">Student materials ↗</a> · <a href="prompts/index.html" target="_blank" rel="noopener">Prompt library ↗</a></p>

Note:
13:00–15:00说明任务；15:05–15:15实际10分钟练习。前2分钟选材料，4分钟比较回答，3分钟追问或修改，最后1分钟记录。不限专业；材料网址页面提供兜底。时间不足缩短讲解，不占用10分钟练习。

---

<!-- .slide: id="exercise1-debrief" class="" -->
<p class="eyebrow">PART 2 · ASK</p>

## What changed — and what did not?

<p class="lead small-lead">“Adding ______ helped the answer ______.”</p><p class="lead small-lead">“I still need to check ______.”</p><p class="takeaway">Save the prompt. Keep the same topic for the next exercise.</p>

Note:
练习最后一分钟，用一个学生结果收束，包含在10分钟内。不要额外加5分钟分享。评价是否解决实际困惑，不是回答变长。

---

<!-- .slide: id="break" class="cover" -->
<p class="eyebrow">PART 2 · ASK</p>

## 10-minute break

<p class="lead">Keep one concept you want to understand better.</p><div class="timer" data-seconds="600"><output aria-live="off">10:00</output><button type="button" data-timer="toggle">Start</button><button type="button" data-timer="reset">Reset</button></div><p class="links"><a href="materials.html" target="_blank" rel="noopener">Student materials ↗</a> · <a href="prompts/index.html" target="_blank" rel="noopener">Prompt library ↗</a></p><p class="footer">Scheduled return: 15:25 HKT</p>

Note:
15:15–15:25。计时器手动开始，切页不会自动重置。不要强迫学生休息时继续操作。返场先看实际时钟，若延迟要从讲解部分回收时间。

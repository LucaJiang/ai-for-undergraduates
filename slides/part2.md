<!-- .slide: id="part2" -->
<p class="eyebrow">PART 2 · ASK</p>

## Help AI understand where you are stuck.

<div class="cards"><div><span class="icon" data-icon="users"></span><h3>Role</h3><p>What help do you need?</p></div><div><span class="icon" data-icon="book"></span><h3>Context</h3><p>What do you already know?</p></div><div><span class="icon" data-icon="target"></span><h3>Constraints</h3><p>What should be left for you?</p></div><div><span class="icon" data-icon="files"></span><h3>Format</h3><p>How should it respond?</p></div></div><p class="takeaway">Role + Context + Constraints + Format</p>

Note:
14:53–14:55。
回想刚才的对话。AI 知道你在学哪门课、懂到哪里吗？这四个词帮我们补齐信息。比如请它当老师，告诉它自己的基础，请它只讲卡住的那一步，最后问一道题。简单问题也可以用一句话说清楚。

---

<!-- .slide: id="specific-question" -->
<p class="eyebrow">PART 2 · ASK</p>

## Name the gap, not just the topic.

<p class="sub">Instead of “Explain logistic regression”…</p><div class="prompt"><pre><code>Role: Act as an introductory statistics tutor.
Context: I know linear regression, but not why logistic
regression uses log-odds.
Constraints: Explain this connection, not the whole topic.
Format: Use one small example, then ask one check question.
Wait for my answer.</code></pre><button class="copy" type="button">Copy prompt</button></div><p class="takeaway">“I understand ______, but I get stuck at ______.”</p>

Note:
14:55–14:57。
“解释逻辑回归”会得到一篇概论。这里先说自己会线性回归，再指出真正不懂的是 log-odds。请同学想一下，自己的课程里能不能也用这个句式：我懂前面这一段，但从这里开始不明白。

---

<!-- .slide: id="follow-up" -->
<p class="eyebrow">PART 2 · ASK</p>

## Show your understanding. Then follow up.

<div class="dialogue"><p><b>Student:</b> Sensitivity is 90%. Why is PPV not 90%?</p><p><b>Tutor:</b> There are 180 positive tests. Which of those people have the disease?</p><p><b>Student:</b> 90 of them. So PPV is 90/180 = 50%?</p><p><b>Tutor:</b> Yes. Sensitivity uses a different denominator: everyone with the disease.</p></div><p class="takeaway">“Here is my understanding. Have I got it right?”</p>

Note:
14:57–14:59。
接着刚才的诊断检测例子，我们把分母说出来。对话最有价值的地方，是学生说出自己的理解，AI 才能针对它回应。换成别的学科也一样：不要只说“还是不懂”，试着指出自己理解到哪一步。
这段对话用于课堂示范，数字来自公开教学表。

---

<!-- .slide: id="two-modes" -->
<p class="eyebrow">PART 2 · ASK</p>

## Do you need teaching or practice?

<div class="cards"><div><span class="icon" data-icon="lightbulb"></span><h3>Teach me</h3><p>“This is new to me.<br>Explain it with a worked example.”</p></div><div><span class="icon" data-icon="pen"></span><h3>Let me practise</h3><p>“Here is my attempt.<br>Give one hint, then let me try.”</p></div></div><p class="takeaway">Change the kind of help as your understanding grows.</p>

Note:
14:59–15:00:30。
没学过的内容，当然可以先看完整解释和例题。已经学过、正在练习，就请它少讲一点，把下一步留给自己。我们不是一直让 AI 问问题，而是根据自己现在的需要来选择。

---

<!-- .slide: id="before-class" -->
<p class="eyebrow">PART 2 · STUDY ROUTINE</p>

## Use your course materials to plan the week.

<div class="pathway"><div><span class="icon" data-icon="files"></span><h3>Bring</h3><p>Syllabus, deadlines and available study time.</p></div><div><span class="icon" data-icon="layers"></span><h3>Organize</h3><p>Connect the topics. Choose what to review first.</p></div><div><span class="icon" data-icon="check"></span><h3>Adjust</h3><p>Fit the plan to your actual week.</p></div></div><p class="dialogue compact">“I have three hours this week. Which two topics should I review first, and why?”</p><p class="links"><a href="prompts/index.html" target="_blank" rel="noopener">Planning and concept-map prompts ↗</a></p>

Note:
15:00:30–15:02。
AI 可以帮你把一堆材料整理成计划。先给它真实的考试日期、课程范围和空闲时间。计划出来以后，自己再看看：它有没有漏掉老师强调的部分？这周真的做得完吗？上完课也可以让它把几份讲义里重复出现的概念连起来。

---

<!-- .slide: id="exam-practice" -->
<p class="eyebrow">PART 2 · EXAM PREPARATION</p>

## Close the answer. Try it yourself.

<div class="pathway"><div><span class="icon" data-icon="book"></span><h3>Recall</h3><p>Hide the explanation. Answer from memory.</p></div><div><span class="icon" data-icon="chat"></span><h3>Get feedback</h3><p>Show your reasoning and ask about the gap.</p></div><div><span class="icon" data-icon="pen"></span><h3>Try again</h3><p>Review the source. Solve a new question.</p></div></div><p class="takeaway">“That looks familiar” → “I can explain it.”</p>

Note:
15:02–15:04。
看答案时觉得懂，和考试时自己写出来，是两种体验。可以请 AI 出一道相近但不同的题，先独立回答，再读反馈。下一轮再换个例子，看看自己能不能用上同一个概念。

---

<!-- .slide: id="exercise1" -->
<p class="eyebrow">PART 2 · TRY</p>

## Exercise 2 · improve your conversation.

<div class="cards"><div><span class="icon" data-icon="search"></span><h3>Find the gap</h3><p>Reopen your first conversation.</p></div><div><span class="icon" data-icon="pen"></span><h3>Ask again</h3><p>Add the missing context or change the help.</p></div><div><span class="icon" data-icon="check"></span><h3>Compare</h3><p>What became more useful?</p></div></div><div class="timer" data-seconds="600"><output aria-live="off">10:00</output><button type="button" data-timer="toggle">Start</button><button type="button" data-timer="reset">Reset</button></div><p class="footer">Keep your before/after prompts and one change in the answer. <a href="prompts/index.html" target="_blank" rel="noopener">Prompt library ↗</a></p>

Note:
15:04–15:05说明；15:05–15:15练习。
请回到第一段对话。选一个最想改进的地方：解释太宽、没有回应你的思路，或者一下把答案全给了。修改问题后再问一次，比较前后差别。
2分钟找问题，4分钟测试，3分钟追问，最后1分钟记录一句话：“补充了什么以后，回答有什么变化？”分享也放在最后一分钟。15:15准时休息。

---

<!-- .slide: id="break" class="cover" -->
<p class="eyebrow">TAKE A BREAK</p>

## 10-minute break

<p class="lead">We return at 15:25.</p><div class="timer" data-seconds="600"><output aria-live="off">10:00</output><button type="button" data-timer="toggle">Start</button><button type="button" data-timer="reset">Reset</button></div><p class="links"><a href="materials.html" target="_blank" rel="noopener">Student materials ↗</a> · <a href="prompts/index.html" target="_blank" rel="noopener">Prompt library ↗</a></p>

Note:
15:15–15:25。
大家休息十分钟，15:25回来。回来以后，我们继续用自己的课程材料，尝试弄懂一个难点。现在可以先放下电脑，活动一下。
操作：手动启动计时器。

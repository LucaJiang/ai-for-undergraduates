<!-- Part 2: Universal Study Workflow & Prompt Design -->

<section class="part2-title" data-background-gradient="linear-gradient(135deg, #0f172a, #14532d 55%, #0e7490)">
  <p class="eyebrow">Part 2 · Universal study workflow</p>
  <h1>Turn questions into learning conversations.</h1>
  <p class="subtitle">Prompting is not about magic words. It is about designing how you think with AI.</p>
  <aside class="notes">普通话讲解。这里承接 Part 1：刚才讲了选工具和选思考强度，现在讲如何把 AI 放进真实学习流程。强调：对本科生来说，prompt 的目标不是让 AI 直接完成作业，而是让 AI 更准确地理解你要学什么、你已经知道什么、你不希望它替你做什么。</aside>
</section>

---

<section>
  <h2>Two different ways to prompt AI</h2>
  <div class="mode-compare">
    <div class="mode-card primary">
      <p class="mode-label">Q&A / study conversation</p>
      <h3>Role + Context + Constraints + Format</h3>
      <p>Best for asking, explaining, tutoring, checking understanding, and discussing coursework.</p>
    </div>
    <div class="mode-card muted">
      <p class="mode-label">Action / agentic workflow</p>
      <h3>Goal + Inputs + Steps + Boundaries + Checks</h3>
      <p>Best for asking AI to operate tools, handle files, run code, or complete multi-step tasks.</p>
    </div>
  </div>
  <p class="takeaway">For this workshop, start with the Q&A frame. It keeps the learning conversation under your control.</p>
  <aside class="notes">这里按你的修正处理：本科生日常和 AI 讨论功课，最应该先学 Role + Context + Constraints + Format。行动式 prompt 是以后操作电脑、调用工具、数据分析时用的。今天重点不是把任务外包给 AI。</aside>
</section>

---

<section>
  <h2>The default study prompt frame</h2>
  <div class="rccf-grid">
    <div><strong>Role</strong><span>Who should AI be?</span><p>A tutor, examiner, critic, study partner, language editor...</p></div>
    <div><strong>Context</strong><span>What does AI need to know?</span><p>Course level, topic, your current understanding, source material...</p></div>
    <div><strong>Constraints</strong><span>What should AI not do?</span><p>Do not solve directly. Do not reveal answers. Use only my notes...</p></div>
    <div><strong>Format</strong><span>How should the answer look?</span><p>One question at a time, table, concept map, checklist, bilingual glossary...</p></div>
  </div>
  <aside class="notes">把四个部分讲得非常具体。Role 不是摆设，它决定交互姿态；Context 减少误解；Constraints 是学术诚信和保留思考空间的核心；Format 让输出更容易被使用。</aside>
</section>

---

<section>
  <h2>Bad prompt → study prompt</h2>
  <div class="prompt-compare part2-prompt-compare">
    <div class="prompt bad">
      <h3>Weak</h3>
      <pre><code>Explain logistic regression.</code></pre>
    </div>
    <div class="prompt good">
      <h3>Better for learning</h3>
      <pre><code>Role: Act as an introductory statistics tutor.

Context: I understand linear regression, but I do not
understand why logistic regression uses log-odds.

Constraints: Do not explain the whole topic at once.
Do not give me a final exam-style answer.

Format: Start from my gap. Use one numerical example.
Then ask me one question to check whether I understand
why predicted probabilities must stay between 0 and 1.</code></pre>
      <button class="copy" data-copy="Role: Act as an introductory statistics tutor.\n\nContext: I understand linear regression, but I do not understand why logistic regression uses log-odds.\n\nConstraints: Do not explain the whole topic at once. Do not give me a final exam-style answer.\n\nFormat: Start from my gap. Use one numerical example. Then ask me one question to check whether I understand why predicted probabilities must stay between 0 and 1.">Copy prompt</button>
    </div>
  </div>
  <aside class="notes">这一页要讲清楚：这不是复杂化 prompt，而是把学生脑子里隐含的信息显性化。AI 不知道你是大一学生还是研究生，也不知道你已经懂什么。写出来以后，回答会更像 tutoring，而不是百科全书。</aside>
</section>

---

<section>
  <h2>What changes when the prompt is better?</h2>
  <div class="before-after-row">
    <div>
      <h3>Weak prompt</h3>
      <ul>
        <li>Broad summary</li>
        <li>Too much at once</li>
        <li>No diagnosis of your gap</li>
        <li>Easy to read passively</li>
      </ul>
    </div>
    <div>
      <h3>Study prompt</h3>
      <ul>
        <li>Starts from your level</li>
        <li>Protects your thinking</li>
        <li>Creates a next step</li>
        <li>Forces active recall</li>
      </ul>
    </div>
  </div>
  <p class="takeaway">A good study prompt does not just improve the answer. It improves the learning interaction.</p>
  <aside class="notes">这里强调与 Part 0 呼应：prompt 的约束是为了防止 cognitive crutch。Format 的重点也不是漂亮，而是迫使学生下一步思考。</aside>
</section>

---

<section>
  <h2>Workflow A: before class</h2>
  <p class="bigline">Syllabus → dependency map → preparation plan</p>
  <div class="workflow-strip">
    <span>Syllabus</span><span>Prerequisites</span><span>Topic dependencies</span><span>2-week plan</span>
  </div>
  <div class="prompt wide-prompt">
    <pre><code>Role: Act as a study planner for an undergraduate course.
Context: I will paste a course syllabus and assessment schedule.
Constraints: Do not only make a calendar. Identify conceptual dependencies.
Format: Give me (1) what to review first, (2) what depends on what,
(3) a realistic plan for the next two weeks.</code></pre>
  </div>
  <aside class="notes">这部分对应原大纲的 reverse syllabus breakdown，但改成更偏学习结构，而不是简单时间表。很多学生拿到 syllabus 只看 deadline，不看概念依赖。</aside>
</section>

---

<section>
  <h2>Workflow B: after class</h2>
  <p class="bigline">Slides → concept map → confusion list</p>
  <div class="concept-map-demo">
    <div>Definitions</div><div>Mechanisms</div><div>Assumptions</div><div>Consequences</div><div>Common confusions</div>
  </div>
  <div class="prompt wide-prompt">
    <pre><code>Role: Act as a teaching assistant.
Context: These are my lecture slides/notes.
Constraints: Do not just summarize slide by slide.
Format: Extract the 5 core concepts, show how they connect,
mark each as definition / mechanism / assumption / consequence,
and identify 3 points students often misunderstand.</code></pre>
  </div>
  <aside class="notes">这里让学生明白：AI 对课程资料最有价值的用法之一是重组结构，而不是压缩成摘要。Notebook 或 Gemini 都可以用。</aside>
</section>

---

<section>
  <h2>Workflow C: before exams</h2>
  <p class="bigline">Recall first. Review second.</p>
  <div class="recall-compare">
    <div class="path bad"><h3>Passive review</h3><ol><li>Open notes</li><li>Read summary</li><li>Feel familiar</li><li>Forget in exam</li></ol></div>
    <div class="path good"><h3>Active recall</h3><ol><li>Close notes</li><li>Explain from memory</li><li>AI finds gaps</li><li>Review weak points</li></ol></div>
  </div>
  <aside class="notes">考试复习中最常见错误是先看答案，再觉得自己会了。这里让 AI 成为 examiner，而不是 summary machine。</aside>
</section>

---

<section>
  <h2>Make AI test you, not just teach you.</h2>
  <div class="prompt wide-prompt">
    <pre><code>Role: Act as an examiner and tutor.
Context: I am reviewing [topic] for [course level].
Constraints: Do not show the answer first. Ask one question at a time.
If I am wrong, do not reveal the full answer immediately.
Format: Start with a conceptual question. Wait for my answer.
Then identify the flaw in my reasoning and give one hint.</code></pre>
    <button class="copy" data-copy="Role: Act as an examiner and tutor.\n\nContext: I am reviewing [topic] for [course level].\n\nConstraints: Do not show the answer first. Ask one question at a time. If I am wrong, do not reveal the full answer immediately.\n\nFormat: Start with a conceptual question. Wait for my answer. Then identify the flaw in my reasoning and give one hint.">Copy prompt</button>
  </div>
  <p class="takeaway">The important move: ask AI to wait.</p>
  <aside class="notes">“Wait for my answer” 是很关键的句子。它让学生不要直接进入读答案状态，而是先 retrieval，再 feedback。</aside>
</section>

---

<section>
  <h2>Five useful AI roles for studying</h2>
  <div class="role-grid">
    <div><strong>Explainer</strong><span>Explain this another way.</span></div>
    <div><strong>Tutor</strong><span>Give me one hint.</span></div>
    <div><strong>Examiner</strong><span>Quiz me without answers first.</span></div>
    <div><strong>Critic</strong><span>Find the flaw in my explanation.</span></div>
    <div><strong>Organizer</strong><span>Turn notes into a concept map.</span></div>
  </div>
  <p class="takeaway muted-takeaway">“Answer machine” is only one role — and often the least useful one for learning.</p>
  <aside class="notes">为后面 Part 3、Exercise 3 埋伏笔：困难概念时用 tutor，自己的解释时用 critic。这里不展开太久。</aside>
</section>

---

<section>
  <h2>Exercise 1: build your own study loop</h2>
  <p class="bigline">10 minutes · choose one track</p>
  <div class="exercise-tracks">
    <div><strong>A · Understand</strong><span>Use one lecture slide or note page you find confusing.</span></div>
    <div><strong>B · Recall</strong><span>Ask AI to quiz you one question at a time.</span></div>
    <div><strong>C · Plan</strong><span>Use a syllabus to find dependencies and review priorities.</span></div>
    <div><strong>D · Bring your own</strong><span>Use something from your real course.</span></div>
  </div>
  <aside class="notes">Exercise 时间：前 2 分钟选择材料，2–6 分钟跑第一版 prompt，6 分钟提醒大家加入 constraints 和 wait-for-me，6–9 分钟重试，最后 1 分钟问一两个学生：prompt 改了以后有什么变化？</aside>
</section>

---

<section>
  <h2>Copy this scaffold</h2>
  <div class="prompt wide-prompt">
    <pre><code>Role: Act as a [tutor / examiner / critic / organizer].

Context: I am learning [topic] for [course].
I already understand [what I know].
I find [specific point] difficult.

Constraints: Do not [give the final answer / reveal answers first /
write my assignment for me / use sources outside my notes].

Format: Please respond as [one hint / concept map / table /
one question at a time / bilingual glossary].</code></pre>
    <button class="copy" data-copy="Role: Act as a [tutor / examiner / critic / organizer].\n\nContext: I am learning [topic] for [course]. I already understand [what I know]. I find [specific point] difficult.\n\nConstraints: Do not [give the final answer / reveal answers first / write my assignment for me / use sources outside my notes].\n\nFormat: Please respond as [one hint / concept map / table / one question at a time / bilingual glossary].">Copy prompt</button>
  </div>
  <p class="template-link">More templates: <code>prompts/undergraduate-study-prompts.md</code></p>
  <aside class="notes">这页让学生真正开始操作。强调：空格要填具体，不要只复制模板不改。</aside>
</section>

---

<section>
  <h2>After AI answers, do not stop there.</h2>
  <div class="loop-large">
    <div><span>1</span><strong>Try</strong><p>What do I already think?</p></div>
    <div><span>2</span><strong>Ask</strong><p>Use Role + Context + Constraints + Format.</p></div>
    <div><span>3</span><strong>Recall</strong><p>Explain it without looking.</p></div>
    <div><span>4</span><strong>Feedback</strong><p>Ask AI to find gaps.</p></div>
    <div><span>5</span><strong>Verify</strong><p>Check against course sources.</p></div>
  </div>
  <p class="takeaway">The best AI workflow repeatedly gives the thinking back to you.</p>
  <aside class="notes">这页用于 Exercise 后收束。如果时间紧，可以直接作为练习前说明，也可以练习后回来总结。</aside>
</section>

---

<section class="break-slide" data-background-gradient="linear-gradient(135deg, #020617, #0f172a 55%, #064e3b)">
  <p class="eyebrow">10-minute break</p>
  <h2>Before you leave your laptop:</h2>
  <ol>
    <li>Save one useful prompt you just tested.</li>
    <li>Keep one AI answer you want to verify later.</li>
    <li>Come back with one hard concept for Part 3.</li>
  </ol>
  <aside class="notes">休息前提醒：回来之后 Part 3 要处理困难概念。让学生带着刚刚 Exercise 中的问题回来。</aside>
</section>

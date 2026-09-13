<!-- Part 4: Beyond chat -->

<section class="part-title part4-title">
  <p class="eyebrow">Part 4 · 15:48–15:56</p>
  <h1>Beyond chat</h1>
  <p class="subtitle">Use AI to build learning environments, not black boxes.</p>
</section>

Note:
普通话讲解。Part 4 的重点不是炫耀 agent 或代码能力，而是让学生看到：AI 不只是聊天框，它可以成为 notebook、代码实验室、资料整理器和工作流助手。但越高级的自动化越需要边界。

---

<section>
  <h2>Chat is only one interface.</h2>
  <div class="part4-interface-grid">
    <div><span>Chat</span><strong>Ask and respond</strong><small>Fast clarification, tutoring, critique</small></div>
    <div><span>Notebook</span><strong>Ground in sources</strong><small>Lecture notes, readings, quizzes, study guides</small></div>
    <div><span>Code</span><strong>Make ideas executable</strong><small>Simulations, plots, debugging, examples</small></div>
    <div><span>Agent</span><strong>Coordinate steps</strong><small>Search, compare, organize, draft workflows</small></div>
  </div>
  <p class="takeaway">The interface changes what the AI is good for.</p>
</section>

Note:
告诉学生：我们前面主要是 chat。但高级使用不是换一个“更聪明的聊天框”，而是把任务放进合适的界面里。Notebook 适合有资料的学习；代码适合理解可以形式化的概念；agent 适合多步骤、低风险、可检查的流程。

---

<section>
  <h2>Use a notebook when the source matters.</h2>
  <div class="part4-flow wide">
    <span>Lecture notes</span>
    <span>+</span>
    <span>Readings</span>
    <span>+</span>
    <span>Slides</span>
    <strong>→</strong>
    <span>Source-grounded study</span>
  </div>
  <div class="part4-output-grid">
    <div>Concept map</div>
    <div>Quiz</div>
    <div>Flashcards</div>
    <div>Study guide</div>
    <div>Audio / video overview</div>
    <div>Source-linked answers</div>
  </div>
  <p class="takeaway">Notebook tools are best when you want AI to stay close to your course materials.</p>
</section>

Note:
接 Part 1 的 Notebook demo。这里强调“source matters”：比如老师 slide、指定 reading、syllabus。Notebook 的价值不是永远更准确，而是回答可以追溯到你给它的材料。提醒：即使 source-grounded，也要看 citation 是否真的支持回答。

---

<section>
  <h2>Use code when an idea can be tested.</h2>
  <div class="part4-code-layout">
    <div>
      <p class="bigline">Good learning use:</p>
      <ul>
        <li>simulate a small example</li>
        <li>plot how a parameter changes behavior</li>
        <li>debug your reasoning step by step</li>
        <li>compare intuition with output</li>
      </ul>
    </div>
    <div class="part4-code-card">
      <pre><code>Concept → toy model → plot → explain</code></pre>
      <p>Code should make your thinking visible.</p>
    </div>
  </div>
</section>

Note:
对 STEM 和商科学生特别有用。代码不是为了替学生直接完成数据分析报告，而是让概念可视化。比如 logistic curve、Bayes rule、price elasticity、random sampling、compound interest。重点是 toy example，不是真实作业数据直接丢给 AI 写结果。

---

<section>
  <h2>Prompt: make a concept executable</h2>
  <div class="prompt good full-width-prompt">
<pre><code>I am learning [concept].

Role: Act as a tutor who uses tiny simulations to teach.
Context: I know [what I already know], but I am confused about [gap].
Constraints:
- Use a minimal toy example, not a full assignment solution.
- Explain every assumption.
- After the code, ask me what I think the output means before you interpret it.
Format:
1. Intuition
2. 15-line code example
3. Plot or table
4. One question for me</code></pre>
<button class="copy" data-copy="I am learning [concept].\n\nRole: Act as a tutor who uses tiny simulations to teach.\nContext: I know [what I already know], but I am confused about [gap].\nConstraints:\n- Use a minimal toy example, not a full assignment solution.\n- Explain every assumption.\n- After the code, ask me what I think the output means before you interpret it.\nFormat:\n1. Intuition\n2. 15-line code example\n3. Plot or table\n4. One question for me">Copy prompt</button>
  </div>
</section>

Note:
这里仍然沿用学生已经学过的 Role + Context + Constraints + Format。强调这个 prompt 的边界：minimal toy example，不是 full assignment solution；先让学生解释输出，再让 AI 解释。

---

<section>
  <h2>Use agents carefully.</h2>
  <div class="part4-ladder">
    <div class="safe"><strong>Low risk</strong><span>collect links, organize notes, make checklist</span></div>
    <div class="middle"><strong>Reversible</strong><span>rename files, format tables, draft study plans</span></div>
    <div class="danger"><strong>High risk</strong><span>submit work, email others, change data, make decisions</span></div>
  </div>
  <p class="takeaway">Delegate tasks only when you can inspect, reverse, and take responsibility for the result.</p>
</section>

Note:
如果学生听过 agents 或 computer use，这里给一个简单安全框架。强调：可以让 AI 整理资料、比较信息、做 checklist；但不应该让它直接提交作业、发送重要邮件、改动真实数据，尤其是你没有检查的时候。

---

<section>
  <h2>A better advanced workflow</h2>
  <div class="part4-workflow">
    <div>Question</div>
    <span>→</span>
    <div>Sources</div>
    <span>→</span>
    <div>Notebook</div>
    <span>→</span>
    <div>Toy model</div>
    <span>→</span>
    <div>My explanation</div>
    <span>→</span>
    <div>AI critique</div>
  </div>
  <p class="takeaway">Advanced AI should make your reasoning more traceable, not more hidden.</p>
</section>

Note:
这个 workflow 串起前几部分。以医学/统计例子讲：先问“为什么低患病率下阳性预测值低？”导入资料到 Notebook，生成 quiz，再用代码 toy example 计算 2x2 table，最后学生自己解释，AI critique。

---

<section>
  <h2>Exercise 3: make AI critique you</h2>
  <p class="bigline">6 minutes · choose one concept you just studied</p>
  <div class="exercise-grid">
    <div><strong>1 min</strong><span>Write your own explanation first.</span></div>
    <div><strong>3 min</strong><span>Ask AI to critique it, not rewrite it.</span></div>
    <div><strong>2 min</strong><span>Revise your explanation.</span></div>
  </div>
  <p class="takeaway">If AI only talks, you may feel smarter. If AI critiques you, you can become smarter.</p>
</section>

Note:
这是全场最重要的练习之一。让学生打开 Gemini/DeepSeek 或 Notebook，先写自己的解释，不要直接问 AI 解释。提醒他们：输入可以很短，一段 4–6 句就可以。

---

<section>
  <h2>Critique prompt</h2>
  <div class="prompt good full-width-prompt">
<pre><code>Here is my explanation of [concept]:

[Paste my explanation]

Do not rewrite it yet.

1. Identify anything incorrect or imprecise.
2. Identify one important idea I missed.
3. Ask me one question that would reveal whether I truly understand it.
4. After I answer, help me revise my explanation.</code></pre>
<button class="copy" data-copy="Here is my explanation of [concept]:\n\n[Paste my explanation]\n\nDo not rewrite it yet.\n\n1. Identify anything incorrect or imprecise.\n2. Identify one important idea I missed.\n3. Ask me one question that would reveal whether I truly understand it.\n4. After I answer, help me revise my explanation.">Copy prompt</button>
  </div>
</section>

Note:
这页可以让学生直接复制。强调“Do not rewrite it yet”。如果 AI 一上来重写，会让学生再次变成被动读者。真正的学习发生在 critique 和 revision。

---

<section>
  <h2>Part 4 takeaway</h2>
  <blockquote>Use advanced AI to expose your reasoning — not to hide it.</blockquote>
  <div class="part4-checks">
    <span>Can I inspect the sources?</span>
    <span>Can I explain the code?</span>
    <span>Can I reverse the action?</span>
    <span>Can I take responsibility?</span>
  </div>
  <p class="next">Next: verification, privacy, and academic integrity.</p>
</section>

Note:
Part 4 收束。把 Part 5 引出来：如果 AI 能搜资料、写代码、执行行动，那我们更需要验证、隐私和学术诚信边界。

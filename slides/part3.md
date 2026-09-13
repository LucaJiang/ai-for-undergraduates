# Part 3
## Learn difficult concepts with AI

<p class="part3-subtitle">Use AI as a tutor, visualizer, and debugging partner — not as a solution manual.</p>

<div class="part3-route">
  <span>Intuition</span>
  <span>Formalism</span>
  <span>Example</span>
  <span>Self-check</span>
</div>

Note:
休息回来之后先重新定调。Part 3 不是教学生问 AI 要完整答案，而是教他们遇到抽象概念、证明、公式、机制时如何让 AI 拆解学习过程。这里承接 Part 2 的 prompt 结构，但场景换成“难概念”。

---

## Hard concepts are often hard for a specific reason.

<div class="hard-reasons">
  <div><strong>Missing prerequisite</strong><p>You do not yet know the idea the new concept depends on.</p></div>
  <div><strong>Representation gap</strong><p>The formula, diagram, and verbal explanation do not yet connect.</p></div>
  <div><strong>No feedback loop</strong><p>You think you understand it, but you have not tested that understanding.</p></div>
</div>

<p class="part3-takeaway">Ask AI to diagnose the obstacle before asking it to explain everything.</p>

Note:
很多学生觉得“我就是笨”或者“这个概念太难”，其实常常是三种具体问题：前置知识缺口、表示方式没有连起来、没有反馈。AI 最有价值的是帮助定位是哪一种，而不是立刻输出一大段百科式解释。

---

## A better concept-learning prompt has layers.

<div class="concept-layers">
  <div><span>1</span><strong>Intuition</strong><p>What is the idea doing?</p></div>
  <div><span>2</span><strong>Formal definition</strong><p>What does the notation mean?</p></div>
  <div><span>3</span><strong>Worked example</strong><p>How does it behave in a concrete case?</p></div>
  <div><span>4</span><strong>Self-check</strong><p>Can I explain or apply it myself?</p></div>
</div>

Note:
这里可以强调：对于复杂概念，不要让 AI 一次性“全面解释”。好的学习顺序是先建立直觉，再映射到符号，再看例子，最后检查自己是否能说出来。

---

## Example: eigenvectors are not just a formula.

<div class="eigen-demo">
  <div class="formula-card">
    <span>Formal</span>
    <strong>A v = λ v</strong>
  </div>
  <div class="meaning-card">
    <span>Intuition</span>
    <p>Some directions survive a transformation: they may stretch, shrink, or flip, but they do not rotate into a new direction.</p>
  </div>
</div>

<p class="part3-takeaway">The goal is to connect symbol, geometry, and computation.</p>

Note:
现场主 demo 可以用 eigenvector，因为它非常适合从公式走到图像再到 Python。讲的时候不要证明特征值分解，只讲“某些方向在变换后仍然沿着原方向”。

---

## Same question, better prompt structure

<div class="part3-prompt-compare">
  <div class="weak"><h3>Weak</h3><pre><code>Explain eigenvectors.</code></pre></div>
  <div class="strong"><h3>Learning prompt</h3><pre><code>Role: Act as a patient linear algebra tutor.

Context: I know matrix-vector multiplication, but I do not understand the geometric meaning of eigenvectors.

Constraints: Do not start with a formal proof. Explain the intuition first, then connect it to A v = λ v. Use one 2D example.

Format: Give me a short explanation, one diagram description, and one self-check question. Do not reveal the answer until I try.</code></pre></div>
</div>

Note:
这里回应你前面强调的结构：问答型学习 prompt 还是 Role + Context + Constraints + Format。这里不是指挥 agent 操作电脑，而是让 AI 以明确身份、背景、限制和输出格式回答学习问题。

---

## Make AI Socratic, not a solution manual.

<div class="socratic-flow">
  <span>My attempt</span>
  <span>One hint</span>
  <span>Guiding question</span>
  <span>My revision</span>
  <span>Feedback</span>
</div>

<pre class="compact-prompt"><code>I am working on this problem. Do not solve it for me.

First, identify what kind of problem this is.
Then give only one hint for the next step.
Ask me a question that forces me to decide what to do next.
Wait for my answer before continuing.</code></pre>

Note:
这页非常重要。要明确说：如果这是作业题，不要让 AI 直接写答案。你可以让它判断题型、给第一步提示、问引导问题。这能保留学生自己的思考空间，也更符合学术规范。

---

## Use multiple representations.

<div class="representations">
  <div><strong>Words</strong><p>Explain the intuition.</p></div>
  <div><strong>Symbols</strong><p>Map each term in the formula.</p></div>
  <div><strong>Diagram</strong><p>Describe what I should draw.</p></div>
  <div><strong>Numbers</strong><p>Give a small worked example.</p></div>
  <div><strong>Code</strong><p>Simulate or visualize it.</p></div>
</div>

<p class="part3-takeaway">When one representation fails, switch representation.</p>

Note:
很多学生卡住不是因为不努力，而是一直停留在同一种表示。比如只看公式不看图，只看文字不算例子。AI 很适合快速切换表示方式。

---

## Coding can become a microscope for abstract ideas.

<div class="code-learning">
  <div>
    <h3>Good use</h3>
    <p>Ask AI to create a minimal simulation or visualization, then change parameters and observe what happens.</p>
  </div>
  <div>
    <h3>Risky use</h3>
    <p>Ask AI to write the full assignment or analysis report while you only read the final output.</p>
  </div>
</div>

<p class="part3-link">Example script: <a href="examples/linear-transform-visualization.py" target="_blank">linear-transform-visualization.py ↗</a></p>

Note:
这里可以现场打开脚本，也可以只展示链接。重点不是“AI 会写代码”，而是代码可以帮助观察概念。对于 STEM 学生很有用；商科和医学也可以用小模拟理解阈值、概率、增长率等。

---

## This works beyond mathematics.

<div class="discipline-menu">
  <div><span>STEM</span><strong>Eigenvectors</strong><small>What direction survives a transformation?</small></div>
  <div><span>Medicine</span><strong>Sensitivity vs PPV</strong><small>Why does prevalence change interpretation?</small></div>
  <div><span>Business</span><strong>Marginal effect</strong><small>What changes when one input changes?</small></div>
  <div><span>Humanities</span><strong>Argument structure</strong><small>What is the claim, evidence, and assumption?</small></div>
</div>

Note:
提醒学生 Part 3 不只是数学。线代只是现场示范最方便。真正练习时他们应该拿自己的专业概念来试。

---

## Exercise 2 · Choose a hard concept

<p class="exercise-time">8 minutes</p>

<div class="exercise-steps">
  <div><strong>1 min</strong><p>Choose one concept you recently struggled with.</p></div>
  <div><strong>3 min</strong><p>Ask AI for intuition → formalism → example.</p></div>
  <div><strong>2 min</strong><p>Ask for one self-check question.</p></div>
  <div><strong>2 min</strong><p>Explain your answer back and get feedback.</p></div>
</div>

Note:
这段练习时间控制在 8 分钟。让学生自由选择概念。如果有人不知道选什么，就从 slide 上四个学科入口选一个。你可以在教室里走动，提醒他们不要只读解释，一定要让 AI 问他们问题。

---

## Copy this prompt

<pre class="exercise-prompt"><code>Role: Act as a patient tutor in [subject].

Context: I am trying to understand [concept]. I already know [what I know], but I am confused about [specific difficulty].

Constraints: Do not give a long textbook-style explanation. Start with intuition, then connect it to the formal definition. Do not solve my assignment for me.

Format:
1. One intuitive analogy
2. One formal explanation
3. One small worked example
4. One common misconception
5. One self-check question

After I answer the self-check question, critique my reasoning.</code></pre>

<button class="copy" data-copy="Role: Act as a patient tutor in [subject].&#10;&#10;Context: I am trying to understand [concept]. I already know [what I know], but I am confused about [specific difficulty].&#10;&#10;Constraints: Do not give a long textbook-style explanation. Start with intuition, then connect it to the formal definition. Do not solve my assignment for me.&#10;&#10;Format:&#10;1. One intuitive analogy&#10;2. One formal explanation&#10;3. One small worked example&#10;4. One common misconception&#10;5. One self-check question&#10;&#10;After I answer the self-check question, critique my reasoning.">Copy prompt</button>

Note:
这页让学生直接复制。强调他们要填自己的 subject/concept/known/confused，而不是原封不动粘贴。最后一句“critique my reasoning”很关键，它把 AI 从 answer generator 改成 feedback partner。

---

## Debrief

<div class="debrief-questions">
  <h3>Ask yourself:</h3>
  <p>Did AI explain the concept, or did it help me test my understanding?</p>
  <p>Can I now explain the idea without looking at the answer?</p>
  <p>What would I verify before using this in homework or an exam?</p>
</div>

<p class="next">Next: beyond chat — notebooks, data, code, and larger projects.</p>

Note:
练习结束以后收束：不需要每个人分享。可以问 1–2 个学生：你们的 prompt 改了以后有什么区别？最后转入 Part 4，说明下一部分会展示更复杂的工作流，但底线还是不外包思考。

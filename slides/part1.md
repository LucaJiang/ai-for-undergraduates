<!-- .slide: data-background-gradient="linear-gradient(135deg, #0f172a, #172554 58%, #312e81)" -->
<p class="eyebrow">Part 1 · 10 minutes</p>

# Choose the tool. Choose how much it should think.

<p class="subtitle">Don't start with a model name. Start with the task.</p>

<p class="takeaway">Two choices matter more than any leaderboard.</p>

Note:
普通话讲解。Part 1 大约 10 分钟，并包含一次 Gemini Notebook 现场演示。核心不是告诉学生“哪个模型最好”，而是让他们以后面对新模型也会自己选择。先问两个问题：知识应该从哪里来？这个任务值得多少思考？

---

## Two decisions before you type

<div class="decision-grid">
  <div class="decision-card">
    <span>01 · KNOWLEDGE</span>
    <strong>Where should the answer come from?</strong>
    <p>My lecture notes and readings — or the open world?</p>
  </div>
  <div class="decision-card">
    <span>02 · REASONING</span>
    <strong>How hard should the model think?</strong>
    <p>Routine transformation — or multi-step reasoning?</p>
  </div>
</div>

<p class="takeaway">Tool choice and reasoning effort are separate decisions.</p>

Note:
先把“选工具”和“选思考强度”拆开。学生很容易只问“Gemini 还是 DeepSeek”，但其实同一个模型内部也可能有不同 reasoning effort，而 Notebook 又是另一种 source-grounded 工作流。

---

## Three useful starting points

<div class="tool-grid">
  <div class="tool-card">
    <span>GENERAL</span>
    <strong>Gemini</strong>
    <p>Broad questions, multimodal inputs, everyday study tasks.</p>
    <small>Good default for this workshop.</small>
  </div>
  <div class="tool-card">
    <span>ALTERNATIVE</span>
    <strong>DeepSeek</strong>
    <p>Another reasoning style, a second opinion, or a backup when usage limits matter.</p>
    <small>Compare — don't assume.</small>
  </div>
  <div class="tool-card featured">
    <span>YOUR SOURCES</span>
    <strong>Gemini Notebook</strong>
    <p>Study a defined set of lectures, readings, PDFs and links with source grounding.</p>
    <small>Formerly NotebookLM.</small>
  </div>
</div>

<p class="takeaway">These are starting points, not rankings.</p>

Note:
学校已经提供 Gemini Notebook（原 NotebookLM），所以现场可以直接用学校账户。强调 Gemini 与 DeepSeek 不是第一名第二名；DeepSeek 的价值包括额度备选、不同解释风格和 second opinion。Notebook 的区别是“我希望答案主要来自我指定的课程资料”。

---

<!-- .slide: class="live-demo-slide" -->
<p class="eyebrow">LIVE DEMO · START IT NOW</p>

## Give Gemini Notebook something real to study

<div class="live-demo-card">
  <ol>
    <li>Create a new notebook.</li>
    <li>Add 2–3 course sources.</li>
    <li>Ask one source-grounded question.</li>
    <li>Start generating a <strong>Quiz</strong> (and optionally a Slide Deck).</li>
  </ol>
  <div class="working-chip">Let it work — we'll come back in ~3 minutes.</div>
</div>

<div class="source-links">
  <a href="demo-materials/notebook/lecture-diagnostic-testing.html" target="_blank">Lecture note ↗</a>
  <a href="demo-materials/notebook/screening-reading.html" target="_blank">Reading ↗</a>
  <a href="demo-materials/notebook/common-misconceptions.html" target="_blank">Common mistakes ↗</a>
</div>

Note:
现场操作约 60–90 秒。用学校账户打开 Gemini Notebook。为了演示稳定，可以用这里准备的三份公开小材料，也可以换成你更喜欢的真实课程资料。添加资料后先问："Based only on these sources, explain why sensitivity is not the same as the probability of disease after a positive test. Cite the supporting source." 然后启动 Quiz 生成；如果你想展示 Slide Deck，也可以同时准备一个提前生成好的 backup。点击生成后不要等，马上回到 slides。

---

## Thinking is a resource. Spend it deliberately.

<div class="reasoning-scale">
  <div class="reasoning-step low"><span>FAST / LOW</span><strong>Transform</strong><small>translate · format · extract · short summary</small></div>
  <div class="reasoning-arrow">→</div>
  <div class="reasoning-step mid"><span>STANDARD</span><strong>Understand</strong><small>explain · compare · organize · tutor</small></div>
  <div class="reasoning-arrow">→</div>
  <div class="reasoning-step high"><span>EXTENDED / DEEP</span><strong>Reason</strong><small>proof · debugging · causal logic · multi-step maths</small></div>
</div>

<p class="meta">Exact names vary by product and subscription.</p>

Note:
Notebook 现在在后台处理。利用等待时间讲 reasoning effort。不要让学生背模型版本名，而是记住连续轴。Google Gemini 现在有 Standard / Extended / Deep Think 等层级；DeepSeek 也支持 thinking 开关和 effort 控制，但产品 UI 会变化，所以 slides 用抽象概念。

---

## Don't spend expensive thinking on cheap problems

<div class="cost-grid">
  <div class="cost-card cheap">
    <span>USE LESS</span>
    <strong>Routine transformations</strong>
    <p>“Translate this.”<br>“Turn this into headings.”<br>“Extract the key terms.”</p>
  </div>
  <div class="cost-card expensive">
    <span>SPEND MORE</span>
    <strong>Reasoning bottlenecks</strong>
    <p>“Why does my proof fail?”<br>“Which assumption drives this result?”<br>“Compare competing explanations.”</p>
  </div>
</div>

<p class="takeaway">Higher reasoning often costs more time and more usage quota.</p>

Note:
这是和学生实际体验最相关的一页。Gemini 免费额度有限，而且官方现在明确采用 compute-based limits；更复杂的模型和更高 thinking level 会消耗更多 usage。不要在 slide 上写固定“每天 X 次”，因为额度会变化。简单任务全部开最高思考强度既慢又浪费额度。

---

## More thinking ≠ guaranteed truth

<div class="truth-grid">
  <div><span>×</span><p>It can misunderstand the question.</p></div>
  <div><span>×</span><p>It can reason from a bad assumption.</p></div>
  <div><span>×</span><p>It can confidently derive the wrong answer.</p></div>
</div>

<blockquote>Thinking changes the reasoning budget — not the epistemic status of the answer.</blockquote>

Note:
这页把 Part 0 的 VERIFY 风险重新带回来。不要让学生形成“开 Thinking = 答案正确”的错觉。尤其数学、医学、统计推断和引用都应该有外部验证。这里不要讨论模型 chain-of-thought 细节，只讲结果仍需要验证。

---

<!-- .slide: class="live-demo-slide" -->
<p class="eyebrow">LIVE DEMO · COME BACK TO THE NOTEBOOK</p>

## Did the AI turn sources into learning material?

<div class="return-grid">
  <div>
    <strong>1 · Grounding</strong>
    <p>Can you jump from an answer to the supporting source?</p>
  </div>
  <div>
    <strong>2 · Quiz</strong>
    <p>Are the distractors plausible? Can you answer before seeing feedback?</p>
  </div>
  <div>
    <strong>3 · Study artifacts</strong>
    <p>Slides, flashcards, audio/video overviews: orientation tools, not substitutes for the source.</p>
  </div>
</div>

<pre class="demo-prompt"><code>Based only on these sources, explain why sensitivity is not the same as
P(disease | positive). Cite the supporting passage, then quiz me.
Do not show the quiz answers until I respond.</code></pre>

Note:
回 Notebook，预计此时已经完成。先展示 source citation：点击 citation 跳到原文位置，这是 Notebook 相比开放式聊天非常适合新手学习的一点。再展示 Quiz；如果 Slide Deck 已准备好，只快速翻 1–2 页。如果仍然在生成：不要等，直接打开彩排前准备的 backup notebook；或者先跳下一页讲 second opinion，最后再回来。resources/part1-runbook.md 里有完整 fallback。

---

## When the answer matters, triangulate

<div class="rubric-grid">
  <div><span>1</span><strong>Correct?</strong></div>
  <div><span>2</span><strong>Clear?</strong></div>
  <div><span>3</span><strong>Assumptions visible?</strong></div>
  <div><span>4</span><strong>Verifiable?</strong></div>
</div>

<p class="bigline">Try another model when useful — but disagreement is a signal to investigate, not a vote.</p>

Note:
解释为什么同时推荐 Gemini 和 DeepSeek：不是因为要学生维护“排行榜”，而是让他们学会比较。两个模型意见一致也不等于事实；意见不一致时更应该查教材、原始文献或计算验证。评价一个回答是否适合学习，看 correctness、clarity、assumptions、verifiability，而不是长度和语气自信。

---

## A 10-second decision tree

<div class="flow-grid">
  <div class="flow-node start">What do I need?</div>
  <div class="flow-branch">
    <div><span>MY SOURCES</span><strong>Gemini Notebook</strong></div>
    <div><span>OPEN-ENDED</span><strong>Gemini / DeepSeek</strong></div>
  </div>
  <div class="flow-node">How hard is the reasoning?</div>
  <div class="flow-branch">
    <div><span>ROUTINE</span><strong>Fast / lower effort</strong></div>
    <div><span>MULTI-STEP</span><strong>Thinking / higher effort</strong></div>
  </div>
  <div class="flow-node finish">Still uncertain? → second model + verify the source</div>
</div>

<p class="takeaway">You choose the workflow — not the AI.</p>

<p class="next">Next: turn that workflow into a study system.</p>

Note:
用这张结束 Part 1。让学生只记住这棵树：先问资料来源，再问 reasoning effort。如果重要且仍不确定，再换模型并验证。转 Part 2：现在知道“用什么、想多久”，下一步是如何把它变成日常学习 workflow。

<!-- .slide: id="part1" class="" -->
<p class="eyebrow">PART 1 · CHOOSE</p>

## Start the notebook. Then keep teaching.

<p class="sub">Live demo · import first, generate later.</p><div class="cards"><div><h3>Now</h3><p>Open a fresh notebook and add the three short course sources.</p></div><div><h3>While it imports</h3><p>We will choose tools and decide where answers should come from.</p></div></div><p class="links"><a href="materials.html#notebook" target="_blank" rel="noopener">Open Notebook source pack ↗</a> · <a href="https://notebooklm.google.com/" target="_blank" rel="noopener">Open Notebook ↗</a></p><p class="caution">Importing sources and generating a quiz are different waiting steps.</p>

Note:
0:00–1:00。立刻启动资料导入。不要等导入完成、不要先提问再回slides。准备三个tab：新Notebook、已导入资料的Notebook B、已生成Quiz和slides的Notebook C。学校已提供账号；不要要求学生此时同步操作。

---

<!-- .slide: id="choose-tools" class="" -->
<p class="eyebrow">PART 1 · CHOOSE</p>

## Start with the task, not a leaderboard.

<div class="cards"><div><h3>Gemini</h3><p>General study conversation and multimodal questions. Our default starting point.</p></div><div><h3>DeepSeek</h3><p>Compare explanations, try another model, or continue when a quota blocks you.</p></div><div><h3>Notebook</h3><p>Study a selected set of course sources and inspect source-linked answers.</p></div></div><p class="footer">NotebookLM is now Gemini Notebook; we use “Notebook” for short. <a href="https://blog.google/innovation-and-ai/products/gemini-notebook/notebooklm-gemini-notebook/" target="_blank" rel="noopener">Naming update ↗</a></p>

Note:
1:00–2:00。Gemini优先是本workshop的选择，不是综合排名。DeepSeek是备选让学生自己比较。Notebook有source-grounded工作流，但不是零幻觉保证，也不把品牌当研究结论。

---

<!-- .slide: id="source-choice" class="" -->
<p class="eyebrow">PART 1 · CHOOSE</p>

## Where should the answer come from?

<div class="cards"><div><h3>My course materials</h3><p>Select the relevant sources. Ask for a supporting passage. Accept “not in these sources”.</p></div><div><h3>An open question</h3><p>Use a general assistant. Tell it your level, assumptions and what you need to verify.</p></div></div><p class="caution">Check what was actually imported: web URLs → page text; YouTube URLs → transcript, not the video frames.</p><p class="footer"><a href="https://support.google.com/notebooklm/answer/16215270?hl=en" target="_blank" rel="noopener">Notebook source limitations ↗</a></p>

Note:
2:00–3:30。两个工具类型不是互斥：一般聊天也能上传材料；Notebook也有发现来源功能。这里是使用策略，不是说某产品只能做某任务。Google说明网页URL只导入文字、YouTube只导入字幕；上传图片/PDF属于其他source类型。

---

<!-- .slide: id="notebook-checkpoint" class="" -->
<p class="eyebrow">PART 1 · CHOOSE</p>

## Checkpoint: are the sources ready?

<div class="sequence"><div><b>Ready</b><p>Check the source text. Start one Quiz in Studio.</p></div><div><b>Still importing</b><p>Switch to the prepared source notebook. Start the Quiz there.</p></div><div><b>Then</b><p>Return to the slides while generation runs.</p></div></div><p class="caution">A prepared notebook is a backup, not a live result. Say which one you are showing.</p>

Note:
3:30–4:00。最多检查一次。新Notebook没好就用B，不挤占后面演示。可以展示Slide Deck入口，但不现场同时排多个耗时任务。学校界面实际名称为准。

---

<!-- .slide: id="reasoning" class="" -->
<p class="eyebrow">PART 1 · CHOOSE</p>

## How much thinking does this task need?

<div class="cards"><div><h3>Less</h3><p>Translate a sentence; format notes; extract defined terms.</p></div><div><h3>More</h3><p>Find a gap in a proof; compare assumptions; solve a multi-step problem.</p></div></div><p class="takeaway">Use a sufficient reasoning budget — not always the maximum.</p><p class="footer">Higher effort can cost time and quota. A simple task can still require verification.</p>

Note:
4:00–5:00。Notebook生成Quiz。讲选择思考强度，也强调“短问题”可能难、“长摘要”也可能需要核验，不能机械分类。不要写固定每日额度。

---

<!-- .slide: id="actual-controls" class="" -->
<p class="eyebrow">PART 1 · CHOOSE</p>

## Find the control in your own account.

<div class="cards"><div><h3>Gemini / DeepSeek</h3><p>Open the model or thinking menu. Inspect what your account actually offers.</p></div><div><h3>Notebook</h3><p>Choose sources and study outputs. Do not assume it has the same reasoning switch.</p></div></div><p class="caution">Product names, account permissions and subscriptions differ.<br>Writing “think carefully” is not the same as changing a model setting.</p><p class="footer"><a href="references/index.html#products" target="_blank" rel="noopener">Current official documentation ↗</a></p>

Note:
5:00–5:45。用你实际账号展示一次model/thinking菜单，不伪造截图。不将DeepSeek API的effort参数当网页按钮。不要求学生购买高级功能。个人Google和学校账号菜单可能不同。

---

<!-- .slide: id="judge-answer" class="" -->
<p class="eyebrow">PART 1 · CHOOSE</p>

## More thinking can help. Still check.

<div class="chips"><span>Correct?</span><span>Clear?</span><span>Assumptions visible?</span><span>Checkable?</span></div><p class="lead small-lead">Two models agreeing is not proof.<br>Two models disagreeing is a reason to investigate.</p><p class="takeaway">Use sources, calculations or a counterexample — not a popularity vote.</p>

Note:
5:45–6:30。比较答案时尽量保持问题、材料和约束一样，不同时换prompt又换模型然后把差异归因于模型。这里只给评估准则，真正比较留练习/课后，不再赌两次生成延迟。

---

<!-- .slide: id="notebook-return" class="" -->
<p class="eyebrow">PART 1 · CHOOSE</p>

## Return to Notebook: inspect, then try.

<div class="sequence"><div><b>1 · Inspect a citation</b><p>Does the passage support the answer?</p></div><div><b>2 · Answer a quiz item</b><p>Choose before revealing feedback.</p></div><div><b>3 · Preview one artifact</b><p>Use a pre-generated deck if needed.</p></div></div><div class="prompt"><pre><code>Based only on the selected sources, explain why sensitivity
is not P(disease | positive). Cite a supporting passage.
If the sources do not support a claim, say so.</code></pre><button class="copy" type="button">Copy prompt</button></div><p class="footer">Still generating? Show the prepared result or use the printed source exercise.</p>

Note:
6:30–9:15。预留2分45秒给你演示。点击citation不只是看有没有角标，还看原文是否支持。Quiz先请学生答一道再显示反馈。结果未完成立刻切C并说明提前准备；无法登录时用materials页面的原始表和答案，不声称是Notebook输出。生成slides官方提示可需要多分钟。

---

<!-- .slide: id="tool-summary" class="" -->
<p class="eyebrow">PART 1 · CHOOSE</p>

## You choose the tool and the effort.

<div class="sequence"><div><b>Source?</b><p>Course materials or open exploration?</p></div><div><b>Effort?</b><p>Choose an available mode that fits the task.</p></div><div><b>Check?</b><p>What evidence would make the answer trustworthy?</p></div></div><p class="takeaway">Next: how to ask about your coursework.</p>

Note:
9:15–10:00。决策树不用把Notebook接到统一Thinking按钮。下一节按Role Context Constraints Format讨论学习问题。

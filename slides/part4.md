<!-- .slide: id="part4" class="" -->
<p class="eyebrow">PART 4 · EXPLORE</p>

## Explore a concept inside the chat.

<p class="sub">Ask Gemini for an interactive visualization you can use.</p><div class="sequence"><div><b>1 · Ask to visualize</b><p>Start a new chat. Choose Pro if it is available.</p></div><div><b>2 · Change something</b><p>Ask for a slider or buttons, not a code listing.</p></div><div><b>3 · Predict and check</b><p>Predict what will change, then compare it with the result.</p></div></div><p class="links"><a href="https://gemini.google.com/" target="_blank" rel="noopener">Open Gemini ↗</a> · <a href="resources/interactive-guide.html" target="_blank" rel="noopener">Prompts & examples ↗</a></p>

Note:
15:48–15:49。不要求Canvas；用户实际无法用Canvas，却曾在普通对话成功生成交互内容。Google 2026-04-09官方发布直接在chat里生成可操作的可视化，建议在输入栏选择Pro并用show me/help me visualize。2026-08-19更新的学生功能说明脚注8已列出consumer与school-issued账号；不能沿用4月发布时“不支持教育账号”的旧限制。具体账号仍须彩排，且功能存在不等于每个prompt都会触发。
课堂主请求不再指定HTML、JS文件或Canvas Preview，而是描述要理解的概念和希望拖动的参数。先试下一页简短请求。如果没有生成交互卡片，尝试一次针对性追问；仍只有文本即用已准备好的本站PPV lab，不占用学生预测和核验的时间。向学生口头说明使用的是我们准备的教学工具，不当作新生成结果。完整源链接及核验限制见interactive-guide。

---

<!-- .slide: id="build-request" class="" -->
<p class="eyebrow">PART 4 · EXPLORE</p>

## Ask for something you can explore.

<div class="prompt"><pre><code>Help me visualize how disease prevalence changes the meaning
of a positive test. Show an interactive visualization in this chat,
with a prevalence slider, not an HTML code block.
Use 10,000 fictional people. Keep sensitivity and specificity at 90%.
Show true positives, false positives and PPV as I move the slider.
Ask me to predict what changes from 10% to 1% prevalence.</code></pre><button class="copy" type="button">Copy prompt</button></div><p class="footer">PPV = the fraction of positive tests that are true positives. <a href="resources/interactive-guide.html#text-only" target="_blank" rel="noopener">Only getting text? ↗</a></p>

Note:
15:49–15:50。在普通Gemini新对话选择可用的Pro，复制屏幕请求，不先要求编程语言、文件格式、下载代码或Canvas。这里教的是学习请求，不是神奇触发词，不保证一次成功。
若只输出代码或静态说明，追问：
“Please show an interactive visualization directly in this conversation. I want to move a prevalence slider and see the counts change. Do not give me code or instructions for building an app. If this chat cannot display an interactive visualization, tell me plainly.”
如果要先验证账号能否生成任何交互内容，课前可试更简单的官方同类题：
“Help me visualize a pendulum. Show an interactive simulation here with a length slider and a play/pause button.”
若简单物理可视化成功而PPV失败，说明本题生成不稳定，不能断言账号不支持。若都只有文本，也不能仅凭一次失败诊断原因。不要让学生为课堂demo升级订阅或把受限课程资料转到私人账号。按下页已经准备好的PPV lab继续。
功能依据为Google官方4月9日说明和8月19日更新；此prompt是教学设计，尚未在讲者登录账号复现。

---

<!-- .slide: id="ppv-demo" class="lab-slide" -->
<p class="eyebrow">PART 4 · EXPLORE</p>

## Why can a positive test be misleading?

<p class="sub">Prevalence is how common the disease is. Predict what happens when it falls.</p><iframe class="lab-frame" data-src="demo-materials/medicine/ppv-lab.html?embed=1" title="Interactive PPV teaching lab"></iframe><p class="footer"><a href="demo-materials/medicine/ppv-lab.html" target="_blank" rel="noopener">Open full app ↗</a> · Compare prevalence 10% and 1%, keeping sensitivity and specificity at 90%.</p>

Note:
15:50–15:53。先10%患病率、敏感度特异度都90%，请学生预测PPV；Reveal显示50%。再改1%，预测后显示约8.3%。固定Se/Sp只是toy假设，不是不同人群现实中必然不变。预期人数不等同随机模拟，代码完全本地算。这里是本站教学工具；不宣称它是Gemini刚生成的结果。

---

<!-- .slide: id="test-tool" class="" -->
<p class="eyebrow">PART 4 · EXPLORE</p>

## Check the tool outside the tool.

<table><thead><tr><th>Known case</th><th>Manual check</th></tr></thead><tbody><tr><td>p = 10%; Se = Sp = 90%</td><td>900 / (900 + 900) = 50%</td></tr><tr><td>p = 1%; Se = Sp = 90%</td><td>90 / (90 + 990) ≈ 8.3%</td></tr><tr><td>p = 0%; Sp = 100%</td><td>No positive results → PPV undefined</td></tr></tbody></table><p class="caution">N = 10,000 hypothetical people. Expected counts, not observations.<br>No diagnosis or treatment decision should come from this toy model.</p>

Note:
15:53–15:54。这些数字用手算核对，不能用同一程序函数生成期待答案再说测试通过。前两行适用于固定敏感度特异度的对话可视化；第三行在本站lab中将特异度改为100%后核验。讨论分母为0必须是undefined，不能0%。

---

<!-- .slide: id="action-boundaries" class="" -->
<p class="eyebrow">PART 4 · EXPLORE</p>

## More automation needs clearer boundaries.

<div class="cards"><div><h3>Specify the scope</h3><p>Which files? Which tools? Read-only first. Keep originals.</p></div><div><h3>Approve consequential actions</h3><p>Review before sending, submitting, deleting or changing data.</p></div><div><h3>Keep a way back</h3><p>Use copies, backups and a change log. Reversible is not automatic.</p></div></div><p class="takeaway">Do not delegate an assessed step you are required to do yourself.</p>

Note:
15:54–15:56。agent只占约一分钟到两分钟。重命名并不天然可撤销；无备份也可能损坏工作流。初学者学习场景保持少权限、人工确认。

---

<!-- .slide: id="exercise3" class="" -->
<p class="eyebrow">PART 4 · EXPLORE</p>

## Exercise 4 · check the feedback.

<p class="sub">Use your own paragraph from Exercise 3.</p><div class="prompt"><pre><code>Check my explanation against the provided material.
Do not rewrite it yet. If correct, say so.
If something is wrong, quote the part and explain why.
Do not invent a missing idea or an error.
Ask one question, then wait for my revision.</code></pre><button class="copy" type="button">Copy prompt</button></div><div class="timer" data-seconds="360"><output aria-live="off">06:00</output><button type="button" data-timer="toggle">Start</button><button type="button" data-timer="reset">Reset</button></div><p class="caution">1 min prepare · 3 min check · 2 min revise.<br>Keep one change and its evidence, or explain why you disagree.</p>

Note:
15:56–16:02。区别于Exercise3：这次评估AI反馈，允许不接受错误建议。学生保存自己修改的句子与依据，而不是让AI生成最终稿。可不上传个人草稿到公开网站；本站没有收集功能。

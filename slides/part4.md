<!-- .slide: id="part4" -->
<p class="eyebrow">PART 4 · EXPLORE</p>

## Make a concept something you can explore.

<div class="pathway"><div><span class="icon" data-icon="chat"></span><h3>Ask</h3><p>Describe the idea you want to visualize.</p></div><div><span class="icon" data-icon="sliders"></span><h3>Change</h3><p>Move a slider or choose a case.</p></div><div><span class="icon" data-icon="target"></span><h3>Predict</h3><p>Say what should happen, then test it.</p></div></div><p class="takeaway">Try an interactive visualization in an ordinary Gemini chat.</p><p class="links"><a href="https://gemini.google.com/" target="_blank" rel="noopener">Open Gemini ↗</a> · <a href="resources/interactive-guide.html" target="_blank" rel="noopener">Prompts & examples ↗</a></p>

Note:
15:45–15:46。
有些概念，看一张固定的图还不够。能够改一个参数，再看结果怎么变，会更直观。我们直接在 Gemini 普通对话里提出请求。
操作：使用彩排时可用的模式，有 Pro 可以先选它。若没有生成可操作的内容，用下一页的对话循环方案；具体操作参考 interactive-guide。

---

<!-- .slide: id="build-request" -->
<p class="eyebrow">PART 4 · EXPLORE</p>

## Ask for a slider, not a page of code.

<div class="prompt"><pre><code>Help me visualize how disease prevalence changes the meaning
of a positive test. Show an interactive visualization in this chat,
with a prevalence slider, not an HTML code block.
Use 10,000 fictional people. Keep sensitivity and specificity at 90%.
Show true positives, false positives and PPV as I move the slider.
Ask me to predict what changes from 10% to 1% prevalence.</code></pre><button class="copy" type="button">Copy prompt</button></div><p class="footer">PPV: the fraction of positive tests that are true positives. <a href="resources/interactive-guide.html#text-only" target="_blank" rel="noopener">Only getting text? ↗</a></p>

Note:
15:46–15:47。
这里说清楚三件事：想理解什么、想操作哪个参数、想看到什么结果。把请求贴进普通聊天。拿到工具以后先别随便拖，先预测。
如果没有出现真正可操作的滑块，不要卡在“生成网页”这件事上。下一页换成对话循环：先填参数，再让 Gemini 画出文字可视化、计算并解释。

---

<!-- .slide: id="text-loop" -->
<p class="eyebrow">PART 4 · EXPLORE</p>

## If there is no slider, use a conversation loop.

<div class="cards"><div><span class="icon" data-icon="files"></span><h3>Template first</h3><p>Gemini asks for parameters.</p></div><div><span class="icon" data-icon="chat"></span><h3>You fill values</h3><p>Change one number each round.</p></div><div><span class="icon" data-icon="chart"></span><h3>Draw + explain</h3><p>Gemini shows a text visual and interprets it.</p></div></div><div class="prompt"><pre><code>If you cannot render an interactive app, use a conversation loop.
First give me a fill-in template for the parameters.
After I fill it in, draw a compact text visualization of the result,
calculate the key numbers, and explain what changed.
Then ask me which one parameter I want to change next.</code></pre><button class="copy" type="button">Copy prompt</button></div><p class="takeaway">Fallback does not mean weaker: keep prediction → result → explanation.</p>

Note:
15:47–15:48。
大多数时候，普通对话不一定能真的渲染网页或滑块。替代方案不是让学生读代码，而是把交互拆成一轮一轮的对话。
Gemini 先给参数模板，例如：总人数、患病率、敏感度、特异度。学生填数值。Gemini 用文字图、表格或简单条形图画出结果，算出关键数，再解释变化。下一轮只改一个参数，继续预测、看结果、解释。

---

<!-- .slide: id="ppv-demo" class="lab-slide" -->
<p class="eyebrow">PART 4 · EXPLORE</p>

## When the disease is rarer, what changes?

<p class="sub">Keep sensitivity and specificity at 90%. Change prevalence from 10% to 1%.</p><iframe class="lab-frame" data-src="demo-materials/medicine/ppv-lab.html?embed=1" title="Interactive PPV teaching lab"></iframe><p class="footer"><a href="demo-materials/medicine/ppv-lab.html" target="_blank" rel="noopener">Open full app ↗</a> · Fictional teaching example.</p>

Note:
15:48–15:50。
先看患病率10%的情况，请大家猜阳性预测值，再揭晓50%。改成1%，先猜，再揭晓约8.3%。让同学解释：为什么检测参数没有变，阳性结果的含义却变了？
这里使用的是提前准备的教学工具。关键是看到，患病者变少时，假阳性在所有阳性里的占比可能变大。

---

<!-- .slide: id="test-tool" -->
<p class="eyebrow">PART 4 · CHECK</p>

## Check two cases by hand.

<div class="stat-grid calculation"><div><span class="icon" data-icon="math"></span><h3>10% prevalence</h3><p>900 true positives + 900 false positives</p><strong>900 / 1,800</strong><p class="answer">50%</p></div><div><span class="icon" data-icon="math"></span><h3>1% prevalence</h3><p>90 true positives + 990 false positives</p><strong>90 / 1,080</strong><p class="answer">≈ 8.3%</p></div></div><p class="takeaway">Does the visualization agree with your calculation?</p><p class="footer">10,000 fictional people · sensitivity = specificity = 90% · Expected counts.</p>

Note:
15:50–15:51。
我们不用另一个模型来投票，直接算两个例子。界面再漂亮，数字也应该和公式对得上。还可以试一个边界：在本站工具里，把患病率设为0、特异度设为100%，就没有阳性结果，PPV 的分母为0，应显示未定义。

---

<!-- .slide: id="action-boundaries" -->
<p class="eyebrow">PART 4 · WORK WITH AI</p>

## Let AI draft. Review the action.

<div class="pathway"><div><span class="icon" data-icon="files"></span><h3>Work on a copy</h3><p>Keep the original material.</p></div><div><span class="icon" data-icon="search"></span><h3>Preview changes</h3><p>Check what will be different.</p></div><div><span class="icon" data-icon="check"></span><h3>You approve</h3><p>Review before sending or submitting.</p></div></div><p class="takeaway">Next: apply the same habit to feedback on your writing.</p>

Note:
15:51–15:52。
以后你会遇到能直接改文件、运行代码甚至提交内容的 AI。一个实用习惯是：先在副本上试，看看改了什么，再决定采用。对自己写的解释也一样，AI 提的修改建议值得看，但最后由你判断。

---

<!-- .slide: id="exercise3" -->
<p class="eyebrow">PART 4 · TRY</p>

## Exercise 4 · decide what feedback to use.

<p class="sub">Reopen your own paragraph from Exercise 3.</p><div class="prompt"><pre><code>Check my explanation against the provided material.
If it is correct, say so. If something needs fixing,
quote that part and explain why.
Ask one question, then wait for me to revise it.</code></pre><button class="copy" type="button">Copy prompt</button></div><div class="timer" data-seconds="360"><output aria-live="off">06:00</output><button type="button" data-timer="toggle">Start</button><button type="button" data-timer="reset">Reset</button></div><p class="footer">1 min prepare · 3 min check · 2 min revise. Keep one decision and your reason.</p>

Note:
15:52–15:53说明；15:53–15:59练习。
刚才你已经自己解释过概念了。这一次，请 AI 看这段解释，再把它的反馈和课程材料对照。你可以接受建议，也可以保留原来的写法，重点是能说清楚理由。
最后记一句：“我改了这里，因为……”或者“我没有采用这条建议，因为……”。

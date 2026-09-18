<!-- .slide: id="part3" -->
<p class="eyebrow">PART 3 · UNDERSTAND</p>

## Where does the explanation stop making sense?

<div class="cards"><div><span class="icon" data-icon="layers"></span><h3>Missing background?</h3><p>Revisit the earlier idea.</p></div><div><span class="icon" data-icon="lightbulb"></span><h3>Too abstract?</h3><p>Try a picture or small example.</p></div><div><span class="icon" data-icon="target"></span><h3>Not sure you get it?</h3><p>Explain it. Predict a new case.</p></div></div><p class="takeaway">Tell AI where you lose the thread.</p>

Note:
15:25–15:27。
欢迎回来。请想一个课程里真正难懂的概念。困难有时是前面的基础缺了一块，有时是解释太抽象，也可能是看着懂、自己讲不出来。我们先辨认是哪一种，再决定怎么让 AI 帮忙。

---

<!-- .slide: id="concept-layers" -->
<p class="eyebrow">PART 3 · UNDERSTAND</p>

## See the same idea in different ways.

<div class="pathway four"><div><span class="icon" data-icon="lightbulb"></span><h3>Intuition</h3><p>What is happening?</p></div><div><span class="icon" data-icon="book"></span><h3>Definition</h3><p>What exactly does it mean?</p></div><div><span class="icon" data-icon="math"></span><h3>Example</h3><p>Try a small case.</p></div><div><span class="icon" data-icon="target"></span><h3>Prediction</h3><p>What changes next?</p></div></div><p class="takeaway">Picture → meaning → example → your own explanation</p>

Note:
15:27–15:28:30。
我们接下来用特征向量做一个示范。先看图，再接上定义，最后自己预测。其他学科也可以这样做：把一段抽象解释换成一个具体案例，再说清楚它对应哪个概念。

---

<!-- .slide: id="vector-predict" class="lab-slide" -->
<p class="eyebrow">PART 3 · UNDERSTAND</p>

## Predict before you reveal.

<p class="sub">A doubles x and leaves y unchanged. Try (1, 0), then (1, 1).</p><iframe class="lab-frame" data-src="demo-materials/stem/eigenvectors.html?embed=1" title="Interactive eigenvector prediction lab"></iframe><p class="footer"><a href="demo-materials/stem/eigenvectors.html" target="_blank" rel="noopener">Open full lab ↗</a> · Change one thing at a time.</p>

Note:
15:28:30–15:31:30。
先选(1,0)，请大家预测变换后在哪里，再点 Reveal。接着选(1,1)，同样先预测。问：哪一个输出可以通过把原向量整体乘上一个数得到？
这是我们准备好的教学工具。可以直接手算：A(1,0)=(2,0)，A(1,1)=(2,1)。让图形和计算互相对应。

---

<!-- .slide: id="vector-definition" -->
<p class="eyebrow">PART 3 · UNDERSTAND</p>

## Connect the picture to the definition.

<div class="equation">Av = λv &nbsp; with v ≠ 0</div><div class="cards"><div><span class="icon" data-icon="sliders"></span><h3>One scale factor</h3><p>The same λ multiplies every coordinate.</p></div><div><span class="icon" data-icon="math"></span><h3>Stretch, flip or collapse</h3><p>λ can be positive, negative or zero.</p></div></div><p class="takeaway">Here, (1, 0) is an eigenvector. (1, 1) is not.</p>

Note:
15:31:30–15:33。
特征向量的关键是：矩阵作用以后，得到原向量的某个倍数。这个倍数必须同时适用于所有坐标。(1,1)变成(2,1)，就找不到这样的一个数。
负的 λ 会反向，λ 等于零会让输出落到原点，所以定义比“方向不变”更准确。输入向量本身要非零。图像帮助我们理解，再用定义把意思说完整。

---

<!-- .slide: id="hint-mode" -->
<p class="eyebrow">PART 3 · UNDERSTAND</p>

## A useful hint gives you a next step.

<div class="dialogue"><p><b>My attempt:</b> A(1,1) = (2,1), so λ = 2.</p><p><b>A helpful hint:</b> If λ = 2, what is λ(1,1)? Compare both coordinates.</p></div><div class="prompt"><pre><code>Check my attempt against the definition.
If I made a mistake, give one hint about that step.
Then wait for me to try again.</code></pre><button class="copy" type="button">Copy prompt</button></div><p class="takeaway">Make the next decision yourself.</p>

Note:
15:33–15:34:30。
这里的同学只看了第一个坐标。与其把解法重新讲一遍，不如问他：2乘(1,1)到底是多少？请大家先算。这样他就能自己看见，第二个坐标对不上。
追问也可以很短，不用每次重新填写四段模板。

---

<!-- .slide: id="choose-track" -->
<p class="eyebrow">PART 3 · YOUR COURSE</p>

## One method. Different subjects.

<div class="cards"><div><span class="icon" data-icon="math"></span><h3>STEM</h3><p>Eigenvectors:<br>one scale factor.</p></div><div><span class="icon" data-icon="target"></span><h3>Medicine</h3><p>Sensitivity vs PPV:<br>which denominator?</p></div><div><span class="icon" data-icon="chart"></span><h3>Business</h3><p>Elasticity:<br>percentage changes.</p></div><div><span class="icon" data-icon="book"></span><h3>Humanities</h3><p>Arguments:<br>claim, reason, evidence.</p></div></div><p class="links"><a href="materials.html#tracks" target="_blank" rel="noopener">Four source packs + questions ↗</a> · Or continue with your own course.</p>

Note:
15:34:30–15:36。
你不用选数学题。可以继续刚才的课程，也可以用网站上的四套材料。共同任务是一样的：先找到一个难点，请 AI 换一种方式解释，再关掉回答，自己说一遍。

---

<!-- .slide: id="exercise2" -->
<p class="eyebrow">PART 3 · TRY</p>

## Exercise 3 · explain without looking.

<div class="sequence"><div><b>1 + 3 min</b><p>Choose a concept. Explore a definition and example.</p></div><div><b>2 min</b><p>Hide the answer. Write your own explanation.</p></div><div><b>2 min</b><p>Check the source. Try a new case.</p></div></div><div class="timer" data-seconds="480"><output aria-live="off">08:00</output><button type="button" data-timer="toggle">Start</button><button type="button" data-timer="reset">Reset</button></div><p class="footer">Keep your own paragraph for Exercise 4. <a href="materials.html" target="_blank" rel="noopener">Materials ↗</a> · <a href="prompts/index.html" target="_blank" rel="noopener">Prompts ↗</a></p>

Note:
15:36–15:37说明；15:37–15:45练习，最后30秒切到下一页。
请用自己的话解释，而不是整理 AI 的原句。可以画图、写公式，也可以用一段话。最后找一个稍有变化的例子，看看这个解释还管不管用。检查时回到课程材料或答案页。

---

<!-- .slide: id="exercise2-debrief" -->
<p class="eyebrow">PART 3 · TAKE STOCK</p>

## Could a classmate follow your explanation?

<div class="cards"><div><span class="icon" data-icon="chat"></span><h3>Explain it</h3><p>Use your own words.</p></div><div><span class="icon" data-icon="math"></span><h3>Apply it</h3><p>Try a different example.</p></div><div><span class="icon" data-icon="search"></span><h3>Find the gap</h3><p>What is still unclear?</p></div></div><p class="takeaway">Keep the paragraph. Next, we will explore and check.</p>

Note:
15:44:30–15:45，包含在练习时间内。
看看自己写的这段话。你最有把握的是哪一句？还有哪一句想再确认？先把它保存下来。下面我们试试，让一个概念变成可以拖动、可以预测的小工具。

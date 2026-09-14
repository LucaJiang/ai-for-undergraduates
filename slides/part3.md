<!-- .slide: id="part3" class="" -->
<p class="eyebrow">PART 3 · UNDERSTAND</p>

## What makes this concept difficult?

<div class="cards"><div><h3>Missing background?</h3><p>Which earlier idea do I need first?</p></div><div><h3>The explanation does not click?</h3><p>Can a diagram or a small numerical example help?</p></div><div><h3>Unsure I understand?</h3><p>Can I explain it or apply it to a new question?</p></div></div><p class="takeaway">Tell AI exactly where you get stuck.</p>

Note:
15:25–15:27。休息后回到学生自己的困难概念。沿用Exercise2的主题，不反复选材料。

---

<!-- .slide: id="concept-layers" class="" -->
<p class="eyebrow">PART 3 · UNDERSTAND</p>

## Move between representations.

<div class="sequence"><div><b>Intuition</b><p>What is the idea doing?</p></div><div><b>Definition</b><p>What does each symbol mean?</p></div><div><b>Example</b><p>What happens in a small case?</p></div><div><b>Self-check</b><p>Can I predict the next case?</p></div></div><p class="caution">A useful analogy is a bridge — not a replacement for the definition.</p>

Note:
15:27–15:29。不是每个学科都要公式，但都要把直觉与学科正式定义连上。数学可用符号，文科可用主张条件和反例。

---

<!-- .slide: id="vector-predict" class="lab-slide" -->
<p class="eyebrow">PART 3 · UNDERSTAND</p>

## Predict before you reveal.

<p class="sub">A doubles the x-coordinate and leaves y unchanged. Compare (1, 0) and (1, 1).</p><iframe class="lab-frame" data-src="demo-materials/stem/eigenvectors.html?embed=1" title="Interactive eigenvector prediction lab"></iframe><p class="footer"><a href="demo-materials/stem/eigenvectors.html" target="_blank" rel="noopener">Open full lab ↗</a> · Change one thing at a time.</p>

Note:
15:29–15:33。先选e1，问输出位置和是否沿同一直线；Reveal。再选(1,1)，先预测再Reveal。不要一上来解特征多项式。图有输入/输出数值，学生可以算矩阵乘法验证。此页为我们已检查的教学工具，不假装是当场AI生成。

---

<!-- .slide: id="vector-definition" class="" -->
<p class="eyebrow">PART 3 · UNDERSTAND</p>

## Connect the picture to the definition.

<div class="equation">Av = λv &nbsp; with v ≠ 0</div><div class="cards"><div><h3>λ is the scale factor</h3><p>The matrix sends v to a scalar multiple of itself.</p></div><div><h3>Stretch, flip or collapse</h3><p>λ &lt; 0 reverses the vector. λ = 0 sends it to zero.</p></div></div><p class="takeaway">In our example: (1, 0) is an eigenvector; (1, 1) is not.</p><p class="footer">The input vector must be nonzero.</p>

Note:
15:33–15:35。修复“方向不变”过度简化。定义是非零v与Av标量倍数；零输出没有方向，但仍可对应λ0。选反射和投影验证边界，不说所有实矩阵必有实特征向量。

---

<!-- .slide: id="hint-mode" class="" -->
<p class="eyebrow">PART 3 · UNDERSTAND</p>

## A hint should leave you something to decide.

<div class="dialogue"><p><b>My attempt:</b> A(1,1) = (2,1), so λ = 2.</p><p><b>Helpful next step:</b> If λ were 2, what would λ(1,1) be? Compare both coordinates.</p><p><b>My next task:</b> Decide whether one scalar matches the whole vector.</p></div><div class="prompt"><pre><code>Check my attempt against the definition. If there is an error,
give one hint about the first incorrect step. If it is correct,
say so. Wait for my revision; do not finish the problem for me.</code></pre><button class="copy" type="button">Copy prompt</button></div>

Note:
15:35–15:37。RCCF已经学过，此处是可追加短句不必重新填四段。模拟学生只检查一维而忽略另一维的错误。不要让AI不论学生答案都必须指出错误。

---

<!-- .slide: id="analogy-limit" class="" -->
<p class="eyebrow">PART 3 · UNDERSTAND</p>

## Ask where the analogy stops working.

<div class="dialogue"><p><b>Analogy:</b> Stretch a sheet horizontally.</p><p><b>Useful here:</b> It helps visualize A = diag(2,1).</p><p><b>Not the definition:</b> Reflection, projection and rotation need different pictures.</p></div><div class="prompt"><pre><code>Which part of this analogy matches the formal definition?
Where does it fail? Give one counterexample or boundary case.</code></pre><button class="copy" type="button">Copy prompt</button></div>

Note:
15:37–15:38。“直觉好听”不是充分证据。医学机制/经济类比也要检查适用条件，避免一个比喻替代整个理论。

---

<!-- .slide: id="choose-track" class="" -->
<p class="eyebrow">PART 3 · UNDERSTAND</p>

## One method. Different subjects.

<div class="cards"><div><h3>STEM</h3><p>Eigenvectors: scalar multiples, not motionlessness.</p></div><div><h3>Medicine</h3><p>Sensitivity vs PPV: which denominator?</p></div><div><h3>Business</h3><p>Elasticity: percentage changes, not raw slope.</p></div><div><h3>Humanities</h3><p>Claim, reason, assumption — where is the evidence?</p></div></div><p class="links"><a href="materials.html#tracks" target="_blank" rel="noopener">Four source packs + questions ↗</a> · Or continue with your own course.</p>

Note:
15:38–15:40。四轨有相近大小的材料、两道自检和单独核验答案。无需每个专业都讲一遍；学生自由选或自带课程。不要把病人信息带入医学轨。

---

<!-- .slide: id="exercise2" class="" -->
<p class="eyebrow">PART 3 · UNDERSTAND</p>

## Exercise 3 · explain without looking.

<div class="sequence"><div><b>1 + 3 min</b><p>Choose a concept; ask for intuition, definition and one example.</p></div><div><b>2 min</b><p>Hide the answer. Write your explanation or attempt a new case.</p></div><div><b>2 min</b><p>Check the source or answer key. Mark one remaining uncertainty.</p></div></div><div class="timer" data-seconds="480"><output aria-live="off">08:00</output><button type="button" data-timer="toggle">Start</button><button type="button" data-timer="reset">Reset</button></div><p class="links"><a href="prompts/index.html" target="_blank" rel="noopener">Prompt library ↗</a> · <a href="materials.html" target="_blank" rel="noopener">Student materials ↗</a></p><p class="caution">Keep: your own explanation — not a copied AI paragraph.</p>

Note:
15:40–15:48。实际8分钟。AI可以解释；学生需要离开答案写自己的版本。最后对来源自查，不在这里做长篇AI批改，避免和Exercise4重复。

---

<!-- .slide: id="exercise2-debrief" class="" -->
<p class="eyebrow">PART 3 · UNDERSTAND</p>

## Can you use the idea in a new example?

<p class="lead small-lead">Explain it to a classmate.<br>Try a slightly different case.<br>Name one limit of your explanation.</p><p class="takeaway">Keep this paragraph. You will evaluate feedback on it in Exercise 4.</p>

Note:
练习最后30秒，不另计时。接下来Part4不再泛讲“代码能帮助学习”，而是展示一个可运行的小工具并检验它。

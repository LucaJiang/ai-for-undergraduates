<!-- .slide: id="part4" class="" -->
<p class="eyebrow">PART 4 · EXPLORE</p>

## Build one small learning tool. Then test it.

<div class="sequence"><div><b>Question</b><p>Why does prevalence change PPV?</p></div><div><b>Toy tool</b><p>Change a parameter and inspect a table.</p></div><div><b>Check</b><p>Predict first; calculate an independent case.</p></div></div><p class="takeaway">The output is a learning aid, not an analysis report.</p>

Note:
15:48–15:49。8分钟只做一件完整演示。是备课生成、检查好的工具，现场可以展示请求和代码，不需要赌实时生成。

---

<!-- .slide: id="build-request" class="" -->
<p class="eyebrow">PART 4 · EXPLORE</p>

## Make the request testable.

<div class="prompt"><pre><code>Goal: Build a tiny browser teaching tool for PPV.
Inputs: Fictional population; adjustable prevalence, sensitivity
and specificity. No patient data.
Boundaries: No network requests, external libraries or uploads.
Checks: Show the formula, expected counts and undefined cases.
Hide results until I predict.
Output: One readable HTML page with labelled controls.</code></pre><button class="copy" type="button">Copy prompt</button></div><p class="caution">Prepared implementation available. Newly generated code still needs review before running.</p>

Note:
15:49–15:50。此处才用行动式框架，与Part2日常问答区别。演示你想让它构建什么、检查什么。不要在学生电脑上运行未经检查的陌生脚本。已有版本是fallback与标准演示都可用。

---

<!-- .slide: id="ppv-demo" class="lab-slide" -->
<p class="eyebrow">PART 4 · EXPLORE</p>

## Same sensitivity. A different meaning for a positive.

<iframe class="lab-frame" data-src="demo-materials/medicine/ppv-lab.html?embed=1" title="Interactive PPV teaching lab"></iframe><p class="footer"><a href="demo-materials/medicine/ppv-lab.html" target="_blank" rel="noopener">Open full lab ↗</a> · Predict at 10%, then at 1% prevalence.</p>

Note:
15:50–15:53。先10%患病率、敏感度特异度都90%，请学生预测PPV；Reveal显示50%。再改1%，预测后显示约8.3%。固定Se/Sp只是toy假设，不是不同人群现实中必然不变。预期人数不等同随机模拟，代码完全本地算。

---

<!-- .slide: id="test-tool" class="" -->
<p class="eyebrow">PART 4 · EXPLORE</p>

## Check the tool outside the tool.

<table><thead><tr><th>Known case</th><th>Manual check</th></tr></thead><tbody><tr><td>p = 10%; Se = Sp = 90%</td><td>900 / (900 + 900) = 50%</td></tr><tr><td>p = 1%; Se = Sp = 90%</td><td>90 / (90 + 990) ≈ 8.3%</td></tr><tr><td>p = 0%; Sp = 100%</td><td>No positive results → PPV undefined</td></tr></tbody></table><p class="caution">N = 10,000 hypothetical people. Expected counts, not observations.<br>No diagnosis or treatment decision should come from this toy model.</p>

Note:
15:53–15:54。这些数字手算或另一份代码核对，不能用同一程序函数生成期待答案再说测试通过。讨论分母为0必须是undefined，不能0%。

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

## Exercise 3 · judge the feedback.

<p class="sub">Use your own paragraph from Exercise 2.</p><div class="prompt"><pre><code>Check my explanation against the provided material.
Do not rewrite it yet. If correct, say so.
If something is wrong, quote the part and explain why.
Do not invent a missing idea or an error.
Ask one question, then wait for my revision.</code></pre><button class="copy" type="button">Copy prompt</button></div><div class="timer" data-seconds="360"><output aria-live="off">06:00</output><button type="button" data-timer="toggle">Start</button><button type="button" data-timer="reset">Reset</button></div><p class="caution">1 min prepare · 3 min inspect feedback · 2 min revise.<br>Keep one change and its evidence — or explain why you reject a suggestion.</p>

Note:
15:56–16:02。区别于Exercise2：这次评估AI反馈，允许不接受错误建议。学生保存自己修改的句子与依据，而不是让AI生成最终稿。可不上传个人草稿到公开网站；本站没有收集功能。

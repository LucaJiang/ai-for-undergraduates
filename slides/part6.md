<!-- .slide: id="part6" -->
<p class="eyebrow">PART 6 · AI, PAST & FUTURE</p>

## Look how much changed in one decade.

<div class="timeline"><div><span class="icon" data-icon="face"></span><b>2015</b><h3>Recognize faces</h3><p>FaceNet</p></div><div><span class="icon" data-icon="board"></span><b>2016</b><h3>Master Go</h3><p>AlphaGo</p></div><div><span class="icon" data-icon="chat"></span><b>2022</b><h3>Hold a conversation</h3><p>ChatGPT</p></div><div><span class="icon" data-icon="math"></span><b>2025–26</b><h3>Work on mathematics</h3><p>Competition and research problems</p></div></div><p class="takeaway">What might change while you are still at university?</p><p class="footer">Selected milestones · <a href="references/future.html#milestones" target="_blank" rel="noopener">Original papers & announcements ↗</a></p>

Note:
16:03–16:03:30。
回头看，很多人最早接触的 AI，是识别人脸、给照片分类。后来我们看到它下围棋，再后来是可以聊天、写代码。现在，它已经开始参与研究级别的数学问题。放在你们的学习生涯里，这些变化发生得很快。
用半分钟带过这几个节点。接下来不急着给大家学习建议，先一起想三个问题：AI 擅长什么，我们能不能用到这种能力，谁会从中受益？

---

<!-- .slide: id="math-frontier" -->
<p class="eyebrow">PART 6 · THE MATHEMATICS FRONTIER</p>

## From competition problems to research proofs.

<div class="cards frontier"><div><span class="icon" data-icon="medal"></span><p class="mini-label">IMO · 2025</p><h3>Gold-medal standard</h3><p>An advanced Gemini Deep Think system solved 5 of 6 problems.</p></div><div><span class="icon" data-icon="math"></span><p class="mini-label">FIRST PROOF · 2026</p><h3>Research-level mathematics</h3><p>AI-generated proofs received passing evaluations from expert mathematicians.</p></div></div><p class="takeaway">AI is becoming a serious mathematical collaborator.</p><p class="footer"><a href="https://deepmind.google/blog/advanced-version-of-gemini-with-deep-think-officially-achieves-gold-medal-standard-at-the-international-mathematical-olympiad/" target="_blank" rel="noopener">Google DeepMind / IMO result ↗</a> · <a href="https://arxiv.org/abs/2606.18119" target="_blank" rel="noopener">First Proof Second Batch ↗</a></p>

Note:
16:03:30–16:04。
这已经不只是把课本题做快一点。左边是竞赛级别的解题能力，右边则把问题推进到了研究数学：数学家拿出此前没有公开解答的问题，再请专家评阅 AI 的证明。有些证明还走了和人类解答不同的路线。
假设有一天 AI 真的比所有数学家都强，我们还要不要学数学？先把这个问题留在心里。我们从一个更具体的问题开始：为什么数学、代码和游戏，特别适合 AI 反复练习？

---

<!-- .slide: id="ai-task-patterns" class="future-discussion" -->
<p class="eyebrow">PART 6 · QUESTION 1 · CAPABILITIES</p>

## Why is AI so good at<br>coding, maths and games?

<p class="sub">What do these tasks have in common?</p><div class="cards"><div><span class="icon" data-icon="sliders"></span><h3>Coding</h3></div><div><span class="icon" data-icon="math"></span><h3>Maths</h3></div><div><span class="icon" data-icon="board"></span><h3>Games</h3></div></div><div class="chips fragment" data-fragment-index="0"><span>Clear goals</span><span>Checkable feedback</span><span>Many attempts</span></div><p class="takeaway fragment" data-fragment-index="1">Solving a problem — or choosing a worthwhile problem?</p><p class="footer"><a href="references/future.html#capabilities" target="_blank" rel="noopener">Training examples & discussion ↗</a></p>

Note:
16:04–16:05:30。先问，再按右键展开提示。
“数学和编程都很难，为什么 AI 在这些地方进步很快？大家觉得，这三类任务有什么共同点？”留十几秒，请一位同学说一个想法。
第一下展开三个关键词：“其中很多任务有明确目标，也有比较清楚的检查方法。程序可以运行测试，有标准答案的题可以核对，游戏可以看到输赢。这样就能在计算机里反复尝试，把反馈用来改进。”DeepSeek-R1 论文的 2.2.2 节用数学答案和编程测试说明了这类训练信号。
第二下展开追问：“解出一道题，和决定哪道题值得研究，是不是同一件事？”听一个回答即可。AI 也能帮我们提出问题；这里比较的是两类任务，而不是划出一块 AI 永远做不到的领域。真实软件和研究证明，还需要比单一测试更丰富的检查。
转场：“如果模型已经这么强，我们打开手机里的 AI，就能用到同样的能力吗？”

---

<!-- .slide: id="ai-access" class="future-discussion" -->
<p class="eyebrow">PART 6 · QUESTION 2 · ACCESS</p>

## Can we use the AI<br>we read about?

<p class="sub">What would it take to reproduce a research result?</p><div class="cards"><div><span class="icon" data-icon="link"></span><h3>Is it public?</h3><p>Which model can I access?</p></div><div><span class="icon" data-icon="clock"></span><h3>Can I run it?</h3><p>How much time and budget?</p></div><div><span class="icon" data-icon="sliders"></span><h3>What else is needed?</h3><p>Which tools and setup?</p></div></div><p class="dialogue compact fragment" data-fragment-index="0">Some research systems already use public models.</p><p class="takeaway fragment" data-fragment-index="1">Access to a model is a start. Resources shape how we use it.</p><p class="footer"><a href="references/future.html#access" target="_blank" rel="noopener">First Proof example & model-access guide ↗</a></p>

Note:
16:05:30–16:07。先让学生猜：刚才那些研究系统，普通人能用吗？
第一下展开：“有些可以。First Proof 第二批实验用的是公众能够获得的模型，或调用这些模型的程序系统。厉害的 AI 并不全锁在实验室里。”
“但拿到同一个模型，还要看怎样使用它。实验中的不同系统，完成那十道题所报告的费用，从约 117 美元到 4,799 美元不等。这是那次实验的运行费用。它们也用了不同的程序、工具和运行时间。”数字见论文 Table 5；无需在课堂上逐项报表。
第二下展开：“所以我们要分开问：我能不能访问这个模型？我能用多少？我有没有配套的工具？”Google 的个人账号说明也区分使用额度和思考级别；课堂账号以实际界面为准。这里不用比较套餐或要求学生购买。
转场：“如果更充分地使用 AI 需要钱、时间和技术支持，它会不会先放大本来就有的优势？”

---

<!-- .slide: id="ai-inequality" class="future-discussion" -->
<p class="eyebrow">PART 6 · QUESTION 3 · OPPORTUNITY</p>

## Will AI narrow the wealth gap —<br>or widen it?

<p class="sub">Narrow it, widen it, or both? Give one reason.</p><div class="cards fragment" data-fragment-index="0"><div><span class="icon" data-icon="users"></span><h3>Could narrow it</h3><p>Lower-cost learning help<br>Support for beginners<br>Lower entry barriers</p></div><div><span class="icon" data-icon="chart"></span><h3>Could widen it</h3><p>Cost and usage limits<br>Unequal skills and support<br>Who owns the tools and profits?</p></div></div><p class="takeaway fragment" data-fragment-index="1">Same AI account. Same opportunities?</p><p class="footer"><a href="references/future.html#inequality" target="_blank" rel="noopener">Evidence on skills, access and income ↗</a></p>

Note:
16:07–16:09。先举手选“缩小”“扩大”或“两者都有”，请两位观点不同的同学各说一句原因，再展开两边提示。
“原来请不起辅导的人，可能第一次有了随时能提问的工具。一项对 5,172 名客服人员的研究中，经验较少、技能较低的员工获得了更明显的改善。这说明，在一些具体工作里，AI 可以帮助初学者追赶。”
“另一边，有人能支付更长时间的运行，有设备、有指导，也有把结果变成收入的机会。还有一个不同的问题：提高效率之后，新增收益属于谁？相关经济研究讨论了高收入劳动者与 AI 互补、以及资本收益增加，可能扩大收入和财富差距的机制。”这些是可能出现的路径；欢迎学生提出反例或两种路径同时成立的条件。对应来源见资料页。
第二下展开：“假设学校给每个人都发同样的 AI 账号，机会就完全一样了吗？除了账号，还需要什么？”可讨论网络、时间、学习指导、项目机会，不要求同学透露家庭收入或个人付费情况。
收束：“做某项工作的技能差距可以缩小，但财富差距仍可能扩大。更会做一件事，和能得到多少收益，是两个问题。”这是结合前述证据提出的讨论，不是对未来的确定预测。
转场：“现在回到你自己：你想真正学懂什么，又需要什么支持？”

---

<!-- .slide: id="future-reflection" class="future-discussion" -->
<p class="eyebrow">PART 6 · ONE MINUTE FOR YOURSELF</p>

## What should we keep learning?

<p class="sub">And what support do we need?</p><div class="reflection-lines"><p><span class="icon" data-icon="book"></span>One thing I want to understand deeply: <b>______</b></p><p><span class="icon" data-icon="sliders"></span>One task I want to do better with AI: <b>______</b></p><p><span class="icon" data-icon="users"></span>One resource or kind of support I need: <b>______</b></p></div><div class="timer" data-seconds="60"><output aria-live="off">01:00</output><button type="button" data-timer="toggle">Start</button><button type="button" data-timer="reset">Reset</button></div><p class="footer">Choose something that matters to you.</p>

Note:
16:09–16:10。开始计时，给学生完整的一分钟书写；分享留到 Q&A。
“回到刚才那个设想：即使 AI 能超过所有数学家，你还想学懂什么？我的想法是，学习不只是为了比谁做得快。我们可以把专业理解、使用工具的能力和判断力放在一起，也可以因为喜欢而继续学。”
“请写下三句话：我想真正理解什么，我想用 AI 做好什么，以及我需要什么资源或支持。最后一项很重要，我们刚才谈到的机会差异，并不全是个人努力能解决的。”
学生安静书写时不继续讲解。16:10 切到问答页，可从一个学生的答案开始。

---

<!-- .slide: id="questions" class="cover" -->
<p class="eyebrow">QUESTIONS & DISCUSSION</p>

## Keep learning.<br>Choose what matters.

<p class="lead">Use AI to think better — and go further.</p><p class="sub">Q&A · 16:10–16:30 HKT</p><p class="links"><a href="materials.html" target="_blank" rel="noopener">Student materials ↗</a> · <a href="prompts/index.html" target="_blank" rel="noopener">Prompt library ↗</a> · <a href="resources/google-study-tools.html" target="_blank" rel="noopener">Google tool guides ↗</a> · <a href="references/future.html" target="_blank" rel="noopener">Further reading ↗</a></p>

Note:
16:10–16:30问答。
今天我们从一道已经会做的作业题开始，练了怎样提问、怎样理解、怎样核查。工具还会不断变，但你可以继续选择自己想理解的问题，用更好的工具把它做得更深。今天最后的三个问题也都可以继续讨论：AI 擅长什么、谁能用到、谁能受益。可以先请一位同学分享刚才写下的学习目标或所需支持。

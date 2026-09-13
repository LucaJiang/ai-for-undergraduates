# Part 3 prompt pack: learning difficult concepts

These prompts are designed for undergraduate study conversations. They are not intended for ghostwriting, assignment outsourcing, or generating final submitted answers.

## 1. Hard concept tutor

```text
Role: Act as a patient tutor in [subject].

Context: I am trying to understand [concept]. I already know [what I know], but I am confused about [specific difficulty].

Constraints: Do not give a long textbook-style explanation. Start with intuition, then connect it to the formal definition. Do not solve my assignment for me.

Format:
1. One intuitive analogy
2. One formal explanation
3. One small worked example
4. One common misconception
5. One self-check question

After I answer the self-check question, critique my reasoning.
```

## 2. Socratic problem-solving guide

```text
Role: Act as a Socratic tutor.

Context: I am working on this problem: [paste problem]. I have tried this: [paste your attempt].

Constraints:
- Do not solve the problem for me.
- Do not reveal the final answer.
- Give only one hint at a time.
- Focus on the next thinking step.

Format:
1. Identify the type of problem.
2. Point out one relevant concept I should use.
3. Ask me one guiding question.
4. Wait for my response.
```

## 3. Multiple-representation explanation

```text
Role: Act as a tutor who explains concepts using multiple representations.

Context: I am learning [concept] in [course]. I get confused when the explanation switches between words, formulas, diagrams, and examples.

Constraints: Do not assume I already understand the notation. Do not skip the link between representations.

Format:
Explain the concept in five forms:
1. Plain language
2. Formal notation
3. Diagram description
4. Small numerical example
5. One real-world application

Then ask me to explain how two of these representations connect.
```

## 4. Misconception finder

```text
Role: Act as a critical but supportive tutor.

Context: Here is my current explanation of [concept]: [paste your explanation].

Constraints:
- Do not rewrite it immediately.
- First diagnose what is correct, incomplete, or wrong.
- Be specific about imprecise wording.

Format:
1. What I understood correctly
2. What is missing
3. What is incorrect or misleading
4. One better way to phrase the core idea
5. One follow-up question to test my understanding
```

## 5. Coding-assisted concept visualization

```text
Role: Act as a coding tutor, not a homework solver.

Context: I am trying to understand [concept] through a small simulation or visualization. I know basic Python, but I do not want a full project.

Constraints:
- Write the smallest useful script.
- Add comments explaining what each line teaches conceptually.
- Avoid unnecessary libraries.
- After the code, suggest two parameter changes I can try myself.

Format:
1. Short explanation of the idea
2. Minimal Python code
3. What I should observe
4. Two experiments I should run by changing the code
```

## 6. Cross-disciplinary examples

### STEM

```text
Role: Act as a linear algebra tutor.
Context: I know matrix-vector multiplication, but I do not understand the geometric meaning of eigenvectors.
Constraints: Explain intuition before proof. Use one 2D example. Do not assume I know diagonalization.
Format: Give an analogy, a diagram description, a numerical example, and one self-check question.
```

### Medicine

```text
Role: Act as a medical statistics tutor.
Context: I know sensitivity and specificity definitions, but I do not understand why positive predictive value changes with prevalence.
Constraints: Use a 2x2 table with simple numbers. Do not use Bayes' theorem until after the intuition.
Format: Explain intuition, then table, then formula, then one clinical interpretation question.
```

### Business / Economics

```text
Role: Act as an economics tutor.
Context: I am learning marginal effects and elasticity. I understand averages, but I do not understand “change at the margin.”
Constraints: Use a price-demand example. Do not rely only on calculus notation.
Format: Plain-language explanation, numerical example, graph description, and one decision-making question.
```

### Humanities / Social Science

```text
Role: Act as a writing and reasoning tutor.
Context: I am reading an argumentative essay and I struggle to separate claim, evidence, assumption, and counterargument.
Constraints: Do not summarize the essay. Reconstruct the argument structure.
Format: Claim / evidence / assumption / counterargument / one question that tests whether the argument is convincing.
```

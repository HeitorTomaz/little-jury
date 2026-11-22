# Domain profile: grant and funding proposals

- **Families:** criteria (the usual one: a bench of evaluators judges the proposal against the call's own evaluation grid, before submission). Audience is rarely useful here; use it only when the author wants to know how the people the project serves (the beneficiaries, a partner community) would receive it, and build those personas from `composition.md`.
- **Round 3 tests:** the proposal's objectives, schedule and budget against the call's requirements: each item puts one requirement of the call (eligibility, mandatory sections, budget rules, deadlines, expected results, page limits) or one commitment of the proposal (a milestone, a deliverable, a cost line) against what the proposal actually says.
- **Users label:** Evaluators

A starting point for evaluating a grant proposal, a research funding application, a public call for projects, a cultural or social project application, or an innovation program submission. The type is `work` (`references/work.md`): the proposal goes in verbatim, and its summary or abstract is the short pitch. **The call itself is the main source of criteria**: when the author gives the call document (the evaluation grid, the eligibility rules, the budget rules), save the evaluation grid verbatim in `input/03-criteria.md` and use its criteria and weights exactly; the default set below is only for when the author has no grid. The personas below are generic; **adapt them to the funder and the field** (a science foundation and a municipal culture fund have very different evaluators). Write them in the language recorded in `config.md`.

## Vocabulary

- Jurors are **evaluators** (or **reviewers**, **committee members**: use the funder's term); the report label (`meta.usersLabel`) is "Evaluators".
- "The work" is "the proposal"; "a revision" is a change the proposal needs before submission.
- A stance of **only if** is "fundable if …": the condition is the change requested, in one sentence.
- Proven problem: the proposal contradicts the call (a budget item the call forbids, a mandatory section missing, a duration above the limit), two parts of the proposal contradict each other (the schedule and the work plan, the budget table and the budget narrative), or the numbers do not add up. A weak argument is a hypothesis, not a proven problem.
- When the call gives weights or scores per criterion, the stances stay yes / only if / no; record the call's weights in `config.md` so the consolidation can say which split criteria weigh most. Do not invent a numeric score.

## Criteria (default set; replace with the call's grid whenever it exists)

| id | Name | Question |
|---|---|---|
| fit | Fit with the call | Does the proposal answer what this call funds, for whom and in which area, and meet its eligibility rules? |
| objectives | Objectives and relevance | Are the objectives specific and measurable, and is the need they answer shown with evidence? |
| plan | Work plan and schedule | Do the activities, milestones and schedule lead to the objectives within the call's duration? |
| budget | Budget | Is every cost justified, allowed by the call and consistent with the work plan? |
| capacity | Team and capacity | Can this team and institution carry out the plan, with the experience and partners shown? |
| results | Results and impact | Are the expected results, how they will be measured and what remains after the funding stated? |

Keep 3 to 7 criteria when there is no call grid. With a call grid, use all of its criteria, even if there are more.

## Evaluators (criteria family, lean: 6, 3 per model)

Distribute the strict and the lenient profiles across both models, so strictness is not confused with the model.

### specialist — Specialist evaluator of the area
- **Perspective:** knows the field and the state of the art; judges relevance and originality.
- **Strictness:** high on objectives and on what is already known; lenient on administration.
- **Reads first:** the objectives and the justification.
- **Tends to miss:** budget and eligibility problems.
- **Rejects when:** the proposal repeats what exists, or the need is asserted without evidence.

### compliance — Call compliance reviewer
- **Perspective:** checks the proposal against the call, line by line, before any merit is discussed.
- **Strictness:** very high on eligibility, mandatory sections, limits and forbidden costs; indifferent to merit.
- **Reads first:** the call's rules, then the proposal's structure and budget.
- **Tends to miss:** whether the project is any good.
- **Rejects when:** a mandatory item is missing or a rule is broken: in many calls, that alone disqualifies.

### generalist — Generalist panel member
- **Perspective:** sits on the panel from another area; must understand the proposal without the specialist's background.
- **Strictness:** medium; strict on clarity and on the summary.
- **Reads first:** the summary and the objectives.
- **Tends to miss:** technical weaknesses the text hides well.
- **Rejects when:** after the summary they still cannot say what will be done and why it matters.

### budget-reviewer — Budget and management reviewer
- **Perspective:** has managed funded projects and knows where they overrun.
- **Strictness:** very high on budget consistency, cost realism and the management plan.
- **Reads first:** the budget table and the schedule.
- **Tends to miss:** the scientific or social value.
- **Rejects when:** costs do not match activities, or the schedule cannot fit the work.

### impact-reviewer — Impact and beneficiaries reviewer
- **Perspective:** asks who benefits, how much, and how anyone will know.
- **Strictness:** high on results, indicators and continuity after the funding.
- **Reads first:** the expected results and the indicators.
- **Tends to miss:** method details.
- **Rejects when:** the results are activities ("we will hold workshops") rather than changes, or nothing can be measured.

### lenient — Supportive evaluator
- **Perspective:** looks for reasons to fund; reads generously and asks what would make the proposal fundable.
- **Strictness:** low; still names the weakest point.
- **Reads first:** whatever the proposal is proudest of.
- **Tends to miss:** problems the proposal does not mention.
- **Rejects when:** even read generously, the proposal does not fit the call.

### Reserved for the full panel
- **funder-staff:** a program officer of the funder who knows what was funded in earlier rounds and what the program wants more of.
- **partner:** a representative of a partner institution named in the proposal; checks that its role is real and agreed.

## Experts

### methods — Methods and work plan specialist
Evaluates whether the activities can reach the objectives: methods, sequence, dependencies, risks and the indicators of success. Asks: which objective has no activity that reaches it? Which milestone depends on something not yet secured (a permit, a partner, a hire)? Are the indicators measurable with what the project will collect?

### budget — Budget specialist
Evaluates the budget against the work plan and the call's rules: eligible and ineligible costs, overheads, matching funds, cost realism, the timing of spending. Asks: rebuild the total from the budget lines; does it match the requested amount? Which cost is not linked to any activity? Which item might the call not allow?

### program — Program and evaluation specialist
Evaluates how evaluators of this kind of call read proposals: the weight of each criterion, common reasons for rejection, the clarity of the summary, and the alignment of the proposal's language with the call's priorities. Asks: if an evaluator reads only the summary and the objectives, what score would they give? Which priority of the call does the proposal not mention?

### call — Call and regulations specialist (the only one who gets web access, in round 2)
Evaluates the call and the rules around it: eligibility, deadlines, required documents, applicable regulations, and earlier funded projects when the funder publishes them. When this persona has web access in a round, it checks the call document and its annexes, the funder's published rules and frequently asked questions, and lists of earlier funded projects in the official sources, and marks [not verified] what it could not check; without web access, it says it is answering without checking.

### Reserved for the full panel
- **ethics — Ethics and data specialist:** consent, data protection and ethics approval when the project involves people or personal data.

## Typical additional questions (they go into `config.md` when they apply)

- **Evaluators, round 1:** "Which single change would most improve this proposal's chance under this call?" (already in `rounds-criteria.md` as the revision question; keep it).
- **Evaluators, round 1:** when the call gives scores per criterion, record its weights in `config.md` and ask each evaluator which criterion they think weighs the proposal down most, without asking for a number.
- **budget, round 2:** "List every budget line with the activity it pays for; mark the lines with no activity and the activities with no cost."
- **methods, round 2:** "Lay the schedule over the call's duration: which milestones fall outside it or overlap impossibly?"
- **call, round 2:** check every eligibility rule and mandatory document in the call and its annexes against the proposal, saying what could not be checked.
- **Round 3:** one item per binding requirement of the call (eligibility, limits, mandatory sections, budget rules) and one per central commitment of the proposal (each main objective, the main milestone, the largest cost), stated neutrally ("Consider the call's requirement X. The proposal's corresponding section: Y.").

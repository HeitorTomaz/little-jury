# Domain profile: scientific papers

- **Families:** criteria (the usual one: a bench of reviewers judges the paper as in peer review, before submission). Audience when the author wants to know how readers would receive it (a review article, a paper written for practitioners, science communication); then use the readers below.
- **Round 3 tests:** the paper's central claims against the strongest objections and alternative explanations (a confounder, a sample that cannot carry the claim, a result that also fits another explanation, a conclusion that goes beyond the data).
- **Users label:** Reviewers (criteria) · Readers (audience)

A starting point for evaluating a scientific paper, a preprint or a manuscript before submission. The type is `work`: the paper goes into the panel verbatim (`references/work.md`), and the abstract is the short pitch. The personas below are generic; **adapt them to the paper's field and method** (a qualitative study needs a different methodologist than a randomized trial), and use the target journal's guidelines as criteria when the author gives them. Write them in the language recorded in `config.md`.

## Vocabulary

- In the criteria family, jurors are **reviewers**; the report label (`meta.usersLabel`) is "Reviewers". In the audience family, users are **readers** ("Readers").
- "The work" is "the paper"; "a revision" is what a reviewer would ask for in a report.
- A stance of **only if** is a "minor or major revision": the condition is the revision requested, in one sentence.
- Proven problem: two passages of the paper contradict each other, or the text contradicts its own tables, figures or reported numbers. A claim the data do not support well enough is a hypothesis, not a proven problem.

## Criteria (default set; replace with the journal's or the author's when given)

| id | Name | Question |
|---|---|---|
| originality | Originality | Does the paper say something that is not already established, and does it say what is new? |
| method | Method fits the question | Can the design, sample and analysis answer the research question as stated? |
| evidence | Evidence supports the claims | Do the results, as reported, carry the conclusions, without going beyond them? |
| clarity | Clarity | Can a reviewer from the field follow the argument, the method and the results without guessing? |
| limits | Limitations and ethics | Are the limitations, possible biases and ethical aspects stated where they matter? |

Keep 3 to 7 criteria. A journal's own review form, when the author has one, is better than this set: save it verbatim in `input/03-criteria.md`.

## Reviewers (criteria family, lean: 6, 3 per model)

Distribute the strict and the lenient profiles across both models, so strictness is not confused with the model.

### area — Reviewer from the area
- **Perspective:** knows the literature of the subfield and the usual way of doing this kind of study.
- **Strictness:** medium to high on originality and on what is missing from the literature.
- **Reads first:** the introduction and the related work, then the conclusions.
- **Tends to miss:** problems in the statistics, if the narrative is convincing.
- **Rejects when:** the contribution is already published, or the paper ignores the work it should answer.

### methodologist — Methodologist
- **Perspective:** judges whether the design can answer the question, independently of the topic.
- **Strictness:** high on method, low on style.
- **Reads first:** the method section and the tables.
- **Tends to miss:** whether the question matters to the field.
- **Rejects when:** the design cannot separate the effect from obvious alternatives, or the analysis was chosen after seeing the data.

### neighbour — Reviewer from a neighbouring field
- **Perspective:** works on related problems with different tools; checks whether the paper makes sense outside its niche.
- **Strictness:** medium; strict on unexplained jargon and on assumptions the subfield takes for granted.
- **Reads first:** the abstract and the figures.
- **Tends to miss:** subfield conventions that are actually fine.
- **Rejects when:** the paper's claims only hold if one accepts assumptions it never states.

### practitioner — Practitioner
- **Perspective:** would apply the result (in a clinic, a classroom, a company, a lab); asks what changes in practice.
- **Strictness:** lenient on novelty, strict on whether the conditions of the study resemble real ones.
- **Reads first:** the discussion and the practical implications.
- **Tends to miss:** methodological detail.
- **Rejects when:** the recommendation does not follow from a setting this artificial.

### early-career — Early-career researcher
- **Perspective:** reads carefully, checks every number, and is afraid of missing something.
- **Strictness:** high on internal consistency (numbers in the text versus the tables, n across sections).
- **Reads first:** everything, in order.
- **Tends to miss:** the big picture: whether the question was worth asking.
- **Rejects when:** the numbers do not add up.

### editor — Handling editor
- **Perspective:** decides whether the paper fits the journal and is worth the reviewers' time; reads for the main claim and its weakest point.
- **Strictness:** lenient on detail, strict on fit and on the gap between the title's promise and the results.
- **Reads first:** the title, the abstract and the last paragraph.
- **Tends to miss:** problems hidden in the method.
- **Rejects when:** the paper promises more than it shows, or belongs to another kind of venue.

### Reserved for the full panel
- **replicator:** would try to reproduce the study; strict on whether the paper gives enough detail (materials, code, data availability) to do it.
- **statistician-reviewer:** a reviewer whose only focus is the analysis plan and the reporting of effects and uncertainty.

## Readers (audience family, lean: 8)

Use these when the question is how the paper will be received, not whether it should be accepted. The eighth seat is the **audience the author imagines**.

- **specialist-reader:** reads everything in the subfield; quits when the paper repeats what they know.
- **student:** reads to learn the topic; quits when the paper assumes knowledge it never points to.
- **practitioner-reader:** looks for something to apply; quits when there is no "so what".
- **skimmer:** reads the abstract, the figures and the conclusion; quits when those three do not tell the story.
- **skeptic-reader:** expects hype; quits at the first claim that outruns the data.
- **outsider:** from another field, curious; quits at the first wall of jargon.
- **policy-reader:** reads for decisions (funding, regulation, guidelines); quits when the uncertainty is not stated plainly.
- **<id> — audience imagined by the author.**

Grid questions for readers: `curiosity` "Would you read past the abstract?"; `value` "Would it change what you know or do?"; `ease` "Could you follow it without outside help?"; `would_try` "Would you cite it or pass it on?".

## Experts

### statistician — Statistician
Evaluates the analysis: whether the tests fit the data and the design, effect sizes and uncertainty, multiple comparisons, missing data, and whether the numbers reported are consistent with each other. Asks: what is the smallest effect this sample could detect? Which analysis decision, made differently, would change the conclusion? Are there numbers that do not add up?

### specialist — Specialist of the topic
Evaluates the paper's place in its field: what is new, what is missing from the literature, whether the interpretation fits what is known. Asks: which known result does this contradict or repeat? What alternative explanation would a specialist raise first? Which claim is the paper's real contribution?

### integrity — Sources and research integrity specialist (the only one who gets web access, in round 2)
Evaluates citations, data availability, ethics approval and reporting standards. When this persona has web access in a round, it checks that cited works exist and say what the paper says they say, that the reporting guideline for this kind of study is followed, and that the journal's requirements are met, marking [not verified] what it could not check (paywalls, unreachable sources); without web access, it says it is answering without checking.

### Reserved for the full panel
- **writing — Scientific editor:** evaluates structure, the abstract and the title, and whether each section does its job.

## Typical additional questions (they go into `config.md` when they apply)

- **Reviewers, round 1:** "Which single revision would change your recommendation most?" (already in `rounds-criteria.md`; keep it).
- **statistician, round 2:** "Is the sample size justified? What would a power or precision analysis say about the main comparison?"
- **specialist, round 2:** "Name the two or three works a reviewer would expect to see discussed, and whether the paper does."
- **integrity, round 2:** check a sample of the citations (the ones that carry the main claims), the target journal's author guidelines and the reporting checklist that applies to this design.
- **Round 3:** for each central claim, include the alternative explanation the reviewers raised most often, written neutrally ("Consider the claim X. Another reading of the same result: Y.").

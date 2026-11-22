# Domain profile: theses and dissertations

- **Families:** criteria (the usual one: a committee judges the thesis before the defense). Audience only when the author wants to know how a non-specialist reader would follow it (for example, a capstone written for a company); then use the readers of `paper.md`.
- **Round 3 tests:** the thesis's central claims and its research question against the committee's strongest objections: does the method answer the question, do the conclusions follow from the results, would a different reading of the data change the conclusion.
- **Users label:** Committee

A starting point for evaluating a thesis, a dissertation, a capstone or final course project (TCC), or a qualifying exam text, before the defense. The type is `work`: the text goes into the panel verbatim (`references/work.md`); a thesis is long, so the question block asks which chapters are in scope, and the abstract is the short pitch. The personas below are generic; **adapt them to the program and the field**, and use the program's regulation or evaluation form as criteria when the author gives it. Write them in the language recorded in `config.md`.

## Vocabulary

- Jurors are **committee members**; the report label (`meta.usersLabel`) is "Committee".
- A stance of **only if** is "approved with revisions": the condition is the revision requested, in one sentence.
- "The defense" is the moment the committee questions the author; round 3 is a rehearsal of its hardest questions.
- Proven problem: two passages of the thesis contradict each other, the text contradicts its own data, or it breaks a rule of the regulation the author gave.

## Criteria (default set; replace with the program's regulation or evaluation form when given)

| id | Name | Question |
|---|---|---|
| question | Research question | Is the research question (or objective) clear, relevant and feasible at this level? |
| literature | Literature | Does the review cover the work the question depends on, and use it, rather than list it? |
| method | Method | Can the method, as described, answer the question, and is it described well enough to be followed? |
| results | Results and conclusions | Are the results presented clearly, and do the conclusions follow from them without going further? |
| writing | Writing and norms | Is the text clear and organized, and does it follow the formatting and citation norms required? |

The level matters: a capstone (TCC) is not judged like a doctoral thesis. Record the level in `config.md` and tell the committee in the prompt.

## Committee (criteria family, standard: 6, 3 per model; quick: 4; deep: 9)

Distribute the strict and the lenient profiles across both models, so strictness is not confused with the model.

### advisor-like — Member close to the advisor's view
- **Perspective:** knows what the student set out to do and judges whether they did it.
- **Strictness:** lenient on scope, strict on whether the promised objectives were met.
- **Reads first:** the objectives and the conclusions, side by side.
- **Tends to miss:** weaknesses the advisor also has a stake in.
- **Rejects when:** the thesis abandoned its own question halfway.

### external — External member
- **Perspective:** from another institution; owes nothing to the program and reads with fresh eyes.
- **Strictness:** high on originality and on the gap between the thesis and the published literature.
- **Reads first:** the introduction and the related work.
- **Tends to miss:** local program conventions that are acceptable.
- **Rejects when:** the contribution is not clear, or ignores work everyone in the field knows.

### methodologist — Methodologist
- **Perspective:** judges whether the design can answer the question, independently of the topic.
- **Strictness:** high on method and on the link from data to conclusion.
- **Reads first:** the method chapter.
- **Tends to miss:** the relevance of the question.
- **Rejects when:** the method cannot answer the question as stated.

### specialist — Specialist of the topic
- **Perspective:** knows the subject deeply; checks that the content is right.
- **Strictness:** high on technical errors, medium on everything else.
- **Reads first:** the core chapters.
- **Tends to miss:** problems of structure and writing.
- **Rejects when:** there is a conceptual error at the center of the work.

### neighbour — Member from a neighbouring area
- **Perspective:** could have been invited for the interdisciplinary angle; asks what the work means outside its niche.
- **Strictness:** medium; strict on unexplained assumptions and jargon.
- **Reads first:** the abstract and the conclusions.
- **Tends to miss:** subfield conventions that are fine.
- **Rejects when:** the conclusions only hold for readers who already agree.

### norms — Member strict on norms and writing
- **Perspective:** reads the text as a document that must meet the program's rules: structure, citations, formatting, language.
- **Strictness:** high on form, low on content.
- **Reads first:** the table of contents, the references and a sample of the citations.
- **Tends to miss:** problems of substance.
- **Rejects when:** the text does not meet mandatory norms, or plagiarism-like reuse appears without citation.

### Reserved for the deep level
- **future-reader:** a student who would build on this thesis next year; asks what they could actually reuse.

## Experts

### methodology — Research methods specialist
Evaluates design, sampling, instruments, analysis and their fit to the question. Asks: which threat to validity is not addressed? What would a stricter design have changed? Which result depends on an analysis choice the text does not justify?

### field — Field specialist
Evaluates the content and its place in the literature. Asks: what is the thesis's actual contribution, in one sentence? Which known work does it contradict or repeat? What will the committee's first hard question be?

### sources — Sources and norms specialist (the only one who gets web access, in round 2)
Evaluates citations and compliance with the norms the program requires. When this persona has web access in a round, it checks that the main cited works exist and say what the thesis says they say, and the citation and formatting standard the author named, marking [not verified] what it could not check; without web access, it says it is answering without checking.

## Typical additional questions (they go into `config.md` when they apply)

- **Committee, round 1:** "What is the question you would ask first at the defense?"
- **methodology, round 2:** "If the committee asks for one more analysis or one more source of data, which one, and would it change the conclusion?"
- **field, round 2:** "Which limitation should the author state before the committee points it out?"
- **Round 3:** include the defense questions the committee raised most often, as claims under challenge.

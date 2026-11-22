# Domain profile: exams and exam answers

- **Families:** both, for two different requests.
  - **Audience** when a teacher wants to know whether **an exam** is fair and clear before giving it: the panel is students facing the exam, and the experts look at the exam and its answer key.
  - **Criteria** when someone wants **an answer graded** against its answer key or rubric (a second opinion on a grade, or calibration between graders): the panel is a bench of graders, and the answer is the work. One answer per panel; two to five answers make two to five panels. A whole class is out of scope for now: say so if asked.
- **Round 3 tests:** audience: the exam's questions against possible answers (a correct answer the key would penalize, an ambiguous reading of the statement, a question answerable without the knowledge it should measure). Criteria: the answer's key steps against the answer key and the graders' objections.
- **Users label:** Students (audience) · Graders (criteria)

A starting point for evaluating an exam, a test, an assignment brief or a graded answer. The type is `work`: the exam (or the answer) goes into the panel verbatim (`references/work.md`); the instructions on the exam's first page are the short pitch. The personas below are generic; **adapt them to the subject and the level** (a university calculus exam is not a primary school reading test). Write them in the language recorded in `config.md`.

## Who receives what

- **Audience family:** students receive **the exam only**, as a student would; they never see the answer key. Experts receive the exam **and** the answer key or rubric, saved in `input/03-criteria.md`. Record this in `prep/decisions.md`.
- **Criteria family:** graders and experts receive the answer, the question it answers, and the answer key or rubric (`input/03-criteria.md`). Anonymize the answer (no name, no class, no identifying detail) and never show one student's answer in another student's panel.

## Vocabulary

- **Audience family:** users are **students**; "use" becomes "take the exam"; "first 15 minutes of use" becomes "the first 15 minutes of the exam". Grid questions: `curiosity` becomes **Understood the task** ("After reading the instructions, do you know what is asked and how you will be graded?"); `value` **Fair** ("Does the exam measure what the course taught, without tricks?"); `ease` **Doable in the time** ("Could a well-prepared student finish it in the time given?"); `would_try` **Would show what you know** ("Would this exam let you show what you know?").
- **Criteria family:** jurors are **graders**; the criteria are the items of the answer key or rubric, one per criterion, each answered "Does the answer meet <item>?". A stance of **only if** is partial credit: the condition says what is missing. The report label is "Graders".

## Students (audience family, standard: 8; quick: 4; deep: 11)

The eighth seat is the **student the teacher has in mind** (the typical student of this class, as the teacher describes it).

### prepared — Well-prepared student
- **Perspective:** studied the whole syllabus and wants the exam to reward it.
- **Test-taking style:** reads everything first, plans the time.
- **Tolerance for ambiguity:** low. Will ask "what exactly does this mean?" and lose time.
- **Looks for:** questions that separate understanding from memorization.
- **Feels it is unfair when:** a question depends on a detail that was never taught, or has two right answers.

### anxious — Anxious student
- **Perspective:** knows more than they can show under pressure.
- **Test-taking style:** starts at question one and gets stuck.
- **Tolerance for ambiguity:** very low; a confusing statement costs them the next question too.
- **Looks for:** clear statements and a predictable layout.
- **Feels it is unfair when:** the first question is the hardest, or the wording hides an easy question.

### strategic — Strategic student
- **Perspective:** maximizes points with minimum effort; looks for what the grader wants.
- **Test-taking style:** skims, answers the cheapest questions first, writes what scores.
- **Tolerance for ambiguity:** high; uses it to their advantage.
- **Looks for:** patterns in the answer key: keywords, formats.
- **Feels it is unfair when:** never; but they show where the exam can be passed without understanding.

### struggling — Student who struggled with the course
- **Perspective:** understood part of the syllabus and wants a chance to show that part.
- **Test-taking style:** answers what they can, leaves the rest.
- **Tolerance for ambiguity:** low.
- **Looks for:** partial credit and questions that build up step by step.
- **Feels it is unfair when:** one early mistake makes every later step worthless.

### second-language — Student in a second language
- **Perspective:** knows the subject, reads the exam slowly in a language that is not their first.
- **Test-taking style:** careful, rereads statements.
- **Tolerance for ambiguity:** very low for wording; idioms and long sentences cost them time, not knowledge.
- **Looks for:** plain wording.
- **Feels it is unfair when:** a question tests reading speed or cultural references instead of the subject.

### lateral — Lateral thinker
- **Perspective:** solves problems in unexpected but valid ways.
- **Test-taking style:** takes the statement literally and finds the reading nobody planned.
- **Tolerance for ambiguity:** high; finds it everywhere.
- **Looks for:** credit for a correct method that is not the one in the key.
- **Feels it is unfair when:** the key accepts only one method or one wording.

### pressed — Student short on time
- **Perspective:** works or has other exams the same week; studied the essentials only.
- **Test-taking style:** fast, skips long statements.
- **Tolerance for ambiguity:** low.
- **Looks for:** an exam whose length matches the time.
- **Feels it is unfair when:** reading the statements takes a large share of the time.

### <id> — Student the teacher has in mind
Write it from what the teacher said about the class. A made-up example, only as a form:
- **Perspective:** second-year student who follows the classes but rarely does the exercises at home.
- **Test-taking style:** recognizes problems seen in class; struggles with new ones.
- **Tolerance for ambiguity:** medium.
- **Looks for:** questions that look like the ones from class.
- **Feels it is unfair when:** a question uses a context never seen in class to test a known idea.

## Graders (criteria family, standard: 6, 3 per model; quick: 4; deep: 9)

Distribute the strict and the lenient graders across both models, so strictness is not confused with the model. Write each with **Perspective, Strictness, Reads first, Tends to miss, Rejects when**, as in `paper.md`:

- **strict:** grades exactly by the key; partial credit only where the rubric says so.
- **lenient:** credits the idea even when the execution is imperfect.
- **specialist:** checks whether the answer is right even where the key did not foresee it (an alternative valid method).
- **previous-level teacher:** knows what students at this stage usually get wrong and why.
- **pedagogue:** judges whether the answer shows understanding or memorization.
- **peer grader:** another teacher of the same course, grading the same exam this week; checks consistency with how the rest of the class would be graded.

## Experts

### assessment — Assessment specialist
Evaluates whether the exam measures what it should: alignment with the course objectives, difficulty spread, time, partial credit, the answer key's coverage. Asks: which question can be answered without the knowledge it should measure? Which correct answer would the key penalize? Is the time realistic?

### subject — Subject specialist
Checks the content: whether statements are correct and unambiguous, whether the key's answers are right, whether alternative valid answers exist. Asks: which statement allows two readings? Which key answer is wrong or incomplete?

### accessibility — Accessibility and language specialist (the only one who gets web access, in round 2)
Evaluates wording, layout, reading load and accommodations. When this persona has web access in a round, it checks the accessibility and assessment guidelines the institution or exam board applies, marking [not verified] what it could not check; without web access, it says it is answering without checking.

## Typical additional questions (they go into `config.md` when they apply)

- **Students, round 2 (audience):** "Which question would you leave for last, and why?" and "Where did you have to guess what the teacher wanted?"
- **assessment, round 2:** "Estimate the time a prepared student needs per question, and the total."
- **subject, round 2:** "For each question, is there a correct answer the key does not accept?"
- **Round 3 (audience):** for each question, possible answers from different students (a correct unexpected method, a literal reading, a partial answer), written neutrally; participants say how the key as written would grade each, and whether that is right.
- **Round 3 (criteria):** the answer's key steps, each against the objection a strict grader raised, and the alternative method a specialist would accept.

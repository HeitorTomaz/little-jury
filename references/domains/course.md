# Domain profile: courses, classes and lesson plans

- **Families:** audience (the usual one: students with different profiles react to the course as it is planned). Criteria when the course must pass a pedagogical review: a curriculum committee, an accreditation requirement, a school's or a platform's teaching rubric; then that document is the criteria.
- **Round 3 tests:** the activities and the assessments against the learning objectives; the plan against the students it will actually meet (one who falls behind in the third week, one who already knows half of it, one who misses a class); the workload week by week, looking for peaks.
- **Users label:** Students (audience) · Reviewers (criteria)

A starting point for evaluating a course, a single class, a training program, a workshop or a lesson plan, in person or online, before it is taught. The type is usually `work` (the syllabus, the plan, the materials go in verbatim, `references/work.md`) or `concept` when the course is still an idea. The short pitch is the course description as a student would see it (the catalog text, the enrollment page). The personas below are generic; **adapt them to the level and the setting** (a primary-school class, a university course, a corporate training and an online course for adults have different students and different constraints). Write them in the language recorded in `config.md`.

## Vocabulary

- In the audience family, users are **students** ("Students"); for corporate training, "participants". In the criteria family, jurors are **reviewers** ("Reviewers").
- "First 15 minutes of use" becomes "the first class" (or "the first week" for a longer course).
- A stance of **only if** in the criteria family is "approve with changes": the condition is the change.
- Proven problem: two parts of the plan contradict each other (an assessment that tests what no activity teaches, a prerequisite used before it is taught, a schedule that does not add up), or the plan contradicts an explicit rule the author gave (the hours of the course, the curriculum it must follow).

## Students (audience family, standard: 8; quick: 4; deep: 11)

The eighth seat is the **audience the author imagines**. When someone is affected by the course without taking it (the parents of young students, the manager who pays for a training), give one seat to them and say so in **Relation to the project**: their answer to a question that does not fit them is "does not apply".

### prepared — Well-prepared student
- **Perspective:** has the prerequisites and wants to go further.
- **Relation to the project:** would take the course.
- **Usually learns with:** reading ahead, exercises, asking questions in class.
- **Tolerance for complexity:** high.
- **Time:** what the course asks, and some more.
- **Looks for:** challenge and a clear path to mastery.
- **Quits when:** the pace is set for the slowest, or the material repeats what they know.

### struggling — Student who struggles
- **Perspective:** is missing part of the prerequisites and knows it.
- **Relation to the project:** would take the course, often because it is required.
- **Usually learns with:** worked examples, step by step, help from peers.
- **Tolerance for complexity:** low. Gets lost when two new ideas arrive at once.
- **Time:** more than the course expects, when they can.
- **Looks for:** knowing what to review and where to get help.
- **Quits when:** they fall behind once and see no way to catch up.

### working-adult — Working adult
- **Perspective:** studies around a job and a family; every hour counts.
- **Relation to the project:** would take the course for a concrete goal.
- **Usually learns with:** short sessions, at night or on weekends, on the phone.
- **Tolerance for complexity:** medium, if the use is clear.
- **Time:** little, fragmented, unpredictable.
- **Looks for:** relevance to their work and flexibility.
- **Quits when:** the course demands fixed times they cannot keep, or work they cannot see the point of.

### fast — Fast learner
- **Perspective:** understands quickly and gets bored quickly.
- **Relation to the project:** would take the course.
- **Usually learns with:** skimming, then jumping to the hard parts.
- **Tolerance for complexity:** very high.
- **Time:** variable; intense when interested.
- **Looks for:** optional depth and the freedom to move ahead.
- **Quits when:** everyone must wait for everyone, or the assessments reward compliance over understanding.

### second-language — Student in a second language
- **Perspective:** understands the content but not always the language of instruction.
- **Relation to the project:** would take the course.
- **Usually learns with:** written materials, translations, rereading.
- **Tolerance for complexity:** medium on content, low on dense language.
- **Time:** more for reading than others.
- **Looks for:** clear written instructions and vocabulary support.
- **Quits when:** the assessments test language more than content.

### constrained — Student with access needs
- **Perspective:** has a disability, a slow connection, an old device or caring responsibilities that shape how they can study.
- **Relation to the project:** would take the course.
- **Usually learns with:** whatever format works with their constraint (captions, text versions, offline materials).
- **Tolerance for complexity:** medium.
- **Time:** depends on the constraint.
- **Looks for:** materials and activities they can actually access.
- **Quits when:** a required activity is impossible for them and there is no alternative.

### skeptic — Reluctant student
- **Perspective:** is there because they must be; doubts the course will matter.
- **Relation to the project:** required to take it.
- **Usually learns with:** the minimum needed to pass.
- **Tolerance for complexity:** low.
- **Time:** as little as possible.
- **Looks for:** a reason to care, early.
- **Quits when:** the first class gives no reason, or the effort seems out of proportion to the result.

### <id> — Audience imagined by the author
Write it from what the author declared about who the course is for.

### Reserved for the deep level
- **returning:** comes back after years away from studying; needs confidence more than content.
- **assistant:** a teaching assistant or tutor who would help run the course; reads for what will go wrong in practice.

## Reviewers (criteria family, standard: 6, 3 per model; quick: 4; deep: 9)

Profiles of the people who approve a course: an instructional designer, a teacher of the subject, a program coordinator, a student representative, an accessibility reviewer and an external examiner. Write each with **Perspective, Strictness, Reads first, Tends to miss, Rejects when**, as in `paper.md`, and spread the strict and lenient profiles across both models.

## Criteria (criteria family; default set, replace with the institution's rubric when given)

| id | Name | Question |
|---|---|---|
| objectives | Clear objectives | Are the learning objectives stated so that one could check, at the end, whether a student reached them? |
| alignment | Alignment | Do the activities teach, and the assessments measure, what the objectives say? |
| sequence | Sequence | Does each part build on what came before, with prerequisites taught or stated before they are used? |
| workload | Workload | Is the work asked of students realistic for the hours and the students the course has? |
| assessment | Fair assessment | Are the assessments transparent, with criteria students know in advance, and fair to students who reached the objectives? |
| inclusion | Inclusion | Can students with different backgrounds, languages and access needs take part in every required activity? |

## Experts

### pedagogy — Learning design specialist
Evaluates the structure: objectives, alignment, the balance of explanation and practice, feedback, assessment. Asks: what does a student do in each class, minute by minute? Where is the first point a student can fall behind without anyone noticing? Which assessment measures something no activity prepares for?

### subject — Specialist of the subject
Evaluates whether the content is correct, current and at the right level, and what is missing. Asks: which concept is taught in a way that will have to be unlearned later? Which topic is missing that the next course will assume? Which example is out of date?

### standards — Curriculum and standards specialist (the only one who gets web access, in round 2)
Evaluates the course against the rules it must follow: national curriculum or standards, accreditation requirements, the institution's or platform's rules, accessibility requirements for educational materials. When this persona has web access in a round, it checks the current official documents that apply where the course will be taught, marking [not verified] what it could not check; without web access, it says it is answering without checking.

### Reserved for the deep level
- **assessment — Assessment specialist:** evaluates the reliability and fairness of the exams and rubrics in detail (`exam.md` covers a single exam in depth).

## Grid questions

For students: `curiosity` "Would you come back after the first class?"; `value` "Would you learn something you need?"; `ease` "Could you keep up with the pace and the workload?"; `would_try` "Would you finish it, and recommend it?". For a required course, `would_try` becomes "Would you take it if it were optional?".

## Typical additional questions (they go into `config.md` when they apply)

- **Students, round 2:** "In which week would you most likely fall behind, and why?" (spread the weeks or modules across students, as with paths in `rounds.md`).
- **Students, round 2:** "Which activity would you skip if you could, and what would you lose?"
- **pedagogy, round 2:** "If the course lost a fifth of its hours, what would go?"
- **standards, round 2:** the curriculum, standards or accreditation rules that apply where the course will be taught; if there is a list of course titles, rank them for the intended students.
- **Round 3:** for each objective, include the student situation the panel raised that most threatens it, written neutrally ("Consider objective X. A student who Y.").

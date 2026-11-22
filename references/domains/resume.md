# Domain profile: CVs and cover letters

- **Families:** criteria (the usual one: a bench of recruiters judges the CV and the cover letter against a real job posting the author gives). Audience is rarely useful here: a CV has one reader who decides, and that reader is already on the bench.
- **Round 3 tests:** the CV's central claims (achievements, skills, the story of the career) against the questions an interviewer would ask about them and against the posting's requirements; gaps and turns in the career (a pause, short jobs, a change of field) against how a screener reads them in a few seconds.
- **Users label:** Recruiters

A starting point for evaluating a CV (résumé) and, when there is one, its cover letter, **for one specific job**. The type is `work`: the CV and the letter go into the panel verbatim (`references/work.md`), and the job posting is the source of the criteria, saved verbatim in `input/03-criteria.md`. Without a real posting, ask for one in the question block; a CV judged against no job can only be judged on form. The personas below are generic; **adapt them to the field, the seniority and the country of the job** (a CV for a research post, a sales role and a public-service exam are read in very different ways). Write them in the language recorded in `config.md`.

Two rules that matter more here than anywhere else:

- **Remove what identifies the person and invites bias** before the panel sees the CV: name, photo, date of birth or age, address, contact details, marital status, nationality when the job does not require it. Replace the name by "the candidate" and record what was removed in `prep/removed.md`. The jurors judge the document, not the person.
- **Never suggest what the candidate did not do.** A quick win can reorder, cut, rewrite or make a real achievement measurable; it can never add an experience, a skill, a title or a number that is not in the material. When the posting asks for something the candidate lacks, the panel says so and suggests how to address it honestly (in the letter, in the interview), never how to hide it.

## Vocabulary

- Jurors are **recruiters**; the report label (`meta.usersLabel`) is "Recruiters".
- "The work" is "the application" (CV plus letter); "a revision" is a change to the CV or the letter.
- A stance of **only if** means "would move forward only with this change", and the condition is the change, in one sentence.
- Proven problem: two passages of the application contradict each other (dates that overlap where they should not, a title in the CV that differs from the one in the letter, a skill listed and then contradicted), or the application contradicts an explicit, mandatory requirement of the posting. A requirement the CV does not show clearly is a hypothesis: maybe the candidate has it and did not say so.

## Criteria (default set; derive the real ones from the posting)

Turn the posting's mandatory requirements, its desirable ones and the way it describes the job into 3 to 7 criteria. Without anything better, use:

| id | Name | Question |
|---|---|---|
| fit | Fit to the requirements | Does the application show that the candidate meets the posting's mandatory requirements? |
| evidence | Evidence of results | Are the achievements concrete (what changed, how much, for whom), rather than a list of duties? |
| scan | Readable in seconds | Can a screener find the role, the level and the key skills in the first few seconds? |
| tailoring | Tailored to this job | Does the application speak to this job and this employer, rather than to any job? |
| consistency | Consistency | Do dates, titles, numbers and claims agree across the CV and the letter? |
| letter | Cover letter | Does the letter add something the CV does not say (motivation, a link to the job, an explanation)? No letter: "does not apply". |

## Recruiters (criteria family, standard: 6, 3 per model; quick: 4; deep: 9)

Distribute the strict and the lenient profiles across both models, so strictness is not confused with the model.

### screener — Screening recruiter
- **Perspective:** reads hundreds of applications for many jobs; decides in a few seconds whether this one goes to the next stage.
- **Strictness:** high on the mandatory requirements and on readability, low on nuance.
- **Reads first:** the current or last role, its dates and the skills section.
- **Tends to miss:** a strong achievement buried in the middle of a paragraph.
- **Rejects when:** a mandatory requirement is not visible, or the document takes effort to read.

### hiring-manager — Hiring manager
- **Perspective:** will work with the person every day; reads for what they have actually done and how they think.
- **Strictness:** lenient on form, strict on substance and on claims that sound inflated.
- **Reads first:** the last two roles and the achievements under them.
- **Tends to miss:** problems of format that the screener would have stopped at.
- **Rejects when:** the achievements are duties in disguise, or the level of the experience does not match the level of the job.

### hr — HR business partner
- **Perspective:** looks at the whole trajectory, the fit with the organization and the practical conditions of the hire.
- **Strictness:** medium; strict on consistency and on the explanation of gaps and changes.
- **Reads first:** the timeline, from the oldest role to the newest.
- **Tends to miss:** technical depth.
- **Rejects when:** the trajectory raises questions the application does not answer.

### ats — Automated screening view
- **Perspective:** reads like a keyword and requirement filter: literal, with no inference, and no credit for what is not written in plain words.
- **Strictness:** very high on exact terms, titles and qualifications named in the posting; indifferent to style.
- **Reads first:** the whole text as plain text, looking for the posting's terms.
- **Tends to miss:** everything that is said with other words, inside images or tables, or implied.
- **Rejects when:** the posting's key terms or required qualifications do not appear as written. This persona judges what a filter would see; it never recommends stuffing keywords the candidate cannot back.

### peer — Peer in the field
- **Perspective:** does the same kind of work; knows what is impressive and what is routine in it.
- **Strictness:** high on technical credibility, lenient on presentation.
- **Reads first:** the skills, the projects and the tools named.
- **Tends to miss:** what a non-specialist screener needs to see spelled out.
- **Rejects when:** the claims do not hold together technically, or the routine is presented as remarkable.

### teammate — Future teammate
- **Perspective:** would share the work with the candidate; reads for how they collaborate and what they would bring to the team.
- **Strictness:** lenient on the requirements, strict on tone and on the letter.
- **Reads first:** the letter, then the most recent role.
- **Tends to miss:** formal requirements and gaps in the timeline.
- **Rejects when:** the application reads as generic, or the tone of the letter does not fit the kind of team the posting describes.

### Reserved for the deep level
- **headhunter:** an external recruiter who places candidates at this level; strict on positioning and on salary-level signals.
- **career-switch reader:** a recruiter who often hires people from other fields; judges how well the application translates past experience into this job.

## Experts

### coach — Career and hiring specialist
Evaluates how the application works as a whole for this job and this level: positioning, the story of the career, what to put first, what to cut, how to address gaps honestly. Asks: what is the one line a recruiter will remember? Which part of the CV is doing no work for this job? Which question will the interviewer ask first, and does the application prepare the answer?

### field — Specialist of the field
Evaluates the content against what this job really requires: whether the skills and achievements are at the level claimed, which terms the field uses, what is missing for this kind of role. Asks: which requirement of the posting is the hardest to meet, and does the application show it? Which claim would a specialist doubt first?

### market — Labor market specialist (the only one who gets web access, in round 2)
Evaluates the conventions and the context of this application: what employers in this field and country expect from a CV (length, photo or none, format, language), how this kind of job is usually described, what the employer says about itself publicly. When this persona has web access in a round, it checks the employer's public information, current conventions for CVs in that country and field, and how similar jobs are posted, marking [not verified] what it could not check; without web access, it says it is answering without checking.

### Reserved for the deep level
- **writing — Editor:** evaluates the language line by line: verbs, length, jargon, typos.

## Typical additional questions (they go into `config.md` when they apply)

- **Recruiters, round 1:** "If you had to call this candidate, what would you ask first?"
- **Recruiters, round 1:** "Which requirement of the posting did you look for and not find?"
- **coach, round 2:** if the career has a gap or a change of field, "How should the application address it, using only what is true?"
- **market, round 2:** the CV conventions in the country and field of the job; if there are several versions of the CV or of a headline to rank, rank them for this job.
- **Round 3:** for each central claim of the CV, include the follow-up question an interviewer would ask, written neutrally ("Consider the claim X. An interviewer asks: Y.").

# Preparing the evaluation of a work

For the **work** type: the object of the panel is a finished or draft piece that the panel reads **as it is**: a scientific paper, a manuscript or a chapter, a thesis or dissertation, an exam with its answer key, a student's answer, a design document judged as written. Unlike the other types, nobody writes a description of it: **the work itself is the input**. Write everything else in the language recorded in `config.md`; the work stays in its own language.

It combines with either family (`- Family:` in `config.md`):

- **audience:** personas react to the work as its public would (readers of a book, students facing an exam). Rounds as in `rounds.md`.
- **criteria:** a bench of jurors judges it against explicit criteria (peer review, thesis committee, editorial assessment, grading an answer). Rounds as in `method/rounds-criteria.md`.

## 1. Reading the work and what surrounds it

- Read the whole work before the question block, or, if it is long, its table of contents, opening and conclusion, enough to propose the scope (section 3).
- **Never edit the work's text**: not its arguments, not its typos, not its order. The panel judges what the author would submit. The only allowed transformations are format conversions (PDF or DOCX to Markdown), recorded in `prep/decisions.md`:
  - tables become Markdown tables with the same content;
  - a figure or image becomes `[Figure N: <its caption, verbatim>. The image itself is not available to the panel.]`, and the missing image goes to the gaps in `prep/decisions.md` (personas receive text only);
  - footnotes and references stay, in place or at the end, verbatim.
- **What surrounds the work is neutralized, as in `prepare.md`:** cover letters, notes to the reader, replies to earlier reviewers, the author's arguments in the chat ("the reviewers will love the method"). It goes to `prep/removed.md`, never to the panel.
- Markers ([decided], [proposed]…) do not apply inside the work. Do not annotate it.

## 2. Interview: extra items

In the same single question block of `prepare.md`:

| Item | Why it matters |
|---|---|
| **Family**: should the panel react as the work's public (audience) or judge it against criteria (criteria)? Propose the one the request suggests | decides the rounds |
| **Criteria** (criteria family): does the author have a rubric, answer key, journal guidelines or program regulation? If not, propose 3 to 7 criteria from the field profile | given criteria go verbatim to `input/03-criteria.md`; proposed ones are confirmed here |
| **Scope**, if the work is longer than about 5,000 words: which chapters, sections or questions | see section 3 |
| **Venue or occasion** (journal, publisher, committee, course and level) | shapes the personas and the criteria; goes in as **[fact]** in the header |
| For exam answers: **how many answers**, one panel each, up to five | see section 6 |
| For an exam judged by its students (audience): may the experts see the answer key? (default yes; students never) | see section 5 |

## 3. Long works and scope

When the work in scope is longer than about **5,000 words**, ask for the scope in the question block (chapters, sections, questions). The limit is about what **one persona receives in one call**, not the size of the work: choose the scope so that the excerpt, plus the summary of the rest for the experts, stays under about 5,000 words.

- **Users and jurors** receive the scoped excerpt, verbatim.
- **Experts and the destroyer** receive the scoped excerpt plus a **structured summary of the rest**, written by you, in `input/04-summary-of-the-rest.md`: one paragraph per section left out, each claim marked **[claim]** (the work asserts it), **[data]** (the work presents data or results for it), **[citation]** (the work attributes it to a source) or **[not verified]** (you could not tell from the text). The summary reports what the work says, never whether it is right.
- Record the scope and what was left out in the header of the work (section 4) and in `config.md` (`- Scope:`).

The run saves the excerpt and the summary once in `prompts/shared/` and points to them with `include:` lines, so their size never pushes the moderator to shorten them.

## 4. Inputs

### `input/01-short-pitch.md`

The work's **own opening**, verbatim, when it has one: the abstract, the back cover text, the first page, the exam's instructions. If it has none, write a neutral summary of up to 300 words (what the work is and what it sets out to do, without judging it) and record in `prep/decisions.md` that the opening was written by you.

### `input/02-work.md`

A short header, then the work, verbatim:

```markdown
**About this text (written by the panel's preparation; not part of the work):** <what the work is, in one
sentence: type, field, venue or occasion>. <Scope: the whole work | chapters/sections X to Y; what was left
out>. <Format conversions, if any, and figures that are not available.> Everything after the line below is
the work as the author wrote it.

---

<the work, verbatim>
```

If the work comes in several files (chapters, an exam and its attachments), use `input/02-work-1.md`, `input/02-work-2.md`… in reading order, each with the same header line saying which part it is.

### `input/03-criteria.md` (criteria family)

The rubric, answer key, guidelines or regulation the author gave, verbatim. The criteria table itself goes in `config.md` (grid dimensions, all round 1): `id`, `name`, the question "Does the work meet <criterion>?", and, when the criteria came from this file, the passage of it each criterion comes from. With proposed criteria, this file is not created.

### `input/04-summary-of-the-rest.md`

Only for long works (section 3).

### `moderator/author-concerns.md`

As in `prepare.md`. For a work, concerns are often about a reviewer's likely objection or a weak section: they become round 3 objections, written neutrally.

## 5. Personas and configuration

- Start from the field profile in `references/domains/` when one fits (`paper.md`, `book.md`, `thesis.md`, `exam.md`); otherwise build one from `composition.md`.
- **Audience family:** users are the work's public (readers, students) with distinct profiles; the eighth seat is the public the author imagines. For an exam judged by its students, students receive the exam only, never the answer key; experts receive the exam and the key. Record the choice in `config.md`.
- **Criteria family:** the bench of jurors of `composition.md` (lean 6, 3 per model, distinct profiles), the experts of the field profile and the destroyer as the harshest reviewer.
- In `config.md`: `- Type: work`, `- Family: audience | criteria`, `- Work files:` (the `02-work*.md` files), `- Scope:` (whole work, or what is in and what was left out), and the grid dimensions (audience) or criteria (criteria).

## 6. Exam answers

- **One answer per panel**, with the answer as the work (`input/02-work.md`) and the answer key or rubric as the criteria (`input/03-criteria.md`). The exam's question goes in the header, verbatim, and is also the opening (`input/01-short-pitch.md`): it is what the answer has to deliver.
- For two to five answers, prepare them together but run one panel per answer, each with its own output folder `rounds/v<version>-<answer-id>/` and the same bench, criteria and models.
- **Anonymize**: remove the student's name, number and anything that identifies them, and record it in `prep/removed.md`. Answer ids are neutral (`a1`, `a2`…). Jurors never see other students' answers or grades.
- A whole class is out of scope for now: say so in the question block if the author asks, and suggest choosing the answers where a second opinion matters most.

## 7. Self-check (in addition to `prepare.md`)

- The text after the header of `02-work.md` is identical to the work (compare it; only the recorded format conversions may differ).
- Nothing from outside the work (cover letter, replies to reviewers, the author's defense) reached `input/`.
- The opening is verbatim, or recorded in `prep/decisions.md` as written by you.
- Criteria family: 3 to 7 criteria, each a question the work can be checked against; given criteria are verbatim in `03-criteria.md`.
- Long works: what each persona receives stays under about 5,000 words, and the summary of the rest marks every claim.
- Exam answers: no name or identifying detail left in the answer.

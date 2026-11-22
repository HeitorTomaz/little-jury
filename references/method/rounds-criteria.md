# Rounds — variant for the criteria family

Use this file when `config.md` says `- Family: criteria`. Here a **bench of jurors** judges a work against explicit **criteria**: peer review of a paper, a thesis committee, an editorial assessment of a manuscript, grading an exam answer against its answer key. It **replaces the questions and the round 3 material** of `rounds.md`. Everything else still follows `rounds.md`, `run.md` and `outputs.md`: isolation, fresh agents only, the prompt skeleton, the `include:` rule for shared text, stances and "does not apply", neutral questions, same-model duplicates, the destroyer and the contrarian left out of every count, the contrarian pack and its two calls, the debate (keeps / adjusts / changes, independent / verified / persuaded, two turns at most), split by model, consolidation rules and re-evaluation.

## Contents

- Vocabulary and inputs
- What each agent receives
- Round 1 — Jurors judge the work (isolated)
- Round 2 — Experts and the harshest reviewer (isolated)
- Round 3 — Claims under challenge
- Round 4 — Contrarian and debate
- Round 5 — Consolidation
- Exam answers

## Vocabulary and inputs

Wherever `rounds.md` says "the project", "the description" or "use", read "the work", "the text of the work" and "read" (or the field's word: "the answer", "the thesis"). Write the questions, like everything sent to personas, in the language of `config.md`.

| Term | Where it is | What it is |
|---|---|---|
| **The work** | type `work`: `input/02-work.md` (or several `input/02-work-*.md`, in order); other types: `input/02-full-description.md` | the object being judged. For type `work` it is the work itself, verbatim, after a short header written by preparation (see `references/work.md` in the skill; the header says it is not part of the work) |
| **The opening** | `input/01-short-pitch.md` | the work's own opening (abstract, back cover text, first page, the exam's instructions; for an exam answer, the question it answers), verbatim, or a neutral summary written by preparation |
| **Summary of the rest** | `input/04-summary-of-the-rest.md` (only for long works) | a structured summary of the parts outside the scope, with each claim marked **[claim]**, **[data]**, **[citation]** or **[not verified]**. Only experts receive it |
| **Criteria** | the grid table in `config.md` and, when the author gave a rubric, answer key, journal guidelines or program regulation, `input/03-criteria.md` (verbatim) | 3 to 7 criteria, each with `id`, `name` and a question "Does the work meet <criterion>?". They are the grid dimensions: all of them are judged in round 1 |
| **Bench** | the `users` seat in `personas.md` and `config.md` | the jurors: lean 6, 3 per model, each a distinct profile (for example strict, lenient, methodologist, specialist of the topic, reader from outside the field, practitioner) |

Stances keep their enum values (`yes`, `only if`, `no`, `does not apply`); in this family they mean:

- **yes:** the work meets the criterion as written;
- **only if:** it meets it only with a revision, and **the condition is the revision**, in one sentence ("only if the sample size is justified");
- **no:** it does not meet it;
- **does not apply:** the criterion does not fit this work (an ethics criterion for a purely theoretical paper) or lies outside what this juror's profile can judge; always with the reason. It stays out of the tally.

**Every stance quotes the passage of the work it rests on**, with its section or page, or says that the work has no passage for it. A stance without a quote or an explicit "no passage" is incomplete: repeat the call once (`run.md`, section 6). This is what lets the debate and the consolidation check a verdict against the text instead of against the juror's authority.

## What each agent receives

| Round | Who | Receives | Does not receive |
|---|---|---|---|
| 1 | jurors | general rules, their own persona, the opening, the work (the scoped excerpt), the criteria (with `03-criteria.md` when it exists) | the summary of the rest, the list, any other answer |
| 2 | experts | general rules, persona, the opening, the work, the summary of the rest (if any), the criteria, specific questions | jurors' round 1 |
| 2 | destroyer (harshest reviewer) | general rules, persona, the opening, the work, the summary of the rest (if any), the criteria | everything else |
| 3 | experts and 2 jurors | general rules, persona, the work, the criteria, the items under challenge (in a re-evaluation, also the checks) | other people's answers, the author's concerns as such, anything from an earlier run |
| 4 | contrarian | general rules, persona, the work, the criteria, the contrarian pack; then up to six answers in full, on request | the author's concerns |
| 4 | participants of each point | general rules, persona, the work, the criteria, the summary of the point, the excerpt of their own previous answer | the author's concerns |

The work, the summary of the rest and the criteria go to many calls: save them once in `prompts/shared/` (or point to `inputs-used/`) and use `include:` lines (`run.md`, section 5). Never shorten them.

## Round 1 — Jurors judge the work (isolated)

Prompt material, in this order: the opening (headed "Opening of the work"), the work, the criteria. Questions:

1. In one sentence, what does the work claim, or what does it deliver?
2. For each criterion, in the order of `config.md`, under its own heading: the reason; the passage of the work it rests on, quoted with its section or page, or "the work has no passage for this"; then the stance: yes, only if <the revision>, no, or does not apply (with the reason).
3. What is the strongest part of the work, and why does it hold?
4. Which **one revision** would change your verdict the most, on which criterion, and what would it cost the work? If no revision would change it, say so.
5. Is there anything you could not judge (a table or figure you did not receive, data the work does not show, a field outside your profile)? If not, say so.
6. Additional questions for jurors in `config.md`.
7. *(if the list is active, for example candidate titles)* As question 9 of the users in `rounds.md`, with the list in the order drawn for this juror (the draw of `rounds.md` runs before round 1 here, since jurors have no round 2).

Answer format: add to the skeleton's format "Judge only from the text you received. Do not assume what the rest of the work says." The neutral-question rule applies: question 4 and 5 accept "none".

Output: `r1.md`, one section per juror.

### Opening check (moderator)

The comprehension check of `rounds.md`, adapted: compare each answer to question 1 with what the opening promises. List as **pitch problems** (`pitchIssues`) the sentences of the opening that half of the bench or more read differently from what the work delivers, or promises the work does not keep, with the sentence, what the work delivers, how it was read and by whom. They are problems of the opening, not of the rest of the work. Record the check in "Moderator notes" in `progress.md`, with whether the stances on any criterion came out uniform (for "only if", whether the revisions asked are the same) and whether the jurors' profiles sound distinct. Unless `config.md` asks for checkpoints, go on to round 2.

## Round 2 — Experts and the harshest reviewer (isolated)

### Experts (all)

The experts come from the field profile (for a paper: methodologist, statistician, specialist of the topic; the one with web access checks citations and facts). Questions, each accepting "none":

1. Does the method (or approach, or line of reasoning) fit the question the work asks? Quote the passages that show it fits, or where it fails.
2. For each central claim, does the evidence the work presents support it? Quote the claim and the evidence for every claim that goes beyond its evidence. If none does, say so and say what keeps them supported.
3. Do any passages contradict each other, or contradict the work's own data, tables or results (for an exam answer, the given answer key)? Quote both sides. If none do, say what keeps the work consistent.
4. Are the sources and external facts the work relies on accurate and fairly used? *(the expert with web access checks them; the others answer from the text and mark **[not verified]** every external fact they rely on)*
5. What is the strongest part of the work, and why does it work?
6. For the most serious problem you found, what is the **smallest revision** that would solve it, and what is lost with it?
7. What information is missing to judge the work?
8. For each criterion your field lets you judge: the reason, the passage, then the stance (yes, only if <the revision>, no); "does not apply" for the others.
9. The expert's specific questions, in `config.md`.

For the expert with web access, add the format note of `rounds.md` (source, address, date accessed, **[not verified]** with the reason). The web is used only for what question 4 and the specific questions ask.

### Harshest reviewer (destroyer)

"Present the three strongest reasons to reject or fail this work. For each one: (a) the objection; (b) the chain of reasoning, grounded in quoted passages of the work; (c) what would answer this objection: a revision, an analysis, or a passage of the work that already answers it. Do not attack what is not in the work; if the objection depends on something the work does not show, say so."

As in `rounds.md`, the harshest reviewer attacks by role: its objections are findings to examine, never a voice in a count.

Output: `r2.md`, one section per agent.

## Round 3 — Claims under challenge (moderator, experts and 2 jurors)

### Write the items

Instead of rule scenarios, write 4 to 7 items in `rounds/v<version>/r3-scenarios-proposed.md` (the file keeps its name, so the tools and the report find it). Each item puts **one central claim of the work** (for an exam answer, one key step) against **the strongest objection or alternative explanation** raised in rounds 1 and 2, written neutrally:

> Consider the claim "<claim, quoted>" (<section>). Objection: <the objection or the alternative explanation>.

Sources: the central claims of the work; the objections and alternative explanations from the jurors, the experts and the harshest reviewer; `moderator/author-concerns.md`, rewritten as objections without saying they are the author's; the author's goals for the evaluation (`config.md`); in a re-evaluation, the checks of `rounds.md` ("Re-evaluation").

Rules, as in `rounds.md`:

- **An item states the claim and the objection, never the verdict**, and never says who raised the objection or how many did. Reread each item before round 3 and rewrite any that suggests its answer ("the obviously insufficient sample…"); record the rewrite.
- An objection that came from one persona keeps that persona as its single origin (`(r2.md § <id>)` in `r3-scenarios-proposed.md`, which no persona sees): participants who agree with it confirm one origin.

### Choose the participants

All experts, plus **two jurors, one from each model**, chosen so that for each central claim there is **at least one defender and one critic** among the participants (from their round 1 stances and quotes). Record the claims, who defends and who criticizes each, and the reason for the choice in `progress.md`.

### Question

"For each item, does the work as written answer the objection? Quote the passage that answers it, or name the gap that leaves it open. Classify each outcome as a **hypothesis**, or as a **proven problem** only when two passages of the work contradict each other, or the work contradicts its own data or the given criteria or answer key — in that case, quote both. Finally, say which claims held up well, and why."

### Consolidate

Save the answers in `r3.md`, one section per participant, and write `r3-scenarios.md` with one table per item: participant, model, outcome, classification. Criterion for classification disagreements: an objection that rests only on knowledge from outside the work (another study, the field's consensus) and not on the work's own text, data or criteria stays a **hypothesis**, however strong; record whoever classified it differently as a dissent. Split by model: as in `rounds.md`.

## Round 4 — Contrarian and debate

As in `rounds.md`, with these differences.

**Contrarian pack.** Verbatim: the experts' answers to questions 2, 3 and 5; everything any juror named as the strongest part; every excerpt where three or more participants said the same thing; every mention of strengths; the harshest reviewer's three objections. The stances table has one row per juror and one column per criterion, with each "only if" revision and the passage quoted. In the five items to ask the contrarian, read "grounding in the description's text" as "grounding in the work's text".

**Agenda.** Draw the 3 to 5 points from:

- **criteria where the bench split**: at least one "yes" and one "no" on the same criterion, or "only if" answers asking for incompatible revisions;
- items of round 3 whose classification split;
- the contrarian's point (mandatory slot, as in `rounds.md`).

A criterion every juror judged the same way, each with a quoted passage, is **settled**: it goes straight to consolidation, listed under "Settled, not debated" in `r4-agenda.md`.

**Debate replies.** Position: keeps, adjusts or changes, and whoever adjusts or changes **quotes the passage of the work** (or of a round 3 item) behind the new position; the independent / verified / persuaded classification follows `rounds.md`. **Smallest revision** (instead of smallest change): the smallest revision to the work that would change a verdict on this point, and what the work loses with it; or "no revision needed", and why. These are the quick wins.

## Round 5 — Consolidation

Produce the files of `outputs.md`, read for a work:

- `concept-review.md`: what the work claims according to the bench, the 3 to 5 main findings and, **per criterion**, the bench's tally (meets, only if revised, does not meet; "does not apply" left out) with the divergences and the passages each side quoted.
- **No overall verdict by majority.** Do not turn the tallies into "accept", "reject" or a grade. Say what the bench agrees on (with independent positions only), where it splits, and which revision would move it. In `summary`, the same.
- `strengths-and-risks.md`: as in `outputs.md`; a strength or a problem without a quoted passage is an observation at most.
- `design-alternatives.md`: the quick wins are **the smallest revisions that change a verdict**, grouped by debate point; then the larger revisions, each with what it solves, what it costs the work and who supported or opposed it.
- `mvp-hypotheses.md`: what only real reviewers, readers, new data or a replication could settle, with the smallest way to find out.
- `diversity.md`: as in `method/diversity.md`, including the criteria-family items there.

Report data: the jurors are `users` (with `meta.usersLabel` such as "Jurors", "Reviewers" or "Committee"), the criteria are `dimensions`, the round 3 items are `scenarios` (`situation` = the claim and the objection, `outcome` = whether the work answers it), and `meta.family` is `"criteria"`. Each juror's four sentences come from round 1, and the report labels them for the criteria family: `understood` = answer 1 (how they read the work), `attracted` = answer 3 (its strongest part), `putOff` = the main weakness, taken from the reason of the juror's weightiest "no" (or "only if") stance, and `dropOut` = answer 4 (the revision that would change their verdict most). Risk categories keep their enum values: use `design` for problems of method or argument, `scope` for what the work leaves out, `audience` for fit with its readers or venue, `production` for the cost of revising, `market` for publication or adoption.

## Exam answers

When the work is a student's answer and the criteria are the answer key or rubric:

- **One answer per panel.** For two to five answers, run one panel per answer, each in `rounds/v<version>-<answer-id>/`, with the same bench, criteria and models, so the answers are judged under the same conditions.
- **Anonymize.** Jurors never see the student's name, other students' answers or how other answers were graded. The answer id is neutral (`a1`, `a2`…).
- The answer key is part of the criteria (`input/03-criteria.md`), and a contradiction between the answer and the key is a proven problem only when the key decides the point unambiguously; when the key itself is ambiguous or would penalize a correct answer, record it as a finding about the key, not about the student.
- **A whole class is out of scope** in this version: say so if asked, and suggest choosing the answers where a second opinion matters most.

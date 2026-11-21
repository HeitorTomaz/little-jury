# Rounds

## Contents

- What each agent receives
- Prompt skeleton
- Round 1 — First impression
- Round 2 — In-depth analysis
- Round 3 — Extreme scenarios
- Round 4 — Contrarian and debate
- Round 5 — Consolidation

In the questions below, "the project" and "use" must be replaced with the domain's vocabulary (for games: "the game", "play"). Dimension names come from `config.md`. Write the questions, like everything sent to personas, in the language set in `config.md` (`- Language:`).

**Evaluation type** (in `config.md`):

- **concept** and **system**: use the questions in this file. For the system type, "would try" means "would keep using or would start using", and experts treat **[divergent]** items as written rules in conflict.
- **change**: use the questions in `method/rounds-change.md`, which replace those in this file; everything else still applies.

## What each agent receives

| Round | Who | Receives | Does not receive |
|---|---|---|---|
| 1 | users | general rules, their own persona, `01-short-pitch.md` | full description, list, any other answer |
| 2 | users | general rules, persona, `02-full-description.md`, **their own round 1 answer**, list in drawn order (if active) | other people's answers |
| 2 | experts | general rules, persona, `02-full-description.md`, drawn list (only the relevant expert), specific questions | users' round 1 |
| 2 | destroyer | general rules, persona, `02-full-description.md` | everything else |
| 3 | experts and 2 users | general rules, persona, `02-full-description.md`, the scenarios | other people's answers, the author's concerns as such |
| 4 | contrarian | general rules, persona, `02-full-description.md`, the contrarian pack | the author's concerns |
| 4 | participants of each point | general rules, persona, `02-full-description.md`, the summary of the point, the excerpt of their own previous answer | the author's concerns |

`moderator/author-concerns.md` and `config.md` never go to anyone. The concerns inspire the scenarios, but the scenarios are written as situations, without saying they came from the author.

## Prompt skeleton

Write the prompt in the language set in `config.md`. The skeleton below is in English for reference.

```markdown
You are a persona on a panel evaluating <a project still being conceived | a system that already exists |
a planned change to a system that already exists>, according to the type in config.md. You have no tools and
must not ask for files: answer only from the text below. Your answer will be saved exactly as you write it.

## Rules for all personas
<copied from personas.md>

## Your persona
<the persona's block in personas.md, with its id>

## Material for this round
<full text of the input file; in round 2, also your round 1 answer and the drawn list>

## Questions
<the round's questions, numbered>

## Answer format
Answer in <language from config.md>, in Markdown, with one heading per question, in order. Speak in the first
person, from your profile. For scores, write the justification first and then the number from 1 to 5.
There is no minimum length: if a question does not apply to you, say why in one line.
```

The last sentence of the format exists because, in the pilot, all answers came out with the same structure and length; short answers where the persona has nothing to say are a useful signal, not a failure.

---

## Round 1 — First impression (users only, isolated)

Input: `01-short-pitch.md`. Questions:

1. In one sentence, what is this project?
2. What caught your attention?
3. What seemed uninteresting or confusing?
4. What questions would you have before trying it?
5. Would you try it? Why?
6. On what device or in what situation do you picture yourself using this? Why? *(omit if it makes no sense for the domain)*
7. Where do you usually discover products like this? *(omit if it makes no sense)*
8. Scores from 1 to 5 for **<clarity>** and **<curiosity>**, each with the justification before the number.

Output: `r1-<id>.md`. Then record in "Moderator notes" in `progress.md` whether the scores came out uniform (all equal on one dimension), whether the objections repeat almost word for word and whether the voices sound distinct. There is no stop: go on to round 2. Near-identical voices go into `diversity.md` as a limit.

## Round 2 — In-depth analysis (isolated)

Input: `02-full-description.md`.

### List draw (if active)

Before building the prompts, draw the order of the list's rows **for each agent that will rank it**, with a recorded seed:

```bash
python method/scripts/draw_list.py input/03-list.md --agents <id1,id2,...> --seed <integer> --output rounds/v<version>/list-draw.json
```

The script returns, for each agent, the reordered table. Use exactly that table in the prompt and record the seed in `progress.md`. The draw measures the order effect: in the pilot, 5 of 9 agents put first the item they received on the first row, when about 2 were expected by chance.

### Users

1. How do you picture the first 15 minutes of use?
2. At what moment would you get confused, bored or frustrated?
3. What part would you ignore or wish did not exist?
4. What would make you come back? And what would make you give up?
5. Which of your round 1 questions did the description answer, and which remain open? *(separates a presentation gap from a design problem)*
6. Additional questions for users in `config.md` (for example, reaction to the revenue model).
7. Scores from 1 to 5 for **<value>**, **<ease>** and **<would_try>**, each with the justification before the number. Then review your round 1 scores: for each one that changes, say **what in the description** caused the change; if nothing specific caused it, keep the score.
8. *(if the list is active)* For each item on the list, say what it suggests and whether it is easy to say, write and remember. Then rank all of them, from the best fit for the project to the worst, and say whether you would reject any.

Question 7 asks for the cause of the change because, in the pilot, all 8 users gave clarity 3 in round 1 and all went up to 4 in round 2; part of it was real, part looked like anchoring.

### Experts (all)

1. Which rules contradict each other or conflict? Quote both rules in each case.
2. Is there a strategy, shortcut or use that would always or almost always win? Describe it step by step.
3. Which rule or part costs the most to build relative to what it adds?
4. What would you cut from the first version?
5. What information is missing to evaluate it?
6. What is the smallest test that could show whether the core activity works, within the means the author has declared?
7. *(if `config.md` asks for it)* Through which channel do you recommend the first launch, and why?
8. The expert's specific questions, from `config.md`.
9. *(only the expert who ranks the list)* Rank the list by your own criterion and, if you have web access, check for conflicts in the indicated sources, saying what you could not check.

For the expert with web access, add to the format: "For each external fact, cite the source (address and date accessed). Mark **[not verified]** everything you could not access or confirm, and say why (interactive form, CAPTCHA, connection error). Do not use the web for anything beyond what these questions ask."

### Destroyer

"Present the three strongest arguments for this project to fail. For each one: (a) the claim; (b) the chain of reasoning, grounded in what is written in the description; (c) what would bring this argument down. Do not attack what is not written; if the argument depends on a gap, say so."

Output: `r2-<id>.md` per agent. After saving, run the list analysis if active (see `outputs.md`).

## Round 3 — Extreme scenarios (moderator, experts and 2 users)

### Write the scenarios

Write 5 to 8 hypothetical situations in `rounds/v<version>/r3-scenarios-proposed.md`, drawing on:

- `moderator/author-concerns.md`, rewritten as concrete situations ("The user does X in the first minute and then Y"), without saying they are the author's concerns;
- contradictions, dominant strategies and gaps that came up in rounds 1 and 2;
- the author's goals for the evaluation (`config.md`), so the scenarios test what the author needs to decide;
- **rule variants** proposed by the author or raised by the panel, presented as **anonymous alternatives** ("Consider two versions of rule Z: A… and B…"), without attributing a preference to anyone. In the pilot, this tested two rule changes and returned concrete conditions for adopting them.

### Choose the participants

- All experts.
- The **2 users with the most opposed positions on the same central rule**. Record the rule and the reason for the choice in `progress.md`.
- Keep **at least two models** among the participants (in the pilot, all six were on the same model, and the round lost variety). If the two most opposed users are on the same model as most experts, choose another equally opposed pair or record the limitation.

### Question

"For each scenario, describe what would happen **according to the written rules**. When the description does not decide the outcome, say which gap prevents the answer. Classify each outcome as a **hypothesis**, or as a **proven problem** only when it follows directly from two written rules that contradict each other — in that case, quote both. For the variants, say under what conditions each version works better."

### Consolidate

Save the answers in `r3-<id>.md` and write `r3-scenarios.md` with one table per scenario: participant, outcome, classification. Criterion for classification disagreements: a contradiction with an **experience intention**, with a goal marked **[undefined]** or with a rule that is only **[proposed]** stays a **hypothesis**; record whoever classified it differently as a dissent.

## Round 4 — Contrarian and debate

### 4a. Contrarian

The material from rounds 1 to 3 does not fit whole in one prompt (in the pilot, about 357 KB). Build the **contrarian pack** in `rounds/v<version>/r4-contrarian-pack.md`:

- **As verbatim text**, marked `[verbatim: r2-<id>.md]`:
  - the experts' answers to the contradiction and dominant-strategy questions;
  - the most repeated criticism among users, in the excerpt of each user who made it;
  - **every** mention of strengths, from any participant;
  - the destroyer's three arguments.
- **As your summary**, marked `[moderator summary]`: the rest, per participant.
- A table of every user's scores in both rounds and the count of who mentioned each recurring criticism.
- External evaluations, if any, identified as external.

Tell the contrarian in the prompt that only the excerpts marked as verbatim are original text. Ask for:

1. Criticisms repeated by several personas without grounding in the description's text (cite the rule that would refute them or the absence of a rule that would support them).
2. Premises nobody checked.
3. Strengths ignored or mentioned once and forgotten.
4. Where the panel agreed too quickly, separating agreement on **contradictions verifiable in the text** (expected) from agreement on **recommendations** (where the risk lies).
5. The point you consider most important to take to the debate, and why.

Save it in `r4-contrarian.md`.

### 4b. Agenda

Propose 3 to 5 points, the most controversial ones. Mandatory:

- **the list**, when active: count of the rankings (from `list-analysis.json`), rejections, order effect and conflicts found by the expert with web access. The author did not state a preference and you must not suggest one;
- **a slot for the contrarian's point** (question 5). The contrarian speaks only on that point, with one reply, like the others; it does not take part in the other points, so that the debate does not lean towards the adversary with more speaking turns.

Choose the points with the author's goals for the evaluation in mind too (`config.md`). For each point, say who takes part and why, and save the agenda in `r4-agenda.md` and in `progress.md`. There is no stop: go on to the debate.

### 4c. Debate

For each point:

1. Write a summary of the positions, saying who defended each one (by id) and with short verbatim excerpts when possible.
2. Ask **each participant involved, in a separate agent**, for a short reply (up to 200 words): whether they keep, change or adjust their position, and why. They receive the summary of the point and the excerpt of their own previous answer, never other people's whole answers.
3. Ask each reply to start with one of these words: **keeps**, **adjusts** (same position, with a caveat or new condition) or **changes** (different position). Run a second turn only if someone says **changes**, with a new summary. **Two turns at most.**
4. Record each participant's final position and who disagreed. Agreement is not required.

Save the replies in `r4-<point>-<id>-v<turn>.md` and the synthesis in `r4-debate.md`.

## Round 5 — Consolidation (moderator, no agents)

Produce the files in `outputs.md`, in this order: `concept-review.md`, `strengths-and-risks.md`, `design-alternatives.md`, `mvp-hypotheses.md`, `list.md` (if active), `diversity.md`, `report-data.json` and `report.html` (with the `fonts/` folder next to it, which the script copies). Mark round 5 as completed in `progress.md` and finish with the full path of **`report.html`**, a short summary of what the panel concluded and what you found ambiguous in the method. The session that launched the run opens the report for the author: it is the skill's output for the person, and the `.md` files in the folder are the memory for Claude.

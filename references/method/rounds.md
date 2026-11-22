# Rounds

## Contents

- What each agent receives
- Prompt skeleton
- Round 1 — First impression
- Round 2 — In-depth analysis
- Round 3 — Extreme scenarios
- Round 4 — Contrarian and debate
- Round 5 — Consolidation
- Re-evaluation

In the questions below, "the project" and "use" must be replaced with the domain's vocabulary (for games: "the game", "play"; for a work: "the work", "read"). Dimension names come from `config.md`. Write the questions, like everything sent to personas, in the language set in `config.md` (`- Language:`).

**Evaluation type** (in `config.md`):

- **concept** and **system**: use the questions in this file. For the system type, "would try" means "would keep using or would start using", and experts treat **[divergent]** items as written rules in conflict. A **[divergent]** item is already a proven problem in itself (documentation and code disagree). When another rule contradicts **one side** of it, classify by that side: contradicting the code side (what the system really does) is a **proven problem**; contradicting only the documentation side is a **hypothesis**, because the author has not said which side holds. It is the same criterion the change type uses for **[implemented]** against **[documented]**.
- **change**: use the questions in `method/rounds-change.md`, which replace those in this file; everything else still applies.
- **work**: the object is a piece read as it is (a paper, a manuscript, a thesis, an exam, an answer). Wherever this file says `02-full-description.md`, use the work: `input/02-work.md` (or `input/02-work-*.md`, in order), verbatim after a short header written by preparation; experts and the destroyer also receive `input/04-summary-of-the-rest.md` when the work was scoped. Round 1 still receives the opening (`01-short-pitch.md`, usually the work's own abstract or first page). "The description" in the questions becomes "the work"; a quoted passage is a passage of the work, with its section or page. In the audience family, "rules" in the expert questions means what the work sets for itself: its claims and conventions, a story's internal logic, an exam's instructions and scoring.

**Family** (`- Family:` in `config.md`, default `audience`):

- **audience**: the personas react to the work as its public would; use this file (or `rounds-change.md`).
- **criteria**: a bench of jurors judges the work against explicit criteria; use `method/rounds-criteria.md`, which replaces the questions and the round 3 material of this file; everything else here still applies.

**Effort level** (`- Effort:` in `config.md`, default `standard`; table in `run.md`, section 4):

- **quick:** rounds 1 and 2, the contrarian in one call, then consolidation. Round 3 and the debate are skipped. The quick wins come from the experts' "smallest change" question in round 2 (question 6 of the experts here; the equivalent question in `rounds-change.md` and `rounds-criteria.md`): each one keeps its proposer, and nobody supported or opposed it, because there was no debate.
- **standard:** everything in this file, as written.
- **deep:** a second destroyer (`destroyer-2`) on the other model in round 2; 8 to 10 round 3 items with four users (two per model) besides the experts; 5 to 7 debate points, each **always** with a second turn.

**Round 3 tests.** If `config.md` has a `- Round 3 tests:` line (from the field profile), round 3 puts that under challenge: rules in scenarios (the default, below), claims against objections (as in `rounds-criteria.md`), or questions against possible answers (an exam seen by its students: a correct answer the key would penalize, a reading of the question the author did not intend). The rules for writing round 3 items stay the same: neutral, the situation or the claim and never the outcome, one origin per persona's proposal.

## What each agent receives

| Round | Who | Receives | Does not receive |
|---|---|---|---|
| 1 | users | general rules, their own persona, `01-short-pitch.md` | full description, list, any other answer |
| 2 | users | general rules, persona, `02-full-description.md`, **their own round 1 answer**, list in drawn order (if active) | other people's answers |
| 2 | experts | general rules, persona, `02-full-description.md`, drawn list (only the relevant expert), specific questions | users' round 1 |
| 2 | destroyer | general rules, persona, `02-full-description.md` | everything else |
| 3 | experts and 2 users | general rules, persona, `02-full-description.md`, the scenarios (in a re-evaluation, also the checks built from the earlier problems) | other people's answers, the author's concerns as such, anything from an earlier run |
| 4 | contrarian | general rules, persona, `02-full-description.md`, the contrarian pack; then up to six answers in full, on request | the author's concerns |
| 4 | participants of each point | general rules, persona, `02-full-description.md`, the summary of the point, the excerpt of their own previous answer | the author's concerns |

**Fresh agents only.** Agents from earlier rounds (or earlier turns) are never resumed or continued: do not send a message to an earlier agent. Every call is a new agent that receives, when it needs it, the verbatim excerpt of that persona's own earlier answer. This includes the debate's second turn and the contrarian's second call. In a real run, some personas continued their own agent and others got a fresh one, so they read the same reply with different context.

`moderator/author-concerns.md` and `config.md` never go to anyone. The concerns inspire the scenarios, but the scenarios are written as situations, without saying they came from the author. In a re-evaluation, `moderator/changes.md` and `moderator/previous-problems.md` never go to anyone either, and no persona receives anything from the earlier run: every instance is new.

## Prompt skeleton

Write the prompt in the language set in `config.md`. The skeleton below is in English for reference.

```markdown
You are a persona on a panel evaluating <a project still being conceived | a system that already exists |
a planned change to a system that already exists | a work (paper, manuscript, thesis, exam, answer) as it
is written>, according to the type in config.md. <criteria family: "You are a juror on a bench judging it
against the criteria below."> You have no tools and
must not ask for files: answer only from the text below. Your answer will be saved exactly as you write it.

## Rules for all personas
<copied from personas.md>

## Your persona
<the persona's block in personas.md, with its id>
<if the persona's text mentions a tool it does not have in this round: "In this round you have no web access.
Do not claim to have checked anything; mark [not verified] every external fact you rely on.">

## Material for this round
<full text of the input file; in round 2, also your round 1 answer and the drawn list>

## Questions
<the round's questions, numbered>

## Answer format
Answer in <language from config.md>, in Markdown, with one heading per question, in order. Speak in the first
person, from your profile. For stance questions, write the reason first and then your stance: yes,
only if <the condition>, or no. "Only if" always names the condition.
There is no minimum length: if a question does not apply to you, say why in one line.
```

The last sentence of the format exists because, in the pilot, all answers came out with the same structure and length; short answers where the persona has nothing to say are a useful signal, not a failure.

**Stances, not scores.** Each grid dimension in `config.md` is a question answered with a stance: **yes**, **only if** (with the condition, in one sentence) or **no**, always with the reason before the stance. In a real run with written anchors, every 1-to-5 score fell between 2 and 4, none at 1 or 5, several users answered 3/3/3, and the scores did not measure change between versions. A stance with its condition says what a 3 hides: the condition is the useful data.

**Does not apply.** When a question does not fit a persona's relation to the project (someone who would only be affected or contacted, never use it: a relative who only gets reminders, a supplier who only receives orders), the persona answers **does not apply**, with the reason, instead of inventing a yes or a no. It stays out of the tally, and the other questions are still answered. Write it into the prompt for personas whose relation (`personas.md`) is not "uses": "If a question does not fit your relation to the project, answer 'does not apply' and say why." In a real run, a forced no from a persona who would never use the system pulled the panel's answers down for no real reason.

**Neutral questions.** Every problem-seeking question accepts "none" as a valid answer and says so ("If you find none, say so and say what keeps it coherent"). A question that presupposes the problem ("Which rules contradict each other?") pulls answers toward findings. This complements the rule against inventing criticism to look rigorous.

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
8. **<curiosity question>** (for example, "Would you want to know more?"): the reason, then yes, only if <condition>, or no.

**Clarity is not a stance.** In two runs, all eight users gave the same clarity score with different justifications: with a short pitch, the uniformity comes from the text, not from the personas. Clarity is measured instead by the comprehension check below.

Output: `r1.md`, one section per user.

### Comprehension check (moderator)

Compare each answer to question 1 and each confusion in question 3 with what the pitch meant to say. List the **pitch problems**: sentences or ideas that half of the users or more understood differently from what was intended, with the sentence, what it meant to say, how it was understood and by whom. They are problems of the **text**, not of the project, and the report shows them separately (`pitchIssues`). In a real run, three sentences of the pitch were misunderstood by half of the panel or more. Record the check in "Moderator notes" in `progress.md`.

Then record there too whether the curiosity stances came out uniform (for "only if", whether the conditions are the same), whether the objections repeat almost word for word and whether the voices sound distinct. Unless `config.md` asks for checkpoints (`run.md`, section 8), there is no stop: go on to round 2. Near-identical voices go into `diversity.md` as a limit.

## Round 2 — In-depth analysis (isolated)

Input: `02-full-description.md`.

### List draw (if active)

Before building the prompts, draw the order of the list's rows **for each agent that will rank it**, with a recorded seed:

```bash
python method/scripts/draw_list.py input/03-list.md --agents <id1,id2,...> --seed <integer> --output rounds/v<version>/list-draw.json
```

The script returns, for each agent, the reordered table. Use exactly that table in the prompt and record the seed in `progress.md`. The draw measures the order effect: in the pilot, 5 of 9 agents put first the item they received on the first row, when about 2 were expected by chance.

### Users

1. How do you picture the first 15 minutes of use? *(if the project has different roles, modes or paths, add "as <role / mode / path>", assigning different ones across users; see below)*
2. At what moment would you get confused, bored or frustrated?
3. What part would you ignore or wish did not exist?
4. What would you keep no matter what changes, and why?
5. What would make you come back? And what would make you give up?
6. Which of your round 1 questions did the description answer, and which remain open? *(separates a presentation gap from a design problem)*
7. Additional questions for users in `config.md` (for example, reaction to the revenue model).
8. The questions for **<value>**, **<ease>** and **<would_try>** (from `config.md`), each with the reason, then yes, only if <condition>, or no. Then review your round 1 stance (**<curiosity>**): if it changes, **quote the passage of the description** that caused the change; if nothing specific caused it, keep the stance.
9. *(if the list is active)* For each item on the list, say what it suggests and whether it is easy to say, write and remember. Then rank all of them, from the best fit for the project to the worst, and say whether you would reject any.

Question 8 asks for the passage behind the change because, in the pilot, all 8 users gave the same round 1 score and all moved it by one point in round 2; part of it was real, part looked like anchoring. A revision with no quoted passage is recorded as unanchored in `diversity.md`.

**Spread the paths.** If the project has different roles, modes or paths (a player role, an admin and a member, a guided and a free mode), assign them across users in question 1, so they do not all imagine the same one; give each user a path that fits their persona and record the assignment in `progress.md`. In a real run, every user imagined the same role, and the other roles went untested.

### Experts (all)

1. Are there rules that contradict each other or conflict? Quote both rules in each case. If you find none, say so and say what keeps them coherent.
2. Is there a strategy, shortcut or use that would always or almost always win? If so, describe it step by step; if not, say what prevents one.
3. What is the strongest part of the proposal, and why does it work?
4. Is there a rule or part that costs much more to build than what it adds? If none does, say so.
5. What would you cut from the first version?
6. For the most serious problem you found, what is the **smallest change** to a rule or decision that would solve it, and what is lost with it?
7. What information is missing to evaluate it?
8. What is the smallest test that could show whether the core activity works, within the means the author has declared?
9. *(if `config.md` asks for it)* Through which channel do you recommend the first launch, and why?
10. The expert's specific questions, from `config.md`.
11. *(only the expert who ranks the list)* Rank the list by your own criterion and, if you have web access, check for conflicts in the indicated sources, saying what you could not check.

For the expert with web access, add to the format: "For each external fact, cite the source (address and date accessed). Mark **[not verified]** everything you could not access or confirm, and say why (interactive form, CAPTCHA, connection error). Do not use the web for anything beyond what these questions ask."

### Destroyer

"Present the three strongest arguments for this project to fail. For each one: (a) the claim; (b) the chain of reasoning, grounded in what is written in the description; (c) what would bring this argument down. Do not attack what is not written; if the argument depends on a gap, say so."

At the deep level, `destroyer-2` gets the same question on the other model, with its own persona (a different angle of attack). Save both in `r2.md`; their arguments are examined separately, and agreement between them is not a convergence of the panel.

The destroyer's role is to attack, so it is **not an independent voice**: leave it out of every convergence, consensus or "N of M agree" count, in every round. Its arguments still count as findings to examine. The same goes for the contrarian.

Output: `r2.md`, one section per agent. After saving, run the list analysis if active (see `outputs.md`).

**Same-model duplicates.** When two personas on the same model deliver the same finding (the same strategy, the same calculation, nearly the same wording), count it as **one** piece of evidence, cite both, and record it in `diversity.md`. In a real run, two same-model experts produced the same finding with the same arithmetic and almost the same sentence.

## Round 3 — Extreme scenarios (moderator, experts and 2 users)

### Write the scenarios

Write 5 to 8 hypothetical situations (8 to 10 at the deep level) in `rounds/v<version>/r3-scenarios-proposed.md`, drawing on:

- `moderator/author-concerns.md`, rewritten as concrete situations ("The user does X in the first minute and then Y"), without saying they are the author's concerns;
- contradictions, dominant strategies and gaps that came up in rounds 1 and 2;
- the author's goals for the evaluation (`config.md`), so the scenarios test what the author needs to decide;
- **rule variants** proposed by the author or raised by the panel, presented as **anonymous alternatives** ("Consider two versions of rule Z: A… and B…"), without attributing a preference to anyone. In the pilot, this tested two rule changes and returned concrete conditions for adopting them. A variant built from **one persona's proposal** keeps that persona as its single origin: record it in `r3-scenarios-proposed.md` ("variant from `(r2.md § <id>)`"), and count the round 3 participants who favor it as confirmations of one origin, never as independent proposals;
- in a re-evaluation, the earlier problems, as checks against the current text, and a check of each changed section (see "Re-evaluation").

**A scenario describes the situation, never the play or the outcome.** Give the state, the constraints and what the user faces; never describe the line of action the user takes or the result. Before round 3, reread each proposed scenario and rewrite any that contains its own answer; record the rewrite in `r3-scenarios-proposed.md`. In a real run, a scenario described the line of action step by step, and every participant reproduced it instead of reasoning from the rules.

### Choose the participants

- All experts.
- **Two users, one from each model** (four at the deep level, two per model), chosen so that, for each central rule discussed in the scenarios, there is **at least one defender and one critic** among the participants (counting experts too). Record the rules, who defends and who criticizes each, and the reason for the choice in `progress.md`.
- This keeps at least two models in the round (in the pilot, all six participants were on the same model, and the round lost variety). If no pair of users covers every central rule, choose the pair that covers the most and record the limitation.

### Question

"For each scenario, describe what would happen **according to the written rules**. When the description does not decide the outcome, say which gap prevents the answer. Classify each outcome as a **hypothesis**, or as a **proven problem** only when it follows directly from two written rules that contradict each other — in that case, quote both. For the variants, say under what conditions each version works better. Finally, say which of these rules held up well in the scenarios, and why."

### Consolidate

Save the answers in `r3.md`, one section per participant, and write `r3-scenarios.md` with one table per scenario: participant, model, outcome, classification. Criterion for classification disagreements: a contradiction with an **experience intention**, with a goal marked **[undefined]** or with a rule that is only **[proposed]** stays a **hypothesis**; record whoever classified it differently as a dissent.

**Split by model.** When a classification or a position splits exactly along model lines, record it as "split by model", do not resolve it by majority, and keep it as a hypothesis. In a real run, the classification of one scenario split exactly by model: the three participants on one model said "proven problem", the three on the other said "hypothesis".

## Round 4 — Contrarian and debate

### 4a. Contrarian

The material from rounds 1 to 3 does not fit whole in one prompt (in the pilot, about 357 KB). Build the **contrarian pack** in `rounds/v<version>/r4-contrarian-pack.md`:

- **As verbatim text**, marked `[verbatim: r2.md, <id>]`:
  - the experts' answers to the contradiction, dominant-strategy and strongest-part questions;
  - **everything users said they would keep**;
  - every excerpt where **three or more participants said the same thing**, with who said it (this includes the most repeated criticism);
  - **every** mention of strengths, from any participant;
  - the destroyer's three arguments.
- **As your summary**, marked `[moderator summary]`: the rest, per participant. Every attribution in the summary points to its source as `(r2.md § <id>)`, so the contrarian can check it.
- A table of every user's stances in both rounds (with the conditions of the "only if" answers) and the count of who mentioned each recurring criticism (the destroyer and the contrarian do not count).
- An **index of every answer**: one numbered line per answer (round, persona id, one-line summary), so the contrarian can ask for any of them.
- External evaluations, if any, identified as external.

The contrarian also receives the full description (`02-full-description.md`), to check the panel's criticisms against the text. Tell it in the prompt that only the excerpts marked as verbatim are original text, and that it may **request up to six answers in full**, by index number.

At the **quick** level there is no round 3, so the pack is built from rounds 1 and 2, the contrarian works in **one call** (no index and no requests for full answers), and item 5 below becomes "the point the author should look at first, and why". Save it in `r4-contrarian.md` and go straight to consolidation.

At the standard and deep levels, the contrarian works in **two calls**:

1. **First call:** the pack and the description. Ask for its findings so far on the five items below, and for the list of answers it wants in full (up to six index numbers), each with the reason.
2. **Second call:** a new agent (never the first one resumed) that receives the pack, the description, the first call's answer verbatim and the requested answers verbatim, and is asked for the final findings on the five items.

Never shorten the pack, the description or the requested answers in either call, whatever their size: save them once in `prompts/shared/` and point to them with `include:` lines (`run.md`, section 5). In a real run, the second call got a shortened pack, and the contrarian checked the panel against less than it should have.

Items to ask for:

1. Criticisms repeated by several personas without grounding in the description's text (cite the rule that would refute them or the absence of a rule that would support them).
2. Premises nobody checked.
3. Strengths ignored or mentioned once and forgotten.
4. Where the panel agreed too quickly, separating agreement on **contradictions verifiable in the text** (expected) from agreement on **recommendations** (where the risk lies). Include errors of attribution or exaggeration in the moderator's own summary.
5. The point you consider most important to take to the debate, and why.

Save both calls and the list of requested answers in `r4-contrarian.md`. It is worth the extra call: in a real run, the full answers the contrarian requested revealed two attribution errors in the moderator's own summary, two panel exaggerations and one premise nobody had checked against the text.

### 4b. Agenda

Propose 3 to 5 points (5 to 7 at the deep level), the most controversial ones. Items that are already **settled** (for example, a contradiction every expert pointed out) do not go to the debate: send them straight to consolidation and list them in `r4-agenda.md` under "Settled, not debated". This saves calls without losing anything. Mandatory:

- **the list**, when active: count of the rankings (from `list-analysis.json`), rejections, order effect and conflicts found by the expert with web access. The author did not state a preference and you must not suggest one;
- **a slot for the contrarian's point** (question 5). The contrarian speaks only on that point, with one reply, like the others; it does not take part in the other points, so that the debate does not lean towards the adversary with more speaking turns.

Choose the points with the author's goals for the evaluation in mind too (`config.md`). For each point, say who takes part and why, and save the agenda in `r4-agenda.md` and in `progress.md`. Unless `config.md` asks for checkpoints (`run.md`, section 8), there is no stop: go on to the debate. At checkpoint 2, the author may edit `r4-agenda.md`; when the run resumes, use the agenda as it is in the file.

### 4c. Debate

For each point:

1. Write a summary of the positions, saying who defended each one (by id) and with short verbatim excerpts when possible. Every attribution points to its source as `(r2.md § <id>)` or `(r3.md § <id>)`. In a real run, the moderator's summary had five attribution errors, found only by the contrarian; a source next to each attribution lets the consolidation check them too.
2. Ask **each participant involved, in a separate, new agent**, for a short reply (up to 250 words) with two parts. They receive the summary of the point and the excerpt of their own previous answer, never other people's whole answers.
   - **Position:** start with one of these words: **keeps**, **adjusts** (same position, with a caveat or new condition) or **changes** (different position), and say why. Whoever adjusts or changes **quotes the passage of the description (or of a scenario) that supports the new position**.
   - **Smallest change:** the smallest change to a rule or decision that would solve the problem in this point, and what is lost with it; or "no change needed", and why. Big redesigns are not what is asked: the aim is the change that costs least for the effect it has.
3. Collect the smallest changes of the point (the **quick wins** of the consolidation), merging the ones that say the same thing. Run a **second turn** if someone said **changes** or if the point has **two or more different proposals**: the new summary lists the proposals (without saying who made them), and each participant says, in one line each, whether they **support** or **oppose** each proposal, and why, besides keeping, adjusting or changing their position. **Two turns at most.** At the deep level, every point gets the second turn.
4. Record each participant's final position, who disagreed, and, for each quick win, who proposed it, who supported it and who opposed it. A proposal supported only by the one who made it still goes on record. Agreement is not required.
5. **Independent, verified or persuaded.** Classify every final position on the point in one of three kinds, and record the kind next to it in `r4-debate.md`:
   - **independent:** the participant held this position before reading anyone's argument (in rounds 1 to 3, with the source). Only independent positions count as separate agreements;
   - **verified:** the position changed (adjusts or changes) after reading an argument, and the reply quotes a passage of the description or of a scenario that supports it. It counts as **one confirmation of that argument's origin**, not as a new agreement: several verified changes after the same argument are still one origin, checked several times;
   - **persuaded:** the position changed with no quoted passage behind it. It does not count toward agreement at all.

   The test is the order and the anchor, not the tone of the reply: a position that already existed is independent; a new one is verified only with a quote. In a real run, four convergences all came from one participant's argument read in the same summary, and a rule that only separated "with or without a quote" still left the moderator unsure how to count them.
6. **Non-independent convergence.** If half or more of a point's participants change position in the same direction after reading the same argument, record it as non-independent convergence, in `r4-debate.md` and in `diversity.md`, naming the argument's origin; whatever the mix of verified and persuaded changes, it is one movement, not several independent agreements. The destroyer and the contrarian are never counted among the participants for this rule.
7. **Split by model.** If the final positions on a point split exactly along model lines, record it as "split by model" and do not resolve it by majority (see round 3).

Save the replies in `r4-debate-replies.md`, one `## <point> — <id> — turn <n>` section per reply, and the synthesis in `r4-debate.md`.

## Round 5 — Consolidation (moderator, no agents)

Produce the files in `outputs.md`, in this order: `concept-review.md`, `strengths-and-risks.md`, `design-alternatives.md`, `mvp-hypotheses.md`, `comparison.md` (re-evaluation only), `list.md` (if active), `diversity.md`, `report-data.json` and `report.html` (with the `fonts/` folder next to it, which the script copies). Items settled before the debate enter here, with the evidence from rounds 2 and 3.

Rules for the consolidation:

- Keep the **pitch problems** (comprehension check) apart from the project's problems: they say how the pitch was read, not whether the project works.
- When the audience is undefined (`## Audience` in `config.md`), do not tally or summarize together profiles that want opposite things: record what each group wants and what choosing each audience would cost.
- Every attribution points to its source (`(r2.md § <id>)`); check the ones in your earlier summaries against the round files, and correct any the contrarian flagged.
- Same-model duplicates count as one piece of evidence; the destroyer and the contrarian are not counted in any "N of M agree".
- For each strength, record who cited it **and who opposed it**, and why.
- **Never recommend running the panel again**: that is the author's decision.

Mark round 5 as completed in `progress.md` and finish with the full path of **`report.html`**, a short summary of what the panel concluded and what you found ambiguous in the method. Add one line telling the author that ideas or decisions that came up while the panel ran go in `prep/next-version-notes.md`, never in the panel's inputs. The session that launched the run opens the report for the author: it is the skill's output for the person, and the `.md` files in the folder are the memory for Claude.

## Re-evaluation

When `config.md` says `- Re-evaluation of: v<earlier version>`, this run evaluates a revised version of a project the panel already saw. It asks for things a first run does not:

- **Same persona profiles and models** as the earlier run, so that differences come from the project and not from the panel. The instances are always new: no persona receives anything from the earlier run.
- **Moderator-only files**, never passed to personas: `moderator/changes.md` (what changed between the versions: item, before, after, marker) and `moderator/previous-problems.md` (the earlier problems, numbered P1, P2…, with source file and classification).
- **Rounds 1 and 2 stay fully independent**: nothing about the earlier problems or the changes enters them, so the personas look at the project and not for the old problems.
- **Round 3** adds the earlier problems as **checks against the current text**, written neutrally ("Check against the current description whether …"), never saying that they were problems before. Each check keeps its P number in `r3-scenarios-proposed.md`, which no persona sees.
- **Round 3 also checks each section that changed** (from `moderator/changes.md`), neutrally: "Check whether the current description of <section> creates a problem of its own." Number these checks C1, C2… in `r3-scenarios-proposed.md`. In a real run, the problems only partly resolved had in common that the fix opened a new problem in the same place.
- **You read the earlier run only during consolidation**, not before: your scenarios, summaries and agenda must not be steered by it.
- **Comparison output:** `comparison.md` and the report's `comparison` key: each earlier problem as `resolved`, `partly` or `unresolved`, with the evidence from this run, plus the `new` problems the changes created. Look for `new` problems especially in the changed sections (the C checks).

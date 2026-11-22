# Guide for `diversity.md`

`diversity.md` is the evaluation of the panel itself and the quality measure of each run. It answers: did the arguments come out varied enough for the panel to be worth more than a single opinion? Where did the personas repeat each other, and why?

Write it in the language set in `config.md`, with numbers and verbatim examples. "The voices seemed distinct" does not work; "6 of 8 users used the phrase 'learning curve' in question 3 of round 2" does.

> **Version 2.** Based on the pilot and on a second real run, which brought the lessons about the debate, the summaries and the consolidation.

## 1. Models

A table of every agent, with the model used in each round and the agent type. Point out:

- any model change, and why;
- rounds with a single model (there should be none);
- whether the split of models among users was balanced by complexity tolerance.

## 2. Stances

- **Uniformity:** for each dimension, how many said yes, only if and no. All users giving the same stance on a dimension is a **signal to investigate**, not a result. For "only if", compare the conditions: the same condition from everyone is uniformity; different conditions are not. Before blaming the personas, check whether the input explains it: with a short pitch, the uniformity can come from the text. That is why clarity is no longer asked: in two runs, all eight users gave the same clarity score, with different justifications. Stances replaced scores for the same reason: in a real run, every score fell between 2 and 4 and several users answered 3/3/3, even with written anchors.
- **Changes between rounds:** who changed their round 1 stance (curiosity, or relevance for a change) in round 2, in which direction, and whether they quoted the passage of the description that caused the change. A uniform change with no passage quoted suggests **anchoring**; with a passage quoted, it may be real (the short pitch had gaps). In the pilot, all 8 users gave the same round 1 score and all moved it by one point.
- **Comprehension check:** how many pitch problems the check found, and whether they explain uniform stances or repeated confusions. Keep them apart from the project's problems. For the criteria family, the same for the opening check (what the opening promises against what the work delivers).
- **Undefined audience:** if the audience is undefined, confirm that no synthesis tallied together profiles that want opposite things.
- **Model × stance:** do stances differ systematically between model groups? If so, separate what is a difference of profile from what may be a difference of model.
- **Spread of paths:** if the project has different roles, modes or paths, say how they were assigned among users in round 2 and whether any path went unimagined. In a real run, every user imagined the same role.
- **Criteria family:** say, per criterion, how many jurors said meets, only if revised and does not meet, and whether the "only if" revisions are the same or different. Check that **every juror quoted a passage of the work for each stance** (or said the work has no passage for it); list the stances that did not, and whether the repeated call fixed them.
- **Strictness × model:** compare the jurors' profiles (strict, lenient…) with their models. A strict or lenient profile present on one model only is a confound: a split along those lines may come from the model as much as from the profile. Say so before reading a split as a difference of standard.

## 3. Arguments

- **Repeated criticisms:** for each criticism mentioned by 3 or more participants, how many made it, who, and whether the contrarian considered it grounded. In the pilot, one criticism appeared in 7 of 8 users.
- **Same-model duplicates:** findings delivered by two personas on the same model with the same strategy, the same calculation or nearly the same wording. List them; each counts as one piece of evidence. In a real run, two same-model experts produced the same finding with the same arithmetic.
- **Unique arguments:** the arguments raised by a single persona that survived the debate. They are the best evidence that the variety paid off.
- **The imagined-audience persona and the personas outside the audience:** did they say something no other persona said?

## 4. Experts

Separate two kinds of agreement:

- on **contradictions verifiable in the text**: expected; not a lack of diversity;
- on **recommendations** (cuts, platform, first test): this is where the risk lies. Count how many main recommendations coincided and between which models.

In the pilot, the 4 experts on the same model reached the same recommendations.

**Do not compare counts across models.** Counts of findings, of "proven problem" classifications or of calculations are not comparable between model groups: one model may show its arithmetic and the other not, or classify more readily. Record such a difference as a model effect, not as one group finding more. In a real run, one model made checkable calculations and the other did not, and the "proven" counts differed by model.

## 5. Shape of the answers

Run `python method/scripts/stats.py rounds/v<version>`: it gives the average length per round and per model and how many answers have the same number of headings. A uniform shape is an effect of the form; record it, but evaluate the content separately. A systematic difference in length between models (in the skill's own test, opus wrote about 50% more than sonnet in round 2) is also a model effect, not a profile effect.

## 6. List (if active)

From `list-analysis.json`: how many agents put first the item they received on the first row, against what chance would give; and, item by item, whether each item's first places look inflated by position. State the draw's seed.

## 7. Round 3

At the quick level there is no round 3 and no debate: write "skipped (effort: quick)" under sections 7 and 8 (keep the contrarian's part of section 8), and record in section 9 that the panel's agreements were never tested against each other. At the deep level, also say what the second destroyer found that the first did not.

Who took part, on which models, the reason for choosing the two users (one per model), and whether every central rule had at least one defender and one critic. List every **split by model**: classifications or positions that divided exactly along model lines, which stay as hypotheses. In a real run, one scenario split exactly by model: three said "proven problem", three said "hypothesis".

## 8. Contrarian and debate

- What the contrarian pointed out that the rest of the panel had not seen, and what the answers it requested in full revealed (including errors in the moderator's own summary).
- How many replies were **keeps**, **adjusts** and **changes**, from whom, and in which direction: the majority's, the destroyer's or the contrarian's. Retreats that almost all go towards an adversary are conformity just as much as those that go towards the majority.
- **Non-independent convergence:** every point where half or more of the participants changed position in the same direction after reading the same argument. Count it as one movement, not as several independent agreements. Say whose argument it was: in a real run, four convergences all came from one participant's argument read in the same summary.
- **Independent, verified or persuaded:** for each point, how many final positions were independent (held before any argument), verified (changed after an argument, with a quoted passage: one confirmation of that argument's origin) and persuaded (changed with no quote: not counted). Only independent positions count as separate agreements.
- **Who is counted:** confirm that the destroyer and the contrarian were left out of every convergence, consensus or "N of M agree" count.
- **Fresh agents:** confirm that every call was a new agent and that no earlier agent was resumed or continued.
- Which items were settled before the debate and sent straight to consolidation, and why.
- Limitation of the contrarian pack: what reached it as a summary rather than as verbatim text, and which answers it did not request.

## 9. Moderator bias risks

The moderator wrote the scenarios, the summaries, the agenda and the synthesis. Say where your choices may have influenced the result: scenarios that favored one reading, summaries that may have softened a position, points left off the agenda and why.

- **Summary attributions:** how many attribution errors the contrarian (or your own check against the sources) found in your summaries, and which were corrected. In a real run, the moderator's summary had five, and it was the strongest filter of the panel.
- **Scenarios that held the answer:** which proposed scenarios described the action or the outcome and were rewritten before round 3, and whether any that reached the participants still suggested its answer (every participant reproducing the same line is the sign).
- **Leading questions:** whether any question presupposed a problem instead of accepting "none".

Pay special attention to **agreement created by scenarios**: when a finding from a single persona becomes a round 3 scenario and other participants confirm it, count one origin and several confirmations, not several independent discoveries. The same goes for a round 3 **variant built from one persona's proposal**: the participants who favor it confirm one origin. Also record the limits noted in "Notes for the moderator" in `config.md` (self-evaluation, large scope, a system with no real users), any resumes, any checkpoint pauses and whether the author edited the agenda at checkpoint 2. In a re-evaluation, confirm that you read the earlier run only during consolidation, and say whether the checks of the changed sections found new problems there.

## 10. Conclusion

In 3 to 5 sentences: was the variety sufficient? What should change in the next run (personas, models, questions, effort level)?

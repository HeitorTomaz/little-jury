# Guide for `diversity.md`

`diversity.md` is the evaluation of the panel itself and the quality measure of each run. It answers: did the arguments come out varied enough for the panel to be worth more than a single opinion? Where did the personas repeat each other, and why?

Write it in the language set in `config.md`, with numbers and verbatim examples. "The voices seemed distinct" does not work; "6 of 8 users used the phrase 'learning curve' in question 3 of round 2" does.

> **Version 1.** Based on the lessons from rounds 1 to 3 of the pilot. The lessons from rounds 4 and 5 are still to be incorporated (see the last section).

## 1. Models

A table of every agent, with the model used in each round and the agent type. Point out:

- any model change, and why;
- rounds with a single model (there should be none);
- whether the split of models among users was balanced by complexity tolerance.

## 2. Scores

- **Uniformity:** for each dimension, the distribution of scores. All users giving the same score on a dimension is a **signal to investigate**, not a result. Before blaming the personas, check whether the input explains it: with a short pitch, the uniformity can come from the text. That is why clarity is no longer a score: in two runs, all eight users gave the same clarity score, with different justifications.
- **Changes between rounds:** who changed their round 1 score (curiosity, or relevance for a change) in round 2, in which direction, and whether they cited what in the description caused the change. A uniform change (everyone +1) with no cause cited suggests **anchoring**; with a cause cited, it may be real (the short pitch had gaps). In the pilot, all 8 users gave the same round 1 score and all moved it by one point.
- **Comprehension check:** how many pitch problems the check found, and whether they explain uniform scores or repeated confusions. Keep them apart from the project's problems.
- **Undefined audience:** if the audience is undefined, confirm that no synthesis averaged profiles that want opposite things.
- **Model × score:** do scores differ systematically between model groups? If so, separate what is a difference of profile from what may be a difference of model.

## 3. Arguments

- **Repeated criticisms:** for each criticism mentioned by 3 or more participants, how many made it, who, and whether the contrarian considered it grounded. In the pilot, one criticism appeared in 7 of 8 users.
- **Unique arguments:** the arguments raised by a single persona that survived the debate. They are the best evidence that the variety paid off.
- **The imagined-audience persona and the personas outside the audience:** did they say something no other persona said?

## 4. Experts

Separate two kinds of agreement:

- on **contradictions verifiable in the text**: expected; not a lack of diversity;
- on **recommendations** (cuts, platform, first test): this is where the risk lies. Count how many main recommendations coincided and between which models.

In the pilot, the 4 experts on the same model reached the same recommendations.

## 5. Shape of the answers

Run `python method/scripts/stats.py rounds/v<version>`: it gives the average length per round and per model and how many answers have the same number of headings. A uniform shape is an effect of the form; record it, but evaluate the content separately. A systematic difference in length between models (in the skill's own test, opus wrote about 50% more than sonnet in round 2) is also a model effect, not a profile effect.

## 6. List (if active)

From `list-analysis.json`: how many agents put first the item they received on the first row, against what chance would give; and, item by item, whether each item's first places look inflated by position. State the draw's seed.

## 7. Round 3

Who took part, on which models, the reason for choosing the two users (one per model), and whether every central rule had at least one defender and one critic. List every **split by model**: classifications or positions that divided exactly along model lines, which stay as hypotheses. In a real run, one scenario split exactly by model: three said "proven problem", three said "hypothesis".

## 8. Contrarian and debate

- What the contrarian pointed out that the rest of the panel had not seen, and what the answers it requested in full revealed (including errors in the moderator's own summary).
- How many replies were **keeps**, **adjusts** and **changes**, from whom, and in which direction: the majority's, the destroyer's or the contrarian's. Retreats that almost all go towards an adversary are conformity just as much as those that go towards the majority.
- **Non-independent convergence:** every point where half or more of the participants changed position in the same direction after reading the same argument. Count it as one movement, not as several independent agreements.
- Which items were settled before the debate and sent straight to consolidation, and why.
- Limitation of the contrarian pack: what reached it as a summary rather than as verbatim text, and which answers it did not request.

## 9. Moderator bias risks

The moderator wrote the scenarios, the summaries, the agenda and the synthesis. Say where your choices may have influenced the result: scenarios that favored one reading, summaries that may have softened a position, points left off the agenda and why.

Pay special attention to **agreement created by scenarios**: when a finding from a single persona becomes a round 3 scenario and other participants confirm it, count one origin and several confirmations, not several independent discoveries. Also record the limits noted in "Notes for the moderator" in `config.md` (self-evaluation, large scope, a system with no real users), any resumes, any checkpoint pauses and whether the author edited the agenda at checkpoint 2. In a re-evaluation, confirm that you read the earlier run only during consolidation.

## 10. Conclusion

In 3 to 5 sentences: was the variety sufficient? What should change in the next run (personas, models, questions, size)?

---

## Pending: lessons from rounds 4 and 5 of the pilot

*Reserved. When the pilot's `diversity.md` arrives, the lessons about the debate and the consolidation go here and in sections 8 and 9, and may change round 4 in `rounds.md`.*

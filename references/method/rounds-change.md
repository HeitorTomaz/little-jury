# Rounds — variant for changes

Use this file when `config.md` says `Type: change`. It **replaces the questions** in `rounds.md`; everything else (isolation, prompt skeleton, language, draw, scenarios, contrarian, debate, consolidation) follows `rounds.md`. In the debate, the "smallest change" is the smallest adjustment to the plan (or, when the problem is in the current system, the smallest change to it that the plan could include).

The dimensions are `relevance` (round 1), `value`, `adaptation` and `would_accept` (round 2) (see `config.md`), each a question answered with a stance (yes, only if <condition>, or no), the reason first. Clarity is not a stance: the moderator runs the comprehension check of `rounds.md` on question 1, comparing "what will change for you" with what the pitch meant to say.

## Round 1 — users

Input: `01-short-pitch.md` (how the system is today + what will change).

1. In one sentence, what will change for you?
2. What caught your attention?
3. What seemed unnecessary, worrying or confusing?
4. What questions would you have before the change goes live?
5. How does this affect what you do in the system today: better, worse or no change? Why?
6. Would you keep using the system (or, if you do not use it today, would you start)? Why?
7. **Relevance**: "Does this change matter for how you use the system?" The reason, then yes, only if <condition>, or no.

## Round 2 — users

Input: `02-full-description.md` and your own round 1 answer.

1. Describe your first day using the system after the change. *(if the change affects different roles, modes or paths differently, assign different ones across users, as in `rounds.md`)*
2. What would stop working the way you are used to? At what moment would you notice?
3. What part of the change would you ignore or wish did not exist?
4. What in the change, or in the system as it is today, would you keep no matter what, and why?
5. What would make you ask to go back to the old way, or give up on the system?
6. Which of your round 1 questions did the description answer, and which remain open?
7. Additional questions for users in `config.md`.
8. **Expected value** ("Would it be worth it for you?"), **Ease of adaptation** ("Could you adapt to it without much cost?") and **Would accept** ("Would you accept it without leaving the system?"): each with the reason, then yes, only if <condition>, or no. Review your round 1 stance (**Relevance**): if it changes, quote the passage of the description that caused the change.
9. *(if the list is active)* as in `rounds.md`.

## Round 2 — experts

1. Do any items of the change (part B) contradict the current system (part A) or each other? Quote both items in each case. If you find none, say so and say what keeps them consistent.
2. Does the change create a loophole, shortcut or misuse that did not exist before? If so, describe it step by step; if not, say what prevents it.
3. What is the strongest part of the change, and why does it work?
4. Could anything break: flows, integrations, data, permissions, reports, anyone who depends on the current behavior? If you see nothing that would, say so and why.
5. How do data and people move from the old to the new? What happens to someone in the middle of a flow when the change goes live?
6. If it goes wrong, how is it undone? What cannot be undone?
7. Which **[divergent]** or **[documented]** items in part A affect the change, and what would need to be confirmed first?
8. What information is missing to evaluate it?
9. What is the smallest test that could show whether the change solves what it intends, within the means the author has declared, before it affects all users?
10. Is there anything you would cut from or postpone in the change? If not, say so.
11. For the most serious problem you found, what is the **smallest adjustment to the plan** that would solve it, and what is lost with it?
12. The expert's specific questions, in `config.md`.

**Effort level.** As in `rounds.md` ("Effort level"): at the **quick** level the quick wins come from the experts' question 11 (the smallest adjustment to the plan); at the **deep** level `destroyer-2` gets the same question on the other model.

## Round 2 — destroyer

"Present the three strongest arguments for this change to fail or to leave the system worse than it is. For each one: (a) the claim; (b) the chain of reasoning, grounded in the description's items (cite A and B); (c) what would bring this argument down. Also consider the option of not making the change: if it is better, say why."

## Round 3 — scenarios

Participants, the closing question ("which of these rules held up well") and the rule that a scenario describes the situation, never the action or the outcome, follow `rounds.md`. In addition to the sources in `rounds.md`, include at least two **transition** scenarios (someone in the middle of a flow when the change goes live; old data that does not fit the new rule; rolling back after a week) and, if the author considered alternatives, present them as **anonymous alternatives**.

Classification: a part B item that contradicts an **[implemented]** part A item is a **proven problem**; one that contradicts a **[documented]** or **[change: proposed]** item stays a **hypothesis**, with any dissent recorded.

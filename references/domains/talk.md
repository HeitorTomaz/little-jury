# Domain profile: talks and conference proposals

- **Families:** criteria (the usual one for a proposal: a program committee judges the submission against the call for papers). Audience for the talk itself (an outline, a script, the text of the slides): attendees from beginner to expert react to it.
- **Round 3 tests:** the talk's promises (title and abstract) against what the outline actually delivers; its central claims against the questions the audience would ask in the Q&A; the plan against the time slot (what happens at minute 20 of a 30-minute talk).
- **Users label:** Reviewers (criteria) · Attendees (audience)

A starting point for evaluating a conference talk, a workshop or a submission to a call for papers or proposals, before it is sent or given. The type is `work`: the proposal (title, abstract, outline, speaker notes, the text of the slides) goes into the panel verbatim (`references/work.md`), and the abstract is the short pitch. Slides that are mostly images go in as their text plus a one-line description of each image, recorded in `prep/decisions.md`. The call for papers, when the author gives it, is the source of the criteria (`input/03-criteria.md`). The personas below are generic; **adapt them to the event** (an academic conference, a developer meetup, an industry summit and a school event want different things). Write them in the language recorded in `config.md`.

Remove the speaker's name, employer and biography before the panel sees the proposal, unless the call for papers asks the committee to judge the speaker; when it does, keep only what the submission form would show, and record the choice in `prep/decisions.md`.

## Vocabulary

- In the criteria family, jurors are **reviewers** of the program committee ("Reviewers"). In the audience family, users are **attendees** ("Attendees").
- "The work" is "the talk" or "the proposal"; "a revision" is a change to the title, the abstract, the outline or the slides.
- A stance of **only if** is "accept with changes": the condition is the change, in one sentence.
- Proven problem: two parts of the proposal contradict each other (the abstract promises what the outline never reaches, the outline does not fit the stated length), or the proposal contradicts an explicit rule of the call (format, length, topic, level).

## Criteria (criteria family; default set, replace with the call's when given)

| id | Name | Question |
|---|---|---|
| fit | Fit to the event | Does the talk fit the event's audience, track and format as the call describes them? |
| novelty | Something new | Will the audience hear something they cannot get from the first search result on the topic? |
| takeaways | Concrete takeaways | Does the proposal say what the audience will be able to do or understand afterwards? |
| timing | Fits the slot | Can the outline be delivered in the time given, with room for questions? |
| abstract | Clear abstract | Would an attendee reading only the title and the abstract know what the talk is and whether it is for them? |

## Reviewers (criteria family, standard: 6, 3 per model; quick: 4; deep: 9)

Distribute the strict and the lenient profiles across both models, so strictness is not confused with the model.

### chair — Track chair
- **Perspective:** builds a balanced track; has more good proposals than slots.
- **Strictness:** high on fit and on overlap with other talks on the same topic.
- **Reads first:** the title, the abstract and the level.
- **Tends to miss:** the quality of the outline.
- **Rejects when:** the talk does not fit the track or repeats a topic the event already covers.

### expert-reviewer — Expert reviewer
- **Perspective:** knows the topic deeply; checks whether the talk says anything new and says it correctly.
- **Strictness:** high on novelty and accuracy, lenient on delivery.
- **Reads first:** the outline and the claims.
- **Tends to miss:** whether a less expert audience could follow.
- **Rejects when:** the content is introductory material presented as new, or contains errors.

### newcomer-advocate — Reviewer for newcomers
- **Perspective:** speaks for the part of the audience that is new to the topic or to the event.
- **Strictness:** lenient on novelty, strict on clarity and on assumed knowledge.
- **Reads first:** the abstract and the stated level.
- **Tends to miss:** depth that experts would want.
- **Rejects when:** the stated level is wrong, or the talk assumes knowledge it never introduces.

### organizer — Organizer
- **Perspective:** worries about the day itself: timing, room, equipment, how the talk fits the schedule.
- **Strictness:** high on timing and logistics, lenient on content.
- **Reads first:** the format, the length and any special needs.
- **Tends to miss:** the substance of the talk.
- **Rejects when:** the plan cannot fit the slot or depends on something the venue cannot provide (a live demo with no fallback, for instance).

### skeptic — Skeptical reviewer
- **Perspective:** has seen many vendor pitches dressed as talks; looks for the sales angle.
- **Strictness:** very high on promotional content and on claims without evidence.
- **Reads first:** the abstract's promises.
- **Tends to miss:** a genuinely useful talk that uses the speaker's own product as an example.
- **Rejects when:** the talk exists to sell, or its claims cannot be checked.

### past-speaker — Experienced speaker
- **Perspective:** has given many talks at events like this; knows what works on stage.
- **Strictness:** medium; strict on structure, on the opening and on the ending.
- **Reads first:** the outline, looking for the arc.
- **Tends to miss:** fit with the call's formal rules.
- **Rejects when:** the talk has no arc (a list of points with no reason to be in that order) or no clear ending.

### Reserved for the deep level
- **diversity-reviewer:** checks whether the examples and the language exclude part of the audience.
- **academic-referee:** for academic conferences, judges the proposal as a short paper.

## Attendees (audience family, standard: 8; quick: 4; deep: 11)

Write each with the structure of `composition.md`. The eighth seat is the **audience the author imagines**.

- **beginner:** new to the topic; came to learn the basics; quits when the first slides assume what they do not know.
- **expert:** knows more than most speakers; came for the one new idea; quits when the talk stays at the surface.
- **manager:** decides what the team adopts; wants the trade-offs, not the details; quits when there is no "so what" for decisions.
- **title-picker:** chooses talks by the title in the program, between two rooms; quits (walks out) when the talk is not what the title promised.
- **remote-viewer:** watches the recording later at 1.5x speed; quits when the talk depends on being in the room (demos too small to see, jokes about the venue).
- **second-language:** follows the talk in a language that is not their first; quits when the speaker relies on idioms and speed.
- **skeptic-attendee:** expects a sales pitch; quits at the first slide that looks like an advertisement.
- **<id> — audience imagined by the author.**

Grid questions for attendees: `curiosity` "Would you choose this talk over the others in its slot?"; `value` "Would you leave with something you can use?"; `ease` "Could you follow it at your level?"; `would_try` "Would you recommend it or share the recording?".

## Experts

### content — Specialist of the topic
Evaluates whether the content is correct, current and at the level announced. Asks: which claim would an expert in the room challenge first? What is the one idea the talk adds? What is missing that the audience will ask about?

### coach — Speaking and structure specialist
Evaluates the arc, the opening, the ending, the pacing and the slides as text. Asks: what does the audience know after the first two minutes? Where will attention drop? Which section could go to fit the time? What is the last thing the audience hears?

### event — Event and community specialist (the only one who gets web access, in round 2)
Evaluates fit with the event and its audience: the call's rules, past programs, the kind of talk that is usually accepted, overlap with talks already given. When this persona has web access in a round, it checks the call for papers, the event's past programs and recordings, and recent talks on the same topic, marking [not verified] what it could not check; without web access, it says it is answering without checking.

### Reserved for the deep level
- **demo — Live demo specialist:** evaluates whether a live demo is worth its risk, and the fallback.

## Typical additional questions (they go into `config.md` when they apply)

- **Reviewers, round 1:** "If you could accept the talk only with one change, what would it be?" (already the revision question in `rounds-criteria.md`; keep it).
- **Attendees, round 2:** "At which point in the outline would you check your phone, if any?"
- **Attendees, round 2:** "What question would you ask in the Q&A?"
- **coach, round 2:** "If the slot were cut by a third, what would go?"
- **event, round 2:** the call's rules and recent talks on the same topic at this event and similar ones; if there is a list of titles, rank them for this event's program.
- **Round 3:** for each central claim, include the hardest question from the audience the panel raised, written neutrally ("Consider the claim X. From the audience: Y?").

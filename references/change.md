# Preparing the evaluation of a change

For the **change** type: the author gave a file with the plan or description of a change to a system that already exists. The panel evaluates **the change**, not the whole system: what it solves, for whom, what it contradicts in what already exists, what breaks, and how to test it before committing the system to it. Write everything in the language recorded in `config.md`.

Read `references/extract-system.md` first: the part of the system affected by the change is extracted with the same rules.

## 1. Reading the plan

- Read the whole file given. If it cites other documents (issues, specs), ask the author in the question block whether they are part of the plan before opening them.
- Separate, as with any concept, what the plan **decides** from what it **proposes** and what it leaves **open**.
- Plans usually come full of defense ("this will finally solve the problem of…", "the most elegant solution"). Remove it, as in `prepare.md`, and record it in `removed.md`.
- If the plan already describes the implementation (classes, tables), translate it into the effect it has on the people who use and operate the system; technical details only go in when they change what the panel can evaluate (data migration, compatibility, performance, a new dependency).
- From the plan, define the extraction scope (affected area plus neighborhood) and include it in the question block.

## 2. Interview: extra items

In addition to what `prepare.md` asks, in the same single question block:

| Item | Why it matters |
|---|---|
| Why the change is being considered, **in facts** (incidents, user requests, limits reached) | becomes **[fact]**; opinions on why it is good stay out |
| Who is affected and how many, if the author knows | defines the current users |
| Transition constraints (no downtime, deadline, data that cannot be lost) | the recommendations must fit them |
| Alternatives the author has already considered | become round 3 scenarios, presented as **anonymous alternatives** |
| What the change deliberately does **not** alter | keeps the panel from criticizing what is out of scope |

## 3. Inputs

### `input/01-short-pitch.md`

Two parts, 350 to 450 words in total, with no references and no jargon:

1. **How the system is today** (100 to 150 words): what the user does today in the affected area, neutrally, without pointing out defects the author wants to fix.
2. **What will change** (250 to 300 words): what changes for the people who use it, when and how they find out, what stays the same.

The round 1 user is someone who already uses the system being told about the novelty. They must not receive the reason for the change in the author's voice; if there is a factual reason (for example, "the system started rejecting files over 10 MB"), it can appear as a fact.

### `input/02-full-description.md`

```markdown
**How to read:** part A describes the system as it is today, only in the affected area. Part B describes the change.
Part A markers: **[implemented]**, **[documented]**, **[divergent]**, **[undefined]**.
Part B markers: **[change: decided]**, **[change: proposed]**, **[change: undefined]**.
**[fact]** describes the author's or team's situation. The `[ref: …]` references show where the information
was extracted from; you do not have access to these files and do not need them to answer.

None of these decisions is untouchable. The panel may recommend changing, postponing or not making the change.
```

- **Part A — Current system (affected area):** numbered items (A1, A2…), with marker and reference.
- **Part B — The change:** numbered items (B1, B2…), each saying **which part A item it alters** ("alters A3") or "new". Include the transition (how data and people move from the old to the new) and the rollback, even if it is **[change: undefined]**.
- **Part C — What does not change:** what the author declared out of scope.
- **Part D — Situation and constraints:** **[fact]** items and decisions that limit the recommendations.

### `moderator/author-concerns.md`

As in `prepare.md`. Include the alternatives the author considered: they become anonymous scenarios.

## 4. Personas and configuration

- **Users:** the current ones, derived from the system (`extract-system.md`, section 5), plus **one or two who do not use it**: someone who might start using it because of the change, or might give up because of it. 8 in total in the lean panel, as with the other types.
- **Experts:** the four in `composition.md`, with the "build" function focused on **migration, compatibility and operations** and the "systems and loopholes" function focused on **the new loopholes and edge cases the change creates**.
- **Dimensions** (in `config.md`, with these `id`s):

| id | name | description | round |
|---|---|---|---|
| clarity | Clarity | Understood what changes from the short pitch | 1 |
| relevance | Relevance | The change matters for how they use it | 1 |
| value | Expected value | How much the change improves their use | 2 |
| adaptation | Ease of adaptation | How costly it is to get used to the change (5 = almost nothing) | 2 |
| would_accept | Would accept | Willingness to accept the change without leaving the system | 2 |

- In `config.md`, fill in `Type: change`, the plan file, the source commit and the extracted areas.

# Prepare

This session is open at the project root and can read the concept document, the code and the change plan. It is the only moment when anyone on the panel's side sees that material. The job here is to turn it into **neutral** inputs, set up a `panel/` folder from which the run cannot see anything else, start the isolated run and deliver the report.

**The author is asked only once, in the question block of section 2.** After that, everything continues to the report without asking them anything. Decide what they did not answer using the skill's recommendations, and record each decision in `prep/decisions.md` for them to check later.

**Language:** ask the questions in the language the author is using in the conversation (default English) and record it in `config.md` as `- Language: <language>`. Everything prep writes (inputs, personas, config values, author concerns, `removed.md`, `decisions.md`) is in that language. The isolated run reads the language from `config.md`.

## Contents

1. Evaluation type and reading the material
2. Questions to the author (the only interaction)
3. Writing the inputs
4. Personas, dimensions and configuration
5. Self-check
6. Setting up the folder
7. Run and deliver
8. A new version of an earlier evaluation

---

## 1. Evaluation type and reading the material

- If the current directory is `panel/` or inside it, stop: preparation must run at the root.
- If `panel/` already exists, read `panel/config.md` to learn what was evaluated before, and also see section 8.
- Decide the type with the table in `SKILL.md`:
  - **concept:** look for the concept document at the root (and only there; do not sweep the disk). Follow this file.
  - **system:** follow this file and `references/extract-system.md`, which says how to extract what the system does from code, documentation and comments.
  - **change:** the file given with the command is the plan. Follow this file, `references/extract-system.md` and `references/change.md`.
- **Read all the material before asking.** For system and change, do the sweep in `extract-system.md` (section 2) at this stage: the system's size and areas go into the questions.
- For system and change, the panel lives **inside the repository**, in `panel/` at the root. Setup generates the configuration that keeps the run from seeing the repository's `CLAUDE.md`, the project rules and the git history (section 6).

## 2. Questions to the author (the only interaction)

Ask **a single block of questions**, in the author's language, only about what the material does not answer, offering options with a recommendation where it fits. If there is doubt about the type or which document to use, it goes in this block. Three questions matter most, because no document usually answers them and because they guide the moderator:

| Item | Why it matters |
|---|---|
| **Who the project is for**, in the author's view | defines the "imagined audience" persona and the user profiles |
| **What the author wants to decide with this evaluation** (go or no-go, what to cut, what to test first, whether a change is worth the risk…) | goes into `config.md` as the objective; the moderator uses it to choose scenarios, the debate agenda and the emphasis of the consolidation. It **never** goes to the personas |
| **What the author wants to test or fears** (concerns) | becomes `moderator/author-concerns.md` |

The other items, when the material does not answer them:

| Item | Why it matters |
|---|---|
| Project type (game, app, physical product, service, business, other) | picks the domain profile and the vocabulary |
| For system and change: scope; if the description is likely to exceed 5,000 words, the split into areas (see `extract-system.md`) | overly long descriptions dilute the personas' attention |
| For system and change: will `panel/` and `prep/` be versioned in git or ignored? | if ignored, add them to `.gitignore`, with the permission given here |
| Version of the concept or system | names the output folder (`rounds/v<version>/`) |
| Author decisions that limit the recommendations (e.g. a fixed launch date, budget, one-person team, "no testing with real users before the first prototype") | without them, the panel recommends what the author cannot do |
| Author situation that is a fact (e.g. an existing developer account) | goes in as **[fact]** |
| Is there a list for the panel to rank? (names, slogans, variants) | turns on the list, the draw and the report section |
| Which external facts need checking against a source (store rules, regulations, trademarks, platform documentation) | defines the questions for the expert with web access |
| Size: lean (default) or full | see `composition.md` |

In the same block, say what happens next: the run takes from tens of minutes to a few hours, makes about 45 to 65 agent calls (it may span more than one usage window of the plan) and ends with the report open in the browser. External evaluations made in another AI tool can be placed in `panel/input/external/` before the author answers; after that there is no way to include them in this run.

Do not ask the author which list item they prefer; the panel must not know.

## 3. Writing the inputs

### Neutrality rules (apply to all inputs)

- **Remove every argument defending the idea**, whether from the author or from assistants who talked with them ("this is innovative because…", "it solves the problem of…", "users will love…").
- **Do not cite comparisons the author made** with existing products ("it's like X meets Y"). The panel must reach its own.
- **Do not use sales adjectives** (unique, revolutionary, addictive, intuitive).
- **Future intentions are intentions**, stated as such, without promises.
- **Do not fill gaps.** If the concept does not say it, the input does not either; in the full description it becomes **[undefined]**.
- **State the decisions that limit the recommendations**, so the suggestions fit the author's real means.
- For system and change, the same rules apply to **code comments, documentation, `CLAUDE.md`, decision records and the change plan**: facts and rules go in, justifications do not.
- The author's objectives with the evaluation do not go into the inputs: only into `config.md`.

**By type:** the sections below describe the **concept** type. For **system**, the short pitch describes what the system is and does today, at the same length, and the full description uses the markers and references from `extract-system.md` (section 4). For **change**, the inputs follow `change.md` (section 3).

**Where to write:** write the inputs in `prep/`, **at the root, outside `panel/`**, with the same names they will have in the panel (`prep/input/01-short-pitch.md`, `prep/moderator/author-concerns.md`, `prep/personas.md`, `prep/config.md` etc.). Setup copies them into `panel/`.

Keep everything you removed, with the original passage and the reason, in `prep/removed.md`. That file **never** goes into `panel/`: the author can check it later, but the moderator must not see it, because it would be influenced too.

### `input/01-short-pitch.md` (round 1, users only)

- 250 to 300 words in the body, not counting the title, the name line and the italic header saying it is round 1 material and nothing should be added.
- Say what it is, what a person does when using it, in what situation, what changes from one time to the next (if anything) and what is planned for the future.
- Name: the current one, or "not yet defined".
- Write like someone describing the project to a stranger without trying to convince them.

### `input/02-full-description.md` (round 2 onwards, everyone)

Open with this block, adapted:

```markdown
**How to read:** each item carries a marker. **[decided]** is the author's choice. **[proposed]** is an idea
not yet confirmed. **[undefined]** is a known gap. **[fact]** describes the author's situation.
Evaluate what is written. If information is missing to judge something, point out the gap instead of
assuming how it works.

None of these decisions is untouchable. The panel may recommend changing any of them.
```

Write this block in the author's language, but keep the markers themselves in English (`[decided]`, `[proposed]`, `[undefined]`, `[fact]` and the others): they are the skill's vocabulary, read by the moderator and the method in any language.


- Organize into sections that make sense for the domain (for a game: experience, structure, actions, rules; for an app: problem, audience, main flow, features, data, revenue model; for a business: proposition, customer, operations, revenue, costs).
- **Each item with exactly one marker.** Use variants when they are true: "[decided for the first version]", "[decided, subject to review]", "[proposed, accepted without testing]".
- Include a section for what does not exist yet, and end by saying what has been built or tested so far (e.g. "Nothing has been built or tested yet. Everything above is design.").
- The author's imagined audience: in the description, **[decided]** if they declared it as a decision and **[undefined]** if they only imagine it. In both cases, the "imagined audience" persona is written from what they imagine.

### `input/03-list.md` (optional)

- A title saying what the list is ("Candidate names", "Candidate slogans").
- A table in **alphabetical order** with a neutral description column (literal meaning, origin), with no hint of preference.
- Say explicitly that the order does not reflect the author's preference and that it will be shuffled per agent.
- Record what the author has already checked and what it did not cover (e.g. "web search found no conflict; did not cover store catalogs or trademark registries").

### `moderator/author-concerns.md` (moderator only)

- Open with an italic warning: do not pass this file, or any part of it, to any persona; it only serves to build the round 3 scenarios.
- One concern per line, as a question. Include rule variants the author is considering: they become scenarios presented as anonymous alternatives.

## 4. Personas, dimensions and configuration

Read `references/composition.md`. For games, start from `references/domains/game.md`; for other domains, generate the personas following the composition rules.

Produce two files:

### `personas.md`

Same format as the domain profile: the general rules for all personas, then each role with its `id`. Each user with perspective, what they usually use, tolerance for complexity, available time, what they look for and what makes them quit. Roles reserved for the full panel at the end.

### `config.md` (read by the moderator only)

```markdown
# Panel configuration

- Project: <name or short description>
- Type: concept | system | change
- Language: <language of the conversation with the author; default English>
- Domain: <game | app | ...>
- Version: <version of the concept or system>   → outputs in rounds/v<version>/
- Source: <concept document | commit and branch | plan file + commit>
- Extracted scope: <whole system | areas>   (system and change types)
- Size: lean | full
- Preparation date: <date>

## Author's objectives with this evaluation
- <what they want to decide; guides scenarios, agenda and consolidation; never goes to the personas>

## Grid dimensions (scores from 1 to 5, higher is better for the project)
<!-- Change type: use the dimensions in change.md (clarity, relevance, value, adaptation, would_accept). -->
<!-- System type: the same as below; "Would try" means "would keep using or start using". -->
| id | name | description | round |
|---|---|---|---|
| clarity | Clarity | Understood the proposal from the short pitch | 1 |
| curiosity | Curiosity | The proposal made them want to know more | 1 |
| value | <Expected value / Expected fun / ...> | <...> | 2 |
| ease | Ease of entry | How easy the proposal seems to start using | 2 |
| would_try | Would try | Willingness to try it | 2 |

## List to rank
- Active: yes | no
- File: input/03-list.md
- Who ranks: all users and <id of the relevant expert>
- What to check: <e.g. trademarks and store catalogs>

## Web access
- Who: <id> (only one)
- What for: <closed list of what they check>

## Additional questions
### Users, round 2
- <e.g. reaction to the proposed revenue model, if any>
### <expert id>, round 2
- <specific questions>

## Launch / channel
- Ask about the launch channel: yes | no
  (yes when the author has not yet decided how the project reaches its audience; no when they have)
- <context: what the author has already decided about the channel>

## Model distribution
| id | group | model | tolerance for complexity |
|---|---|---|---|

## Author decisions that limit the recommendations
- <copied from the full description, for the moderator to check the recommendations against>

## Notes for the moderator
- <known limits of this run: self-evaluation, scope above 5,000 words kept by the author,
  system without real users etc.; they go in as limits in diversity.md>
```

In a system that has no users yet besides the author, the user personas are in practice potential users: in "Usually uses" write what each one uses today instead of this system, and record this under "Notes for the moderator".

## 5. Self-check

There is no author review before the run. Instead, check it yourself and fix what fails:

- [ ] The short pitch has 250 to 300 words in the body (350 to 450 for the change type), no sales adjectives, no author comparisons, no `[ref: …]` references.
- [ ] Every item in the full description has exactly one marker; for system and change, every [implemented], [documented] or [divergent] item has a reference.
- [ ] Re-read three [implemented] rules at random against the code (system and change types).
- [ ] No passage from `removed.md`, no author objective and no author concern appears in the inputs.
- [ ] The personas meet the requirements of `composition.md` (someone outside the audience, someone from the imagined audience, spread tolerances, opposite motivations) and pass the opposite-pair test.
- [ ] Every question that requires external checking goes to the expert with web access, and no question to a tool-less persona depends on a tool.
- [ ] `config.md` records the language, and everything you wrote is in it.
- [ ] `prep/decisions.md` lists what you decided on the author's behalf.

## 6. Setting up the folder

Run the setup script in the skill's folder (the one containing `SKILL.md`), with `python` or `python3`, whichever exists:

```bash
python <skill-folder>/scripts/assemble_panel.py <project-root>/panel
```

It creates the structure and:

- **generates `.claude/settings.json` for the folder's location**: read block outside it, `claudeMdExcludes` with every `CLAUDE.md`, `CLAUDE.local.md` and `.claude/rules/` in the folders above (a repository's `CLAUDE.md`, for example) and `includeGitInstructions: false`, which takes the git status and recent commits out of the run's context. In a test with version 2.1.329, without that last option the last commit message reached the context. If the folder is moved, run the script again: the patterns are computed from the path; It also denies edits to `method/` and `.claude/`, so the isolated run cannot replace the scripts it is allowed to execute, nor its own settings.
- copies the two agent definitions, `method/` (the run method and scripts) and `template/` (the report template and its fonts);
- never overwrites `input/`, `moderator/`, `personas.md`, `config.md` or `rounds/`.

Then copy the files in `prep/` to the same paths inside `panel/`, **except `prep/removed.md` and `prep/decisions.md`**:

```
panel/
├─ .claude/settings.json            read block, CLAUDE.md exclusions, git out of context
├─ .claude/agents/persona-isolated.md
├─ .claude/agents/persona-web.md
├─ README.md                        points to method/
├─ method/                          method copied from the skill + scripts
├─ template/report-template.html    and template/fonts/
├─ config.md
├─ personas.md
├─ input/01-short-pitch.md
├─ input/02-full-description.md
├─ input/03-list.md                 if any
├─ input/external/README.md
└─ moderator/author-concerns.md
```

Check that nothing from `removed.md`, `decisions.md`, the concept document, the change plan or the code was written inside `panel/`.

## 7. Run and deliver

The run **cannot** happen in this session: it can see the concept and the code. Start a new Claude Code session, isolated inside `panel/`, with the skill's script:

```bash
python <skill-folder>/scripts/run_panel.py <project-root>/panel --open
```

- Run it **in the background** if your terminal tool allows it, and wait for the completion notice; the run takes from tens of minutes to a few hours. Do not keep polling for progress.
- The script opens `claude -p` with the working directory in `panel/`, allows only the tools the method needs (files inside the folder, subagents, web, the scripts in `method/scripts/`) and saves the output in `panel/runs/`.
- When it finishes, it says whether the run completed (and opens the report in the browser, with `--open`) or was interrupted, for example by the plan's usage limit.

**Completed:** validate the report (`python panel/method/scripts/report.py validate <report.html> --template panel/template/report-template.html`) and deliver to the author, in their language, in this order:
1. the full path of `report.html`, which is already open in the browser: it is the deliverable for them;
2. in a few lines, what the panel concluded, from `concept-review.md`;
3. where to see what you decided on their behalf (`prep/decisions.md`) and what was removed from the inputs (`prep/removed.md`);
4. that the `.md` files in `panel/rounds/v<version>/` are for Claude: to continue the conversation about the project in a future session, just point Claude at that folder.

**Interrupted:** tell the author at which stage it stopped (from `progress.md`) and how to resume: `/mock-jury run` at the project root, after the usage limit resets. The script resumes where it stopped.

## 8. A new version of an earlier evaluation

- Earlier outputs stay in `rounds/v<earlier-version>/`, each with a copy of the inputs it used; do not delete them.
- In a repository, a change evaluation after a system evaluation (or another change) uses the same `panel/` folder: give the version a name that says what was evaluated (for example, `v2.3-billing-change`).
- Write new inputs from the updated material. You may overwrite `input/` and `moderator/`, because the earlier run kept its own copy.
- Keep the same personas and the same model distribution, unless the author asks otherwise: that is what makes versions comparable.
- Run `assemble_panel.py` again to update `method/` and `template/` if the skill changed; the script warns if the method version changed, and the author must be told, because it affects the comparison.
- Update the version in `config.md`.

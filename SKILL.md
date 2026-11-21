---
name: mock-jury
description: Critically evaluates a project still on paper, a system that already exists, or a planned change to an existing system (game, app, product, service, business) with a mock jury, a panel of synthetic personas (users, experts and adversarial agents) that work in isolated rounds and end in a report with tensions, risks, gaps and hypotheses to test. Use it whenever someone wants to put a concept document, a change plan, an idea not yet built or their own system through a critical review, simulate how different audiences would react, "test it with personas", find contradictions and loopholes in their own rules, decide what to test first, or rank names and other candidates with simulated opinion, even if they never say "panel" or "mock jury". Also use it to prepare, run, resume or continue a panel already set up (a panel/ folder with method/ or progress.md). Requires isolated Claude Code subagents.
argument-hint: "prepare [change-plan-file] | run"
---

# Mock jury

A mock jury: a panel of agents that examines a project the way an independent group would, before the real decision, and leaves the decision to the author. It tries to find out whether the proposal is interesting, for whom, what the problems are and what to test first. It does not exist to improve or defend the idea. The main session is both orchestrator and moderator: it builds the prompts, creates the agents, saves the answers and consolidates the result.

**Language.** Talk to the user and write every output in the language the user is using in this conversation; default to English. Preparation records it in `config.md` as `- Language: <language>`, because the isolated run session cannot see this conversation. The method files stay in English; everything the panel produces (questions to the author, inputs, personas, persona prompts and answers, round files, `.md` outputs, report data and report labels) is in that language. The skill's machine-readable vocabulary stays in English in every language: markers such as `[decided]` or `[implemented]`, ids, dimension ids, file and folder names, JSON keys and enum values. The "How to read" block of the full description explains the markers in the author's language.

**What the panel does well:** contradictions between the project's own rules; dominant strategies, shortcuts and loopholes; specification gaps; audience splits (what attracts one profile and pushes another away); minimal tests for the main hypothesis; checking external facts against a source. For an existing system, also divergences between documentation and code, and the impact of a change on what already exists.

**What it does not do, and you must tell the author if they expect it:** whether the proposal works or is enjoyed in practice; forecasts of market interest or commercial success; approval percentages. Simulated opinions are not research.

Arguments for this invocation: `$ARGUMENTS`

## Commands

| Command | Where the session is open | What it does |
|---|---|---|
| `/mock-jury prepare` | at the project root | evaluates a **concept** (no code) or the **existing system** (with code), from start to report |
| `/mock-jury prepare <file>` | at the repository root | evaluates a **planned change**, described in the file, to the existing system, from start to report |
| `/mock-jury run` | at the root, with `panel/` already set up | runs or resumes the run in an isolated session inside `panel/` and delivers the report |

Natural-language requests ("prepare a panel for this concept", "run the panel") count the same as the commands.

**The author is asked only once**, in the question block at the start of preparation: the project, who it is for, and what they want to decide with the evaluation. After that, everything continues without intervention until the report opens in the browser, unless the author asked for the optional **checkpoints** (after round 1 and before the debate): the run then saves everything, stops, and `/mock-jury run` continues it.

**Re-evaluation.** When `panel/rounds/` already has a completed run of an earlier version of the same project, `prepare` treats the revised version as a re-evaluation: same persona profiles and models, fresh instances, the earlier problems checked in round 3 and a comparison (resolved, partly, unresolved, new) in the report. See section 8 of `references/prepare.md`.

Isolation is what gives the panel its value: if a persona sees the author's decision history, the arguments the author used to defend the idea, the code with its comments, or another persona's answer, it stops being an independent opinion. That is why the run never happens in the session that prepared it: the script `scripts/run_panel.py` opens a new Claude Code session (`claude -p`) with its working directory inside `panel/`, where the read block and the context exclusions apply.

## How to know what to do

1. The working directory contains `method/run.md` and `.claude/settings.json` → this already is the isolated session: follow **Run** below (if an incomplete `rounds/<version>/progress.md` exists, it is a resume). If the author asked to "prepare" here, explain that preparation runs at the project root.
2. The directory ends in `panel` but has no `method/` → stop and say so: the folder was put together by hand or preparation did not finish.
3. The author asks to **run** and the session is at the root, with `panel/method/` below → **do not run in this session**, which can see the concept and the code. Start the isolated session as section 7 of `references/prepare.md` says, and deliver the report.
4. Any other case → **Prepare**, with the type decided as follows (ask in the question block when it is not obvious):

| Situation | Type | Main input |
|---|---|---|
| There is no project code; there is a concept document | **concept** | the concept document |
| There is code (and maybe documentation) and no file was given | **system** | what the system does today, extracted from code, documentation and comments |
| There is code and a file with the plan or description of a change was given | **change** | the plan + the part of the system it affects |

If the file given does not look like a change plan (for example, it is the concept of a new product in an empty repository), ask before deciding.

## Principles

They apply to every type. Explain them to the author when asked for something that goes against them.

1. **Isolated initial evaluations.** No agent sees another's answer before the debate. This is what keeps the panel from becoming an echo of a single opinion.
2. **An adversarial group** to fight artificial agreement, the natural defect of several agents on the same model.
3. **Every claim is classified** as an **observation**, a **hypothesis** or a **proven problem**. A proven problem only when it follows directly from two written rules that contradict each other (in an existing system, code and documentation count as written rules); everything else is a hypothesis until someone uses the product.
4. **Do not invent what is not specified.** Gaps are recorded as gaps: a panel that fills holes with assumptions is evaluating a project that does not exist.
5. **Preserve minority positions**, recording who disagreed.
6. **Do not force consensus.**
7. **Every recommendation states** what problem it solves, what benefit it expects and what is lost.
8. **The final decision belongs to the author.**

## Prepare

Read `references/prepare.md` and follow it. Depending on the type, it also points you to `references/extract-system.md` (system and change types) and `references/change.md` (change type). In short:

1. Decide the type and read all the material (for system and change, already sweeping the repository).
2. **A single block of questions to the author**, in their language: who the project is for, what they want to decide with the evaluation, what they fear, and whatever else the material does not answer.
3. Write the neutral inputs in `prep/`, outside `panel/`, recording in `prep/removed.md` what was removed and in `prep/decisions.md` what you decided on the author's behalf.
4. Propose personas and grid dimensions (`references/composition.md`; for games, `references/domains/game.md`) and run the self-check.
5. Set up `panel/` with `scripts/assemble_panel.py` (which generates the context exclusions for the folder's location) and copy the inputs in.
6. Start the isolated run with `scripts/run_panel.py`, wait, and deliver the report.

## Run (inside `panel/`)

In this session the method is **copied inside `panel/method/`**. Read `method/run.md` and follow it; it points to the other files in `method/`. Do not read the reference files in this skill's folder: with the read block active they may be out of reach, and the local copy is the version of the method this panel was set up with, which keeps runs from the same folder comparable.

The run continues until the report. It stops only if an isolation test fails or at the optional checkpoints recorded in `config.md` (`- Checkpoints:`), where it saves everything and ends; `/mock-jury run` resumes it.

## Files in this skill

| File | When to read |
|---|---|
| `references/prepare.md` | prepare, start to finish |
| `references/extract-system.md` | prepare for the system and change types |
| `references/change.md` | prepare for the change type |
| `references/composition.md` | when proposing personas and models |
| `references/domains/game.md` | when the project is a game |
| `references/method/*` | do not read directly; it is copied to `panel/method/` and read there |
| `assets/panel-template/` | copied to `panel/` by the setup script |
| `scripts/assemble_panel.py` | sets up or updates the `panel/` folder |
| `scripts/run_panel.py` | runs or resumes the panel in an isolated session and opens the report |

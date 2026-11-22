# little-jury

A [Claude Code](https://code.claude.com) skill that puts your project or your work in front of a **little jury**, a mock jury of synthetic personas (users or jurors, experts and two adversaries) that review it in isolated rounds and hand you an HTML report with the tensions, risks, gaps and what to test or revise first.

It is not only for software. It works on:

- **a concept** that is still on paper (a game, an app, a product, a service, a business);
- **an existing system**, described from its code, docs and comments;
- **a planned change** to an existing system, described in a plan file;
- **a piece of work** judged as written: a scientific paper, a book or chapter, a thesis, an exam and its answer key, an exam answer.

The jury works in one of two ways. In the **audience** family, the personas react as your public would (players, users, readers, students facing an exam). In the **criteria** family, a bench of jurors judges the work against explicit criteria, like a peer review, a thesis committee or a grader with an answer key.

The jury deliberates; **you decide**. The report never gives a verdict.

## What it is good at, and what it is not

**Good at:** contradictions between your own rules, dominant strategies and loopholes, gaps in the specification, audience splits (what attracts one profile and drives away another), the smallest test for your main hypothesis, quick wins (the smallest change that would solve each problem, and what it costs), sentences of your pitch that readers misunderstand, and checking external facts against their sources (store rules, platform docs). Trademark registries often cannot be checked automatically (interactive forms, CAPTCHAs); the report marks them [not verified].

**Not:** telling you whether people will actually like it, predicting market interest, or giving approval percentages. Simulated opinions are not research, and the report says so. That is also why the personas do not rate the project from 1 to 5: each one answers a few questions (would you want to know more, would it be worth it, would you try it) with **yes**, **no** or **only if…**, and the condition behind an "only if" is usually the most useful line in the report. A persona the question does not fit (someone who would only get notifications, say) answers **does not apply**, with the reason, and stays out of the count.

## How it works

1. **You ask once.** Run `/little-jury` at the root of your project, optionally followed by what you want to find out. The skill reads your material and asks one block of questions: who the project is for, what you want to find out (it only confirms it if you already said it, and offers a general evaluation of the project if you did not), what worries you, and anything the material does not answer.
2. **It writes neutral inputs.** It strips your arguments in favor of the idea, your comparisons with other products and the justifications in code comments, and records what it removed in `prep/removed.md` so you can check later.
3. **It runs the jury in isolation.** It assembles a `panel/` folder and starts a separate Claude Code session inside it. That session cannot read the rest of your project: reads outside the folder are blocked, the project's `CLAUDE.md` files and git history are kept out of its context, and the personas run as subagents with no tools at all.
4. **Five rounds:** first impression, detailed analysis, extreme scenarios, debate (with a consensus challenger) and consolidation. By default there are no stops; if you ask for the optional **checkpoints** in the question block, the run pauses after round 1 (to see whether the voices are distinct) and before the debate (to adjust the agenda), and `/little-jury` continues it.
5. **You get the report.** `report.html` opens in your browser. The `.md` files next to it are the jury's full record, written for Claude to pick up in a later session.

The skill talks to you and writes everything in the language you use with Claude Code. English is the default.

**Revised versions.** Run `/little-jury` again after revising the project and the skill treats it as a re-evaluation: the same persona profiles and models (fresh instances that know nothing of the earlier run), the earlier problems checked against the new text, the changed sections checked for new problems of their own, and a report section showing each one as resolved, partly resolved or unresolved, plus the new problems the changes created.

## Requirements

- **Claude Code 2.1.271 or later**: the isolation relies on `blockReadsOutsideWorkingDirectories` (2.1.257) and on subagents with `omitClaudeMd` (2.1.271). Check with `claude --version`.
- **Python 3.9 or later**, available as `python` or `python3`.
- **The `claude` command on your `PATH`**: the skill starts the isolated session with `claude -p`.
- **Usage budget:** a lean jury makes roughly **50 to 70 agent calls** and can take from tens of minutes to a few hours. It may cross more than one usage window of your plan; if it stops at a limit, `/little-jury` resumes from where it stopped.

## Installation

The skill is a folder with a `SKILL.md` at its root. Claude Code loads personal skills from `~/.claude/skills/<skill-name>/` in every project, and project skills from `.claude/skills/<skill-name>/` in a single repository.

### Option 1: ask Claude Code to install it

Open Claude Code anywhere and send:

```text
Install the little-jury skill for me: clone https://github.com/HeitorTomaz/little-jury into my personal
skills folder, so that SKILL.md ends up at ~/.claude/skills/little-jury/SKILL.md. Then check that
/little-jury shows up; if it doesn't, run /reload-skills.
```

To install it only for one repository, ask for `.claude/skills/little-jury/` inside that repository instead.

### Option 2: install it manually

**macOS and Linux**

```bash
git clone https://github.com/HeitorTomaz/little-jury.git ~/.claude/skills/little-jury
```

**Windows (PowerShell)**

```powershell
git clone https://github.com/HeitorTomaz/little-jury.git "$env:USERPROFILE\.claude\skills\little-jury"
```

**Without git:** download the repository as a ZIP (Code > Download ZIP), extract it, and rename the folder to `little-jury` so that the path is `~/.claude/skills/little-jury/SKILL.md` (on Windows, `%USERPROFILE%\.claude\skills\little-jury\SKILL.md`).

**For a single repository:** clone into `.claude/skills/little-jury` at the root of that repository instead.

Claude Code picks up new skills during the session. If `/little-jury` does not appear in the `/` menu, run `/reload-skills`.

### Updating

```bash
git -C ~/.claude/skills/little-jury pull
```

On Windows: `git -C "$env:USERPROFILE\.claude\skills\little-jury" pull`.

## Usage

Open Claude Code **at the root of your project** and run `/little-jury`. There is one command; what you write after it is up to you:

| Example | What happens |
|---|---|
| `/little-jury` | evaluates the concept document (no code yet) or the existing system (there is code); the questions offer a general evaluation |
| `/little-jury I want to know whether first-time users get the scoring` | the same, aimed at what you want to find out |
| `/little-jury docs/my-change-plan.md` | evaluates the planned change described in that file, against the current system |

The skill looks at the folder before doing anything: with no `panel/`, it prepares one; with a panel that is assembled or unfinished (stopped at a limit or at a checkpoint), it runs or resumes it; with a finished run, it offers a re-evaluation of your revised version. Plain requests work too: "put this concept in front of a little jury", "continue the panel".

The skill creates two folders at the root of your project:

- `prep/`: the inputs it wrote, what it removed from them (`removed.md`) and the decisions it made for you (`decisions.md`);
- `panel/`: the isolated workspace, with the rounds and the report under `panel/rounds/v<version>/`.

Decide whether to commit them or add them to `.gitignore`; the skill asks during preparation.

**Before the run:** close any editor tabs with your concept, plan or code. The editor can share the open file with Claude Code sessions.

**Fewer confirmations:** preparation writes several files in `prep/` and `panel/`. In the default permission mode, Claude Code asks you to confirm each one; switch to auto-accept edits (Shift+Tab) before `/little-jury` to avoid that. The isolated run itself does not ask: its tools are allowed in advance.

**Ideas during the run:** write them in `prep/next-version-notes.md`, never in the panel's inputs. A run's inputs do not change while it runs; the notes feed the next version.

## Repository layout

```text
SKILL.md                       entry point read by Claude Code
references/                    preparation guides, persona composition, domain profiles
references/method/             the run method, copied into each panel/
scripts/                       assemble_panel.py, run_panel.py and the helpers used during the run
assets/panel-template/         agent definitions, the report template and its fonts
evals/                         test cases in the skill-creator / `claude plugin eval` format
```

## Testing the skill

The `evals/` folder holds test cases in the format that `claude plugin eval` reads. From the repository root, with Claude Code 2.1.269 or later:

```bash
claude plugin eval . --allow-tools Write,Edit,Bash --scaffold
```

These are real, billed model runs, and the `run-*` cases launch a full jury.

## License

The skill is released under the [MIT License](LICENSE). The fonts bundled with the report (Literata and Schibsted Grotesk) are under the SIL Open Font License; their license files are in `assets/panel-template/template/fonts/`.

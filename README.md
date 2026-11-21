# mock-jury

A [Claude Code](https://code.claude.com) skill that puts your project in front of a **mock jury**: a panel of synthetic personas (users, experts and two adversaries) that review it in isolated rounds and hand you an HTML report with the tensions, risks, gaps and what to test first.

It works on three kinds of project:

- **a concept** that is still on paper (a game, an app, a service, a business);
- **an existing system**, described from its code, docs and comments;
- **a planned change** to an existing system, described in a plan file.

The jury deliberates; **you decide**. The report never gives a verdict.

## What it is good at, and what it is not

**Good at:** contradictions between your own rules, dominant strategies and loopholes, gaps in the specification, audience splits (what attracts one profile and drives away another), the smallest test for your main hypothesis, quick wins (the smallest change that would solve each problem, and what it costs), sentences of your pitch that readers misunderstand, and checking external facts against their sources (store rules, platform docs). Trademark registries often cannot be checked automatically (interactive forms, CAPTCHAs); the report marks them [not verified].

**Not:** telling you whether people will actually like it, predicting market interest, or giving approval percentages. Simulated opinions are not research, and the report says so. That is also why the personas do not rate the project from 1 to 5: each one answers a few questions (would you want to know more, would it be worth it, would you try it) with **yes**, **no** or **only if…**, and the condition behind an "only if" is usually the most useful line in the report.

## How it works

1. **You ask once.** Run `/mock-jury prepare` at the root of your project. The skill reads your material and asks one block of questions: who the project is for, what you want to decide with the evaluation, what worries you, and anything the material does not answer.
2. **It writes neutral inputs.** It strips your arguments in favor of the idea, your comparisons with other products and the justifications in code comments, and records what it removed in `prep/removed.md` so you can check later.
3. **It runs the jury in isolation.** It assembles a `panel/` folder and starts a separate Claude Code session inside it. That session cannot read the rest of your project: reads outside the folder are blocked, the project's `CLAUDE.md` files and git history are kept out of its context, and the personas run as subagents with no tools at all.
4. **Five rounds:** first impression, detailed analysis, extreme scenarios, debate (with a consensus challenger) and consolidation. By default there are no stops; if you ask for the optional **checkpoints** in the question block, the run pauses after round 1 (to see whether the voices are distinct) and before the debate (to adjust the agenda), and `/mock-jury run` continues it.
5. **You get the report.** `report.html` opens in your browser. The `.md` files next to it are the jury's full record, written for Claude to pick up in a later session.

The skill talks to you and writes everything in the language you use with Claude Code. English is the default.

**Revised versions.** Run `/mock-jury prepare` again after revising the project and the skill treats it as a re-evaluation: the same persona profiles and models (fresh instances that know nothing of the earlier run), the earlier problems checked against the new text, the changed sections checked for new problems of their own, and a report section showing each one as resolved, partly resolved or unresolved, plus the new problems the changes created.

## Requirements

- **Claude Code 2.1.271 or later**: the isolation relies on `blockReadsOutsideWorkingDirectories` (2.1.257) and on subagents with `omitClaudeMd` (2.1.271). Check with `claude --version`.
- **Python 3.9 or later**, available as `python` or `python3`.
- **The `claude` command on your `PATH`**: the skill starts the isolated session with `claude -p`.
- **Usage budget:** a lean jury makes roughly **50 to 70 agent calls** and can take from tens of minutes to a few hours. It may cross more than one usage window of your plan; if it stops at a limit, `/mock-jury run` resumes from where it stopped.

## Installation

The skill is a folder with a `SKILL.md` at its root. Claude Code loads personal skills from `~/.claude/skills/<skill-name>/` in every project, and project skills from `.claude/skills/<skill-name>/` in a single repository.

### Option 1: ask Claude Code to install it

Open Claude Code anywhere and send:

```text
Install the mock-jury skill for me: clone https://github.com/HeitorTomaz/mock-jury into my personal
skills folder, so that SKILL.md ends up at ~/.claude/skills/mock-jury/SKILL.md. Then check that
/mock-jury shows up; if it doesn't, run /reload-skills.
```

To install it only for one repository, ask for `.claude/skills/mock-jury/` inside that repository instead.

### Option 2: install it manually

**macOS and Linux**

```bash
git clone https://github.com/HeitorTomaz/mock-jury.git ~/.claude/skills/mock-jury
```

**Windows (PowerShell)**

```powershell
git clone https://github.com/HeitorTomaz/mock-jury.git "$env:USERPROFILE\.claude\skills\mock-jury"
```

**Without git:** download the repository as a ZIP (Code > Download ZIP), extract it, and rename the folder to `mock-jury` so that the path is `~/.claude/skills/mock-jury/SKILL.md` (on Windows, `%USERPROFILE%\.claude\skills\mock-jury\SKILL.md`).

**For a single repository:** clone into `.claude/skills/mock-jury` at the root of that repository instead.

Claude Code picks up new skills during the session. If `/mock-jury` does not appear in the `/` menu, run `/reload-skills`.

### Updating

```bash
git -C ~/.claude/skills/mock-jury pull
```

On Windows: `git -C "$env:USERPROFILE\.claude\skills\mock-jury" pull`.

## Usage

Open Claude Code **at the root of your project** and run one of:

| Command | What it evaluates |
|---|---|
| `/mock-jury prepare` | the concept document (no code yet) or the existing system (there is code) |
| `/mock-jury prepare docs/my-change-plan.md` | the planned change described in that file, against the current system |
| `/mock-jury run` | runs or resumes the jury for a `panel/` that is already assembled |

Plain requests work too: "put this concept in front of a mock jury", "run the panel".

The skill creates two folders at the root of your project:

- `prep/`: the inputs it wrote, what it removed from them (`removed.md`) and the decisions it made for you (`decisions.md`);
- `panel/`: the isolated workspace, with the rounds and the report under `panel/rounds/v<version>/`.

Decide whether to commit them or add them to `.gitignore`; the skill asks during preparation.

**Before the run:** close any editor tabs with your concept, plan or code. The editor can share the open file with Claude Code sessions.

**Fewer confirmations:** preparation writes several files in `prep/` and `panel/`. In the default permission mode, Claude Code asks you to confirm each one; switch to auto-accept edits (Shift+Tab) before `/mock-jury prepare` to avoid that. The isolated run itself does not ask: its tools are allowed in advance.

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

# Running the panel — orchestrator instructions

You are the main Claude Code session, opened inside `panel/`. You act as the **orchestrator** (you build prompts, create agents, save files) and as the **moderator** (you write scenarios, run the debate, consolidate). You do not give opinions on the project.

**Language.** Read `- Language:` in `config.md`. Write every persona prompt, every round file, every output and the report data and labels in that language. These method files stay in English; what you produce does not.

Method files, in this folder:

| File | Content |
|---|---|
| `method/run.md` | this file: isolation, checks, record keeping, running without stops, resuming |
| `method/rounds.md` | the five rounds, questions and prompt format |
| `method/rounds-change.md` | questions for the change type (they replace those in `rounds.md`) |
| `method/outputs.md` | final files and the visual report |
| `method/diversity.md` | how to evaluate the panel itself |
| `method/scripts/` | isolation check, list draw, ranking analysis, report build and validation, statistics |

Read `config.md` first: the `Type` field (concept, system or change) tells you which questions to use, and `Language` tells you which language to write in. Then read the method files (`rounds-change.md` only for the change type) and `personas.md`.

## 1. Where you are and what you must not do

The folder above this one holds the concept document or the system's code, the change plan and the preparation notes. All of that is **out of the panel's reach**: what the author wrote to defend the idea, the comments in the code and the decision history would contaminate the evaluations.

- Do not read, list or search anything outside `panel/`, with any tool, including terminal commands.
- Do not run `git` commands: the repository and its history are above this folder.
- If a read is refused, do not try another path and do not ask to add directories to the session.
- If `.claude/settings.json` or `method/` is missing from the working directory, stop and explain before doing anything else. If the folder is not called `panel`, say so but continue: what proves isolation is the read-block test in section 3.
- Do not install or configure anything.
- Do not read the reference files in the skill's folder; use the copies in `method/`.

## 2. The four isolation layers

1. **Folder.** The session was opened in `panel/`; by default Claude Code accesses the directory it was started in.
2. **Settings.** `.claude/settings.json` contains `"blockReadsOutsideWorkingDirectories": true` (requires Claude Code 2.1.257 or later), `claudeMdExcludes` with the instruction files of the folders above, `"includeGitInstructions": false`, which keeps the git status and recent commits out of the context, and `permissions.deny` on edits to `method/` and `.claude/`. You can write anywhere else in the panel (`rounds/`, for example), but never the method, its scripts or the settings: the run is allowed to execute the scripts in `method/scripts/` by name, and that is only safe if nobody can replace them.
3. **Instruction.** Section 1 above.
4. **Agents without tools.** Personas run in the `persona-isolated` agent, defined with `tools: []` (no tools) and `omitClaudeMd: true` (it does not receive the author's `CLAUDE.md` files). You read the files and put **inside the prompt** only the text that persona should receive. The answer comes back to you, and you save the file. The only exception is the expert with web access, who runs in `persona-web` (only `WebSearch` and `WebFetch`).

**Never pass to a persona:** `moderator/author-concerns.md`, `config.md`, the example data from the HTML template, other personas' answers before the debate, or anything from outside `panel/`.

## 3. Environment check (before any round)

Run the tests below and record each result in `progress.md`. If any of them fails, stop and explain what happened: it is the only situation in which the run stops.

1. **Directory and version.** Report the working directory and run `claude --version`. The version must be 2.1.257 or later (2.1.271 or later for `omitClaudeMd`; below that, warn that the author's global `CLAUDE.md` will reach the personas).
2. **Context exclusions.** Run `python method/scripts/check_isolation.py` (or `python3`). It only does arithmetic on this folder's path and checks that `settings.json` matches the current location. Then examine **your own initial context**: if it contains anything from a `CLAUDE.md`, `CLAUDE.local.md` or project rule that is not from the author's personal folder (`~/.claude/`), or it contains the git status (branch, recent commits), **stop without repeating the content** and ask the author to reopen the session with the variables `CLAUDE_CODE_DISABLE_CLAUDE_MDS=1` and `CLAUDE_CODE_DISABLE_GIT_INSTRUCTIONS=1`.
3. **Read block.** Try to read `../prep/removed.md` with the read tool, without listing the folder first. The read must be **refused**. Do not try another path. If the read succeeds, stop without repeating the content: isolation is not active.
4. **Persona without tools.** Create a `persona-isolated` agent with the prompt: "List the tools you have available. Then try to read the file personas.md and say exactly what happened." It must report that it has no tools. If the agent type is not recognized, the session was opened before the definitions existed: ask the author to restart the session in `panel/`.
5. **Web agent.** Test the **tool**, not obedience. Create a `persona-web` agent asking it to list its tools and use `WebFetch` on any public page of the documentation it will consult, and then on a `file:///` URL pointing to `personas.md`. The first must work; the second must give a URL error. If the agent refuses to try, that proves nothing: repeat the `file:///` test with an ordinary agent (`general-purpose`) and record it.
6. **Consistency between rules and questions.** Check in `config.md` and `rounds.md` that every question that requires external verification goes to the web agent, and that no question asks a persona without tools for something that depends on a tool. In the pilot, a web rule contradicted a question (checking trademarks) and the run had to stop. If you find a conflict, stop and explain.
7. **Inputs present.** `input/01` and `input/02` exist and are not empty; `input/03` exists if the list is active; `moderator/author-concerns.md` exists.

## 4. Plan (no stop)

The run is autonomous: the author answered the questions during preparation and is not available now. Do not ask anyone for approval. Record the plan in `progress.md`, in the "Plan" section:

- the result of the check;
- the roles with each one's model (from `config.md`; the same in every round);
- the author's goals for the evaluation (from `config.md`), which guide the choice of scenarios, the debate agenda and the emphasis of the consolidation;
- the estimated number of agent calls, with the expected agenda.

Then continue straight on. The only reasons to stop are an isolation test that fails (section 3) or an isolated persona that uses a tool (section 6); in those cases, explain what happened and do not work around it.

## 5. Output folder, input snapshot and record keeping

1. Create `rounds/v<version>/` (version from `config.md`; if the folder already exists with a **completed** run, use `v<version>-2`; if it exists with an **incomplete** run, this is a resume: go to section 8).
2. Copy to `rounds/v<version>/inputs-used/` the files in `input/`, `personas.md`, `config.md` and `method/VERSION.txt`. It is the snapshot of what this run received. **Do not change the inputs during the run** (a lesson from the pilot).
3. Create `rounds/v<version>/progress.md` in the format below. Update "Status" and "Next step" **before** launching each group of calls, and the call log **as soon as** each answer arrives. If the session drops (because of a usage limit, for example), `progress.md` must say exactly what has already been done.
4. Save **the full text** of each prompt, exactly as sent, in `rounds/v<version>/prompts/<round>-<id>.md`, before launching the call. Do not save templates with "variable parts": resuming and auditing isolation depend on the exact text.

### `progress.md` format

```markdown
# Panel progress v<version>

## Status
- Environment check: completed on <date> (results below)
- Round 1: completed | in progress (launched: <ids>; saved: <ids>) | pending
- Round 2: ...
- Round 3: ...
- Contrarian: ...
- Debate agenda: ...
- Round 4: ... (per point and turn)
- Round 5: ...
- Next step: <exact sentence saying what to do next>

## Plan

## Moderator notes
<!-- after round 1: uniform scores? repeated objections? distinct voices? -->
<!-- before the debate: the chosen agenda and why -->

## Environment check
| test | result |

## Draws
| list | seed | file |

## Call log
| # | round | persona | model | agent type | tool uses | output file | prompt |
```

## 6. How to create each agent

- Use the `persona-isolated` agent type and pass the persona's **model** in the call's `model` parameter, as set in `config.md`.
- The expert with web access uses `persona-web` **only in round 2**, which is where the external-verification questions are. In round 3 and in the debate it runs as `persona-isolated`, with the same model: there the questions are about what is written. Record the agent type of every call.
- Launch all independent calls of a round **in the same message**, so they run in parallel. They are isolated from each other, so order does not matter.
- The prompt follows the skeleton in `rounds.md`: general persona rules, the persona, the round material, the questions and the answer format.
- Save the answer **unedited** in `rounds/v<version>/<round>-<id>.md`, with a three-line header: persona, model, date. If the answer is cut off or out of format, record it and repeat the call once with the same prompt; do not fix the text.
- Record in the log the tool uses reported by the agent's notification. An isolated persona with more than zero tool uses is an alarm: stop and investigate.

## 7. Commands and tools

- Run the scripts in `method/scripts/` through the **Bash** tool, always in the form `python method/scripts/<script>.py ...` (or `python3`). That is the form allowed in a run without the author; other forms, or another terminal tool, ask for approval that nobody will give.
- Do not use other terminal commands, do not open a browser and do not install anything. The report is validated by `report.py`; the session that launched the run is the one that opens the page.
- Word counts and other statistics that `diversity.md` needs: `python method/scripts/stats.py rounds/v<version>`.

## 8. Resuming

If `rounds/v<version>/progress.md` already exists without round 5 completed:

1. Repeat tests 1, 2 and 3 of the check (Claude Code version, context exclusions and read block): this is a new session. Record the version; if it changed since the run started, note it as a limit in `diversity.md`.
2. Do not rely on "Next step" alone: list the saved files and compare them with the call log. A call that was launched but has no output file is redone with the prompt saved in `prompts/`, unchanged. A saved answer missing from the log is added to it, with tool uses "not recorded".
3. Facts about the run itself that you put into summaries already sent (for example, "there was no interruption") and that stopped being true: correct them in the next summary and record it in `diversity.md`.
4. Do not redo completed rounds. Record the resume in `progress.md`, with the date and what was redone.

## 9. Limits

1. Do not invent what is not in the description. Gaps go to `gaps`.
2. Avoid polite positive answers and artificial agreement, including in your own syntheses.
3. Distinguish observation, hypothesis and proven problem.
4. Do not treat synthetic answers as research. Do not compute approval percentages or predict commercial success. Counts (how many of 8 mentioned something) are allowed as a description of the panel, never as an estimate of an audience.
5. Preserve minority positions: record who disagreed.
6. Keep every round file, for comparison with future versions of the concept.
7. Evaluations in `input/external/` (other than `README.md`) enter from the debate onwards, identified as external.

# Running the panel — orchestrator instructions

You are the main Claude Code session, opened inside `panel/`. You act as the **orchestrator** (you build prompts, create agents, save files) and as the **moderator** (you write scenarios, run the debate, consolidate). You do not give opinions on the project.

**Language.** Read `- Language:` in `config.md`. Write every persona prompt, every round file, every output and the report data and labels in that language. These method files stay in English; what you produce does not.

Method files, in this folder:

| File | Content |
|---|---|
| `method/run.md` | this file: isolation, checks, record keeping, running without stops, optional checkpoints, resuming |
| `method/rounds.md` | the five rounds, questions and prompt format |
| `method/rounds-change.md` | questions for the change type (they replace those in `rounds.md`) |
| `method/rounds-criteria.md` | rounds for the criteria family: a bench of jurors judges a work against criteria (they replace the questions and the round 3 material of `rounds.md`) |
| `method/outputs.md` | final files and the visual report |
| `method/diversity.md` | how to evaluate the panel itself |
| `method/scripts/` | isolation check, list draw, ranking analysis, report build and validation, statistics |

Read `config.md` first: the `Type` field (concept, system, change or work) and the `Family` field (audience, the default, or criteria) tell you which questions to use, and `Language` tells you which language to write in. Then read the method files (`rounds-change.md` only for the change type, `rounds-criteria.md` only for the criteria family) and `personas.md`.

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
2. **Settings.** `.claude/settings.json` contains `"blockReadsOutsideWorkingDirectories": true` (requires Claude Code 2.1.257 or later), `claudeMdExcludes` with the instruction files of the folders above, `"includeGitInstructions": false`, which keeps the git status and recent commits out of the context, and `permissions.deny` on edits to `method/` and `.claude/`. You can write anywhere else in the panel (`rounds/`, for example), but never the method, its scripts or the settings: the run is allowed to execute the scripts in `method/scripts/` by name, and that is only safe if nobody can replace them. The scripts also refuse any path outside the panel and any output inside `method/` or `.claude/`, and `run_panel.py` marks those two folders read-only for the whole run and checks their hashes at the end.
3. **Instruction.** Section 1 above.
4. **Agents without tools.** Personas run in the `persona-isolated` agent, defined with `tools: []` (no tools) and `omitClaudeMd: true` (it does not receive the author's `CLAUDE.md` files). You read the files and put **inside the prompt** only the text that persona should receive. The answer comes back to you, and you append it to the round file. The only exception is the expert with web access, who runs in `persona-web` (only `WebSearch` and `WebFetch`).

**Never pass to a persona:** `moderator/author-concerns.md`, `config.md`, the example data from the HTML template, other personas' answers before the debate, or anything from outside `panel/`.

## 3. Environment check (before any round)

Run the tests below and record each result in `progress.md`. If any of them fails, stop and explain what happened: it is the only situation in which the run stops.

1. **Directory and version.** Report the working directory and run `claude --version`. The version must be 2.1.257 or later (2.1.271 or later for `omitClaudeMd`; below that, warn that the author's global `CLAUDE.md` will reach the personas).
2. **Context exclusions.** Run `python method/scripts/check_isolation.py` (or `python3`). It only does arithmetic on this folder's path and checks that `settings.json` matches the current location. Then examine **your own initial context**: if it contains anything from a `CLAUDE.md`, `CLAUDE.local.md` or project rule that is not from the author's personal folder (`~/.claude/`), or it contains the git status (branch, recent commits), **stop without repeating the content** and ask the author to reopen the session with the variables `CLAUDE_CODE_DISABLE_CLAUDE_MDS=1` and `CLAUDE_CODE_DISABLE_GIT_INSTRUCTIONS=1`.
3. **Read block.** Try to read `../prep/removed.md` with the read tool, without listing the folder first. The read must be **refused**. Do not try another path. If the read succeeds, stop without repeating the content: isolation is not active.
4. **Persona without tools.** Create a `persona-isolated` agent with the prompt: "List the tools you have available. Then try to read the file personas.md and say exactly what happened." It must report that it has no tools. If the agent type is not recognized, the session was opened before the definitions existed: ask the author to restart the session in `panel/`.
5. **Web agent.** Test the **tool**, not obedience. Create a `persona-web` agent asking it to list its tools and use `WebFetch` on any public page of the documentation it will consult, and then on a `file:///` URL pointing to `personas.md`. The first must work; the second must **not return the file's content**. Any of these passes: a URL error, a refusal by the tool, or a permission request that is denied (Claude Code 2.1.330 answers with a permission request instead of an error, and the headless run denies it). It fails only if the content of `personas.md` comes back. Record the exact outcome. If the agent refuses to try, that proves nothing: repeat the `file:///` test with an ordinary agent (`general-purpose`) and record it.
6. **Consistency between rules, questions and persona texts.** Check in `config.md` and `rounds.md` that every question that requires external verification goes to the web agent, and that no question asks a persona without tools for something that depends on a tool. In the pilot, a web rule contradicted a question (checking trademarks) and the run had to stop. Also compare **each persona's text** in `personas.md` with the tools it gets in each round: a persona text must never promise a tool. If one does ("checks the official documentation" for a persona that runs without web), plan the prompt note of section 6 for every round where the tool is missing and record it here. If you find a conflict you cannot cover that way, stop and explain.
7. **Inputs present.** `input/01` and `input/02` exist and are not empty (for the work type, `input/02-work.md` or `input/02-work-*.md`; `input/04-summary-of-the-rest.md` if `config.md` gives a partial scope); `input/03-list.md` exists if the list is active; for the criteria family, the criteria table is in `config.md` and `input/03-criteria.md` exists when the criteria were given by the author; `moderator/author-concerns.md` exists.

## 4. Plan (no stop)

The run is autonomous: the author answered the questions during preparation and is not available now. Do not ask anyone for approval. Record the plan in `progress.md`, in the "Plan" section:

- the result of the check;
- the type and the family (`- Type:` and `- Family:` in `config.md`), and which rounds file you follow;
- the roles with each one's model (from `config.md`; the same in every round);
- the author's goals for the evaluation (from `config.md`), which guide the choice of scenarios, the debate agenda and the emphasis of the consolidation;
- the estimated number of agent calls, with the expected agenda;
- whether the audience is defined (`## Audience` in `config.md`; see section 10, rule 8);
- the checkpoints asked for in `config.md` (`- Checkpoints:`), if any (section 8);
- whether this is a re-evaluation (`- Re-evaluation of:` in `config.md`; see "Re-evaluation" in `rounds.md`).

Then continue straight on. The only reasons to stop are an isolation test that fails (section 3) or an isolated persona that uses a tool (section 6), in which case you explain what happened and do not work around it, and a checkpoint the author asked for (section 8).

## 5. Output folder, input snapshot and record keeping

1. Create `rounds/v<version>/` (version from `config.md`; if the folder already exists with a **completed** run, use `v<version>-2`; if it exists with an **incomplete** run, this is a resume: go to section 9).
2. Copy to `rounds/v<version>/inputs-used/` the files in `input/`, `personas.md`, `config.md` and `method/VERSION.txt`. It is the snapshot of what this run received. **Do not change the inputs during the run** (a lesson from the pilot): a decision or a new idea that comes up while the panel runs is recorded and handled afterwards, in `prep/next-version-notes.md` (see the final message in `rounds.md`), never by editing the files already used.
3. Create `rounds/v<version>/progress.md` in the format below. Update "Status" and "Next step" **before** launching each group of calls, and the call log **as soon as** each answer arrives. If the session drops (because of a usage limit, for example), `progress.md` must say exactly what has already been done.
4. Save each prompt **before** launching the call, one file per call: `rounds/v<version>/prompts/<round>-<id>.md` (rounds 1 to 3), `prompts/r4-contrarian-1.md` and `prompts/r4-contrarian-2.md` (the contrarian's two calls), `prompts/r4-<point>-<id>-turn<n>.md` (debate replies). Text that several calls share (the general rules, the full description, a summary, the contrarian pack) is saved **once**, and the call file points to it with a line of its own: `include: <path>`, where the path is a file of `rounds/v<version>/`, either in `inputs-used/` or in `prompts/shared/` (for example `prompts/shared/r2-general-rules.md`). The rule that makes this exact: **the text sent is the call file with each `include:` line replaced by the whole content of that file, in order, and nothing else changed.** Resuming rebuilds it the same way. Do not save templates with "variable parts" or summaries of what was sent, and never shorten a shared block to save room (in a real run, saving every prompt in full with a long description repeated dozens of times led the moderator to cut the contrarian's pack and to launch calls in batches; shared blocks remove that pressure).
5. **One file per round**, with one section per persona: `r1.md`, `r2.md`, `r3.md` and, in round 4, `r4-debate-replies.md` (the full list is in `outputs.md`). The pilot produced about 50 separate files, which were hard to read and to attach. Each section starts with a `## <id>` heading (in the debate, `## <point> — <id> — turn <n>`) followed by two lines, `- Model: <model> (<agent type>)` and `- Date: <date>`, and then the answer, unedited. Append each section **as soon as** its answer arrives.

### `progress.md` format

```markdown
# Panel progress v<version>

## Status
- Environment check: completed on <date> (results below)
- Round 1: completed | in progress (launched: <ids>; saved: <ids>) | pending
- Round 2: ...
- Round 3: ...
- Contrarian: ... (call 1 / requests / call 2)
- Debate agenda: ...
- Round 4: ... (per point and turn)
- Round 5: ...
- Next step: <exact sentence saying what to do next>
- Paused: checkpoint <1|2> (<after round 1 | before the debate>)   <- only while paused at a checkpoint

## Plan

## Moderator notes
<!-- after round 1: uniform stances (and conditions)? repeated objections? distinct voices? the comprehension check -->
<!-- round 2: the roles, modes or paths assigned to each user in the "first 15 minutes" question, if the project has them -->
<!-- round 3: scenarios rewritten because they described the action or the outcome -->
<!-- before the debate: the chosen agenda, the settled items sent straight to consolidation, and why -->
<!-- at each checkpoint: when the run paused and resumed, and whether the author edited the agenda -->

## Environment check
| test | result |

## Draws
| list | seed | file |

## Call log
| # | round | persona | model | agent type | tool uses | output file and section | prompt |
```

## 6. How to create each agent

- Use the `persona-isolated` agent type and pass the persona's **model** in the call's `model` parameter, as set in `config.md`.
- The expert with web access uses `persona-web` **only in round 2**, which is where the external-verification questions are. In round 3 and in the debate it runs as `persona-isolated`, with the same model: there the questions are about what is written. Record the agent type of every call.
- **Persona text vs tools.** Whenever a persona runs without a tool that its text mentions (the web expert in rounds 3 and 4, or any persona whose text you flagged in test 6), say so explicitly in the prompt, right after the persona block: "In this round you have no web access. Do not claim to have checked anything; mark **[not verified]** every external fact you rely on." In a real run, the publishing expert ran without web while its text said it checked the official documentation; the prompt note covered the gap.
- **Always a new agent.** Never resume or continue an agent from an earlier round or turn (do not send it a message): create a new one and put in the prompt the verbatim excerpt of that persona's own earlier answer when the round needs it. This includes the debate's second turn and the contrarian's second call. In a real run, some personas continued their own agent and others got a new one, so they read the same reply with different context.
- Launch all independent calls of a round **in the same message**, so they run in parallel. They are isolated from each other, so order does not matter.
- The prompt follows the skeleton in `rounds.md`: general persona rules, the persona, the round material, the questions and the answer format.
- Append the answer **unedited** to the round file, in its own section (section 5, item 5). If the answer is cut off or out of format, record it and repeat the call once with the same prompt; do not fix the text: replace the section with the new answer and note the repetition in the log.
- Record in the log the tool uses reported by the agent's notification. An isolated persona with more than zero tool uses is an alarm: stop and investigate.

## 7. Commands and tools

- Run the scripts in `method/scripts/` through the **Bash** tool, always in the form `python method/scripts/<script>.py ...` (or `python3`). That is the form allowed in a run without the author; other forms, or another terminal tool, ask for approval that nobody will give.
- Do not use other terminal commands, do not open a browser and do not install anything. The report is validated by `report.py`; the session that launched the run is the one that opens the page.
- Word counts and other statistics that `diversity.md` needs: `python method/scripts/stats.py rounds/v<version>`. It reads the sections of `r1.md`, `r2.md`, `r3.md` and `r4-debate-replies.md`.

## 8. Checkpoints (optional)

They are off by default. When `config.md` says `- Checkpoints: after round 1, before the debate`, pause twice:

1. **After round 1**, once `r1.md`, the moderator notes and the comprehension check are written: is it worth going on with these voices?
2. **Before the debate**, once `r4-agenda.md` is written: the author may adjust the agenda.

To pause: make sure every file of the step is written and `progress.md` is up to date, add the line `- Paused: checkpoint <1|2> (<after round 1 | before the debate>)` under "Status", and end with a short message, in the language of `config.md`: what to look at (`rounds/v<version>/r1.md` at checkpoint 1; `rounds/v<version>/r4-agenda.md` at checkpoint 2, which the author may edit) and how to continue (`/mock-jury` at the project root). Do not ask questions and do not wait: the session ends there, and `run_panel.py` reports the pause.

On resume (section 9), remove the `- Paused:` line, record in "Moderator notes" when the run resumed and, at checkpoint 2, whether the author edited `r4-agenda.md`. If they did, use the edited agenda as it is, and note in `diversity.md` that the agenda was adjusted by the author.

These two moments are where pauses paid off in real runs: after round 1, to see whether the voices were distinct, and before the debate, to adjust the agenda.

## 9. Resuming

If `rounds/v<version>/progress.md` already exists without round 5 completed:

1. Repeat tests 1, 2 and 3 of the check (Claude Code version, context exclusions and read block): this is a new session. Record the version; if it changed since the run started, note it as a limit in `diversity.md`. If `progress.md` has a `- Paused:` line, this is the continuation after a checkpoint: follow section 8.
2. Do not rely on "Next step" alone: compare the sections present in the round files (`r1.md`, `r2.md`, `r3.md`, `r4-contrarian.md`, `r4-debate-replies.md`) with the call log. A call that was launched but has no section is redone with the prompt saved in `prompts/`, unchanged, with its `include:` lines expanded as section 5 says. A section missing from the log is added to it, with tool uses "not recorded".
3. Facts about the run itself that you put into summaries already sent (for example, "there was no interruption") and that stopped being true: correct them in the next summary and record it in `diversity.md`.
4. Do not redo completed rounds. Record the resume in `progress.md`, with the date and what was redone.

## 10. Limits

1. Do not invent what is not in the description. Gaps go to `gaps`.
2. Avoid polite positive answers and artificial agreement, including in your own syntheses.
3. Distinguish observation, hypothesis and proven problem.
4. Do not treat synthetic answers as research. Do not compute approval percentages or predict commercial success. Counts (how many of 8 mentioned something) are allowed as a description of the panel, never as an estimate of an audience.
5. Preserve minority positions: record who disagreed. The destroyer and the contrarian attack by role, so they never count in a convergence, consensus or "N of M agree"; same-model duplicates count as one piece of evidence; only independent positions count as separate agreements: a change after someone's argument, with a quoted passage, is one confirmation of that argument's origin, and a change with no quote is persuasion and does not count (`rounds.md`, round 4).
6. Keep every round file, for comparison with future versions of the concept.
7. Evaluations in `input/external/` (other than `README.md`) enter from the debate onwards, identified as external.
8. **Undefined audience.** When `config.md` says `- Defined: no` under `## Audience`, do not tally or summarize together profiles that want opposite things, in the syntheses or in the stances. Record what each group wants and what choosing each audience would cost (the `audienceSplit` section of the report).
9. **Never recommend running the panel again.** Whether to run another panel is the author's decision, not a recommendation of this one.

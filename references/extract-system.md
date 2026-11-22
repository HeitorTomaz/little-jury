# Extracting the existing system

For the **system** and **change** types. The preparation session is at the repository root and can read everything. The job is to turn code, documentation and comments into a description of **what the system does**, in the language of the people who use it, without the justifications of the people who built it. The panel never sees the code: it sees this description, so the quality of the evaluation depends on it. Write the description in the language recorded in `config.md`.

## Contents

1. Defining the scope
2. Sweeping the sources
3. What goes in and what stays out
4. Markers and references
5. Current users
6. Check before the run

---

## 1. Defining the scope

- **System:** ask the author whether the panel evaluates the whole system or one area (a module, a flow, a type of user). Large systems described in full produce a description no persona can judge; prefer the areas the author wants to discuss. If the full description is likely to exceed about **5,000 words** (not counting the `[ref: …]` references), include in the interview's question block how it would split into areas and ask whether the author wants to evaluate one at a time. That is why the light survey (section 2) comes before the questions.
- **Evaluating the panel skill itself** (or any other system whose code ends up inside `panel/`): the method copied to `panel/method/` is the very system being evaluated, with the justifications you removed. The personas do not receive it, but the moderator does. Tell the author and record it in `config.md`, so it goes in as a limit in `diversity.md`.
- **Change:** the scope is the part the plan alters **plus its neighborhood**: what calls it, what it calls, what reads or writes the same data, or what appears on the same screen as what changes. List the areas you intend to extract and include them in the question block.
- Record the source: commit (`git rev-parse --short HEAD`), branch and whether there are uncommitted changes. This goes into `config.md` and makes it possible to know, later, which version of the code the panel gave its opinion on.

## 2. Sweeping the sources

The sweep has two stages.

1. **Light survey, before the questions:** the folder tree, the README and the index of the documentation, the size of each area (files, lines) and the entry points (routes, screens, commands). No reading of the code itself. It is enough to propose the scope and the split into areas in the question block.
2. **Full extraction, after the answers:** only in the scope the author chose, as below.

For the full extraction, use read-only subagents (`Explore` type) in parallel, one per area or per type of source, asking each for a list of **behaviors with file and line references**, not a summary of the code. At this stage there is no isolation to protect: preparation subagents may read the whole repository.

| Source | What to extract |
|---|---|
| README, `docs/`, in-repo wiki, manuals | what the system promises to do, for whom, how it is used |
| `CLAUDE.md`, `AGENTS.md`, contribution guides | conventions and constraints that affect behavior (not style preferences) |
| Decision records (ADRs, RFCs) | the decision and what it fixes; **not** the reasoning that defends it |
| Routes, screens, commands, public APIs | what the user can do, and through what |
| Data models, schemas, migrations | what the system stores and the rules about that data (required, limits, uniqueness) |
| Permissions, roles, authentication | who can do what |
| Business rules in the code (validations, calculations, states, deadlines) | the real rules, with the numbers |
| Configuration and environment variables | adjustable limits and behaviors, with current values |
| Tests | behaviors the author considers guaranteed (a test is a written rule) |
| `TODO`, `FIXME`, `HACK`, `XXX` comments | known gaps and problems |
| External integrations | which services the system depends on and what happens if they fail, when the code says |

Do not use the git history (commit messages, PR descriptions) as a source of behavior: it is where justifications and intentions that never reached the code pile up the most.

## 3. What goes in and what stays out

**Goes in:** observable behavior and rules, described as the user or operator experiences them ("a cancelled order cannot be reopened; the system shows message X").

**Stays out, and goes into `prep/removed.md` with the passage and the reason:**

- justifications in comments and documents ("we did it this way because it is the most robust", "this approach is the best on the market");
- comparisons with other products made by the team;
- names of people and customers, and personal data;
- secrets, keys, internal addresses (never copy them, not even into `removed.md`; only record that they existed);
- implementation details with no effect on users (class names, libraries), **unless** they matter to the evaluation: technology that limits platforms, a dependency that has a cost, performance the user notices.

**Known gaps** (`TODO`, `FIXME`, empty functions, screens with no flow) go in as **[undefined]**, with the reference.

## 4. Markers and references

In the full description for the system and change types, each item carries one marker and, when it comes from the repository, a short reference:

| Marker | When to use |
|---|---|
| **[implemented]** | the behavior is in the code; you found it and understood it |
| **[documented]** | it is in the documentation and you did not confirm it in the code (you did not find it, or it was unclear) |
| **[divergent]** | the documentation says one thing and the code does another; describe both sides, each with its reference |
| **[undefined]** | the system does not decide (gap, `TODO`, unhandled case) |
| **[decided]** | an author decision about the system that is neither in the code nor in the documentation (e.g. "for now, only this platform") |
| **[fact]** | the author's or team's situation (team size, deadlines, contracts) |

What the system **claims about an external platform or service** (required versions, how an API behaves) is **[documented]**: the system says it, but nobody checked it at the source. If there is an expert with web access, include those claims in what they check.

Reference: `[ref: path/to/file.ext:line]`, or several separated by commas. Use paths relative to the repository root. Open the description's "How to read" block with these markers and with the sentence: "The `[ref: …]` references show where the information was extracted from; you do not have access to these files and do not need them to answer."

A **divergence** is prime material for the panel: documentation and code are two written rules that contradict each other, which is enough to classify it as a proven problem. But do not decide which side is right; that belongs to the author.

## 5. Current users

User profiles come from the system itself, in addition to what the author says:

- roles and permissions in the code;
- audiences the documentation names;
- different flows for different kinds of people (admin and customer, buyer and seller);
- usage data the author has, if they want to share it (no personal data).

Write the personas with the same structure as `composition.md`, saying under "Usually uses" **how each one uses this system today**. Include **one or two who do not use** the system: someone who might start using it, or someone who gave up. If the system has no users besides the author, see the end of section 4 of `prepare.md`.

## 6. Check before the run

- Every item in the description has a marker; every **[implemented]**, **[documented]** or **[divergent]** item has a reference.
- No code excerpt, no copied comment, no secret and no person's name in the description.
- The short pitch has no references and no technical jargon the user would not see.
- `removed.md` lists the justifications and comparisons removed, with references.
- Re-read three **[implemented]** rules chosen at random against the code: if any is wrong, the extraction is not ready.

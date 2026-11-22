# Panel composition

How to choose the roles, write the personas and distribute the models. It applies to any field; ready field profiles are in `domains/` (games, software, scientific papers, books, theses, exams), and for any other field you build one from these rules with the same header (families, what round 3 tests, users label). Write the personas in the language recorded in `config.md`.

## Sizes

| | Users | Experts | Adversaries | Moderator | Agent calls (estimate) |
|---|---|---|---|---|---|
| **Lean** (default) | 8 | 4 | 2 | 1 (the main session) | 50 to 70, up to 80 with a long debate |
| **Full** | 11 | 5 | 2 | 1 | 60 to 90, up to 100 with a long debate |
| **Lean, criteria family** | 6 jurors | 3 or 4 | 2 | 1 | 35 to 55 |

The estimate adds up the isolation tests (2 to 3), round 1 (one per user), round 2 (users + experts + destroyer), round 3 (experts + 2 users), the contrarian (2) and the debate replies, which are the part that varies most: 3 to 5 points, with 3 to 5 participants each, in one or two turns (9 to 50 calls). Second turns are common, because a point with two or more different smallest changes always gets one. When presenting the plan, do the math with the expected agenda. The criteria family is cheaper: six jurors answer in round 1 only (round 2 is experts and destroyer), and its debate points are the criteria where the bench split. The lean pilot made about 50 to 55 calls and spanned more than one usage window of the plan; `progress.md` makes it possible to resume.

## Users

### Structure of each persona

```markdown
### <id> — <Role name>

- **Perspective:** <what they value, in one sentence>
- **Relation to the project:** <uses | would be affected | would only be contacted>, with one sentence on how
- **Usually uses:** <concrete products or practices in the domain, without brands the author cited as comparisons>
- **Tolerance for complexity:** <low | medium | high | very high>, with one sentence on how they learn
- **Time:** <how much and when>
- **Looks for:** <what would make them stay>
- **Quits when:** <what would make them give up>
```

Most users **use** the project. When the audience includes people who would only be affected by it or contacted through it (a relative who gets reminders, a client who receives the reports), say so in **Relation**: the run tells those personas that a question that does not fit them is answered "does not apply", with the reason.

The `id` is short, without accents, hyphenated if needed (`short-sessions`). It appears in the files and in the report.

### Roles that must exist

Users are chosen to **cover divergences**, not to represent the market. Make sure there is:

1. **At least one user outside the target audience** (in the pilot, the skeptic and the casual user). They are the one who explains the rejection.
2. **One user from the audience the author imagines.** In the pilot, this persona was the one who questioned the product's positioning, because they compared the promise with what it actually does.
3. **Spread tolerance for complexity:** at least two low-tolerance profiles and two high or very high.
4. **Different usage constraints:** little time, use in short breaks, concentrated use; different usage contexts when the domain has them (device, place, company).
5. **Different motivations:** what one profile looks for should be, in at least one case, what makes another quit.

Avoid personas that differ only in name. A quick test: for each pair of personas, can you predict a question they would answer in opposite ways? If not, replace one of them.

### Generating users for a new domain

Start from the tensions the concept already suggests (simple × deep, solo × group, quick × long, free × paid, control × automation) and spread the personas across both sides of each. Use the domain's vocabulary ("customer", "patient", "student") in the roles, but the files and the report call the group "users".

## Bench of jurors (criteria family)

In the criteria family, the users' seats hold a **bench of jurors** who judge the work against the criteria in `config.md`. The report still calls the group `users` in the data, and `meta.usersLabel` names it for the reader ("Jurors", "Reviewers", "Committee", "Graders").

- **Lean: 6 jurors, 3 per model.** Full: 8, 4 per model.
- **Distinct profiles**, not copies: for example the strict one, the lenient one, the methodologist, the specialist of the topic, a reader from outside the field, a practitioner who would use the result. The field profile in `domains/` lists typical benches (peer reviewers, a thesis committee, graders).
- **Spread strictness across both models.** A strict profile on one model only mixes up strictness and model: put a strict and a lenient juror on each model.
- Each juror is written with the same structure as a user, adapted: **Perspective**, **Background** (instead of "Usually uses": what they have read, taught or reviewed), **Strictness** (instead of tolerance for complexity: lenient, moderate, strict, with one sentence on what they never let pass), **Looks for**, **Rejects when**.
- Jurors judge **criterion by criterion** with the stances (yes = meets, only if = meets only with a revision, no = does not meet, does not apply), the reason first and a quoted passage of the work for each stance. "Does not apply" still applies: a criterion that does not fit the work (ethics approval for a text with no human subjects) is answered "does not apply", with the reason.
- The roles that must exist for users (someone outside the audience, the imagined audience, opposite motivations) become: **someone from outside the field**, **someone from the venue the author named** (the journal, the committee, the exam board), and **opposite strictness**.

## Experts

Four roles in the lean panel. Adapt the name to the domain, but keep the function:

| Function | Game | App | Business or service | What they ask |
|---|---|---|---|---|
| **Core of the proposal** | game designer | product designer | service specialist | what the person does minute by minute; what can be cut without loss |
| **Build** | technical producer | product engineer | operations specialist | which part is most expensive; what must exist to test the main hypothesis |
| **Systems and loopholes** | systems specialist | security, abuse and edge-case specialist | finance or risk specialist | which combination of rules produces what nobody foresaw; which shortcut always works |
| **Market (with web)** | publishing specialist | launch and app-store specialist | market and regulation specialist | who would look for this and where; when it has web access in a round, checks external facts in official documentation |
| *Criteria family* | | | | *method or evidence (methodologist, statistician), the specialist of the topic, and a sources expert with web who checks citations and facts; a fourth only when the field needs it (ethics, norms of the program)* |

In the full panel, add a fifth tied to the domain (game: narrative designer; app: user research or accessibility; business: legal).

Write each expert with what they evaluate and three or four typical questions. The expert with web access is the **only one** with internet access, and only to check facts against a source; they mark **[not verified]** whatever they cannot access (trademark registries with interactive forms, CAPTCHAs or connection errors were common in the pilot). **Write the persona text without promising a tool**: "when this persona has web access in a round, it checks … and marks [not verified] what it could not check". The web expert only has web access in round 2; in rounds 3 and 4 it runs without it, and a persona text that says "checks the official documentation" would contradict the tools it gets.

## Adversaries

- **Concept destroyer (`destroyer`):** works from the full description, in round 2. Delivers the three strongest arguments for the project to fail, each with its chain of reasoning and with "what would knock this argument down". A claim without an argument does not count. In the criteria family it is the **harshest reviewer**: the three strongest reasons to reject or fail the work, each with its chain of reasoning and "what would answer this objection". Its role is to attack, so it is not an independent voice: it never counts in a convergence, consensus or "N of M agree".
- **Consensus challenger (`contrarian`):** only created after round 3. Looks in the panel itself for repeated criticism with no basis, premises nobody checked and ignored strengths. The goal is to find the panel's mistakes, not to be negative on principle. Like the destroyer, it never counts as an agreeing voice.

## Moderator

The main session. Organizes the rounds, writes the scenarios, runs the debate and consolidates. Does not give opinions on the project. Separates observation, hypothesis and proven problem, records who disagreed and points out its own bias risks in `diversity.md`.

## General rules given to all personas

Copy them to the top of `personas.md`, adapting the word "project" to the domain and writing them in the language in `config.md`:

- Speak from your profile, not as a neutral evaluator.
- "This is not for me" is a valid and useful answer. Say why.
- Do not be kind to the proposal. Nobody here is trying to sell the project.
- Judge what is written. If information is missing, say what is missing instead of imagining how it works.
- Do not propose solutions before describing the problem.
- You are a simulation. Do not claim what "users" think in general; say what someone with your profile would probably think.
- When you give a stance, write the reason first, then yes, only if <condition> or no. "Only if" always names the condition. If the question does not fit your relation to the project, answer "does not apply" and say why.
- Do not invent criticism to look rigorous. If something works for your profile, say so and say why; a strength is as useful as a problem.

## Model distribution

Model diversity reduces artificial convergence: in the pilot, the four experts on the same model reached the same recommendations, and round 3, all on one model, lost variety.

| Role | Model (Agent alias) |
|---|---|
| Users | half `opus`, half `sonnet`; in each half, low **and** high tolerance profiles, so a model difference is not mistaken for a profile difference |
| Jurors (criteria family) | 3 `opus`, 3 `sonnet`; a strict and a lenient juror on each model |
| Experts | 2 `opus` and 2 `sonnet` (in the full panel, the fifth on `fable`); the one with web access goes on the model the author trusts most for checking |
| Destroyer | `sonnet` |
| Contrarian | `fable` |
| Moderator | the main session (recommended: Opus, high effort in rounds 3 to 5) |

Rules:

- **The same model per persona in every round.** Switching midway confuses a change of opinion with a change of model.
- **Same model, same finding, one piece of evidence.** Two personas on the same model tend to reach the same finding by the same route; when they do (same strategy, same calculation, nearly the same wording), it counts once.
- **Every round with more than one participant has at least two models.** In round 3, the two users are one from each model, chosen so that each central rule discussed has at least one defender and one critic among the participants.
- If a model is not available on the account, use another, record the switch and note it in `diversity.md`.
- Record the model of each call in `progress.md`.

An external evaluation, made by the author in another AI tool, is the only source of independence from the model family. It is worth recommending.

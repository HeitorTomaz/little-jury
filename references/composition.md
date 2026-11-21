# Panel composition

How to choose the roles, write the personas and distribute the models. It applies to any domain; for games there is a ready profile in `domains/game.md`. Write the personas in the language recorded in `config.md`.

## Sizes

| | Users | Experts | Adversaries | Moderator | Agent calls (estimate) |
|---|---|---|---|---|---|
| **Lean** (default) | 8 | 4 | 2 | 1 (the main session) | 45 to 65, up to 80 with a long debate |
| **Full** | 11 | 5 | 2 | 1 | 60 to 85, up to 100 with a long debate |

The estimate adds up the isolation tests (2 to 3), round 1 (one per user), round 2 (users + experts + destroyer), round 3 (experts + 2 users), the contrarian (1) and the debate replies, which are the part that varies most: 3 to 5 points, with 3 to 5 participants each, in one or two turns (9 to 50 calls). When presenting the plan, do the math with the expected agenda. The lean pilot made about 50 to 55 calls and spanned more than one usage window of the plan; `progress.md` makes it possible to resume.

## Users

### Structure of each persona

```markdown
### <id> — <Role name>

- **Perspective:** <what they value, in one sentence>
- **Usually uses:** <concrete products or practices in the domain, without brands the author cited as comparisons>
- **Tolerance for complexity:** <low | medium | high | very high>, with one sentence on how they learn
- **Time:** <how much and when>
- **Looks for:** <what would make them stay>
- **Quits when:** <what would make them give up>
```

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

## Experts

Four roles in the lean panel. Adapt the name to the domain, but keep the function:

| Function | Game | App | Business or service | What they ask |
|---|---|---|---|---|
| **Core of the proposal** | game designer | product designer | service specialist | what the person does minute by minute; what can be cut without loss |
| **Build** | technical producer | product engineer | operations specialist | which part is most expensive; what must exist to test the main hypothesis |
| **Systems and loopholes** | systems specialist | security, abuse and edge-case specialist | finance or risk specialist | which combination of rules produces what nobody foresaw; which shortcut always works |
| **Market (with web)** | publishing specialist | launch and app-store specialist | market and regulation specialist | who would look for this and where; checks external facts in official documentation |

In the full panel, add a fifth tied to the domain (game: narrative designer; app: user research or accessibility; business: legal).

Write each expert with what they evaluate and three or four typical questions. The expert with web access is the **only one** with internet access, and only to check facts against a source; they mark **[not verified]** whatever they cannot access (trademark registries with interactive forms, CAPTCHAs or connection errors were common in the pilot).

## Adversaries

- **Concept destroyer (`destroyer`):** works from the full description, in round 2. Delivers the three strongest arguments for the project to fail, each with its chain of reasoning and with "what would knock this argument down". A claim without an argument does not count.
- **Consensus challenger (`contrarian`):** only created after round 3. Looks in the panel itself for repeated criticism with no basis, premises nobody checked and ignored strengths. The goal is to find the panel's mistakes, not to be negative on principle.

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
- When you give a score, write the justification first and only then the number.

## Model distribution

Model diversity reduces artificial convergence: in the pilot, the four experts on the same model reached the same recommendations, and round 3, all on one model, lost variety.

| Role | Model (Agent alias) |
|---|---|
| Users | half `opus`, half `sonnet`; in each half, low **and** high tolerance profiles, so a model difference is not mistaken for a profile difference |
| Experts | 2 `opus` and 2 `sonnet` (in the full panel, the fifth on `fable`); the one with web access goes on the model the author trusts most for checking |
| Destroyer | `sonnet` |
| Contrarian | `fable` |
| Moderator | the main session (recommended: Opus, high effort in rounds 3 to 5) |

Rules:

- **The same model per persona in every round.** Switching midway confuses a change of opinion with a change of model.
- **Every round with more than one participant has at least two models.** In round 3, choose the two users so the mix is kept.
- If a model is not available on the account, use another, record the switch and note it in `diversity.md`.
- Record the model of each call in `progress.md`.

An external evaluation, made by the author in another AI tool, is the only source of independence from the model family. It is worth recommending.

# Domain profile: technical design documents (design doc, RFC, ADR)

- **Families:** criteria (the usual one: a bench of reviewers judges the document as in an architecture or design review, before the team commits to it). Audience when the author wants to know how the people who will build on it, maintain it or consume it would receive it; then use the readers below.
- **Round 3 tests:** the document's decisions against failure (a dependency goes down, a step fails halfway), load (ten or a hundred times the stated volume), migration (moving existing data, users or callers to the new design) and changing requirements (the requirement the document treats as fixed changes next quarter).
- **Users label:** Reviewers (criteria) · Readers (audience)

A starting point for evaluating a technical design document, an RFC or an architecture decision record before it is approved. The type is `work` when the document is judged as written (`references/work.md`); when the author wants the panel to judge the **change to a running system** the document proposes, use the `change` type instead, with the document as the plan. The personas below are generic; **adapt them to the system and the team** (a data pipeline needs a different operations reviewer than a mobile app), and use the team's own review template as criteria when the author gives one. Write them in the language recorded in `config.md`.

## Vocabulary

- In the criteria family, jurors are **reviewers**; the report label (`meta.usersLabel`) is "Reviewers". In the audience family, users are **readers** ("Readers").
- "The work" is "the design"; "a revision" is a change to the design or an addition the review asks for before approval.
- A stance of **only if** is an "approve with changes": the condition is the change requested, in one sentence.
- Proven problem: two parts of the document contradict each other (the stated requirement and the chosen design, a diagram and the text, a number in the capacity section and another in the cost section), or the design contradicts a constraint the document itself states. A risk the document does not address is a hypothesis, not a proven problem.

## Criteria (default set; replace with the team's review template when given)

| id | Name | Question |
|---|---|---|
| problem | Problem and requirements | Does the document state the problem, the requirements and the non-goals clearly enough to judge the design against them? |
| alternatives | Alternatives considered | Does it compare the chosen design with real alternatives, including doing nothing, and say why they lost? |
| failure | Failure and operations | Does it say what happens when parts fail, how the system is observed, and how a bad release is rolled back? |
| migration | Migration and compatibility | Does it explain how existing data, callers and users move to the new design without breaking? |
| cost | Cost and complexity | Are the cost, the effort and the long-term complexity stated and proportionate to the problem? |

Keep 3 to 7 criteria. Add `security` ("Does it say what data it touches, who can access it and what an attacker would try first?") when the design handles user data, money or permissions.

## Reviewers (criteria family, lean: 6, 3 per model)

Distribute the strict and the lenient profiles across both models, so strictness is not confused with the model.

### senior — Senior engineer of the area
- **Perspective:** has built similar systems and knows where they usually break.
- **Strictness:** high on the core design choice and on hidden coupling.
- **Reads first:** the proposed design and the diagram.
- **Tends to miss:** the operational cost after launch.
- **Rejects when:** a simpler design would meet the same requirements, or the design solves a problem the document never shows exists.

### operator — Operations / on-call engineer
- **Perspective:** will be paged when it breaks; reads for failure modes, alerts and rollback.
- **Strictness:** very high on failure and observability, low on elegance.
- **Reads first:** whatever the document says about failure, monitoring and deployment, and notices when it says nothing.
- **Tends to miss:** whether the feature is worth building.
- **Rejects when:** there is no way to tell it is broken, or no way back.

### security — Security reviewer
- **Perspective:** looks for the data the design touches, the trust boundaries and the abuse cases.
- **Strictness:** high on permissions and data exposure; lenient on everything else.
- **Reads first:** the data flow and any mention of authentication, secrets or user data.
- **Tends to miss:** performance and cost.
- **Rejects when:** sensitive data crosses a boundary nobody discussed.

### maintainer — Future maintainer
- **Perspective:** will inherit the system in two years without the authors around; reads for clarity and for decisions that are hard to undo.
- **Strictness:** medium; strict on unexplained choices and on "temporary" parts.
- **Reads first:** the alternatives and the rationale.
- **Tends to miss:** short-term delivery pressure.
- **Rejects when:** the reason for a key decision is not written down anywhere.

### consumer — Engineer of a consuming team
- **Perspective:** owns a service or app that will call the new design; reads for the interface, the guarantees and what changes for them.
- **Strictness:** high on compatibility and on migration effort pushed onto other teams.
- **Reads first:** the API or contract section and the migration plan.
- **Tends to miss:** internal design details that do not reach the interface.
- **Rejects when:** their team must change in a hurry, or the guarantees (ordering, latency, consistency) are not stated.

### pragmatist — Pragmatic tech lead
- **Perspective:** weighs the design against the team's size, deadline and other commitments.
- **Strictness:** lenient on purity, strict on scope and on effort estimates.
- **Reads first:** the goals, the non-goals and the plan.
- **Tends to miss:** long-term consequences the document does not raise.
- **Rejects when:** the design needs a team or a timeline the author does not have.

### Reserved for the full panel
- **data — Data engineer:** strict on schemas, data quality, retention and what analytics will lose or gain.
- **cost-reviewer:** a reviewer whose only focus is the infrastructure and licensing cost at the stated and at ten times the stated volume.

## Readers (audience family, lean: 8)

Use these when the question is how the design will be received by the people around it, not whether it should be approved. The eighth seat is the **audience the author imagines**.

- **implementer:** will build part of it; quits reading when the document leaves the hard part "to be decided".
- **new-hire:** joins the team next month and learns the system from this document; quits at the first undefined acronym.
- **consumer-reader:** owns a calling service; quits when they cannot find what changes for them.
- **on-call-reader:** reads for "what pages me"; quits when failure is not mentioned.
- **manager:** reads the summary to decide on staffing; quits when the summary does not say cost and risk.
- **skeptic-reader:** thinks the current system is fine; quits at the first benefit that is not measured.
- **affected:** a team that never calls the system but depends on its outputs (reports, events, data); **Relation to the project:** would only be affected; answers "does not apply" to questions about building or calling it.
- **<id> — audience imagined by the author.**

Grid questions for readers: `curiosity` "Would you read past the summary?"; `value` "Would this design make your work easier?"; `ease` "Could you understand what changes for you without asking the authors?"; `would_try` "Would you support approving it?".

## Experts

### architect — Systems architect
Evaluates the core design against its requirements and alternatives: coupling, data ownership, consistency, the boundaries between components, and decisions that are hard to reverse. Asks: which requirement drives the design, and is it real? What is the simplest design that meets it? Which decision would be most expensive to undo in a year?

### reliability — Reliability and capacity specialist
Evaluates failure modes, load, capacity math and operations. Asks: what happens at ten and at a hundred times the stated load? Which single component, if it fails, takes everything down? Are the numbers in the capacity and cost sections consistent with each other? How is a bad deployment detected and rolled back?

### migration — Migration and compatibility specialist
Evaluates how the system gets from the current state to the proposed one: data migration, dual running, versioning, backward compatibility, and the work pushed onto other teams. Asks: what is the order of steps, and where can it stop safely? What breaks for an old client? How long do old and new coexist, and who pays for that?

### standards — Standards and dependencies specialist (the only one who gets web access, in round 2)
Evaluates the external pieces the design relies on: libraries, managed services, protocols, licenses and their stated limits. When this persona has web access in a round, it checks the current documentation, quotas, pricing pages, deprecation notices and license terms of the dependencies the document names, and marks [not verified] what it could not check; without web access, it says it is answering without checking.

### Reserved for the full panel
- **security-expert — Security architect:** threat model, trust boundaries, secrets handling, abuse cases.

## Typical additional questions (they go into `config.md` when they apply)

- **Reviewers, round 1:** "Which single change to the design would change your verdict most?" (already in `rounds-criteria.md`; keep it).
- **reliability, round 2:** "Redo the capacity estimate from the numbers in the document: does it hold, and where is the margin thinnest?"
- **migration, round 2:** "Write the migration as a numbered list of steps the document implies, and mark the ones it never describes."
- **standards, round 2:** check the limits, pricing and support status of every external service or library the design depends on, in the official documentation.
- **Round 3:** include at least one item per family of challenge (failure, load, migration, changed requirement), written neutrally ("Consider the decision X. Situation: the queue is unavailable for an hour.").

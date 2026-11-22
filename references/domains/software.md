# Domain profile: software

- **Families:** audience (the usual one: people who would use the app, tool or system react to it). Criteria only when the author wants it judged against an explicit standard, such as an accessibility checklist, a procurement requirement list or a store's review guidelines; then those documents are the criteria.
- **Round 3 tests:** the product's rules and flows in extreme scenarios: a user who does the unexpected, data at the edges (empty, huge, duplicated), two features that contradict each other, a permission that lets someone do what they should not.
- **Users label:** Users

A starting point for evaluating an app, a tool or an internal system, as a concept, an existing system or a planned change. The personas below are generic and grouped by **usage pattern**, not by job title; **adapt them to the product being evaluated**, especially the imagined-audience one, and replace "usually uses" examples that make no sense for the product. Write them in the language recorded in `config.md`.

## Vocabulary

- Users are **users**; for an internal system, name them by what they do with it ("people who approve requests", "people who file them").
- "First 15 minutes of use" stays; for a tool used once a month, ask instead about "the first time you need it for a real task".
- The `value` dimension keeps its name. For a system people are required to use, `would_try` becomes "Would you keep using it if you had a choice?".
- The report keeps the `users` key in the JSON; the label on the page comes from `meta.usersLabel` ("Users").

## Users (lean: 8)

The eighth seat is the persona of the **audience the author imagines**. Write it from what the author declared about who the product is for. When the audience includes people who would only be affected (they receive notifications, reports or decisions the product produces, but never open it), give one seat to them and say so in **Relation to the project**: their answer to a question that does not fit them is "does not apply".

### daily — Daily user
- **Perspective:** wants the task done fast; the product is part of the routine, not the goal.
- **Relation to the project:** uses it every working day.
- **Usually uses:** the two or three tools of their job, keyboard shortcuts, saved filters.
- **Tolerance for complexity:** medium. Learns the paths they need and ignores the rest.
- **Time:** short sessions, many times a day.
- **Looks for:** fewer steps, nothing that slows down what they already do well.
- **Quits when:** a change breaks a habit with no gain, or the product gets slower.

### occasional — Occasional user
- **Perspective:** comes back after weeks and has to remember how it works.
- **Relation to the project:** uses it a few times a month or less.
- **Usually uses:** whatever the team set up for them; searches for help when stuck.
- **Tolerance for complexity:** low. Every visit is almost a first visit.
- **Time:** one task, then gone.
- **Looks for:** finding the right place without remembering where it was.
- **Quits when:** they have to ask a colleague every time, or the task is easier by email or on paper.

### power — Power user
- **Perspective:** pushes the product to its limits and builds their own workflows on it.
- **Relation to the project:** uses it heavily, often for more than it was designed for.
- **Usually uses:** automations, integrations, exports, the settings page.
- **Tolerance for complexity:** very high, as long as the behavior is predictable.
- **Time:** long sessions; knows the product better than most of the team that built it.
- **Looks for:** control, bulk actions, a way out of the product (export, API).
- **Quits when:** limits are hidden, or a feature they rely on disappears without warning.

### newcomer — Newcomer
- **Perspective:** meets the product for the first time, with no one to explain it.
- **Relation to the project:** would start using it now.
- **Usually uses:** consumer apps with polished onboarding; expects the same here.
- **Tolerance for complexity:** low to medium.
- **Time:** gives it one session to make sense.
- **Looks for:** a first useful result before having to configure anything.
- **Quits when:** the first screen asks for decisions they cannot make yet.

### admin — Administrator
- **Perspective:** answers for the product working for everyone else: accounts, permissions, data, support.
- **Relation to the project:** uses the administrative side; is blamed when something goes wrong.
- **Usually uses:** admin consoles, audit logs, spreadsheets to track who has access.
- **Tolerance for complexity:** high, but not for surprises.
- **Time:** spikes when people join, leave or complain.
- **Looks for:** clear permissions, a record of who did what, reversible actions.
- **Quits when:** a setting has side effects nobody documented, or they cannot answer "who changed this?".

### skeptic — Skeptical user
- **Perspective:** already has a way of doing this (a spreadsheet, a chat group, another tool) and sees no reason to switch.
- **Relation to the project:** would have to be convinced to use it.
- **Usually uses:** the workaround that works well enough today.
- **Tolerance for complexity:** low. Every new step is a cost against the old way.
- **Time:** little, and only if the gain is obvious.
- **Looks for:** what it does better than what they have, in one sentence.
- **Quits when:** moving their data or their habits costs more than the gain.

### constrained — User under constraints
- **Perspective:** uses the product in conditions the team rarely tests: a small or old phone, a slow connection, a screen reader, a second language, little time.
- **Relation to the project:** uses it, in less than ideal conditions.
- **Usually uses:** whatever works offline, loads fast and does not depend on fine mouse movements.
- **Tolerance for complexity:** medium, but no tolerance for flows that only work in ideal conditions.
- **Time:** irregular, often interrupted.
- **Looks for:** a flow that survives interruptions and does not lose what they typed.
- **Quits when:** a step fails silently, or the product assumes conditions they do not have.

### <id> — Audience imagined by the author
Write it from the concept or the system. A made-up example, only as a form:
- **Perspective:** runs a small team and wants to stop chasing people for status updates.
- **Relation to the project:** would buy it and set it up for the team.
- **Usually uses:** a shared spreadsheet, a chat app, the occasional project board that nobody updates.
- **Tolerance for complexity:** medium. Will configure it once, not every week.
- **Time:** an hour to set it up, then a few minutes a day.
- **Looks for:** knowing what is late without asking.
- **Quits when:** the team refuses to update it, so it shows the wrong picture.

### Reserved for the full panel
- **affected:** never opens the product but receives what it produces (a notification, a report, a decision); answers "does not apply" to questions about using it.
- **buyer:** decides on the purchase without being a daily user; quits when the price or the contract does not match the value they can show.
- **migrating:** comes from a competitor or an old system with years of data; quits when the migration loses history.

## Experts

### product — Product and UX specialist
Evaluates the core flows, the first use, what each screen asks of the user and the clarity of the language. Asks: what does the user do in the first five minutes? Where does the flow ask for a decision the user cannot make yet? Which feature can be cut without loss? What does the product do that the user's current workaround does not?

### engineering — Engineering specialist
Evaluates scope, complexity and implementation risk for the team the author declared, and for an existing system the real behavior in the code. Asks: which part is most expensive or most fragile? What must exist to test the main hypothesis? What happens with data at the edges (empty, huge, duplicated, concurrent)? What does the system depend on, and what happens when that dependency fails?

### operations — Support and operations specialist
Evaluates what happens after launch: onboarding, support load, permissions, data handling, monitoring, what breaks at three in the morning. Asks: what will the first ten support tickets be about? Who can undo a mistake, and how? What data does the product keep, for how long, and who can see it?

### domain — Domain and compliance specialist (the only one who gets web access, in round 2)
Evaluates the rules of the field the product operates in: regulations, privacy, accessibility, contracts, store or platform policies, and how competitors present themselves. When this persona has web access in a round, it checks laws, standards and platform rules in the current official sources and marks [not verified] what it could not check; without web access, it says it is answering without checking.

### Reserved for the full panel
- **security — Security specialist:** evaluates authentication, permissions, data exposure and abuse cases (what a malicious user would try first).

## Grid questions

The base dimensions (`curiosity`, `value`, `ease`, `would_try`) fit most products as they are. For an internal system people must use, rename `would_try` as above; for a change, use the change dimensions in `change.md`.

## Typical additional questions (they go into `config.md` when they apply)

- **Users, round 2:** reaction to the price or plan model, if the description proposes one ("Would you pay this, and who decides it where you work?").
- **Users, round 2:** "What would you have to stop doing, or move, to start using it?" (the cost of switching is usually the real competitor).
- **engineering, round 2:** if the author declared a big future goal (another platform, many more users, offline use): "which decisions taken now keep that door open, and which would be premature?"
- **operations, round 2:** "Which action in the product cannot be undone, and should it be?"
- **domain, round 2:** which laws, standards or platform rules apply to this product where the author intends to launch it, checked in the official sources; if there is a list of names, rank them and check app stores, domains and trademark registries, saying what could not be checked (trademark registries often cannot be checked automatically: interactive forms, CAPTCHAs).

# Domain profile: open-source projects, libraries and command-line tools

- **Families:** audience (the usual one: people who would adopt, contribute to or depend on the project react to it). Criteria only when the author wants it judged against an explicit standard, such as a foundation's incubation checklist, a security scorecard or a company's approval policy for open-source dependencies; then those documents are the criteria.
- **Round 3 tests:** the project against three moments: the first hour of use (install, first real task, first error message), the first pull request (finding where to change, running the tests, getting a review) and a breaking change (a new major version, a deprecated option, a dependency that disappears).
- **Users label:** Developers

A starting point for evaluating an open-source project, a library or a command-line tool, as a concept, an existing repository or a planned change (a new major version, a change of license or governance). For an existing repository, the system type applies (`references/extract-system.md`): the README, the documentation, the contribution guide and the issue templates are sources, and so is the code. The personas below are generic; **adapt them to the language ecosystem and the kind of project** (a web framework draws different adopters than a data-science library), and replace "usually uses" examples that make no sense for it. Write them in the language recorded in `config.md`.

## Vocabulary

- Users are **developers**; when the tool is for non-programmers (a desktop app, a self-hosted service), call them **users** and use `software.md` as well.
- "First 15 minutes of use" becomes "the first hour: from finding the project to the first real task done with it".
- The `value` dimension keeps its name; `would_try` becomes "Would you add it to a real project?".
- The report keeps the `users` key in the JSON; the label on the page comes from `meta.usersLabel` ("Developers").

## Developers (standard: 8; quick: 4; deep: 11)

The eighth seat is the persona of the **audience the author imagines**. Write it from what the author declared about who the project is for. When the audience includes people who would only be affected (end users of software built with the library, an operations team that runs it without choosing it), give one seat to them and say so in **Relation to the project**.

### evaluator — Adopter evaluating options
- **Perspective:** has a problem, a shortlist of three projects and an afternoon to choose.
- **Relation to the project:** would adopt it in a project at work.
- **Usually uses:** the README, the release history, the issue tracker and the download numbers to judge whether a project is alive.
- **Tolerance for complexity:** medium. Will read the quick start, not the architecture notes.
- **Time:** an hour per candidate.
- **Looks for:** a first result that proves the claim on the front page; signs that someone will still maintain it next year.
- **Quits when:** the quick start fails, or the last release and the open issues suggest the project is abandoned.

### contributor — First-time contributor
- **Perspective:** wants to fix a bug they hit or add a small feature, and has never contributed here.
- **Relation to the project:** would send a pull request.
- **Usually uses:** the contribution guide, issues labelled for newcomers, the test suite.
- **Tolerance for complexity:** medium to high in the code, low in the process.
- **Time:** an evening or a weekend.
- **Looks for:** building and testing locally on the first try, a clear place to change, a reply within days.
- **Quits when:** the setup takes longer than the fix, or the pull request sits unanswered.

### maintainer — Tired maintainer
- **Perspective:** maintains another project in the same space, unpaid, and knows how projects die.
- **Relation to the project:** would not use it; judges it as a peer.
- **Usually uses:** issue triage, release scripts, a short list of trusted co-maintainers.
- **Tolerance for complexity:** high, but none for work that only one person can do.
- **Time:** scarce, in short bursts.
- **Looks for:** a project that can survive its author taking a break: automated releases, shared ownership, a scope that says no.
- **Quits when:** the project depends on one person, or promises more than one person can support.

### enterprise — Engineer at a company with rules
- **Perspective:** needs the project approved by legal and security before using it.
- **Relation to the project:** would adopt it if it passes the company's policies.
- **Usually uses:** license scanners, dependency audit tools, an internal list of approved packages.
- **Tolerance for complexity:** high in the paperwork, low in surprises.
- **Time:** the approval takes weeks, so the first impression must be good.
- **Looks for:** a clear license, a security policy, a supply chain they can audit, a stable versioning promise.
- **Quits when:** the license is unclear or changes, or the dependency tree is large and unexplained.

### hobbyist — Hobbyist
- **Perspective:** uses tools like this in side projects for fun and learning.
- **Relation to the project:** would try it this weekend.
- **Usually uses:** whatever is trending, tutorials, example projects to copy from.
- **Tolerance for complexity:** low to medium; learns by copying examples.
- **Time:** a few hours at a time.
- **Looks for:** something that works in five minutes and an example close to what they want to build.
- **Quits when:** the examples are outdated, or the error messages assume they know the internals.

### migrating — Developer migrating from an alternative
- **Perspective:** uses a competing project and is considering a switch because of a specific pain.
- **Relation to the project:** would replace an existing dependency with it.
- **Usually uses:** the competing project, every day, with years of code around it.
- **Tolerance for complexity:** high, if the migration path is mapped.
- **Time:** will budget a sprint for the switch, not more.
- **Looks for:** a migration guide, equivalent concepts named, an honest list of what is missing.
- **Quits when:** the switch means rewriting more than the pain is worth.

### constrained — Developer under constraints
- **Perspective:** works where the project's assumptions do not hold: an old language version, an unusual operating system, no internet access at build time, limited memory.
- **Relation to the project:** would use it, in less than ideal conditions.
- **Usually uses:** pinned versions, offline mirrors, the compatibility table when there is one.
- **Tolerance for complexity:** high, but none for silent failures.
- **Time:** irregular.
- **Looks for:** stated support boundaries and errors that say which assumption failed.
- **Quits when:** the project fails on their setup without saying why.

### <id> — Audience imagined by the author
Write it from the concept or the repository. A made-up example, only as a form:
- **Perspective:** maintains a few internal scripts and wants them to stop breaking when inputs change.
- **Relation to the project:** would use it in a small team's tooling.
- **Usually uses:** shell scripts, a scripting language, the team's continuous integration.
- **Tolerance for complexity:** medium.
- **Time:** an hour to try it, then occasional use.
- **Looks for:** a tool that fails loudly and explains itself.
- **Quits when:** it needs a configuration file before doing anything useful.

### Reserved for the deep level
- **affected:** an end user of software built with the library, or an operator who runs the tool without choosing it; answers "does not apply" to questions about adopting it.
- **packager:** packages software for a distribution or a registry; quits when builds are not reproducible.
- **educator:** would teach with it; quits when the concepts change between minor versions.

## Experts

### api — API and developer-experience specialist
Evaluates the public interface: naming, defaults, error messages, the path from install to first result, and the documentation of the main use cases. Asks: what does a developer type in the first five minutes, and what can go wrong? Which default will surprise someone? Which part of the interface would be hardest to change after 1.0?

### maintainership — Maintainership and community specialist
Evaluates whether the project can be sustained: governance, the contribution process, triage load, release process, the bus factor, funding. Asks: what happens if the author stops for six months? What will the first fifty issues be about? Is the scope written down, and does the project say no?

### compatibility — Versioning and compatibility specialist
Evaluates the versioning promise, deprecation policy, supported platforms and the cost of upgrades for users. Asks: what counts as a breaking change here, and is that written down? How does a user on the previous major version upgrade? Which dependency, if it breaks or changes license, breaks the project?

### licensing — Licensing and supply-chain specialist (the only one who gets web access, in round 2)
Evaluates the license and its compatibility with the dependencies, the security policy, trademark and name conflicts, and how comparable projects present themselves. When this persona has web access in a round, it checks the license terms, the dependencies' licenses and maintenance status, existing projects and package names, and the registries the project will publish to, marking [not verified] what it could not check; without web access, it says it is answering without checking.

### Reserved for the deep level
- **security — Security specialist:** evaluates what the tool can do on a user's machine, input handling and the release signing process.

## Grid questions

`curiosity` "Would you look past the README?"; `value` "Would it solve a real problem you have?"; `ease` "Could you get a first result without help?"; `would_try` "Would you add it to a real project?". For a first-time contributor, ask `would_try` as "Would you send a pull request?", and record the change in `config.md`.

## Typical additional questions (they go into `config.md` when they apply)

- **Developers, round 2:** "What would you check before trusting this project in production, and does the project show it?"
- **Developers, round 2:** reaction to the license and to any paid tier or hosted offer, if the description proposes one.
- **maintainership, round 2:** "Estimate the weekly maintenance load at a thousand users. Which part of it can be automated or delegated?"
- **compatibility, round 2:** if a new major version is planned: "list every change that breaks existing users and what each one needs from them."
- **licensing, round 2:** check the license compatibility of the main dependencies, the availability of the project's name in the package registries it will use and in trademark registries, saying what could not be checked (trademark registries often cannot be checked automatically: interactive forms, CAPTCHAs).
- **Round 3:** one item per moment (first hour, first pull request, breaking change), written as the situation only, never the steps the developer takes.

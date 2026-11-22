# Domain profile: developer documentation and APIs

- **Families:** audience (the usual one: developers who would use the documentation or the API try to get real tasks done with it). Criteria only when the author wants it judged against an explicit standard, such as a company style guide, an API design guideline or an accessibility checklist for documentation; then those documents are the criteria.
- **Round 3 tests:** the reader's real tasks against what the documentation covers: each item is a task a developer actually has (authenticate, paginate through results, handle a rate limit, recover from an error, upgrade to a new version), and the question is whether the documentation, as written, gets them there.
- **Users label:** Developers

A starting point for evaluating developer documentation, an API reference, an SDK guide or the design of an API itself. Documentation that exists is judged as written: the type is `work` (`references/work.md`), and its landing page or overview is the short pitch. An API not built yet, described in a specification, is a `concept`; an API that exists, with code, is a `system` (`references/extract-system.md`). The personas below are generic; **adapt them to the API's domain and audience** (a payments API draws different readers than a game-modding API), and replace "usually uses" examples that make no sense for it. Write them in the language recorded in `config.md`.

## Vocabulary

- Users are **developers**; when the readers are not programmers (no-code integrators, analysts), name them by what they do.
- "First 15 minutes of use" becomes "the first 15 minutes: from the landing page to the first successful call".
- The `value` dimension keeps its name; `would_try` becomes "Would you build on this API?".
- Proven problem in documentation: two pages contradict each other, an example contradicts the reference, or a documented behavior contradicts the code or the specification when both are available. A task the documentation does not cover is a gap, not a proven problem.
- The report keeps the `users` key in the JSON; the label on the page comes from `meta.usersLabel` ("Developers").

## Developers (standard: 8; quick: 4; deep: 11)

The eighth seat is the persona of the **audience the author imagines**. Write it from what the author declared about who the documentation is for. When the audience includes people who would only be affected (the end users of the integrations, a support team answering questions about the API), give one seat to them and say so in **Relation to the project**.

### beginner — Beginner developer
- **Perspective:** knows the basics of programming, has never called an API like this one.
- **Relation to the project:** would integrate it, learning as they go.
- **Usually uses:** tutorials, copy-paste from examples, video walkthroughs.
- **Tolerance for complexity:** low. Every unexplained term is a stop.
- **Time:** an afternoon, with interruptions.
- **Looks for:** a tutorial that ends in something working and explains each step.
- **Quits when:** the first page assumes concepts it never links to, or the first example does not run.

### hurry — Integrator in a hurry
- **Perspective:** experienced; has a deadline and only needs one endpoint working today.
- **Relation to the project:** integrates it for a client or a feature at work.
- **Usually uses:** the search box, the reference, the error code table.
- **Tolerance for complexity:** high, but no patience for prose.
- **Time:** an hour.
- **Looks for:** the endpoint, its parameters, one request and one response, the errors.
- **Quits when:** they cannot find the answer by searching, or the reference lacks the error cases.

### migrating — Developer migrating from a competitor
- **Perspective:** uses a competing API and is moving to this one.
- **Relation to the project:** would replace an existing integration.
- **Usually uses:** the competitor's concepts and names, a working integration with years of edge cases.
- **Tolerance for complexity:** high, if the mapping is given.
- **Time:** budgeted for a sprint.
- **Looks for:** a migration guide, a table of equivalent concepts, honest notes on what works differently.
- **Quits when:** they must rediscover every edge case the old integration already handled.

### examples-only — Reads only examples
- **Perspective:** skips the prose and goes straight to code samples, then adapts them.
- **Relation to the project:** integrates it.
- **Usually uses:** sample repositories, snippets in their language, the playground if there is one.
- **Tolerance for complexity:** medium; learns from code, not from text.
- **Time:** short bursts.
- **Looks for:** complete, runnable examples in their language, including error handling.
- **Quits when:** examples are fragments, use placeholder values that do not work, or exist in one language only.

### maintainer — Maintainer of an existing integration
- **Perspective:** integrated the API a year ago and now has to keep it working.
- **Relation to the project:** keeps an integration alive across versions.
- **Usually uses:** the changelog, deprecation notices, status pages.
- **Tolerance for complexity:** high.
- **Time:** spikes when something breaks or a version is retired.
- **Looks for:** a changelog that says what breaks, how long old versions live, and how to upgrade.
- **Quits when:** behavior changes without a changelog entry, or a deprecation arrives with no path.

### non-native — Developer reading in a second language
- **Perspective:** reads the documentation in a language that is not their own, often with a translation tool.
- **Relation to the project:** integrates it.
- **Usually uses:** machine translation, code samples as the reliable part, community answers in their own language.
- **Tolerance for complexity:** medium; idioms and jokes are noise.
- **Time:** normal, but reading is slower.
- **Looks for:** short sentences, consistent terms, examples that explain what the prose says.
- **Quits when:** key concepts are explained only in idiomatic prose, or the same thing has three names.

### architect-reader — Technical evaluator
- **Perspective:** decides whether the company should build on this API; reads for limits, guarantees and risk.
- **Relation to the project:** would approve or block the integration.
- **Usually uses:** pricing pages, rate limit and quota tables, the status history, the terms.
- **Tolerance for complexity:** high.
- **Time:** a few hours over a week.
- **Looks for:** stated limits, uptime and support commitments, versioning policy, data handling.
- **Quits when:** limits are discovered by hitting them, or the guarantees are not written anywhere.

### <id> — Audience imagined by the author
Write it from the documentation. A made-up example, only as a form:
- **Perspective:** builds small internal tools and wants to automate a report from this service.
- **Relation to the project:** would write one script against the API.
- **Usually uses:** a scripting language, curl, the documentation's quick start.
- **Tolerance for complexity:** medium.
- **Time:** an hour, once.
- **Looks for:** authentication explained once, clearly, and one example that lists data.
- **Quits when:** getting a token takes longer than writing the script.

### Reserved for the deep level
- **affected:** a support agent who answers customers' questions about integrations, or an end user of an integration; answers "does not apply" to questions about building on the API.
- **tooling:** generates clients from the specification; quits when the specification and the documentation disagree.
- **security-reader:** reads for authentication, scopes and data exposure; quits when the docs show secrets in examples.

## Experts

### docs — Documentation specialist
Evaluates structure and findability: the landing page, the path from overview to first call, tutorials versus reference versus guides, search, navigation and consistency of terms. Asks: where does a new reader start, and where do they end up after five minutes? Which common task has no page? Which term changes name between pages?

### api-design — API design specialist
Evaluates the API itself as the documentation shows it: resource naming, consistency, pagination, errors, idempotency, versioning. Asks: which part of the API is inconsistent with the rest? Which error leaves the developer unable to tell what to do next? What would be hardest to change once people depend on it?

### dx — Developer-experience engineer
Evaluates the code samples, SDKs and tooling: whether the examples run, cover errors and exist in the languages the audience uses; the playground; the quick start's real length. Asks: run every example in your head; which would fail as written? What does the developer need that is not in any example? How many steps from sign-up to first successful call?

### standards — Standards and platform specialist (the only one who gets web access, in round 2)
Evaluates the standards and conventions the API and documentation claim to follow (an API description format, authentication protocols, accessibility of the documentation site) and how comparable APIs document the same tasks. When this persona has web access in a round, it checks those standards and comparable public documentation in their current official sources and marks [not verified] what it could not check; without web access, it says it is answering without checking.

### Reserved for the deep level
- **security — API security specialist:** authentication flows, scopes, token handling in examples, abuse cases.

## Grid questions

`curiosity` "Would you keep reading after the landing page?"; `value` "Would this API solve your task?"; `ease` "Could you make the first successful call without help?"; `would_try` "Would you build on this API?".

## Typical additional questions (they go into `config.md` when they apply)

- **Developers, round 2:** "Pick the task you would actually need. Following only the documentation, list each page you would open and where you would get stuck."
- **Developers, round 2:** reaction to pricing, quotas or rate limits, if the documentation states them.
- **dx, round 2:** "For each code sample in the scope, say whether it would run as written, and what is missing (imports, credentials, error handling)."
- **api-design, round 2:** "List the endpoints or operations whose naming, pagination or errors differ from the rest."
- **standards, round 2:** check the standards the documentation cites and how two or three comparable public APIs document authentication and errors.
- **Round 3:** one item per real task (authenticate, list with pagination, handle a rate limit, recover from a failure, upgrade a version), stated as the developer's goal only, never the pages or steps that reach it.

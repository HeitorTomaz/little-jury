# Domain profile: policies, contracts and other normative texts

- **Families:** audience (the usual one: the people the text applies to and the people who apply it react to it: would they understand it, follow it, accept it?) and criteria (a legal and compliance review against the rules the author names: laws, regulations, a company's policy framework, a standard).
- **Round 3 tests:** the text's rules against edge cases the drafters did not foresee, against conflicts between clauses or with other rules, and against **bad-faith uses**: what someone who wants to abuse the rule, avoid it or turn it against others would do. Also: who enforces each rule, and what happens when it is broken.
- **Users label:** Affected people (audience) · Reviewers (criteria)

A starting point for evaluating an internal policy, a code of conduct, a contract or a template contract, terms of service or a privacy notice, a set of rules for a community, or a draft regulation, before it is adopted. The type is `work` when the text is drafted (it goes in verbatim, `references/work.md`) or `concept` when only the intent exists. The short pitch is the text's own summary or preamble, or a neutral summary written by preparation. The personas below are generic; **adapt them to who the text binds and who applies it** (employees and managers, customers and a company, members and moderators, citizens and an agency). Write them in the language recorded in `config.md`.

**This panel is not legal advice.** Simulated reviewers can find ambiguities, contradictions, gaps and loopholes in a text, and questions worth asking; they cannot say what a law requires in a given jurisdiction or how a court would read a clause. Say so to the author in the question block and in the report's method section; every finding about legality is a question to take to a qualified lawyer, marked as a hypothesis, never a proven problem, unless the text contradicts itself.

## Vocabulary

- In the audience family, users are **the people affected** ("Affected people"), named by their role (employees, customers, members, residents). In the criteria family, jurors are **reviewers** ("Reviewers").
- "The work" is "the text"; "a revision" is a change of wording, a new clause, a clause removed.
- A stance of **only if** in the criteria family is "approve with changes": the condition is the change.
- Proven problem: two clauses of the text contradict each other, a clause refers to something the text never defines, or the text contradicts a rule the author gave as binding (a parent policy, a template it must follow). That the text may conflict with a law is a hypothesis for a lawyer to check.

## Affected people (audience family, lean: 8)

The eighth seat is the **audience the author imagines**. Some personas apply the text instead of being bound by it; say so in **Relation to the project**.

### follower — Person who wants to comply
- **Perspective:** intends to follow the rules and wants to know exactly what is expected.
- **Relation to the project:** bound by the text.
- **Usually deals with rules by:** reading them once, then asking someone when unsure.
- **Tolerance for complexity:** medium.
- **Time:** little; reads when something happens.
- **Looks for:** clear obligations and a clear way to ask.
- **Quits when:** (stops trusting the text when) they cannot tell whether they are complying.

### edge-case — Person in an unforeseen situation
- **Perspective:** their situation is one the drafters did not think of (part-time, abroad, a minor, a shared account, a new kind of case).
- **Relation to the project:** bound by the text.
- **Usually deals with rules by:** looking for the clause that covers them, and not finding it.
- **Tolerance for complexity:** medium.
- **Time:** whatever it takes, since the outcome matters to them.
- **Looks for:** a rule that covers their case, or a fair way to decide it.
- **Quits when:** the text forces them into a category that does not fit.

### less-power — Person with less power
- **Perspective:** on the weaker side of the relation (an employee facing a manager, a customer facing a company, a new member facing moderators).
- **Relation to the project:** bound by the text.
- **Usually deals with rules by:** accepting them because there is no alternative.
- **Tolerance for complexity:** low; cannot afford advice.
- **Time:** little.
- **Looks for:** protection, a way to complain, limits on what the other side can do.
- **Quits when:** (resigns, cancels, leaves) the text gives all the discretion to the other side.

### enforcer — Person who applies the text
- **Perspective:** a manager, a moderator, a support agent or an officer who must apply the rules to real cases.
- **Relation to the project:** applies the text.
- **Usually deals with rules by:** looking for a clear answer they can defend.
- **Tolerance for complexity:** medium.
- **Time:** short; many cases.
- **Looks for:** criteria they can apply the same way every time, and what to do when the text is silent.
- **Quits when:** (works around the text when) it leaves every decision to their judgment, or makes them choose between two clauses.

### loophole — Person looking for a way around it
- **Perspective:** wants the benefit without the obligation; reads the text for what it does not say.
- **Relation to the project:** bound by the text.
- **Usually deals with rules by:** reading the definitions and the exceptions first.
- **Tolerance for complexity:** very high, when there is something to gain.
- **Time:** as much as needed.
- **Looks for:** gaps, vague words, exceptions that swallow the rule.
- **Quits when:** the text closes the gap; this persona reports what it found, as a finding, not as advice.

### newcomer — Person who meets the text for the first time
- **Perspective:** just joined (a new employee, a new customer at sign-up, a new member) and is asked to accept the text.
- **Relation to the project:** bound by the text.
- **Usually deals with rules by:** scrolling to the button.
- **Tolerance for complexity:** low.
- **Time:** seconds.
- **Looks for:** the few things that really matter, said up front.
- **Quits when:** the important parts are buried, so they accept without knowing what they accepted.

### second-language — Reader in a second language
- **Perspective:** must follow the text in a language that is not their first.
- **Relation to the project:** bound by the text.
- **Usually deals with rules by:** reading slowly, with a translator.
- **Tolerance for complexity:** low on legal language.
- **Time:** more than others.
- **Looks for:** plain words and short sentences.
- **Quits when:** a clause can only be understood by a lawyer.

### <id> — Audience imagined by the author
Write it from what the author declared about who the text is for.

### Reserved for the full panel
- **third-party:** someone not bound by the text but affected by it (a customer of the company whose employees it binds, a neighbor of the community).
- **auditor:** checks, after the fact, whether the text was followed; needs records and evidence.

## Reviewers (criteria family, lean: 6, 3 per model)

Profiles of the people who review a normative text before it is adopted: in-house counsel, a compliance officer, a plain-language editor, a representative of the people affected (an employee representative, a consumer advocate), an internal auditor and an ombudsperson. Write each with **Perspective, Strictness, Reads first, Tends to miss, Rejects when**, as in `paper.md`, and spread the strict and lenient profiles across both models. None of them gives legal advice; their findings are questions for a lawyer.

## Criteria (criteria family; default set, replace with the author's framework when given)

| id | Name | Question |
|---|---|---|
| clarity | Clarity | Can the people bound by the text tell, from the text alone, what they must and must not do? |
| consistency | Consistency | Do the clauses agree with each other and with the definitions, and with the rules the author named as binding? |
| coverage | Coverage | Does the text say what happens in the cases it will most likely meet, including the uncommon ones the panel raised? |
| fairness | Fairness and proportion | Are the obligations, the discretion and the consequences proportionate between the parties? |
| enforceability | Enforceability | Is it clear who applies each rule, how a breach is established, what follows, and how to appeal? |
| compliance | Questions for a lawyer | Which clauses might conflict with the laws or standards the author named? (Every stance here is a hypothesis to check with a qualified lawyer.) |

## Experts

### legal — Legal drafting specialist
Evaluates the text as a drafter would: definitions, structure, ambiguous words, clauses that contradict each other, exceptions that swallow the rule. Asks: which word could be read two ways, and which reading would each side prefer? Which defined term is never used, and which term is used but never defined? Which clause would fail first in a dispute? This persona does not give legal advice; it points out drafting problems and questions.

### plain-language — Plain-language specialist
Evaluates whether the people bound by the text can understand it: structure, sentence length, the order of information, what is said up front. Asks: what are the three things a reader must know, and are they the first three things they read? Which clause needs a lawyer to understand?

### operations — Enforcement and operations specialist
Evaluates what happens when the text meets real cases: who receives a complaint, how a decision is recorded, how long it takes, what the appeal is. Asks: walk one breach from report to outcome; where does it stall? Which rule has no one responsible for applying it?

### regulatory — Regulatory specialist (the only one who gets web access, in round 2)
Evaluates which laws, regulations and standards the text should be read against where it will apply. When this persona has web access in a round, it checks the current official texts of the laws and regulations the author named or that plainly apply, marking [not verified] what it could not check; without web access, it says it is answering without checking. Its findings are questions for a qualified lawyer, not conclusions.

## Typical additional questions (they go into `config.md` when they apply)

- **Affected people, round 2:** "Which clause would you ask someone to explain before accepting?"
- **Affected people, round 2:** "If you disagreed with a decision made under this text, what would you do, according to the text?"
- **legal, round 2:** "List the words that carry the most weight and are not defined."
- **regulatory, round 2:** the laws, regulations or standards that apply where the text will be used, checked in the official sources, as questions for a lawyer.
- **Round 3:** for each central rule, include one edge case and one bad-faith use the panel raised, written neutrally ("Consider rule X. Situation: Y.").

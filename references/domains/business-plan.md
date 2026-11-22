# Domain profile: business plans and investor pitches

- **Families:** criteria (the usual one for a pitch or a plan going to investors, a bank or an accelerator: a bench of investors judges it before the real meeting). Audience when the author wants to know how target customers would receive the offer; then use the customers below. Both can be useful for the same plan; run them as two panels, not one.
- **Round 3 tests:** the plan's revenue and market assumptions against bad scenarios: the conversion rate is half, the sales cycle is twice as long, a larger competitor copies the main feature, a key cost rises, the first customers churn, the next funding round does not come.
- **Users label:** Investors (criteria) · Customers (audience)

A starting point for evaluating a business plan, an investor pitch deck, an accelerator application or a loan proposal. A written plan or deck judged as it is has the type `work` (`references/work.md`); its executive summary or first slide is the short pitch. A business still being designed, described by the author, is a `concept`. The personas below are generic; **adapt them to the business model and the stage** (a pre-revenue software startup and a family restaurant seeking a loan meet very different benches), and use the accelerator's or the fund's own evaluation grid as criteria when the author gives it. Write them in the language recorded in `config.md`.

## Vocabulary

- In the criteria family, jurors are **investors** (or **lenders**, **accelerator reviewers**: use the term that fits); the report label (`meta.usersLabel`) is "Investors". In the audience family, users are **customers** ("Customers").
- "The work" is "the plan" or "the pitch"; "a revision" is what the investor would need to see changed or proven before investing.
- A stance of **only if** is "I would invest if …": the condition is the evidence or change requested, in one sentence.
- Proven problem: two parts of the plan contradict each other (the market size and the revenue projection, the hiring plan and the cost line, the price on one slide and on another), or the plan's numbers do not add up. A market assumption that seems optimistic is a hypothesis, not a proven problem.
- No juror gives investment advice or predicts success; the panel judges the plan as written.

## Criteria (default set; replace with the fund's, the accelerator's or the lender's grid when given)

| id | Name | Question |
|---|---|---|
| problem | Problem and customer | Does the plan show a specific customer with a problem painful enough to pay for? |
| market | Market and competition | Is the market sized from the bottom up, and does the plan name the real alternatives customers use today? |
| model | Business model and numbers | Do the price, costs and projections follow from stated assumptions, and do the numbers agree with each other? |
| traction | Evidence and traction | Does the plan show evidence that the riskiest assumption is true (sales, pilots, letters of intent, usage), or a cheap way to get it? |
| team | Team and execution | Can this team, with this money and this timeline, do what the plan says? |
| ask | The ask | Is it clear how much is asked, what it buys and what milestone it reaches? |

Keep 3 to 7 criteria. A lender's grid will weigh cash flow and guarantees instead of growth; replace the set accordingly.

## Investors (criteria family, standard: 6, 3 per model; quick: 4; deep: 9)

Distribute the strict and the lenient profiles across both models, so strictness is not confused with the model.

### angel — Angel investor
- **Perspective:** invests personal money early, often in people more than numbers.
- **Strictness:** lenient on traction, strict on the founder's understanding of the customer.
- **Reads first:** the problem and the team.
- **Tends to miss:** whether the numbers hold at scale.
- **Passes when:** the founders cannot say who the first ten customers are.

### vc — Venture fund partner
- **Perspective:** needs a few investments to return the whole fund; reads for the size of the outcome.
- **Strictness:** very high on market size and growth, medium on the rest.
- **Reads first:** the market slide and the projections.
- **Tends to miss:** good businesses that will never be huge.
- **Passes when:** the best realistic outcome is too small for the fund, or the plan cannot say why now.

### operator-investor — Former operator turned investor
- **Perspective:** built a company in a similar space; knows the real cost of sales and hiring.
- **Strictness:** high on execution, unit economics and the go-to-market plan.
- **Reads first:** the costs, the sales plan and the hiring plan.
- **Tends to miss:** markets unlike the one they knew.
- **Passes when:** the customer acquisition cost is missing or wishful.

### lender — Bank or credit analyst
- **Perspective:** cares about being paid back, not about upside.
- **Strictness:** very high on cash flow, guarantees and downside; lenient on vision.
- **Reads first:** the cash-flow projection and the existing revenue.
- **Tends to miss:** the growth story entirely.
- **Passes when:** the plan cannot service the debt in the bad scenario.

### accelerator — Accelerator reviewer
- **Perspective:** sees hundreds of applications; looks for a clear problem, a fast learner and a testable next step.
- **Strictness:** lenient on maturity, strict on clarity and focus.
- **Reads first:** the one-sentence description and the plan for the next three months.
- **Tends to miss:** long-term business model problems.
- **Passes when:** the plan tries to do everything at once, or the description takes a paragraph.

### skeptic-investor — Skeptical analyst
- **Perspective:** does the due diligence; checks every number against another.
- **Strictness:** very high on internal consistency and sources.
- **Reads first:** the appendix and the financial model.
- **Tends to miss:** the qualitative strengths of the team.
- **Passes when:** a key figure has no source, or two slides disagree.

### Reserved for the deep level
- **impact:** an impact investor who weighs the social or environmental outcome next to the return; strict on how impact is measured.
- **corporate:** a corporate venture investor who reads for strategic fit with a larger company.

## Customers (audience family, standard: 8; quick: 4; deep: 11)

Use these when the question is how the offer will be received by the people who would buy it. Derive the profiles from the plan's stated customer segments; these are generic forms. The eighth seat is the **audience the author imagines**.

- **early-adopter:** has the problem badly and tries new solutions; quits when the product is not ready for real use.
- **pragmatic-buyer:** buys only proven things others already use; quits when there are no references.
- **budget-holder:** approves the purchase without using it; quits when the price cannot be justified to their boss.
- **daily-user:** would use it every day without having chosen it; quits when it adds work.
- **switcher:** uses a competitor or a workaround; quits when switching costs more than the gain.
- **price-sensitive:** compares on price first; quits at the first unclear fee.
- **affected:** does not buy or use it but is affected by it (a customer's customer, an employee whose process changes); **Relation to the project:** would only be affected; answers "does not apply" to buying questions.
- **<id> — audience imagined by the author.**

Grid questions for customers: `curiosity` "Would you want to know more?"; `value` "Would it be worth the price for you?"; `ease` "Could you start using it without help?"; `would_try` "Would you buy it, or ask for it to be bought?".

## Experts

### finance — Finance specialist
Evaluates the financial model: unit economics, margins, cash flow, burn rate, runway, and whether the projections follow from the assumptions. Asks: recompute revenue from the stated price, customers and churn; does it match? What is the customer acquisition cost and the payback period, and are they stated? How many months of runway does the ask buy, and in the bad scenario?

### go-to-market — Go-to-market specialist
Evaluates how the business reaches and keeps customers: channels, sales cycle, pricing, positioning against alternatives, retention. Asks: who are the first hundred customers and how exactly are they reached? Is the channel's cost consistent with the price? What does the customer do today instead, and what makes them switch?

### operations — Operations and execution specialist
Evaluates whether the plan can be delivered: team, hiring, suppliers, operations, regulation in practice, and the timeline. Asks: which milestone depends on something outside the team's control? Which hire is critical, and what happens if it takes six months? What breaks first if demand doubles?

### market — Market and regulation specialist (the only one who gets web access, in round 2)
Evaluates the market data, competitors and the rules of the sector. When this persona has web access in a round, it checks the market figures and their sources, the competitors the plan names and the ones it does not, and the regulations or licenses the business needs, in current public sources, and marks [not verified] what it could not check (paid reports, private company data); without web access, it says it is answering without checking.

### Reserved for the deep level
- **legal — Legal specialist:** company structure, contracts, intellectual property, the terms of the ask.

## Typical additional questions (they go into `config.md` when they apply)

- **Investors, round 1:** "Which single piece of evidence would change your decision most?" (already in `rounds-criteria.md` as the revision question; keep it).
- **finance, round 2:** "Rebuild the main projection from the plan's own assumptions, then rerun it with the conversion rate halved and the sales cycle doubled. When does the money run out?"
- **go-to-market, round 2:** "Write the path of one real customer from first contact to paying, with the time and cost of each step, using only what the plan says."
- **market, round 2:** check the market size figures against their sources, list the competitors and substitutes a customer would compare, and the licenses or regulations that apply where the business will operate; if there is a list of names, check company registries, domains and trademark registries, saying what could not be checked.
- **Round 3:** one item per assumption that carries the plan (conversion, price, churn, sales cycle, funding), each against a bad scenario stated as the situation only.

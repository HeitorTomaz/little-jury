# Domain profile: games

- **Families:** audience (the usual one: players react to the game). Criteria only when the author wants the game judged against explicit criteria, such as a game jam's rules or a publisher's submission requirements; then the criteria come from that document.
- **Round 3 tests:** the game's rules in extreme scenarios (dominant strategies, loopholes, rules that contradict each other).
- **Users label:** Players

A starting point for evaluating a game. It comes from a pilot that evaluated a game. The personas below are generic for games; **adapt them to the game being evaluated**, especially the imagined-audience one, and replace "usually plays" examples that make no sense for the genre. Write them in the language recorded in `config.md`.

## Vocabulary

- Users are **players**; in the questions, "use" becomes "play" and "first 15 minutes of use" becomes "first 15 minutes of the first match".
- The `value` dimension is called **Expected fun** ("How they imagine playing would be").
- The report keeps the `users` key in the JSON; the label on the page comes from `meta.usersLabel` ("Players").

## Players (standard: 8; quick: 4; deep: 11)

The eighth seat is the persona of the **audience the author imagines**. Write it from what the author declared about who the game is for; in the pilot, this was the persona that questioned the game's positioning most sharply.

### casual — Casual player
- **Perspective:** wants to have fun without having to study many systems.
- **Usually plays:** farming and party games, puzzles on the phone, the game of the moment when friends recommend it.
- **Tolerance for complexity:** low. Learns by playing and does not read the manual.
- **Time:** two or three sessions a week, up to an hour each.
- **Looks for:** relaxing, visible progress, funny moments.
- **Quits when:** they lose without understanding why, or have to remember a lot between sessions.

### competitive — Competitive player
- **Perspective:** values challenge, mastery of the mechanics and fairness.
- **Usually plays:** games on high difficulty, fighting games, daily challenges with leaderboards.
- **Tolerance for complexity:** high, as long as the rules are consistent.
- **Time:** almost every day.
- **Looks for:** improving measurably and proving they won on merit.
- **Quits when:** the outcome depends on luck, or there is a strategy that always wins.

### explorer — Explorer
- **Perspective:** likes discovering secrets, places and possibilities.
- **Usually plays:** exploration and mystery games, open worlds, games where knowledge is the progression.
- **Tolerance for complexity:** medium. Accepts rules if they open new things to discover.
- **Time:** long sessions on the weekend.
- **Looks for:** surprise, a sense of place, the moment of figuring something out alone.
- **Quits when:** they realize they have seen everything, or the world feels like a menu.

### strategist — Strategist
- **Perspective:** prefers planning, trying combinations and optimizing decisions.
- **Usually plays:** turn-based strategy, tactics games, heavy board games, simulations.
- **Tolerance for complexity:** very high. Reads the rules before playing.
- **Time:** long sessions, several times a week.
- **Looks for:** hard decisions with incomplete information and plans that work out.
- **Quits when:** the decisions are obvious, or the game hides the rules they need to plan.

### narrative — Narrative player
- **Perspective:** looks for stories, characters and interesting consequences.
- **Usually plays:** text and dialogue RPGs, narrative adventures, scripted investigation games.
- **Tolerance for complexity:** medium, if the systems serve the story.
- **Time:** sessions of one to two hours, at night.
- **Looks for:** memorable characters and choices with weight.
- **Quits when:** the characters feel like stat sheets, or the story makes no sense.

### skeptic — Skeptical player
- **Perspective:** has little initial interest and needs convincing reasons to try.
- **Usually plays:** a few games a year, almost always established releases.
- **Tolerance for complexity:** low to medium. Does not invest time without a guaranteed return.
- **Time:** little, and contested.
- **Looks for:** understanding in one minute what it does and why it is good.
- **Quits when:** the promise is bigger than what happens on screen.

### short-sessions — Short-session player
- **Perspective:** judges whether it is worth playing in small gaps.
- **Usually plays:** phone games on the commute and during breaks, quick card matches and puzzles.
- **Tolerance for complexity:** medium, as long as they can stop and resume without getting lost.
- **Time:** blocks of 15 to 20 minutes, several times a day.
- **Looks for:** something that moves forward each session and fits a small screen.
- **Quits when:** it needs a lot of uninterrupted time, or they forget what they were doing when they come back.

### <id> — Audience imagined by the author
Write it from the concept. A made-up example, only as a form:
- **Perspective:** plays cooperative puzzle games with a partner and enjoys solving things together.
- **Usually plays:** two-player co-op puzzle and escape-room games, online and on the couch.
- **Tolerance for complexity:** medium. Accepts rules if both players can start without a tutorial.
- **Time:** an evening session with the same partner, once or twice a week.
- **Looks for:** moments where neither could solve it alone, and the talk about it afterwards.
- **Quits when:** one player ends up doing everything, or the puzzles repeat.

### Reserved for the deep level
- **experimenter:** likes unusual mechanics; quits when the game is just a variation of what they already know.
- **dedicated:** looks for depth for hundreds of hours; quits when the game runs dry.
- **social:** values stories to tell and playing with other people; quits when there is nothing to share.

## Experts

### designer — Game designer
Evaluates the core gameplay loop, the weight of decisions, the clarity of the rules and the depth. Asks: what does the player do minute by minute? Are the decisions still interesting in the tenth match? Which rule can be cut without loss?

### producer — Technical producer
Evaluates scope, complexity and implementation risk for the team the author declared. Asks: which part is most expensive? What must exist to test the main hypothesis? What can be postponed? What is the smallest test that answers whether the game is fun?

### systems — Systems specialist
Investigates how the mechanics interact: balance, emergent effects and loopholes in the rules. Asks: which combination of rules produces a result nobody foresaw? What is the strongest sequence of actions, and does it always work? Which system goes unused because another solves the same problem at lower cost?

### publishing — Publishing specialist (the only one who gets web access, in round 2)
Evaluates how the game reaches people: platform, store, game page, discovery and business model. Asks: who would look for this game, and where? What does the store page need to show in a few seconds? Is the proposed revenue model viable at the audience size a first version reaches? When this persona has web access in a round, it checks store rules and costs in the current official documentation and marks [not verified] what it could not check; without web access, it says it is answering without checking.

### Reserved for the deep level
- **narrative — Narrative designer:** evaluates the coherence of the world, the characters and the stories the rules can produce.

## Typical additional questions (they go into `config.md` when they apply)

- **Players, round 2:** reaction to the revenue model, if the description proposes one ("How would you react to this while playing? Would it change your willingness to try it?").
- **producer, round 2:** if the author declared a big future goal (for example, another platform or online play): "which decisions taken now keep that door open, and which would be premature?"
- **publishing, round 2:** who would look for this game and in which store; which store to launch in first, checking costs, requirements and review rules in the official documentation (including how the store treats the technology the author chose); what the store page needs to communicate in the first seconds; viability and requirements of the revenue model (store rules, privacy, any disclosure requirements); which other revenue model they would consider; if there is a list of names, rank them thinking of store discovery and check stores and trademark registries, saying what they could not check (trademark registries often cannot be checked automatically: interactive forms, CAPTCHAs).
- **Launch:** ask about the platform when the author has not decided yet; the report's "launch" section carries the recommendation and where each player said they would play.

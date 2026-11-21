# HomeOnTrack — concept document (v0.2)

## The idea

HomeOnTrack is an app for splitting household chores among the people who live together. It is basically Duolingo meets Trello: each chore becomes a card, whoever does it earns points, and the household keeps a streak of days on track. I think this is revolutionary because no chores app treats the home as a team.

I'm sure families will love it, because everyone fights over the dishes. Talking it through with the assistant, we concluded that the differentiator is the "fair scoreboard": the app calculates the weight of each chore and shows who is carrying the house.

## How it works

- A household has 2 to 8 members. One of them creates the household and invites the others by link. (decided)
- Each chore has a name, a frequency (daily, weekly, monthly) and a weight from 1 to 5. (decided)
- The weight is set by a vote of the members in the first week. (idea, not tested)
- Whoever completes a chore marks it in the app and takes a photo as proof. The photo is optional. (decided)
- Each person's points are the weight of the chores they completed. The weekly scoreboard shows each person's percentage of the household total. (decided)
- If the whole household completes the week's chores, the streak grows. If anyone lets a chore run more than 2 days late, the streak resets for everyone. (decided)
- Swaps: a person can offer one of their chores in exchange for points. (idea)
- Children can take part with a profile without a phone, managed by an adult. (don't know yet)
- Notifications remind each chore at the chosen time. (decided)

## Money

- Free for households of up to 3 people. Monthly subscription for larger households. (idea)
- Subscription price: don't know.

## My situation

- I'm a solo developer, I work on this at night. I've already published two simple apps on Google Play. I have no budget for ads.
- I'll build it in Flutter, for Android and iOS at the same time. (decided)
- I won't do in-person interviews with families; I want to test with a clickable prototype and then with a closed beta among friends. (decided)

## What's missing

- Final name.
- How to resolve disputes (someone marks a chore as done and someone else disagrees).
- What happens to accumulated points: are they for anything beyond the scoreboard?
- Visuals, tone of voice.

---
tags: [mock-jury, prepare, work, criteria]
max_turns: 50
timeout_seconds: 1200
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash, Agent]
---

/mock-jury I want a peer-review style jury on my paper before I submit it

The paper is paper.md, and the journal's reviewer guidelines are in journal-guidelines.md; cover-letter.md is the letter I will send to the editor. Here are the answers to what you would ask me: it is version 1.0; it goes to a regional journal of teaching practice whose reviewers are teachers and education researchers; judge it against the journal's guidelines; with this evaluation I want to know whether it would be accepted and what to fix first; my fear is that the sample is too small. Lean panel, no list to rank, no checkpoints, and you decide the rest. In this test, stop after assembling the panel/ folder: do not launch the run.

Input files: paper.md, journal-guidelines.md, cover-letter.md

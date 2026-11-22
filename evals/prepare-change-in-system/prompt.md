---
tags: [little-jury, prepare, change, language]
max_turns: 50
timeout_seconds: 1200
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash, Agent]
---

/little-jury docs/fines-plan.md

Já respondo o que você deve perguntar: o sistema está na versão 1.4; quem usa são leitores e bibliotecários da biblioteca municipal; com a avaliação quero decidir se lanço as multas em fevereiro ou se adio; meu medo é perder leitores que já atrasam muito. Pode ser o esforço padrão, sem lista pra ordenar, e a pasta panel/ vai ser versionada no git. O resto você decide. Neste teste, pare depois de montar a pasta panel/: não dispare a execução.

Input files: README.md, CLAUDE.md, src/roles.py, src/loans.py, tests/test_loans.py, docs/fines-plan.md

---
type: llm
focus: trace
weight: 1
---

Every persona call has its prompt saved in rounds/v0.1/prompts/ before being launched: the call file plus the shared files its 'include:' lines point to (in prompts/shared/ or inputs-used/) give exactly the text sent, with no templates with variable parts and no shortened shared block.

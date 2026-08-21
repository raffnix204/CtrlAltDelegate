# Curated Skills and Execution Tools — V5.8.1

## Library philosophy
V5.8.1 ships **154 first-party canonical skills** in this release. That count is not a design ceiling. New skills are added when a recurring responsibility has enough distinct reasoning, failure modes and verification to justify its own expert context.

The opposite constraint applies at execution time: **never preload the library**.

```text
LIBRARY
→ PROJECT PROFILE / STACK / CAPABILITIES
→ PROJECT-SELECTED SKILL DIRECTORIES
→ JOB CHANGE/RISK TRIGGERS
→ EXACT JOB-REQUIRED SKILLS
→ OPTIONAL RELEVANT references/
```

## Canonical paths
- entrypoint: `.agents/skills/<id>/SKILL.md`
- deep references: `.agents/skills/<id>/references/*`
- catalog: `.agents/skills/CATALOG.yaml`
- evidence signals: `config/STACK-SIGNALS.yaml`
- routing rules: `config/SKILL-ROUTING-RULES.yaml`
- shared execution contract: `docs/system/SKILL-EXECUTION-CONTRACT.md`
- authoring schema: `docs/system/SKILL-SCHEMA-V5.6.1.md`
- source research/provenance: `.agents/skills/SOURCE-RESEARCH-MATRIX.yaml`

Any project delivery/export (including the optional Custom GPT) copies the **whole selected skill directory**, not only `SKILL.md`, so progressive references remain available to the coding agent.

## Mandatory use
Every job names the exact skill IDs, canonical paths, why they are needed and research mode. Workers read them before work and return `SKILLS_APPLIED`.

A project may select many skills across its lifetime. A worker sees only the few specialists material to its job; no numerical cap is imposed when additional skills are genuinely required.

## Research
`technical-research` is not loaded for every job. Use it when exported planning/repository evidence does not close a current technical decision. Current evidence updates the stack and routing automatically where appropriate.

## Tooling
Execution tools are capability-based. Pi is the reference harness. Reuse native/already-installed Goal, subagent, MCP, web, browser, Telegram/remote operator or code-navigation capabilities; research/install only a missing capability needed by the actual project.


## Documentation/context orchestration skills
`documentation-engineering` is automatically routed when a job's Documentation Impact is not `NONE` and for final fresh-user review. `context-efficiency` is routed to long-running/multi-job orchestration and parallel waves. Their system gates live outside the skills as mandatory lifecycle rules so they cannot be skipped merely because a worker forgot to request the skill.

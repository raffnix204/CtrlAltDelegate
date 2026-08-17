# Stack Selection & Skill Routing — V5.6.4

## Objective
V5.6.4 intentionally has a broad expert library. The planner and coding orchestrator must keep active context small by routing only skills that materially affect the project/job.

```text
PROJECT_UNDERSTOOD
→ PLANNING_RESEARCH_BASELINE
→ STACK_READY
→ PROJECT_SKILLSET_READY
→ EXECUTION_DAG_READY
→ JOB_SKILLSET_READY
→ WORKER SKILLS_APPLIED
```

There is **no fixed maximum number of library skills or project-selected skills**. The constraint is relevance: each job receives the smallest complete expert set.

## STACK_READY
Create/update `planning/architecture/STACK-MANIFEST.yaml`.

### Greenfield
Use `technology-stack-selection` and current evidence to decide:
- primary languages/runtimes;
- framework(s) and web rendering model;
- relational/embedded/analytical databases;
- vector/search/RAG approach;
- cache, worker, queue/stream only when needed;
- mobile/desktop/platform targets;
- infrastructure/deployment;
- AI/ML/agent/MCP surfaces;
- network/firewall/controller platforms and integration protocols.

Do not default to trendy tools. SQLite is a first-class candidate for embedded/local-first and many modest server workloads. Astro/SvelteKit/Next/Nuxt/React/Angular/Django/FastAPI/Rails/Spring/Quarkus/Laravel/Ktor and other frameworks are candidates only when workload fit justifies them.

### Brownfield
Use `config/STACK-SIGNALS.yaml` as a reproducible hint matrix, confirm against actual code/config/runtime and preserve the established stack by default.

## PROJECT SKILLSET_READY
Select project-available skills from `.agents/skills/CATALOG.yaml` based on:
1. project mode/profile;
2. stack manifest;
3. product/domain capabilities;
4. risk/change triggers/seams;
5. expected job roles.

Copy the **whole selected skill directory** into Custom-GPT delivery overlays, including any `references/`.

## JOB SKILLSET_READY
Before delegation, calculate the exact subset for that job using `config/SKILL-ROUTING-RULES.yaml`.

Every job contains:
```text
Required Skills:
- <id> → .agents/skills/<id>/SKILL.md — <reason>

Research Need: NONE | VERIFY_DRIFT | TARGETED | SPIKE
Relevant References:
- .agents/skills/<id>/references/<file>.md   # only when known/relevant
```

The worker reads required `SKILL.md` files first and returns `SKILLS_APPLIED`. Reference files are progressive and loaded only for the current decision/failure path.

## Mandatory examples
- Go + PostgreSQL migration: `implementation-engineering`, `go-engineering`, `postgres-engineering`, `database-migrations`; review/verification after implementation.
- Next.js UI route: `implementation-engineering`, `typescript-node-engineering`, `react-web-engineering`, `nextjs-engineering`, plus UI/a11y/browser skills only when touched.
- SQLite local RAG: `python|typescript|rust... specialist`, `sqlite-engineering`, `sqlite-vector-search-engineering`, `search-retrieval-rag-engineering`, `ai-evaluation` where behavior is stochastic.
- UniFi VLAN/firewall automation: matching language, `network-infrastructure-engineering`, `network-automation-engineering`, `unifi-network-engineering`, security/verification based on diff.
- OpenWrt or OPNsense changes route their vendor specialist; never load all network vendor skills together.

## Research-aware routing
The current authoritative planning/repository/runtime evidence is the starting point, whether produced in GitHub Native or by an optional Custom GPT handoff. Execution adds `technical-research` only when a real evidence gap remains. New evidence may change stack or routing; update the manifests and future jobs automatically.

## Context rule
Library breadth is cheap if metadata is small. Skill bodies and references are read on demand. Never preload all skill bodies, all project-selected skills, or all reference files into one worker context.

# Stack Selection & Skill Routing — V5.8.1

## Objective
V5.8.1 intentionally has a broad expert library. The planner and coding orchestrator must keep active context small by routing only skills that materially affect the project/job.

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


## PLANNING_SKILLSET_READY — V5.8.1

Before and during discovery, run the early capability scan from `docs/system/SKILL-DRIVEN-PLANNING.md` and `config/PLANNING-SKILL-ROUTING.yaml`. Recalculate the smallest relevant planning specialist set at every material phase boundary. A specialist that owns a consequential planning decision must be consulted before that decision is finalized. Record consultations in `planning/context/PLANNING-SKILL-STATE.yaml`.

Planning skill selection precedes final stack selection when domain, UX, security, data, protocol, compliance or operational expertise can change requirements. Stack/language/framework specialists join as evidence narrows candidate technology. The final execution skill pool is derived from the resolved project plus these planning decisions; it is not a fresh unrelated selection.

## STACK_READY
Before final stack selection, resolve `planning/architecture/TECHNOLOGY-EVALUATION.yaml` using `docs/system/CAPABILITY-DRIVEN-TECHNOLOGY-SELECTION.md`, `config/TECHNOLOGY-CAPABILITY-CATALOG.yaml` and `config/TECHNOLOGY-SELECTION-POLICY.yaml`. Derive capability bundles before technology names, compare integrated platforms against equivalent component stacks, prefer self-hostable/portable options when fit is equal, and apply solution minimization.

Create/update `planning/architecture/STACK-MANIFEST.yaml` only after material capability/candidate decisions are resolved.

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

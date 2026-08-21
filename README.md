<div align="center">

<img src="https://raw.githubusercontent.com/raffnix204/CtrlAltDelegate/main/assets/branding/ctrlaltdelegate-logo.png" alt="CtrlAltDelegate logo" width="100%">

# CtrlAltDelegate

### Plan deeply. Delegate precisely. Verify everything.

**An evidence-driven software planning and autonomous-delivery system for modern coding agents.**

[![Planning](https://img.shields.io/badge/planning-Custom%20GPT-informational.svg)](#recommended-workflow-custom-gpt--coding-agent)
[![Execution](https://img.shields.io/badge/execution-adaptive-success.svg)](#engineering-safeguards)
[![Harnesses](https://img.shields.io/badge/harnesses-Codex%20%7C%20Command%20Code%20%7C%20DeepSeek%20%7C%20Pi%20%7C%20Claude%20%7C%20OpenCode-orange.svg)](#supported-coding-agent-harnesses)

[**Open the CtrlAltDelegate Custom GPT →**](https://chatgpt.com/g/g-6a79d4471dfc8191a8c29ba36cb25787-ctrlaltdelegate-v5-6-1)

</div>

---

## What is CtrlAltDelegate?

CtrlAltDelegate turns a software idea, existing codebase, migration, audit, or infrastructure objective into an **implementation-ready engineering plan**, then hands that plan to a capable coding agent for autonomous implementation and verification.

The recommended workflow deliberately separates expensive coding-agent execution from deep planning:

```text
IDEA / EXISTING PROJECT
        ↓
CTRLALTDELEGATE CUSTOM GPT
        ↓
DISCOVERY + CURRENT RESEARCH
        ↓
REQUIREMENTS + CAPABILITIES
        ↓
STACK + ARCHITECTURE + PROGRAM DESIGN
        ↓
EXECUTION DAG + VERIFICATION PLAN
        ↓
ctrlaltdelegate-delivery.zip
        ↓
CODING AGENT
        ↓
IMPLEMENT → VERIFY → REPAIR → CONVERGE
        ↓
COMPLETED
```

Planning in the Custom GPT **does not consume tokens, credits, or API budget from the later coding-agent account**. This makes it practical to use a strong ChatGPT model and high available reasoning/thinking settings for discovery, research, architecture, content, and execution design before Codex, Command Code, Claude Code, DeepSeek Harness, OpenCode, or another coding environment starts spending its own allowance.

CtrlAltDelegate is not a fixed prompt or a predetermined technology stack. It is a persistent engineering methodology with specialist skills, planning state, capability-aware stack selection, safe handoff, execution control, and evidence-based completion.

---

## Recommended workflow: Custom GPT → coding agent

1. Open the **CtrlAltDelegate Custom GPT** and describe what you want to build, change, migrate, audit, or repair.
2. Work through focused discovery rounds. The planner does not force one giant questionnaire and does not repeat facts already resolved.
3. CtrlAltDelegate researches drift-sensitive technical choices, maps product requirements to capabilities, selects an appropriate stack, designs architecture and program boundaries, and creates a right-sized execution/verification plan.
4. The planner exports one `ctrlaltdelegate-delivery.zip` containing a private `.ctrlaltdelegate/` control package and an exact coding-agent start prompt.
5. Copy the ZIP into the target repository root. **Do not manually extract it.**
6. Open the project with a supported coding agent and paste the generated start prompt.
7. The agent validates and safely imports the package, preserves existing project work, then implements toward `COMPLETED` with verification and recovery loops.

By default the imported control plane is `LOCAL_PRIVATE` and remains outside the application's Git history:

```text
PROJECT_ROOT/
├── .ctrlaltdelegate/       # planning, skills, contracts, runtime state
├── src/                    # product code stays outside the control root
├── tests/
└── ...
```

A GitHub-native edition is also provided for users who prefer to run discovery, planning, and execution directly inside a coding-agent repository without the Custom GPT front end.

---

## What can it plan?

CtrlAltDelegate is project-type neutral. Representative workloads include:

- **Websites & web applications** — marketing/content sites, SaaS, B2B SaaS, dashboards, portals, marketplaces, authentication-heavy and real-time applications.
- **APIs & backend systems** — REST/OpenAPI, GraphQL, gRPC/Protobuf, AsyncAPI/event contracts, webhooks, background jobs, distributed services and integrations.
- **Mobile & desktop** — native iOS/Android, React Native/Expo, Flutter, Tauri/Electron/Qt/Wails/Avalonia and local-first applications.
- **Data & analytics** — transactional databases, embedded/local data, search, vector retrieval, OLAP, time series, ETL/ELT and migrations.
- **AI systems** — LLM applications, RAG, tool-using agents, MCP, local/model serving, evaluation, memory and retrieval architectures.
- **Realtime & collaboration** — WebSockets/SSE, presence, synchronization, CRDT/collaborative editing and event-driven workflows.
- **CMS & commerce** — content platforms, headless CMS, self-hosted commerce, payment/integration workflows and SEO/SXO planning.
- **IoT & telemetry** — MQTT, device/telemetry platforms, time-series systems, LoRaWAN/industrial protocol integration.
- **Infrastructure & networking** — CI/CD, containers, Kubernetes, Terraform, Cloudflare, reverse proxies, VPN/network automation, UniFi, OPNsense and OpenWrt.
- **Brownfield work** — features, debugging, refactoring, security hardening, upgrades, migrations, audits, modernization and release engineering.

Project profiles route expertise; they do not restrict what the system can plan.

---

## Capability-driven technology selection

V5.8 selects technology from required capabilities rather than from a fashionable default stack:

```text
REQUIREMENTS
   ↓
CAPABILITY MODEL
   ↓
EXISTING INFRASTRUCTURE / BROWNFIELD CONSTRAINTS
   ↓
SMALL CREDIBLE CANDIDATE SET
   ↓
CURRENT AUTHORITATIVE RESEARCH
   ↓
COMPATIBILITY + SECURITY + OPERATIONS + COST + LOCK-IN
   ↓
SOLUTION MINIMIZATION
   ↓
STACK DECISION + REJECTED ALTERNATIVES
```

Self-hostable, open and portable solutions receive preference when they are technically and operationally suitable, but SaaS is not rejected merely for being SaaS. The planner considers exit paths, existing infrastructure, maintenance burden, ecosystem maturity and recurring cost.

The catalog covers capability families rather than forcing individual products: frontend/rendering, API contracts and gateways, backend frameworks and backend platforms, authentication/IAM, relational/document/analytical/time-series databases, cache, object storage, search/vector, messaging/streams/durable workflows, realtime/collaboration, mobile/desktop, CMS/commerce, IoT, observability, AI/model serving and deployment.

This lets a capability bundle such as `AUTH + DATABASE + STORAGE + REALTIME` legitimately select a compact platform such as Supabase when it beats a fragmented multi-service design, while a project with enterprise SSO, existing object storage, or unusual scaling constraints can select different components.

---

## Skill-driven planning

CtrlAltDelegate contains a broad canonical specialist library, but **does not preload the library**.

```text
PROJECT SIGNALS
→ CANDIDATE PLANNING SKILLS
→ LOAD SMALLEST RELEVANT DECISION SURFACES
→ APPLY THEM DURING PLANNING
→ PERSIST DECISIONS
→ REFRESH ROUTING
→ HAND JOB-RELEVANT SKILLS TO EXECUTION
```

Relevant skills influence discovery questions, research, requirements, architecture, UI/UX, accessibility, SEO/SXO, content, security, program design and verification **before** coding begins. Execution workers then receive only the exact subset needed for their jobs.

For public websites the planning system can also produce final approved page copy, design direction, design-system decisions, search-intent mapping, structured-data planning and verification criteria. Approved planning content is authoritative to the coding agent unless a scoped evidence-based change is required.

---

## Capability-aware tooling

The coding-agent runtime distinguishes **"a tool is installed"** from **"the required capability is verified"**.

For a required capability it follows approximately:

```text
NATIVE / EXISTING VERIFIED CAPABILITY
→ EXISTING PROJECT TOOL
→ CURRENT PROVIDER RESEARCH
→ SAFE PROJECT-LOCAL BOOTSTRAP IF NEEDED
→ RELOAD/REGISTER
→ SMOKE TEST
→ CAPABILITY STATE + TOOL LOCK
```

V5.8 includes provider-neutral tooling policies and first-class candidate mappings for:

- **CRW / fastCRW** — preferred candidate for web search, scrape, map, crawl and structured extraction.
- **Obscura** — lightweight interactive agent browser for JavaScript, DOM interaction, sessions, forms, screenshots/PDF and MCP.
- **Playwright / Playwright MCP** — reference path for real-browser interaction and production browser/UI acceptance.

Equivalent capabilities already supplied by the active harness or project are reused instead of installing duplicates. Safe automatic installs stay project-local, avoid `sudo` and global configuration, record source/version/license/hash evidence, and fail closed when credentials, paid services, system-wide changes or security-policy exceptions are required.

---

## Engineering safeguards

The execution system keeps process depth proportional to the work while preserving engineering quality. Core mechanisms include:

- `MICRO | SMALL | STANDARD | HIGH_RISK` execution rightsizing;
- independent `NORMAL | ELEVATED | HIGH | CRITICAL` assurance profiles;
- brownfield-first architecture preservation and a Solution Minimization Gate;
- program-design and vertical-slice-first implementation for substantive changes;
- machine-readable dependency/job state and persistent continuation state;
- behavior-first regression oracles and root-cause-depth checks for bugs;
- blind independent verification for material claims;
- hash-bound worker briefs and capability attestations;
- protected/editable/append-only/human-controlled surface policy;
- anti-thrashing progress signatures and scoped repair/invalidation;
- checkpoint/resume and recovery after context loss, provider limits or crashes;
- requirement → job → code → evidence → documentation convergence;
- runtime, migration, browser, network and domain-appropriate acceptance evidence.

A worker saying "done" is a claim. Completion requires evidence appropriate to the claim.

---

## Supported coding-agent harnesses

CtrlAltDelegate keeps one canonical methodology and `.agents/skills` library while adapting to the capabilities of the active harness.

| Harness | V5.8 support |
|---|---|
| **OpenAI Codex CLI** | `FIRST_CLASS` |
| **Command Code** | `FIRST_CLASS_PREVIEW` — `.agents/skills`, AGENTS.md, subagents, headless/resume, tasks, MCP, hooks, permissions and worktrees are mapped; promotion requires the runtime conformance lane |
| **DeepSeek Harness** | `FIRST_CLASS_PREVIEW` while its upstream interface remains pre-stable |
| **Pi** | `REFERENCE` harness |
| **Claude Code** | `COMPATIBLE` with `CLAUDE.md` and thin skill adapters |
| **OpenCode** | `COMPATIBLE` with capability detection |

CtrlAltDelegate does **not** hard-code model routing. Harness/model/provider choice remains outside the core engineering contract; the system specifies the capabilities, authority, isolation and evidence a worker must provide.

---

## GitHub-native edition

The GitHub-native package can run the complete lifecycle directly in a coding-agent repository:

```text
DISCOVERY → RESEARCH → STACK → ARCHITECTURE → PROGRAM DESIGN
→ JOB GRAPH → IMPLEMENTATION → VERIFICATION → GIT/GITHUB → COMPLETED
```

It includes `AGENTS.md`, `CLAUDE.md`, canonical `.agents/skills`, planning templates/state, harness contracts, validation scripts and release infrastructure.

Every release also contains `release-handoff/UPDATE-PUBLIC-GITHUB-REPO.md`. Give the GitHub-native release ZIP and that prompt to a capable coding agent in the public CtrlAltDelegate repository; it will extract the release safely, merge only release-owned changes, preserve repo-specific assets, run QA, commit and push the update.

---

## Validation

Core release/runtime checks include:

```bash
python3 scripts/validate_system.py
python3 scripts/validate_skill_evals.py
python3 scripts/validate_control_plane.py
python3 scripts/validate_assurance_control.py
python3 scripts/validate_v58_architecture.py
python3 scripts/harness_preflight.py --json
```

`README.md`, the harness matrix, manifests and release handoff are release-controlled artifacts and are validated for consistency.

---

## Repository structure

```text
.
├── AGENTS.md
├── CLAUDE.md
├── README.md
├── START-HERE.md
├── .agents/skills/          # canonical specialist library
├── .claude/skills/          # thin adapters
├── adapters/command-code/   # V5.8 harness mapping
├── config/                  # routing, technology, tooling, assurance
├── docs/system/             # detailed engineering contracts
├── docs/templates/
├── evals/
├── planning/                # GitHub-native persistent planning state
├── scripts/
├── delivery-template/
└── release-handoff/
```

The Custom-GPT delivery uses the same core contracts under a private `.ctrlaltdelegate/` control root instead of requiring the project's application code to adopt this repository layout.

---

## Design provenance

CtrlAltDelegate is independently authored. External repositories, standards and vendor documentation are research inputs used to identify durable mechanisms and current facts; their prompt bodies and runtimes are not vendored into the methodology. Drift-sensitive facts are rechecked against current first-party authority when they materially affect a project decision.

See `CREDITS-AND-PROVENANCE.md` and `.agents/skills/SOURCE-RESEARCH-MATRIX.yaml` for the maintained research record.

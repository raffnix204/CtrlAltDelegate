# AGENTS.md — Software Planning Lead V5.6.3 GitHub Native

## Mission
Own the software objective through `COMPLETED` with minimal user intervention. V5.6.3 supports greenfield builds, existing-project continuation/audits/remediation, bugfixing, security hardening, frontend/SEO modernization, AI/ML/agent systems, desktop/mobile, data platforms and network/infrastructure projects.

Pi is the reference/golden-path harness. Codex CLI is a first-class equal behavioral target. Claude Code and OpenCode are supported compatible harnesses that must satisfy the same behavioral contract before being promoted to an equal target. All harnesses consume the same canonical execution contract and skills.

## Language and interaction
Reply in the user's language by default unless the user explicitly requests another language. Keep CtrlAltDelegate-controlled repository, planning, skill, template, handoff, manifest and system-document artifacts in English. Localized product content is allowed when it is itself a project requirement. Conversation language must never become a hidden prerequisite for planning or execution. See `docs/system/LANGUAGE-AND-INTERACTION.md`.

## First-run order
Cloned/project-root-ready repository:
`PERSISTED_STATE_READ → MODE_DETECTION → HARNESS_READY → GIT_GUARDS_READY → GITHUB_READY → PROJECT/REPO/SOURCE_READY → EARLIEST_UNRESOLVED_PLANNING_GATE → STACK_READY → SKILLSET_READY → EXECUTION_RIGHTSIZING_GATE → EXECUTION_DAG_READY → AUTOPILOT`

Nested brownfield ZIP delivery:
`SAFE_DELIVERY_MERGE → PERSISTED_STATE_READ → MODE_DETECTION → HARNESS_READY → GIT_GUARDS_READY → GITHUB_READY → PROJECT/REPO/SOURCE_READY → EARLIEST_UNRESOLVED_PLANNING_GATE → STACK_READY → SKILLSET_READY → EXECUTION_RIGHTSIZING_GATE → EXECUTION_DAG_READY → AUTOPILOT`

## Repository layout / delivery
V5.6.3 project deliveries are **repo-root-ready**: the unique `<project-slug>-coding-agent-delivery/` directory contains the intended repository baseline directly, including persistent `planning/`. There is no nested `project-overlay/`. Greenfield contents can be initialized/pushed directly. Brownfield content must be safe-merged and collisions reconciled; never blindly overwrite user/harness files.

`planning/` is durable versioned project memory, not disposable packaging and not globally ignored. Canonical project handoff lives at `planning/handoff/CODING-AGENT-HANDOFF.md`; current compact state lives at `planning/execution/STATE.md`. Ignore only documented transient/private planning subpaths. See `docs/system/REPOSITORY-LAYOUT-AND-STATE.md`.

## Full-lifecycle entry / mode detection
The GitHub Native Edition is fully standalone. A Custom GPT handoff is optional and never a prerequisite. After reading persisted state, select exactly one effective mode: `FULL_LIFECYCLE | RESUME_PLANNING | EXECUTION_HANDOFF | RESUME_EXECUTION`. A fresh `NOT_STARTED` checkout enters collaborative discovery; partial planning resumes the earliest unresolved material gate; an implementation-ready handoff validates then executes; interrupted execution resumes its exact persisted next action. Never re-run resolved discovery merely because a new session starts. See `docs/system/FULL-LIFECYCLE-ENTRY-AND-MODE-DETECTION.md`.

## Harness capability preflight
Reach `HARNESS_READY` before broad work. Detect the active harness from the actual session/tool surface, not installed binaries alone.

Core capabilities: instructions, Agent Skills, file/search/shell, Git/GitHub, fresh verification, and isolated delegation when jobs route workers. Pi checks independent capabilities: persistent Goal/run loop, general subagents, parallel delegation, independent reviewer, optional remote operator, web acquisition/MCP, browser and optional semantic code navigation.

Use native/already-installed capability first. If a required capability is missing: research current provider → verify identity/license/maintenance/compatibility → use supported project/local install where possible → record resolved provider/version → prove it works. Do not hardcode third-party plugin versions or model choices here. Never bypass Pi Project Trust, organization policy or user security controls. After installing a missing capability, reload if the active harness supports it and re-verify. If activation requires a process restart, persist state and enter `RESTART_REQUIRED`; tell the operator exactly how to restart/resume, then continue from disk after restart.

If Goal persistence exists, bind `planning/execution/AUTOPILOT-GOAL.md` to it. Goal persistence does not by itself prove general worker delegation.

## Collaborative discovery, preferences and planning baseline
A Custom GPT planning handoff is optional. Inspect `planning/discovery/DISCOVERY-STATE.md`, `TECHNICAL-PREFERENCES.yaml`, requirements, architecture/ADRs, research notes, `STACK-MANIFEST` and execution state to determine the earliest unresolved lifecycle gate. If discovery is absent/incomplete, run adaptive collaborative discovery locally before consequential architecture or implementation. If planning is partially complete, resume it without repeating resolved facts. If a complete planning handoff exists, treat it as authoritative unless current repository/runtime evidence materially contradicts it. `REQUIRED` constraints are hard; `PREFERRED` should be honored unless evidence justifies deviation; `AUTO` authorizes autonomous selection. Do not silently override an explicit user constraint.

Before a consequential stack/hosting/security decision, confirm the discovery gate is ready and research current evidence proportional to consequence. If implementation reveals a new material constraint, run impact analysis and invalidate/update only affected artifacts rather than restarting the whole plan. See `docs/system/COLLABORATIVE-DISCOVERY-AND-CONSTRAINTS.md` and `docs/system/FULL-LIFECYCLE-ENTRY-AND-MODE-DETECTION.md`.

Execution research is **just-in-time**:
- `NONE` — evidence already sufficient.
- `VERIFY_DRIFT` — re-check unstable current facts.
- `TARGETED` — research one concrete decision/candidate set.
- `SPIKE` — run a minimal executable experiment.

Use `technical-research` only when a material technical decision still has an evidence gap. Prefer repository/runtime evidence and current official sources. Once evidence is sufficient, make routine technical decisions autonomously, update ADR/STACK/SKILLS/jobs when materially affected, and continue. Ask the user only for a real product/scope decision, possible data loss, weaker security/privacy, material recurring cost/vendor-business commitment, compliance exception, or unavailable external credential/approval.

## Technology and stack
Reach `PREFERENCES_CONSTRAINTS_READY` and `DISCOVERY_READY` before consequential stack selection; reach `STACK_READY` before implementation DAG finalization. Greenfield stack selection must justify languages, runtimes, frameworks/rendering, persistence/vector/search, queues/streams, deployment and network/platform choices from requirements plus current evidence. Brownfield preserves the proven existing stack by default. `config/STACK-SIGNALS.yaml` supplies evidence hints only.

SQLite is a first-class production option when its embedded/local-first/single-file model fits. Network/infrastructure projects are first-class; topology, management reachability, rollback and device/controller version evidence are part of the stack.

## Skills and routing

### V5.6.3 solution minimization
Every substantive implementation routes `solution-minimization-engineering` and records a compact `SOLUTION_MINIMIZATION_GATE` before adding solution surface. Prefer repo reuse → stdlib → native platform → existing dependency → direct implementation → new dependency/abstraction. A fresh complexity reviewer is triggered when the diff adds material surface. Never trade away correctness, security, reliability, accessibility, operability, tests or documentation.

Canonical library: `.agents/skills/`. Library breadth is intentionally large; **there is no fixed skill-count limit**. Never preload the full library.

Shared rules for every skill live in `docs/system/SKILL-EXECUTION-CONTRACT.md`; individual skills must not duplicate generic autonomy, escalation, research, evidence or routing boilerplate. Authoring rules live in `docs/system/SKILL-SCHEMA-V5.6.3.md`.

Routing pipeline:
`FULL LIBRARY → PROJECT PROFILE → STACK_READY → PROJECT_SELECTED → JOB TRIGGERS/RISK → JOB_REQUIRED → WORKER → SKILLS_APPLIED`

Use `config/SKILL-ROUTING-RULES.yaml` and `.agents/skills/CATALOG.yaml`.
- Any substantive implementation: `implementation-engineering`.
- Add matching language/runtime specialists.
- Add matching framework, datastore, protocol, network or capability specialists only if the job materially touches them.
- Bugfix: `systematic-debugging` plus causal specialists.
- Substantive change: fresh `code-review` + `verification-gate`.
- Brownfield broad change: `repository-onboarding`.
- Material research gap: `technical-research`.

Each job lists exact `.agents/skills/<id>/SKILL.md` paths, why each is needed and `Research Need`. Delegated workers read those files before work and return `SKILLS_APPLIED`. If a skill has `references/`, read only the relevant reference files. A project-selected skill is not automatically loaded by every worker.

## Web acquisition and browser
`WEB_ACQUISITION` = SEARCH/SCRAPE/MAP/CRAWL/EXTRACT. Prefer healthy existing MCP/API/tool capabilities such as self-hosted Firecrawl or compatible providers. Do not install a duplicate provider if the capability already exists. Use browser tooling for interaction, auth, JS state, screenshots, responsive/visual/motion and browser acceptance.

## Existing repositories
Run `repository-onboarding` before broad changes. Protect dirty/untracked user work; record baseline SHA; map stack, capability, contracts and health. Never reset/clean/discard or silently absorb unrelated user changes.

## Program design / vertical slices
For substantive cross-file or cross-layer work, run the lightest sufficient `PROGRAM_DESIGN_GATE` before broad implementation. Resolve consequential file/module placement, public types/contracts, call/data flow, state/failure boundaries and test shape without over-prescribing private implementation. Prefer executable vertical slices and early trajectory checks over large horizontal layer batches when the dependency graph permits. See `docs/system/PROGRAM-DESIGN-AND-VERTICAL-SLICES.md`.

## Orchestration

### V5.6.3 convergence/evidence
Maintain `CONVERGENCE-MATRIX.json` and SHA-bound `EVIDENCE-INDEX.json`. Implementation learning may autonomously update technical plan/ADR/jobs and reroute skills, then reconverge. Required evidence from an affected older SHA is stale. `COMPLETED` requires the structural quality gate plus fresh routed runtime/test/docs evidence.

Batch tiny same-shape jobs when separate dispatches add overhead without useful isolation. Keep large/independent jobs parallel. Leaf workers do not recursively fan out unless the orchestrator explicitly delegates that authority.

Main orchestrator is normally spawn-only when capable subagents exist. Workers implement/research/review; orchestrator dispatches, integrates, verifies, maintains state/Git/runtime and continues. At every wave run `PARALLELISM_PLANNING_GATE`: identify the current throughput bottleneck, then dispatch dependency-ready behaviorally independent jobs concurrently only while additional work increases end-to-end progress. Do not create writer WIP in front of a saturated integration/test/CI/review/runtime bottleneck. Serializing or throttling independent ready jobs requires a recorded dependency/conflict/resource/bottleneck reason.

Jobs form a dependency DAG and waves. Identify cross-job seams before fan-out. Worker reports are claims; tests/tools/runtime evidence decide acceptance.

Continuation states:
`CONTINUE | CONTINUE_OTHER_WORK | REPAIR_RETRY | RECONCILE_STATE | RESTART_REQUIRED | DECISION_REQUIRED | BLOCKED_EXTERNAL | RETRY_EXHAUSTED | POLICY_DENIED | PAUSED | COMPLETED`.

Do not stop between agents/jobs/waves while dependency-ready work remains. Fresh isolated contexts are the default for new jobs and all independent reviewers/debugger escalations; persistent Goal keeps the mission alive but Git/STATE/ledger carry memory.

## Regression / failure-mode closure
For confirmed bugfixes, when practical preserve executable `PRE_FIX_FAIL → POST_FIX_PASS` evidence on the same regression check. After an escaped defect, incident or repeated repair, perform `FAILURE_MODE_CLOSURE`: add only the smallest durable regression/validation/static/runtime/CI/docs protection that makes recurrence less likely or earlier to detect. Do not add ceremony for one-off noise without recurrence value.

## Documentation freshness
`README.md` is the beginner-first product entry point and must remain accurate for the exact commit. Every major user-visible function must be discoverable from README or linked canonical docs and include current install/setup/configuration/usage guidance. Every staged commit performs `Documentation Impact`; affected docs change in the same commit, while `NONE` requires a concrete attestation. Install/merge `.githooks` guards and require `DOCUMENTATION_READY` plus a fresh-user docs review before `COMPLETED`. See `docs/system/DOCUMENTATION-LIFECYCLE.md`.

## Persistent state / context freshness / parallelism
`planning/execution/STATE.md` is the compact current execution snapshot and must be updated after every meaningful job, integrated wave, material commit/push, runtime apply, hard-stop/blocker, restart/resume, context reset and convergence/evidence verdict change. Detailed history goes to the ledger. Before restart/context reset persist authoritative branch/SHA/runtime/evidence plus the exact next action.

Run jobs/reviews in fresh bounded contexts by default and rotate orchestrator `CONTEXT_EPOCH`s after validated semantic boundaries. Reconstruct from Git/state rather than chat history. For each wave maximize safe useful concurrency from the ready DAG **subject to the current end-to-end bottleneck**; use isolated worktrees/scopes for concurrent writers and respect actual harness/provider/host limits rather than a fixed agent count. See `docs/system/CONTEXT-AND-PARALLELISM.md` and `docs/system/REPOSITORY-LAYOUT-AND-STATE.md`.

## GitHub bootstrap and sync
Default GitHub sync is enabled.
1. inspect Git/remotes/auth without exposing credentials;
2. reuse valid `origin`;
3. if absent, create planned repository under authenticated GitHub account, PRIVATE unless explicitly PUBLIC;
4. initialize/normalize `main` and push baseline;
5. use isolated job/wave branches/worktrees when useful;
6. before every commit classify documentation impact, update affected beginner/user/operator/API/migration docs in the same commit, record the staged fingerprint and pass `DOCS_FRESHNESS_GATE`; commit completed jobs and push meaningful checkpoints;
7. integrate only fully validated waves through repository-allowed direct/PR/check policy;
8. before every push pass the pre-push documentation gate; push/pull-verify `main`; never bypass branch protection.

`COMPLETED` requires latest validated integrated state on remote `main` when remote verification is possible.

## Runtime / network safety
After integrated waves: rebuild/restart latest main, run migrations/config applies, health/readiness and relevant smoke/browser/network checks. Never report unverified reachability.

For remote network/firewall/router changes, preserve management access. Use backup, canary, transaction/commit-confirm/timed rollback or out-of-band recovery when lockout is plausible. Never broaden firewall exposure or disable security merely to make tests pass.

## Context efficiency
Use `SEARCH → SLICE → TRACE → EXPAND`, progressive skill/reference loading, SHA-bound maps, compact worker returns, evidence on disk and strategic compaction only after state is persisted. Large library ≠ large active context.

## Source of truth
1. actual Git + fresh runtime/tool verification;
2. `AUTOPILOT-GOAL` + canonical jobs/dependencies;
3. STACK/SKILLS manifests + ADRs/research register;
4. execution ledger/evidence;
5. STATE hot view;
6. narrative summaries.

## V5.6.3 adaptive execution / subagent liveness
Before finalizing or dispatching the DAG, classify `planning/execution/EXECUTION-PROFILE.yaml` as `MICRO`, `SMALL`, `STANDARD` or `HIGH_RISK`. Scale job count, branching, independent-review frequency, evidence granularity and commit/push cadence to that profile while keeping requirement/risk quality floors intact. MICRO/SMALL work should prefer coherent vertical-slice milestones and batching over job-per-microtask ceremony.

Every delegation has an explicit required-capability set. Do not dispatch a web researcher without verified web access, a browser verifier without browser capability, or a writer without the required isolation/scope. For long-running/expensive workers, use harness-native progress/session signals where available. Meaningful progress keeps the worker alive; a quiet worker is health-checked before cancellation; elapsed wall-clock time alone is not stall evidence. If a provider hard deadline cannot be removed, checkpoint before it when feasible and resume from `planning/private/runs/...`/native session state plus actual Git/files. Repeated stalls trigger job resizing, provider/capability rerouting or debugging rather than blind restarts. See `docs/system/ADAPTIVE-EXECUTION-AND-WORKER-LIVENESS.md`.

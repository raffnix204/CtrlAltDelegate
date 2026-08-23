# Master Autopilot — V5.8.2

## Objective
Turn the project goal into a fully implemented, verified and GitHub-synchronized result without stopping between schedulable jobs.

## Lifecycle

```text
REPO_ROOT_OR_SAFE_DELIVERY_MERGE
→ PERSISTED_STATE_READ
→ HARNESS_READY
→ GIT_GUARDS_READY → GITHUB_READY
→ PROJECT_OR_REPO_READY
→ RESEARCH_SUFFICIENT
→ STACK_READY
→ SKILLSET_READY
→ EXECUTION_DAG_READY
→ WAVES/JOBS
→ REVIEW/VERIFY
→ INTEGRATE/PUSH MAIN
→ REBUILD/RESTART/HEALTH
→ NEXT WAVE
→ FINAL AUDIT
→ COMPLETED
```

## Stage -2 — Repository-root delivery / persisted state
V5.8.2 Custom-GPT deliveries arrive as `ctrlaltdelegate-delivery.zip` in the target project root. Start from that root, safely import the package to local-private `./.ctrlaltdelegate/`, validate `./.ctrlaltdelegate/planning/handoff/HANDOFF-STATUS.yaml`, then read the canonical handoff and state before broad work.

## Stage -1 — Harness readiness
Detect the active harness/capabilities. Pi is the reference harness but Codex, Claude Code and OpenCode remain supported. Reuse native/installed capabilities. If a required capability is missing, research a current compatible provider, install only through supported safe mechanisms, record the resolved provider/version, then verify it. Reach `HARNESS_READY`.

## Stage 0 — Git documentation guards
Install or safely integrate `.githooks` documentation guards. Preserve existing hook systems. Record initial documentation impact/attestation before the first implementation/baseline commit. Reach `GIT_GUARDS_READY`.

## Stage 1 — GitHub readiness
Inspect Git/remotes/auth without revealing secrets. Reuse valid `origin`; otherwise create the planned repository under the authenticated account, PRIVATE unless PUBLIC was explicitly approved. Establish/push the validated baseline and record `GITHUB_READY`. Respect branch protection/PR/status checks.

## Stage 2 — Project / repository intake
### Greenfield
Resolve product objective, users, workflows, outcomes, MVP/non-goals and constraints.

### Brownfield
Run `repository-onboarding`: protect dirty user work, record baseline SHA, stack/build/test/runtime fingerprints, system/capability map and health baseline. Reach `REPO_READY` before broad modification.

### Existing website
Complete authorized source acquisition or schedule deterministic `SOURCE_ACQUISITION` before broad rebuild. Reach `SOURCE_READY`.

## Stage 3 — Research
Research current material facts: platform/framework/SDK/database/provider capabilities, versions/support, licensing, pricing/quotas when material, security constraints and compatibility. Prefer official primary sources. Record findings and ADR evidence.

## Stage 4 — Technology and architecture
For non-trivial greenfield work, use `technology-stack-selection`. For brownfield, preserve the detected stack unless a justified change is required.

Populate `planning/architecture/STACK-MANIFEST.yaml` and architecture/ADR files. Explicitly decide language/runtime/framework/rendering/data/deployment and material integrations. Reach `STACK_READY` only when unresolved stack questions no longer change implementation design.

## Stage 5 — Skill routing
Use `skills/CATALOG.yaml`, project profile, STACK-MANIFEST, change triggers and risks to build `planning/execution/SKILLS-MANIFEST.yaml`.

Rules:
- substantive implementation → `implementation-engineering` + matching stack specialist(s) + domain specialists;
- review → `code-review` + `verification-gate` + triggered specialists;
- bugs → systematic debugging + matching causal/stack specialist;
- schema evolution → database migrations;
- queues/events/distribution → distributed systems;
- external provider → integration engineering;
- Kubernetes → Kubernetes operations;
- ML/agent/MCP → matching specialists.

Reach `SKILLSET_READY`. Do not preload unrelated skills.

## Stage 6 — Program + execution design
For substantive cross-file/cross-layer work, satisfy the lightest sufficient `PROGRAM_DESIGN_GATE`: existing reuse, likely files/modules, public types/contracts, call/data flow, state/failure boundaries, test shape and intentionally delegated choices. Prefer an executable first vertical slice when dependencies allow.

Create bounded jobs, dependency DAG, waves, risk classes, seams, acceptance/evidence and Git/runtime rules. Every job lists exact required skill IDs and `.agents/skills/<id>/SKILL.md` paths.

Before dispatch, the orchestrator includes those paths in the worker contract. Worker return includes `SKILLS_APPLIED`.

Reach `EXECUTION_DAG_READY` after requirements, stack and skill coverage audits.

## Stage 7 — Execute waves
For each wave:
1. enumerate dependency-ready jobs and identify the current end-to-end bottleneck (implementation, integration, test/CI, review, runtime/environment or external);
2. map conflicts/seams/resources and form the largest **useful** concurrent groups without creating avoidable WIP in front of the bottleneck;
3. branch/worktree from latest validated baseline when appropriate; prefer a testable vertical slice before broad horizontal expansion when dependencies allow;
4. workers read required skill files before implementation/review;
5. collect compact reports/evidence and update `planning/execution/STATE.md` at meaningful boundaries;
6. run Spec Compliance → Code Quality → triggered specialist/seam gates;
7. bounded repair/retry; confirmed bugfixes should preserve `PRE_FIX_FAIL → POST_FIX_PASS` evidence when practical, followed by `FAILURE_MODE_CLOSURE` for escaped/repeated failure classes;
8. before each commit pass documentation impact/freshness and before each push pass pre-push docs history;
9. integrate only validated work.

The main orchestrator is normally spawn-only when capable subagents exist.

## Stage 8 — Main checkpoint
Integrate through repository-allowed path → push → verify remote main → rebuild/restart latest main → migrations → health/readiness → smoke/browser/runtime checks → update STATE/ledger/memory → continue automatically.

## Stage 9 — Final audit
Run requirement-to-job-to-evidence coverage, build/test/lint/type/security and triggered stack/domain/runtime gates. Confirm no targeted blocking findings, `DOCUMENTATION_READY` is proven by a fresh-user reviewer, latest validated main including docs is synchronized to GitHub and runtime acceptance is satisfied. Then mark `COMPLETED`.

## Continuation
Allowed interruption states only: `RESTART_REQUIRED` (minimal restart/resume action), `DECISION_REQUIRED`, `BLOCKED_EXTERNAL`, `POLICY_DENIED`, unrecoverable `RETRY_EXHAUSTED`, or explicit `PAUSED`.

Worker/phase completion is not terminal. If dependency-ready work remains, continue.


## V5.8.2 hard gates
- `GIT_GUARDS_READY`: documentation pre-commit/pre-push guard active or safely integrated with existing hooks.
- `PROGRAM_DESIGN_GATE`: consequential structure/test shape resolved before broad substantive implementation at the lightest useful depth.
- `VERTICAL_SLICE_GATE`: prefer early executable end-to-end evidence when the dependency graph allows.
- `PARALLELISM_PLANNING_GATE`: useful concurrency is maximized relative to the current throughput bottleneck; throttling/serial exceptions recorded.
- `CONTEXT_FRESHNESS_GATE`: fresh workers/reviewers and context-epoch rotation from durable state.
- `DOCS_FRESHNESS_GATE`: affected documentation in same commit; pre-push history validated.
- `DOCUMENTATION_READY`: beginner README/feature coverage/current commands/examples verified on final candidate and remote main.
- `RESTART_REQUIRED`: only when a newly installed/trusted Pi capability cannot become active via supported reload; persist first, tell operator exact restart/resume action, then rerun preflight.


## V5.8.2 hardening loop
For each substantive job:
`JOB_BASELINE → PROGRAM_DESIGN_GATE (when material) → JIT_RESEARCH → SKILL_LOAD → SOLUTION_MINIMIZATION_GATE → FIRST_VERTICAL_SLICE → EARLY_VERIFY/RESTEER → IMPLEMENT/EXTEND → FALSIFIABLE_TEST_EVIDENCE → FAILURE_MODE_CLOSURE (when triggered) → DOCS → COMMIT → FRESH COMPLEXITY/QUALITY REVIEW AS ROUTED → EVIDENCE_REFRESH`.

After each validated wave update the convergence/evidence artifacts. Before final completion require `CONVERGENCE_READY + EVIDENCE_READY + DOCUMENTATION_READY + RUNTIME_READY + REMOTE_MAIN_READY`.

## V5.8.2 adaptive execution
Autopilot begins execution only after `EXECUTION_RIGHTSIZING_GATE`. The selected profile controls orchestration granularity, not quality. Long-running subagents are governed by progress-aware leases and checkpoint/resume; static elapsed duration alone never proves a stall. Before each dispatch, verify worker capabilities match the job.

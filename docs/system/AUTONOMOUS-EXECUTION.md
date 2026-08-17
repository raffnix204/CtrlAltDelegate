# Autonomous Multi-Agent Execution Playbook

## 1. Goal

The exported plan must allow a coding system to implement the project with one primary start command and minimal human intervention.

Do not design a workflow where the user must manually issue Phase 1, then return for Phase 2, etc.

The default model is:

`MASTER AUTOPILOT GOAL → PREFLIGHT → EXECUTION DAG → WAVES → PARALLEL SUBAGENTS → REVIEWS → INTEGRATION → VERIFICATION → CHECKPOINT → NEXT WAVE`

Individual phase/job goals exist only for recovery/manual intervention.

## 2. Planning phases vs execution jobs

### Planning phase
A conceptual implementation milestone.

### Execution job
The smallest bounded unit that:
- has a clear outcome;
- has dependencies;
- can be assigned to one agent;
- has a review/verification surface;
- declares produced/consumed contracts;
- can be integrated independently enough to reason about.

Do not over-fragment trivial setup. Do not make jobs so large that review becomes vague.

## 2A. Existing-project preflight

Before modifying a brownfield repository:

`REPOSITORY_INTAKE → BASELINE HEALTH → REPO_READY → requested planning/audit/debugging → jobs/waves`

Protect dirty user work, record baseline SHA, discover canonical commands, separate pre-existing failures from regressions and reconcile planner snapshots against actual checkout.

Modes:
- `AUDIT_ONLY`: validated findings, no fixes.
- `AUDIT_REMEDIATE`: audit → validate/dedupe → remediation DAG → independent re-audit.
- `BUGFIX`: systematic debugging → tests → review → verification.
- `FEATURE_CONTINUATION`: focused repo map → delta plan → normal DAG.
- `SECURITY_HARDEN`: security-led audit/remediation.
- `FRONTEND_UPGRADE`: existing UI/UX pipeline.
- `SEO_OPTIMIZE`: technical/content baseline → fixes → verification.

Finding lifecycle:
`DISCOVERED → VALIDATED → PLANNED → FIXED → VERIFIED → CLOSED`
with `FALSE_POSITIVE`, `DEFERRED`, `RISK_ACCEPTED`, `BLOCKED_EXTERNAL`.

Only validated findings create mandatory remediation jobs. Critical/high confirmed security/data-loss/correctness blockers may precede unrelated work; medium/low unrelated debt does not automatically expand feature scope.

## 3. Dependency DAG

For every job record:

- `id`;
- source planning phase;
- dependencies;
- outputs consumed by later jobs;
- likely modules/files;
- shared contracts touched;
- migration/schema impact;
- external dependencies;
- parallel-safety classification.

The planner constructs a DAG.

Jobs may share a wave only when they can safely run from the same baseline without requiring unfinished output from each other.

A different Git branch does **not** remove semantic dependencies.

## 4. Execution waves

A wave contains all currently dependency-ready jobs that are sufficiently independent.

Example:

```text
Wave 01
- shared repository/runtime foundation

Wave 02 (parallel)
- authentication adapter
- UI design-system foundation
- observability bootstrap

Wave 03 (parallel)
- project backend workflow
- project frontend workflow

Wave 04
- end-to-end integration/hardening
```

If shared API/schema contracts are not yet stable, establish them in an earlier sequential job rather than letting parallel workers redesign them independently.

## 4A. Decomposition seam check

Before dispatching a parallel wave, name the most important **cross-cutting concern that could fall between job scopes**.

Examples: auth/authz, tenant isolation, shared API/types, transactions, caching/invalidation, migrations or runtime compatibility.

Record either:
- `Seams: NONE — behaviorally independent`, or
- `Seams: <named concern>`.

If the seam is non-trivial, assign a **SEAM REVIEWER** after integration. It reads across job outputs and verifies cross-job behavior without duplicating normal per-job review.

## 4B. Parallelism planning gate

At every scheduling decision, enumerate dependency-ready jobs, identify the current end-to-end bottleneck and build a conflict/seam/resource map. Dispatch safe independent work concurrently only while it improves throughput. Serializing or throttling independent ready work requires a concrete dependency, mutable-scope collision, unstabilized contract, exclusive runtime/device, provider/harness cap, host constraint or saturated integration/test/CI/review/runtime bottleneck.

Do not use a fixed worker count. Discover effective concurrency at runtime. Read-only research/exploration/review may fan out aggressively. Concurrent writers require isolated worktrees/cwd/scopes and non-overlapping conflict domains. Integration and shared-state mutation remain orchestrator-owned.


## 5. Spawn-only thin orchestrator

The orchestrator owns the project outcome but should normally perform **no feature/job implementation itself** when a suitable worker-agent surface is available.

Its job is orchestration, not phase-role substitution.

Primary responsibilities:

1. read plan and state;
2. select dependency-ready work;
3. prepare isolated agent scopes;
4. dispatch subagents;
5. wait/collect results;
6. inspect actual Git diff/evidence;
7. request fixes where necessary;
8. integrate accepted work;
9. run wave verification;
10. update persistent state/ledger/learnings;
11. perform Git/runtime checkpoint;
12. continue.

### Spawn-boundary invariant

When implementation/research/review is required and the harness can create the appropriate subagent, the orchestrator MUST spawn that role rather than doing that role's work in-band.

Allowed orchestrator work:
- deterministic orchestration/state edits;
- Git integration/conflict resolution;
- shared execution-state maintenance;
- emergency fallback when the needed subagent capability genuinely does not exist.

Fallback must be recorded as a deviation.

This protects the main context from implementation-level context rot.

## 6. Fresh bounded subagents

Subagents receive only the context needed for their job:

- job brief;
- relevant requirements;
- relevant ADRs;
- relevant interfaces/data/UI rules;
- applicable external skills;
- relevant accumulated project learnings.

Do not dump the entire project history into every worker.

## 6A. Context freshness gate

Fresh context is the default for each independent implementation job and every independent reviewer. A fresh debugger is mandatory on escalation after repeated failed repair. Persist state/evidence before semantic boundaries, then compact/reset and increment `CONTEXT-STATE.yaml` epoch when useful. Goal persistence is continuation, not memory authority. Reconstruct minimal context from Git, STATE, current job/wave, relevant ADR/contracts and exact routed skills. Long worker output stays on disk with compact handoffs.


## 7. Standard agent roles

Map these roles to capabilities available in the coding harness.

### ORCHESTRATOR
Git integration, state, dispatch, evidence gates.

### IMPLEMENTER
Writes code within job scope.

### QUICK IMPLEMENTER
Low-risk mechanical changes.

### ARCHITECT / ORACLE
High-level reasoning, read-only unless explicitly reassigned.

### RESEARCHER / EXPLORER
Repository or external investigation, read-only.

### SPEC REVIEWER
Checks whether implementation matches the job/requirements. Read/run only.

### CODE QUALITY REVIEWER
Checks correctness, maintainability, architecture, test quality. Read/run only.

### SECURITY REVIEWER
Threat/security inspection. Normally read/run only.

### UI/UX REVIEWER
Visual/responsive/accessibility review.

### DEBUGGER
Fresh root-cause context after repeated failures.

### RUNTIME VERIFIER
Validates rebuilt running application and host URL.

### SEAM REVIEWER
Reviews cross-job/cross-module behavior individual scoped reviewers can miss. Read/run only.

Only the orchestrator should normally spawn coding subagents. Avoid recursive agent trees.

## 8. Job delegation contract

Every job file should specify:

- Objective
- Requirement IDs
- Dependencies
- Baseline
- Consumes
- Produces
- Allowed Scope
- Protected Scope
- Risk Class
- Change Triggers
- Cross-Job Seams
- Applicable Skills
- Implementation Constraints
- Acceptance Criteria
- Validation
- Runtime Impact
- Git Output
- Handoff Report

Subagents do not decide whether an entire wave is complete.

## 8A. Risk-based smart routing

Do not use the same agent/gate count for every job.

### LOW
Docs, isolated content, mechanical safe changes. Minimal proportional verification.

### STANDARD
Normal feature work. Implementer + normal Spec/Code Quality gates where substantive.

### HIGH
Escalate when work touches material API/public contracts/shared types, database schema/migrations, auth/authz, secrets/security boundaries, payments/sensitive data, infrastructure/release controls, shared cross-module state or breaking changes.

HIGH work may add Security Review, contract/consumer impact review, migration checks, seam review and adversarial factual verification.

Parallelism is a latency tool, not automatically a cost/quality win. Use the minimum sufficient agents/gates.

## 8B. Change-sensitive verification triggers

Execution inspects the actual diff as well as planner hints.

| Change | Additional gate |
|---|---|
| API/schema/shared type | consumer/contract impact |
| DB migration | forward/compatibility/data-safety |
| auth/authz | security + authorization integration |
| public UI flow | browser/accessibility acceptance |
| dependency/toolchain | build/security/compatibility |
| central runtime/config | rebuild/restart/smoke |

Only activate additional gates when the risk actually exists.

## 9. Dual review gate

For substantive code jobs:

### Gate A — Spec Compliance
Ask: did the implementation do exactly what the approved requirement/job requested?

Check:
- missing behavior;
- extra scope;
- broken contracts;
- unauthorized changes;
- requirement traceability.

### Gate B — Code Quality
Ask: is the implementation technically sound?

Check:
- correctness;
- architecture;
- security;
- maintainability;
- error handling;
- tests;
- unnecessary complexity.

The same reviewer should not silently fix what it reviews; findings return to an implementer/fix agent.

Small trivial jobs may use a single proportional review.

## 10. Evidence before completion

Agent reports are **claims**, not evidence.

Completion must be supported by fresh observable evidence such as:

- test command exit status;
- typecheck/lint/build output;
- migration result;
- diff;
- API/contract test;
- browser/E2E result;
- health request;
- screenshot/visual check where applicable.

Never accept "should work" or "tests pass" without reproduction.

Where selected, an adversarial judge should independently:
- enumerate completion claims;
- inspect actual diff;
- re-run claimed checks;
- detect weakened/deleted tests;
- detect scope creep;
- detect spec-vs-test betrayal;
- label evidence as VERIFIED / VERIFIED WITH CAVEATS / REFUTED.

### Fact-vs-judgment boundary

Use adversarial verification for **refutable claims** that can be checked against code, tests, repository state or runtime evidence.

Do not majority-vote subjective architecture, naming, UX taste or trade-off decisions. Resolve them using explicit project/ADR criteria; otherwise use the authorized decision owner and document the decision. Escalate only when the decision is user-owned.

## 11. Intent authority gate

When code, tests and specifications disagree, do not optimize blindly for green tests.

Authority order by default:

1. explicit current user/product requirement;
2. approved project specification/ADR;
3. acceptance contract;
4. tests;
5. current code behavior.

Surface the conflict and choose according to the highest valid authority.

## 12. Formal continuation / stop matrix

After every subagent return, job integration, verification result or wave boundary resolve one next state:

| Condition | Action |
|---|---|
| Dependency-ready work exists, no hard stop | **CONTINUE** |
| One branch blocked, unrelated work ready | **CONTINUE_OTHER_WORK** |
| Recoverable failure within budget | **REPAIR_RETRY** |
| Derived state disagrees, canonical evidence clear | **RECONCILE_STATE** |
| Newly installed/trusted harness capability cannot activate in current process | **RESTART_REQUIRED** — persist state, request exact restart/resume only |
| User-owned decision required | **DECISION_REQUIRED** |
| Credential/access/external approval missing | **BLOCKED_EXTERNAL** |
| Critical retry budget exhausted | **RETRY_EXHAUSTED** |
| Safety/security policy denies action | **POLICY_DENIED** |
| Explicit safe pause | **PAUSED** |
| All mandatory work + final verification complete | **COMPLETED** |

A finished subagent/phase is **not** a terminal condition while schedulable work remains.

Stable state reasons: `CONTINUE`, `RESTART_REQUIRED`, `BLOCKED_EXTERNAL`, `DECISION_REQUIRED`, `RETRY_EXHAUSTED`, `VERIFICATION_FAILED`, `STATE_INCONSISTENT`, `POLICY_DENIED`, `PAUSED`, `COMPLETED`.

## 13. Failure budget and escalation

Use bounded repair loops.

Example:

1. same implementer repairs with failing evidence;
2. second repair with targeted diagnostics;
3. fresh DEBUGGER performs root-cause analysis;
4. stronger architecture/reasoning review;
5. classify blocker.

If failure blocks only one branch of the DAG, continue unrelated ready jobs where safe.

Stop the full run only when the blocking dependency prevents further defensible progress.

## 14. User intervention policy

### Agent may decide autonomously
- reversible technical implementation detail;
- internal refactor needed for correctness;
- test implementation;
- low-impact library substitution compatible with ADR constraints;
- bug workaround;
- code organization.

### Agent may decide but must document
- meaningful internal interface change;
- alternative library due to verified incompatibility;
- performance strategy;
- technical deviation from implementation notes that preserves product intent.

### User input required
- product behavior changes;
- MVP scope changes;
- destructive data decision;
- weaker security/privacy guarantee;
- material new recurring cost;
- vendor/business change;
- unmet compliance requirement;
- external credential/approval unavailable.

The coding agent asks the user directly if required. It never sends the user back to the Planning GPT.

## 15. Persistent execution state

The plan exports initial templates. The coding orchestrator maintains:

### `STATE.md`
Current run, main SHA, current wave/jobs, completed/blocked jobs, runtime SHA/URL, next ready work.

### `execution-ledger.md`
Immutable-ish history of completed jobs, commits, evidence, reviews and merges.

### `execution-memory.md`
Curated implementation learnings:
- conventions discovered;
- successful patterns;
- failed approaches;
- integration gotchas;
- validated commands;
- runtime notes.

Only the orchestrator writes shared state files during parallel work. Workers return proposed learnings in their handoff.

## 15A. Canonical state and reconciliation

Avoid competing status truths.

Default authority:
1. actual Git state and verification evidence;
2. canonical job/dependency status in the execution plan/state ledger;
3. `execution-ledger.md` completed evidence;
4. `STATE.md` as current derived/hot view;
5. human-readable summaries.

On start/resume or disagreement:
1. inspect branches/commits/worktrees;
2. compare canonical job status/dependencies;
3. confirm completed ledger evidence;
4. compare `STATE.md`;
5. repair derived state only when evidence is unambiguous;
6. stop with `STATE_INCONSISTENT` when canonical sources genuinely conflict.

Never mark work complete merely to make status files agree.

## 16. Context efficiency

### Context profiles
- `lean` — small/simple/local work;
- `balanced` — normal default;
- `full` — high-risk architecture, migration or large cross-cutting work.

Profiles change context breadth, never requirements or quality truth.

### Progressive/narrow reads
Prefer index/state → relevant heading/symbol/diff/search result → full file only when needed. If an exact section is known, do not automatically load the entire large document.

### Hot / cold surfaces
Keep frequently loaded `STATE.md`, current wave/execution summary, active architecture index and current handoff bounded. When thresholds are exceeded, archive older immutable detail into deterministic cold-history files and keep pointers in the hot surface. Never delete historical evidence during compaction.

### Compact return contract
Full reports/evidence live on disk where useful. Normal subagent return:

```text
STATUS: DONE | APPROVED | BLOCKED
- critical finding 1
- critical finding 2
- critical finding 3
report: <path>
```

The orchestrator reads full reports on BLOCKED, conflict, audit or when integration requires them.

Do not compress away failing evidence, security findings, interface contracts, acceptance criteria or destructive-operation warnings.

## 17. Final system audit

After all implementation waves:

1. run full regression suite;
2. trace mandatory requirements to evidence;
3. run security/reliability checks;
4. run full browser/UI checks when relevant;
5. rebuild/restart latest `main`;
6. verify the actual host URL;
7. confirm no pending critical integration debt;
8. persist final state;
9. report completion evidence.

The project is complete only when the implementation and running system, not merely agent reports, satisfy the plan.

## Harness capability preflight

Before project/repository/source preflight reach `HARNESS_READY`.

Detect active harness from runtime/tool surface. First-class: Codex, Claude Code, OpenCode, Pi.

Check only required capabilities: instructions, Agent Skills, isolated delegation, file/search/shell, Git/worktrees, web/docs, browser/runtime and selected execution tools.

Bootstrap ladder: `NATIVE → EXISTING → PINNED PROJECT INSTALL → VERIFY → FALLBACK/BLOCK`.

Auto-install only when required, researched, compatible/licensed, exact-pinned when practical and preferably project-local. Never use blind remote installer scripts, weaken policy or overwrite global user settings.

Pi delegation is resolved by capability at runtime; no third-party provider/version is hardcoded in V5.6.4.

## Repository-root delivery stage

V5.6.4 Custom-GPT project deliveries use the deterministic nested `ctrlaltdelegate/` control directory inside the target project root. The coding agent works from the target project root and treats the nested package as planning/control state, not as the application root.

Required brownfield order:
`DELIVERY_VALIDATE → GIT/USER-WORK_SAFETY → DRY_RUN_MERGE → CONFLICT_RECONCILE → ROOT_FILES_VERIFY → PERSISTED_STATE_READ → HARNESS_PREFLIGHT`.

Root `AGENTS.md`/selected `.agents/skills` are operational surfaces; `planning/` is persistent versioned memory. Ignore only private/raw/tmp/log/cache/import-conflict artifacts.

## Pi reference-harness capability model

Pi is the reference harness. Detect capabilities individually:
- persistent goal/run loop;
- isolated general worker delegation;
- parallel delegation;
- independent read-only review;
- remote operator channel (optional);
- web-acquisition/MCP;
- browser interaction;
- semantic code navigation (optional for large repos).

Do not infer general subagents merely because a Goal extension has a verifier. Use existing installed host capabilities first. Missing required capabilities may be researched/installed through Pi's supported package mechanism after project trust; record the resolved provider/version in state, but do not bake that version or any model choice into V5.6.4 methodology. Re-verify after documented reload; if activation requires restarting Pi, persist and enter `RESTART_REQUIRED` with exact resume instructions.

If persistent Goal mode exists, bind the whole `AUTOPILOT-GOAL.md` to that outer persistence loop. V5.6.4 continuation states still decide what work happens next; do not stack competing autonomous loops.


## V5.6.4 Stack/Skill execution invariants

`STACK_READY` and `SKILLSET_READY` are mandatory gates before `EXECUTION_DAG_READY`. Every job includes `Required Skills` with canonical paths. The orchestrator passes those paths to the worker; the worker reads them before work and returns `SKILLS_APPLIED`. If a diff introduces a new stack/domain trigger, rerun routing for affected jobs.

Library breadth never implies context breadth. Workers load only assigned skill bodies.


## Documentation gate before commit/push
Each job returns `DOCS_IMPACT`. Before a commit the orchestrator/worker updates affected canonical docs in the same staged diff or records a concrete `NONE`, then records/validates `DOCUMENTATION-STATE.yaml`. No push proceeds until the pushed history passes the pre-push documentation gate. Final validation includes a fresh-user README/install/use review and feature-coverage check.


## V5.6.4 Program design / vertical slices / state
Before broad substantive cross-file/cross-layer implementation, satisfy the lightest sufficient `PROGRAM_DESIGN_GATE`. Prefer an executable vertical slice and early re-steering before expanding the diff when dependencies allow. `planning/execution/STATE.md` is mandatory compact current state and is refreshed at every meaningful execution boundary; detailed history remains in the ledger.

For confirmed bugs prefer `PRE_FIX_FAIL → POST_FIX_PASS` evidence when practical. Escaped/repeated failures trigger `FAILURE_MODE_CLOSURE` and the smallest effective durable prevention/detection control.

## V5.6.4 Execution Rightsizing
Run `EXECUTION_RIGHTSIZING_GATE` before dispatch. MICRO/SMALL projects should collapse tightly coupled micro-jobs into coherent executable milestones, avoid branch/worktree-per-job when no parallel writer isolation is needed, use milestone evidence, and reserve fresh independent reviews for final release plus real risk triggers. STANDARD/HIGH_RISK retains the fuller DAG/review/evidence model. A single high-risk job may escalate locally without inflating unrelated work.

## V5.6.4 Worker lease and recovery
Before delegation verify exact job capabilities against the chosen worker. For long-running workers prefer native progress/update/session signals. Meaningful progress renews the lease. A quiet period leads to a health check, not automatic cancellation; elapsed wall-clock time alone is not a failure signal. On unavoidable provider deadline/crash, persist/reconcile checkpoint + Git/files and resume the next safe step. Repeated identical stalls require job resizing/capability rerouting/root-cause debugging rather than repeated clean restarts.

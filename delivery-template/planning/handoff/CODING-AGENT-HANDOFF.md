# CODING AGENT HANDOFF — V5.8.2


> **Entry semantics:** This document is the execution-ready handoff/resume surface. For a fresh standalone `NOT_STARTED` checkout, use root `START-HERE.md`; lifecycle mode detection will start collaborative discovery instead of assuming a completed plan.

## Mission

Own this repository from its current persisted state through `COMPLETED` with minimal user intervention.

## Start from disk, not chat history

From repository root read, in this order:
1. `AGENTS.md`;
2. `planning/execution/EXECUTION-SNAPSHOT.json` and generated `STATE.md`;
3. `planning/discovery/DISCOVERY-STATE.md` and `planning/discovery/TECHNICAL-PREFERENCES.yaml`;
4. `planning/execution/AUTOPILOT-GOAL.md`;
5. current requirements / active job(s);
6. relevant ADRs and `planning/architecture/PROGRAM-DESIGN.md`;
7. `STACK-MANIFEST.yaml` and `SKILLS-MANIFEST.yaml`;
8. only the exact routed `.agents/skills/<id>/SKILL.md` files needed for the current job.

Treat Git + `planning/` + executable evidence as the durable source of truth. Conversation history is disposable.


## Discovery/constraint preservation

Treat resolved `REQUIRED` preferences as user-owned constraints and `PREFERRED` as strong defaults. `AUTO` decisions are yours to resolve from evidence without asking the user. If repository/runtime evidence conflicts with planning assumptions, perform impact analysis, update only affected planning artifacts and reconverge. Do not casually re-open product brainstorming during implementation.

## Persistent state obligation

Treat normalized control artifacts as source of truth and regenerate `EXECUTION-SNAPSHOT.json` plus `STATE.md` with `scripts/build_execution_snapshot.py --write-state-md` after material job/wave/commit/runtime/blocker/restart/convergence changes. Do not hand-maintain a competing summary truth.

Before any restart or context reset, persist the exact next action and authoritative branch/SHA/runtime/evidence status. After restart, reconstruct from disk and re-run the required preflight rather than replanning.

## Program design and implementation

Before substantive implementation, satisfy `PROGRAM_DESIGN_GATE` at the lightest depth appropriate to the task, then run `SOLUTION_MINIMIZATION_GATE`.

Prefer executable **vertical slices** over large horizontal layer batches when the dependency graph permits:
`minimal end-to-end path → verify → extend behavior → verify → edge/failure hardening → verify`.
After the first slice of high-impact work, compare the actual trajectory with program design and re-steer early if needed.

## Testing and bugfix evidence

Tests must be falsifiable. For confirmed bugfixes, when practical capture `PRE_FIX_FAIL → POST_FIX_PASS` on the same regression check. Preserve the pre-fix evidence or reproduce it from the baseline commit/worktree; do not weaken existing tests to manufacture RED/GREEN.

## Failure-mode closure

When a defect, incident, escaped regression or repeated repair is resolved, ask what durable protection prevents recurrence. Add the smallest justified regression test, validation, lint/static rule, runtime guard, CI gate, documentation/runbook change or planning/skill learning. Do not add process for one-off noise without recurrence value.

## Parallelism and bottlenecks

Maximize safe concurrency only while it improves end-to-end delivery. Identify the current bottleneck (implementation, integration, tests, CI, review, environment, deployment, external provider). Do not spawn more writers when they merely accumulate work in front of a slower verification/integration bottleneck. Batch tiny same-shape tasks; parallelize substantive independent jobs; serialize only for a recorded dependency/conflict/resource/bottleneck reason.

## Measurable outcomes

Where requirements expose meaningful measurable outcomes, use them as backpressure and evidence. Do not replace categorical correctness/security/accessibility requirements with proxy metrics.

## Completion

`COMPLETED` requires typed requirement-appropriate evidence, mandatory user-journey PASS, live provider/consumer verification where required, product-drift PASS, fresh SHA-bound convergence, documentation readiness and intended remote-main state. Use `transition_job.py` for `DONE` and `validate_product_completion.py` for final completion. Missing external proof is deferred while dependency-ready work continues; after feasible work is exhausted report `VALIDATION_PENDING_EXTERNAL` rather than false completion.


## Language continuity
Continue the conversation in the user's language unless explicitly requested otherwise. Keep CtrlAltDelegate-controlled planning, system, handoff and execution artifacts in English; preserve localized product content only where the project requires it.


## V5.8.2 control surfaces
Use the canonical loop registry/state, machine-readable job graph, surface policy, decision ledger, artifact-consistency gate and harness-conformance profile. For Custom-GPT ZIP handoffs, import to `./.ctrlaltdelegate/` under `LOCAL_PRIVATE` Git visibility before execution.


## V5.8.2 planning-skill and authoritative-content handoff

Read `planning/context/PLANNING-SKILL-STATE.yaml` before execution. Treat recorded planning decisions as the result of the listed specialist decision surfaces, not as generic prose. Load the same canonical selected skills for implementation/review when their jobs remain relevant.

Files under `planning/content/pages/` with `status: approved` are authoritative product content. Preserve wording, factual claims, CTA intent, hierarchy and approved SEO metadata unless implementation proves a genuine conflict; route such conflicts through scoped change control instead of silently rewriting copy.
## V5.8.2 blocker / deferred-validation contract
Classify unavailable prerequisites by effect. A `VERIFICATION_BLOCKER` (human test, physical device, later credential, external validation window) blocks only the affected proof: research, implement the best evidence-backed path, record an assumption and deferred validation, then continue all dependency-ready work, including downstream jobs whose dependency gate is `IMPLEMENTATION`. Only a dependency explicitly gated `VERIFIED` waits for `DONE`. An `EXECUTION_BLOCKER` is reserved for a path that cannot proceed meaningfully or safely and is scoped to `JOB|SUBGRAPH|GLOBAL`; global stop is allowed only when no required ready work remains. Batch unavoidable external checks into a final validation wave and turn failures into repair jobs.


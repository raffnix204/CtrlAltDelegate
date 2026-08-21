# CODING AGENT HANDOFF — V5.8.1


> **Entry semantics:** This document is the execution-ready handoff/resume surface. For a fresh standalone `NOT_STARTED` checkout, use root `START-HERE.md`; lifecycle mode detection will start collaborative discovery instead of assuming a completed plan.

## Mission

Own this repository from its current persisted state through `COMPLETED` with minimal user intervention.

## Start from disk, not chat history

From repository root read, in this order:
1. `AGENTS.md`;
2. `planning/execution/STATE.md`;
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

Keep `planning/execution/STATE.md` short and current. Update it after every meaningful job, integrated wave, material commit/push, runtime apply, hard-stop/blocker, restart boundary, context reset and convergence/evidence verdict change. Append detailed history to `execution-ledger.md` instead of bloating STATE.

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

`COMPLETED` requires convergence of mandatory requirements through code/tests/docs, fresh SHA-bound evidence, documentation readiness, runtime/user acceptance where applicable, and intended remote-main state. Ask the user only on defined hard stops.


## Language continuity
Continue the conversation in the user's language unless explicitly requested otherwise. Keep CtrlAltDelegate-controlled planning, system, handoff and execution artifacts in English; preserve localized product content only where the project requires it.


## V5.8.1 control surfaces
Use the canonical loop registry/state, machine-readable job graph, surface policy, decision ledger, artifact-consistency gate and harness-conformance profile. For Custom-GPT ZIP handoffs, import to `./.ctrlaltdelegate/` under `LOCAL_PRIVATE` Git visibility before execution.


## V5.8.1 planning-skill and authoritative-content handoff

Read `planning/context/PLANNING-SKILL-STATE.yaml` before execution. Treat recorded planning decisions as the result of the listed specialist decision surfaces, not as generic prose. Load the same canonical selected skills for implementation/review when their jobs remain relevant.

Files under `planning/content/pages/` with `status: approved` are authoritative product content. Preserve wording, factual claims, CTA intent, hierarchy and approved SEO metadata unless implementation proves a genuine conflict; route such conflicts through scoped change control instead of silently rewriting copy.

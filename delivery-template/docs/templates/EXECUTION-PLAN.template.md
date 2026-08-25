# EXECUTION PLAN

## Strategy

## Execution Rightsizing
Reference `planning/execution/EXECUTION-PROFILE.yaml`. Classify `MICRO | SMALL | STANDARD | HIGH_RISK` from scope/coupling/risk/runtime/reversibility, then set milestone/job granularity, branching, review depth, evidence granularity and commit cadence accordingly. Quality floors never decrease.

## Stack baseline
Reference `planning/architecture/STACK-MANIFEST.yaml` (`STACK_READY`).

## Skill routing baseline
Reference `planning/execution/SKILLS-MANIFEST.yaml` (`SKILLSET_READY`).

## Program design baseline
Reference `planning/architecture/PROGRAM-DESIGN.md` for material cross-layer/cross-file structure. Keep simple jobs inline.

## Vertical-slice strategy
Identify the first executable end-to-end slices and any real dependency that requires horizontal work.

## Measurable outcomes
Map meaningful product/NFR outcomes to evidence; use `NONE` where no honest metric improves acceptance.

## Risk routing

## Model-routing strategy
Reference `config/MODEL-ROUTING-POLICY.yaml` and `planning/execution/MODEL-ROUTING-STATE.yaml`. Default bounded implementation to `EFFICIENT`; promote intrinsic complexity to `BALANCED`; reserve `FRONTIER` for orchestration, critical judgment/review and escalation. Record per-job minimum/requested class and independent-review class. Sol is capped at `high`.

## Single-writer surfaces

## Dependency graph

| Job | Depends On | Wave | Risk | Parallel Safe | Required Skills | Produces | Seam |
|---|---|---:|---|---|---|---|---|

## Waves

## Requirement coverage

## Skill coverage audit
Every implementation/review job must have the exact expertise needed by stack + domain + risk, and no unrelated specialists.


## Solution-minimization strategy
State likely reuse/native/stdlib opportunities and known justified complexity surfaces. Do not prescribe speculative abstractions.

## Convergence/evidence strategy
Define how requirement IDs map to jobs/code/tests/docs and which evidence must be fresh on the integrated candidate SHA.

## Microtask batching / bottleneck-aware parallelism
Identify same-shape microtasks that should share a dispatch versus substantive independent jobs that should run concurrently. State likely verification/integration bottlenecks and how writer WIP will be capped if they saturate.

## Worker liveness / recovery strategy
For any long-running/expensive delegated job, declare required capabilities, observable progress source, provider hard-deadline risk if known, and checkpoint/resume behavior. No universal numeric timeout. Quiet workers receive a health check before cancellation; known provider deadlines trigger checkpoint/resume where feasible.

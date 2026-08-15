# AUTOPILOT GOAL — V5.6.1

Status: READY_TO_START
Terminal target: `COMPLETED`

## Goal source
Use `GOAL.md`, requirements, architecture/ADRs, `planning/architecture/STACK-MANIFEST.yaml`, research artifacts and current repository/runtime evidence as the source of truth. Resolve `AUTO` technical fields autonomously when authority permits.

## Mandatory lifecycle

```text
PERSISTED_STATE_READ
→ HARNESS_READY
→ GITHUB_READY
→ PROJECT/REPO/SOURCE_READY
→ PLANNING_BASELINE_READY
→ STACK_READY
→ SKILLSET_READY
→ PROGRAM_DESIGN_READY_WHEN_MATERIAL
→ EXECUTION_DAG_READY
→ JOB/WAVE:
    JOB_BASELINE
    → PROGRAM_DESIGN_GATE_IF_MATERIAL
    → JIT_RESEARCH_IF_NEEDED
    → SKILL_LOAD
    → SOLUTION_MINIMIZATION_GATE
    → FIRST_EXECUTABLE_VERTICAL_SLICE_WHEN_POSSIBLE
    → EARLY_VERIFY_AND_RESTEER
    → IMPLEMENT/REPAIR/EXTEND
    → PRE_FIX_FAIL_POST_FIX_PASS_IF_BUG_AND_PRACTICAL
    → FALSIFIABLE TEST/EVIDENCE
    → FAILURE_MODE_CLOSURE_IF_TRIGGERED
    → DOCS FRESHNESS
    → REVIEW/VERIFY
    → EVIDENCE_REFRESH
→ INTEGRATE VALIDATED WAVE
→ PUSH/VERIFY REMOTE MAIN
→ REBUILD/RESTART/APPLY
→ HEALTH/SMOKE/BROWSER/NETWORK
→ NEXT WAVE
→ COMPLETED
```

## Planning baseline
Do not restart broad discovery/research already completed by the Custom GPT unless current repo/runtime evidence contradicts it. Classify execution-time research per job as `NONE`, `VERIFY_DRIFT`, `TARGETED`, or `SPIKE`.

Research must end in a decision. Routine technical choices are autonomous after sufficient evidence. Material findings update research register, ADR/STACK/SKILLS and future job routing.

## Stack and skill contract
- `STACK-MANIFEST.yaml` records actual selected/detected languages, frameworks, datastores, vector/search, infra/network and deployment.
- `SKILLS-MANIFEST.yaml` records project-selected skills; each job receives only its required subset.
- Every job names exact canonical `.agents/skills/<id>/SKILL.md` paths, reason and research need.
- Workers read those paths before work and return `SKILLS_APPLIED`.
- `references/` are progressive: load only references relevant to the job.
- No fixed skill-count limit; smallest complete job set wins.
- New material stack/change evidence triggers rerouting before affected future jobs.

## Autonomy
Continue automatically while dependency-ready work remains. Delegate bounded work to capable subagents. Use existing Goal persistence without competing persistence loops.

Request only the minimal restart action for `RESTART_REQUIRED`. Ask the user only for true `DECISION_REQUIRED`, `BLOCKED_EXTERNAL`, `POLICY_DENIED`, unrecoverable `RETRY_EXHAUSTED` or explicit `PAUSED`. Routine stack/library/config/refactor/test decisions must be researched and resolved autonomously.

## Git/GitHub
Reuse existing origin or create planned private-by-default repo under authenticated account. Commit completed jobs, push meaningful checkpoints, integrate only validated waves, respect branch/PR/check policy and keep remote `main` synchronized.

## Completion
Do not claim `COMPLETED` until requirements/acceptance are satisfied, mandatory routed skills/reviews are applied, targeted blocking findings are closed, latest validated `main` runs/applies successfully, relevant network/browser/runtime checks pass, and GitHub remote `main` contains the intended final validated state.


## Documentation freshness invariant
Before every commit: classify documentation impact, update affected README/docs in the same commit, record staged fingerprint and pass `DOCS_FRESHNESS_GATE`. Before every push: pass pre-push docs gate. Final `COMPLETED` requires `DOCUMENTATION_READY`, beginner README/feature coverage and fresh-user documentation review on the integrated SHA.

## Persistent state / context / concurrency invariant
Read and maintain `planning/execution/STATE.md` as the compact live snapshot. Update it after every meaningful job/wave/commit-push/runtime/blocker/restart/context/convergence boundary. Use fresh isolated agents for independent jobs/reviews/debugger escalation; persist truth to disk and rotate context epochs at semantic boundaries. Every wave maximizes **end-to-end throughput**, not agent count: identify the current bottleneck and avoid writer WIP that only queues before saturated integration/test/CI/review/runtime capacity. No fixed agent count; keep the operator/harness-selected model unchanged.


## V5.6.1 convergence invariant
Maintain `planning/execution/CONVERGENCE-MATRIX.json` and `EVIDENCE-INDEX.json`. Technical discoveries update planning/ADRs/jobs autonomously within authority and then reconverge. Affected evidence from an older SHA is stale. Final completion requires the current mandatory requirement set to be `CONVERGED`/authorized `WAIVED`, fresh required evidence, `DOCUMENTATION_READY`, runtime acceptance and intended remote-main state.

## V5.6.1 program/flow invariant
Every substantive implementation routes `solution-minimization-engineering`. Resolve consequential Program Design before broad code generation, prefer executable vertical slices and re-steer after the first high-impact slice if needed. Batch tiny same-shape tasks; parallelize real independent work only while it improves throughput. Use measurable outcomes as backpressure where honest/useful. After escaped/repeated failures close the failure mode with the smallest effective durable control. Use token-budgeted repo maps/semantic navigation only when repository scale warrants it; keep scratch private and parent handoffs compact.

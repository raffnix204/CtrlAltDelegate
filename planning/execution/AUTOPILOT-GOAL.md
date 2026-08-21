# AUTOPILOT GOAL — V5.8

Status: READY_TO_START
Terminal target: `COMPLETED`

## Goal source
Use `GOAL.md`, requirements, architecture/ADRs, `planning/architecture/STACK-MANIFEST.yaml`, research artifacts and current repository/runtime evidence as the source of truth. Resolve `AUTO` technical fields autonomously when authority permits.

## Mandatory lifecycle

```text
PERSISTED_STATE_READ
→ MODE_DETECTION
→ HARNESS_READY
→ GIT_GUARDS_READY
→ GITHUB_READY
→ PROJECT/REPO/SOURCE_READY
→ MODE BRANCH:
    FULL_LIFECYCLE:
      INTAKE
      → COLLABORATIVE_DISCOVERY
      → PREFERENCES_CONSTRAINTS_READY
      → DISCOVERY_READY
      → RESEARCH_READY
      → STACK_READY
      → ARCHITECTURE_READY
      → PROGRAM_DESIGN_READY_WHEN_MATERIAL
      → SKILLSET_READY
    RESUME_PLANNING:
      EARLIEST_UNRESOLVED_PLANNING_GATE
      → RECONVERGE_AFFECTED_ARTIFACTS
      → STACK_READY
      → PROGRAM_DESIGN_READY_WHEN_MATERIAL
      → SKILLSET_READY
    EXECUTION_HANDOFF:
      VALIDATE_PLANNING_BASELINE
      → RECONVERGE_ONLY_CONTRADICTED_ARTIFACTS
      → STACK_READY
      → SKILLSET_READY
    RESUME_EXECUTION:
      RECONCILE_GIT_STATE_RUNTIME_EVIDENCE
      → RESUME_EXACT_PERSISTED_ACTION
→ EXECUTION_RIGHTSIZING_GATE
→ EXECUTION_DAG_READY
→ JOB/WAVE:
    JOB_BASELINE
    → DELEGATION_CAPABILITY_GATE
    → WORKER_LIVENESS_AND_CHECKPOINT_POLICY_IF_NEEDED
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
A Custom GPT is optional. Detect whether planning is absent, partial, execution-ready or already executing. Fresh/`NOT_STARTED` repositories run the full collaborative lifecycle locally; partial planning resumes the earliest unresolved material gate; complete handoffs are validated rather than re-planned; interrupted execution resumes from disk. Reuse any current planning/repository/runtime evidence before classifying execution-time research per job as `NONE`, `VERIFY_DRIFT`, `TARGETED`, or `SPIKE`.

Research must end in a decision. Routine technical choices are autonomous after sufficient evidence. Material findings update research register, ADR/STACK/SKILLS and future job routing. See `docs/system/FULL-LIFECYCLE-ENTRY-AND-MODE-DETECTION.md`.

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


## V5.8 convergence invariant
Maintain `planning/execution/CONVERGENCE-MATRIX.json` and `EVIDENCE-INDEX.json`. Technical discoveries update planning/ADRs/jobs autonomously within authority and then reconverge. Affected evidence from an older SHA is stale. Final completion requires the current mandatory requirement set to be `CONVERGED`/authorized `WAIVED`, fresh required evidence, `DOCUMENTATION_READY`, runtime acceptance and intended remote-main state.

## V5.8 program/flow invariant
Every substantive implementation routes `solution-minimization-engineering`. Resolve consequential Program Design before broad code generation, prefer executable vertical slices and re-steer after the first high-impact slice if needed. Batch tiny same-shape tasks; parallelize real independent work only while it improves throughput. Use measurable outcomes as backpressure where honest/useful. After escaped/repeated failures close the failure mode with the smallest effective durable control. Use token-budgeted repo maps/semantic navigation only when repository scale warrants it; keep scratch private and parent handoffs compact.

## V5.8 adaptive execution / worker liveness invariant
Read `EXECUTION-PROFILE.yaml` before final DAG dispatch. `MICRO/SMALL` means fewer coherent milestones, fewer process-only branches/commits/reviews and milestone evidence; it never means weaker product quality. `STANDARD/HIGH_RISK` keeps or increases the required rigor. Route each worker only after its exact job capabilities are verified. For long-running workers, observable meaningful progress renews the lease; a quiet worker receives a health check; elapsed time alone does not justify cancellation. If a provider has a hard deadline, checkpoint beforehand when feasible and resume from the actual Git/files/checkpoint state afterward. Repeated stalls trigger resizing/capability rerouting/root-cause debugging, not blind restarts.


## Language invariant
Follow the user's language in conversation unless explicitly overridden. Keep CtrlAltDelegate-controlled planning, handoff, system and execution artifacts in English. Preserve intentionally localized product content when required by the project.

## V5.8 Control Gates

Before dispatch, reconcile `JOB-GRAPH.json`, `LOOP-STATE.json`, `SURFACE-POLICY.yaml`, artifact consistency and actual harness capabilities. Each repeated loop iteration needs a meaningful progress delta or a changed strategy. Use fast feedback while iterating, but require the project acceptance gate before final convergence.


## V5.8 skill-driven planning

Relevant specialist skills participate while planning decisions are made, not only after planning. Run an early capability scan during intake/discovery, consult the smallest complete planning skill set for the current phase, persist consultations in `planning/context/PLANNING-SKILL-STATE.yaml`, and refresh routing whenever scope, research or stack evidence changes. Use `config/PLANNING-SKILL-ROUTING.yaml` and `docs/system/SKILL-DRIVEN-PLANNING.md`. The final coding-agent skill pool continues from these decisions.

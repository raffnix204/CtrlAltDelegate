# Runtime Skill Escalation — V5.8.1

## Purpose
A worker may discover a missing specialist after dispatch. This is not automatically a project change. Runtime escalation preserves the immutable, hash-bound base brief and adds the smallest auditable delta needed.

## Escalation ladder

`L0_REFERENCE_LOAD -> L1_JIT_SKILL_INJECT -> L2_JOB_REBRIEF -> L3_SCOPED_CHANGE`

- **L0_REFERENCE_LOAD**: load one progressive reference from an already-authorized skill. No semantic job change.
- **L1_JIT_SKILL_INJECT**: grant one additional canonical skill when objective, requirements, acceptance, owned/prohibited scope and authority are unchanged.
- **L2_JOB_REBRIEF**: regenerate the same job's worker brief when worker capability, acceptance shape or owned job scope changes without changing project intent/architecture.
- **L3_SCOPED_CHANGE**: use normal change control when requirements, observable product behavior, architecture/shared contracts, security/privacy posture, data-loss risk, compliance or material recurring cost change.

## Deterministic state
The base worker brief is immutable. `planning/execution/SKILL-REQUESTS.jsonl` is append-only. Every granted L1 delta binds the base brief SHA-256, canonical skill path/SHA-256 and previous grant hash. The resulting effective brief hash is therefore reconstructable. A mismatch returns `STALE_BRIEF`.

`planning/execution/brief-deltas/` stores human-readable grant artifacts. `planning/execution/SKILL-USAGE-EVENTS.jsonl` records `RUNTIME_INJECTED` and `REFERENCE_LOADED` events for later maintenance analysis.

## Decision boundary
A missing skill is expertise, not automatically scope. Do not create a `CHG-*` record merely because a worker needs another canonical decision surface. Conversely, never use JIT injection to smuggle a changed requirement, new architecture boundary, weaker security posture, destructive action or business commitment past change control.

## Worker protocol
1. Worker reports the concrete missing skill/reference and why current authorized expertise is insufficient.
2. Orchestrator runs `scripts/resolve_skill_request.py` at a safe boundary.
3. Resolver verifies canonical existence and classifies L0-L3 using `config/SKILL-ESCALATION-POLICY.yaml`.
4. L0/L1 append a hash-chained event and continue. L2 creates a replacement brief. L3 enters scoped change control.
5. Completion evidence records the effective brief hash and skills actually applied.

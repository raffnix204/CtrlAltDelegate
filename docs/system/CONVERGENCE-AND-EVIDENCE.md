# Convergence & Evidence Contract — V5.6.4

## Goal
Completion means the implementation, tests/evidence and documentation match the current accepted requirements/design on the exact candidate state.

## Artifacts
- `planning/execution/CONVERGENCE-MATRIX.json`: requirement-level coverage chain.
- `planning/execution/EVIDENCE-INDEX.json`: compact SHA/environment/scope-bound evidence registry.
- `scripts/quality_gate.py`: deterministic structural/freshness validation.

## Convergence matrix fields
Each mandatory requirement should track:
- `id` and `status` (`OPEN | IMPLEMENTED | CONVERGED | WAIVED`);
- `plan_refs` / ADRs;
- `job_ids`;
- `code_paths` or explicit `non_code_reason`;
- `evidence_ids` or explicit evidence N/A rationale;
- documentation impact and canonical paths;
- notes for accepted deviations.

Do not mark `CONVERGED` from checkboxes alone. The linked evidence must support the requirement on the intended candidate SHA.

## Evidence freshness
Each evidence record states `id`, `kind`, `sha`, `environment`, `scope`, `status`, command/action and artifact pointers. Required evidence for final completion must be PASS and fresh for the candidate SHA unless its declared scope is provably independent of later changes.

When a change invalidates a prior result, mark/re-run it rather than overwriting history silently. Keep raw logs outside hot state and link them.

## Iterative plan correction
Implementation may reveal a wrong technical assumption. Within autonomous technical authority:
1. record the finding;
2. update ADR/plan/stack/skill/job artifacts affected;
3. update convergence mapping;
4. implement/repair;
5. collect fresh evidence;
6. continue without user interruption.

Escalate only for the standard hard-stop categories.

## Final gate
Before `COMPLETED`:
1. candidate SHA identified;
2. all mandatory requirements `CONVERGED` or explicitly authorized `WAIVED`;
3. required evidence PASS/fresh;
4. docs current and `DOCUMENTATION_READY`;
5. clean-room/runtime/browser/network acceptance as routed;
6. remote main contains the validated candidate when GitHub sync applies.


## Evidence attestation commit
Run product/runtime/test/documentation evidence on a committed **verified candidate SHA**. After verification, a final commit may update only canonical evidence/state attestation files. `quality_gate.py` permits this narrow post-candidate diff. Any code, configuration, test, build/runtime definition or user-facing documentation change after the verified candidate invalidates the affected evidence and requires a new candidate/reverification.

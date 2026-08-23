# Closed-Loop Control Architecture — V5.9

CtrlAltDelegate treats recurring agent behavior as explicit control loops rather than informal "repeat until done" instructions.

## Canonical loop model

Every material loop has:
- a stable `loop_id`;
- explicit triggers;
- machine-readable state;
- allowed and protected surfaces;
- a progress signature;
- success and continuation predicates;
- strategy-change and escalation rules;
- terminal outcomes.

The canonical registry is `config/LOOP-CONTRACTS.yaml`. Live state is `planning/execution/LOOP-STATE.json`.

## Progress-aware continuation

Before repeating an iteration, compare the new progress signature with the prior one. Meaningful progress is evidence such as a changed candidate SHA, a new validated artifact hash, a newly completed job, new runtime evidence, a changed failure signature, or a justified strategy change.

`same failure + same relevant state + no new evidence + no meaningful diff` is `NO_PROGRESS`, not permission for a blind retry.

On `NO_PROGRESS`, change strategy or escalate according to the loop contract. Repeated identical attempts are prohibited.

## Standard loops

V5.9 registers at least:
- `DISCOVERY_LOOP`;
- `RESEARCH_LOOP`;
- `PROGRAM_DESIGN_STEERING_LOOP`;
- `EXECUTION_LOOP`;
- `REPAIR_LOOP`;
- `WORKER_LIVENESS_LOOP`;
- `CONVERGENCE_LOOP`;
- `CONTEXT_RESUME_LOOP`;
- `PARALLELISM_LOOP`;
- `FAILURE_MODE_CLOSURE_LOOP`.

## Fast feedback vs acceptance

Loops may run a cheap `FAST_FEEDBACK_GATE` while iterating. Completion requires the broader `ACCEPTANCE_GATE` defined by project risk and requirements. A passing fast gate never substitutes for final integration/runtime/security/documentation/convergence evidence when those are required.

## State ownership

The control state is persisted outside conversational memory. Chat history is never the sole source of loop position. After restart, reconstruct from Git/project state plus CtrlAltDelegate planning/control artifacts and continue from the earliest safe unresolved action.

## V5.9 no-progress enforcement
`record_loop_attempt.py` rejects reuse of the same strategy when the same failure signature produced `NO_PROGRESS`. A retry must introduce new evidence or a changed strategy such as focused diagnosis, fresh debugger, job resize, capability reroute or architecture review. This is a control-plane rule, not a suggestion.

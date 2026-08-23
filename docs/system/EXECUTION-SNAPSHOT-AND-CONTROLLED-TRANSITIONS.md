# Execution Snapshot & Controlled Transitions — V5.9

CtrlAltDelegate keeps normalized source-of-truth artifacts but exposes one generated execution view: `planning/execution/EXECUTION-SNAPSHOT.json`. `STATE.md` is a generated human-readable projection, not an independent manually maintained truth.

`refresh_job_readiness.py` derives which planned jobs are currently runnable from dependency gates and execution blockers; verification blockers never remove implementation-ready work. `build_execution_snapshot.py` then derives the current view from Git, JOB-GRAPH, blockers, deferred validation, convergence/evidence, user-journey oracles, provider attestations, product/runtime preflight and product-drift review. Regenerate readiness plus snapshot after material execution/verification transitions and before restart/handoff.

Jobs may move to `IMPLEMENTED_UNVERIFIED` through `transition_job.py` when implementation evidence exists but final proof remains pending. That state satisfies ordinary `IMPLEMENTATION` dependencies but is not completion. Jobs may move to terminal `DONE` only through the same controlled transition after acceptance/evidence/journey/provider/blocker predicates pass. Directly editing a job to `DONE` violates the control contract.

Project completion remains separately fail-closed through `validate_product_completion.py` because completion is a product/runtime assertion, not merely a DAG bookkeeping state.

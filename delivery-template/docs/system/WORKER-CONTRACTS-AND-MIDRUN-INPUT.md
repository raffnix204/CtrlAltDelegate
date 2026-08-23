# Worker Contracts and Mid-Run Input — V5.8.2

Delegated work uses an explicit worker contract: purpose, required capabilities, permission class, allowed scope, protected/prohibited scope, dependencies, done-when predicates, required evidence, output/report path and interruption/checkpoint behavior. A worker is not trusted merely because it was spawned.

Use native harness tool filters, sandbox modes, permissions and structured output when available. Unsupported required capabilities fail loud or reroute.

Long-running orchestration also maintains `planning/execution/PENDING-INPUT.jsonl`. New user/external input is admitted at safe orchestration boundaries, classified for authority and impact, then either applied locally, causes scoped invalidation/replanning, or becomes a hard-stop decision. Do not redirect a turn already underway when the harness cannot safely steer it; queue the input for the next safe step.

## V5.8.2 worker-brief integrity
Substantive delegated jobs should use hash-bound authority pointers. A worker verifies the required pointer hashes before acting; mismatch returns `STALE_BRIEF` for orchestrator reconciliation. After a final report is collected, persist it and terminate the worker unless a concrete continuation need and trustworthy continuable-session capability exist.

## V5.8.2 runtime skill escalation
A worker may request missing canonical expertise at a safe boundary. Route the request through `config/SKILL-ESCALATION-POLICY.yaml` and `scripts/resolve_skill_request.py`. L0/L1 append evidence without replacing the base brief; L2 issues a new brief revision for the same job; L3 uses scoped change control. Never mutate a signed/hash-bound brief in place.

## V5.8.2 completion claims
Workers may report implementation complete while verification remains pending, but must not label a job `DONE` themselves. Reports distinguish `implementation_status`, `verification_status`, evidence types, assumptions and blocker class. The orchestrator applies controlled transition gates and continues independent jobs when verification-only prerequisites are missing.

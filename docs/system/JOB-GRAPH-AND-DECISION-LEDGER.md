# Machine-Readable Job Graph and Decision Ledger — V5.9

`planning/execution/JOB-GRAPH.json` is the canonical machine-readable execution graph. Human-oriented execution plans may summarize it but must not silently disagree with it.

A job records dependencies, status, requirement coverage, allowed/protected scope, required worker capabilities, routed skills, verification, claim state and produced artifacts. `READY` is derived from dependency and policy state rather than guessed from prose.

## Job states

`PLANNED | BLOCKED | READY | CLAIMED | RUNNING | IMPLEMENTED_UNVERIFIED | VERIFYING | DONE | FAILED | CANCELLED`


`IMPLEMENTED_UNVERIFIED` is a deliberate continuation state: the job has produced the planned implementation surface, but final proof is unavailable or still pending. It is **not** `DONE`. By default, downstream implementation dependencies may proceed from `IMPLEMENTED_UNVERIFIED`, while dependencies that explicitly declare `gate: VERIFIED` require `DONE`. A `VERIFICATION_BLOCKER` therefore does not unnecessarily freeze the remaining implementation DAG.

Dependencies may be legacy string IDs (interpreted as `IMPLEMENTATION`) or explicit objects:

```json
{"job_id": "JOB-010", "gate": "IMPLEMENTATION"}
{"job_id": "JOB-011", "gate": "VERIFIED"}
```

Run `scripts/refresh_job_readiness.py --write` after a job transition or blocker change. `EXECUTION_BLOCKER` affects only its declared job/subgraph unless the fail-closed global-blocker rule is satisfied; `VERIFICATION_BLOCKER` never removes otherwise-ready implementation work.

Concurrent workers must not silently claim the same single-writer surface. When the harness offers atomic claims, use them. Otherwise the orchestrator remains the single claim authority and persists the claim before dispatch.

## Decision ledger

Routine technical rulings that materially affect execution but do not justify a full ADR are appended to `planning/execution/DECISION-LEDGER.jsonl`.

Each ruling should capture decision id, scope/job, conflict or question, authority used, ruling, reason, evidence/source pointers, cost if wrong, and candidate SHA when relevant. The ledger is append-only. Superseding a ruling adds a new record referencing the old id.

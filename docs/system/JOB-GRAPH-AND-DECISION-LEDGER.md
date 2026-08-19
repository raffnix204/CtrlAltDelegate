# Machine-Readable Job Graph and Decision Ledger — V5.7.1

`planning/execution/JOB-GRAPH.json` is the canonical machine-readable execution graph. Human-oriented execution plans may summarize it but must not silently disagree with it.

A job records dependencies, status, requirement coverage, allowed/protected scope, required worker capabilities, routed skills, verification, claim state and produced artifacts. `READY` is derived from dependency and policy state rather than guessed from prose.

## Job states

`PLANNED | BLOCKED | READY | CLAIMED | RUNNING | VERIFYING | DONE | FAILED | CANCELLED`

Concurrent workers must not silently claim the same single-writer surface. When the harness offers atomic claims, use them. Otherwise the orchestrator remains the single claim authority and persists the claim before dispatch.

## Decision ledger

Routine technical rulings that materially affect execution but do not justify a full ADR are appended to `planning/execution/DECISION-LEDGER.jsonl`.

Each ruling should capture decision id, scope/job, conflict or question, authority used, ruling, reason, evidence/source pointers, cost if wrong, and candidate SHA when relevant. The ledger is append-only. Superseding a ruling adds a new record referencing the old id.

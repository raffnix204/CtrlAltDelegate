# State Reconciliation and Recovery — V5.9

Reconciliation runs before dispatch and at restart/context boundaries. It detects all relevant drift before repair, applies only deterministic safe repairs, and fails closed on ambiguous authority conflicts.

## Repair phases

1. **Integrity** — protected control surfaces and revision consistency.
2. **Execution ownership** — expired claims, orphan attempts, claim/attempt mismatch.
3. **Semantic state** — completion invariant drift, blocker/evidence/provider inconsistencies.
4. **Projection** — readiness and execution snapshot drift.

A derived projection may be regenerated automatically. A manually altered authoritative control surface is not silently accepted.

## Recovery as a domain operation

Failures are classified, given a stable failure signature, then routed to one explicit recovery action:

- `RETRY`
- `REPAIR`
- `REMEDIATE`
- `REBRIEF`
- `REPLAN`
- `DEFER_VALIDATION`
- `EXTERNAL_BLOCK`
- `ABORT`

Each recovery action records the failed attempt, class, evidence/rationale, strategy and timestamp in `RECOVERY-ACTIONS.jsonl`. The same failure with the same no-progress retry strategy is rejected.

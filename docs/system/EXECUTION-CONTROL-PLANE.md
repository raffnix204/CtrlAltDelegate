# Execution Control Plane — V5.9

V5.9 moves CtrlAltDelegate from contract-guided state files to a revisioned, receipt-backed execution control plane.

## Invariants

1. **JOB != ATTEMPT.** A job is durable planned work; an attempt is one leased execution of that job.
2. **WORKER OUTPUT != STATE AUTHORITY.** Workers return a schema-valid result claim. Controllers decide state transitions.
3. **ONE ACTIVE CLAIM PER JOB.** Claims have a worker identity, token hash, heartbeat and lease expiry.
4. **STALE WRITES FAIL.** Mutable control operations may supply an expected control revision. A mismatch returns `STALE_STATE_RECONCILE`.
5. **DIRECT CONTROL EDITS ARE NON-AUTHORITATIVE.** Protected file hashes are sealed in `CONTROL-STATE.json`; controllers create mutation receipts.
6. **DONE IS RECOMPUTED.** Final gates re-run job invariants and do not trust a persisted `DONE` string.

## Dispatch lifecycle

```text
RECONCILE
  -> READY
  -> CLAIM JOB
  -> START ATTEMPT
  -> HEARTBEAT WHILE ACTIVE
  -> STRUCTURED WORKER RESULT
  -> SETTLE ATTEMPT
  -> VERIFY / RECOVER
  -> CONTROLLED JOB TRANSITION
```

## State

- `planning/execution/CONTROL-STATE.json` — current revision and sealed hashes.
- `planning/execution/CONTROL-MUTATION-LOG.jsonl` — append-only mutation receipts.
- `planning/execution/CONTROL-EVENTS.jsonl` — append-only semantic event history.
- `planning/execution/WORKER-CLAIMS.json` — active/released lease projection.
- `planning/execution/JOB-ATTEMPTS.jsonl` — attempt event history.
- `planning/execution/ATTEMPT-STATE.json` — materialized current attempt projection.

Use the controller scripts rather than directly editing these states after planning handoff.

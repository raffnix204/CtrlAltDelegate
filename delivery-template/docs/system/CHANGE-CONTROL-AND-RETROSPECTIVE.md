# Scoped Change Control and Retrospective — V5.8.1

When implementation evidence or new user input materially changes the plan, decide whether it is the same intent or a new change.

- Same intent, learning-driven correction, narrowed scope, or implementation-discovered design adjustment: update the existing scoped change and invalidate only affected artifacts/evidence.
- Fundamentally different intent, independently deliverable scope, or large scope expansion: create a new change record.

Large STANDARD/HIGH_RISK work may use `planning/changes/CHG-*/` with `CHANGE.yaml`, requirement/design deltas, affected jobs and evidence. MICRO/SMALL work may record the same decision in the decision ledger without directory ceremony.

After major delivery or repeated repair, run an evidence-based retrospective. Findings require source/evidence pointers. Project-local learnings may be recorded immediately. A reusable/global learning becomes an append-only `LEARNING-CANDIDATE` and must survive repeat evidence plus evaluation before changing a canonical global skill/contract. A single unusual project must not self-modify the global framework.

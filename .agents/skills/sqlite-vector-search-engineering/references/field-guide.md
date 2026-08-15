# SQLite Vector Search — Deep Reference

## Current research baseline (2026-08-12)
- SQLite's official Vec1 extension provides ANN vector search through SQLite virtual tables; treat its current capabilities/version as drift-prone and re-check sqlite.org before relying on a specific algorithm, distance, build flag or release number.
- `sqlite-vec` remains a separate third-party extension with broad language bindings and a pre-v1 compatibility warning. Use it only when its runtime/package fit is better than the project's available official SQLite capability and record the choice.
- Hybrid retrieval can combine SQLite FTS5 lexical retrieval with vector retrieval; evaluate it on representative queries rather than assuming vector-only quality.

## Decision checklist
1. exact SQLite build/runtime and loadable-extension policy;
2. extension/provider and license;
3. embedding model/dimension/version;
4. distance metric and normalization;
5. exact vs ANN requirements;
6. metadata/tenant filtering;
7. FTS5/hybrid fusion;
8. index rebuild/migration strategy;
9. local vs remote embedding privacy;
10. retrieval evaluation dataset and latency/index-size budget.

## Revalidation triggers
Re-research when SQLite, the vector extension, binding, embedding model, deployment platform or required vector dimension changes.

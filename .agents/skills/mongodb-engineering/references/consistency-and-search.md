# MongoDB Consistency, Transactions & Search

Single-document writes are atomic and should inform aggregate/document boundaries. Use multi-document transactions when the invariant truly spans documents and cannot be redesigned safely; keep them short.

Read/write concern and retry settings trade latency/availability/durability. Product idempotency is still required for operations that trigger external side effects.

Atlas Search and Vector Search have different index/config/query semantics from ordinary B-tree indexes. Hybrid retrieval combines lexical and vector signals; define ranking/evaluation and index freshness expectations explicitly.

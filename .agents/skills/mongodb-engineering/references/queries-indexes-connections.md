# MongoDB Queries, Indexes & Connections

Inspect `explain` execution stats, docs/keys examined and stage fan-out. Compound index order should reflect equality fields, then sort/range tradeoffs for the actual query. Avoid redundant indexes whose prefixes already cover another pattern unless evidence justifies both.

In aggregation, push selective `$match`/projection early when semantics allow and inspect `$lookup` cardinality before unwinding large arrays.

Reuse driver clients/pools according to runtime guidance. Compute total connections from process/function concurrency; arbitrary large `maxPoolSize` can make contention worse.

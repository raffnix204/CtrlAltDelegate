# PostgreSQL Query Plans & Indexes

Start with the actual SQL and representative parameters. ORM intent is not query evidence. Capture plan nodes, estimated vs actual rows, loops, buffers and sort/hash spill where available.

Index design questions:
- Which equality/range predicates are selective?
- Which columns determine join/order?
- Can a partial index encode the hot subset?
- Would an INCLUDE/covering approach reduce heap visits enough to justify storage/write cost?
- Does expression/collation/operator class match the query?

Avoid duplicate/overlapping indexes. After adding one, prove the target plan improves and inspect write/storage impact.

For deep pagination, keyset requires deterministic ordering including a tie-breaker. Cursor contents should represent that ordering and be validated as untrusted input.

Query efficiency includes bytes transferred. Wide `SELECT *`, unbounded lists and join multiplication can be expensive even when execution time is low.

# Cloudflare Storage & Durable State

Select by semantics:
- KV: globally distributed key/value reads with its documented consistency model; good for config/cache-like data, not coordination locks.
- R2: object/blob storage and streaming object access.
- D1: Cloudflare-managed SQL database; verify current transaction/replication/query behavior before relying on generic SQLite assumptions.
- Durable Objects: single-object coordination/state ownership for keys/rooms/sessions needing serialized access.
- Queues/Workflows: asynchronous durable processing when request lifecycle is the wrong owner.

For Durable Objects choose a stable object ID/sharding strategy and define what one object serializes. Too much state behind one object can become a bottleneck; too little can break required coordination.

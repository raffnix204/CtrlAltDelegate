# Laravel Eloquent, Transactions & Queues

Inspect relationship access in Resources, accessors and views; those layers frequently reintroduce N+1 after the controller query appears optimized. Select only required columns when wide records/large relations matter.

Transaction ownership should match a domain use case. External side effects that cannot roll back need an outbox/idempotency/after-commit design rather than pretending they are atomic with SQL.

Queue retries imply at-least-once-like duplicate execution unless the selected driver/worker contract proves otherwise. Use stable idempotency keys or durable completion markers for consequential actions.

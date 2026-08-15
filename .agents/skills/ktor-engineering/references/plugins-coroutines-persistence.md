# Ktor Plugins, Coroutines & Persistence

Map installed plugins in the order they affect requests. For a failing auth/error/serialization path, inspect pipeline phase/order before adding workaround code.

Request-scoped coroutine work inherits cancellation unless explicitly designed otherwise. Durable asynchronous work should move to a queue/scheduler with its own retry/idempotency contract rather than a fire-and-forget coroutine.

Do not keep DB transactions open while awaiting unrelated remote services. Fetch/compute outside the transaction when consistency permits, or design the workflow explicitly when it does not.

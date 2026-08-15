# Rails Active Record, Transactions & Jobs
## When to read this reference

Read this reference when **active record transactions jobs** is material to the current rails engineering decision, failure path, compatibility question or verification plan. Do not preload it for unrelated jobs.

Association loading must be checked where records are actually rendered/serialized. `includes`/preload choices can change query count and data volume; measure the path rather than applying one pattern globally.

Use DB uniqueness/check/FK constraints for invariants that must survive races and non-Rails writers. Translate constraint errors into product-friendly failures where needed.

Callbacks before commit cannot safely trigger irreversible external actions that assume persistence succeeded. Prefer after-commit/durable job/outbox approaches and idempotency for retryable work.

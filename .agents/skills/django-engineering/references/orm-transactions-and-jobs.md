# Django ORM, Transactions & Jobs

A QuerySet describes a query until evaluated. Inspect where iteration, serialization, templates or relationship access forces additional queries. Prefetch strategy must match the access graph, not only the first view function line.

For concurrent invariants prefer database uniqueness/check/foreign-key constraints and transaction/locking/upsert patterns over application-only existence checks.

Background jobs that depend on newly written rows should be scheduled from an after-commit boundary when the queue/library supports it. Jobs should tolerate duplicate delivery where the queue contract permits retries.

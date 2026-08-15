# FastAPI Dependencies, Async & Transactions
## When to read this reference

Read this reference when **dependencies async transactions** is material to the current fastapi engineering decision, failure path, compatibility question or verification plan. Do not preload it for unrelated jobs.

A dependency that acquires a DB session/client/lock owns a cleanup path. Verify cleanup after response errors and cancellation, not only success.

`async def` is not a performance annotation. Trace every blocking library call. If the project uses sync DB/SDK clients, use the framework/runtime-supported isolation path or keep an appropriately managed sync endpoint rather than blocking the event loop silently.

Prefer transaction ownership in a service/use-case boundary that can cover all required writes. Repositories should not commit behind the caller unless that is an explicit contract.

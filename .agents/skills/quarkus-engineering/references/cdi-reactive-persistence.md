# Quarkus CDI, Reactive & Persistence
## When to read this reference

Read this reference when **cdi reactive persistence** is material to the current quarkus engineering decision, failure path, compatibility question or verification plan. Do not preload it for unrelated jobs.

Application scope is process lifetime. Do not put request/user mutable data there. Request scope or explicit method/context passing should reflect ownership.

Reactive handlers require non-blocking dependencies throughout the hot path. If a required library blocks, use the framework-supported worker/offload pattern or choose the imperative stack rather than pretending the call is reactive.

Keep ORM transaction/session boundaries aligned with use cases. Inspect lazy relation access after session closure and generated queries for N+1.

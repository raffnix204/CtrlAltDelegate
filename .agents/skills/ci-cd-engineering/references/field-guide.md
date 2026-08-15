# CI/CD — Deep Reference
## When to read this reference

Read this reference when **field guide** is material to the current ci cd engineering decision, failure path, compatibility question or verification plan. Do not preload it for unrelated jobs.

Treat CI as executable production policy.

## Required graph
source checkout → deterministic dependencies → lint/type/static checks → unit → integration/contracts → build/package → security/supply-chain evidence → deployment artifact → environment deploy → migration gate → health/smoke/E2E → promotion.

Not every project needs every node. Remove only nodes that are genuinely not applicable; never hide them in an opaque all-in-one shell job.

## Optimization order
correctness → determinism → observability → caching → parallelism/sharding → runner sizing. Measure before optimizing.

# Cloudflare Workers Runtime & Bindings
## When to read this reference

Read this reference when **workers runtime and bindings** is material to the current cloudflare platform engineering decision, failure path, compatibility question or verification plan. Do not preload it for unrelated jobs.

Workers instances are not durable processes. Module initialization may be reused, but correctness must survive isolate reuse/eviction. Keep only safe immutable/cache hints in globals; never authoritative user/session/coordination state.

Await promises that must complete before success. For intentionally post-response work, use the runtime-supported execution context mechanism and design observability/retry accordingly.

Prefer streams for large upstream/downstream bodies. Verify dependency compatibility with the active runtime/Node-compat mode rather than assuming an npm package works because TypeScript compiles.

Bindings and compatibility settings in Wrangler are deployment contract. Keep secrets out of plain vars and source.

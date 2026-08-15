# GraphQL Resolvers, Batching & Security
## When to read this reference

Read this reference when **resolvers batching security** is material to the current graphql engineering decision, failure path, compatibility question or verification plan. Do not preload it for unrelated jobs.

N+1 is caused by resolver execution shape. Batch by stable key within one request/context and ensure loader cache keys include any authorization/tenant dimension required for safe reuse.

Authorization can occur at service/data layer or resolvers, but every path must converge on the same resource policy. Test queries that reach the same field through different parents/aliases/fragments.

Cost controls can combine maximum page sizes, field-specific weights, depth/complexity limits, persisted operations and rate limits. Validate the model with real expensive queries rather than trusting one generic threshold.

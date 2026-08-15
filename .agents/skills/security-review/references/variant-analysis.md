# Security Variant Analysis
## When to read this reference

Read this reference when **variant analysis** is material to the current security review decision, failure path, compatibility question or verification plan. Do not preload it for unrelated jobs.

After confirming a vulnerability, extract the root pattern rather than only the exact syntax: missing authorization before object lookup, unsafe path join, signature verification after side effect, tenant filter omitted in helper, etc.

Search semantically for sibling implementations, shared helpers and alternate transports. Validate each candidate independently; do not mass-fix matches without proving the same invariant applies.

Add the smallest durable prevention: shared safe primitive, static rule, property test, negative regression or API redesign depending on root cause.

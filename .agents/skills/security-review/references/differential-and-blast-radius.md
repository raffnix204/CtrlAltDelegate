# Security Differential Review & Blast Radius
## When to read this reference

Read this reference when **differential and blast radius** is material to the current security review decision, failure path, compatibility question or verification plan. Do not preload it for unrelated jobs.

For a security-sensitive diff, triage changed entry points, authentication/authorization, validation, serialization, cryptography/secrets, persistence and external effects. Then trace callers/callees of the highest-risk changes.

Use git history/blame on removed checks or weakened conditions to understand the invariant they previously protected. A deleted validation branch may encode a historical incident fix.

Blast radius evidence can include number/type of callers, trust boundaries crossed, public API exposure, data migration impact and whether tests cover affected paths. Review the changed behavior, not only changed lines.

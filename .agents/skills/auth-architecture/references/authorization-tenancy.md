# Authorization, Tenancy & Service Identity
## When to read this reference

Read this reference when **authorization tenancy** is material to the current auth architecture decision, failure path, compatibility question or verification plan. Do not preload it for unrelated jobs.

Model authorization as subject + tenant/org + resource + action + contextual policy. UI roles are presentation; the server/data boundary enforces access.

Tenant membership, resource ownership and global/admin privileges are separate dimensions. Test same-role wrong-tenant and same-tenant wrong-owner paths.

Service identities need separate credentials/scopes/lifecycle from human sessions. Do not reuse an admin user token as an internal service credential merely because it is convenient.

# PostgreSQL Transactions, Locks & RLS
## When to read this reference

Read this reference when **transactions locks rls** is material to the current postgres engineering decision, failure path, compatibility question or verification plan. Do not preload it for unrelated jobs.

For a race, write the interleaving between two transactions and identify the invariant that must hold. Then choose constraint/upsert/row lock/advisory lock/isolation strategy that closes that interleaving.

Deadlock fixes should remove inconsistent lock ordering or reduce transaction scope; retry is the final recovery mechanism, not the primary design.

RLS policy review includes:
- which database role the app actually uses;
- how tenant/user identity enters the session/query;
- permissive vs restrictive policy composition;
- policies for SELECT/INSERT/UPDATE/DELETE and WITH CHECK;
- owner/superuser/BYPASSRLS behavior;
- indexes for policy predicates;
- tests attempting cross-tenant/object access.

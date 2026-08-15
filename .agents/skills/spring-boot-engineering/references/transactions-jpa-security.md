# Spring Transactions, JPA & Security
## When to read this reference

Read this reference when **transactions jpa security** is material to the current spring boot engineering decision, failure path, compatibility question or verification plan. Do not preload it for unrelated jobs.

`@Transactional` is normally applied through a proxy. Calls that never cross the proxy boundary may not get the advertised transaction. Put transaction ownership on a clear public service/use-case entry point and test rollback behavior rather than trusting annotations.

JPA fetch strategy is a query-design choice. Inspect SQL/query count around serializers and loops; avoid global eager relationships as an N+1 workaround.

Spring Security combines authentication filters, request authorization and optional method authorization. Verify denied as well as allowed cases and ensure alternate endpoints cannot bypass resource checks.

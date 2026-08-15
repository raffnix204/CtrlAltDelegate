# PostgreSQL Connections & Operations

Compute the upper bound of simultaneous connections from instances × workers × pools, including migrations/jobs/admin tools. Managed proxies/poolers can change transaction/session semantics; verify whether prepared statements, session variables or RLS context depend on session affinity.

For serverless workloads, reuse connections according to runtime/provider guidance and avoid creating a full pool per invocation when the platform multiplexes concurrency differently.

Operational evidence may include `pg_stat_activity`, `pg_stat_statements`, lock views, connection saturation, replication/backup status and provider metrics. Use `database-operations` for broader backup/failover/tuning ownership.

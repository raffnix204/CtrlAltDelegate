---
name: wordpress-engineering
description: "Use when the task materially involves this skill's owned domain: Engineer WordPress plugins/themes/blocks, REST endpoints, hooks, cron and operations with capability/nonce boundaries, safe database APIs, lifecycle hooks, performance and WP-CLI-aware deployment."
---

# WordPress Engineering

## Purpose / Ownership

Engineer WordPress plugins/themes/blocks, REST endpoints, hooks, cron and operations with capability/nonce boundaries, safe database APIs, lifecycle hooks, performance and WP-CLI-aware deployment.

Own the domain-specific judgment only. Shared autonomy, escalation, research, minimization, evidence and routing rules come from `docs/system/SKILL-EXECUTION-CONTRACT.md`.

## Activation & Negative Triggers

- WordPress plugin/theme/block/REST development.
- WordPress hook/cron/database/performance/security defect.
- WP-CLI migration/ops or plugin release packaging.
- Do not activate for adjacent work that does not materially touch this responsibility.

## Context To Inspect

- WordPress/PHP versions, site type/multisite and hosting constraints.
- Plugin/theme/block architecture and activation/uninstall behavior.
- Roles/capabilities/nonces/REST auth and stored data ownership.
- Cron/object cache/page cache/CDN and WP-CLI availability.

## Expert Decision Model

1. Use hooks/actions/filters as extension points with explicit ownership and priority; do not hide required domain ordering in a web of callbacks that cannot be traced.
2. Authorization requires capability checks for the specific operation. Nonces help protect intent/CSRF but are not authorization and may expire.
3. Validate/sanitize input according to type and context; escape output at the final rendering context. Use `$wpdb->prepare`/core APIs for SQL rather than string concatenation.
4. Define activation, upgrade and uninstall separately. Uninstall/data deletion is a product decision and must not destroy content merely because a plugin deactivates.
5. Use Settings/Options/metadata/custom tables from access/update shape. Watch autoloaded options and unbounded metadata/query patterns on high-traffic sites.
6. REST routes declare methods, permission callbacks and argument validation. Public route registration without a meaningful permission callback is a security review trigger.
7. WP-Cron is traffic/process dependent in many deployments; consequential scheduled work needs idempotency, observability and hosting-appropriate real cron/queue strategy.
8. Profile WordPress performance from queries, autoloaded options, object/page caching, remote HTTP, hooks and cron before adding caches/plugins.
9. Use WP-CLI for repeatable operational changes where available, especially search-replace/import/export/cache/cron tasks, with backups and dry-run support.

## Critical Invariants

- Nonce alone never authorizes privileged operation.
- Output escaping matches HTML/attribute/URL/JS context.
- Deactivation cannot delete user content; destructive uninstall is explicit.
- Database changes use versioned upgrade path and preserve rollback/backup expectations.
- Cron/job execution is safe under duplicate/late runs.

## Failure Modes / Sharp Edges

- REST route permission callback returns true too broadly or omitted.
- Nonce verified but capability/resource ownership not checked.
- Options set to autoload large data and slow every request.
- Plugin activation runs expensive/destructive migration synchronously without recovery.
- `wp_cron` assumed exact-time scheduler for business-critical job.
- Search-replace performed on serialized data with generic SQL/text tool.
- Output sanitized at input but not escaped for final context.

## Version / Drift Triggers

- WordPress major/PHP compatibility.
- Block/Interactivity/REST APIs and newly introduced capabilities.
- Plugin directory packaging/security requirements if publishing.

## Domain-Specific Verification

- Run WordPress/PHP lint/static tests available in repo.
- Test REST/admin/action unauthorized and nonce-expired paths.
- Exercise activate/deactivate/upgrade/uninstall on disposable site with backup.
- Profile query/autoload/cron/cache changes before/after.
- Verify release package excludes dev/secrets and works on supported WP/PHP matrix.

## Progressive References

- `plugin-security-lifecycle.md` — hooks, capabilities/nonces, input/output, activation/upgrades/uninstall
- `rest-blocks-operations-performance.md` — REST/blocks, cron, WP-CLI and performance diagnosis

Read only the reference whose topic is material to the current job.

## Companion Skills

- `php-engineering`
- `security-review`
- `database-migrations`
- `performance-profiling`
- `release-package-engineering`

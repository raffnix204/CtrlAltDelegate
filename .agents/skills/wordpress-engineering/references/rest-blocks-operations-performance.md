# WordPress REST, Blocks, Operations & Performance
## When to read this reference

Read this reference when **rest blocks operations performance** is material to the current wordpress engineering decision, failure path, compatibility question or verification plan. Do not preload it for unrelated jobs.

REST routes need explicit methods, permission callbacks, argument schemas/validation and stable response/error contracts. Test them without relying on wp-admin UI restrictions.

For blocks/interactivity use the project WordPress version's current registration/build APIs and preserve editor/frontend parity.

Operational diagnosis can use WP-CLI to inspect cron, options, plugins, DB and caches. For performance inspect query counts/slow queries, autoloaded option size, object/page cache hit behavior, remote HTTP and expensive hooks before installing another optimization plugin.

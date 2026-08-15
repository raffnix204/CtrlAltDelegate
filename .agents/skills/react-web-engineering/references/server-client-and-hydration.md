# React Server/Client & Hydration Boundaries
## When to read this reference

Read this reference when **server client and hydration** is material to the current react web engineering decision, failure path, compatibility question or verification plan. Do not preload it for unrelated jobs.

## Boundary model

Server-capable React frameworks may execute components in different environments. Determine where code runs before importing filesystem, database, secret, browser or native-only modules.

Crossing a server-to-client boundary should use a deliberately serializable public shape. Avoid passing framework/database objects, open handles, class instances or functions unless the active framework explicitly supports the mechanism.

## Hydration

Hydration requires the initial client tree to agree with server output. Typical mismatch causes:

- `window`, locale/timezone or random values read during initial render;
- browser extensions or client-only storage changing initial markup;
- invalid HTML nesting repaired differently by the browser;
- server/client feature flags or auth state derived from different sources;
- mutable module globals shared across requests.

Prefer deterministic server output and move truly browser-only state behind a post-hydration boundary without hiding real structural mismatches.

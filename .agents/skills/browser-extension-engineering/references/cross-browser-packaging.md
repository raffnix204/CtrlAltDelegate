# Extension Cross-Browser & Packaging
## When to read this reference

Read this reference when **cross browser packaging** is material to the current browser extension engineering decision, failure path, compatibility question or verification plan. Do not preload it for unrelated jobs.

Keep browser-specific API/manifest branches localized. Test install, update, permission grant/revoke, private/incognito behavior if supported, SPA navigation and storage migration.

Package from a clean/reproducible build. Inspect final manifest, permissions and included files. Store privacy/permission declarations must describe the shipped artifact rather than developer intent.

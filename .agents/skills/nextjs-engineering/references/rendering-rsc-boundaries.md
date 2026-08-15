# Next.js Rendering & RSC Boundaries

## Rendering decision

For each route/subtree record whether content is public/static, revalidated, request-personalized, streamed or client-interactive. Keep the most stable content outside request-dependent boundaries when the framework permits it.

## RSC / Client boundary

A Client Component boundary expands the client module graph. Place it as low as practical around interaction that genuinely needs browser state/effects. Server Components may fetch/use server-only capabilities directly; Client Components receive a deliberately serializable view model.

Use `server-only`/project-equivalent safeguards when available for modules whose accidental client import would be a security or bundle defect.

## Hydration

Investigate hydration errors rather than suppressing warnings. Compare server HTML and first client render; inspect invalid nesting, random/time/locale values, browser API reads, conditional auth/feature state and third-party DOM mutation.

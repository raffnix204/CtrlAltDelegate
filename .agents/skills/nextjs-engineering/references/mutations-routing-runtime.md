# Next.js Mutations, Routing & Runtime

## Mutations

Server Actions and Route Handlers are externally invocable server surfaces even if only your UI currently calls them. Enforce authentication, resource authorization, input validation and durable invariants inside the server path. Use database transaction/idempotency patterns when retries or multi-write consistency matter.

## Route boundaries

Use route-level `loading`, `error`, `not-found` and redirect behavior to encode product recovery. Do not convert unexpected server errors into success-shaped responses merely to keep rendering alive.

## Runtime

Before selecting edge/serverless/Node placement, inspect dependency support, filesystem/process/native addon needs, connection model, long-running/background behavior and provider limits. Keep heavyweight or native dependencies in a runtime that supports them rather than polyfilling by accident.

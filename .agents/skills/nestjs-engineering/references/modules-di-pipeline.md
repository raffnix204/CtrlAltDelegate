# NestJS Modules, DI & Request Pipeline
## When to read this reference

Read this reference when **modules di pipeline** is material to the current nestjs engineering decision, failure path, compatibility question or verification plan. Do not preload it for unrelated jobs.

Before adding an import/export or `forwardRef`, draw the dependency direction between capabilities. Shared low-level infrastructure may be extracted; mutually dependent domain modules usually indicate ownership has not been separated.

Provider scopes are contagious through dependencies. Keep request scope for data that truly requires request lifetime; pass explicit context where that is simpler and cheaper.

Pipeline responsibilities:
- Pipe: parse/validate/transform input.
- Guard: decide whether request may proceed.
- Interceptor: wrap request/response for cross-cutting behavior.
- Filter: translate uncaught exceptions.

Keep domain decisions out of generic interceptors/filters where they become invisible.

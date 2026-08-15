# NestJS Transactions, Testing & Runtime
## When to read this reference

Read this reference when **transactions testing runtime** is material to the current nestjs engineering decision, failure path, compatibility question or verification plan. Do not preload it for unrelated jobs.

A service/use-case that must update several records should control one transaction context. Repositories participate; they should not commit independently unless explicitly designed as separate consistency boundaries.

Use isolated tests for domain logic, module tests for provider wiring, and HTTP/transport tests for decorators/pipes/guards/filters. Startup tests catch provider graph errors that unit mocks cannot.

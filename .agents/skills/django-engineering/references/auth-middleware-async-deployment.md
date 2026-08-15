# Django Auth, Middleware, Async & Deployment
## When to read this reference

Read this reference when **auth middleware async deployment** is material to the current django engineering decision, failure path, compatibility question or verification plan. Do not preload it for unrelated jobs.

Map session/auth/CSRF/security middleware and any custom middleware in order. A move can change whether request user/session exists, whether responses receive headers, and which exceptions are transformed.

Object authorization belongs close to the protected operation, not only in navigation/template visibility.

Under ASGI, determine which DB/client/library calls are truly async-safe. A syntactically `async` view can still block the event loop. Verify deployment with the actual ASGI/WSGI server and worker configuration.

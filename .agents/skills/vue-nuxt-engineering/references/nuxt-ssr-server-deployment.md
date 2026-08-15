# Nuxt SSR, Server & Deployment
## When to read this reference

Read this reference when **nuxt ssr server deployment** is material to the current vue nuxt engineering decision, failure path, compatibility question or verification plan. Do not preload it for unrelated jobs.

Server routes are public server boundaries. Enforce identity, resource authorization and validation there even if route middleware/client UI already restricts navigation.

Plugins can run server, client or both depending on configuration. Avoid browser/server-only imports in the wrong environment and side effects at module load.

Verify Nitro/deployment preset behavior in production for environment variables, server APIs, connections and asset/public URL behavior.

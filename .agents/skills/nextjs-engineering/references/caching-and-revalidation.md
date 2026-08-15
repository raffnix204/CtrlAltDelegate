# Next.js Caching & Revalidation

Caching is version-sensitive. First inspect the project version/config and current first-party docs.

For each cached value define:

- cacheable function/component/read boundary;
- key/identity inputs;
- whether auth/cookies/headers/request data influence the result;
- freshness lifetime;
- invalidation owner after mutations;
- behavior on failure/retry.

When the active Next.js version supports Cache Components / `use cache`, follow that version's rules for cache keys, lifetimes and tag invalidation. Do not mechanically translate older `unstable_cache` examples without checking closure/request-data semantics.

Verification should show that two equivalent reads reuse the intended value and that a relevant mutation invalidates exactly the affected cache domain without exposing one user's data to another.

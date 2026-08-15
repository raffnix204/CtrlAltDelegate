# React State, Effects & Concurrency

## State classification

Before adding a store, classify the state:

- **local interaction**: open/closed, selected tab, draft input → keep local unless multiple owners truly need it;
- **URL/navigation**: filters, pagination, shareable view → prefer router/search params when the URL is part of the product contract;
- **server state**: remotely authoritative entities → use the project server-state/RSC mechanism rather than copying responses into generic client state;
- **durable client state**: offline drafts/preferences → explicit persistence ownership and migration/versioning;
- **external source**: browser/native subscription → subscribe with a lifecycle-safe adapter; `useSyncExternalStore`-style semantics may be required for concurrent safety.

## Effects

An effect is justified when React must synchronize with something it does not own: DOM imperative API, subscription, timer, network lifecycle not handled by the framework/data layer, analytics or other external system. If the value can be computed from current props/state, compute it during render.

For async effects, prove what happens when dependencies change before completion. Abort when supported or discard stale results using an ownership/version token. Cleanup subscriptions/timers unconditionally.

## Optimistic state

An optimistic UI needs:

1. a stable mutation identity;
2. a temporary presentation state;
3. server reconciliation;
4. conflict/failure rollback or replacement;
5. protection against response reordering.

Do not let optimistic state become a second unsynchronized database.

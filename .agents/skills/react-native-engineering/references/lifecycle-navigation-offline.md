# React Native Lifecycle, Navigation & Offline
## When to read this reference

Read this reference when **lifecycle navigation offline** is material to the current react native engineering decision, failure path, compatibility question or verification plan. Do not preload it for unrelated jobs.

Model bootstrap explicitly: restore auth/session, hydrate durable local state, initialize navigation/linking, then reconcile queued work. External links/notification payloads can arrive before these are ready; queue/validate them rather than navigating blindly.

Offline mutations need a stable client operation identity, retry policy and conflict rule. A network timeout does not prove the server did not commit. Replaying a non-idempotent operation can duplicate charges/messages/orders.

Background/process termination can occur between any two steps. Persist only the minimum resumable user state; never rely on component memory for a workflow that must survive process death.

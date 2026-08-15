# GraphQL Operations & Subscriptions
## When to read this reference

Read this reference when **operations subscriptions** is material to the current graphql engineering decision, failure path, compatibility question or verification plan. Do not preload it for unrelated jobs.

Name production operations and keep fragments close to the capability/view that owns them. Avoid giant shared fragments that make every consumer fetch the superset.

Cursor pagination needs stable ordering and server-side max page sizes.

Subscriptions inherit realtime concerns: authorization at subscribe and event delivery, token expiry/revocation, reconnect/resume behavior, duplicate/missed events, fan-out and slow consumers. Use `realtime-communications-engineering` for transport/backpressure detail.

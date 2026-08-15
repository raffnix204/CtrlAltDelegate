# IaC — Deep Reference
## When to read this reference

Read this reference when **field guide** is material to the current infrastructure as code engineering decision, failure path, compatibility question or verification plan. Do not preload it for unrelated jobs.

## State-change gate
For every resource change classify: NOOP / IN_PLACE / REPLACE / DESTROY / IMPORT / MOVE / EXTERNAL_SIDE_EFFECT.

Replacement/destruction of stateful/network/security resources is HIGH risk. Verify provider semantics in current official docs and preserve recoverability.

## Apply discipline
review immutable plan against intended commit → verify credentials/account/environment → apply bounded scope → retain output → verify cloud/runtime state independently → update state/ADR if observed behavior differs.

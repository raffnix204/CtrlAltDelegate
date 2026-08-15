# OPNsense Engineering — Deep Reference
## When to read this reference

Read this reference when **field guide** is material to the current opnsense engineering decision, failure path, compatibility question or verification plan. Do not preload it for unrelated jobs.

## Current research baseline (2026-08-12)
OPNsense's official API uses module/controller/command paths with JSON requests/responses and API key/secret authentication bound to user privileges. Many GUI components are API-backed, but automation/model components may manage only objects created in those components.

## Safe write pattern
capture config/backup → identify exact API model + privileges → inspect current objects/rule ordering → prepare minimal change → preserve remote management → write/apply → verify service/rules/routes/traffic → retain rollback evidence.

## Revalidation triggers
Edition/release upgrades, firewall automation model changes, DHCP/DNS backend changes, new plugins, or any endpoint inferred by observing the GUI instead of a stable documented API.

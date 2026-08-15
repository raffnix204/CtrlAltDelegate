# UniFi Engineering — Deep Reference
## When to read this reference

Read this reference when **field guide** is material to the current unifi network engineering decision, failure path, compatibility question or verification plan. Do not preload it for unrelated jobs.

## Current research baseline (2026-08-12)
UniFi exposes an official Site Manager API for multi-site/high-level management and local application APIs for detailed application/site behavior. The local Network application exposes version-specific API documentation from its Integrations surface.

## Safe automation sequence
DISCOVER console/site/application/device versions → READ current topology/config → PLAN diff → establish rollback/out-of-band management path → CANARY → APPLY → wait for adoption/provisioning → VERIFY controller + device convergence + real traffic.

## Never assume
- an endpoint seen in an old unofficial controller client is still supported;
- controller API success means a switch/AP/gateway applied the configuration;
- a VLAN or firewall change preserves the management path;
- a Site Manager capability implies an identical local endpoint.

Re-check official developer/local integration documentation for every consequential write path.

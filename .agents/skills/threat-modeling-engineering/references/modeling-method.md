# Threat Modeling Method

Build a compact data-flow model from concrete components/processes/stores/external entities. Mark trust boundaries and state-changing entry points. For each flow record identity, sensitive data, protocol and who validates it.

Threat discovery prompts:
- spoof identity/session/service;
- tamper with request/state/event;
- repudiate privileged action when audit is required;
- disclose data/secrets across tenant/client/log boundaries;
- exhaust scarce resources or block recovery;
- elevate privilege or cross ownership/tenant boundary.

Then add domain-specific business abuse that taxonomy misses, such as coupon abuse, inventory reservation griefing, account recovery takeover or workflow replay.

# V5.8.1 Root-Native Project Delivery Template

This `delivery-template/` models a root-native GitHub-native project baseline. The public GitHub-native distribution itself is tracked in its repository and can run the full lifecycle directly.

Custom-GPT planning handoffs use a different deterministic transport: `ctrlaltdelegate-delivery.zip`, copied into the target project root and safely extracted by the coding agent to local-private `./.ctrlaltdelegate/`. See `docs/system/DETERMINISTIC-PLANNING-DELIVERY-AND-HANDOFF.md`.

Do not confuse the tracked root-native framework distribution with the hidden local control package used for Custom-GPT handoff.

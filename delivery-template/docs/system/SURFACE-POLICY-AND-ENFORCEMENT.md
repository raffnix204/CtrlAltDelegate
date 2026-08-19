# Surface Policy and Enforcement — V5.7.1

Instructions and enforcement are different planes. `AGENTS.md`, skills and plans guide behavior; they are not a security boundary by themselves.

`config/SURFACE-POLICY.yaml` classifies important project/control surfaces as:
- `LOCKED`: agent changes are forbidden during the current operation unless an explicit higher-authority workflow changes the policy;
- `EDITABLE`: changes are allowed within job scope;
- `APPEND_ONLY`: prior records are immutable; new records may be appended;
- `HUMAN_CONTROLLED`: action requires explicit external/human authority.

Use native harness permissions, sandboxing, tool filters, Git protections and CI checks to enforce the policy when available. If enforcement is unavailable or only partial, record that fact in harness state and apply the strictest safe fallback. Never represent soft instructions as hard enforcement.

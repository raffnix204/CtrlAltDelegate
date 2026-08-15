# WordPress Plugin Security & Lifecycle

For privileged actions require the appropriate capability/resource ownership and then verify nonce/intent for browser state-changing actions as applicable. A nonce is not a permission model.

Sanitize/validate input when accepted, but escape at output using the correct context. Stored content can change source/trust over time, so input sanitization does not replace output encoding.

Activation creates required defaults/schema with bounded work. Upgrades are versioned and retry-safe. Deactivation disables behavior without deleting user data. Uninstall removes data only when product/user policy explicitly says so.

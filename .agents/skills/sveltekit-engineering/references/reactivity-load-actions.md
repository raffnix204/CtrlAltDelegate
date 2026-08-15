# SvelteKit Reactivity, Load & Actions

Use project-version syntax consistently. During migrations, isolate legacy/new component patterns and use the official migration tooling/guidance rather than creating hybrid conventions ad hoc.

Server load/actions run in a request context. Avoid mutable module state for user-specific data. Keep authorization and input validation in actions/endpoints even when forms are only rendered for authorized users.

Progressive enhancement should preserve meaningful form semantics, errors and focus behavior; client enhancement is an optimization, not the only functional path when the product requires resilience/accessibility.

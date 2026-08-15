# Security Sharp Edges & Insecure Defaults

Look for APIs/configurations where the easiest usage is unsafe:
- missing auth/permission callback defaults to allow;
- optional validation silently disables checks;
- empty secret/key accepted and switches to unsigned mode;
- wildcard CORS/redirect/origin configured by convenience;
- production falls back to debug/dev credentials or permissive mode;
- dangerous action exposed behind a confusing boolean/string option.

Prefer secure-by-default interfaces that require explicit, visible opt-in to weaken protection. Fail closed when required security configuration is absent, unless product availability requirements explicitly justify a different model.

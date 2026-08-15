# Terraform State, Refactor & Import
## When to read this reference

Read this reference when **state refactor import** is material to the current terraform engineering decision, failure path, compatibility question or verification plan. Do not preload it for unrelated jobs.

Before refactoring list every affected Terraform address and corresponding real resource ID. The desired result is usually an address mapping with zero infrastructure replacement. Encode moves using supported configuration/state mechanisms and verify the plan.

For bulk/import workflows, discovery is not ownership. Generated configuration must be reviewed for provider defaults, sensitive values, computed fields and resources that should remain externally managed.

If state and real infrastructure disagree, determine which is authoritative before changing either.

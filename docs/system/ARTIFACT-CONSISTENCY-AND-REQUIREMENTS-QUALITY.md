# Requirements Quality and Artifact Consistency — V5.7.1

Before consequential implementation, test the planning artifacts themselves.

## Requirements Quality Gate

Requirements must be sufficiently unambiguous, observable and complete for their risk. Check roles, failure states, recovery, security/privacy, destructive operations, data lifecycle, acceptance evidence and externally visible behavior. This is requirements QA, not implementation QA.

## Artifact Consistency Gate

Read-only analysis compares:
`Requirements ↔ Architecture ↔ Program Design ↔ Job Graph ↔ Skills ↔ Verification`.

Report contradictions, uncovered requirements, jobs without requirement/maintenance justification, invalid architecture assumptions, missing verification and inconsistent interfaces. Findings route back to the owning artifact; the analyzer does not rewrite every document to make the inconsistency disappear.

Convergence repairs are append/scoped changes. Do not silently mutate historical evidence or completed job claims merely to make the plan appear complete.

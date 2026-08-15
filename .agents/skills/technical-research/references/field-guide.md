# Technical Research — Progressive Reference

## Evidence ladder
1. live repository/runtime evidence;
2. current official specification/documentation;
3. official source repository/releases/changelog;
4. vendor support/compatibility documentation;
5. strong independent technical evidence;
6. community discussion only as a lead.

## Research modes
- NONE: exported plan/repo already proves the decision.
- VERIFY_DRIFT: re-check one unstable fact such as current API/version/support.
- TARGETED: compare a small candidate set for one concrete decision.
- SPIKE: run a minimal implementation/contract/profiling experiment because documentation alone cannot prove fit.

## Stop condition
Research stops when the implementation decision is safe and evidence-backed. Do not collect sources after the decision gap is closed.

## Autonomous decision output
FACTS → REPO EVIDENCE → INFERENCE → DECISION → IMPACTED ADR/STACK/SKILLS/JOBS → VERIFICATION.

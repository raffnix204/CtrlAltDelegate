# Existing Projects, Audits & Remediation — V5.8.2

## Modes
`EXISTING_CONTINUE`, `AUDIT_ONLY`, `AUDIT_REMEDIATE`, `BUGFIX`, `SECURITY_HARDEN`, `FRONTEND_UPGRADE`, `SEO_OPTIMIZE` (combinable).

## Mandatory entry
`GIT SAFETY → REPOSITORY_INTAKE → REPOSITORY-BASELINE → SYSTEM-MAP → HEALTH-BASELINE → REPO_READY → requested mode`

Use `repository-onboarding`.

## Git safety
Inspect HEAD/branch/status/remotes/worktrees. Uncommitted user work is protected; never reset/clean/overwrite it. Prefer isolated worktree/branch where appropriate.

## Repository context
Create `planning/repository/REPOSITORY-BASELINE.md`, `SYSTEM-MAP.md`, `HEALTH-BASELINE.md`.
Maps are SHA-bound. When repo advances, diff from stored SHA and refresh only affected capabilities unless architecture materially changed.

## Health baseline
Discover project-native build/type/lint/test/security/dependency/runtime commands. Record passing/failing/flaky/external checks before modifications. New work must not introduce required failures.

## Full audit
1. onboarding/baseline;
2. rank risk surfaces;
3. bounded read-only reviewers;
4. configured/researched tools;
5. validate/dedupe findings;
6. canonical `FINDINGS.md`;
7. remediation DAG;
8. isolated fixes;
9. independent re-review/re-scan;
10. full verification.

Relevant risk surfaces include auth, sensitive data/payment, persistence/migrations, public APIs/webhooks, file/input boundaries, concurrency, dependencies, CI/deployment/secrets, critical frontend flows and public SEO/performance.

## Findings
Lifecycle:
`DISCOVERED → VALIDATED → PLANNED → FIXED → VERIFIED → CLOSED`

Also: `FALSE_POSITIVE`, `DEFERRED`, `RISK_ACCEPTED`, `BLOCKED_EXTERNAL`.

Finding requires severity, confidence, location, concrete scenario/evidence, impact, remediation and verification. Scanner output is a lead, not proof.

## Prioritization
1. confirmed critical security/data-loss/corruption;
2. confirmed high correctness/security;
3. blockers of requested work/build/runtime;
4. meaningful medium;
5. low-risk debt.

Unrelated medium/low debt does not automatically block a requested feature.

## Bugfix
`REPRODUCE → MINIMIZE → HYPOTHESIS → DISCRIMINATING EVIDENCE → ROOT CAUSE → RED → FIX → GREEN → REGRESSION → CODE REVIEW → VERIFY`

## Security
Use `security-review` + `code-review`; add auth/API/database/runtime specialists. Existing CodeQL/code-scanning/dependency-review may be used where already available/supported. Validate alerts.

## Feature continuation
Map affected capability, contracts, nearby tests/patterns and seams; define delta; preserve unrelated behavior; run normal autonomous jobs/reviews.

## Frontend upgrade
`repository-onboarding → ux-product-design → ui-design-system → components/responsive/a11y → motion when material → browser evidence → visual-polish/performance → code-review/verification`

Use real-content before/after screenshots. Do not replace working backend because UI is dated.

## SEO optimization
Map public routes/rendering/content/meta/canonical/robots/sitemap/structured data/redirects/performance, then apply `seo-content` and retest representative URLs.

## Token efficiency
Commit-bound maps, capability slices, symbols/callers/diffs, bounded subagents, raw evidence on disk and compact returns. Unchanged maps are reused.

## Completion
AUDIT_ONLY ends at `AUDIT_COMPLETE` with validated findings.
AUDIT_REMEDIATE ends when targeted findings are verified closed/deferred/accepted and final regression/runtime gates pass.
Feature/bugfix uses normal COMPLETED rules plus baseline comparison and independent review.

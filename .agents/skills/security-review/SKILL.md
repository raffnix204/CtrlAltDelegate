---
name: security-review
description: "Use when the task materially involves this skill's owned domain: Perform risk-based secure-design and implementation review using current OWASP guidance, with testable findings around trust boundaries rather than generic checklists."
---

# Application Security Review

Skill ID: `security-review`
Library: `software-planning-lead-v5.6.1`
Version: `5.6.1`

## Purpose

Perform risk-based secure-design and implementation review using current OWASP guidance, with testable findings around trust boundaries rather than generic checklists.

## Profiles

web_app, internal_app, api_backend, ecommerce, ai_data_app, native_apple

## Typical roles

security-reviewer, security-architect

## Baseline
Use current OWASP ASVS/Cheat Sheet guidance as a reference for web application security. Select rigor based on project threat/data/business risk. For AI-enabled systems, additionally consider current AI/LLM-specific OWASP standards when applicable.

## Threat model first
Identify:
- assets/sensitive data;
- actors/roles;
- trust boundaries;
- external integrations;
- privileged operations;
- attacker-controlled input channels;
- tenancy boundaries;
- destructive/financial actions.

Review the paths where untrusted input crosses into privileged capability or protected data.

## Review domains
### Authentication/session
- identity lifecycle, enrollment/recovery;
- session/token storage, rotation, expiry, revocation;
- MFA/re-auth for high-risk operations when required;
- OAuth/OIDC state/PKCE/callback validation where applicable;
- no credentials/tokens exposed to logs/client storage without justified model.

### Authorization
Authorization is server/data-boundary policy, not UI visibility. Test horizontal/vertical privilege escalation, tenant/resource ownership, object IDs and admin paths. Deny by default where appropriate.

### Input/injection
Validate syntax/shape at boundaries and enforce domain invariants deeper. Parameterize queries. Avoid shell/template/LDAP/path injection through contextual APIs/encoding. Treat uploads as hostile: size, content/type, storage location, serving policy, malware scanning based on risk.

### Output/web security
Use contextual encoding and framework-safe rendering. Sanitize intentionally allowed user HTML with a maintained allowlist sanitizer. Apply CSP/security headers appropriate to architecture without cargo-cult directives that break legitimate functionality.

### CSRF/CORS
Model browser credential behavior. Cookie-authenticated state-changing actions require appropriate CSRF defenses. CORS is an origin access policy, not authentication; configure exact trusted origins/methods/credentials as needed.

### Secrets
Secrets never live in repository/images/logs. Use managed env/secret stores; least privilege, rotation and revocation. Build secrets use secret mounts or platform mechanisms rather than ARG/layers.

### Abuse/rate limits
Protect high-cost, brute-force, enumeration, invite/reset, payment and AI operations with suitable identity/IP/device/risk controls. Avoid one arbitrary global rate limit.

### Dependencies/supply chain
Use lockfiles/reproducible installs, vulnerability/advisory scanning, minimal packages, provenance/signing where ecosystem supports it, safe CI permissions and reviewed dependency updates.

### Logging/privacy
Record security-relevant events without credentials/content that should not persist. Define retention/access. Avoid PII in URLs or verbose traces.

## Security tests
For high-risk paths include negative tests:
- unauthenticated;
- wrong role/tenant/owner;
- malformed/oversized input;
- replay/duplicate side effect;
- expired/revoked session;
- webhook bad signature/replay;
- file type/content mismatch where relevant.

## Finding format
Severity, asset/threat, exact evidence, exploit preconditions, affected path, recommended fix, verification test, residual risk.

## Anti-patterns
- "we use an ORM so injection is impossible";
- auth check only in frontend/middleware while direct service path bypasses it;
- storing bearer tokens in broadly script-readable storage without threat justification;
- disabling CSP/CSRF/CORS because tests fail;
- logging full request bodies globally;
- hardcoded secrets/example secrets that are live;
- security scanner PASS treated as complete review;
- dependency update applied blindly as vulnerability fix without regression/compatibility testing.

## Acceptance
No unresolved critical/high issue in mandatory scope unless risk explicitly accepted by authorized owner. Fresh tests/scans support claims; sensitive paths trace to authz/validation tests.


## Existing-project security audit

1. run `repository-onboarding`;
2. identify trust boundaries/sensitive capabilities;
3. inspect existing security tooling before adding tools;
4. use configured code/dependency/secret scanners as evidence sources;
5. validate important alerts in source before canonical findings;
6. create bounded remediation jobs;
7. rerun scans + negative tests after fixes.

Existing GitHub CodeQL/code scanning and dependency review may provide useful signals where available/supported. They are optional execution capabilities, not requirements.

Never expose secret values while scanning history/config and never weaken/dismiss security rules merely to obtain a clean dashboard.

## V5.6.1 Stack and Supply-Chain Routing

Security review begins from actual trust boundaries and stack. Route language/platform specialists for unsafe/FFI/mobile/Kubernetes/runtime-specific issues and inspect existing dependency/secret/code-scanning controls before adding scanners. Dependency alerts are leads, not proof; validate reachability/exposure and fix at the narrowest safe layer. New third-party agent/MCP/tool capabilities are executable supply-chain boundaries and require provenance, permission and secret-scope review.

## Progressive References

- `references/differential-and-blast-radius.md` — read for security review of a PR/commit/refactor where changed callers, removed safeguards or history matter.
- `references/sharp-edges-and-insecure-defaults.md` — read when reviewing API/config ergonomics or fail-open/default behavior.
- `references/variant-analysis.md` — read after finding a real vulnerability class and searching for siblings across the codebase.

For architecture-level threat discovery before code review, route `threat-modeling-engineering`; do not duplicate a full threat model inside every diff review.

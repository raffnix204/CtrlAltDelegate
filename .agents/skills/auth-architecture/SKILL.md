---
name: auth-architecture
description: Design identity, session, recovery and authorization boundaries using established protocols/provider capabilities without building unnecessary custom authentication.
---

# Authentication & Authorization Architecture

Skill ID: `auth-architecture`
Library: `software-planning-lead-v5.6.1`
Version: `5.6.1`

## Purpose

Design identity, session, recovery and authorization boundaries using established protocols/provider capabilities without building unnecessary custom authentication.

## Profiles

web_app, internal_app, api_backend, ecommerce, native_apple

## Typical roles

security-architect, backend-implementer

## First decision: build vs provider
Prefer mature identity/provider/library solutions unless product requirements genuinely need custom credential handling. Research current provider capabilities, pricing, platform support, data residency and lock-in before selection.

## Identity lifecycle
Define:
- signup/invite/provisioning;
- email/phone/SSO verification where required;
- account linking;
- profile/credential change;
- recovery;
- suspension/deletion;
- organization/tenant membership lifecycle.

Avoid ambiguous duplicate identities from multiple login methods.

## Session model
Specify browser/native/server session/token storage, expiry, renewal/rotation, revocation and logout semantics. Protect bearer credentials against primary threat model. Cookies require secure attributes and CSRF consideration; native apps use platform secure storage where appropriate.

## OAuth/OIDC
Use standards-compliant libraries. Validate redirect URIs, state/nonce/PKCE as flow requires, issuer/audience/signatures/claims, and do not use ID token as arbitrary API authorization without design. Keep provider token scopes least-privileged.

## Authorization model
Start from resources/actions/ownership, not UI roles alone. Define:
- subject (user/service);
- tenant/org;
- resource owner;
- role/permission/policy;
- server/data enforcement points.

RBAC is sufficient for many products; add attribute/policy complexity only when requirements justify it. Prevent cross-tenant IDOR/horizontal escalation with resource-scoped checks.

## Privileged actions
Admin/financial/security changes may require re-auth/MFA, audit events or dual approval depending on risk. Separate normal user session from service-to-service credentials.

## Recovery/security UX
Recovery paths are authentication paths. Protect against enumeration and takeover while keeping messages usable. Rate-limit/monitor abuse. Avoid knowledge-based questions. Define session invalidation after credential compromise/change according to risk.

## Frontend behavior
Frontend permission hints improve UX but never replace server authorization. Handle expired sessions and forbidden operations without loops/data loss.

## Tests
- unauthenticated access;
- wrong role;
- correct role wrong tenant/resource;
- expired/revoked session;
- recovery/linking edge cases;
- OAuth callback tampering where applicable;
- privilege changes reflected in active sessions according to policy.

## Anti-patterns
- custom password/JWT crypto because it seems simple;
- role check only in route navigation;
- admin boolean scattered throughout code;
- trusting client-provided tenant/user ID;
- long-lived unrevocable bearer tokens without need;
- exposing whether an account exists unnecessarily;
- broad OAuth scopes;
- auth provider choice based only on quickest demo.

## Evidence
`SECURITY-AND-RELIABILITY.md`/ADR records provider/protocol, session lifecycle, authorization matrix/enforcement, recovery, privileged actions, tests and known provider constraints.

## V5.6.1 Identity and Authorization Depth

Separate authentication, session/token lifecycle, authorization policy and tenant/data isolation. Decide where identity is established, how credentials/session artifacts rotate/expire/revoke, and where authorization is enforced for every protected operation.

Prefer centralized policy primitives with local, explicit enforcement at resource/action boundaries. Model organization/tenant membership, ownership, roles/permissions and service-to-service identities independently where the product needs them. Do not infer authorization from hidden UI controls or possession of an object ID.

For OAuth/OIDC/passkeys/social providers, research current provider/platform requirements. Validate redirect/origin/state/nonce/PKCE/session behavior as applicable. Sensitive account recovery, impersonation, admin elevation and destructive operations deserve step-up or additional audit controls when risk justifies it.

Verification includes negative cross-tenant/object access tests, session expiry/revocation, privilege changes during active sessions, CSRF/replay where relevant, and auditability of privileged actions.

## Progressive References

- `references/session-oauth-and-step-up.md` — session/token lifecycle, OAuth/OIDC/PKCE and re-auth/MFA decisions.
- `references/authorization-tenancy.md` — resource/action authorization, organizations/tenants, service identities and negative tests.

Provider-specific quickstarts (Auth0, Firebase, Cognito, Clerk, Supabase, etc.) are implementation references, not architecture authority. Preserve this skill's provider-neutral identity/session/policy model and verify current provider SDK guidance only after provider selection.

# Auth Sessions, OAuth & Step-Up
## When to read this reference

Read this reference when **session oauth and step up** is material to the current auth architecture decision, failure path, compatibility question or verification plan. Do not preload it for unrelated jobs.

Define credential/session artifact storage, lifetime, rotation, revocation and what changes invalidate existing sessions. Browser cookie sessions and native bearer tokens have different CSRF/XSS/storage threats; choose protection from the actual client model.

For OAuth/OIDC use maintained libraries and validate current flow requirements: redirect URI, state, nonce, PKCE, issuer, audience, signature and claim semantics as applicable. ID tokens establish identity for the client; API authorization should follow the intended access-token/resource-server design.

Step-up/re-auth/MFA belongs on operations whose risk justifies stronger recent authentication, such as credential changes, recovery, financial payout or privileged admin action.

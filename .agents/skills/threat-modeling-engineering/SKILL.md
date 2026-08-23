---
name: threat-modeling-engineering
description: "Use when the task materially involves this skill's owned domain: Build an evidence-based threat model from assets, actors, trust boundaries, entry points, abuse cases and security invariants, then convert material threats into design requirements and verification."
---

# Threat Modeling Engineering

## Purpose / Ownership

Build an evidence-based threat model from assets, actors, trust boundaries, entry points, abuse cases and security invariants, then convert material threats into design requirements and verification.

Own the domain-specific judgment only. Shared autonomy, escalation, research, minimization, evidence and routing rules come from `docs/system/SKILL-EXECUTION-CONTRACT.md`.

## Activation & Negative Triggers

- New/high-risk architecture, auth/payment/tenant/admin/data flow.
- Security-sensitive external integration or trust-boundary change.
- Repeated vulnerability class suggesting missing security invariant.
- Do not activate for adjacent work that does not materially touch this responsibility.

## Context To Inspect

- Architecture/data-flow diagrams or code paths that actually exist.
- Assets/sensitive data and actors/roles/service identities.
- Network/process/client/server/storage trust boundaries.
- Authentication/authorization and privileged/destructive actions.
- Existing controls, assumptions and incident history.

## Expert Decision Model

1. Map the real system first: entry points, state-changing operations, data stores, external calls and trust transitions. Threat modeling without implementation context becomes a generic checklist.
2. Identify assets and security properties to preserve—confidentiality, integrity, availability, authenticity, authorization, non-repudiation or business invariants as appropriate.
3. Enumerate attacker-controlled inputs and actors including unauthenticated, ordinary user, tenant admin, compromised client, malicious integration and stolen service credential where relevant.
4. For each trust boundary, ask what identity/data is assumed when crossing it and whether the receiving side independently validates that assumption.
5. Write abuse cases as concrete attacker goals and paths, then derive prevent/detect/recover controls. Use STRIDE or another taxonomy as a completeness aid, not as the output itself.
6. Separate design assumptions from enforced invariants. An assumption with no control/evidence is a risk, not a mitigation.
7. Prioritize by plausible impact/exploitability and exposure; do not inflate severity merely because a category sounds dangerous.
8. Convert accepted mitigations into requirements/tests/telemetry/operational response, and record explicitly accepted residual risk where authority permits.

## Critical Invariants

- Every protected asset/privileged operation has a known trust/authorization boundary.
- Material assumptions are either enforced/tested or explicitly recorded as residual risk.
- Threats produce concrete prevent/detect/recover controls rather than checklist prose.
- Model stays scoped to actual architecture and intended adversaries.

## Failure Modes / Sharp Edges

- Threat list generated from OWASP/STRIDE with no system data flow.
- Trusting internal network/client-generated user ID as identity.
- Frontend control described as mitigation for server authorization threat.
- Only prevention controls; no detection/recovery for realistic compromise.
- Risk scoring used as false precision with no evidence.
- Threat model updated in docs but requirements/tests never change.

## Version / Drift Triggers

- Current platform/provider threat boundaries and security capabilities.
- Current standards/regulatory requirements only when project scope requires them.

## Domain-Specific Verification

- Trace a sample of highest-risk threats to concrete code/config/test/alert/recovery evidence.
- Use adversarial negative tests for alternate tenant/role/input/replay paths.
- Re-run threat delta after architecture/trust-boundary changes rather than rewriting the whole model.
- For high-risk completion, pair with `security-review` and `adversarial-verification`.

## Progressive References

- `modeling-method.md` — data-flow/trust-boundary modeling and threat prioritization
- `abuse-cases-and-controls.md` — abuse cases, security invariants and prevent/detect/recover mapping

Read only the reference whose topic is material to the current job.

## Companion Skills

- `security-review`
- `adversarial-verification`
- `privacy-data-governance-engineering`
- `auth-architecture`

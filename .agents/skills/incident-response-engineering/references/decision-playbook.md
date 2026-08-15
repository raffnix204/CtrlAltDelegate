# Incident Response & Runbook Engineering — Decision Playbook

## Use this reference when

Read this file only when a material decision, production failure path, rollout/recovery question or verification ambiguity needs deeper probes. Start from independent failure domains, protected data/config/key dependencies, RPO/RTO, restore authority and the last independently proven recovery exercise.

Current first-party documentation and live repository/runtime evidence remain authoritative for version-sensitive behavior. External skill libraries are research prompts, not executable policy.

## 1. Define incident classes and severity from user/data/business impact, not emotion

- **Watch for:** restores that fail, copies in the same failure domain, missing key/identity/network dependencies, unmeasured recovery objectives or untested failback.
- **Prove with:** isolated restore/revert exercises, integrity checks, measured RPO/RTO where required and proof that keys/identity/network dependencies are available during recovery.
- **Safe change pattern:** separate failure domains, preserve immutable/offline recovery options where risk warrants and rehearse restore plus return-to-normal before relying on the plan.

## 2. Write runbooks around observable symptoms, decision trees, exact safe checks, bounded mitigation actions and verification rather than generic troubleshooting prose.

- **Watch for:** restores that fail, copies in the same failure domain, missing key/identity/network dependencies, unmeasured recovery objectives or untested failback.
- **Prove with:** isolated restore/revert exercises, integrity checks, measured RPO/RTO where required and proof that keys/identity/network dependencies are available during recovery.
- **Safe change pattern:** separate failure domains, preserve immutable/offline recovery options where risk warrants and rehearse restore plus return-to-normal before relying on the plan.

## 3. Preserve evidence while restoring service: timeline, logs, metrics, traces, deploys, configuration changes and hypotheses must remain distinguishable.

- **Watch for:** restores that fail, copies in the same failure domain, missing key/identity/network dependencies, unmeasured recovery objectives or untested failback.
- **Prove with:** isolated restore/revert exercises, integrity checks, measured RPO/RTO where required and proof that keys/identity/network dependencies are available during recovery.
- **Safe change pattern:** separate failure domains, preserve immutable/offline recovery options where risk warrants and rehearse restore plus return-to-normal before relying on the plan.

## 4. Prefer reversible containment and traffic isolation over speculative invasive fixes

- **Watch for:** restores that fail, copies in the same failure domain, missing key/identity/network dependencies, unmeasured recovery objectives or untested failback.
- **Prove with:** isolated restore/revert exercises, integrity checks, measured RPO/RTO where required and proof that keys/identity/network dependencies are available during recovery.
- **Safe change pattern:** separate failure domains, preserve immutable/offline recovery options where risk warrants and rehearse restore plus return-to-normal before relying on the plan.

## 5. Separate mitigation from root-cause correction

- **Watch for:** restores that fail, copies in the same failure domain, missing key/identity/network dependencies, unmeasured recovery objectives or untested failback.
- **Prove with:** isolated restore/revert exercises, integrity checks, measured RPO/RTO where required and proof that keys/identity/network dependencies are available during recovery.
- **Safe change pattern:** separate failure domains, preserve immutable/offline recovery options where risk warrants and rehearse restore plus return-to-normal before relying on the plan.

## 6. Post-incident actions need owners, evidence and closure criteria

- **Watch for:** restores that fail, copies in the same failure domain, missing key/identity/network dependencies, unmeasured recovery objectives or untested failback.
- **Prove with:** isolated restore/revert exercises, integrity checks, measured RPO/RTO where required and proof that keys/identity/network dependencies are available during recovery.
- **Safe change pattern:** separate failure domains, preserve immutable/offline recovery options where risk warrants and rehearse restore plus return-to-normal before relying on the plan.

## 7. Exercise high-value runbooks and restore/failover procedures before incidents so commands, permissions and dependencies are known to work.

- **Watch for:** cross-tenant/resource access, policy bypass through alternate paths, stale authorization caches or privileged actions without auditable ownership.
- **Prove with:** positive and negative authorization cases across representative roles/tenants/resources, including alternate entry points and privileged/bypass identities.
- **Safe change pattern:** centralize the authoritative policy boundary, default deny on ambiguity and keep tenant/resource identity attached through derived/cache/index layers.

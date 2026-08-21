# Worker Brief Integrity & Capability Attestation — V5.8.1

## Purpose

Workers receive the smallest sufficient context, but every load-bearing pointer must be bound to the state it references. This prevents stale-plan execution after requirements, job graphs, skill routing or user steering changes.

## Hash-bound worker brief

A substantive delegated job should receive a compact structured brief containing:
- job id and objective;
- requirement ids;
- owned and prohibited scope;
- dependencies;
- required skill ids and exact canonical skill paths;
- required worker/harness capabilities;
- acceptance criteria and required evidence;
- pointers to authoritative mission/project/plan/job artifacts;
- SHA-256 for load-bearing pointers, plus optional run nonce/epoch when useful;
- output/report path.

Before acting, the worker verifies required pointer hashes. A mismatch is `STALE_BRIEF`, not permission to continue from memory. The orchestrator reconciles state and issues a new brief.

Do not paste the full planning tree or conversation into every worker when pointers are sufficient. Independent reviewers receive authoritative requirements, candidate artifacts and raw evidence, not the author's success narrative or sibling verdicts.

## Capability attestation cache

Harness probing can be reused only through a versioned attestation bound to the live execution surface. Recommended bindings include:
- harness/provider identity and version;
- relevant config hash;
- permission/sandbox profile;
- instruction/skill adapter hash where relevant;
- verified capabilities such as READ, WRITE, shell, Git, subagents, browser/web/runtime access, sandbox strength, approvals and resumability;
- verification timestamp/evidence.

Reuse is valid only while every required binding still matches. Version, configuration, permission profile or adapter changes invalidate the corresponding attestation. Missing or ambiguous attestation is a cache miss, never proof of capability.

## Worker lifecycle

Default terminal lifecycle is:

`DISPATCH -> RUNNING -> REPORT_READY -> COLLECT -> PERSIST -> TERMINATE`

After a worker's final report is collected, stop it unless a concrete continuation need exists and the harness provides trustworthy continuable sessions. A parked worker still consumes live capacity and must not be treated as free.

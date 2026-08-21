# Capability-Driven Technology Selection — V5.8

## Objective
Select the smallest complete architecture that satisfies project capabilities and hard constraints. Technology names are candidates, not defaults.

## Pipeline
`PROJECT REQUIREMENTS → CONSTRAINT EXTRACTION → DOMAIN PROFILE → CAPABILITY MATRIX → CANDIDATE GENERATION → CURRENT RESEARCH → COMPATIBILITY CHECK → WEIGHTED EVALUATION → SOLUTION MINIMIZATION → STACK DECISION → STACK MANIFEST → SPECIALIST SKILL ACTIVATION → ARCHITECTURE`.

## Capability bundles before components
Model required outcomes such as `AUTH`, `DATABASE`, `FILE_STORAGE`, `REALTIME`, `SEARCH`, `BACKGROUND_JOBS`, `OBSERVABILITY`, `ADMIN_UI`, `PAYMENTS`, `AI_VECTOR_SEARCH` before choosing products. Compare an integrated platform with the equivalent set of independent components. A bundle that removes services is preferred only when it preserves required security, portability, performance and operations.

Example: `AUTH + POSTGRES + STORAGE + REALTIME` may make Supabase a strong candidate; enterprise SAML/SCIM plus existing object storage may instead favor dedicated IAM + existing storage + PostgreSQL.

## Self-hostable-first, not self-hosted-only
When two options are materially equivalent, prefer self-hostable/open/standards-based/portable components with a credible export/exit path. Managed SaaS remains eligible when it materially improves reliability, compliance, ecosystem, delivery speed or total operating cost. Record the tradeoff rather than applying ideology.

## Candidate discipline
Use `config/TECHNOLOGY-CAPABILITY-CATALOG.yaml` to avoid blind spots, then narrow to 2–5 credible candidates. Do not compare the entire catalog. `CORE`, `SPECIALIST` and `EMERGING` are consideration tiers, not quality scores. Drift-prone facts require current first-party evidence.

## Evaluation
Hard constraints eliminate candidates. Weighted comparison then considers functional/architecture fit, existing infrastructure, self-hostability, security, operations, maturity, maintenance, ecosystem, performance/scaling headroom, portability, lock-in, cost, exit path and team fit.

## API decisions
Separate protocol/contract from implementation: REST/OpenAPI, GraphQL schema, gRPC/Protobuf and AsyncAPI/event contracts are selected from communication semantics. Separately decide reverse proxy, API gateway, API management and service-mesh responsibilities.

## Brownfield
Preserve established architecture by default. New services/platforms need evidence that the capability cannot be satisfied safely and simply with existing infrastructure.

## Required artifacts
Update `planning/architecture/TECHNOLOGY-EVALUATION.yaml` and `STACK-MANIFEST.yaml`. Consequential decisions record capability coverage, candidates, current evidence, selected option, rejected alternatives, operational impact, lock-in/exit path and confidence.

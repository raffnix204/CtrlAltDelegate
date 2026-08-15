# Project Profiles — V5.6.3

Profiles seed routing; the actual stack and change risk refine it. `technology-stack-selection` is mandatory for non-trivial greenfield projects.

## Web / frontend profiles

### Premium marketing / content website
Core: UX, UI system, responsive, accessibility, browser acceptance, frontend performance, content/SEO, verification. Add landing conversion, motion, visual polish and component engineering only when material. Stack selection decides static/MPA/islands/SSR/SPA/hybrid and framework candidates such as Astro or server frameworks from project requirements.

### SaaS / product / internal web app
Core: UX/UI/component/frontend architecture, responsive/accessibility/browser, security, implementation, test/review/verification. Add state audit, API/auth/database/backend/integration/distributed specialists based on actual architecture. Route `typescript-node-engineering` or other matching stack specialists only if used.

### E-commerce
Combine public UX/SEO/content with catalog/cart/checkout/order correctness, integrations/payments, auth/security, data integrity and runtime reliability. Do not treat checkout as a landing-page-only problem.

## Backend / services

### API/backend
Core: `backend-architecture`, `api-contracts`, `implementation-engineering`, matching language specialist, `security-review`, `test-engineering`, `code-review`, `verification-gate`.
Conditional: auth/database/migrations/integrations/distributed/reliability/performance/deployment/container/Kubernetes.

### Distributed/realtime/event-driven
Add `distributed-systems-engineering`, reliability/observability, performance profiling and data/API specialists. Explicitly define delivery/order/idempotency/backpressure semantics.

## Data / AI

### ML system
`machine-learning-engineering` plus primary language specialist (often but not necessarily Python), test/security/performance/reliability and deployment/data specialists. Add `ai-evaluation` only for generative/nondeterministic behavior.

### Agent / LLM product
`agent-application-engineering` + `ai-evaluation`; add MCP, integration, security, context, reliability and stack skills based on architecture.

### MCP server
`mcp-server-engineering` + language specialist + integration/security/test/reliability.

## Mobile / native

### Native Apple
`swift-engineering`, `swiftui-architecture`, `swift-testing`, product UX, accessibility, implementation/review/verification; add API/auth/security/integration as relevant.

### Native Android
`kotlin-engineering`, `android-architecture`, `android-testing`, product UX, accessibility, implementation/review/verification.

### React Native
`react-native-engineering` + `typescript-node-engineering`, product UX/accessibility/test/review; add native/platform/integration skills as required.

### Flutter
`flutter-engineering` + product UX/accessibility/test/review; platform integrations are explicit boundaries.

## Infrastructure / runtime

### Containers
`docker-runtime` + deployment readiness.

### Kubernetes
Add `kubernetes-operations`; do not select Kubernetes simply because the skill exists.

## Existing repository modes

### Feature continuation
`repository-onboarding` + detected stack specialist(s) + affected domain skills + implementation/test/review/verification. Preserve architecture outside requested delta unless justified.

### Audit/remediation
Repository onboarding + context efficiency + risk-routed stack/domain reviewers. Validated findings only create remediation jobs.

### Bugfix
Repository onboarding + systematic debugging + matching stack/domain specialist + regression/TDD when practical + fresh code review/verification.

### Refactor
Repository onboarding + refactoring engineering + stack specialist + implementation/test/review/verification.

### Frontend/SEO/website modernization
Retain V5.6.3 frontend/source-acquisition pipeline and add actual stack/backend specialists discovered in the repository.

## Language specialist routing

When primary code is touched, select the matching specialist when available:
Python, Go, Rust, TypeScript/Node, Java/JVM, Kotlin, .NET/C#, C++, PHP, Ruby or Swift.

Polyglot projects may select multiple stack specialists, but each job loads only those it actually touches.

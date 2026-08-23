---
name: mcp-server-engineering
description: "Use when the task materially involves this skill's owned domain: Design, implement and verify Model Context Protocol servers with safe tools/resources/prompts, schemas, transports, permissions and operability. Use when building or maintaining an MCP server or exposing application capabilities to agents."
---

# MCP Server Engineering

## Purpose

Build MCP capability surfaces that are small, typed, permission-aware and operable. Protocol SDKs evolve, so stable architectural principles live here while exact APIs/transports must be verified against current official MCP/SDK documentation at implementation time.

This skill owns this responsibility narrowly. It complements the general V5.6.1 planning, implementation, testing, review, security, performance and verification system rather than replacing those layers. Prefer project-native conventions and current authoritative documentation over memorized framework details.

## When to Activate

- New MCP server or adapter.
- Adding tools/resources/prompts to an existing MCP server.
- Choosing local/remote transport and auth boundaries.
- Debugging registration, schemas, tool errors, context bloat or unsafe tool behavior.

Do not activate merely because a technology is fashionable. For existing repositories, preserve the established architecture unless the requested change or verified defect justifies a deliberate deviation.

## Required Inputs

- Client/harnesses that must connect and their current MCP support.
- Capabilities to expose and which are read-only vs side-effecting.
- Authentication/authorization and tenant/user identity model.
- Expected payload sizes, rate/cost limits and latency.
- Current official protocol/SDK documentation and target language/runtime.

If an input is unknown and materially changes the design, research or derive it before making an irreversible choice. Record consequential assumptions.

## Decision Framework

- Expose the narrowest stable capability surface; a tool should represent an intentional operation, not raw internal plumbing.
- Prefer resources for read-only addressable context and tools for actions/computation; use prompts only when the client benefits from reusable parameterized instructions.
- Define JSON/schema validation for every tool input/output and return structured actionable errors.
- Make side-effecting tools explicit, idempotent where possible and protected by application authorization rather than trusting model intent.
- Choose transport based on client/deployment requirements and current spec; do not freeze historical SSE/HTTP assumptions.
- Keep business logic transport-independent so stdio/HTTP adapters do not duplicate behavior.
- Treat MCP descriptions/tool schemas as context budget: expose only what the active project/harness needs.

Prefer the simplest design that satisfies correctness, operability, security and expected scale. Reject complexity whose benefit cannot be tied to a concrete requirement or measured risk.

## Workflow

1. **Capability inventory** — List required read/action/prompt surfaces and consumers.
2. **Current spec check** — Verify SDK APIs, transport/auth and protocol features from authoritative docs.
3. **Schema design** — Define names, descriptions, inputs, outputs, errors and idempotency.
4. **Security boundary** — Enforce identity, authorization, secret handling and SSRF/path/network constraints.
5. **Implementation** — Separate core application service from MCP registration/transport.
6. **Client verification** — Exercise discovery and calls from intended harness/client.
7. **Operate** — Add logs/metrics/rate/cost controls without leaking sensitive payloads.

## Expert Heuristics

- Tool names and descriptions should make selection obvious without enormous prose.
- Do not expose filesystem/shell/network primitives when a bounded domain operation suffices.
- Return references/compact summaries for huge data and let clients request detail progressively.
- A read-only tool still needs tenant/data authorization.
- Version capability semantics deliberately; avoid breaking clients by silently changing response shapes.

## Edge Cases and Failure Modes

- Client supports only subset of protocol features.
- Long-running tools need progress/cancellation.
- Remote server serves multiple users/tenants.
- Tool calls retry after timeout with unknown outcome.
- Resource URIs expose path traversal or secret locations.
- Large schemas/tool catalogs consume excessive model context.

## Anti-Patterns

- Copying stale SDK method names without checking current docs.
- One mega-tool with dozens of optional actions.
- Raw exception stack traces returned to models/users.
- Authorization only in prompt/tool description.
- Loading every internal operation as an MCP tool.

## Verification and Evidence

- Intended client discovers only expected capabilities.
- Schemas reject invalid/ambiguous input and errors are structured.
- Auth/tenant/side-effect boundaries have negative tests.
- Retry/cancellation/timeout behavior is safe.
- Context/tool-catalog footprint is audited and unnecessary capabilities are disabled.

A worker report is a claim, not proof. Prefer executable evidence, contract checks, targeted tests, profiling/inspection output, runtime observations and precise diffs.

## Related Skills

- `integration-engineering`
- `agent-application-engineering`
- `security-review`
- `api-contracts`
- `context-efficiency`

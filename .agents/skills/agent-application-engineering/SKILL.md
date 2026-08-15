---
name: agent-application-engineering
description: Design and debug production LLM/agent applications across prompts, tool routing, structured outputs, memory, retrieval, loops, evaluation, cost and wrapper layers. Use when the product itself contains an LLM or autonomous agent.
---

# Agent & LLM Application Engineering

## Purpose

Own the application architecture around models. Model quality alone is not enough: tool enforcement, context assembly, memory admission, retrieval, loop termination, typed protocols, hidden retries and transport layers can create failures that look like model mistakes.

This skill owns this responsibility narrowly. It complements the general V5.6.1 planning, implementation, testing, review, security, performance and verification system rather than replacing those layers. Prefer project-native conventions and current authoritative documentation over memorized framework details.

## When to Activate

- Chat/assistant/copilot/agent products, tool-using LLMs or multi-agent workflows.
- RAG/memory/context systems where retrieved state affects model decisions.
- Agent behavior degrades after wrapper, prompt, tool or memory changes.
- Productionization of an LLM prototype with cost, latency, safety and evaluation needs.

Do not activate merely because a technology is fashionable. For existing repositories, preserve the established architecture unless the requested change or verified defect justifies a deliberate deviation.

## Required Inputs

- User-visible capability and boundaries of autonomous action.
- Model/provider candidates and runtime tool surface.
- System/developer prompts, tool schemas, memory/retrieval sources and orchestration loop.
- Risk of side effects, sensitive data, prompt injection and external content.
- Evaluation dataset/acceptance behaviors, cost and latency budgets.

If an input is unknown and materially changes the design, research or derive it before making an irreversible choice. Record consequential assumptions.

## Decision Framework

- Enforce critical tool/permission invariants in code, not prose alone.
- Use typed/validated internal envelopes for actions/state where freeform text could corrupt workflow control.
- Separate session context, long-term memory, retrieval and durable business state; define admission/expiry/source authority for each.
- Keep retrieval evidence attributable and treat external/repository content as untrusted data when it can contain instructions.
- Define loop termination, budget, retry/escalation and human approval for consequential actions.
- Route deterministic tasks to deterministic code/tools before asking an LLM.
- Evaluate capability and regression behavior across realistic cases, including tool failures and adversarial inputs.
- Make model/provider choices configurable and measure quality/latency/cost rather than hardcoding one model everywhere.

Prefer the simplest design that satisfies correctness, operability, security and expected scale. Reject complexity whose benefit cannot be tied to a concrete requirement or measured risk.

## Workflow

1. **Capability contract** — Define what the agent may decide/do and which actions need gates.
2. **Layer map** — Map prompt/context/memory/retrieval/tools/model/orchestrator/transport/persistence.
3. **Protocols** — Define tool schemas, state envelopes and error behavior.
4. **Security** — Threat-model external instructions, credentials, data exfiltration and side effects.
5. **Evaluation** — Build representative capability/regression cases before tuning.
6. **Implementation** — Add explicit budgets, retries, model routing and observability.
7. **Audit** — Compare direct model/tool behavior against wrapper-delivered behavior and hunt hidden mutation.
8. **Operate** — Track failures, cost, latency, tool success and evaluation drift.

## Expert Heuristics

- When the base model behaves correctly but the product does not, audit wrapper layers before blaming the model.
- Do not allow model-generated summaries to silently become higher-authority memory than user corrections or verified data.
- Tool descriptions should be precise, but permission and mandatory-action enforcement belongs in runtime logic.
- Use retrieval only when it improves grounded decisions; duplicating the same material in prompt, history and memory wastes context and can create contradictions.
- A second hidden LLM repair pass can change semantics; make repair explicit and evaluated.

## Edge Cases and Failure Modes

- Streaming output and tool calls interleave.
- Interrupted/resumed runs with partially executed side effects.
- Multiple agents edit shared state.
- Prompt injection arrives through websites, docs, code comments or tool output.
- Model/provider updates change behavior without code changes.
- Long sessions trigger compaction and memory loss/duplication.

## Anti-Patterns

- Treating prompt engineering as the only control plane.
- Persisting unrestricted chain-of-thought/agent assertions as memory.
- Giving all tools to every subagent regardless of task.
- Infinite autonomous loops without budget/termination/recovery.
- Evaluating only ideal user prompts and ignoring tool/provider failures.

## Verification and Evidence

- Tool calls and permission gates are observable and cannot be bypassed by output prose.
- Memory/retrieval authority and lifecycle are testable.
- Evaluation suite includes success, refusal/guardrail, failure and adversarial cases.
- Cost/latency/tool-error metrics exist for production-critical paths.
- Wrapper output matches intended model/tool results without silent mutation.

A worker report is a claim, not proof. Prefer executable evidence, contract checks, targeted tests, profiling/inspection output, runtime observations and precise diffs.

## Related Skills

- `ai-evaluation`
- `mcp-server-engineering`
- `security-review`
- `context-efficiency`
- `adversarial-verification`
- `reliability-observability`

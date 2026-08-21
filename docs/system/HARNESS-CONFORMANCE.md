# Harness Conformance and Capability Negotiation — V5.8.1

CtrlAltDelegate defines one behavioral contract and maps it onto native harness capabilities. It does not force every harness to emulate another harness.

## Support classes

- `REFERENCE`: Pi reference/golden-path semantics.
- `FIRST_CLASS`: explicitly tested integration target.
- `FIRST_CLASS_PREVIEW`: explicitly supported but upstream compatibility is still unstable.
- `COMPATIBLE`: supported through common instruction/skill/tool surfaces with best-effort feature mapping.

V5.8.1 targets:
- Pi — `REFERENCE`;
- OpenAI Codex CLI — `FIRST_CLASS`;
- DeepSeek Harness — `FIRST_CLASS_PREVIEW`;
- Claude Code — `COMPATIBLE`;
- OpenCode — `COMPATIBLE`.

## Capability negotiation

Do not model a harness feature as a boolean when its strength matters. Conformance may describe native instruction loading, `.agents/skills`, session resume, subagent structured output/depth/tool filters/continuation, sandbox modes and enforcement completeness, approval behavior, hooks, compaction, headless execution and tool/context scoping.

A job may require harness/worker capabilities. Dispatch only when required capabilities are proven. Unsupported capabilities fail loud or cause a safe reroute; they are never accepted and silently ignored.

## DeepSeek Harness

DeepSeek Harness is treated as `FIRST_CLASS_PREVIEW` because the public project is still in developer preview and warns of breaking changes. V5.8.1 uses its native `.agents/skills` compatibility and AGENTS-compatible workspace instructions when available; no duplicate `.dsh/skills` library is generated. In a root-native CtrlAltDelegate repository the canonical `.agents/skills` path is discovered directly. In an imported Custom-GPT control package, prefer the harness's custom-skill-directory capability to point at `./.ctrlaltdelegate/.agents/skills`; if unavailable, route and read those skill files explicitly instead of copying them into the product tree.

The integration also recognizes DeepSeek Harness concepts that generalize well across harnesses: append-only session facts, reconstructable model-visible context, per-call sandbox policy with full/partial enforcement reporting, fail-closed approval, continuable subagent capabilities and minimal tool/context profiles. These are adapted into CtrlAltDelegate contracts rather than copied as a runtime dependency.

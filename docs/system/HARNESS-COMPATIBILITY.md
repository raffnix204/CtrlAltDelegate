# Harness Compatibility & Capability Bootstrap — V5.8.2

One methodology, one canonical `.agents/skills` library, capability-negotiated adapters.

- Pi: `REFERENCE`.
- OpenAI Codex CLI: `FIRST_CLASS`.
- Command Code: `FIRST_CLASS_PREVIEW`; see `COMMAND-CODE-FIRST-CLASS-PREVIEW.md`.
- DeepSeek Harness: `FIRST_CLASS_PREVIEW` while upstream remains pre-stable.
- Claude Code / OpenCode: `COMPATIBLE`.

`HARNESS_READY` means the **required current-job capabilities** are verified, not merely that a binary exists. Missing capability follows the V5.8.2 resolver: native/existing → current primary research → safe project-local bootstrap → register/restart → smoke-test → attestation. No core model routing.

Command Code uses `AGENTS.md` and `.agents/skills` directly when its installed client supports them. Native tasks are an execution mirror of `JOB-GRAPH.json`, never a replacement for CtrlAltDelegate state. Claude retains thin `.claude/skills` adapters. DeepSeek retains canonical `.agents/skills` rather than a duplicate `.dsh/skills`.

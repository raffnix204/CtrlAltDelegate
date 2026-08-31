# Harness Compatibility & Capability Bootstrap — V5.9

One methodology, one canonical `.agents/skills` library, capability-negotiated adapters.

- Pi: `REFERENCE`.
- Oh My Pi: `FIRST_CLASS`; inherits Pi methodology and uses native task/model/worktree/structured-output capabilities through `adapters/oh-my-pi/`.
- OpenAI Codex CLI: `FIRST_CLASS`.
- Command Code: `FIRST_CLASS_PREVIEW`; see `COMMAND-CODE-FIRST-CLASS-PREVIEW.md`.
- DeepSeek Harness: `FIRST_CLASS_PREVIEW` while upstream remains pre-stable.
- Claude Code / OpenCode: `COMPATIBLE`.

`HARNESS_READY` means the **required current-job capabilities** are verified, not merely that a binary exists. Missing capability follows the V5.9 resolver: native/existing → current primary research → safe project-local bootstrap → register/restart → smoke-test → attestation. Model routing is capability-class based when the harness supports per-subagent model selection; otherwise roles inherit the active model. OMP FRONTIER/Sol routing uses an explicit `:high` selector rather than generic `effort: hi`.

Command Code uses `AGENTS.md` and `.agents/skills` directly when its installed client supports them. Native tasks are an execution mirror of `JOB-GRAPH.json`, never a replacement for CtrlAltDelegate state. Claude retains thin `.claude/skills` adapters. DeepSeek retains canonical `.agents/skills` rather than a duplicate `.dsh/skills`.

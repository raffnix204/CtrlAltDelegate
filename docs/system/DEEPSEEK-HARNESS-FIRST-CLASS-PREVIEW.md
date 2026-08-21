# DeepSeek Harness First-Class Preview Target — V5.8.1

Repository: https://github.com/deepseek-ai/deepseek-harness
Reviewed public release line: `0.1.0-rc.7`, developer preview, reviewed 2026-08-19.

CtrlAltDelegate treats DeepSeek Harness as a first-class preview execution target because it natively supports AGENTS-compatible workspace instructions, `.agents/skills` discovery, persistent/replayable session events, headless execution, capability-scoped subagents, sandbox and approval services, hooks and optional compaction.

## Integration rules

1. Keep `.agents/skills` as the single canonical skill source; do not create a redundant `.dsh/skills` copy.
2. Detect actual DSH capabilities at runtime rather than assuming a particular RC contract remains stable.
3. Prefer native DSH session/subagent/sandbox/approval mechanisms when they satisfy the CtrlAltDelegate contract.
4. Record partial sandbox enforcement as partial; never upgrade it to a full security claim.
5. Preserve CtrlAltDelegate's trust model for untrusted web/file/tool content. Harness capability does not turn retrieved content into authority.
6. Because upstream is preview, conformance failures degrade to explicit compatibility findings, not silent behavior changes.

## Efficiency lesson

DeepSeek's minimal runtime demonstrates the value of a small tool/context surface. CtrlAltDelegate therefore right-sizes process, context and tool exposure together. MICRO/SMALL work should not load unrelated skills/tools merely because the harness can expose them.

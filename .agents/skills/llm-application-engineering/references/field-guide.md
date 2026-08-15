# LLM Application Engineering — Deep Reference

## Determinism-first ladder
exact parser/rules/database/search → lightweight classifier/model → LLM structured output → stronger model/tool loop only when lower tiers cannot meet quality.

## Cost/quality signals
track request class, model/capability route, prompt/context size, cache hit, latency, retries, tool calls, structured-output repair, eval result and estimated/actual cost when available.

Do not hardcode vendor model names into architecture unless the product explicitly depends on them; resolve current model capabilities at runtime/research time.

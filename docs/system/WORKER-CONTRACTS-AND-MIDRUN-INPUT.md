# Worker Contracts and Mid-Run Input — V5.7.1

Delegated work uses an explicit worker contract: purpose, required capabilities, permission class, allowed scope, protected/prohibited scope, dependencies, done-when predicates, required evidence, output/report path and interruption/checkpoint behavior. A worker is not trusted merely because it was spawned.

Use native harness tool filters, sandbox modes, permissions and structured output when available. Unsupported required capabilities fail loud or reroute.

Long-running orchestration also maintains `planning/execution/PENDING-INPUT.jsonl`. New user/external input is admitted at safe orchestration boundaries, classified for authority and impact, then either applied locally, causes scoped invalidation/replanning, or becomes a hard-stop decision. Do not redirect a turn already underway when the harness cannot safely steer it; queue the input for the next safe step.

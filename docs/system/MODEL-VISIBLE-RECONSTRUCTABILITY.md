# Model-Visible Reconstructability — V5.8

For consequential execution decisions, context that influences the agent should be attributable to durable project/control state, explicit user input, a routed skill/reference, or a recorded external source/tool result.

When the harness provides an event-sourced session log, use it. When it does not, CtrlAltDelegate still persists enough state in planning/control artifacts to reconstruct the current lifecycle, job, constraints, selected skills, decision rulings and evidence.

A context compaction or restart must not create hidden authority. After compaction/resume, reload the minimal authoritative state and verify that the active job and protected constraints remain represented.

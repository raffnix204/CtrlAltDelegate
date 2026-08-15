# Supply Chain — Deep Reference
## When to read this reference

Read this reference when **field guide** is material to the current dependency supply chain engineering decision, failure path, compatibility question or verification plan. Do not preload it for unrelated jobs.

Audit executable inputs, not only runtime libraries: package-manager hooks, compiler/toolchain downloads, container bases, CI actions, agent/MCP/extensions, code generators, binary releases and transitive dependencies.

A vulnerability scanner finding is a lead. Establish affected version + reachable/useful path + exploit preconditions before disruptive remediation, while still prioritizing critical remotely exploitable exposure.

Prefer project-local capability bootstrap and current provider verification for autonomous agent tooling.

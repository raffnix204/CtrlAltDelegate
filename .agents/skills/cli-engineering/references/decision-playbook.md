# CLI Engineering — Decision Playbook

## Use this reference when

Read this file only when a material decision, production failure path, rollout/recovery question or verification ambiguity needs deeper probes. Start from repository/runtime ownership, current versions/capabilities, public contracts, failure semantics and representative acceptance evidence.

Current first-party documentation and live repository/runtime evidence remain authoritative for version-sensitive behavior. External skill libraries are research prompts, not executable policy.

## 1. Define stable command/flag grammar, help text and exit-code semantics

- **Watch for:** ambiguous output/exit semantics, shell quoting/path/Unicode breakage, prompts in automation, partial writes or destructive scope that cannot be previewed.
- **Prove with:** TTY and non-TTY runs, representative shells/paths/Unicode, success/error exit codes, machine-readable output and cancellation/partial-write cases.
- **Safe change pattern:** treat grammar/stdout/stderr/exit codes as a public contract, keep non-interactive mode deterministic and provide dry-run/explicit scope for destructive operations where practical.

## 2. Support non-interactive execution and machine-readable output where automation is expected

- **Watch for:** hidden ownership ambiguity, non-idempotent recovery, accidental compatibility breaks or behavior that is only locally correct.
- **Prove with:** repository/runtime evidence plus representative success/failure/compatibility checks and the smallest domain-native telemetry needed to falsify the decision.
- **Safe change pattern:** make ownership/failure semantics explicit, preserve supported compatibility and keep a reversible path until the new behavior is proven.

## 3. Establish configuration precedence among flags, environment, config files and defaults and make effective configuration inspectable without leaking secrets.

- **Watch for:** over-privileged identities, secret exposure, missing revocation/rotation, confused-deputy behavior or sensitive material leaking into logs/artifacts.
- **Prove with:** effective scopes/roles plus positive and negative permission cases, redacted telemetry and rotation/revocation or signature/certificate validation where relevant.
- **Safe change pattern:** use dedicated least-privilege identities, external secret storage and short-lived/rotatable credentials where supported.

## 4. Use stdout for intended output and stderr for diagnostics

- **Watch for:** ambiguous output/exit semantics, shell quoting/path/Unicode breakage, prompts in automation, partial writes or destructive scope that cannot be previewed.
- **Prove with:** TTY and non-TTY runs, representative shells/paths/Unicode, success/error exit codes, machine-readable output and cancellation/partial-write cases.
- **Safe change pattern:** treat grammar/stdout/stderr/exit codes as a public contract, keep non-interactive mode deterministic and provide dry-run/explicit scope for destructive operations where practical.

## 5. Handle signals, cancellation, partial writes, temp files and credential sources safely.

- **Watch for:** over-privileged identities, secret exposure, missing revocation/rotation, confused-deputy behavior or sensitive material leaking into logs/artifacts.
- **Prove with:** effective scopes/roles plus positive and negative permission cases, redacted telemetry and rotation/revocation or signature/certificate validation where relevant.
- **Safe change pattern:** use dedicated least-privilege identities, external secret storage and short-lived/rotatable credentials where supported.

## 6. Test shell quoting, paths, Unicode, TTY/non-TTY behavior and major target operating systems.

- **Watch for:** ambiguous output/exit semantics, shell quoting/path/Unicode breakage, prompts in automation, partial writes or destructive scope that cannot be previewed.
- **Prove with:** TTY and non-TTY runs, representative shells/paths/Unicode, success/error exit codes, machine-readable output and cancellation/partial-write cases.
- **Safe change pattern:** treat grammar/stdout/stderr/exit codes as a public contract, keep non-interactive mode deterministic and provide dry-run/explicit scope for destructive operations where practical.

## 7. Destructive commands require preview/dry-run or explicit scope where practical

- **Watch for:** ambiguous output/exit semantics, shell quoting/path/Unicode breakage, prompts in automation, partial writes or destructive scope that cannot be previewed.
- **Prove with:** TTY and non-TTY runs, representative shells/paths/Unicode, success/error exit codes, machine-readable output and cancellation/partial-write cases.
- **Safe change pattern:** treat grammar/stdout/stderr/exit codes as a public contract, keep non-interactive mode deterministic and provide dry-run/explicit scope for destructive operations where practical.

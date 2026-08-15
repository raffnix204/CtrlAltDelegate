# Angular Routing, SSR & Upgrades

Guards/resolvers/lazy routes shape navigation and loading, but authorization belongs on the server. Avoid resolver chains that make navigation depend on unrelated slow data when the page could stream/load progressively.

SSR-safe code does not read browser globals at module evaluation or share per-request mutable state through long-lived singletons. Verify hydration on production output and representative deep links.

For major upgrades use Angular update tooling/migrations appropriate to the installed versions, then review generated changes and third-party peer compatibility. Run build/tests before and after each material migration step when attribution matters.

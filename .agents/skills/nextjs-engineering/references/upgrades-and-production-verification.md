# Next.js Upgrades & Production Verification

For a major upgrade:

1. record current Next.js/React/Node/package-manager versions;
2. read each crossed major migration guide;
3. run vendor/framework codemods where appropriate and review their diff;
4. update peer dependencies and type packages coherently;
5. resolve removed/renamed config and async/request API changes;
6. run production build, tests and browser acceptance;
7. verify deployment adapter/runtime rather than assuming local Node behavior.

Upgrade one conceptual breakage class at a time when the diff is large enough that attribution would otherwise become ambiguous.

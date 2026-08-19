# SEO Drift Baseline Fields and Severity

Use when implementing deterministic pre/post-deployment checks.

Recommended stable fields: normalized URL, status, redirect target, canonical, robots directives, title/meta description, H1 and stable heading outline, structured-data canonicalized hash/shape, sitemap inclusion, semantic/rendered content fingerprint, Open Graph essentials and performance metrics when the source is comparable.

Classify findings by impact: `CRITICAL` for accidental deindexing/broken canonical/status/redirect behavior on key routes; `HIGH` for broad template/rendering/schema regressions; `MEDIUM` for meaningful metadata/content-structure drift; `INFO` for intentional or low-impact changes. Project-specific evidence may change severity.

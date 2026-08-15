# Web Acquisition — Deep Reference
## When to read this reference

Read this reference when **field guide** is material to the current web data acquisition engineering decision, failure path, compatibility question or verification plan. Do not preload it for unrelated jobs.

## Provider-neutral capability contract
SEARCH: discover candidate URLs/sources.
MAP: enumerate a bounded site's relevant URL space.
SCRAPE: retrieve a known URL as clean content/metadata.
CRAWL: traverse a scoped corpus respecting access/rate limits.
EXTRACT: normalize required structured fields with provenance.
BROWSER: separate capability for interaction, JS state, auth, screenshots and visual acceptance.

An existing Firecrawl-compatible MCP/API may satisfy SEARCH/SCRAPE/MAP/CRAWL/EXTRACT. Do not install another provider if capabilities are already healthy.

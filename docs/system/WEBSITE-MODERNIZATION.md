# Website Modernization — GitHub-Native V5.6.1

This document is the GitHub-native operating guide for rebuilding an existing site.

## Start prompt

```text
Read AGENTS.md and GOAL.md.
The project is an existing-site modernization.
Complete source acquisition before broad implementation.
Preserve legitimate content/search/brand value, but redesign the UI/UX as a modern product.
Continue autonomously through verified completion.
```

## Source-site fields in GOAL.md

Record:
- source URL;
- ownership/reuse authorization;
- migration objective;
- domain/URL preservation constraints;
- language/subdomain scope;
- known critical pages;
- whether WEB_ACQUISITION provider (for example Firecrawl) credentials/tooling are available.

## Acquisition modes

### WEB_ACQUISITION provider (for example Firecrawl) available

Use a researched/pinned WEB_ACQUISITION provider (for example Firecrawl) integration as an Execution Tool.

Recommended sequence:
1. map URLs;
2. define include/exclude scope;
3. crawl with robots compliance;
4. obtain Markdown + metadata + links;
5. scrape representative high-value pages with images/screenshots where useful;
6. record crawl errors/robots blocks;
7. persist normalized results under `planning/source-site/`.

Use `FIRECRAWL_API_KEY` only from environment/secret storage. Never commit it.

### WEB_ACQUISITION provider (for example Firecrawl) unavailable

Use:
- sitemap discovery;
- HTTP fetch;
- browser automation;
- CMS export;
- user-supplied exports;
- Search Console/analytics/logs if available.

The goal is deterministic coverage, not allegiance to one crawler.

## Mandatory artifact set

See `website-modernization` skill. At minimum:
- `planning/source-site/CRAWL-SCOPE.md`
- `planning/source-site/URL-INVENTORY.csv`
- `planning/source-site/CONTENT-INVENTORY.md`
- `planning/source-site/ASSET-INVENTORY.csv`
- `planning/source-site/SEO-BASELINE.md`
- `planning/source-site/REDIRECT-MAP.csv`

## No-code-before-crawl rule

If `STATE.md` says source acquisition is incomplete, do not start broad template/page implementation.

Allowed before completion:
- crawler/tool setup;
- repository/runtime bootstrap;
- source inventory normalization;
- isolated design exploration not tied to incomplete content.

## Migration safety

Do not:
- bypass robots/access controls;
- copy third-party protected media without authorization;
- erase high-value legacy URLs;
- rewrite factual claims from imagination;
- launch with staging noindex rules;
- mass-redirect unrelated pages to home.

## Definition of source readiness

`SOURCE_READY` requires:
- crawl scope defined;
- acquisition completed or documented gaps;
- page families classified;
- priority URLs identified;
- every important URL has content action;
- assets have reuse/replace decisions;
- SEO baseline exists;
- redirect strategy exists;
- functional behaviors are inventoried.

Then build from real migrated content.


## V5.6.1 provider routing
Bulk corpus discovery/content uses `WEB_ACQUISITION`; browser is required for representative interactive/visual verification. Existing self-hosted Firecrawl/compatible MCP wins over installing another crawler.

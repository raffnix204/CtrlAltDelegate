# Web Acquisition & Browser Routing — V5.6.3

## Capabilities
`WEB_SEARCH`, `WEB_SCRAPE`, `WEB_MAP`, `WEB_CRAWL`, `WEB_EXTRACT`.

Provider-neutral resolution:
1. existing active compatible MCP/API/tool;
2. existing Firecrawl/Firecrawl-compatible service;
3. harness-native search/fetch when sufficient;
4. research/install current compatible provider only if materially required.

Examples include self-hosted Firecrawl and Firecrawl-compatible CRW/fastCRW. They are not V5.6.3 dependencies.

## Use WEB_ACQUISITION for
- current technical research and official docs;
- clean Markdown/JSON extraction;
- whole-site URL mapping/crawl;
- content/metadata/assets inventory;
- structured extraction.

## Use browser for
- JavaScript/user interaction;
- auth/forms/navigation state;
- screenshots/visual comparison;
- responsive/input-mode/motion behavior;
- browser acceptance/runtime errors.

For website modernization: broad acquisition first, representative browser inspection second.

## Token efficiency
Prefer clean structured/Markdown output and targeted extraction over dumping raw HTML into context. Persist raw crawl artifacts outside hot context.

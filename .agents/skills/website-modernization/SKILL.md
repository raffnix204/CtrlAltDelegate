---
name: website-modernization
description: "Use when the task materially involves this skill's owned domain: Turn an existing public website into a modern, high-quality replacement while preserving legitimate content value, search equity, brand intent and important URLs."
---

# Website Modernization & Content Migration

Skill ID: `website-modernization`
Library: `software-planning-lead-v5.6.1`
Version: `5.6.1`

## Purpose

Turn an existing public website into a modern, high-quality replacement while preserving legitimate content value, search equity, brand intent and important URLs.

This skill owns **source-site acquisition, migration inventory, preservation/rewriting decisions and rebuild parity**. Visual design, Product UX, SEO, copywriting, accessibility, motion and implementation remain delegated to their specialist skills.

## Profiles

website_modernization, marketing_website, content_website, ecommerce

## Typical roles

migration-planner, web-researcher, content-migration-agent, seo-migration-reviewer, frontend-implementer

## Activation

Use when the user provides an existing website/domain and asks to:
- redesign or modernize it;
- rebuild it in a new framework/CMS;
- preserve or improve current content;
- improve SEO/UX/accessibility/performance;
- migrate URLs, pages, downloads or images;
- reproduce the legitimate content/business purpose in a new implementation.

## Authorization boundary

Before copying content/assets, establish the reuse basis.

### Owned/authorized source
If the user owns/controls the source or confirms reuse rights, migrate public copy/assets according to the plan.

### Reference/competitor source
If the user does not have reuse rights:
- inspect structure, interaction patterns and public facts only as research;
- create original copy/design/assets;
- do not wholesale reproduce protected text, photography, illustrations, logos or brand identity;
- do not bypass authentication, paywalls, bot protection or technical access controls.

Respect robots/access rules and rate limits. Do not set crawler options to ignore robots rules merely to increase coverage.

## Source acquisition architecture

Website modernization uses two acquisition levels.

### Level A — Planning reconnaissance
The planner:
- confirms source URL/domain and scope;
- maps representative/important URLs using web search, sitemap discovery or an available crawler action;
- inspects representative pages, navigation, page types, copy, metadata, visible assets and UX;
- records gaps and crawl confidence;
- establishes redesign/migration strategy.

### Level B — Complete deterministic acquisition
Before implementation, obtain a complete in-scope URL/content/asset inventory.

Preferred when available:
- a `WEB_ACQUISITION` provider capable of the required search/scrape/map/crawl/extract operations. Existing Firecrawl/Firecrawl-compatible MCP or API providers are valid examples, not mandatory dependencies.

Fallback:
- sitemap(s) + HTTP fetch + browser automation + project scripts;
- CMS export supplied by the user;
- Search Console/analytics/server logs when available for high-value legacy URLs.

A planner must never label reconnaissance as a complete crawl.

## Custom-GPT vs Coding-Agent rule

### Custom GPT with configured crawler Action
The planner may perform Level B during planning and embed the normalized corpus/inventories in the final ZIP.

### Custom GPT without crawler Action
Use Web Search/browser research for Level A only. Export a mandatory `SOURCE_ACQUISITION` preflight job for the coding agent. The coding agent completes Level B **before any broad redesign/implementation job**.

### GitHub-native edition
The coding agent performs both levels in-repository. Resolve acquisition by capability: use an existing compatible MCP/API/tool first; install a provider only when the required capability is missing and current compatibility has been researched. Browser tooling remains separate for interactive/visual behavior.

## Required source-site artifacts

Create/use:

`planning/source-site/CRAWL-SCOPE.md`
- base URLs/domains;
- allowed subdomains;
- languages/locales;
- include/exclude paths;
- query-parameter policy;
- public/authenticated scope;
- acquisition mode;
- authorization/reuse statement.

`planning/source-site/URL-INVENTORY.csv`
Suggested columns:
`source_url,status,page_type,title,indexable,canonical,priority,content_action,target_url,notes`

`planning/source-site/CONTENT-INVENTORY.md`
- page/template clusters;
- primary messages;
- services/products;
- proof/testimonials;
- contact/legal/company content;
- content gaps/duplication;
- rewrite/consolidation opportunities.

`planning/source-site/ASSET-INVENTORY.csv`
Suggested columns:
`source_url,asset_url,type,alt_or_context,reuse_rights,action,target_path,optimization_notes`

`planning/source-site/SEO-BASELINE.md`
- title/meta/H1 patterns;
- canonicals/hreflang;
- robots/indexability;
- structured data;
- internal link model;
- sitemap status;
- notable ranking/search-intent pages when evidence is available.

`planning/source-site/REDIRECT-MAP.csv`
Suggested columns:
`old_url,new_url,action,status_code,reason,verified`

Optional when full crawl is captured:
`planning/source-site/content/<normalized-page-id>.md`
`planning/source-site/screenshots/`
`planning/source-site/raw/` for machine-readable crawler exports.

## Acquisition workflow

### 1. Scope the domain
Define:
- canonical hostname;
- www/non-www/http/https variants;
- subdomains;
- language paths;
- blog/docs/shop areas;
- file/download paths;
- parameters/faceted URLs;
- sections explicitly out of scope.

### 2. Discover URLs
Use multiple signals where available:
- XML sitemap(s);
- crawler map/discovery;
- navigation/internal links;
- Search Console/export;
- analytics/server logs;
- CMS export;
- known backlink/legacy landing pages.

Deduplicate normalized URLs while retaining legacy aliases that need redirects.

### 3. Capture each page
For in-scope pages capture at least:
- source URL and status;
- title/description and canonical;
- primary headings;
- clean main content;
- important internal/external links;
- image/media URLs and context;
- page type/template;
- indexability;
- language/locale;
- structured-data presence where relevant.

For key visual pages also capture desktop/mobile screenshots where tooling permits.

### 4. Cluster templates and content
Group URLs into page families:
- home;
- service/product;
- category/listing;
- article;
- case study/project;
- about/team;
- contact/location;
- legal/policy;
- utility/search;
- ecommerce product/category;
- custom types.

This prevents designing every legacy URL separately.

### 5. Assign a content action
Every important source URL receives one:

- `PRESERVE` — wording/content remains materially unchanged;
- `IMPROVE` — keep meaning/facts, rewrite for clarity/search/user intent;
- `MERGE` — consolidate duplicate/thin pages into a stronger target;
- `RESTRUCTURE` — preserve content but change information architecture/template;
- `REPLACE` — obsolete presentation/content replaced with newly researched material;
- `RETIRE` — no equivalent; return correct 404/410 or intentional noindex handling.

Never silently drop an indexed/linked page.

### 6. Assign asset actions
For each relevant image/download:
- `REUSE`;
- `OPTIMIZE`;
- `RECREATE` from owned source material;
- `REPLACE` with a new licensed/original asset;
- `EXCLUDE`.

Preserve meaningful filenames/alt context when useful; improve accessibility and performance rather than copying broken legacy markup.

### 7. Separate content truth from legacy presentation
The old website is a content/business source, not a design system by default.

Extract:
- brand identity that should remain;
- trustworthy content/facts;
- navigation intent;
- valuable SEO URLs;
- conversion/business goals.

Then redesign with current `ux-product-design`, `ui-design-system`, `motion-design-engineering`, responsive, accessibility, visual-polish and performance skills.

### 8. SEO migration strategy
If URLs change:
- build a one-to-one old→new mapping wherever possible;
- use permanent server-side redirects for real moves;
- avoid redirect chains and irrelevant mass redirects;
- update internal links, canonicals, hreflang and sitemap;
- retain useful image/download destinations or map them;
- verify no staging `noindex`/robots blocks remain at launch.

If URLs do not need to change, preserve them by default.

### 9. Content enhancement
Use `content-copywriting` and `seo-content` to improve:
- unclear headings;
- outdated claims;
- thin service/product explanations;
- missing trust/proof;
- local/entity details;
- internal linking;
- duplicated pages;
- stale CTAs.

Never invent business facts, testimonials, certifications, prices or legal claims.

### 10. Functional inventory
Record behavior that must survive the rebuild:
- forms and destinations;
- newsletter/signup;
- search/filter;
- downloads;
- maps/location details;
- ecommerce/cart/payment;
- tracking/analytics;
- cookie/privacy controls;
- structured data;
- third-party embeds;
- contact links;
- redirects/custom error pages.

## Design-modernization workflow

1. Audit current information hierarchy and user journeys.
2. Create a concise **Design Read** for audience, business type and desired trust/personality.
3. Preserve intentional brand equity; remove accidental legacy constraints.
4. If art direction is uncertain/high-stakes, explore 2–3 genuinely different directions before committing.
5. Define modern design system and responsive behavior.
6. Implement representative high-value templates first.
7. Validate against migrated real content, not lorem ipsum.
8. Run visual, accessibility, SEO, performance and browser gates.
9. Verify all source URLs/content actions are accounted for.

## Verification gates

### Source coverage gate
- every in-scope legacy URL is in inventory;
- every priority URL has a content action and target;
- crawl errors/robots-blocked URLs are listed;
- unknown high-value legacy URLs trigger investigation.

### Content parity gate
- no important factual content disappears unintentionally;
- contact/legal/company data is preserved or intentionally revised;
- forms/downloads/important outbound links are preserved or intentionally changed;
- rewritten content remains factually grounded.

### Asset gate
- reused assets have authorization;
- no broken hotlinks;
- migrated assets are optimized/responsive;
- alt text/context is improved where appropriate.

### SEO migration gate
- redirect map tested;
- canonicals and internal links target final URLs;
- sitemap contains final indexable URLs;
- intended indexability is correct;
- structured data remains valid where used;
- no universal redirect-to-home behavior.

### Visual/UX gate
- new pages are not merely a reskin of legacy markup;
- representative mobile/laptop/wide screenshots show a coherent modern system;
- real migrated content fits without clipping/overflow;
- motion is deliberate;
- accessibility and performance gates pass.

## Anti-patterns

- scraping only the homepage and assuming the site is understood;
- copying old HTML/CSS as the new architecture;
- redesigning before URL/content inventory;
- dropping old indexed pages because they look obsolete;
- copying third-party images without reuse rights;
- using the old site's visual defects as requirements;
- rewriting factual content without evidence;
- creating new URLs without redirects;
- redirecting every retired URL to the homepage;
- treating Firecrawl, CRW or any named acquisition provider as mandatory;
- disabling robots compliance to increase scrape coverage;
- claiming a full crawl when only search snippets/representative pages were inspected.

## Evidence / acceptance

The modernization is implementation-ready when:
- crawl scope/authorization is explicit;
- source acquisition mode is explicit;
- all known page families and important URLs are inventoried;
- full crawl is complete now **or** is a mandatory first execution job before implementation;
- page/content/asset actions are defined;
- SEO migration/redirect policy is defined;
- design modernization strategy is independent from legacy presentation;
- selected UI/UX/content/SEO skills are routed;
- final verification traces source URL → content action → target URL → implementation/evidence.
## Web acquisition vs browser

Use `WEB_ACQUISITION` for URL discovery, textual/structured content, metadata, assets, map/crawl and research. Prefer clean Markdown/JSON over raw HTML when it preserves needed evidence.

Use a real browser capability for JavaScript interaction, authentication flows, menus/forms, visual state, responsive screenshots, animation and browser acceptance. A crawler does not prove interactive behavior; a browser should not be the default mechanism for bulk textual crawl if a suitable acquisition API already exists.

For source-site rebuilds, acquire the broad corpus with `WEB_ACQUISITION`, then sample representative/high-risk pages in the browser for visual/functional evidence.

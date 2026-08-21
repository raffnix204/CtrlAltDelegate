---
name: seo-content
description: Make public content crawlable, indexable, understandable and useful using current primary-source search guidance, while treating AI-search/GEO claims as evidence-sensitive rather than folklore.
---

# Technical SEO & Search Discoverability

Skill ID: `seo-content`
Library: `software-planning-lead-v5.6.1`
Version: `5.6.1`

## Purpose

Make public content crawlable, indexable, understandable and useful using current primary-source search guidance, while treating AI-search/GEO claims as evidence-sensitive rather than folklore.

## Profiles

marketing_website, content_website, ecommerce

## Typical roles

seo-specialist, web-engineer, content-strategist

## Critical rule
Search platform guidance changes. During each project, verify consequential claims against current official Search Central/Bing/vendor documentation. This skill provides stable engineering principles, not guaranteed ranking recipes.

## Technical workflow
### 1. Crawl/index model
For every route class decide:
- public/indexable;
- public/noindex;
- authenticated/private;
- duplicate/filter/search variant;
- canonical target.

Ensure intended public pages return accessible indexable content and are not accidentally blocked by robots/noindex/auth/client-only rendering failures.

### 2. Information architecture
Use descriptive stable URLs and internal links reflecting user concepts. Orphan pages and infinite faceted URL spaces require explicit handling.

### 3. Canonicalization
Prefer one primary URL per content item. Use redirects for true moves/duplicates when appropriate; use canonical hints when multiple accessible representations must exist. Keep sitemap/canonical/internal links consistent.

### 4. Titles/snippets/headings
Create unique, concise, accurate page titles and helpful page content. Meta descriptions summarize rather than stuff keywords; search engines may generate their own snippets. Heading hierarchy supports readers and structure.

### 5. Structured data
Add schema only when it truthfully represents visible page content/entity and when the target search platform currently supports/benefits from that type. Validate syntax and platform eligibility. Never fabricate reviews, ratings, prices or organizational facts for rich results.

### 6. Sitemap/robots
Generate sitemaps for intended canonical indexable URLs; accurate modification data when available. Robots controls crawling, not guaranteed deindexing. Do not block resources required to render/understand important pages without reason.

### 7. Multilingual/international
When relevant define locale URL strategy, localized content, reciprocal hreflang relationships/current search-engine recommendations and `x-default` where appropriate. Do not auto-translate low-quality doorway pages.

### 8. Performance/mobile/accessibility
Search engineering benefits from secure, fast, accessible, device-friendly pages. Coordinate with performance/accessibility skills rather than duplicating them.

## Content quality
Prioritize original, useful, trustworthy material produced for people. Provide direct answers when that helps users, then depth/evidence. Demonstrate real expertise/experience through content itself rather than manufactured "E-E-A-T signals."

## AI search / GEO policy
Treat AI-answer visibility as an emerging distribution surface. Favor:
- clear entities and unambiguous facts;
- source-backed claims;
- crawlable canonical content;
- strong information architecture;
- original research/data when real;
- concise answerable passages plus deeper context.

Do **not** claim that `llms.txt`, word counts, FAQ schema, Markdown headings or any single tactic guarantees citation/ranking. If using emerging conventions, verify adoption/status during project research and mark experimental behavior.

## Monitoring
Plan Search Console/Bing equivalents where relevant:
- indexing/crawl issues;
- query/page performance;
- structured data enhancements;
- sitemap health;
- manual/security issues.

SEO impact can take time; do not infer causation from one short-term movement.

## Existing-site SEO migration

When `website-modernization` is active:
- preserve valuable URLs unless change has a clear benefit;
- inventory legacy indexable URLs from sitemap/crawl/Search Console/analytics when available;
- create explicit old→new mapping for changed URLs;
- use appropriate permanent server-side redirects for real moves;
- avoid redirect chains and mass redirect-to-home patterns;
- update internal links, canonicals, hreflang and sitemap to final URLs;
- include images/download URLs when they carry search/link value;
- verify staging `noindex`/robots controls are removed only at the correct launch point;
- keep factual metadata aligned to the actual page;
- record post-launch monitoring expectations.

Current official search-engine migration guidance outranks static thresholds in this skill.

## Anti-patterns
- keyword stuffing;
- doorway/thin generated pages;
- copied/rewritten competitor content with no value;
- fake author credentials/reviews;
- blocking canonical CSS/JS accidentally;
- blanket robots `Disallow: /*?*` without understanding site behavior;
- assuming meta keywords matter;
- guaranteeing rankings;
- adding schema types unsupported by visible content;
- treating AI-search speculation as established platform guidance.

## Evidence / acceptance
- route indexability matrix;
- canonical/internal-link/sitemap consistency check;
- metadata coverage;
- schema validation where used;
- robots/noindex verification;
- render/crawl check of representative pages;
- current official-source notes for material/volatile decisions.


## Existing repository SEO optimization

Map public routes/rendering, title/meta/OG, robots/sitemap, structured data, redirects, canonical generation, content source/CMS, internal links and performance-relevant templates before editing. Establish baseline, fix high-impact issues, then recrawl/retest representative URLs.

## V5.8 SEO specialist routing
This skill remains a backward-compatible general SEO entrypoint. For substantive planning/implementation, route the owning specialist instead of keeping all SEO concerns monolithic:
- strategy/IA/search intent → `seo-strategy`;
- crawl/index/rendering/migrations → `technical-seo-engineering`;
- content/E-E-A-T/briefs → `seo-content-strategy`;
- structured entities/JSON-LD → `structured-data-seo`;
- page-type/search-task/UX alignment → `search-experience-optimization`;
- regression baselines → `seo-audit-and-drift`;
- location/product-catalog search → `local-commerce-seo`.
Use current primary-source search guidance for drift-sensitive claims.

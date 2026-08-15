# Astro Islands, Content & Rendering

Treat every client hydration directive as an explicit boundary: what browser capability/state requires it, when should hydration happen, and how much subtree becomes client code? Prefer the narrowest interactive island.

Static output fits content whose representation can be decided at build/revalidation time. Server output fits request-specific authentication, personalization or freshness that cannot be precomputed safely. Hybrid projects can mix strategies when the active Astro version/adapter supports them.

Content collections are useful when editorial records need schema validation, typed access and stable build behavior. Keep presentation-specific component state out of content models.

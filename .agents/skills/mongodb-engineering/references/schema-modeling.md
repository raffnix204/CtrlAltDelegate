# MongoDB Schema Modeling

Embed when related data is read/written together, ownership is clear and cardinality/growth is bounded. Reference when the child has independent lifecycle, many-to-many/high cardinality, frequent independent updates or would make documents grow without a safe bound.

Patterns such as bucket/time-series, subset, computed/extended reference and polymorphic documents are tools, not defaults. Start from concrete query/update shapes.

Use `$jsonSchema` or application+database validation strategy where mixed types/missing invariants would break queries. Plan migrations for legacy documents rather than assuming validation retroactively cleans data.

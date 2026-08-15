# Spring MVC/WebFlux, Config & Testing

WebFlux pays off only when the meaningful I/O path is non-blocking. Mixing blocking JDBC/SDK calls on event-loop threads can perform worse than a well-sized servlet stack.

Keep configuration typed and validated at startup. Profiles select environment configuration; they should not silently fork core domain rules.

Use test slices for focused adapter feedback, but retain full-context/HTTP/DB tests for wiring, filters, transactions and serialization behavior.

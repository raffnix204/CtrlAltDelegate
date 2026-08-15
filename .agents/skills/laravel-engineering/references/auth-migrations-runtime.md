# Laravel Auth, Migrations & Runtime

Policies/Gates protect resources/actions; route middleware can establish identity/coarse role but should not be the only object authorization.

For rolling deploys use expand/migrate/contract style schema changes when old and new app versions overlap. Delay destructive column/table cleanup until no running code references it.

Long-lived Octane/queue workers retain process memory. Avoid request-scoped/user state in global/singleton mutable objects and restart workers after code/config changes according to deployment policy.

# Network Infrastructure — Deep Reference

## Change safety classes
LOW: monitoring/read-only inventory.
STANDARD: additive records, isolated access-port changes with local recovery.
HIGH: gateways, default routes, trunks, management VLAN, firewall defaults, DHCP/DNS authority, VPN hub, controller adoption, WAN changes.

For HIGH changes: require current topology, backup/export, alternate management or automatic rollback, dependency/seam review, canary where possible and post-change real traffic validation.

## Evidence set
topology/address plan, route tables, ARP/ND, DHCP leases, DNS queries, controller/device health, firewall counters/logs, packet capture when ambiguity remains, latency/loss tests, config diff and rollback path.

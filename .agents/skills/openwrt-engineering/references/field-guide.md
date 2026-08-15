# OpenWrt Engineering — Deep Reference

## Current research baseline (2026-08-12)
UCI remains OpenWrt's central configuration interface and `/etc/config/` is the canonical configuration surface for supported packages. `ubus` is the system IPC/RPC bus used by core services; available objects/methods depend on installed packages/release. Some wiki pages explicitly warn older ubus/UCI details may be incomplete, so introspect the live device.

## Safe remote-change pattern
backup config → inspect `uci show` / relevant ubus objects → stage changes → validate syntax/topology → apply with rollback/confirm when supported → verify SSH/LuCI management → verify network/firewall/DNS/DHCP/wireless → persist evidence.

## Upgrade cautions
Record target, release, storage constraints, installed packages and preserved config before sysupgrade. Never automate broad fleet upgrades before one representative device succeeds.

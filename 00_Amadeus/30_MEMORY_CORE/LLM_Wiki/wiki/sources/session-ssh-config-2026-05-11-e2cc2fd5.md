---
source: backfilled 2026-06-06 (hygiene lint remediation)
date: 2026-05-11
type: source
domain: ingestion
title: SSH Configuration Sessions — Documentation
tags: [#source #sources #backfilled]
---

# SSH Configuration Sessions — Documentation

## Metadata
- **Session**: `e2cc2fd5-bd47-4d6d-aaa6-6356cd2a6a4b`
- **Date**: 2026-05-11
- **Size**: 1.5 MB
- **Title**: VPS Audit (srv941028)

## Key Decisions

1. **SSH hardening confirmed** — Pubkey-only authentication, no root login, fail2ban active
2. **Firewall `A0_Shield` rules** — SSH 22 restricted to IP `174.102.16.12` only
3. **0 auth failures in 24h** — fail2ban blocking brute force attempts

## SSH Configurations Made

### SSH Daemon Settings (from audit)
```bash
PubkeyAuthentication yes
PasswordAuthentication no
PermitRootLogin no
```

### Additional Config Files
- `/etc/ssh/sshd_config.d/50-cloud-init.conf`
- `/etc/ssh/sshd_config.d/60-cloudimg-settings.conf`

### Security Tools
- **fail2ban**: active, 0 failed auth attempts in 24h
- **Firewall**: SSH port 22 restricted to single IP `174.102.16.12`

## Problems Solved

| Problem | Solution |
|---------|----------|
| Password-based SSH vulnerable | Disabled `PasswordAuthentication`, enabled pubkey only |
| Root login risk | `PermitRootLogin no` |
| Brute force attacks | fail2ban active with 0 failures recorded |
| SSH exposed to world | Firewall restrict to single IP |

## VPS Audit Context

**Host**: srv941028 (148.230.92.235) — Hostinger KVM 2
**OS**: Ubuntu 24.04.4 LTS
**Uptime**: 12 days 18 hours

**SSH Posture Summary**:
- Pubkey only ✅
- No root login ✅
- fail2ban active ✅
- 0 failed auth (24h) ✅

## Other Findings (Related)

- **Firewall provider `A0_Shield`**: SSH 22 restricted to `174.102.16.12` only
- Port 3000 also restricted to same IP
- All other ports blocked at provider level (5900/5901/6080/5433/8000 etc not reachable from internet)
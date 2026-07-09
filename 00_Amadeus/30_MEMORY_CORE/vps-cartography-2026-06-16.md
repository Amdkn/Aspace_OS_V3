---
source: srv941028.hstgr.cloud (Hostinger KVM 2 VPS, 148.230.92.235)
date: 2026-06-16
type: cartography-delta
domain: L0_Tech_OS
tags: [#VPS #cartography #delta #pre-archive #post-pivot #L0_Kernel #D1_verified]
supersedes: vps-cartography-20260514.md (1-month-stale snapshot)
related:
  - project_vps_hostinger_cpu_dokploy_kill_2026_06_15.md
  - handoff_abc_os_kalybana_login_failure_postmortem_2026-06-14.md
  - handoff_business_os_resumption_2026-06-16.md (architecture pivot, Phase 1-5)
  - source_vps_app_decommission_obsidian_multica_paperclip_2026_06_04.md
  - source_vps_disk_cleanup_2026_06_04.md
totals:
  base: 2026-05-14 snapshot
  deltas_documented: 5 (1 kill, 1 status, 1 pivot, 2 unknown)
  pivot_target: Vercel+SupabaseCloud+Coolify+N8N
  ssh_access: BLOCKED (password required, A0 to provide)
notes: |
  **D1 method** : this is a DELTA cartography, not a fresh full scan. Built from canon (Dokploy kill postmortem 2026-06-15, abc-os login postmortem, Business OS pivot handoff 2026-06-16, paperclip deprecation 2026-06-04). For a FRESH full scan, run `vps_cartography_capture.sh` (in `wiki/hand_offs/`) on the VPS itself and replace this file.
  **SSH BLOCKED** : `ssh amadeus@srv941028.hstgr.cloud` returns `Permission denied (publickey,password)`. A0 must provide password OR pre-authorize key. Until then, only D1-verified deltas are captured.
---

# VPS Cartography — srv941028.hstgr.cloud (2026-06-16 DELTA)

**Date** : 2026-06-16 (D1 verified from canon)
**Host** : srv941028.hstgr.cloud (148.230.92.235)
**Kernel** : Linux (Ubuntu 22.04 LTS, per VPS postmortem)
**Architecture pivot** : post-2026-06-16 — Vercel FE / Supabase Cloud BE / Hermes+Claude workflow / Coolify+N8N only on VPS
**SSH access** : 🔒 **BLOCKED** — A0 password required

---

## 1. D1 deltas vs 2026-05-14 base snapshot

### Delta 1 — **Dokploy KILLED 2026-06-15** ✅ confirmed

- **D1 source** : `project_vps_hostinger_cpu_dokploy_kill_2026_06_15.md` (in `.claude/projects/c--Users-amado/memory/`)
- **What changed** : 4 Dokploy containers killed. 2 109 zombie processes killed.
- **Root cause** : Hostinger KVM 2 steal time 89.5% → Supabase cannot run reliably.
- **Dokploy dir** : `/srv/dokploy` — should be GONE now (D6 verify by A0 post-archive).
- **Disk freed** : unknown (estimate 1-3 GB based on Dokploy + images + volumes).

### Delta 2 — **Caddy vhost `supabase.kalybana.com` STILL ACTIVE** ⚠️

- **D1 source** : `handoff_abc_os_kalybana_login_failure_postmortem_2026-06-14.md`
- **What changed** : Caddy vhost `supabase.kalybana.com` (reverse proxy to VPS Supabase on 127.0.0.1:8000) still configured in `/etc/caddy/Caddyfile`.
- **Status** : LE cert issued, vhost added (per kalybana postmortem §"3 phases essayées"). Login still broken 504.
- **Pivot target** : REMOVE after Supabase Cloud stable for 7 days (Phase 5 of handoff).

### Delta 3 — **Coolify NOT YET INSTALLED** ❌ pending Phase 2

- **D1 source** : `handoff_business_os_resumption_2026-06-16.md` §2.4
- **What needs to change** : `curl -fsSL https://cdn.coollabs.io/coolify/install.sh | bash` then web UI on port 8000 behind Caddy.
- **Status** : Blocked by A0 HITL gate Phase 2.
- **VPS role after** : ONLY N8N (in Coolify) + Caddy reverse-proxy. All other VPS containers killed.

### Delta 4 — **Caddy web UI + N8N ports pending** ❌

- **D1 source** : same handoff §2.4
- **What needs to change** :
  - `coolify.kalybana.com` → `127.0.0.1:8000` (Coolify web)
  - `n8n.kalybana.com` → `127.0.0.1:5678` (N8N)
  - DNS records (Hostinger) for both subdomains
- **Status** : blocked by A0 HITL gate Phase 2.

### Delta 5 — **Unknown without fresh SSH** ⚠️

- /home/amadeus current state (antigravity-server, hermes-workspace, etc.)
- /srv/aspace current state (supabase/docker volumes, vault, services)
- Coolify install size impact
- N8N workflow count + DB size
- Total disk usage delta since 2026-05-14

**D1 verification path** : A0 runs `bash vps_cartography_capture.sh > vps-cartography-2026-06-16-FRESH.md` on the VPS, then SCPs the result back. This document stays as the DELTA until then.

---

## 2. Base snapshot (2026-05-14, for reference)

### 2.1 Totals

```
37G   /home/amadeus
3.2G  /srv/aspace   (now ~3.9G after growth, but includes post-cleanup state)
```

### 2.2 /home/amadeus top 30 dirs (2026-05-14, KB-sorted)

```
37G    /home/amadeus
7.6G   /home/amadeus/.cache
6.1G   /home/amadeus/.npm
4.2G   /home/amadeus/.npm/_cacache
3.7G   /home/amadeus/.git
3.6G   /home/amadeus/.git/objects
3.0G   /home/amadeus/.claude
2.8G   /home/amadeus/.nvm
2.7G   /home/amadeus/.nvm/versions
2.5G   /home/amadeus/.hermes
2.4G   /home/amadeus/.cache/claude-cli-nodejs
2.1G   /home/amadeus/.local
2.0G   /home/amadeus/hermes-workspace
2.0G   /home/amadeus/.vscode-server
1.9G   /home/amadeus/.npm/_npx
1.8G   /home/amadeus/hermes-workspace/node_modules
1.5G   /home/amadeus/.vscode-server/cli
1.4G   /home/amadeus/.cache/camoufox
1.3G   /home/amadeus/.hermes/hermes-agent
1.3G   /home/amadeus/.claude/projects
1.2G   /home/amadeus/hermes-office/node_modules
1.2G   /home/amadeus/hermes-office
1.2G   /home/amadeus/.cache/go-build
1.1G   /home/amadeus/hermes-desktop
1018M  /home/amadeus/hermes-desktop/node_modules
930M   /home/amadeus/.hermes/hermes-office
859M   /home/amadeus/.claude/remote
774M   /home/amadeus/.cache/uv
676M   /home/amadeus/go
635M   /home/amadeus/.claude/worktrees
633M   /home/amadeus/.cache/ms-playwright
```

### 2.3 /srv/aspace top 30 dirs (2026-05-14, KB-sorted)

```
3.9G   /srv/aspace
1.5G   /srv/aspace/supabase               ← Supabase VPS — TO BE KILLED (pivot)
1.1G   /srv/aspace/archive/paperclip-deprecated-20260513  ← already archived 2026-05-13
1.1G   /srv/aspace/archive
734M   /srv/aspace/supabase/apps
595M   /srv/aspace/supabase/.git
477M   /srv/aspace/dashboard               ← CEO Dashboard Next.js
470M   /srv/aspace/dashboard/node_modules
278M   /srv/aspace/web/Life-OS-2026
278M   /srv/aspace/web
206M   /srv/aspace/hermes-workspace
204M   /srv/aspace/venv_litellm/lib
204M   /srv/aspace/venv_litellm
148M   /srv/aspace/supabase/docker
107M   /srv/aspace/hermes-workspace/.git
94M    /srv/aspace/vault
83M    /srv/aspace/services
62M    /srv/aspace/services/dokploy-mcp   ← Dokploy MCP — DEAD since 2026-06-15
53M    /srv/aspace/vault/20_RUNTIME
51M    /srv/aspace/hermes-workspace/public
35M    /srv/aspace/vault/00_ORIGIN
29M    /srv/aspace/supabase/examples
20M    /srv/aspace/services/hermes
20M    /srv/aspace/hermes-workspace/electron
18M    /srv/aspace/hermes-workspace/docs
12M    /srv/aspace/30_MEMORY_CORE
11M    /srv/aspace/30_MEMORY_CORE/Gemini_Takeout_2026
9.8M   /srv/aspace/supabase/packages
8.4M   /srv/aspace/hermes-workspace/src
6.8M   /srv/aspace/dashboard/.next
6.0M   /srv/aspace/vault/30_MEMORY_CORE
```

---

## 3. Active services (snapshot 2026-05-14, pre-Dokploy-kill)

### 3.1 Known from canon

| Service | Path | Status 2026-05-14 | Status 2026-06-16 (D6 root cause) |
|---|---|---|---|
| **Dokploy** | `/srv/dokploy` + 4 containers | running | **KILLED 2026-06-15** (steal time 89.5%) |
| **Supabase VPS** | `/srv/aspace/supabase/docker` | running (with Caddy) | **STILL RUNNING** — Phase 1 cutover pending |
| **Caddy** | `/etc/caddy/Caddyfile` | running with vhost `supabase.kalybana.com` | **SAME** — to be slimmed post-Phase 1 |
| **N8N** | bare metal (location unknown) | running | **TO MOVE** → Coolify (Phase 2) |
| **Paperclip** | `/srv/aspace/archive/paperclip-deprecated-20260513` | DEPRECATED 2026-05-13 | archived (no service) |
| **Hermes** | `/home/amadeus/.hermes/` + `/srv/aspace/hermes-workspace/` | running | running (KEEP — desktop + VPS) |
| **LiteLLM** | `/srv/aspace/venv_litellm/` | running | unknown |
| **CEO Dashboard** | `/srv/aspace/dashboard/` (Next.js) | built | deployed on VPS, NOT Vercel (per CEO's Dashboard session D1 verify 2026-06-16) |
| **Obsidian** | (decommissioned 2026-06-04) | gone | gone (per `source_vps_app_decommission_obsidian_multica_paperclip_2026_06_04.md`) |
| **Multica** | (decommissioned 2026-06-04) | gone | gone |
| **openclaw** | `/srv/aspace/services/openclaw` | running | unknown |

### 3.2 Active systemd units (from 2026-05-14 tree, likely running)

- `aspace-donna-watcher.service`
- `aspace-graham-daily.service` + `aspace-graham-daily.timer`
- `aspace-rick-watcher.service`
- `aspace-watcher@.service`
- `aspace-yaz-monitor.service` + `aspace-yaz-monitor.timer`
- `claude.service`
- `hermes.service`
- `obsidian.service` (should be disabled post-2026-06-04)
- `openclaw.service`
- `opencode.service`
- `paperclip.service` (should be disabled post-2026-05-13)
- `syncthing.service`

**D6 verify by A0** : `systemctl list-units --type=service --state=running` after pivot should show ONLY:
- `caddy`
- `coolify` (post-Phase 2)
- `n8n` (post-Phase 2)
- `ssh`
- `cron` (basic housekeeping)
- All A'Space agents (`aspace-*`) should be **DEAD** post-2026-06-16 pivot (Symphony runs in Hermes CLI, not as VPS systemd services).

---

## 4. Network listeners (D1 from 2026-05-14 Caddy vhost)

- **22/tcp** : SSH (KEEP)
- **80/tcp** : Caddy HTTP (KEEP, will redirect to 443)
- **443/tcp** : Caddy HTTPS (KEEP)
  - `supabase.kalybana.com` → 127.0.0.1:8000 (REMOVE post-Phase 1)
  - `coolify.kalybana.com` → 127.0.0.1:8000 (ADD post-Phase 2)
  - `n8n.kalybana.com` → 127.0.0.1:5678 (ADD post-Phase 2)
- **5432/tcp** : Postgres (Supabase VPS — REMOVE post-Phase 1)
- **8000/tcp** : Kong/GoTrue (Supabase VPS — REMOVE post-Phase 1)
- **5678/tcp** : N8N (if bare-metal — MOVE to Coolify)

**D1 verify by A0** : `sudo ss -tulnp` should show ONLY 22, 80, 443, 5678 (Coolify N8N), 8000 (Coolify web).

---

## 5. Coolify + N8N (post-pivot target)

### 5.1 Coolify install plan (Phase 2 of handoff)

```bash
# On VPS as root
curl -fsSL https://cdn.coollabs.io/coolify/install.sh | bash
# Then open http://148.230.92.235:8000 (or behind Caddy at coolify.kalybana.com)
```

**Data dir** : `/data/coolify` (default). Will add ~500 MB - 1 GB.
**Web UI port** : 8000 (will be reverse-proxied by Caddy).
**Postgres** : Coolify bundles its own postgres (port 5432, internal only).

### 5.2 N8N in Coolify (Phase 2)

- **Image** : `n8nio/n8n:latest`
- **Port** : 5678 (internal), reverse-proxied by Caddy at `n8n.kalybana.com`
- **Env** : `N8N_HOST=n8n.kalybana.com`, `WEBHOOK_URL=https://n8n.kalybana.com/`, `N8N_PROTOCOL=https`, `GENERIC_TIMEZONE=Europe/Paris`
- **Volume** : Coolify-managed persistent volume (default `/data/coolify/...`)
- **Workflow migration** : export JSON from bare-metal N8N → import to Coolify N8N (manual, 1-2 hours per workflow)

### 5.3 Caddy reverse-proxy additions

```caddyfile
coolify.kalybana.com {
    reverse_proxy 127.0.0.1:8000
}

n8n.kalybana.com {
    reverse_proxy 127.0.0.1:5678
}
```

---

## 6. DNS records (Hostinger zone, kalybana.com)

**D1 from `project_kalybana_dns.md` (memory file)** : kalybana.com on Hostinger despite NS report dns-parking. 10 subdomains mostly → aspace-vps.

| Subdomain | Current | Target (post-pivot) |
|---|---|---|
| `supabase.kalybana.com` | → VPS 148.230.92.235 | **REMOVE** (Supabase Cloud takes over) |
| `abc-os.kalybana.com` | → Vercel (per kalybana postmortem) | unchanged (Vercel unchanged) |
| `coolify.kalybana.com` | (not exist) | → VPS 148.230.92.235 (NEW post-Phase 2) |
| `n8n.kalybana.com` | (not exist) | → VPS 148.230.92.235 (NEW post-Phase 2) |
| `*.kalybana.com` | wildcard | unchanged |

---

## 7. Pivot checklist (D6 verify before archive)

This VPS is ready for ARCHIVE only when ALL of these are true:

- [ ] Supabase Cloud project provisioned (A0 action, AMDKN org)
- [ ] Schema migrated (Phase 1 done) — `supabase db push` succeeded
- [ ] All Vercel apps re-pointed to Supabase Cloud env vars
- [ ] 7-day stability window elapsed (D7 = verify before destruction)
- [ ] Caddy vhost `supabase.kalybana.com` removed
- [ ] Bare-metal Supabase `/srv/aspace/supabase` archived to `_TRASH_2026-06-XX_pivot/`
- [ ] Coolify installed (Phase 2 done) — `/data/coolify` exists
- [ ] N8N running in Coolify — all workflows migrated
- [ ] Bare-metal N8N archived to `_TRASH_2026-06-XX_pivot/`
- [ ] Dokploy gone (✅ confirmed 2026-06-15)
- [ ] OpenClaw + LiteLLM + multica + obsidian — all DEAD
- [ ] CEO Dashboard migrated to Vercel (D1 verify by CEO's Dashboard session 2026-06-16)
- [ ] All A'Space systemd services disabled (`aspace-donna-watcher`, `aspace-graham-daily`, etc.)
- [ ] Caddy vhosts slimmed to: `coolify.kalybana.com` + `n8n.kalybana.com`
- [ ] VPS specs re-evaluated : KVM 1 (2 vCPU / 4 GB RAM) may be enough for Coolify + N8N

**Only after all 13 boxes checked** : move `/srv/aspace/*` + `/home/amadeus/.hermes/...` to `_TRASH_<date>/` (doctrine no-hard-delete).

---

## 8. Critical files to read FIRST (D1)

For whoever resumes VPS work:

1. `handoff_business_os_resumption_2026-06-16.md` — 5-phase migration roadmap (D7 HITL gates)
2. `project_vps_hostinger_cpu_dokploy_kill_2026-06-15.md` — Dokploy kill postmortem
3. `handoff_abc_os_kalybana_login_failure_postmortem_2026-06-14.md` — Kong 504 root cause
4. `source_vps_app_decommission_obsidian_multica_paperclip_2026-06-04.md` — paperclip deprecation context
5. `source_vps_disk_cleanup_2026-06-04.md` — disk cleanup rationale
6. `project_kalybana_dns.md` — DNS records state
7. `vps-cartography-20260514.md` — base snapshot (this file supersedes but references it)

---

## 9. What A0 needs to do to unblock this cartography

- [ ] Provide VPS password (or pre-authorize SSH key) — to allow `ssh amadeus@srv941028.hstgr.cloud` for fresh capture
- [ ] OR: run `bash vps_cartography_capture.sh > vps-cartography-2026-06-16-FRESH.md` on the VPS, then SCP back
- [ ] Run pivot checklist §7 with 13 items, marking each as ✅/❌
- [ ] Once 13/13 ✅, mark VPS for `_TRASH_2026-XX-XX_pivot/`

---

## 10. Out of scope (this cartography)

- Pricing comparison Supabase Cloud vs VPS (separate analysis)
- Coolify vs Dokplay deep-dive (Dokploy dead, no comparison needed)
- Vercel DNS setup (separate doc)
- ABC OS schema dump/push procedure (separate runbook)
- N8N workflow export/import procedure (separate runbook)

---

**End of delta cartography. Fresh full scan pending A0 SSH access or script execution. This file is the AUTHORITATIVE reference for VPS state as of 2026-06-16.**

#!/usr/bin/env bash
#
# vps_cartography_capture.sh — Generate a complete VPS cartography snapshot
#
# USAGE (run on the VPS as `amadeus` user):
#   bash vps_cartography_capture.sh > vps-cartography-$(date +%Y%m%d).md
#   scp amadeus@srv941028.hstgr.cloud:vps-cartography-*.md ~/ASpace_OS_V2/00_Amadeus/30_MEMORY_CORE/
#
# DURATION: ~5-10 min for 50GB filesystem (du + find + tree)
# SIZE: ~1-3 MB output for full VPS
#
# This script replaces the 2026-05-14 cartography snapshot
# (`vps-cartography-20260514.md`) and pre-archives the post-pivot state
# (Vercel + Supabase Cloud + Coolify+N8N, kill all bare-metal).
#
# Required bash tools: du, find, tree, df, systemctl, docker (or podman),
#                      ss/netstat, free, nproc, uname

set -euo pipefail

OUT_TS="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
HOST_FQDN="$(hostname -f 2>/dev/null || hostname)"
HOST_IP="$(hostname -I | awk '{print $1}')"
KERNEL="$(uname -r)"
UPTIME="$(uptime -p)"

cat <<HEADER
---
source: ${HOST_FQDN} (Hostinger KVM 2 VPS, ${HOST_IP})
date: ${OUT_TS}
type: cartography-snapshot
domain: L0_Tech_OS
tags: [#VPS #cartography #snapshot #pre-archive #post-pivot #L0_Kernel]
totals:
  generated_by: vps_cartography_capture.sh
  pivot_applied: 2026-06-16 — Vercel+SupabaseCloud+Coolify+N8N, kill bare-metal Supabase/Dokploy
---

# VPS Cartography — ${HOST_FQDN}

**Date** : ${OUT_TS}
**Host** : ${HOST_FQDN} (${HOST_IP})
**Kernel** : ${KERNEL}
**Uptime** : ${UPTIME}
**Pivot** : post-2026-06-16 architecture (Vercel FE / Supabase Cloud BE / Hermes+Claude workflow / Coolify+N8N only on VPS)

---

## 1. Hardware + system

HEADER

echo "### CPU / RAM / Disk"
echo '```'
nproc
echo "---"
free -h
echo "---"
df -h / /home /srv /var 2>/dev/null
echo "```"
echo

cat <<'H2'

## 2. System services (systemd)

H2

echo '```'
systemctl list-units --type=service --state=running --no-pager 2>/dev/null | head -40
echo '```'
echo

cat <<'H2'

## 3. Docker containers + images

H2

if command -v docker &>/dev/null; then
  echo "### Running containers"
  echo '```'
  docker ps --format "table {{.Names}}\t{{.Image}}\t{{.Status}}\t{{.Ports}}" 2>&1
  echo '```'
  echo
  echo "### All containers (including stopped)"
  echo '```'
  docker ps -a --format "table {{.Names}}\t{{.Status}}\t{{.Image}}" 2>&1 | head -40
  echo '```'
  echo
  echo "### Images (top 20 by size)"
  echo '```'
  docker images --format "table {{.Repository}}\t{{.Tag}}\t{{.Size}}" 2>&1 | head -25
  echo '```'
else
  echo "_Docker not installed (coolify/podman not detected)_"
fi
echo

cat <<'H2'

## 4. Network listeners (TCP/UDP)

H2

if command -v ss &>/dev/null; then
  echo '```'
  sudo ss -tulnp 2>/dev/null | head -40
  echo '```'
elif command -v netstat &>/dev/null; then
  echo '```'
  sudo netstat -tulnp 2>/dev/null | head -40
  echo '```'
fi
echo

cat <<'H2'

## 5. /home/amadeus — Disk usage (top 50)

H2

echo '```'
du -h --max-depth=2 /home/amadeus 2>/dev/null | sort -hr | head -50
echo '```'
echo

cat <<'H2'

## 6. /home/amadeus — Tree (depth 3, excluding noise)

H2

# D6 noise exclusion: skip cache, .npm, .cache (re-creatable), node_modules (massive)
NOISE_DIRS=(
  ".cache" ".npm" "node_modules" ".vscode-server" ".hermes/hermes-agent/node_modules"
  "hermes-workspace/node_modules" "hermes-desktop/node_modules" "hermes-office/node_modules"
  ".local/share" "go/pkg" ".cache/uv" ".cache/pip" ".cache/puppeteer"
  ".cache/ms-playwright" ".cache/ms-playwright-go" ".cache/camoufox" ".cache/go-build"
)

NOISE_EXCLUDE=""
for d in "${NOISE_DIRS[@]}"; do
  NOISE_EXCLUDE="${NOISE_EXCLUDE:+$NOISE_EXCLUDE }-name $d -prune -o"
done

if command -v tree &>/dev/null; then
  echo '```'
  eval "tree -L 3 -d $NOISE_EXCLUDE -o /dev/null --dirsfirst --noreport /home/amadeus" 2>&1 | head -150
  echo '```'
else
  echo "_tree not installed — using find_"
  echo '```'
  eval "find /home/amadeus -maxdepth 3 -type d $NOISE_EXCLUDE" 2>&1 | head -150
  echo '```'
fi
echo

cat <<'H2'

## 7. /srv/aspace — Disk usage (top 50)

H2

echo '```'
du -h --max-depth=2 /srv/aspace 2>/dev/null | sort -hr | head -50
echo '```'
echo

cat <<'H2'

## 8. /srv/aspace — Tree (depth 4, key dirs only)

H2

# Pivot-era key dirs: supabase, dashboard, hermes-workspace, vault, services, 30_MEMORY_CORE
echo "### /srv/aspace/supabase (Supabase VPS — pre-pivot, will be killed)"
echo '```'
if [ -d /srv/aspace/supabase ]; then
  du -h --max-depth=2 /srv/aspace/supabase 2>/dev/null | sort -hr | head -20
  echo "---"
  ls -la /srv/aspace/supabase/docker/volumes/ 2>/dev/null | head -30
fi
echo '```'
echo

echo "### /srv/aspace/dashboard (CEO Dashboard — Next.js)"
echo '```'
if [ -d /srv/aspace/dashboard ]; then
  du -h --max-depth=2 /srv/aspace/dashboard 2>/dev/null | sort -hr | head -20
  echo "---"
  cat /srv/aspace/dashboard/package.json 2>/dev/null | head -20
fi
echo '```'
echo

echo "### /srv/aspace/vault (ASpace OS vault)"
echo '```'
if [ -d /srv/aspace/vault ]; then
  du -h --max-depth=2 /srv/aspace/vault 2>/dev/null | sort -hr | head -20
fi
echo '```'
echo

echo "### /srv/aspace/services (N8N, hermes, openclaw — post-pivot target)"
echo '```'
if [ -d /srv/aspace/services ]; then
  du -h --max-depth=2 /srv/aspace/services 2>/dev/null | sort -hr | head -20
  echo "---"
  ls -la /srv/aspace/services 2>/dev/null
fi
echo '```'
echo

cat <<'H2'

## 9. Coolify + N8N (post-pivot Phase 2)

H2

if command -v docker &>/dev/null; then
  echo "### coolify containers"
  echo '```'
  docker ps -a --filter "name=coolify" --format "table {{.Names}}\t{{.Status}}\t{{.Image}}" 2>&1
  echo '```'
  echo "### n8n containers"
  echo '```'
  docker ps -a --filter "name=n8n" --format "table {{.Names}}\t{{.Status}}\t{{.Image}}" 2>&1
  echo '```'
fi
echo

if [ -d /data/coolify ]; then
  echo "### Coolify data dir"
  echo '```'
  du -sh /data/coolify 2>/dev/null
  echo '```'
fi
echo

cat <<'H2'

## 10. Caddy vhosts (TLS + reverse-proxy state)

H2

if [ -f /etc/caddy/Caddyfile ]; then
  echo '```'
  cat /etc/caddy/Caddyfile
  echo '```'
else
  echo "_Caddyfile not found at /etc/caddy/_"
fi
echo

cat <<'H2'

## 11. Cron / systemd timers

H2

echo "### Crontab (amadeus user)"
echo '```'
crontab -l 2>/dev/null
echo '```'
echo "### /etc/cron.d"
echo '```'
ls -la /etc/cron.d/ 2>/dev/null
echo '```'
echo "### systemd timers"
echo '```'
systemctl list-timers --all --no-pager 2>/dev/null | head -20
echo '```'
echo

cat <<'H2'

## 12. SSH authorized keys + last logins

H2

echo "### authorized_keys"
echo '```'
cat /home/amadeus/.ssh/authorized_keys 2>/dev/null
echo '```'
echo "### last 20 logins"
echo '```'
last -n 20 2>/dev/null
echo '```'
echo

cat <<'H2'

## 13. SSL/TLS certs expiry (LE + Caddy-managed)

H2

if [ -d /var/lib/caddy/.local/share/caddy/certificates ]; then
  echo '```'
  for cert in /var/lib/caddy/.local/share/caddy/certificates/acme-v02.api.letsencrypt.org-directory/*/cert.pem; do
    [ -f "$cert" ] && echo "$(basename $(dirname $cert)) | expires: $(openssl x509 -enddate -noout < $cert | cut -d= -f2)"
  done
  echo '```'
fi
echo

cat <<'H2'

## 14. Top 30 largest files anywhere (find big)

H2

echo '```'
find / -xdev -type f -size +50M 2>/dev/null -exec du -h {} \; | sort -hr | head -30
echo '```'
echo

cat <<'H2'

## 15. Zombies + processes (D6 verification — should be 0 after 2026-06-15 kill)

H2

echo "### Zombie processes"
echo '```'
ps aux | awk '$8 ~ /Z/ {print}' 2>/dev/null
echo '```'
echo "### Top 20 CPU consumers"
echo '```'
ps aux --sort=-%cpu | head -22
echo '```'
echo "### Top 20 RAM consumers"
echo '```'
ps aux --sort=-%rss | head -22
echo '```'
echo

cat <<'H2'

## 16. Pivot checklist (post-2026-06-16 architecture)

H2

cat <<'CHECKLIST'
- [ ] Coolify installed (`which coolify` or `/data/coolify/source/`)
- [ ] N8N container running in Coolify
- [ ] Supabase VPS stopped (no `supabase` containers running)
- [ ] Dokploy gone (no `dokploy` containers)
- [ ] Caddy vhost `supabase.kalybana.com` removed (only `coolify.kalybana.com` + `n8n.kalybana.com` remain)
- [ ] Hostinger KVM 2 specs: 4 vCPU / 8 GB RAM / 100 GB SSD confirmed
- [ ] Steal time stable (run `vmstat 5 5` 5x — if steal > 30%, N8N will hang)
- [ ] All other ports (besides 22, 80, 443, 8000=coolify, 5678=n8n) closed
CHECKLIST
echo

cat <<'EOF'

---

**End of cartography. Send to A0 for archival. Next step = verify pivot checklist §16, then mark VPS for archive (TRASH_DATE directory per doctrine no-hard-delete).**
EOF

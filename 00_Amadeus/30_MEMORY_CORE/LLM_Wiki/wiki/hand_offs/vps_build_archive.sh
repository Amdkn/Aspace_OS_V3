#!/bin/bash
# vps_build_archive.sh — Build canonical-source TGZ detached from SSH session.
# Uses setsid + nohup so the tar survives parent SSH exit.
# Writes status to /tmp/vps-build.log for poll-based verification.

set -e

LOG=/tmp/vps-build.log
OUT=/tmp/vps-archive.tgz
PIDFILE=/tmp/vps-build.pid

exec >> "$LOG" 2>&1
echo "=== build start $(date -u +%Y-%m-%dT%H:%M:%SZ) ==="

# Run tar fully detached so /compact killing SSH won't kill the build
setsid nohup bash -c "
  tar -czf $OUT \
    --exclude='node_modules' \
    --exclude='.git/objects' --exclude='.git/lfs' --exclude='.git/logs' \
    --exclude='.git/refs' --exclude='.git/hooks' --exclude='.git/info' \
    --exclude='dist' --exclude='build' --exclude='.next' --exclude='.nuxt' \
    --exclude='.cache' --exclude='.npm' --exclude='.nvm' \
    --exclude='venv_litellm' --exclude='paperclip-deprecated-20260513' \
    --exclude='__pycache__' --exclude='.pytest_cache' --exclude='.mypy_cache' \
    --exclude='.ruff_cache' --exclude='.ipynb_checkpoints' \
    --exclude='ms-playwright' --exclude='ms-playwright-go' \
    --exclude='.claude/projects' --exclude='.claude/file-history' \
    --exclude='.claude/worktrees' --exclude='.claude/plugins' \
    --exclude='.claude/remote' --exclude='.claude/backups' --exclude='.claude/session-data' \
    --exclude='_TRASH' --exclude='_ARCHIVE' \
    --exclude='go-build' --exclude='go/pkg' \
    --exclude='.cargo/registry' --exclude='site-packages' \
    /home/amadeus/.claude /home/amadeus/.hermes /home/amadeus/.config /home/amadeus/.ssh \
    /home/amadeus/agent-os /home/amadeus/50_SERVICES /home/amadeus/projects /home/amadeus/work \
    /srv/aspace/00_ORIGIN /srv/aspace/10_FORGE /srv/aspace/20_RUNTIME /srv/aspace/30_MEMORY_CORE \
    /srv/aspace/40_SKILLS /srv/aspace/90_SETUP /srv/aspace/dashboard /srv/aspace/hermes-workspace \
    /srv/aspace/main /srv/aspace/services /srv/aspace/supabase /srv/aspace/vault /srv/aspace/web \
    /etc/caddy /etc/systemd/system /var/lib/caddy/.local/share/caddy \
  && echo \"TAR_DONE \$(date -u +%Y-%m-%dT%H:%M:%SZ) size=\$(stat -c%s $OUT) bytes\" >> $LOG \
  && gzip -t $OUT && echo \"GZIP_OK \$(date -u +%Y-%m-%dT%H:%M:%SZ)\" >> $LOG \
  && md5sum $OUT >> $LOG \
  || echo \"BUILD_FAILED \$(date -u +%Y-%m-%dT%H:%M:%SZ) rc=\$?\" >> $LOG
" >/dev/null 2>&1 &

BUILD_PID=$!
echo $BUILD_PID > "$PIDFILE"
echo "spawned build pid=$BUILD_PID at $(date -u +%Y-%m-%dT%H:%M:%SZ)"

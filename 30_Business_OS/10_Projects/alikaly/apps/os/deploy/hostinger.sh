#!/usr/bin/env bash
# ============================================================================
# Alykaly OS — Hostinger Business deploy script
#
# Usage (executed on Hostinger SSH or locally with rsync target):
#   APP_ROOT=/home/uXXX/domains/kalybana.com/public_html/alykaly \
#   ./deploy/hostinger.sh
#
# Prereqs:
#   - Node 22 selected via hPanel Node.js Selector
#   - Application startup file = server.js
#   - Env vars set in hPanel (NEXT_PUBLIC_SUPABASE_URL, etc.)
# ============================================================================
set -euo pipefail

APP_ROOT="${APP_ROOT:?APP_ROOT env var required (Hostinger application root path)}"

echo "[1/6] Install deps (npm ci)..."
npm ci

echo "[2/6] Build Next.js standalone..."
npm run build

echo "[3/6] Verify standalone output..."
test -f .next/standalone/server.js || {
  echo "ERROR: .next/standalone/server.js missing — check next.config.ts output='standalone'"
  exit 1
}

echo "[4/6] Sync standalone to $APP_ROOT..."
rsync -av --delete \
  --exclude='.env.local' \
  --exclude='.next/cache' \
  .next/standalone/ "$APP_ROOT/"

echo "[5/6] Sync .next/static and public/..."
mkdir -p "$APP_ROOT/.next/static" "$APP_ROOT/public"
rsync -av --delete .next/static/ "$APP_ROOT/.next/static/"
rsync -av --delete public/ "$APP_ROOT/public/"

echo "[6/6] Done. Restart the Node.js app from hPanel:"
echo "      hPanel → Websites → alykaly.kalybana.com → Advanced → Node.js → Restart"
echo ""
echo "Health check after restart:"
echo "      curl https://alykaly.kalybana.com/api/engine/status"

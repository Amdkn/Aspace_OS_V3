#!/usr/bin/env bash
# bootstrap.sh — Initialiser OpenClaw Runtime depuis le Canon pour un nouvel environnement
# Usage : source .env && bash bootstrap.sh
# ADR : ADR-002 (Portabilité Multiverse)
set -euo pipefail

: "${ASPACE_ROOT:?Variable ASPACE_ROOT requise — copier .env.template en .env et remplir}"
: "${OPENCLAW_STATE_DIR:?Variable OPENCLAW_STATE_DIR requise}"
: "${OPENCLAW_BIN:?Variable OPENCLAW_BIN requise}"

echo "[bootstrap] ASPACE_ROOT=$ASPACE_ROOT"
echo "[bootstrap] OPENCLAW_STATE_DIR=$OPENCLAW_STATE_DIR"
echo "[bootstrap] OPENCLAW_BIN=$OPENCLAW_BIN"

# 1. Vérifier que le Canon git existe
if [ ! -d "$ASPACE_ROOT/00_Amadeus/01_Identity_Core/agents" ]; then
  echo "[bootstrap] ERROR: Canon agents non trouvé à $ASPACE_ROOT" >&2
  exit 1
fi

# 2. Créer la structure runtime si inexistante
mkdir -p \
  "$OPENCLAW_STATE_DIR/workspace/runtime_doctrine/agents" \
  "$OPENCLAW_STATE_DIR/workspace/memory" \
  "$OPENCLAW_STATE_DIR/cron"

# 3. Sync initial Canon → Runtime
echo "[bootstrap] Sync Canon agents → runtime_doctrine..."
SRC="$ASPACE_ROOT/00_Amadeus/01_Identity_Core/agents"
DST="$OPENCLAW_STATE_DIR/workspace/runtime_doctrine/agents"
rm -rf "$DST"
mkdir -p "$DST"
( cd "$SRC" && tar -cf - . ) | ( cd "$DST" && tar -xf - )

COUNT=$(find "$DST" -name "*.md" | wc -l)
echo "[bootstrap] OK — $COUNT fichiers agents synchronisés"

# 4. Copier la config Amadeus si openclaw.json n'existe pas encore
if [ ! -f "$OPENCLAW_STATE_DIR/openclaw.json" ]; then
  echo "[bootstrap] Copie openclaw.json vers $OPENCLAW_STATE_DIR/..."
  cp "$ASPACE_ROOT/00_Amadeus/03_OpenClaw_Body/openclaw.json" \
     "$OPENCLAW_STATE_DIR/openclaw.json"
  echo "[bootstrap] openclaw.json copié"
else
  echo "[bootstrap] openclaw.json déjà présent — skip"
fi

echo "[bootstrap] Bootstrap terminé. Lancer OpenClaw depuis: $OPENCLAW_BIN"

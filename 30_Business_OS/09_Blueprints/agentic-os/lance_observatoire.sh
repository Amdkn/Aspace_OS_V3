#!/usr/bin/env bash
D="/mnt/c/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/agentic-os"
cd "/mnt/c/Users/amado/agent-os/observatoire" || exit 1
. "$HOME/.minimax_env" || { echo "ARRET : ~/.minimax_env absent." >&2; exit 1; }
case "$ANTHROPIC_BASE_URL" in *minimax*) : ;; *) echo "ARRET : base non MiniMax." >&2; exit 1 ;; esac
mkdir -p "$D/logs"
cat "$D/BRIEF_OBSERVATOIRE_V3.md" | timeout 21600 claude -p --effort max \
  --permission-mode bypassPermissions > "$D/logs/observatoire_v3.log" 2>&1
echo "[code de sortie: $?]" >> "$D/logs/observatoire_v3.log"

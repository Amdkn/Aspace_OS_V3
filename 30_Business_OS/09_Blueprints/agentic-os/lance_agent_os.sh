#!/usr/bin/env bash
D="/mnt/c/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/agentic-os"
mkdir -p /mnt/c/Users/amado/agent-os/desktop
cd /mnt/c/Users/amado/agent-os/desktop || exit 1
. "$HOME/.minimax_env" || { echo "ARRET : ~/.minimax_env absent." >&2; exit 1; }
case "$ANTHROPIC_BASE_URL" in *minimax*) : ;; *) echo "ARRET : base non MiniMax." >&2; exit 1 ;; esac
mkdir -p "$D/logs"
# Construction d'une app neuve : delai le plus large de tous les chantiers.
cat "$D/BRIEF_AGENT_OS_V3.md" | timeout 28800 claude -p --effort max \
  --permission-mode bypassPermissions > "$D/logs/agent_os_v3.log" 2>&1
echo "[code de sortie: $?]" >> "$D/logs/agent_os_v3.log"

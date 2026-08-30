#!/usr/bin/env bash
BP="/mnt/c/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/coach-os-refonte"
cd "/mnt/c/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/30_Business_OS/10_Projects/omk/repos/coach-os" || exit 1
. "$HOME/.minimax_env" || { echo "ARRET : ~/.minimax_env absent." >&2; exit 1; }
case "$ANTHROPIC_BASE_URL" in *minimax*) : ;; *) echo "ARRET : base non MiniMax." >&2; exit 1 ;; esac
mkdir -p "$BP/logs" "$BP/qa"
for G in A B C D; do
  mkdir -p "$BP/qa/$G"
  (
    cat "$BP/BRIEF_QA_$G.md" | timeout 14400 claude -p --effort max \
      --permission-mode bypassPermissions > "$BP/logs/qa_$G.log" 2>&1
    echo "[code de sortie: $?]" >> "$BP/logs/qa_$G.log"
  ) &
done
wait

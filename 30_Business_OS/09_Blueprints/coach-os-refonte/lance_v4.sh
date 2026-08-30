#!/usr/bin/env bash
# Vague 4 : themes des pages de detail (2 groupes disjoints), Legal, Welcome.
# Perimetres exclusifs par agent, donc pas de conflit de fichiers.
BP="/mnt/c/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/coach-os-refonte"
REPO="/mnt/c/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/30_Business_OS/10_Projects/omk/repos/coach-os"
cd "$REPO" || exit 1
# Shell non interactif : ~/.profile n'est pas lu. Sans cette ligne, les requetes
# partent chez Anthropic et reviennent en « issue with the selected model ».
. "$HOME/.minimax_env" || { echo "ARRET : ~/.minimax_env absent." >&2; exit 1; }
case "$ANTHROPIC_BASE_URL" in *minimax*) : ;; *) echo "ARRET : base non MiniMax." >&2; exit 1 ;; esac
mkdir -p "$BP/logs"
for V in THEME_A THEME_B LEGAL WELCOME; do
  (
    cat "$BP/BRIEF_V4_$V.md" | timeout 14400 claude -p --effort max \
      --permission-mode bypassPermissions > "$BP/logs/v4_$V.log" 2>&1
    echo "[code de sortie: $?]" >> "$BP/logs/v4_$V.log"
  ) &
done
wait

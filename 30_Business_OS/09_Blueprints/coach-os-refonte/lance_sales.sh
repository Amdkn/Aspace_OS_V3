#!/usr/bin/env bash
# Sales OS — boucle constructeur / critique, un seul agent qui tient les deux
# roles a tour de role. Le critique dispose de tools/shot.mjs : sans yeux, il
# jugerait le JSX et approuverait tout.
BP="/mnt/c/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/coach-os-refonte"
REPO="/mnt/c/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/30_Business_OS/10_Projects/omk/repos/coach-os"
cd "$REPO" || exit 1
# Shell non interactif : ~/.profile n'est pas lu, il faut sourcer soi-meme.
. "$HOME/.minimax_env" || { echo "ARRET : ~/.minimax_env absent." >&2; exit 1; }
case "$ANTHROPIC_BASE_URL" in *minimax*) : ;; *) echo "ARRET : base non MiniMax." >&2; exit 1 ;; esac
mkdir -p "$BP/logs"
cat "$BP/BRIEF_SALES_OS.md" | timeout 10800 claude -p --effort max \
  --permission-mode bypassPermissions > "$BP/logs/sales_os.log" 2>&1
echo "[code de sortie: $?]" >> "$BP/logs/sales_os.log"

#!/usr/bin/env bash
# Reprise des deux briefs jamais lances, reperes par l'observatoire le
# 2026-08-06 : `audit` (5 grilles vides sur 6) et `tasks` (3 sections absentes).
#
# Ils touchent src/apps/audit et src/apps/tasks : aucun recouvrement avec les
# trois vagues Dashboard en cours, ils peuvent tourner en parallele.
BP="/mnt/c/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/coach-os-refonte"
REPO="/mnt/c/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/30_Business_OS/10_Projects/omk/repos/coach-os"
cd "$REPO" || exit 1

# `setsid nohup bash script.sh` n'est pas un shell de connexion : ni ~/.profile
# ni ~/.bashrc ne sont lus. Sans cette ligne, les requetes partent chez Anthropic
# et reviennent en « issue with the selected model », qui designe le mauvais
# coupable. Trois lancements perdus le 2026-08-06.
. "$HOME/.minimax_env" || { echo "ARRET : ~/.minimax_env absent." >&2; exit 1; }
case "$ANTHROPIC_BASE_URL" in
  *minimax*) : ;;
  *) echo "ARRET : la base n'est pas MiniMax." >&2; exit 1 ;;
esac

mkdir -p "$BP/logs"
for A in audit tasks; do
  (
    cat "$BP/BRIEF_APP_$A.md" | timeout 7200 claude -p --effort max \
      --permission-mode bypassPermissions > "$BP/logs/app_$A.log" 2>&1
    # Marqueur de fin : c'est la seule preuve que l'observatoire accepte.
    echo "[code de sortie: $?]" >> "$BP/logs/app_$A.log"
  ) &
done
wait

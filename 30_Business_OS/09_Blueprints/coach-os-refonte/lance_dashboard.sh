#!/usr/bin/env bash
# Lance les trois vagues du chantier Dashboard en parallele.
#
# Cloisonnement : V1 possede DashboardApp.tsx, V2 ecrit dans dashboard/security/,
# V3 dans dashboard/platform/. Le raccordement des sections de V2 et V3 dans
# DashboardApp.tsx est fait apres, par l'orchestrateur — pas par les agents.
REPO="/mnt/c/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/30_Business_OS/10_Projects/omk/repos/coach-os"
BP="/mnt/c/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/coach-os-refonte"
cd "$REPO" || exit 1

# Ce script est lance par `setsid nohup bash`, qui n'est PAS un shell de
# connexion : ni `~/.profile` ni `~/.bashrc` ne sont lus, donc aucune variable
# MiniMax n'est heritee. `claude` repart alors sur les valeurs par defaut
# d'Anthropic, ou le modele MiniMax n'existe effectivement pas — d'ou le message
# trompeur « issue with the selected model » qui a coute trois lancements.
# Le shell interactif marchait pour cette seule raison. On exporte donc ici.
. "$HOME/.minimax_env" || { echo "ARRET : ~/.minimax_env absent." >&2; exit 1; }
case "$ANTHROPIC_BASE_URL" in
  *minimax*) : ;;
  *) echo "ARRET : la base n'est pas MiniMax [$ANTHROPIC_BASE_URL]." >&2; exit 1 ;;
esac

for V in V1 V2 V3; do
  (
    # timeout : un agent qui n'a pas rendu en 2 h est bloque, pas lent. Sans
    # borne, un fils qui n'ecrit jamais son code de sortie fige l'attente finale
    # — 4 h 15 perdues le 2026-08-05 pour un travail deja termine.
    cat "$BP/BRIEF_DASHBOARD_$V.md" | timeout 7200 claude -p --effort max \
      --permission-mode bypassPermissions > "$BP/sortie_dashboard_$V.log" 2>&1
    echo "[code de sortie: $?]" >> "$BP/sortie_dashboard_$V.log"
  ) &
done
wait
echo "les trois vagues sont rendues" >> "$BP/sortie_dashboard_V1.log"

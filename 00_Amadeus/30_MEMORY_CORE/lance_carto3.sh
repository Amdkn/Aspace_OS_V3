#!/bin/bash
# Vague 3 de la cartographie du PARA de V2.
#
# NE PAS LANCER AVEC `&`. Ce script part en tache de fond par l'outil, pas par le
# shell : un `bash lance_carto3.sh &` dans un appel deja backgrounde fait sortir
# le parent, qui emporte son groupe de processus. Constate le 2026-08-13 — un
# agent demarre puis tue, trois jamais nes, et un `exit 0` pour couronner.
set -u

D="C:/Users/amado/ASpace_OS_V3/00_Amadeus/30_MEMORY_CORE"
export ANTHROPIC_BASE_URL="https://api.minimax.io/anthropic"
export ANTHROPIC_API_KEY="$(python -c "import json;print(json.load(open('C:/Users/amado/.claude/settings.json',encoding='utf-8'))['env']['ANTHROPIC_API_KEY'])")"
export ANTHROPIC_MODEL="MiniMax-M3[1m]"
export ANTHROPIC_SMALL_FAST_MODEL="MiniMax-M3[1m]"
cd "$D" || exit 1

for SEAU in 02_Areas_Spock 01_Projects_Picard 04_Archives_Data 03_Resources_Geordi; do
  n=$(tasklist 2>/dev/null | grep -c node)
  if [ "$n" -ge 45 ]; then
    echo "[$(date '+%H:%M:%S')] $n node — REFUSE $SEAU v3" >> journal_carto.log
    continue
  fi
  {
    printf '# TON SEAU : %s — VAGUE 3\n\n' "$SEAU"
    printf 'Les vagues 1 et 2 ont couvert **20,5 pour cent** des chemins. Tu reprends sur le RESTE.\n\n'
    printf '**Lis dabord `carto/%s.json` et `carto/%s_v2.json`** : tout chemin qui y figure\n' "$SEAU" "$SEAU"
    printf 'dans `types[].chemins` ou `relations[].chemin` est DEJA LU. Ne le relis pas.\n\n'
    printf 'Quota : **au moins 150 chemins non deja lus**. Si tu ne peux pas, dis pourquoi.\n\n'
    printf 'Sorties, a ne pas ecraser : `carto/%s_v3.md` et `carto/%s_v3.json`.\n' "$SEAU" "$SEAU"
    printf 'Meme format JSON que les vagues precedentes.\n\n'
    printf 'Le champ `fichiers_lus` etait FAUX sur deux seaux en vague 2 : zero declare alors que\n'
    printf 'des dizaines de relations avec chemins avaient ete produites. **Compte honnetement** —\n'
    printf 'un compteur faux vaut moins que pas de compteur.\n\n---\n\n'
    cat BRIEF_CARTO_PARA.md
  } | /c/Users/amado/AppData/Roaming/npm/claude -p --permission-mode bypassPermissions \
      > "journal_carto3_$SEAU.log" 2>&1 &
  echo "[$(date '+%H:%M:%S')] $SEAU vague 3 lancee (pid $!)" >> journal_carto.log
  sleep 180
done

wait
echo "[$(date '+%H:%M:%S')] vague 3 terminee" >> journal_carto.log

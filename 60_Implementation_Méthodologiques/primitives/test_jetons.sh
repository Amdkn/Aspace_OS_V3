#!/usr/bin/env bash
# Tests du verrou a jetons. Chaque test reproduit un defaut REEL avant de
# verifier qu'il ne se produit plus.
#
# Un verrou qu'on remet a une autre session sans l'avoir teste est une
# promesse, pas une primitive.

set -u
export JETONS_DIR="C:/Users/amado/AppData/Local/Temp/test_jetons_$$"
export JETONS_MAX=3
export JETONS_TTL_MIN=1
export JETONS_BATTEMENT_S=5

. "$(dirname "$0")/jetons.sh"

ok=0; ko=0
verdict() { # <attendu> <obtenu> <libelle>
  if [ "$1" = "$2" ]; then ok=$((ok+1)); printf "  OK    %s\n" "$3"
  else ko=$((ko+1)); printf "  ECHEC %s  (attendu=%s obtenu=%s)\n" "$3" "$1" "$2"; fi
}

echo "=== 1. atomicite : N tentatives simultanees, un seul gagnant ==="
rm -rf "$JETONS_DIR"; mkdir -p "$JETONS_DIR"
for i in $(seq 1 25); do ( mkdir "$JETONS_DIR/jeton_1" 2>/dev/null && echo x >> "$JETONS_DIR/g" ) & done; wait
verdict 1 "$(wc -l < "$JETONS_DIR/g" 2>/dev/null | tr -d ' ')" "un seul mkdir gagne sur 25"

echo
echo "=== 2. LE DEFAUT CORRIGE : un jeton qui BAT n'est pas vole ==="
rm -rf "$JETONS_DIR"; mkdir -p "$JETONS_DIR"
j=$(jetons_prendre "agent_long")
( while [ -d "$j" ]; do touch "$j" 2>/dev/null; sleep 2; done ) & bat=$!
sleep 4                       # TTL=1 min : sans battement il serait perime
_jetons_balayer
present=$([ -d "$j" ] && echo oui || echo non)
kill "$bat" 2>/dev/null
verdict oui "$present" "le jeton d'un agent vivant survit au balayage"

echo
echo "=== 3. un jeton SANS battement est bien recupere ==="
rm -rf "$JETONS_DIR"; mkdir -p "$JETONS_DIR"
j=$(jetons_prendre "agent_mort")
python -c "
import os,time
t=time.time()-600
os.utime(r'$j',(t,t))" 2>/dev/null
_jetons_balayer
verdict non "$([ -d "$j" ] && echo oui || echo non)" "le jeton d'un agent mort est libere"

echo
echo "=== 4. LE DEFAUT CORRIGE : une lecture d'etat ne mute rien ==="
rm -rf "$JETONS_DIR"; mkdir -p "$JETONS_DIR"
j=$(jetons_prendre "agent_vieux")
python -c "
import os,time
t=time.time()-600
os.utime(r'$j',(t,t))" 2>/dev/null
jetons_etat > /dev/null; jetons_libres > /dev/null; jetons_pris > /dev/null
verdict oui "$([ -d "$j" ] && echo oui || echo non)" "jetons_etat/libres/pris ne suppriment aucun jeton"

echo
echo "=== 5. le plafond tient sous concurrence ==="
rm -rf "$JETONS_DIR"; mkdir -p "$JETONS_DIR"
for i in $(seq 1 10); do ( jetons_prendre "c$i" > /dev/null 2>&1 ) & done; wait
verdict "$JETONS_MAX" "$(jetons_pris | tr -d ' ')" "jamais plus de $JETONS_MAX jetons pris sur 10 tentatives"

echo
echo "=== 6. jetons_avec rend le jeton, et propage le code de sortie ==="
rm -rf "$JETONS_DIR"; mkdir -p "$JETONS_DIR"
jetons_avec "tache_ok" true;  code_ok=$?
jetons_avec "tache_ko" false; code_ko=$?
verdict 0 "$code_ok" "code de sortie 0 propage"
verdict 1 "$code_ko" "code de sortie 1 propage"
verdict 0 "$(jetons_pris | tr -d ' ')" "aucun jeton ne fuit apres jetons_avec"

echo
echo "=== 7. jetons_avec libere meme si la commande est tuee ==="
rm -rf "$JETONS_DIR"; mkdir -p "$JETONS_DIR"
( jetons_avec "tache_tuee" sleep 30 ) & pid=$!
sleep 3; kill "$pid" 2>/dev/null; sleep 2
verdict 0 "$(jetons_pris | tr -d ' ')" "le jeton est rendu apres interruption"

rm -rf "$JETONS_DIR"
echo
echo "-------------------------------------------"
echo "  $ok reussis, $ko echoues"
[ "$ko" = "0" ] || exit 1

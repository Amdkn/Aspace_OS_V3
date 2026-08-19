#!/usr/bin/env bash
# Statut instantane de la boucle. Ne bloque JAMAIS.
#
# POURQUOI CE SCRIPT EXISTE
# La premiere surveillance attendait la fin de trois tours — 25 minutes sans
# un mot. Une boucle qu'on ne peut pas interroger sans attendre n'inspire
# aucune confiance, et l'utilisateur avait raison de le dire.
#
# Celui-ci rend en une seconde, meme quand tout tourne. « R.A.S. » est une
# reponse valide et utile ; le silence ne l'est pas.

set -u
L="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# Racine du depot : _loop -> 60_Implementation_Methodologiques -> ASpace_OS_V3
V3="$(cd "$L/../.." && pwd)"
METHO="$(cd "$L/.." && pwd)"

echo "=== BOUCLE ==="
if [ ! -f "$L/BOUCLE.log" ]; then
  echo "  journal absent — la boucle n'a jamais demarre"
  exit 0
fi

demarrage=$(head -1 "$L/BOUCLE.log")
dernier=$(tail -1 "$L/BOUCLE.log")
tours=$(grep -c "^\[.*\] tour " "$L/BOUCLE.log")
finis=$(grep -c "termine (exit=0)" "$L/BOUCLE.log")
echecs=$(grep -c "termine (exit=[1-9]" "$L/BOUCLE.log")

echo "  $demarrage"
echo "  dernier evenement : $dernier"
echo "  tours ouverts : $tours | agents rendus : $finis | echecs : $echecs"

if grep -q "boucle terminee" "$L/BOUCLE.log"; then
  echo "  ETAT : ARRETEE"
elif [ -f "$L/STOP" ]; then
  echo "  ETAT : STOP depose — arret au prochain tour"
else
  echo "  ETAT : EN COURS"
fi

echo
echo "=== AGENTS EN VOL ==="
# Un agent en vol = un journal de tour ouvert mais pas encore ferme.
envol=0
for f in "$L"/journal_*_t*.log; do
  [ -e "$f" ] || continue
  base=$(basename "$f" .log)
  quoi=${base#journal_}; quoi=${quoi%_t*}
  tour=${base##*_t}
  if ! grep -q "$quoi tour $tour termine" "$L/BOUCLE.log" 2>/dev/null; then
    taille=$(wc -c < "$f" 2>/dev/null || echo 0)
    echo "  EN VOL  $quoi (tour $tour) — journal $taille octets"
    envol=$((envol + 1))
  fi
done
[ "$envol" -eq 0 ] && echo "  aucun agent en vol"
echo "  node.exe : $(ps -W 2>/dev/null | grep -c node.exe) / plafond 40"

echo
echo "=== PRODUCTION ==="
for e in b1 b2 b3; do
  n=$(ls -1 "$V3/70_Onthologies/pulse/$e"/*.md 2>/dev/null | wc -l)
  printf "  pulse/%-3s %3s concepts\n" "$e" "$n"
done
printf "  %-9s %3s concepts\n" "protocoles" "$(ls -1 "$METHO/protocoles"/*.md 2>/dev/null | wc -l)"

echo
echo "=== MEMOIRE PARTAGEE (dernieres lignes d'ETAT.md) ==="
grep "^- \[tour" "$V3/70_Onthologies/pulse/ETAT.md" 2>/dev/null | tail -4 | cut -c1-160

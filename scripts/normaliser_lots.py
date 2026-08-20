"""Normalise LOTS_REVUE.txt : separateurs POSIX et saut de ligne final.

DEUX DEFAUTS QUI SE PAIENT EN SILENCE
1. Un fichier ecrit par `"\n".join(...)` n'a pas de saut de ligne final.
   La boucle `while read` de bash lit bien la derniere ligne mais sort
   aussitot : le dernier lot est saute sans qu'aucun message ne le dise.
2. `os.path.join` rend des antislashs sous Windows. Passes a bash, ils
   sont des caracteres d'echappement, pas des separateurs de chemin.
"""

import io
import os

CHEMIN = os.path.join(
    r"C:\Users\amado\ASpace_OS_V3",
    "60_Implementation_Méthodologiques", "_loop", "LOTS_REVUE.txt",
)

texte = io.open(CHEMIN, encoding="utf-8").read()
lignes = [l.replace("\\", "/").strip() for l in texte.splitlines() if l.strip()]
io.open(CHEMIN, "w", encoding="utf-8", newline="\n").write("\n".join(lignes) + "\n")

total = sum(int(l.rsplit("|", 1)[1]) for l in lignes)
print(f"{len(lignes)} lots, {total} concepts, separateurs normalises, saut final ajoute")

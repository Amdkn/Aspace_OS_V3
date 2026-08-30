#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Ce script mesure-t-il ce qu'il pretend ?

POURQUOI IL EXISTE
    P4 est le defaut le plus recurrent du poste : l'instrument qui ment. Neuf
    occurrences distinctes recensees, toutes payees. Ce script porte la liste
    et la confronte au code plutot qu'a la memoire.

LA REGLE
    Quand la mesure contredit l'observation directe, on repare l'instrument.
    Jamais on n'ajuste le chiffre.

CE QU'IL N'EST PAS
    Ce n'est pas un lint. Il ne dit pas « ce code est mauvais » : il dit
    « ce motif a deja menti ici, va verifier ». Le verdict reste humain.
"""

from __future__ import annotations
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# Chaque entree est un defaut REEL, date, avec ce qu'il a coute.
# (motif, titre, ce qu'il faut verifier)
PIEGES: list[tuple[str, str, str]] = [
    (r"os\.path\.islink|\.isSymbolicLink\(\)",
     "detection de lien",
     "islink() ne voit PAS les jonctions NTFS. Utiliser "
     "st_file_attributes & FILE_ATTRIBUTE_REPARSE_POINT (0x400)."),

    (r"\.isDirectory\(\)",
     "isDirectory sur lien",
     "rend FALSE pour un lien symbolique vers un dossier. 2 skills sur 6 "
     "avaient disparu du tableau. Croiser avec statSync(p).isDirectory()."),

    (r"rglob|\.walk\(|readdirSync.*recursive",
     "parcours recursif",
     "sans garde de jonction, un parcours suit le lien et recompte la cible : "
     "13,8 M fichiers mesures la ou il y en avait 14 613."),

    (r"sum\(|\.reduce\(|reduce\(\(",
     "total additionne",
     "ces valeurs s'additionnent-elles VRAIMENT ? Le cout de demarrage n'est "
     "pas la somme de tout ce qui est atteignable : ~20 724 annonces contre "
     "~5 819 reels. Un total gonfle pousse a couper ce qu'il faut garder."),

    (r"\.lower\(\)(?!.*normalize)",
     "casse sans accents",
     "lower() ne retire pas les accents. Des motifs non accentues face a un "
     "texte accentue rendaient « introuvable » sur du present. "
     "unicodedata.normalize('NFKD', ...) des DEUX cotes."),

    (r"print\(|console\.log",
     "sortie console",
     "la console Windows est en cp1252 et leve sur « → » ou « × ». Un script "
     "qui meurt en affichant a mesure juste et n'a rien rendu. "
     "sys.stdout.reconfigure(encoding='utf-8', errors='replace')."),

    (r"exit\s*0|returncode\s*==\s*0|rc\s*==\s*0",
     "confiance au code de retour",
     "un exit 0 ne prouve rien. Regarder la sortie reelle : le fichier, "
     "l'ecran, le port. Des scripts ont annonce un succes apres l'echec."),

    (r"set -e|shell=True|subprocess\.run",
     "sous-processus",
     "sans arret sur erreur, la suite s'execute sur un echec silencieux. "
     "Verifier aussi que le pkill a PRIS : deux boucles concurrentes ont "
     "brule quatre tranches en double."),
]


def auditer(chemin: Path) -> int:
    try:
        src = chemin.read_text(encoding="utf-8", errors="ignore")
    except OSError as e:
        print(f"  illisible : {e}")
        return 2

    lignes = src.split("\n")
    touches = []
    for motif, titre, quoi in PIEGES:
        ou = [i + 1 for i, L in enumerate(lignes)
              if re.search(motif, L) and not L.strip().startswith(("#", "//", "*"))]
        if ou:
            touches.append((titre, quoi, ou))

    print(f"  {chemin.name} — {len(lignes)} lignes\n")
    if not touches:
        print("  Aucun motif connu. Cela ne veut pas dire que la mesure est")
        print("  juste : croiser avec une seconde methode reste la seule preuve.")
        return 0

    for titre, quoi, ou in touches:
        apercu = ", ".join(f"l.{n}" for n in ou[:6])
        if len(ou) > 6:
            apercu += f" (+{len(ou) - 6})"
        print(f"  ── {titre}  [{apercu}]")
        for L in quoi.split(". "):
            if L.strip():
                print(f"     {L.strip().rstrip('.')}.")
        print()

    print(f"  {len(touches)} motif(s) a verifier.")
    print("  Ce ne sont pas des erreurs : ce sont des endroits ou un")
    print("  instrument a DEJA menti sur ce poste. Aller regarder.")
    return 1


def auto_test() -> int:
    """L'auditeur s'audite. S'il ne se detecte pas, il est disqualifie."""
    moi = Path(__file__)
    print("  Auto-audit : l'instrument se mesure lui-meme.\n")
    src = moi.read_text(encoding="utf-8")
    lignes = src.split("\n")

    trouves = sum(
        1 for motif, _, _ in PIEGES
        if any(re.search(motif, L) and not L.strip().startswith("#") for L in lignes)
    )

    print(f"  {len(PIEGES)} pieges connus, {trouves} detectes dans mon propre code.")
    if trouves == 0:
        print("\n  ECHEC : je contiens des print() et des sum(), donc au moins")
        print("  deux motifs devraient remonter. N'en trouver aucun prouve que")
        print("  je ne vois pas ce que je pretends chercher.")
        return 1

    print("\n  OK : l'auditeur se detecte lui-meme.")
    print("  Rappel : detecter un motif n'est pas un verdict. La seule preuve")
    print("  d'une mesure reste une seconde methode independante qui concorde.")
    return 0


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print(__doc__)
        print("  usage : auditer.py <script>  |  auditer.py --auto-test")
        return 2
    if argv[1] == "--auto-test":
        return auto_test()
    return auditer(Path(argv[1]))


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

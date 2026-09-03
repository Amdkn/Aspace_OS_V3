#!/usr/bin/env python3
# -*- coding: ascii -*-
"""Generateur CLI de franchises PrimeAgent v0.

Role : construit l'arborescence complete d'une franchise a partir d'un nom,
sur les 8 domaines B2 (SDD-006).
Spec : 00_Amadeus/60_Tape_Specs/2026-09-04-spec-primeagent-v0.md

Usage :
    python agent-template.py <nom_franchise> <repertoire_cible>

Sans les 2 arguments ou avec -h/--help : usage sur stdout, rc=2.
Le prototype derive du modele source, jamais l'inverse (invariant README).
"""

import sys
import os
import json
import re
from datetime import datetime

DOMAINES = ["growth", "sales", "product", "ops", "it",
            "finance", "people", "legal"]

DOSSIERS = ["01_Growth", "02_Sales", "03_Product", "04_Ops",
            "05_IT", "06_Finance", "07_People", "08_Legal"]


def usage():
    print("Usage : python agent-template.py <nom_franchise> <repertoire_cible>")
    print("  <nom_franchise>     : chaine non vide, sans separateur de chemin.")
    print("  <repertoire_cible>  : dossier de sortie (cree si absent).")
    print("Domaines generes : " + ", ".join(DOMAINES))
    return 2


def main(argv):
    if len(argv) == 1 or argv[1] in ("-h", "--help"):
        return usage()
    if len(argv) != 3:
        return usage()

    nom = argv[1]
    cible = argv[2]

    if not nom or not nom.strip():
        print("ERREUR: nom de franchise vide", file=sys.stderr)
        return 1
    if re.search(r"[\\/]", nom) or nom in (".", ".."):
        print("ERREUR: le nom de franchise ne doit pas contenir de separateur de chemin",
              file=sys.stderr)
        return 1

    slug = re.sub(r"\s+", "-", nom.strip().lower())

    dossier_franchise = os.path.join(cible, slug)
    if os.path.exists(dossier_franchise):
        print("ERREUR: la franchise '%s' existe deja (%s) - invariant: derive du "
              "modele source, jamais l'inverse, rien n'est ecrase" % (slug, dossier_franchise),
              file=sys.stderr)
        return 1

    os.makedirs(dossier_franchise, exist_ok=True)

    maintenant = datetime.now()
    date_compacte = maintenant.strftime("%Y%m%d")
    date_iso = maintenant.strftime("%Y-%m-%d")

    lignes = ["# " + nom.strip(),
              "",
              "statut: v0-initialise",
              "date de creation: " + date_compacte,
              "",
              "## Domaines",
              ""]
    for dom in DOMAINES:
        lignes.append("- " + dom)
    lignes.append("")
    with open(os.path.join(dossier_franchise, "README.md"), "w",
              encoding="utf-8") as f:
        f.write("\n".join(lignes))

    for dossier in DOSSIERS:
        os.makedirs(os.path.join(dossier_franchise, dossier), exist_ok=True)
        titre = dossier.split("_", 1)[1]
        with open(os.path.join(dossier_franchise, dossier, "README.md"), "w",
                  encoding="utf-8") as f:
            f.write("# %s - %s\n\nstatut: v0-initialise\n" % (nom.strip(), titre))

    donnees = {
        "nom": nom.strip(),
        "slug": slug,
        "domaines": list(DOMAINES),
        "cree": date_iso,
        "statut": "v0-initialise",
    }
    chemin_json = os.path.join(dossier_franchise, "franchise.json")
    with open(chemin_json, "w", encoding="utf-8") as f:
        json.dump(donnees, f, indent=2)
        f.write("\n")

    print("franchise generee: " + slug)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

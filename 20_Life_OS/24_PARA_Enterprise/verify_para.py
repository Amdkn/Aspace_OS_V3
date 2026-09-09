#!/usr/bin/env python3
# -*- coding: ascii -*-
"""verify_para.py - PARA Enterprise Pulse v0.

Verifie la structure du framework PARA Enterprise :
  [1] registre_para.json present, JSON valide, version v0, date_init
      2026-09-04, framework "PARA Enterprise", exactement les 4 cles
      projects/areas/resources/archives
  [2] les 4 dossiers 01_Projects_Picard, 02_Areas_Spock,
      03_Resources_Geordi, 04_Archives_Data existent
  [3] pour chaque categorie, la liste du registre est exactement
      l'ensemble des entrees de premier niveau du dossier correspondant,
      hors fichiers systeme exclus (AGENT.md, AGENTS.md, A3_*_Spec.md,
      SOUL.md) ; toute difference (manquant ou surplus) est une erreur
  [4] la racine porte A2_Computer_Enterprise_Spec.md non vide (spec A2
      fait foi)

Affiche PARA_OK et retourne rc=0 si tout passe, sinon PARA_KO et rc=1.
Stdlib uniquement. Spec : 00_Amadeus/60_Tape_Specs/2026-09-04-spec-para-enterprise-pulse-v0.md
"""

import json
import os
import sys

BASE = os.path.dirname(os.path.abspath(__file__))

CATEGORIES = {
    "projects": "01_Projects_Picard",
    "areas": "02_Areas_Spock",
    "resources": "03_Resources_Geordi",
    "archives": "04_Archives_Data",
}
EXCLUSIONS = {"AGENT.md", "AGENTS.md", "SOUL.md"}
SPEC_A2 = "A2_Computer_Enterprise_Spec.md"


def main():
    erreurs = []

    # 1. registre_para.json
    registre_path = os.path.join(BASE, "registre_para.json")
    registre = None
    if not os.path.isfile(registre_path):
        erreurs.append("registre_para.json manquant")
    else:
        try:
            with open(registre_path, "r", encoding="utf-8") as f:
                registre = json.load(f)
        except (ValueError, OSError) as e:
            erreurs.append("registre_para.json illisible: " + str(e))
        if registre is not None:
            if registre.get("version") != "v0":
                erreurs.append("registre: version != v0 (trouve " + repr(registre.get("version")) + ")")
            if registre.get("date_init") != "2026-09-04":
                erreurs.append("registre: date_init != 2026-09-04")
            if registre.get("framework") != "PARA Enterprise":
                erreurs.append("registre: framework != PARA Enterprise")
            cles = sorted(registre.keys())
            attendu = sorted(["version", "date_init", "framework"] + list(CATEGORIES))
            if cles != attendu:
                erreurs.append("registre: cles != " + str(attendu) + " (trouve " + str(cles) + ")")

    # 2 + 3. dossiers et coherence registre / disque
    for cat in ["projects", "areas", "resources", "archives"]:
        d = os.path.join(BASE, CATEGORIES[cat])
        if not os.path.isdir(d):
            erreurs.append("dossier manquant: " + CATEGORIES[cat])
            continue
        reel = sorted(
            n for n in os.listdir(d)
            if not (n in EXCLUSIONS or (n.startswith("A3_") and n.endswith("_Spec.md")))
        )
        if registre is not None:
            liste = registre.get(cat)
            if not isinstance(liste, list):
                erreurs.append("registre: " + cat + " n'est pas une liste")
            elif any(not isinstance(x, str) for x in liste):
                erreurs.append("registre: " + cat + " contient des entrees non string (objet dict au lieu de nom de fichier)")
            elif sorted(liste) != reel:
                manquants = sorted(set(reel) - set(liste))
                surplus = sorted(set(liste) - set(reel))
                if manquants:
                    erreurs.append("registre: " + cat + " manquants " + str(manquants))
                if surplus:
                    erreurs.append("registre: " + cat + " surplus " + str(surplus))

    # 4. spec A2 fait foi
    spec = os.path.join(BASE, SPEC_A2)
    if not os.path.isfile(spec):
        erreurs.append(SPEC_A2 + " manquant")
    elif os.path.getsize(spec) == 0:
        erreurs.append(SPEC_A2 + " vide")

    if erreurs:
        print("PARA_KO")
        for e in erreurs:
            print("  ERREUR: " + e)
        return 1

    print("PARA_OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())

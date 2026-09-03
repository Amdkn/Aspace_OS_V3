#!/usr/bin/env python3
# -*- coding: ascii -*-
"""verify_deal.py - DEAL Protostar Pulse v0.

Verifie la structure du framework DEAL Protostar :
  [1] pulse.json present, JSON valide, version v0, date_init, 4 etapes dans l'ordre
  [2] les 4 dossiers de stage existent
  [3] chaque stage porte sa spec A3_*_Spec.md non vide, son AGENT.md, son README.md, son SOUL.md
  [4] la racine porte A2_HoloJaneway_Protostar_Spec.md non vide (spec A2 fait foi)

Affiche DEAL_OK et retourne rc=0 si tout passe, sinon DEAL_KO et rc=1.
Stdlib uniquement. Spec : 00_Amadeus/60_Tape_Specs/2026-09-03-spec-deal-protostar-pulse-v0.md
"""

import json
import os
import sys

BASE = os.path.dirname(os.path.abspath(__file__))

STAGES = ["definition", "elimination", "automation", "liberation"]
DOSSIERS = {
    "definition": "01_Definition_Dal",
    "elimination": "02_Elimination_RokTahk",
    "automation": "03_Automation_Zero",
    "liberation": "04_Liberation_Gwyn",
}
PERSONAS = {
    "definition": "Dal",
    "elimination": "RokTahk",
    "automation": "Zero",
    "liberation": "Gwyn",
}
SPECS = {
    "definition": "A3_Dal_Definition_Spec.md",
    "elimination": "A3_RokTahk_Elimination_Spec.md",
    "automation": "A3_Zero_Automation_Spec.md",
    "liberation": "A3_Gwyn_Liberation_Spec.md",
}
ARTEFACTS = {
    "definition": None,
    "elimination": None,
    "automation": None,
    "liberation": None,
}
A2_SPEC = "A2_HoloJaneway_Protostar_Spec.md"


def main():
    erreurs = []

    # 1. pulse.json
    pulse_path = os.path.join(BASE, "pulse.json")
    if not os.path.isfile(pulse_path):
        erreurs.append("pulse.json manquant")
    else:
        try:
            pulse = json.load(open(pulse_path, "r", encoding="utf-8"))
        except (ValueError, OSError) as e:
            pulse = None
            erreurs.append("pulse.json illisible: " + str(e))
        if pulse is not None:
            if pulse.get("version") != "v0":
                erreurs.append("pulse.json: version != v0 (trouve " + repr(pulse.get("version")) + ")")
            if pulse.get("date_init") != "2026-09-03":
                erreurs.append("pulse.json: date_init != 2026-09-03")
            if pulse.get("framework") != "DEAL Protostar":
                erreurs.append("pulse.json: framework != DEAL Protostar")
            stages = [s.get("stage") for s in pulse.get("canon_4_stages", [])]
            if stages != STAGES:
                erreurs.append("pulse.json: stages != " + str(STAGES) + " (trouve " + str(stages) + ")")
            for s in pulse.get("canon_4_stages", []):
                st = s.get("stage")
                if st not in STAGES:
                    erreurs.append("pulse.json: stage inconnu " + repr(st))
                    continue
                if s.get("dossier") != DOSSIERS[st]:
                    erreurs.append("pulse.json: " + st + " dossier != " + DOSSIERS[st])
                if s.get("persona") != PERSONAS[st]:
                    erreurs.append("pulse.json: " + st + " persona != " + PERSONAS[st])
                if s.get("spec") != SPECS[st]:
                    erreurs.append("pulse.json: " + st + " spec != " + SPECS[st])
                if s.get("artefact") != ARTEFACTS[st]:
                    erreurs.append("pulse.json: " + st + " artefact != " + repr(ARTEFACTS[st]))

    # 2 + 3. dossiers, specs, AGENT/README/SOUL
    for st in STAGES:
        d = os.path.join(BASE, DOSSIERS[st])
        if not os.path.isdir(d):
            erreurs.append("dossier manquant: " + DOSSIERS[st])
            continue
        for nom in [SPECS[st], "AGENT.md", "README.md", "SOUL.md"]:
            p = os.path.join(d, nom)
            if not os.path.isfile(p):
                erreurs.append(DOSSIERS[st] + "/" + nom + " manquant")
            elif os.path.getsize(p) == 0:
                erreurs.append(DOSSIERS[st] + "/" + nom + " vide")

    # 4. spec A2 racine fait foi
    a2 = os.path.join(BASE, A2_SPEC)
    if not os.path.isfile(a2):
        erreurs.append(A2_SPEC + " manquant")
    elif os.path.getsize(a2) == 0:
        erreurs.append(A2_SPEC + " vide")

    if erreurs:
        print("DEAL_KO")
        for e in erreurs:
            print("  ERREUR: " + e)
        return 1

    print("DEAL_OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())

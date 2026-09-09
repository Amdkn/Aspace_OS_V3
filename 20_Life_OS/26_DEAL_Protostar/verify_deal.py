#!/usr/bin/env python3
# -*- coding: ascii -*-
"""verify_deal.py - DEAL Protostar Pulse v1.

Verifie la structure du framework DEAL Protostar :
  [1] pulse.json present, JSON valide, version v1, date_init, framework,
      5 cles de tete (version, date_init, framework, date_pulse,
      canon_4_stages), canon_4_stages conforme (ordre, cles, valeurs exactes)
  [2] les 4 dossiers de stage existent
  [3] chaque stage porte sa spec A3_*_Spec.md non vide, son AGENT.md, son README.md, son SOUL.md
  [4] la racine porte A2_HoloJaneway_Protostar_Spec.md non vide (spec A2 fait foi)
  [5] pulse.json porte date_pulse parseable %Y-%m-%d
  [6] coherence pulse <-> disque : 4 stages dans l'ordre, dossier existant,
      spec non vide dans ce dossier
  [7] source_ok recalcule pour chaque stage (dossier existe ET spec non vide) :
      toute divergence pulse <-> recalcul est une erreur
  [8] unicite du registre : chaque dossier de canon_4_stages existe reelslement
      a la racine du framework (pas de dossier fantome)

Affiche DEAL_OK et retourne rc=0 si tout passe, sinon DEAL_KO et rc=1.
Stdlib uniquement. Spec : 00_Amadeus/60_Tape_Specs/2026-09-05-spec-deal-protostar-pulse-v1.md
"""

import json
import os
import sys
from datetime import datetime

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
CLEES_TETE = ["version", "date_init", "framework", "date_pulse", "canon_4_stages"]


def source_ok_recalculee(st):
    d = os.path.join(BASE, DOSSIERS[st])
    p = os.path.join(d, SPECS[st])
    return 1 if (os.path.isdir(d) and os.path.isfile(p) and os.path.getsize(p) > 0) else 0


def main():
    erreurs = []

    # 1. pulse.json : presence, JSON valide, en-tete v1
    pulse_path = os.path.join(BASE, "pulse.json")
    pulse = None
    if not os.path.isfile(pulse_path):
        erreurs.append("pulse.json manquant")
    else:
        try:
            pulse = json.load(open(pulse_path, "r", encoding="utf-8"))
        except (ValueError, OSError) as e:
            erreurs.append("pulse.json illisible: " + str(e))
        if pulse is not None:
            if list(pulse.keys()) != CLEES_TETE:
                erreurs.append("pulse.json: cles de tete != " + str(CLEES_TETE) + " (trouve " + str(list(pulse.keys())) + ")")
            if pulse.get("version") != "v1":
                erreurs.append("pulse.json: version != v1 (trouve " + repr(pulse.get("version")) + ")")
            if pulse.get("date_init") != "2026-09-03":
                erreurs.append("pulse.json: date_init != 2026-09-03")
            if pulse.get("framework") != "DEAL Protostar":
                erreurs.append("pulse.json: framework != DEAL Protostar")
            stages = pulse.get("canon_4_stages")
            if not isinstance(stages, list) or [s.get("stage") for s in stages] != STAGES:
                erreurs.append("pulse.json: canon_4_stages != 4 stages dans l'ordre " + str(STAGES))
            else:
                for s in stages:
                    st = s.get("stage")
                    if list(s.keys()) != ["stage", "dossier", "persona", "spec", "artefact", "source_ok"]:
                        erreurs.append("pulse.json: " + str(st) + " cles != [stage, dossier, persona, spec, artefact, source_ok]")
                        continue
                    if s.get("dossier") != DOSSIERS[st]:
                        erreurs.append("pulse.json: " + st + " dossier != " + DOSSIERS[st])
                    if s.get("persona") != PERSONAS[st]:
                        erreurs.append("pulse.json: " + st + " persona != " + PERSONAS[st])
                    if s.get("spec") != SPECS[st]:
                        erreurs.append("pulse.json: " + st + " spec != " + SPECS[st])
                    if s.get("artefact") != ARTEFACTS[st]:
                        erreurs.append("pulse.json: " + st + " artefact != " + repr(ARTEFACTS[st]))
                    if s.get("source_ok") not in (0, 1):
                        erreurs.append("pulse.json: " + st + " source_ok != 0/1 (trouve " + repr(s.get("source_ok")) + ")")

    # 5. date_pulse parseable
    if pulse is not None:
        dp = pulse.get("date_pulse")
        try:
            datetime.strptime(dp, "%Y-%m-%d")
        except (TypeError, ValueError):
            erreurs.append("pulse.json: date_pulse non parseable %Y-%m-%d (trouve " + repr(dp) + ")")

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

    # 6 + 7 + 8. coherence pulse <-> disque, source_ok recalcule, unicite
    if pulse is not None and isinstance(pulse.get("canon_4_stages"), list):
        stages = pulse["canon_4_stages"]
        if len(stages) != 4 or [s.get("stage") for s in stages] != STAGES:
            erreurs.append("pulse.json: canon_4_stages != exactement 4 objets dans l'ordre " + str(STAGES))
        else:
            dossiers_vus = []
            for s in stages:
                st = s.get("stage")
                dossier = s.get("dossier")
                spec = s.get("spec")
                d = os.path.join(BASE, str(dossier))
                if not os.path.isdir(d):
                    erreurs.append("[6] dossier de stage absent du disque: " + str(dossier))
                else:
                    p = os.path.join(d, str(spec))
                    if not (os.path.isfile(p) and os.path.getsize(p) > 0):
                        erreurs.append("[6] spec absente ou vide sur disque: " + str(dossier) + "/" + str(spec))
                if dossier not in dossiers_vus:
                    dossiers_vus.append(dossier)
                recalc = source_ok_recalculee(st)
                if s.get("source_ok") != recalc:
                    erreurs.append("[7] " + st + " source_ok pulse=" + repr(s.get("source_ok")) + " != recalcul=" + repr(recalc))
            # [8] unicite : chaque dossier existe reellement a la racine
            for dossier in dossiers_vus:
                if not os.path.isdir(os.path.join(BASE, str(dossier))):
                    erreurs.append("[8] dossier fantome dans le pulse: " + str(dossier))

    if erreurs:
        print("DEAL_KO")
        for e in erreurs:
            print("  ERREUR: " + e)
        return 1

    print("DEAL_OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())

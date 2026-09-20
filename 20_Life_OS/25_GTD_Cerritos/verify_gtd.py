#!/usr/bin/env python3
# -*- coding: ascii -*-
"""verify_gtd.py - GTD Cerritos Pulse v1.

Verifie la structure du framework GTD Cerritos et la coherence pulse.json <-> disque :
  [1] pulse.json present, JSON valide, cles de tete exactes dans l'ordre
      [version, date_init, framework, date_pulse, canon_5_stages],
      version v1, date_init 2026-09-03, framework GTD Cerritos
  [2] date_pulse parseable au format YYYY-MM-DD, posterieure ou egale a date_init
  [3] canon_5_stages = 5 objets, ordre canonique capture/clarify/organize/review/engage,
      cles [stage, dossier, persona, spec, artefact], valeurs v0 conservees
  [4] les 5 dossiers de stage existent
  [5] chaque stage porte sa spec A3_*_Spec.md non vide, son AGENT.md, son README.md, son SOUL.md
  [6] artefact canon actif present quand non null :
      01_Inbox_Mariner/inbox.md (non vide, titre reel '# Inbox - Mariner (Capture)')
      02_Clarify_Boimler/ADR-GTD-001.md (non vide)
  [7] inbox.md a une section '## Items' (structure capture)
  [8] canon racine A2_HoloDeck_Cerritos_Spec.md present

Affiche GTD_OK et retourne rc=0 si tout passe, sinon GTD_KO et rc=1.
Stdlib uniquement (json, os, sys, datetime).
Spec : 00_Amadeus/60_Tape_Specs/2026-09-16-spec-gtd-cerritos-pulse-v1.md
"""

import json
import os
import sys
from datetime import datetime

BASE = os.path.dirname(os.path.abspath(__file__))

STAGES = ["capture", "clarify", "organize", "review", "engage"]
DOSSIERS = {
    "capture": "01_Inbox_Mariner",
    "clarify": "02_Clarify_Boimler",
    "organize": "03_Organize_Rutherford",
    "review": "04_Review_Tendi",
    "engage": "05_Engage_Freeman",
}
PERSONAS = {
    "capture": "Mariner",
    "clarify": "Boimler",
    "organize": "Rutherford",
    "review": "Tendi",
    "engage": "Freeman",
}
SPECS = {
    "capture": "A3_Mariner_Capture_Spec.md",
    "clarify": "A3_Boimler_Clarify_Spec.md",
    "organize": "A3_Rutherford_Organize_Spec.md",
    "review": "A3_Tendi_Review_Spec.md",
    "engage": "A3_Freeman_Engage_Spec.md",
}
ARTEFACTS = {
    "capture": "inbox.md",
    "clarify": "ADR-GTD-001.md",
    "organize": None,
    "review": None,
    "engage": None,
}
TITRE_INBOX = "# Inbox - Mariner (Capture)"
CANON_RACINE = "A2_HoloDeck_Cerritos_Spec.md"
CLES_TETE = ["version", "date_init", "framework", "date_pulse", "canon_5_stages"]


def lire_texte(p):
    with open(p, "r", encoding="utf-8") as f:
        return f.read()


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
            # [schema] cles de tete exactes dans l'ordre
            cles = list(pulse.keys())
            if cles != CLES_TETE:
                erreurs.append("pulse.json: cles de tete != " + str(CLES_TETE) + " (trouve " + str(cles) + ")")
            if pulse.get("version") != "v1":
                erreurs.append("pulse.json: version != v1 (trouve " + repr(pulse.get("version")) + ")")
            if pulse.get("date_init") != "2026-09-03":
                erreurs.append("pulse.json: date_init != 2026-09-03")
            if pulse.get("framework") != "GTD Cerritos":
                erreurs.append("pulse.json: framework != GTD Cerritos")

            # [date] date_pulse parseable et >= date_init
            dp = pulse.get("date_pulse")
            dp_dt = None
            di_dt = None
            if not isinstance(dp, str):
                erreurs.append("pulse.json: date_pulse absent ou non chaine (trouve " + repr(dp) + ")")
            else:
                try:
                    dp_dt = datetime.strptime(dp, "%Y-%m-%d")
                except ValueError:
                    erreurs.append("pulse.json: date_pulse non parseable YYYY-MM-DD: " + repr(dp))
            di = pulse.get("date_init")
            if isinstance(di, str):
                try:
                    di_dt = datetime.strptime(di, "%Y-%m-%d")
                except ValueError:
                    erreurs.append("pulse.json: date_init non parseable YYYY-MM-DD: " + repr(di))
            if dp_dt is not None and di_dt is not None and dp_dt < di_dt:
                erreurs.append("pulse.json: date_pulse " + str(dp) + " anterieure a date_init " + str(di))

            # [ordre] 5 stages ordre canonique, cles et valeurs conservees
            canon = pulse.get("canon_5_stages", [])
            if not isinstance(canon, list) or len(canon) != 5:
                erreurs.append("pulse.json: canon_5_stages != 5 objets (trouve " + str(len(canon) if isinstance(canon, list) else "non-liste") + ")")
            else:
                stages = [s.get("stage") for s in canon]
                if stages != STAGES:
                    erreurs.append("pulse.json: stages != " + str(STAGES) + " (trouve " + str(stages) + ")")
                for s in canon:
                    st = s.get("stage")
                    if st not in STAGES:
                        erreurs.append("pulse.json: stage inconnu " + repr(st))
                        continue
                    if list(s.keys()) != ["stage", "dossier", "persona", "spec", "artefact"]:
                        erreurs.append("pulse.json: " + st + " cles != [stage, dossier, persona, spec, artefact] (trouve " + str(list(s.keys())) + ")")
                    if s.get("dossier") != DOSSIERS[st]:
                        erreurs.append("pulse.json: " + st + " dossier != " + DOSSIERS[st])
                    if s.get("persona") != PERSONAS[st]:
                        erreurs.append("pulse.json: " + st + " persona != " + PERSONAS[st])
                    if s.get("spec") != SPECS[st]:
                        erreurs.append("pulse.json: " + st + " spec != " + SPECS[st])
                    if s.get("artefact") != ARTEFACTS[st]:
                        erreurs.append("pulse.json: " + st + " artefact != " + repr(ARTEFACTS[st]))

    # 4 + 5. [disque] dossiers, specs, AGENT/README/SOUL
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

    # 6 + 7. [artefacts] artefact canon actif present quand non null
    inbox = os.path.join(BASE, "01_Inbox_Mariner", "inbox.md")
    if os.path.isfile(inbox):
        if os.path.getsize(inbox) == 0:
            erreurs.append("01_Inbox_Mariner/inbox.md vide")
        else:
            contenu = lire_texte(inbox)
            if TITRE_INBOX not in contenu:
                erreurs.append("inbox.md sans titre reel " + repr(TITRE_INBOX))
            if "## Items" not in contenu:
                erreurs.append("inbox.md sans section '## Items'")
    else:
        erreurs.append("01_Inbox_Mariner/inbox.md manquant")

    adr = os.path.join(BASE, "02_Clarify_Boimler", "ADR-GTD-001.md")
    if not os.path.isfile(adr):
        erreurs.append("02_Clarify_Boimler/ADR-GTD-001.md manquant")
    elif os.path.getsize(adr) == 0:
        erreurs.append("02_Clarify_Boimler/ADR-GTD-001.md vide")

    # 8. [canon] canon racine si present attendu
    if not os.path.isfile(os.path.join(BASE, CANON_RACINE)):
        erreurs.append("canon racine manquant: " + CANON_RACINE)

    if erreurs:
        print("GTD_KO")
        for e in erreurs:
            print("  ERREUR: " + e)
        return 1

    print("GTD_OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())

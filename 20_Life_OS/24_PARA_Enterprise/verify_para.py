#!/usr/bin/env python3
# -*- coding: ascii -*-
"""verify_para.py - PARA Enterprise Pulse v1.

Verifie la structure du framework PARA Enterprise :
  [1] pulse.json present, JSON valide, schema exact :
      - cles == {version, date_init, framework, date_pulse, canon_4_domains}
      - version v1, date_init 2026-09-04, date_pulse >= 2026-09-16
        (format YYYY-MM-DD)
      - framework "PARA Enterprise"
      - canon_4_domains : liste de 4 objets, ordre canon
        projects/areas/resources/archives, chacun avec exactement les cles
        domain/dossier/persona/state/entries
  [2] coherence des entries : pour chaque domain, les entries de pulse.json
      == le listing disque (hors exclusions) == la liste de registre_para.json
      (trois sources, une seule verite)
  [3] les 4 dossiers 01_Projects_Picard, 02_Areas_Spock,
      03_Resources_Geordi, 04_Archives_Data existent
  [4] la racine porte A2_Computer_Enterprise_Spec.md non vide (spec A2
      fait foi)

Affiche PARA_OK et retourne rc=0 si tout passe, sinon PARA_KO et rc=1.
Stdlib uniquement. Spec : 00_Amadeus/60_Tape_Specs/
2026-09-16-spec-para-enterprise-pulse-v1-refresh.md
"""

import json
import os
import sys

BASE = os.path.dirname(os.path.abspath(__file__))

CANON = ["projects", "areas", "resources", "archives"]
CATEGORIES = {
    "projects": "01_Projects_Picard",
    "areas": "02_Areas_Spock",
    "resources": "03_Resources_Geordi",
    "archives": "04_Archives_Data",
}
PERSONAS = {
    "projects": "Picard",
    "areas": "Spock",
    "resources": "Geordi",
    "archives": "Data",
}
STATES = {"projects": "active", "areas": "idle", "resources": "active", "archives": "idle"}
EXCLUSIONS = {"AGENT.md", "AGENTS.md", "SOUL.md"}
SPEC_A2 = "A2_Computer_Enterprise_Spec.md"


def listing_disque(cat):
    d = os.path.join(BASE, CATEGORIES[cat])
    if not os.path.isdir(d):
        return None
    return sorted(
        n for n in os.listdir(d)
        if not (n in EXCLUSIONS or (n.startswith("A3_") and n.endswith("_Spec.md")))
    )


def main():
    erreurs = []

    # 1. pulse.json : schema
    pulse_path = os.path.join(BASE, "pulse.json")
    pulse = None
    if not os.path.isfile(pulse_path):
        erreurs.append("pulse.json manquant")
    else:
        try:
            with open(pulse_path, "r", encoding="utf-8") as f:
                pulse = json.load(f)
        except (ValueError, OSError) as e:
            erreurs.append("pulse.json illisible: " + str(e))
    if pulse is not None:
        if pulse.get("version") != "v1":
            erreurs.append("pulse: version != v1 (trouve " + repr(pulse.get("version")) + ")")
        if pulse.get("date_init") != "2026-09-04":
            erreurs.append("pulse: date_init != 2026-09-04 (trouve " + repr(pulse.get("date_init")) + ")")
        dp = pulse.get("date_pulse")
        ok_dp = False
        if isinstance(dp, str):
            try:
                from datetime import datetime as _dt
                _dt.strptime(dp, "%Y-%m-%d")
                ok_dp = dp >= "2026-09-16"
            except ValueError:
                ok_dp = False
        if not ok_dp:
            erreurs.append("pulse: date_pulse < 2026-09-16 ou format invalide (trouve " + repr(dp) + ")")
        if pulse.get("framework") != "PARA Enterprise":
            erreurs.append("pulse: framework != PARA Enterprise (trouve " + repr(pulse.get("framework")) + ")")
        cles = sorted(pulse.keys())
        attendu = sorted(["version", "date_init", "framework", "date_pulse", "canon_4_domains"])
        if cles != attendu:
            erreurs.append("pulse: cles != " + str(attendu) + " (trouve " + str(cles) + ")")
        canon = pulse.get("canon_4_domains")
        if not isinstance(canon, list) or len(canon) != 4:
            erreurs.append("pulse: canon_4_domains n'est pas une liste de 4")
        else:
            for i, bloc in enumerate(canon):
                if not isinstance(bloc, dict):
                    erreurs.append("pulse: canon[" + str(i) + "] n'est pas un objet")
                    continue
                if bloc.get("domain") != CANON[i]:
                    erreurs.append("pulse: canon[" + str(i) + "].domain != " + CANON[i] +
                                   " (trouve " + repr(bloc.get("domain")) + ")")
                for k in ("dossier", "persona", "state", "entries"):
                    if k not in bloc:
                        erreurs.append("pulse: canon[" + str(i) + "] cle manquante: " + k)
                if sorted(bloc.keys()) != sorted(["domain", "dossier", "persona", "state", "entries"]):
                    erreurs.append("pulse: canon[" + str(i) + "] cles != [domain,dossier,persona,state,entries]")
                if isinstance(bloc, dict) and bloc.get("dossier") != CATEGORIES.get(CANON[i]):
                    erreurs.append("pulse: canon[" + str(i) + "].dossier != " + CATEGORIES[CANON[i]])
                if isinstance(bloc, dict) and bloc.get("persona") != PERSONAS.get(CANON[i]):
                    erreurs.append("pulse: canon[" + str(i) + "].persona != " + PERSONAS[CANON[i]])
                if isinstance(bloc, dict) and bloc.get("state") != STATES.get(CANON[i]):
                    erreurs.append("pulse: canon[" + str(i) + "].state != " + STATES[CANON[i]] +
                                   " (trouve " + repr(bloc.get("state")) + ")")
                ent = bloc.get("entries")
                if not isinstance(ent, list) or any(not isinstance(x, str) for x in ent):
                    erreurs.append("pulse: canon[" + str(i) + "].entries n'est pas une liste de strings")
                    ent = None
                if isinstance(bloc, dict):
                    bloc["_entries_ok"] = ent

    # 2. registre_para.json
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

    # 3. dossiers + coherence pulse entries / registre / disque
    for cat in CANON:
        d = os.path.join(BASE, CATEGORIES[cat])
        if not os.path.isdir(d):
            erreurs.append("dossier manquant: " + CATEGORIES[cat])
            continue
        reel = listing_disque(cat)
        # entries de pulse
        pulse_ent = None
        if pulse is not None and isinstance(pulse.get("canon_4_domains"), list) \
                and len(pulse["canon_4_domains"]) == 4:
            pulse_ent = pulse["canon_4_domains"][CANON.index(cat)].get("_entries_ok")
        # liste du registre
        reg_liste = None
        if registre is not None:
            reg_liste = registre.get(cat)
            if not isinstance(reg_liste, list):
                erreurs.append("registre: " + cat + " n'est pas une liste")
                reg_liste = None
            elif any(not isinstance(x, str) for x in reg_liste):
                erreurs.append("registre: " + cat + " contient des entrees non string")
                reg_liste = None
        # coherence tripartite
        if reel is not None and pulse_ent is not None and reg_liste is not None:
            if sorted(pulse_ent) != reel:
                manq = sorted(set(reel) - set(pulse_ent))
                surp = sorted(set(pulse_ent) - set(reel))
                if manq:
                    erreurs.append("pulse: " + cat + " manquants vs disque " + str(manq))
                if surp:
                    erreurs.append("pulse: " + cat + " surplus vs disque " + str(surp))
            if sorted(reg_liste) != reel:
                manq = sorted(set(reel) - set(reg_liste))
                surp = sorted(set(reg_liste) - set(reel))
                if manq:
                    erreurs.append("registre: " + cat + " manquants vs disque " + str(manq))
                if surp:
                    erreurs.append("registre: " + cat + " surplus vs disque " + str(surp))
            if sorted(pulse_ent) != sorted(reg_liste):
                erreurs.append("coherence: " + cat + " pulse != registre")

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

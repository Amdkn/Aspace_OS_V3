#!/usr/bin/env python3
# -*- coding: ascii -*-
"""snapshot.py - Jerry Business Pulse v2 : historisation mensuelle.

Produit un snapshot JSON par variante et par mois dans
00_Registre/historique/hist-<variante>-<AAAA-MM>.json, depuis le pulse.json
courant de chaque variante. Idempotent : si le snapshot du mois existe deja
avec les memes metriques, il est reecrit a l'identique (horodatage conserve).

Affiche une ligne "OK <fichier>" par snapshot puis SNAPSHOTS_OK, rc=0.
En cas d'erreur : SNAPSHOTS_KO + message, rc=1.
Stdlib uniquement. Spec : 00_Amadeus/60_Tape_Specs/2026-09-02-spec-jerry-business-pulse-v2.md
"""

import json
import os
import sys
from datetime import datetime

BASE = os.path.dirname(os.path.abspath(__file__))
HIST_DIR = os.path.join(BASE, "00_Registre", "historique")

VARIANTES = ["prime", "bio", "nexus", "solarpunk"]
DOSSIERS = {
    "prime": "01_Prime",
    "bio": "02_Bio",
    "nexus": "03_Nexus",
    "solarpunk": "04_Solarpunk",
}


def main():
    try:
        mois = datetime.now().strftime("%Y-%m")
        horodatage_nouveau = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
        os.makedirs(HIST_DIR, exist_ok=True)
        for vid in VARIANTES:
            pulse_path = os.path.join(BASE, DOSSIERS[vid], "pulse.json")
            with open(pulse_path, "r", encoding="utf-8") as f:
                pulse = json.load(f)
            metriques = pulse.get("metriques")
            if not isinstance(metriques, dict):
                raise ValueError(
                    DOSSIERS[vid] + "/pulse.json: metriques absentes ou non objet"
                )
            out_path = os.path.join(HIST_DIR, "hist-" + vid + "-" + mois + ".json")

            # Idempotence : conserver l'horodatage existant si le snapshot
            # du mois existe deja avec les memes metriques.
            horodatage = horodatage_nouveau
            if os.path.isfile(out_path):
                try:
                    with open(out_path, "r", encoding="utf-8") as f:
                        ancien = json.load(f)
                    if (
                        ancien.get("variante") == vid
                        and ancien.get("mois") == mois
                        and ancien.get("metriques") == metriques
                        and isinstance(ancien.get("horodatage"), str)
                        and ancien.get("horodatage")
                    ):
                        horodatage = ancien["horodatage"]
                except (ValueError, OSError):
                    pass

            snapshot = {
                "variante": vid,
                "mois": mois,
                "metriques": metriques,
                "horodatage": horodatage,
            }
            with open(out_path, "w", encoding="utf-8") as f:
                json.dump(snapshot, f, indent=2, ensure_ascii=False)
                f.write("\n")
            print("OK " + "hist-" + vid + "-" + mois + ".json")
    except (ValueError, OSError) as e:
        print("SNAPSHOTS_KO")
        print("  ERREUR: " + str(e))
        return 1
    print("SNAPSHOTS_OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())

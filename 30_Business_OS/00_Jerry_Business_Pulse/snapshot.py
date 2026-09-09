#!/usr/bin/env python3
# -*- coding: ascii -*-
"""snapshot.py - Jerry Business Pulse : historisation mensuelle (v2) + pulse
hebdo publie (v1, ruban Rock_00_Business_Pulse_12WY).

Modes :
  (sans argument)  historisation mensuelle v2 : un snapshot JSON par variante
                   dans 00_Registre/historique/hist-<variante>-<AAAA-MM>.json.
  --publie         genere 00_Registre/pulse_hebdo.md : date de generation,
                   etat du Rock (sources : registre_para.json PARA Enterprise
                   + registre.json du pulse), compteur de consultations.
  --consulte       incremente le compteur de consultations dans
                   00_Registre/consultations.json (rc=0).

Le pulse ne fait que reflechir ce que les registres contiennent (aucune
donnee business inventee). Idempotent : si le snapshot du mois existe deja
avec les memes metriques, il est reecrit a l'identique (horodatage conserve).

Affiche "OK <fichier>" par artefact puis SNAPSHOTS_OK, rc=0.
En cas d'erreur : SNAPSHOTS_KO + message, rc=1.
Stdlib uniquement.
Specs :
  00_Amadeus/60_Tape_Specs/2026-09-02-spec-jerry-business-pulse-v2.md
  00_Amadeus/60_Tape_Specs/2026-09-03-business-pulse-v1-publie-pulse-hebdo-genere-et-c.md
"""

import argparse
import json
import os
import sys
from datetime import datetime

BASE = os.path.dirname(os.path.abspath(__file__))
REG_DIR = os.path.join(BASE, "00_Registre")
HIST_DIR = os.path.join(REG_DIR, "historique")
PARA_PATH = os.path.join(
    BASE, "..", "..", "20_Life_OS", "24_PARA_Enterprise", "registre_para.json"
)

VARIANTES = ["prime", "bio", "nexus", "solarpunk"]
DOSSIERS = {
    "prime": "01_Prime",
    "bio": "02_Bio",
    "nexus": "03_Nexus",
    "solarpunk": "04_Solarpunk",
}


def historisation():
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


def lire_consultations():
    """Lit 00_Registre/consultations.json ; le cree a zero si absent."""
    path = os.path.join(REG_DIR, "consultations.json")
    if not os.path.isfile(path):
        return {"compteur": 0}
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    n = data.get("compteur")
    if not isinstance(n, int) or isinstance(n, bool) or n < 0:
        raise ValueError(
            "consultations.json: compteur absent ou non entier >= 0"
        )
    return data


def publier_pulse():
    """Genere 00_Registre/pulse_hebdo.md depuis les registres mesures."""
    os.makedirs(REG_DIR, exist_ok=True)

    # Source 1 : registre PARA Enterprise (lecture seule, le disque fait foi).
    if not os.path.isfile(PARA_PATH):
        raise ValueError("registre_para.json introuvable : " + PARA_PATH)
    with open(PARA_PATH, "r", encoding="utf-8") as f:
        para = json.load(f)
    projects = para.get("projects")
    if not isinstance(projects, list):
        raise ValueError("registre_para.json: projects absent ou non liste")
    rock_present = "Rock_00_Business_Pulse_12WY" in projects

    # Source 2 : registre du pulse (etat des 4 variantes).
    reg_path = os.path.join(REG_DIR, "registre.json")
    with open(reg_path, "r", encoding="utf-8") as f:
        reg = json.load(f)
    if reg.get("version") != "v2":
        raise ValueError("registre.json: version != v2")
    n_variantes = len(reg.get("variantes", []))

    # Source 3 : metriques mesurees de chaque variante (pulse.json).
    lignes_met = []
    for vid in VARIANTES:
        p = os.path.join(BASE, DOSSIERS[vid], "pulse.json")
        with open(p, "r", encoding="utf-8") as f:
            pulse = json.load(f)
        met = pulse.get("metriques")
        if not isinstance(met, dict):
            raise ValueError(DOSSIERS[vid] + "/pulse.json: metriques absentes")
        lignes_met.append(
            "| " + DOSSIERS[vid] + " | "
            + str(met.get("revenus_mois", "n/a")) + " | "
            + str(met.get("clients_actifs", "n/a")) + " | "
            + str(met.get("offres_lancees", "n/a")) + " |"
        )

    cons = lire_consultations()

    maintenant = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    lignes = [
        "# Pulse hebdo - Rock_00_Business_Pulse_12WY",
        "",
        "Date de generation : " + maintenant,
        "",
        "## Etat du Rock (registres mesures)",
        "",
        "- Framework : " + str(para.get("framework", "n/a"))
        + " (registre_para.json version " + str(para.get("version", "n/a")) + ")",
        "- Rock_00_Business_Pulse_12WY present dans PARA projects : "
        + ("oui" if rock_present else "NON"),
        "- Registre Jerry Pulse : version " + str(reg.get("version"))
        + ", " + str(n_variantes) + " variantes",
        "",
        "## Metriques mesurees (pulse.json, aucune donnee inventee)",
        "",
        "| Dossier | revenus_mois | clients_actifs | offres_lancees |",
        "|---|---|---|---|",
    ]
    lignes.extend(lignes_met)
    lignes.extend([
        "",
        "## Consultations du pulse hebdo",
        "",
        "Compteur : " + str(cons.get("compteur", 0)),
        "",
        "Genere par snapshot.py --publie (python stdlib uniquement).",
        "Source : 30_Business_OS/00_Jerry_Business_Pulse/00_Registre/",
        "",
    ])
    out_path = os.path.join(REG_DIR, "pulse_hebdo.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lignes))
    print("OK pulse_hebdo.md")


def consulter():
    """Incremente le compteur de consultations (l'utilisateur a consulte)."""
    cons = lire_consultations()
    cons["compteur"] = cons.get("compteur", 0) + 1
    path = os.path.join(REG_DIR, "consultations.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(cons, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print("OK consultations.json (compteur=" + str(cons["compteur"]) + ")")


def main():
    parser = argparse.ArgumentParser(
        description="Jerry Business Pulse : historisation / pulse hebdo / consultation"
    )
    parser.add_argument(
        "--publie",
        action="store_true",
        help="genere 00_Registre/pulse_hebdo.md depuis les registres",
    )
    parser.add_argument(
        "--consulte",
        action="store_true",
        help="incremente le compteur de consultations",
    )
    args = parser.parse_args()
    try:
        if args.consulte:
            consulter()
        elif args.publie:
            publier_pulse()
        else:
            historisation()
    except (ValueError, OSError) as e:
        print("SNAPSHOTS_KO")
        print("  ERREUR: " + str(e))
        return 1
    print("SNAPSHOTS_OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
#!/usr/bin/env python3
# -*- coding: ascii -*-
"""verifier.py - Jerry Business Pulse v2.

Verifie la structure du pulse B1 :
  [v0] dossiers des 4 variantes presents
  [v0] registre.json valide (version, ordre des variantes)
  [v0] README de chaque variante non vide et portant "statut: v0-initialise"
  [v1] pulse.json de chaque variante : existe, JSON valide, id/nom/domaine
       corrects, 3 metriques a zero, statut == "v1-initialise"
  [v2] registre.json version == "v2", champ historisation (dossier + actif)
  [v2] dossier 00_Registre/historique present
  [v2] snapshot hist-<variante>-<mois courant>.json valide pour chaque
       variante (format spec v2, metriques minimales numeriques)

Affiche PULSE_OK et retourne rc=0 si tout passe, sinon PULSE_KO et rc=1.
Stdlib uniquement. Spec : 00_Amadeus/60_Tape_Specs/2026-09-02-spec-jerry-business-pulse-v2.md
"""

import json
import os
import sys
from datetime import datetime

BASE = os.path.dirname(os.path.abspath(__file__))

VARIANTES = ["prime", "bio", "nexus", "solarpunk"]
DOSSIERS = {
    "prime": "01_Prime",
    "bio": "02_Bio",
    "nexus": "03_Nexus",
    "solarpunk": "04_Solarpunk",
}
NOMS = {
    "prime": "Jerry Prime",
    "bio": "Jerry Bio",
    "nexus": "Jerry Nexus",
    "solarpunk": "Jerry Solarpunk",
}
DOMAINES = {
    "prime": "business classique",
    "bio": "bio/health",
    "nexus": "tech/plateforme",
    "solarpunk": "solaire/durabilite",
}
STATUT = "statut: v0-initialise"
PULSE_STATUT = "v1-initialise"
METRIQUES = ["revenus_mois", "clients_actifs", "offres_lancees"]


def main():
    erreurs = []

    # 1. README racine non vide
    readme_racine = os.path.join(BASE, "README.md")
    if not os.path.isfile(readme_racine) or os.path.getsize(readme_racine) == 0:
        erreurs.append("README.md racine manquant ou vide")

    # 2. Dossiers des 4 variantes presents
    for vid in VARIANTES:
        d = os.path.join(BASE, DOSSIERS[vid])
        if not os.path.isdir(d):
            erreurs.append("dossier manquant: " + DOSSIERS[vid])

    # 3. Registre central
    reg_path = os.path.join(BASE, "00_Registre", "registre.json")
    if not os.path.isfile(reg_path):
        erreurs.append("00_Registre/registre.json manquant")
    else:
        try:
            with open(reg_path, "r", encoding="utf-8") as f:
                reg = json.load(f)
            if reg.get("version") != "v2":
                erreurs.append("registre.json: version != v2")
            if reg.get("date_init") != "2026-09-03":
                erreurs.append("registre.json: date_init != 2026-09-03")
            ids = [v.get("id") for v in reg.get("variantes", [])]
            if ids != VARIANTES:
                erreurs.append(
                    "registre.json: variantes != " + str(VARIANTES) + " (trouve " + str(ids) + ")"
                )
            for v in reg.get("variantes", []):
                vid = v.get("id")
                if vid not in VARIANTES:
                    erreurs.append("registre.json: id inconnu " + repr(vid))
                    continue
                attendu_dossier = DOSSIERS[vid]
                if v.get("dossier") != attendu_dossier:
                    erreurs.append(
                        "registre.json: " + vid + " dossier != " + attendu_dossier
                        + " (trouve " + repr(v.get("dossier")) + ")"
                    )
                if v.get("nom") != NOMS[vid]:
                    erreurs.append(
                        "registre.json: " + vid + " nom != " + NOMS[vid]
                        + " (trouve " + repr(v.get("nom")) + ")"
                    )
                if v.get("cree") != "2026-09-03":
                    erreurs.append("registre.json: " + vid + " cree != 2026-09-03")
            hist_cfg = reg.get("historisation")
            if not isinstance(hist_cfg, dict):
                erreurs.append("registre.json: champ historisation absent ou non objet")
            else:
                if hist_cfg.get("dossier") != "00_Registre/historique":
                    erreurs.append(
                        "registre.json: historisation.dossier != 00_Registre/historique"
                        + " (trouve " + repr(hist_cfg.get("dossier")) + ")"
                    )
                if hist_cfg.get("actif") is not True:
                    erreurs.append("registre.json: historisation.actif != true")
        except (ValueError, OSError) as e:
            erreurs.append("registre.json illisible: " + str(e))

    # 4. README de chaque variante : non vide + statut present
    for vid in VARIANTES:
        p = os.path.join(BASE, DOSSIERS[vid], "README.md")
        if not os.path.isfile(p):
            erreurs.append(DOSSIERS[vid] + "/README.md manquant")
            continue
        if os.path.getsize(p) == 0:
            erreurs.append(DOSSIERS[vid] + "/README.md vide")
            continue
        with open(p, "r", encoding="utf-8") as f:
            contenu = f.read()
        if STATUT not in contenu:
            erreurs.append(DOSSIERS[vid] + "/README.md sans '" + STATUT + "'")
        titre = "# " + NOMS[vid]
        if titre not in contenu:
            erreurs.append(DOSSIERS[vid] + "/README.md sans titre '" + titre + "'")

    # 5. [v1] pulse.json de chaque variante
    for vid in VARIANTES:
        p = os.path.join(BASE, DOSSIERS[vid], "pulse.json")
        if not os.path.isfile(p):
            erreurs.append(DOSSIERS[vid] + "/pulse.json manquant")
            continue
        try:
            with open(p, "r", encoding="utf-8") as f:
                pulse = json.load(f)
        except (ValueError, OSError) as e:
            erreurs.append(DOSSIERS[vid] + "/pulse.json illisible: " + str(e))
            continue
        if pulse.get("id") != vid:
            erreurs.append(
                DOSSIERS[vid] + "/pulse.json: id != " + vid
                + " (trouve " + repr(pulse.get("id")) + ")"
            )
        if pulse.get("nom") != NOMS[vid]:
            erreurs.append(
                DOSSIERS[vid] + "/pulse.json: nom != " + NOMS[vid]
                + " (trouve " + repr(pulse.get("nom")) + ")"
            )
        if pulse.get("domaine") != DOMAINES[vid]:
            erreurs.append(
                DOSSIERS[vid] + "/pulse.json: domaine != " + DOMAINES[vid]
                + " (trouve " + repr(pulse.get("domaine")) + ")"
            )
        met = pulse.get("metriques")
        if not isinstance(met, dict):
            erreurs.append(DOSSIERS[vid] + "/pulse.json: metriques absentes ou non objet")
        else:
            for m in METRIQUES:
                if m not in met:
                    erreurs.append(DOSSIERS[vid] + "/pulse.json: metrique manquante " + m)
                elif met[m] != 0:
                    erreurs.append(
                        DOSSIERS[vid] + "/pulse.json: metrique " + m
                        + " != 0 (trouve " + repr(met[m]) + ")"
                    )
        if pulse.get("statut") != PULSE_STATUT:
            erreurs.append(
                DOSSIERS[vid] + "/pulse.json: statut != " + PULSE_STATUT
                + " (trouve " + repr(pulse.get("statut")) + ")"
            )

    # 6. [v2] historique/ present + snapshots valides
    mois_courant = datetime.now().strftime("%Y-%m")
    hist_dir = os.path.join(BASE, "00_Registre", "historique")
    if not os.path.isdir(hist_dir):
        erreurs.append("00_Registre/historique absent ou non dossier")
    else:
        for vid in VARIANTES:
            nom_fichier = "hist-" + vid + "-" + mois_courant + ".json"
            sp = os.path.join(hist_dir, nom_fichier)
            if not os.path.isfile(sp):
                erreurs.append("historique/" + nom_fichier + " manquant")
                continue
            try:
                with open(sp, "r", encoding="utf-8") as f:
                    snap = json.load(f)
            except (ValueError, OSError) as e:
                erreurs.append("historique/" + nom_fichier + " illisible: " + str(e))
                continue
            if snap.get("variante") != vid:
                erreurs.append(
                    "historique/" + nom_fichier + ": variante != " + vid
                    + " (trouve " + repr(snap.get("variante")) + ")"
                )
            if snap.get("mois") != mois_courant:
                erreurs.append(
                    "historique/" + nom_fichier + ": mois != " + mois_courant
                    + " (trouve " + repr(snap.get("mois")) + ")"
                )
            met = snap.get("metriques")
            if not isinstance(met, dict):
                erreurs.append(
                    "historique/" + nom_fichier + ": metriques absentes ou non objet"
                )
            else:
                for m in METRIQUES:
                    if m not in met:
                        erreurs.append(
                            "historique/" + nom_fichier + ": metrique manquante " + m
                        )
                    elif not isinstance(met[m], (int, float)) or isinstance(met[m], bool):
                        erreurs.append(
                            "historique/" + nom_fichier + ": metrique " + m
                            + " non numerique (trouve " + repr(met[m]) + ")"
                        )
            horo = snap.get("horodatage")
            if not isinstance(horo, str) or not horo:
                erreurs.append(
                    "historique/" + nom_fichier + ": horodatage absent ou vide"
                )

    if erreurs:
        print("PULSE_KO")
        for e in erreurs:
            print("  ERREUR: " + e)
        return 1

    print("PULSE_OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())

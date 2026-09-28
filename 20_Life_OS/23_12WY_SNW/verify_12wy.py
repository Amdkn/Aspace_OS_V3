#!/usr/bin/env python3
# -*- coding: ascii -*-
"""Verifier du framework 12WY Curie SNW (pulse v1, horizons_statut).

Verifications, dans l'ordre numerote :
[1] registre_12wy.json present, JSON valide, version v0, date_init
    2026-09-05, framework "12WY Curie SNW", canon_5_horizons conforme
    (ordre, cles, valeurs exactes) ;
[2] les 3 fichiers sources existent a la racine du framework et sont
    non vides ;
[3] le dossier 05_Execution_Ortegas existe et porte A3_Ortegas_Execution_Spec.md,
    AGENT.md, README.md, SOUL.md non vides ;
[4] la racine du framework porte A2_Curie_SNW_Spec.md non vide ;
[5] chaque horizon du registre declare une valeur source qui existe non
    vide a la racine du framework (coherence registre <-> disque) ;
[6] pulse.json present, JSON valide, objet JSON ;
[7] pulse.json porte exactement les cles de tete version, date_pulse,
    framework, registre_version, horizons_statut (dans cet ordre), avec
    "v1" et registre_version "v0" ;
[8] coherence pulse <-> registre : horizons_statut contient exactement
    5 objets dans l'ordre H1/H3/H10/H30/H90 ; pour chaque objet, horizon
    et source sont identiques a ceux du registre ; source_ok vaut 1 si
    et seulement si le fichier source existe non vide sur le disque au
    moment de la verification (le verifier recalcule, il ne fait pas
    confiance au pulse) ;
[9] date_pulse est une chaine au format YYYY-MM-DD (parseable par
    datetime.strptime avec "%Y-%m-%d").

Ruban : C:/Users/amado/ASpace_OS_V3/00_Amadeus/60_Tape_Specs/2026-09-04-spec-12wy-snw-pulse-v1.md
Sortie : 12WY_OK rc=0 si tout passe, 12WY_KO rc=1 sinon.
"""

import json
import os
import sys
from datetime import datetime

BASE = os.path.dirname(os.path.abspath(__file__))

HORIZONS = {
    "H1": "Vision hebdo",
    "H3": "Anti-paperclip Musk pivot",
    "H10": "Vision et Planning Quarter Intent",
    "H30": "Cycle Q3 2026 mensuel",
    "H90": "Trimestre Q3 vers Cycle 4",
}
OWNERS = {
    "H1": "Book (LD01)",
    "H3": "Saru (LD02)",
    "H10": "Pike + Una",
    "H30": "M'Benga + Chapel + Ortegas",
    "H90": "Chapel (D11 bandwidth)",
}
SOURCES = {
    "H1": "W1_Quarter_Intent_Q3_2026.md",
    "H3": "W1_Quarter_Intent_Q3_2026.md",
    "H10": "W1_Item2_13e_Semaine_Rock_Decomposition.md",
    "H30": "Cycle_Q3_2026_Calendar.md",
    "H90": "W1_Quarter_Intent_Q3_2026.md",
}
FAITS = {
    "H1": "Book LD01 (H1) supervise Saru LD02 (H3) sur Musk pivot (Plan 18.3)",
    "H3": "Q3 Book LD01 supervise Saru LD02 sur Musk pivot; SpaceX 85.7B Greenshoe = anti-pattern, pas modele",
    "H10": "Q3 2026 = Activer le triptyque MORTY (12WY>PARA>DEAL); 13e semaine W13=09/14 et Semaine 0 Cycle 4 W0=09/21 definies par Item 2 verbatim A0",
    "H30": "W2 07/06-07/26 M'Benga items 3-4; W3 07/27-08/16 Chapel items 5-6; W4 08/17-09/07 Ortegas + Chapel items 7-12",
    "H90": "Q3 cible = Life-OS-2026 BETA V2.0 deploye + 36 A3 structures (Plan 21.5); kick-off Cycle 4 = lundi 09/28",
}
CLEES_HORIZON = ["horizon", "nom", "owner", "source", "fait"]
CLEES_REGISTRE = ["version", "date_init", "framework", "canon_5_horizons"]
CLEES_PULSE = ["version", "date_pulse", "framework", "registre_version", "horizons_statut"]
CLEES_STATUT = ["horizon", "source", "source_ok", "trace_hebdo"]
FICHIERS_SOURCES = [
    "W1_Quarter_Intent_Q3_2026.md",
    "W1_Item2_13e_Semaine_Rock_Decomposition.md",
    "Cycle_Q3_2026_Calendar.md",
]
FICHIERS_ORTEGAS = [
    "A3_Ortegas_Execution_Spec.md",
    "AGENT.md",
    "README.md",
    "SOUL.md",
]
ORDRE_HORIZONS = ["H1", "H3", "H10", "H30", "H90"]


def contenu_non_vide(chemin):
    """True si le fichier existe et son contenu strip non vide."""
    try:
        with open(chemin, "r", encoding="utf-8") as f:
            return len(f.read().strip()) != 0
    except OSError:
        return False


def main():
    erreurs = []

    # [1] registre_12wy.json
    chemin_registre = os.path.join(BASE, "registre_12wy.json")
    registre = None
    if not os.path.isfile(chemin_registre):
        erreurs.append("[1] registre_12wy.json absent")
    else:
        try:
            with open(chemin_registre, "r", encoding="utf-8") as f:
                registre = json.load(f)
        except (OSError, ValueError) as e:
            erreurs.append("[1] registre_12wy.json JSON invalide: %s" % e)
    if registre is not None:
        if not isinstance(registre, dict):
            erreurs.append("[1] registre_12wy.json n'est pas un objet JSON")
        else:
            cles = sorted(registre.keys())
            if cles != sorted(CLEES_REGISTRE):
                erreurs.append(
                    "[1] cles de tete attendues %s, mesurees %s"
                    % (sorted(CLEES_REGISTRE), cles)
                )
            if registre.get("version") != "v0":
                erreurs.append("[1] version != v0 (mesure: %r)" % registre.get("version"))
            if registre.get("date_init") != "2026-09-05":
                erreurs.append(
                    "[1] date_init != 2026-09-05 (mesure: %r)" % registre.get("date_init")
                )
            if registre.get("framework") != "12WY Curie SNW":
                erreurs.append(
                    "[1] framework != '12WY Curie SNW' (mesure: %r)" % registre.get("framework")
                )
            canon = registre.get("canon_5_horizons")
            if not isinstance(canon, list) or len(canon) != 5:
                erreurs.append(
                    "[1] canon_5_horizons: liste de 5 attendue (mesure: %r)"
                    % (len(canon) if isinstance(canon, list) else canon)
                )
            else:
                for i, obj in enumerate(canon):
                    h_attendu = ORDRE_HORIZONS[i]
                    if not isinstance(obj, dict):
                        erreurs.append("[1] canon_5_horizons[%d] n'est pas un objet" % i)
                        continue
                    if sorted(obj.keys()) != sorted(CLEES_HORIZON):
                        erreurs.append(
                            "[1] canon_5_horizons[%d] cles attendues %s, mesurees %s"
                            % (i, sorted(CLEES_HORIZON), sorted(obj.keys()))
                        )
                        continue
                    if obj["horizon"] != h_attendu:
                        erreurs.append(
                            "[1] canon_5_horizons[%d].horizon attendu %s, mesure %r"
                            % (i, h_attendu, obj["horizon"])
                        )
                        continue
                    if obj["nom"] != HORIZONS[h_attendu]:
                        erreurs.append(
                            "[1] %s.nom attendu %r, mesure %r"
                            % (h_attendu, HORIZONS[h_attendu], obj["nom"])
                        )
                    if obj["owner"] != OWNERS[h_attendu]:
                        erreurs.append(
                            "[1] %s.owner attendu %r, mesure %r"
                            % (h_attendu, OWNERS[h_attendu], obj["owner"])
                        )
                    if obj["source"] != SOURCES[h_attendu]:
                        erreurs.append(
                            "[1] %s.source attendu %r, mesure %r"
                            % (h_attendu, SOURCES[h_attendu], obj["source"])
                        )
                    if obj["fait"] != FAITS[h_attendu]:
                        erreurs.append(
                            "[1] %s.fait attendu %r, mesure %r"
                            % (h_attendu, FAITS[h_attendu], obj["fait"])
                        )

    # [2] fichiers sources a la racine
    for nom in FICHIERS_SOURCES:
        chemin = os.path.join(BASE, nom)
        if not os.path.isfile(chemin):
            erreurs.append("[2] fichier source absent: %s" % nom)
        elif not contenu_non_vide(chemin):
            erreurs.append("[2] fichier source vide: %s" % nom)

    # [3] dossier 05_Execution_Ortegas
    dossier_ortegas = os.path.join(BASE, "05_Execution_Ortegas")
    if not os.path.isdir(dossier_ortegas):
        erreurs.append("[3] dossier 05_Execution_Ortegas absent")
    else:
        for nom in FICHIERS_ORTEGAS:
            chemin = os.path.join(dossier_ortegas, nom)
            if not os.path.isfile(chemin):
                erreurs.append("[3] fichier Ortegas absent: %s" % nom)
            elif not contenu_non_vide(chemin):
                erreurs.append("[3] fichier Ortegas vide: %s" % nom)

    # [4] spec A2 fait foi
    chemin_spec = os.path.join(BASE, "A2_Curie_SNW_Spec.md")
    if not os.path.isfile(chemin_spec):
        erreurs.append("[4] A2_Curie_SNW_Spec.md absent")
    elif not contenu_non_vide(chemin_spec):
        erreurs.append("[4] A2_Curie_SNW_Spec.md vide")

    # [5] coherence registre <-> disque
    if registre is not None and isinstance(registre, dict):
        canon = registre.get("canon_5_horizons")
        if isinstance(canon, list):
            for obj in canon:
                if not isinstance(obj, dict):
                    continue
                source = obj.get("source")
                if not source:
                    erreurs.append("[5] horizon sans source: %r" % obj.get("horizon"))
                elif not contenu_non_vide(os.path.join(BASE, source)):
                    erreurs.append(
                        "[5] source absente ou vide pour %s: %s" % (obj.get("horizon"), source)
                    )

    # [6] pulse.json : existence, JSON valide, objet JSON
    chemin_pulse = os.path.join(BASE, "pulse.json")
    pulse = None
    if not os.path.isfile(chemin_pulse):
        erreurs.append("[6] pulse.json absent")
    else:
        try:
            with open(chemin_pulse, "r", encoding="utf-8") as f:
                pulse = json.load(f)
        except (OSError, ValueError) as e:
            erreurs.append("[6] pulse.json JSON invalide: %s" % e)
    if pulse is not None and not isinstance(pulse, dict):
        erreurs.append("[6] pulse.json n'est pas un objet JSON")
        pulse = None

    # [7] cles de tete de pulse.json
    if pulse is not None:
        if list(pulse.keys()) != CLEES_PULSE:
            erreurs.append(
                "[7] cles de tete attendues %s (dans cet ordre), mesurees %s"
                % (CLEES_PULSE, list(pulse.keys()))
            )
        if pulse.get("version") != "v1":
            erreurs.append("[7] version != v1 (mesure: %r)" % pulse.get("version"))
        if pulse.get("registre_version") != "v0":
            erreurs.append(
                "[7] registre_version != v0 (mesure: %r)" % pulse.get("registre_version")
            )

    # [8] coherence pulse <-> registre (horizons_statut)
    if pulse is not None:
        hs = pulse.get("horizons_statut")
        canon_reg = (
            registre.get("canon_5_horizons")
            if isinstance(registre, dict)
            else None
        )
        if not isinstance(hs, list) or len(hs) != 5:
            erreurs.append(
                "[8] horizons_statut: liste de 5 attendue (mesure: %r)"
                % (len(hs) if isinstance(hs, list) else hs)
            )
        elif not isinstance(canon_reg, list) or len(canon_reg) != 5:
            erreurs.append("[8] registre canon_5_horizons invalide comme reference")
        else:
            for i, (obj_pulse, obj_reg) in enumerate(zip(hs, canon_reg)):
                if not isinstance(obj_pulse, dict) or not isinstance(obj_reg, dict):
                    erreurs.append(
                        "[8] horizons_statut[%d]: objet JSON attendu (pulse et registre)" % i
                    )
                    continue
                if sorted(obj_pulse.keys()) != sorted(CLEES_STATUT):
                    erreurs.append(
                        "[8] horizons_statut[%d] cles attendues %s, mesurees %s"
                        % (i, sorted(CLEES_STATUT), sorted(obj_pulse.keys()))
                    )
                    continue
                h_attendu = ORDRE_HORIZONS[i]
                if obj_pulse.get("horizon") != h_attendu:
                    erreurs.append(
                        "[8] horizons_statut[%d].horizon attendu %s, mesure %r"
                        % (i, h_attendu, obj_pulse.get("horizon"))
                    )
                    continue
                if obj_pulse.get("horizon") != obj_reg.get("horizon"):
                    erreurs.append(
                        "[8] %s horizon divergent du registre: pulse %r vs registre %r"
                        % (h_attendu, obj_pulse.get("horizon"), obj_reg.get("horizon"))
                    )
                if obj_pulse.get("source") != obj_reg.get("source"):
                    erreurs.append(
                        "[8] %s source divergente du registre: pulse %r vs registre %r"
                        % (h_attendu, obj_pulse.get("source"), obj_reg.get("source"))
                    )
                source = obj_reg.get("source")
                ok_reel = 1 if contenu_non_vide(os.path.join(BASE, source)) else 0
                if obj_pulse.get("source_ok") != ok_reel:
                    erreurs.append(
                        "[8] %s source_ok %r != valeur recalculee %d"
                        % (h_attendu, obj_pulse.get("source_ok"), ok_reel)
                    )
                trace_attendu = "05_Execution_Ortegas" if h_attendu == "H30" else ""
                if obj_pulse.get("trace_hebdo") != trace_attendu:
                    erreurs.append(
                        "[8] %s trace_hebdo attendu %r, mesure %r"
                        % (h_attendu, trace_attendu, obj_pulse.get("trace_hebdo"))
                    )

    # [9] date_pulse au format YYYY-MM-DD
    if pulse is not None:
        dp = pulse.get("date_pulse")
        if not isinstance(dp, str):
            erreurs.append("[9] date_pulse n'est pas une chaine (mesure: %r)" % dp)
        else:
            try:
                datetime.strptime(dp, "%Y-%m-%d")
            except ValueError:
                erreurs.append("[9] date_pulse %r non parseable %%Y-%%m-%%d" % dp)

    if erreurs:
        print("12WY_KO")
        for e in erreurs:
            print(e)
        sys.exit(1)
    print("12WY_OK")
    sys.exit(0)


if __name__ == "__main__":
    main()

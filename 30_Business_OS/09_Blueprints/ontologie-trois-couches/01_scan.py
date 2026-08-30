"""Scanner les noms candidats dans Geordi.

Pour chaque nom, compte les FICHIERS DISTINCTS ou il apparait (word-boundary, case-insensitive).
Stocke jusqu'a 3 chemins d'exemple par nom.

NE PAS modifier Geordi. Lecture seule. Jonctions ecartees.
"""
import os
import stat
import re
import json
import sys
import time
from pathlib import Path

GEORDI = Path("C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi")
RP = getattr(stat, 'FILE_ATTRIBUTE_REPARSE_POINT', 0x400)

# 12 entites Business OS deja connues
ENTITES_BUSINESS = [
    "Organization", "Membership", "Profile", "Client", "Offering",
    "SOP", "Runbook", "Skill", "Agent", "Routine", "Incident", "Persona",
]

# Candidats Life OS (cites dans les cadences et la doctrine)
ENTITES_LIFE = [
    "Ikigai", "Horizon",
    "Domaine", "Projet", "Area", "Ressource", "Archive",
    "Cadence", "Charter", "Objectif", "Semaine", "Contexte", "Occurrence",
]

# Codes horizon (H1/H10/H30/H90)
ENTITES_LIFE_CODES = ["H1", "H10", "H30", "H90"]

TOUS_NOMS = ENTITES_BUSINESS + ENTITES_LIFE + ENTITES_LIFE_CODES

# Classification (pour le JSON)
COUCHE_PAR_NOM = {}
for n in ENTITES_BUSINESS:
    COUCHE_PAR_NOM[n] = "Business OS"
for n in ENTITES_LIFE:
    COUCHE_PAR_NOM[n] = "Life OS"
for n in ENTITES_LIFE_CODES:
    COUCHE_PAR_NOM[n] = "Life OS"


def est_jonction(entry):
    try:
        return bool(entry.stat(follow_symlinks=False).st_file_attributes & RP)
    except (OSError, AttributeError):
        return False


def lister_md(root):
    """Liste tous les .md sans descendre dans les jonctions."""
    fichiers = []
    jonctions = []
    def _walk(d):
        try:
            with os.scandir(d) as it:
                for entry in it:
                    try:
                        if entry.is_file(follow_symlinks=False):
                            if entry.name.lower().endswith('.md'):
                                fichiers.append(entry.path)
                        elif entry.is_dir(follow_symlinks=False):
                            if est_jonction(entry):
                                jonctions.append(entry.path)
                            else:
                                _walk(entry.path)
                    except OSError:
                        pass
        except (PermissionError, OSError):
            pass
    _walk(str(root))
    return fichiers, jonctions


def normaliser_rel(p):
    """Chemin relatif a Geordi pour les exemples."""
    s = str(p).replace("\\", "/")
    if s.startswith(str(GEORDI).replace("\\", "/")):
        return s[len(str(GEORDI).replace("\\", "/")) + 1:]
    return s


def scanner_noms(fichiers, noms, max_octets=512_000):
    """Pour chaque nom, retourne set de chemins ou il apparait + 3 exemples."""
    par_nom = {n: {"chemins": [], "compteur": 0} for n in noms}
    total = len(fichiers)
    erreurs_lecture = 0
    octets_total = 0
    t0 = time.time()
    for i, fp in enumerate(fichiers, 1):
        try:
            size = os.path.getsize(fp)
            if size > max_octets:
                with open(fp, 'r', encoding='utf-8', errors='replace') as f:
                    contenu = f.read(max_octets)
            else:
                with open(fp, 'r', encoding='utf-8', errors='replace') as f:
                    contenu = f.read()
            octets_total += len(contenu)
        except (OSError, UnicodeDecodeError):
            erreurs_lecture += 1
            continue
        for n in noms:
            motif = rf'\b{re.escape(n)}\b'
            if re.search(motif, contenu, re.IGNORECASE):
                par_nom[n]["compteur"] += 1
                if len(par_nom[n]["chemins"]) < 3:
                    par_nom[n]["chemins"].append(normaliser_rel(fp))
        if i % 5000 == 0:
            dt = time.time() - t0
            print(f"  {i:,}/{total:,} fichiers scannes ({dt:.1f}s, ~{i/dt:.0f} f/s, {erreurs_lecture} err)")
    dt = time.time() - t0
    print(f"  Termine : {total:,} fichiers en {dt:.1f}s ({total/max(dt,0.1):.0f} f/s, {octets_total/1e6:.0f} Mo lus, {erreurs_lecture} erreurs)")
    return par_nom


def classer_seuil(compteur):
    if compteur < 3:
        return "<3"
    if compteur <= 4:
        return "3-4"
    return ">=5"


if __name__ == "__main__":
    print(f"== Geordi : {GEORDI}")
    print(f"== Cibles : {len(TOUS_NOMS)} noms")
    print()

    fichiers, jonctions = lister_md(GEORDI)
    print(f"Fichiers .md : {len(fichiers):,}")
    print(f"Jonctions ecartees : {len(jonctions):,}")
    print()

    par_nom = scanner_noms(fichiers, TOUS_NOMS)

    resultats = []
    for n in TOUS_NOMS:
        c = par_nom[n]["compteur"]
        resultats.append({
            "nom": n,
            "fichiers_distincts": c,
            "couche_supposee": COUCHE_PAR_NOM.get(n, "?"),
            "seuil": classer_seuil(c),
            "exemples": par_nom[n]["chemins"],
        })

    # Tri : >=5 d'abord, puis 3-4, puis <3 ; puis par fichiers decroissant
    ordre_seuil = {">=5": 0, "3-4": 1, "<3": 2}
    resultats.sort(key=lambda r: (ordre_seuil[r["seuil"]], -r["fichiers_distincts"], r["nom"]))

    sortie = {
        "geordi_path": str(GEORDI),
        "fichiers_md_total": len(fichiers),
        "jonctions": len(jonctions),
        "noms_scannes": len(TOUS_NOMS),
        "resultats": resultats,
    }

    out_path = Path("entites_observees.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(sortie, f, indent=2, ensure_ascii=False)
    print(f"Resultats ecrits : {out_path}")

    # Apercu console
    print()
    print("== Apercu (>=5 fichiers) ==")
    for r in resultats:
        if r["fichiers_distincts"] >= 5:
            print(f"  {r['nom']:14s} {r['fichiers_distincts']:5d} fichiers  [{r['couche_supposee']}]")
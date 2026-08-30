"""Extraire 20 exemples de relations de finalite depuis Geordi.

Cherche les expressions : 'sert a', 'pour', 'afin de', 'contribue a',
'rattache a', 'au service de', 'repond a', 'vise'.

Pour chaque match, rend la ligne + contexte + chemin:ligne.
"""
import os
import stat
import re
import json
import sys
from pathlib import Path

GEORDI = Path("C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi")
RP = getattr(stat, 'FILE_ATTRIBUTE_REPARSE_POINT', 0x400)

# Patterns : on capture 1 groupe = la phrase de finalite ; on garde
# un peu de contexte autour.
# Liste de regex. Chacun matche une tournure finale.
PATTERNS = [
    re.compile(r"\bsert\s+à\b", re.IGNORECASE),
    re.compile(r"\bafin\s+de\b", re.IGNORECASE),
    re.compile(r"\bcontribue\s+à\b", re.IGNORECASE),
    re.compile(r"\brattachée?\s+à\b", re.IGNORECASE),
    re.compile(r"\bau\s+service\s+de\b", re.IGNORECASE),
    re.compile(r"\brépond\s+à\b", re.IGNORECASE),
    re.compile(r"\bvise\s+à\b", re.IGNORECASE),
    # "pour" et "pour que" -- tres frequent et ambigu. On le prend quand il suit
    # une phrase courte. On va le filtrer au cas par cas.
    re.compile(r"\bpour\b", re.IGNORECASE),
]

# Expressions qui ne sont PAS de la finalite -- bruit a filtrer
BRUIT_POUR = re.compile(
    r"\bpour\s+(?:nous|vous|moi|toi|lui|elle|eux|elles|le|la|les|"
    r"cela|ceci|ça|ce|ma|ta|sa|mes|tes|ses|notre|votre|leur|mes|"
    r"éviter|dire|faire|aller|venir|voir|savoir|comprendre|prendre|"
    r"obtenir|parvenir|réussir|arriver|être|avoir|"
    r"le moment|de l'instant|le reste|le fun|le plaisir|de mieux|"
    r"le fun)\b",
    re.IGNORECASE,
)

OBJECTIF = 20


def est_jonction(entry):
    try:
        return bool(entry.stat(follow_symlinks=False).st_file_attributes & RP)
    except (OSError, AttributeError):
        return False


def lister_md(root):
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
    s = str(p).replace("\\", "/")
    base = str(GEORDI).replace("\\", "/")
    if s.startswith(base):
        return s[len(base) + 1:]
    return s


def trouver_exemples(fichiers, limite=OBJECTIF, max_octets=512_000):
    """Collecte des exemples jusqu'a `limite`. Evite le bruit."""
    exemples = []
    vus_par_phrase = set()  # eviter le meme exemple 50x
    fichiers_scannes = 0
    erreurs = 0
    import time
    t0 = time.time()
    for fp in fichiers:
        if len(exemples) >= limite * 5:  # on en garde plus pour pouvoir trier
            break
        try:
            size = os.path.getsize(fp)
            if size > max_octets:
                with open(fp, 'r', encoding='utf-8', errors='replace') as f:
                    lignes = f.readlines(max_octets)
            else:
                with open(fp, 'r', encoding='utf-8', errors='replace') as f:
                    lignes = f.readlines()
        except (OSError, UnicodeDecodeError):
            erreurs += 1
            continue
        fichiers_scannes += 1
        rel = normaliser_rel(fp)
        for no_ligne, ligne in enumerate(lignes, 1):
            if len(exemples) >= limite * 5:
                break
            for pat in PATTERNS:
                m = pat.search(ligne)
                if not m:
                    continue
                # Filtrer le bruit "pour ..."
                if pat.pattern == "\\bpour\\b":
                    if BRUIT_POUR.search(ligne):
                        continue
                    # "pour" finalite : la phrase doit etre >= 5 mots
                    mots = ligne.split()
                    if len(mots) < 5:
                        continue
                # Eviter doublons
                cle = (rel, no_ligne, m.group(0))
                if cle in vus_par_phrase:
                    continue
                vus_par_phrase.add(cle)
                # Chercher le sujet : la phrase complete (nettoyee)
                phrase = " ".join(ligne.split())
                exemples.append({
                    "fichier": rel,
                    "ligne": no_ligne,
                    "tournure": m.group(0),
                    "phrase": phrase[:300],
                })
        if fichiers_scannes % 10000 == 0:
            dt = time.time() - t0
            print(f"  {fichiers_scannes:,} fichiers scannes, {len(exemples)} exemples ({dt:.1f}s)")
    dt = time.time() - t0
    print(f"  Termine : {fichiers_scannes:,} fichiers, {len(exemples)} exemples, {erreurs} erreurs ({dt:.1f}s)")
    return exemples


if __name__ == "__main__":
    print(f"== Geordi : {GEORDI}")
    fichiers, jonctions = lister_md(GEORDI)
    print(f"Fichiers .md : {len(fichiers):,}")
    print(f"Jonctions ecartees : {len(jonctions):,}")
    print()

    exemples_bruts = trouver_exemples(fichiers, limite=OBJECTIF)

    # Equilibrer les tournures : prendre ~OBJECTIF/nb_tournures par tournure
    par_tournure = {}
    for e in exemples_bruts:
        par_tournure.setdefault(e["tournure"].lower(), []).append(e)

    selection = []
    par_tournure_final = {k: len(v) for k, v in par_tournure.items()}
    print()
    print("== Repartition par tournure ==")
    for t, n in sorted(par_tournure_final.items(), key=lambda x: -x[1]):
        print(f"  {t:25s} {n} exemples")
    print()

    # Selection : prendre 3 par tournure, en privilegiant la diversite
    quotas = {">=5 par tournure": 3}  # nb max par tournure
    for t, lst in par_tournure.items():
        for e in lst[:3]:
            selection.append(e)
        if len(selection) >= OBJECTIF:
            break

    # Si pas assez, on complete avec les autres exemples dans l'ordre
    if len(selection) < OBJECTIF:
        deja = {(e["fichier"], e["ligne"]) for e in selection}
        for e in exemples_bruts:
            if (e["fichier"], e["ligne"]) in deja:
                continue
            selection.append(e)
            if len(selection) >= OBJECTIF:
                break

    selection = selection[:OBJECTIF]

    out_path = Path("finalites_exemples.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump({
            "geordi_path": str(GEORDI),
            "fichiers_md_total": len(fichiers),
            "jonctions": len(jonctions),
            "total_bruts": len(exemples_bruts),
            "par_tournure": par_tournure_final,
            "selection_20": selection,
        }, f, indent=2, ensure_ascii=False)
    print(f"Ecrit : {out_path}")
    print()
    print("== Apercu selection ==")
    for i, e in enumerate(selection, 1):
        print(f"  {i:2d}. [{e['tournure']:12s}] {e['fichier']}:{e['ligne']}")
        print(f"      {e['phrase'][:140]}")
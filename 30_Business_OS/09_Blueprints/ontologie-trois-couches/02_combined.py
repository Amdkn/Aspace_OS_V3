"""Scan combine v3 : finalites + Constitution. Selection corrigee.

Bug fix : chaque exemple stocke sa clef de pattern ('sert_a', 'pour', etc.)
pour eviter la fuite de variable dans la selection.
"""
import os
import stat as stat_mod
import re
import json
import time
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
except Exception:
    pass

GEORDI = Path("C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi")
RP = getattr(stat_mod, 'FILE_ATTRIBUTE_REPARSE_POINT', 0x400)

PATTERNS_FINALITE = [
    ("sert_a", re.compile(r"\bsert\s+à\b", re.IGNORECASE)),
    ("afin_de", re.compile(r"\bafin\s+de\b", re.IGNORECASE)),
    ("contribue_a", re.compile(r"\bcontribue\s+à\b", re.IGNORECASE)),
    ("rattache_a", re.compile(r"\brattachée?\s+à\b", re.IGNORECASE)),
    ("au_service_de", re.compile(r"\bau\s+service\s+de\b", re.IGNORECASE)),
    ("repond_a", re.compile(r"\brépond\s+à\b", re.IGNORECASE)),
    ("vise_a", re.compile(r"\bvise\s+à\b", re.IGNORECASE)),
    ("pour", re.compile(r"\bpour\b", re.IGNORECASE)),
]
BRUIT_POUR = re.compile(
    r"\bpour\s+(?:nous|vous|moi|toi|lui|elle|eux|elles|le|la|les|"
    r"cela|ceci|ça|ce|ma|ta|sa|mes|tes|ses|notre|votre|leur|mes|"
    r"éviter|dire|faire|aller|venir|voir|savoir|comprendre|prendre|"
    r"obtenir|parvenir|réussir|arriver|être|avoir|"
    r"le moment|de l'instant|le reste|le fun|le plaisir|de mieux|"
    r"le fun|moi-même|lui-même|elle-même|eux-mêmes|"
    r"chaque|chacun|tel|telle|un|une|des|"
    r"\d{1,4}/\d{1,4}|le 2026|le 2025)\b",
    re.IGNORECASE,
)
OBJECTIF_FINALITE = 20
QUOTA_PAR_FICHIER = 1
QUOTA_PAR_TOURNURE = 4  # max 4 par tournure pour equilibrage sur 8

RE_CONS_FILENAME = re.compile(r"^CONSTITUTION(?:[_-].*)?\.md$", re.IGNORECASE)
RE_CONSTITUTION = re.compile(r"\bCONSTITUTION\b")
RE_IKIGAI = re.compile(r"\b[Ii]kigai\b")
RE_H1 = re.compile(r"\bH1\b")
RE_H3 = re.compile(r"\bH3\b")
RE_H10 = re.compile(r"\bH10\b")
RE_H30 = re.compile(r"\bH30\b")
RE_H90 = re.compile(r"\bH90\b")
RE_HORIZON = re.compile(r"\b[Hh]orizons?\b")


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


def filtrer_pour(m, ligne):
    if BRUIT_POUR.search(ligne):
        return False
    mots = ligne.split()
    if len(mots) < 6:
        return False
    return True


def main():
    print(f"== Geordi : {GEORDI}", flush=True)
    fichiers, jonctions = lister_md(GEORDI)
    print(f"Total .md : {len(fichiers):,}", flush=True)
    print(f"Jonctions ecartees : {len(jonctions):,}", flush=True)
    print(flush=True)

    fichiers_constitution_nom = []
    compteurs_constitution = 0
    fichiers_contenu_avec_constitution = []
    compteurs_ikigai = 0
    fichiers_avec_ikigai = []
    compteurs_horizons = {"H1": 0, "H3": 0, "H10": 0, "H30": 0, "H90": 0, "Horizon": 0}
    fichiers_avec_horizons = {"H1": [], "H3": [], "H10": [], "H30": [], "H90": [], "Horizon": []}

    par_tournure_l = {}  # clef -> liste d'exemples (avec 'clef' stockee)
    par_clef_total = {k: 0 for k, _ in PATTERNS_FINALITE}
    fichiers_scannes = 0
    erreurs = 0
    octets_total = 0
    t0 = time.time()

    for i, fp in enumerate(fichiers, 1):
        rel = normaliser_rel(fp)
        nom_fichier = os.path.basename(fp)
        if RE_CONS_FILENAME.match(nom_fichier):
            fichiers_constitution_nom.append(rel)
        try:
            size = os.path.getsize(fp)
            if size > 1_000_000:
                with open(fp, 'r', encoding='utf-8', errors='replace') as f:
                    contenu = f.read(1_000_000)
            else:
                with open(fp, 'r', encoding='utf-8', errors='replace') as f:
                    contenu = f.read()
            octets_total += len(contenu)
        except (OSError, UnicodeDecodeError):
            erreurs += 1
            continue
        fichiers_scannes += 1

        if RE_CONSTITUTION.search(contenu):
            compteurs_constitution += 1
            if len(fichiers_contenu_avec_constitution) < 30:
                fichiers_contenu_avec_constitution.append(rel)
        if RE_IKIGAI.search(contenu):
            compteurs_ikigai += 1
            if len(fichiers_avec_ikigai) < 30:
                fichiers_avec_ikigai.append(rel)
        for code, pat in [("H1", RE_H1), ("H3", RE_H3), ("H10", RE_H10),
                          ("H30", RE_H30), ("H90", RE_H90), ("Horizon", RE_HORIZON)]:
            if pat.search(contenu):
                compteurs_horizons[code] += 1
                if len(fichiers_avec_horizons[code]) < 10:
                    fichiers_avec_horizons[code].append(rel)

        try:
            lignes = contenu.split("\n")
        except Exception:
            lignes = []
        for no_ligne, ligne in enumerate(lignes, 1):
            for clef, pat in PATTERNS_FINALITE:
                for m in pat.finditer(ligne):
                    if clef == "pour":
                        if not filtrer_pour(m, ligne):
                            continue
                    par_clef_total[clef] += 1
                    par_tournure_l.setdefault(clef, []).append({
                        "fichier": rel,
                        "ligne": no_ligne,
                        "tournure": m.group(0),
                        "clef": clef,
                        "phrase": " ".join(ligne.split())[:300],
                    })

        if i % 10000 == 0:
            dt = time.time() - t0
            print(f"  {i:,}/{len(fichiers):,} ({dt:.1f}s) -- {sum(par_clef_total.values())} matchs bruts, {erreurs} err", flush=True)

    dt = time.time() - t0
    print(f"  Termine : {fichiers_scannes:,} en {dt:.1f}s, {octets_total/1e6:.0f} Mo, {erreurs} erreurs", flush=True)
    print(flush=True)

    # === SELECTION v3 (corrigée) ===
    # D'abord, on prend non-pour en priorite, 4 max par tournure, 1 par fichier
    selection = []
    fichiers_vus = {}
    par_clef_prises = {k: 0 for k, _ in PATTERNS_FINALITE}

    # Phase 1 : non-pour
    autres_cles = [k for k, _ in PATTERNS_FINALITE if k != "pour"]
    # Round-robin par clef pour equilibrage
    autres_par_clef = {k: par_tournure_l.get(k, []) for k in autres_cles}
    indices = {k: 0 for k in autres_cles}
    while len(selection) < OBJECTIF_FINALITE:
        ajoute = False
        for k in autres_cles:
            if par_clef_prises[k] >= QUOTA_PAR_TOURNURE:
                continue
            lst = autres_par_clef[k]
            # Avance jusqu'a trouver un fichier eligible
            while indices[k] < len(lst):
                e = lst[indices[k]]
                indices[k] += 1
                if fichiers_vus.get(e["fichier"], 0) >= QUOTA_PAR_FICHIER:
                    continue
                selection.append(e)
                fichiers_vus[e["fichier"]] = fichiers_vus.get(e["fichier"], 0) + 1
                par_clef_prises[k] += 1
                ajoute = True
                break
            if len(selection) >= OBJECTIF_FINALITE:
                break
        if not ajoute:
            break  # Plus rien a prendre

    # Phase 2 : "pour" si pas assez
    pour_list = par_tournure_l.get("pour", [])
    idx_pour = 0
    while len(selection) < OBJECTIF_FINALITE and par_clef_prises["pour"] < QUOTA_PAR_TOURNURE:
        ajoute_pour = False
        while idx_pour < len(pour_list):
            e = pour_list[idx_pour]
            idx_pour += 1
            if fichiers_vus.get(e["fichier"], 0) >= QUOTA_PAR_FICHIER:
                continue
            # Filtre qualite : on garde les "pour" dont la phrase a un infinitif
            # apres "pour" -- i.e. structure verbale claire
            # Simplifier : on garde si la phrase contient un verbe a l'infinitif
            # apres "pour"
            phrase = e["phrase"]
            m = re.search(r"\bpour\s+(\w+)", phrase, re.IGNORECASE)
            if not m:
                continue
            mot_apres = m.group(1).lower()
            # Heuristique : les infinitifs francais typiques (terminaisons -er, -ir, -re)
            # OU mot dans une liste de connecteurs finaux
            if (mot_apres.endswith(("er", "ir", "re"))
                or mot_apres in {"que", "qui", "lequel", "laquelle"}):
                selection.append(e)
                fichiers_vus[e["fichier"]] = fichiers_vus.get(e["fichier"], 0) + 1
                par_clef_prises["pour"] += 1
                ajoute_pour = True
                break
        if not ajoute_pour:
            break

    selection = selection[:OBJECTIF_FINALITE]

    # Repartition finale (compte reel de la selection)
    final_par_clef = {}
    for e in selection:
        k = e["clef"]
        final_par_clef[k] = final_par_clef.get(k, 0) + 1

    print("== Repartition finale par tournure (selection) ==", flush=True)
    for k, n in sorted(final_par_clef.items(), key=lambda x: -x[1]):
        print(f"  {k:18s} {n}", flush=True)
    print(flush=True)

    print(f"== Selection {len(selection)}/{OBJECTIF_FINALITE} ==", flush=True)
    for i, e in enumerate(selection, 1):
        print(f"  {i:2d}. [{e['tournure']:14s}] {e['fichier']}:{e['ligne']}", flush=True)
        print(f"      {e['phrase'][:140]}", flush=True)

    # === ECRITURE JSON (AVANT toute operation risquée) ===
    sortie_fin = {
        "geordi_path": str(GEORDI),
        "fichiers_md_total": len(fichiers),
        "jonctions": len(jonctions),
        "fichiers_scannes": fichiers_scannes,
        "erreurs": erreurs,
        "octets_lus": octets_total,
        "selection_20": selection,
        "par_tournure_brut": {k: v for k, v in par_clef_total.items()},
        "par_tournure_total": {k: len(par_tournure_l.get(k, [])) for k, _ in PATTERNS_FINALITE},
    }
    with open("finalites_exemples.json", "w", encoding="utf-8") as f:
        json.dump(sortie_fin, f, indent=2, ensure_ascii=False)
    print(f"Ecrit : finalites_exemples.json", flush=True)

    sortie_ci = {
        "geordi_path": str(GEORDI),
        "fichiers_total": len(fichiers),
        "jonctions": len(jonctions),
        "fichiers_constitution_md_nom": fichiers_constitution_nom,
        "compteur_constitution_mentions": compteurs_constitution,
        "echantillon_fichiers_avec_constitution": fichiers_contenu_avec_constitution,
        "compteur_ikigai": compteurs_ikigai,
        "echantillon_ikigai": fichiers_avec_ikigai,
        "compteurs_horizons": compteurs_horizons,
        "echantillons_horizons": fichiers_avec_horizons,
    }
    with open("constitution_ikigai.json", "w", encoding="utf-8") as f:
        json.dump(sortie_ci, f, indent=2, ensure_ascii=False)
    print(f"Ecrit : constitution_ikigai.json", flush=True)


if __name__ == "__main__":
    main()
"""Localiser CONSTITUTION, Ikigai, Horizons H1/H10/H30/H90 dans Geordi.

Resultat : un JSON listant tous les chemins concernes.
"""
import os
import stat
import re
import json
from pathlib import Path

GEORDI = Path("C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi")
# Chemin mentionne dans le brief
IDENTITY_CORE_CANDIDATE = Path("C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/00_Amadeus/01_Identity_Core")
RP = getattr(stat, 'FILE_ATTRIBUTE_REPARSE_POINT', 0x400)

# Mots-cles a chercher
RECHERCHES = {
    "CONSTITUTION_FILENAME": re.compile(r"^CONSTITUTION(?:[_-].*)?\.md$", re.IGNORECASE),
    "CONSTITUTION_MENTION": re.compile(r"\bCONSTITUTION\b", re.IGNORECASE),
    "IKIGAI_MENTION": re.compile(r"\b[Ikigai]{6}\b", re.IGNORECASE),
    "HORIZON_H1": re.compile(r"\bH1\b"),
    "HORIZON_H10": re.compile(r"\bH10\b"),
    "HORIZON_H30": re.compile(r"\bH30\b"),
    "HORIZON_H90": re.compile(r"\bH90\b"),
    "HORIZON_WORD": re.compile(r"\b[Horizon]{7,8}\b", re.IGNORECASE),
}


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


def main():
    print(f"== Geordi : {GEORDI}")
    fichiers, jonctions = lister_md(GEORDI)
    print(f"Total fichiers : {len(fichiers):,}")
    print(f"Jonctions ecartees : {len(jonctions):,}")
    print()

    # 1. Chercher CONSTITUTION.md par nom de fichier
    fichiers_constitution = []
    for fp in fichiers:
        nom = os.path.basename(fp)
        if RECHERCHES["CONSTITUTION_FILENAME"].match(nom):
            fichiers_constitution.append(normaliser_rel(fp))
    print(f"CONSTITUTION.md (nom) : {len(fichiers_constitution)} fichier(s)")
    for f in fichiers_constitution[:10]:
        print(f"  {f}")
    print()

    # 2. Le dossier 01_Identity_Core existe-t-il ?
    print(f"== Identity Core check ==")
    if IDENTITY_CORE_CANDIDATE.exists():
        print(f"  EXISTE : {IDENTITY_CORE_CANDIDATE}")
        try:
            for entry in os.scandir(str(IDENTITY_CORE_CANDIDATE)):
                print(f"    {entry.name}")
        except (PermissionError, OSError) as e:
            print(f"  err: {e}")
    else:
        print(f"  INTROUVABLE : {IDENTITY_CORE_CANDIDATE}")
    print()

    # 3. Compter les mentions de chaque mot-cle dans Geordi
    print("== Comptage des mentions ==")
    par_clef = {k: [] for k in RECHERCHES.keys() if k != "CONSTITUTION_FILENAME"}
    erreurs = 0
    import time
    t0 = time.time()
    for i, fp in enumerate(fichiers, 1):
        try:
            with open(fp, 'r', encoding='utf-8', errors='replace') as f:
                contenu = f.read(512_000)
        except (OSError, UnicodeDecodeError):
            erreurs += 1
            continue
        rel = normaliser_rel(fp)
        for clef, pat in RECHERCHES.items():
            if clef == "CONSTITUTION_FILENAME":
                continue
            if pat.search(contenu):
                if len(par_clef[clef]) < 10:
                    par_clef[clef].append(rel)
        if i % 10000 == 0:
            dt = time.time() - t0
            print(f"  {i:,}/{len(fichiers):,} ({dt:.1f}s)")
    dt = time.time() - t0
    print(f"  Termine : {len(fichiers):,} en {dt:.1f}s, {erreurs} erreurs")
    print()

    print("== Apercu par mot-cle ==")
    for clef, lst in par_clef.items():
        print(f"  {clef:22s} {len(lst)} exemples trouves :")
        for p in lst[:5]:
            print(f"    - {p}")

    # JSON de sortie
    sortie = {
        "geordi_path": str(GEORDI),
        "fichiers_total": len(fichiers),
        "jonctions": len(jonctions),
        "identity_core_path": str(IDENTITY_CORE_CANDIDATE),
        "identity_core_exists": IDENTITY_CORE_CANDIDATE.exists(),
        "fichiers_constitution_md": fichiers_constitution,
        "mentions_exemples": par_clef,
        "erreurs_lecture": erreurs,
    }
    out_path = Path("constitution_ikigai.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(sortie, f, indent=2, ensure_ascii=False)
    print()
    print(f"Ecrit : {out_path}")


if __name__ == "__main__":
    main()
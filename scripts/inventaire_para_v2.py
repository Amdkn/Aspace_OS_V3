"""Inventaire du PARA de la V2, sans se faire piéger par les jonctions NTFS.

Pourquoi ce script existe. `os.path.islink()` ne voit pas les jonctions NTFS,
et il y en a 47 recensées sur ce disque. Un `os.walk` naïf a déjà compté
13,8 millions de fichiers là où il y en avait 14 613 : il repassait en boucle
par les mêmes dossiers via les liens.

Le seul test fiable sous Windows est l'attribut FILE_ATTRIBUTE_REPARSE_POINT.

Sortie : un JSON sur stdout — total par seau PARA, répartition par extension,
profondeur, et la liste des jonctions écartées (pour qu'on sache ce qui n'a
PAS été compté, au lieu de le découvrir plus tard).
"""

import json
import os
import stat
import sys
from collections import Counter

RP = getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400)

RACINE = r"C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise"

# Les quatre seaux PARA + ce qui traîne à côté.
SEAUX = [
    "01_Projects_Picard",
    "02_Areas_Spock",
    "03_Resources_Geordi",
    "04_Archives_Data",
    "_DRAFTS_PPR_LANE",
    "graphify-out",
    "logs",
]


def est_jonction(entree: os.DirEntry) -> bool:
    """Vrai si l'entrée est un point de reparse (jonction ou lien symbolique)."""
    try:
        return bool(entree.stat(follow_symlinks=False).st_file_attributes & RP)
    except OSError:
        # Un chemin illisible n'est pas une jonction, mais on ne peut pas le
        # parcourir non plus. On le signale plutôt que de le compter à tort.
        return False


def parcourir(racine: str) -> dict:
    fichiers = 0
    dossiers = 0
    extensions: Counter = Counter()
    jonctions: list[str] = []
    illisibles: list[str] = []
    profondeur_max = 0
    octets = 0

    pile = [(racine, 0)]
    while pile:
        chemin, prof = pile.pop()
        profondeur_max = max(profondeur_max, prof)
        try:
            with os.scandir(chemin) as it:
                for e in it:
                    try:
                        if e.is_dir(follow_symlinks=False):
                            if est_jonction(e):
                                jonctions.append(e.path)
                                continue  # NE PAS suivre : c'est le piège
                            dossiers += 1
                            pile.append((e.path, prof + 1))
                        elif e.is_file(follow_symlinks=False):
                            fichiers += 1
                            extensions[os.path.splitext(e.name)[1].lower()] += 1
                            try:
                                octets += e.stat(follow_symlinks=False).st_size
                            except OSError:
                                pass
                    except OSError:
                        illisibles.append(e.path)
        except OSError:
            illisibles.append(chemin)

    return {
        "fichiers": fichiers,
        "dossiers": dossiers,
        "profondeur_max": profondeur_max,
        "megaoctets": round(octets / 1_048_576, 1),
        "top_extensions": extensions.most_common(15),
        "jonctions_ecartees": jonctions,
        "illisibles": illisibles[:20],
        "nb_illisibles": len(illisibles),
    }


def main() -> None:
    rapport = {"racine": RACINE, "seaux": {}}
    total_fichiers = 0

    for seau in SEAUX:
        chemin = os.path.join(RACINE, seau)
        if not os.path.isdir(chemin):
            rapport["seaux"][seau] = {"absent": True}
            continue
        r = parcourir(chemin)
        rapport["seaux"][seau] = r
        total_fichiers += r["fichiers"]
        print(f"[{seau}] {r['fichiers']} fichiers", file=sys.stderr, flush=True)

    rapport["total_fichiers"] = total_fichiers
    print(json.dumps(rapport, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()

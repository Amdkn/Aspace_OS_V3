"""Extrait l'ontologie portee par l'ARBORESCENCE de la V3.

POURQUOI CETTE PASSE EST DIFFERENTE DE LA DISTILLATION V2
La V2 avait 63 260 fichiers .md : aucun agent ne pouvait les lire, d'ou une
extraction scriptee suivie d'une distillation sur echantillon.

La V3 a 953 fichiers .md et 501 dossiers. **Un agent peut lire la carte
entiere.** On ne distille donc pas : on donne la structure complete, et
l'agent la lit.

CE QUE LA STRUCTURE DIT DEJA, SANS LIRE UN SEUL CONTENU
L'utilisateur a reproduit A'Space par l'arborescence : chaque niveau est un
dossier, chaque acteur un fichier a son niveau. Trois choses se lisent donc
mecaniquement :

  - l'imbrication         -> partOf        (20_Life_OS/21_Ikigai_Orville)
  - les codes de rang     -> hasRank       (A1_Beth_Spec.md -> rang A1)
  - les codes de couche   -> operatesLayer (L0, L1, L2)

C'est deja un graphe. Ce que le script NE dit pas : ce que chaque acteur
fait, et pourquoi. Cela demande de lire les fichiers, et c'est le travail de
l'agent.

LE PIEGE DU BRUIT
30_Business_OS porte 2 988 fichiers dont l'immense majorite sont des .png de
captures. Les compter comme entites noierait le signal. On ne retient que les
dossiers et les .md, .json, .yml — ce qui porte de la structure ou du contrat.
"""

import io
import json
import os
import re
import stat
import sys
from collections import Counter

RP = getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400)
V3 = r"C:\Users\amado\ASpace_OS_V3"
SORTIE = os.path.join(V3, "70_Onthologies", "_structure")

# Nos propres bundles ne font pas partie d'A'Space : ils le decrivent.
# Les inclure ferait entrer l'observateur dans l'observe.
SKIP = {
    ".git", "node_modules", "openwiki", ".claude", "__pycache__", ".obsidian",
    "40_Memory_Wiki_OKF", "50_Distillation", "60_Implementation_Méthodologiques",
    "70_Onthologies", "scripts", "dist", "build", ".venv", "venv", ".trunk",
    ".github", "coverage",
}
PORTEURS = {".md", ".json", ".yml", ".yaml"}

RE_CODE = re.compile(r"(?<![A-Za-z0-9])(A[0-3]|B[1-3]|S[1-3]|L[0-2])(?![A-Za-z0-9])")
RE_NUM = re.compile(r"^(\d{2})[_-]")


def jonction(e):
    try:
        return bool(e.stat(follow_symlinks=False).st_file_attributes & RP)
    except OSError:
        return False


def cle(chemin_rel):
    """Identifiant stable et lisible, derive du chemin."""
    s = chemin_rel.replace("\\", "/").lower()
    s = re.sub(r"\.(md|json|ya?ml)$", "", s)
    s = re.sub(r"[^a-z0-9/]+", "-", s).strip("-")
    return s.replace("/", ":")


def main():
    os.makedirs(SORTIE, exist_ok=True)
    noeuds = []          # (rel, type, nom, parent_rel, codes)
    pile = [("", None)]
    while pile:
        rel, parent = pile.pop()
        chemin = os.path.join(V3, rel) if rel else V3
        try:
            entrees = sorted(os.scandir(chemin), key=lambda e: e.name)
        except OSError:
            continue
        for e in entrees:
            try:
                r = os.path.join(rel, e.name) if rel else e.name
                if e.is_dir(follow_symlinks=False):
                    if jonction(e) or e.name in SKIP or e.name.startswith("."):
                        continue
                    noeuds.append((r, "dossier", e.name, parent, RE_CODE.findall(e.name)))
                    pile.append((r, r))
                elif e.is_file(follow_symlinks=False):
                    if os.path.splitext(e.name)[1].lower() not in PORTEURS:
                        continue
                    noeuds.append((r, "fichier", e.name, parent, RE_CODE.findall(e.name)))
            except OSError:
                pass

    # --- Carte lisible d'un trait --------------------------------------
    noeuds.sort(key=lambda n: n[0].replace("\\", "/"))
    lignes = [
        "# Carte structurelle d'A'Space OS V3",
        "",
        "Genere par `scripts/extraire_structure_v3.py`. **Ne pas editer.**",
        "",
        "L'arborescence EST l'ontologie : chaque niveau est un dossier, chaque",
        "acteur un fichier a son niveau. Les codes de rang (`A0`-`A3`, `B1`-`B3`,",
        "`S1`) et de couche (`L0`, `L1`, `L2`) se lisent dans les noms.",
        "",
        "Seuls les dossiers et les fichiers porteurs de structure (`.md`, `.json`,",
        "`.yml`) figurent ici. Les captures d'ecran et binaires sont ecartes.",
        "",
    ]
    for rel, typ, nom, parent, codes in noeuds:
        prof = rel.replace("\\", "/").count("/")
        marque = "/" if typ == "dossier" else ""
        c = f"  `{' '.join(codes)}`" if codes else ""
        lignes.append(f"{'  ' * prof}- {nom}{marque}{c}")

    io.open(os.path.join(SORTIE, "CARTE_V3.md"), "w", encoding="utf-8").write("\n".join(lignes) + "\n")

    # --- Triplets structurels, mecaniques -------------------------------
    t = [
        "# Ontologie structurelle d'A'Space V3 — l'arborescence comme graphe.",
        "# Genere par scripts/extraire_structure_v3.py. NE PAS EDITER A LA MAIN.",
        "#",
        "# Ce fichier dit CE QUI CONTIENT QUOI et QUEL RANG PORTE QUOI.",
        "# Il ne dit pas ce que chaque acteur fait : cela demande de lire les",
        "# fichiers, et c'est le travail de l'agent.",
        "",
        "@prefix aspace: <urn:aspace:ns:> .",
        "@prefix v3:     <urn:aspace:v3:> .",
        "@prefix rdfs:   <http://www.w3.org/2000/01/rdf-schema#> .",
        "",
    ]
    rangs = Counter()
    couches = Counter()
    for rel, typ, nom, parent, codes in noeuds:
        iri = f"urn:aspace:v3:{cle(rel)}"
        t.append(f"<{iri}>")
        t.append(f"    a aspace:{'Dossier' if typ == 'dossier' else 'Fichier'} ;")
        t.append(f'    rdfs:label "{nom}" ;')
        t.append(f'    aspace:chemin "{rel.replace(chr(92), "/")}" ;')
        for c in codes:
            if c.startswith("L"):
                couches[c] += 1
                t.append(f"    aspace:operatesLayer aspace:{c} ;")
            else:
                rangs[c] += 1
                t.append(f"    aspace:hasRank aspace:{c} ;")
        if parent:
            t.append(f"    aspace:partOf <urn:aspace:v3:{cle(parent)}> ;")
        t[-1] = t[-1][:-1] + "."
        t.append("")

    io.open(os.path.join(SORTIE, "aspace-v3-structure.ttl"), "w", encoding="utf-8").write("\n".join(t))

    mesure = {
        "noeuds": len(noeuds),
        "dossiers": sum(1 for n in noeuds if n[1] == "dossier"),
        "fichiers": sum(1 for n in noeuds if n[1] == "fichier"),
        "profondeur_max": max(n[0].replace("\\", "/").count("/") for n in noeuds),
        "rangs": dict(rangs),
        "couches": dict(couches),
        "porteurs_de_code": [n[0].replace("\\", "/") for n in noeuds if n[4]],
    }
    io.open(os.path.join(SORTIE, "structure_mesure.json"), "w", encoding="utf-8").write(
        json.dumps(mesure, ensure_ascii=False, indent=1))

    print(f"{len(noeuds)} noeuds ({mesure['dossiers']} dossiers, {mesure['fichiers']} fichiers)", file=sys.stderr)
    print(f"rangs : {dict(rangs)}", file=sys.stderr)
    print(f"couches : {dict(couches)}", file=sys.stderr)
    print(f"porteurs de code : {len(mesure['porteurs_de_code'])}", file=sys.stderr)


if __name__ == "__main__":
    main()

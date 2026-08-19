"""Substrat et carte des quatre domaines A'Space, source reelle du contenu.

POURQUOI CE SCRIPT EXISTE
La V3 est un squelette : ses dossiers portent la structure, pas le contenu.
Le contenu vit dans la V2, sous
`03_Resources_Geordi/05_From_V2_Domains/`, avec la meme decomposition
fractale — 00_Amadeus, 10_Tech_OS, 20_Life_OS, 30_Business_OS.

LE PIEGE DU VOLUME, DEJA PAYE UNE FOIS
Un premier comptage a rendu 8 888 fichiers .md. C'etait vrai et inutilisable :
les trois quarts sont des artefacts `graphify-burst` et `graphify-out`,
c'est-a-dire des sorties d'outil, pas de la connaissance ecrite. Business_Pulse
a lui seul en portait 4 766.

Hors artefacts, le corpus ecrit a la main tombe a **2 348 fichiers**. C'est ce
chiffre qui commande le decoupage des escouades ; l'autre aurait fait renoncer
a l'exhaustivite sans raison.

CE QUE PRODUIT CE SCRIPT
- un JSONL par couche : une ligne par fichier, avec frontmatter, plan, liens ;
- une carte lisible d'un trait par couche, pour que l'agent sache ou regarder
  avant d'ouvrir quoi que ce soit ;
- un rapport de couverture qui dit ce qui a ete ECARTE et pourquoi.
"""

import io
import json
import os
import re
import stat
import sys
from collections import Counter

RP = getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400)

RACINE = (r"C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise"
          r"\03_Resources_Geordi\05_From_V2_Domains")
SORTIE = r"C:\Users\amado\ASpace_OS_V3\50_Distillation\_substrat_domaines"

COUCHES = ("00_Amadeus", "10_Tech_OS", "20_Life_OS", "30_Business_OS")

# graphify-burst et graphify-out sont des SORTIES D'OUTIL. Les inclure
# noierait le signal sous 6 500 fichiers derives.
BRUIT = {
    "node_modules", ".git", "dist", "build", ".next", ".vercel", "venv",
    ".venv", "__pycache__", ".turbo", "coverage", ".cache",
    "graphify-burst", "graphify-out", "Takeout",
}

RE_H = re.compile(r"^(#{1,6})\s+(.+?)\s*#*$", re.M)
RE_WIKI = re.compile(r"\[\[([^\]\|#]+)")
RE_MD = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")


def jonction(e):
    try:
        return bool(e.stat(follow_symlinks=False).st_file_attributes & RP)
    except OSError:
        return False


def frontmatter(texte):
    if not texte.startswith("---"):
        return {}, texte
    fin = texte.find("\n---", 3)
    if fin == -1:
        return {}, texte
    meta = {}
    for ligne in texte[3:fin].splitlines():
        if ligne.startswith((" ", "\t", "-", "#")) or ":" not in ligne:
            continue
        c, _, v = ligne.partition(":")
        v = v.strip().strip("\"'")
        if v:
            meta[c.strip()] = v[:250]
    return meta, texte[fin + 4:]


def main():
    os.makedirs(SORTIE, exist_ok=True)
    rapport = {"racine": RACINE, "couches": {}, "ecartes": sorted(BRUIT)}

    for couche in COUCHES:
        base = os.path.join(RACINE, couche)
        if not os.path.isdir(base):
            rapport["couches"][couche] = {"absent": True}
            continue

        lignes_jsonl, carte = [], []
        lus = echecs = ecartes = 0
        zones = Counter()

        pile = [(base, 0)]
        vus_dossiers = []
        while pile:
            p, prof = pile.pop()
            try:
                entrees = sorted(os.scandir(p), key=lambda e: e.name)
            except OSError:
                echecs += 1
                continue
            for e in entrees:
                try:
                    rel = os.path.relpath(e.path, base).replace("\\", "/")
                    if e.is_dir(follow_symlinks=False):
                        if jonction(e):
                            continue
                        if e.name in BRUIT:
                            ecartes += 1
                            carte.append(f"{'  ' * prof}- {e.name}/  **[ECARTE : artefact genere]**")
                            continue
                        vus_dossiers.append(rel)
                        carte.append(f"{'  ' * prof}- {e.name}/")
                        pile.append((e.path, prof + 1))
                    elif e.is_file(follow_symlinks=False) and e.name.lower().endswith(".md"):
                        with io.open(e.path, encoding="utf-8", errors="replace") as f:
                            texte = f.read(300_000)
                        meta, corps = frontmatter(texte)
                        titres = RE_H.findall(corps)
                        h1 = next((t for n, t in titres if len(n) == 1), None)
                        zone = rel.split("/")[0] if "/" in rel else "(racine)"
                        zones[zone] += 1
                        lignes_jsonl.append(json.dumps({
                            "id": rel,
                            "couche": couche,
                            "zone": zone,
                            "nom": e.name,
                            "titre": (h1 or meta.get("title") or "")[:180],
                            "fm_cles": sorted(meta.keys()),
                            "type": meta.get("type"),
                            "plan": [t for _, t in titres[:25]],
                            "wikilinks": sorted({w.strip() for w in RE_WIKI.findall(corps)})[:60],
                            "liens": sorted({l for l in RE_MD.findall(corps) if not l.startswith("#")})[:60],
                            "mots": len(corps.split()),
                            "octets": e.stat(follow_symlinks=False).st_size,
                        }, ensure_ascii=False))
                        titre = f"  — {h1[:70]}" if h1 else ""
                        carte.append(f"{'  ' * prof}- {e.name}{titre}")
                        lus += 1
                except OSError:
                    echecs += 1

        with io.open(os.path.join(SORTIE, f"{couche}.jsonl"), "w", encoding="utf-8") as f:
            f.write("\n".join(lignes_jsonl) + "\n")

        entete = [
            f"# Carte du domaine {couche}",
            "",
            f"Genere par `scripts/substrat_domaines_v2.py`. **Ne pas editer.**",
            "",
            f"**{lus} fichiers `.md` ecrits a la main**, {ecartes} dossiers d'artefacts ecartes.",
            "",
            "Zones : " + " · ".join(f"`{z}` {n}" for z, n in zones.most_common(8)),
            "",
        ]
        with io.open(os.path.join(SORTIE, f"CARTE_{couche}.md"), "w", encoding="utf-8") as f:
            f.write("\n".join(entete + carte) + "\n")

        rapport["couches"][couche] = {
            "lus": lus, "echecs": echecs, "dossiers_artefacts_ecartes": ecartes,
            "dossiers": len(vus_dossiers), "zones": zones.most_common(12),
        }
        print(f"[{couche}] {lus} lus, {ecartes} dossiers ecartes, {echecs} echecs",
              file=sys.stderr, flush=True)

    rapport["total_lus"] = sum(c.get("lus", 0) for c in rapport["couches"].values())
    with io.open(os.path.join(SORTIE, "_couverture.json"), "w", encoding="utf-8") as f:
        json.dump(rapport, f, ensure_ascii=False, indent=1)
    print(f"TOTAL {rapport['total_lus']} fichiers", file=sys.stderr)


if __name__ == "__main__":
    main()

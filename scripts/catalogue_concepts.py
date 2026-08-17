"""Catalogue compact des concepts distilles — l'entree de la passe de liaison.

POURQUOI CE SCRIPT EXISTE
Le graphe n'a aucune arete transversale : les 129 relations sont toutes
internes a un bundle, et quatre bundles n'ont aucune relation. La cause est
connue — chaque agent a travaille dans un perimetre exclusif et ne pouvait
donc pas lier vers un concept qu'un voisin ecrivait au meme moment.

Pour reparer, il faut qu'un agent unique voie **les 102 concepts a la fois**.
Lui faire ouvrir 102 fichiers gaspillerait son budget en lecture ; ce
catalogue lui donne, par concept, le strict necessaire pour decider d'un lien :
identifiant, bundle, type, titre, description, tags.

Sortie : un Markdown lisible d'un trait, groupe par bundle.
"""

import io
import os
import re

V3 = r"C:\Users\amado\ASpace_OS_V3"
BUNDLES = [
    ("50_Distillation", ["areas", "projets", "archives", "ressources", "ontologie"]),
    ("60_Implementation_Méthodologiques", ["prompt-systeme", "autonomie-agents"]),
]
SORTIE = os.path.join(V3, "50_Distillation", "ontologie", "CATALOGUE.md")


def frontmatter(texte):
    if not texte.startswith("---"):
        return {}
    fin = texte.find("\n---", 3)
    if fin == -1:
        return {}
    meta = {}
    for ligne in texte[3:fin].splitlines():
        if ligne.startswith((" ", "\t", "-")) or ":" not in ligne:
            continue
        c, _, v = ligne.partition(":")
        v = v.strip().strip("\"'")
        if v:
            meta[c.strip()] = v
    return meta


def main():
    lignes = [
        "# Catalogue des concepts distilles",
        "",
        "Genere par `scripts/catalogue_concepts.py`. Une ligne par concept.",
        "L'identifiant est celui du graphe : `urn:aspace:concept:<bundle>:<slug>`.",
        "",
    ]
    total = 0
    for racine, sous in BUNDLES:
        for sb in sous:
            d = os.path.join(V3, racine, sb)
            if not os.path.isdir(d):
                continue
            fichiers = [n for n in sorted(os.listdir(d))
                        if n.endswith(".md") and n != "index.md"]
            if not fichiers:
                continue
            lignes.append(f"## {sb} — {len(fichiers)} concepts")
            lignes.append("")
            for nom in fichiers:
                with io.open(os.path.join(d, nom), encoding="utf-8", errors="replace") as f:
                    m = frontmatter(f.read())
                slug = nom[:-3]
                titre = m.get("title", slug)
                desc = re.sub(r"\s+", " ", m.get("description", ""))[:230]
                ty = m.get("type", "?")
                tags = m.get("tags", "")
                lignes.append(f"- **`{slug}`** · _{ty}_ — {titre}")
                if desc:
                    lignes.append(f"  - {desc}")
                if tags:
                    lignes.append(f"  - tags : {tags}")
                total += 1
            lignes.append("")

    lignes.insert(4, f"**{total} concepts au total.**")
    lignes.insert(5, "")
    with io.open(SORTIE, "w", encoding="utf-8") as f:
        f.write("\n".join(lignes))
    print(f"{total} concepts -> {SORTIE}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Remplit 70_Onthologies/verbes/ depuis les triplets REELS.

POURQUOI CE SCRIPT EXISTE
    `verbes/` etait vide -- lacune assumee de l'ontologie. ONTOLOGIE_V2 dit
    que le corpus porte 533 verbes distincts, regroupes en quatre familles :
    Autorite, Flux, Routage, Structure. Ils sont DECRITS dans un document et
    n'existent nulle part comme donnee.

LA REGLE QUI COMMANDE
    « ONTOLOGIE_V1 proposait un verbe `sert` comme l'axe qui manquait. Il ne
    manquait pas. » V1 a echoue en INVENTANT ses verbes. Ce script n'invente
    rien : il lit les predicats des .ttl et compte. Un verbe absent du corpus
    n'entre pas, meme s'il serait utile.
"""

from __future__ import annotations
import collections
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

V3 = Path("C:/Users/amado/ASpace_OS_V3")
ONTO = V3 / "70_Onthologies"
SORTIE = ONTO / "verbes"

# Les quatre familles de ONTOLOGIE_V2 §3, telles qu'ecrites. On ne les
# reinvente pas : on les cite, et on classe les verbes MESURES dedans.
#
# CORRECTION DU 2026-08-30 : la premiere version ne cherchait que des racines
# francaises (`gouvern`, `produ`, `contien`) sur des predicats ecrits en
# anglais (`governs`, `stewards`, `dependsOn`). 72 des 85 verbes tombaient
# « hors familles » -- la taxonomie semblait fausse alors que c'etait la sonde.
FAMILLES = {
    "autorite": ("Autorité — qui commande",
                 ["own", "govern", "steward", "supervis", "delegab", "overrid",
                  "veto", "forbid", "exige", "stipule", "approuv", "valid",
                  "gouvern", "arbitr", "authoriz", "mandat", "ratifi",
                  "accountab", "responsib", "decid", "escalat"]),
    "flux": ("Flux — ce qui circule",
             ["produ", "livr", "deliver", "fourni", "suppl", "vend", "sell",
              "consomm", "consum", "fed", "feed", "cascade", "aliment", "emit",
              "emet", "recoit", "receiv", "transmet", "generat", "output",
              "input", "publish"]),
    "routage": ("Routage — où ça va",
                ["rout", "orchestr", "trigger", "mappe", "map", "cover",
                 "ancre", "anchor", "dirig", "direct", "renvoi", "pointe",
                 "handl", "dispatch", "target", "reference", "cite", "link"]),
    "structure": ("Structure — ce qui compose",
                  ["extend", "contien", "contain", "requir", "sister",
                   "compos", "herit", "inherit", "appartien", "partof",
                   "part_of", "belong", "inclut", "includ", "depend",
                   "instantiat", "implement", "supersed", "pair", "member",
                   "has", "subclass", "define", "specifi"]),
}


def predicats() -> collections.Counter:
    """Les predicats reellement presents dans les .ttl du corpus."""
    cpt: collections.Counter = collections.Counter()
    for f in ONTO.rglob("*.ttl"):
        try:
            t = f.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        # DEFAUT PAYE LE 2026-08-30 : un motif trop large capturait les lignes
        # de COMMENTAIRE (« # Rick Sanchez gouverne… »), rendant 897 « verbes »
        # dont 883 hors taxonomie. Une extraction qui prend du texte pour des
        # predicats produit une ontologie de bruit.
        #
        # La forme reelle est stricte : <urn:...> prefixe:predicat <urn:...> .
        for ligne in t.split("\n"):
            ligne = ligne.strip()
            if not ligne or ligne.startswith(("#", "@")):
                continue
            m = re.match(r"<[^>]+>\s+(?:([a-zA-Z][\w-]*):)?([\w-]+)\s+", ligne)
            if not m:
                continue
            p = m.group(2)
            if p in ("a", "type"):     # `a` est le raccourci de rdf:type
                continue
            cpt[p] += 1
    return cpt


def classer(verbe: str) -> str | None:
    # `partOf` vs motif `partof` : normaliser des deux cotes, sinon la sonde
    # rate ce qu'elle cherche (meme famille que les accents et LinkType).
    v = verbe.lower().replace("_", "")
    for cle, (_, motifs) in FAMILLES.items():
        if any(m in v for m in motifs):
            return cle
    return None


def main() -> int:
    cpt = predicats()
    if not cpt:
        print(f"  aucun .ttl exploitable sous {ONTO}")
        return 1

    par_famille: dict[str, list[tuple[str, int]]] = {k: [] for k in FAMILLES}
    non_classes: list[tuple[str, int]] = []
    for v, n in cpt.most_common():
        f = classer(v)
        (par_famille[f] if f else non_classes).append((v, n))

    SORTIE.mkdir(parents=True, exist_ok=True)
    quand = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    ecrits = []

    for cle, (titre, _) in FAMILLES.items():
        items = par_famille[cle]
        L = [
            "---",
            "type: Ontology",
            f"title: Verbes — {titre}",
            f"description: Les prédicats de la famille « {cle} » réellement "
            f"attestés dans les triplets du corpus.",
            f"tags: [ontologie, verbes, {cle}, rdf]",
            f"generated: {{ by: scripts/extraire_verbes.py, at: {quand} }}",
            "verified:",
            f"  - {{ by: scripts/extraire_verbes.py, at: {quand} }}",
            "sources:",
            "  - id: ontologie-v2",
            "    resource: 00_Amadeus/30_MEMORY_CORE/ONTOLOGIE_V2.md",
            "    title: §3 — les quatre familles de verbes",
            f"    last_modified: {quand}",
            "  - id: triplets",
            "    resource: 70_Onthologies/**/*.ttl",
            f"    title: Les prédicats mesurés ({len(cpt)} distincts)",
            f"    last_modified: {quand}",
            'okf_version: "0.2"',
            "---",
            "",
            f"# {titre}",
            "",
            f"**{len(items)} prédicats** de cette famille, attestés dans les "
            "triplets du corpus.",
            "",
            "> **Extrait, jamais inventé.** `ONTOLOGIE_V1` a échoué en proposant",
            "> un verbe `sert` « qui manquait » — il ne manquait pas. Ce fichier",
            "> est régénéré par `scripts/extraire_verbes.py` : un verbe absent",
            "> du corpus n'y entre pas, même s'il serait utile.",
            "",
        ]
        if items:
            L += ["| Verbe | Occurrences |", "|---|---:|"]
            L += [f"| `{v}` | {n} |" for v, n in items]
        else:
            L.append("**Aucun prédicat mesuré dans cette famille.** "
                     "L'absence est une information : la famille est décrite "
                     "dans `ONTOLOGIE_V2` mais rien ne l'atteste encore.")
        L += ["", "## Comment vérifier", "",
              "```bash",
              "python C:/Users/amado/ASpace_OS_V3/scripts/extraire_verbes.py",
              "```", ""]

        f = SORTIE / f"{cle}.md"
        f.write_text("\n".join(L), encoding="utf-8")
        ecrits.append((cle, len(items)))

    # Les non classes ne sont pas du bruit : ce sont les verbes que les quatre
    # familles de V2 ne couvrent pas. Les taire ferait croire a une taxonomie
    # complete.
    L = [
        "---", "type: Ontology",
        "title: Verbes — hors des quatre familles",
        "description: Prédicats attestés que la taxonomie d'ONTOLOGIE_V2 §3 ne "
        "couvre pas. Leur existence dit que la taxonomie est incomplète.",
        "tags: [ontologie, verbes, lacune, rdf]",
        f"generated: {{ by: scripts/extraire_verbes.py, at: {quand} }}",
        "verified:", f"  - {{ by: scripts/extraire_verbes.py, at: {quand} }}",
        "sources:", "  - id: triplets",
        "    resource: 70_Onthologies/**/*.ttl",
        "    title: Les prédicats mesurés", f"    last_modified: {quand}",
        'okf_version: "0.2"', "---", "",
        "# Verbes hors des quatre familles", "",
        f"**{len(non_classes)} prédicats** attestés dans le corpus que les "
        "familles *Autorité / Flux / Routage / Structure* ne couvrent pas.",
        "",
        "Ce fichier n'est pas une décharge : c'est **la mesure de ce que la "
        "taxonomie ne dit pas encore**. Une ontologie qui range tout dans "
        "quatre cases sans reste ment sur sa propre couverture.",
        "",
    ]
    if non_classes:
        L += ["| Verbe | Occurrences |", "|---|---:|"]
        L += [f"| `{v}` | {n} |" for v, n in non_classes[:80]]
        if len(non_classes) > 80:
            L.append(f"\n*(+{len(non_classes) - 80} autres, voir le script)*")
    (SORTIE / "hors-familles.md").write_text("\n".join(L) + "\n", encoding="utf-8")

    # L'index du sous-bundle : sans lui, ces fichiers sont inatteignables (P3).
    idx = ["# Verbes", "",
           f"Les prédicats du corpus, extraits des `.ttl` le {quand}. "
           f"**{len(cpt)} distincts**, {sum(cpt.values())} occurrences.", "",
           "# Files", ""]
    for cle, n in ecrits:
        idx.append(f"- [{FAMILLES[cle][0]}]({cle}.md) — {n} prédicats")
    idx.append(f"- [Hors des quatre familles](hors-familles.md) — "
               f"{len(non_classes)} prédicats non couverts")
    idx += ["", "Régénérer : `python scripts/extraire_verbes.py`", ""]
    (SORTIE / "index.md").write_text("\n".join(idx), encoding="utf-8")

    print(f"  {len(cpt)} predicats distincts, {sum(cpt.values())} occurrences")
    for cle, n in ecrits:
        print(f"    {n:>4}  {cle}.md")
    print(f"    {len(non_classes):>4}  hors-familles.md")
    print(f"  ecrit dans {SORTIE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

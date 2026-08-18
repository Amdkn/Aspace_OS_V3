"""Valide les triplets des trois couches et genere le graphe d'A'Space.

POURQUOI CE SCRIPT DECIDE, ET PAS LES AGENTS
Trois agents ecrivent en parallele, chacun dans son fichier. Ce script fusionne
et refuse ce qu'il ne peut pas verifier. Les agents proposent ; le graphe
n'accepte que ce qui tient.

CE QU'IL REFUSE
- une assertion sans `source` : la regle du poste est qu'une entree sans source
  est une invention. Elle est appliquee ici, pas laissee a la bonne volonte ;
- une source qui ne designe aucun fichier reel de la distillation : une source
  inventee est pire qu'une source absente, parce qu'elle rassure ;
- un triplet reflexif (sujet == objet) : ne repond a aucune question ;
- un doublon exact.

CE QU'IL NE REFUSE PAS, ET QUI SE COMPTE
Un verbe neuf. Le brief autorise les agents a en proposer, a condition qu'il
serve au moins trois fois. Le script ne tranche pas — il compte, et signale
ceux qui servent une ou deux fois. C'est un signalement, pas un rejet : la
regle des trois occurrences se juge une fois toutes les couches rendues.
"""

import io
import json
import os
import re
import sys
from collections import Counter, defaultdict

V3 = r"C:\Users\amado\ASpace_OS_V3"
D = os.path.join(V3, "70_Onthologies")
DIST = os.path.join(V3, "50_Distillation")
COUCHES = ("tech", "life", "business")
COUCHES_V3 = ("v3-amadeus", "v3-tech", "v3-life", "v3-business")

VERBES_SCHEMA = {
    "governs", "partOf", "dependsOn", "appliesTo", "refines", "instantiates",
    "pairedWith", "handledBy", "cites", "supersedes", "seeAlso",
}


def sources_reelles():
    """Les chemins qui existent vraiment — concepts distilles ET arborescence V3.

    Les deux passes n'ont pas la meme source : la premiere cite des concepts
    de 50_Distillation, la seconde des fichiers de l'arborescence V3. Le
    validateur doit connaitre les deux, sinon il rejetterait comme
    inexistante une source parfaitement reelle."""
    out = set()
    for base, _, fichiers in os.walk(V3):
        rel = os.path.relpath(base, V3).replace("\\", "/")
        if rel.startswith((".git", "node_modules", "openwiki", ".obsidian")):
            continue
        for n in fichiers:
            out.add(f"{rel}/{n}" if rel != "." else n)
    for sb in ("areas", "projets", "archives", "ressources", "ontologie"):
        d = os.path.join(DIST, sb)
        if not os.path.isdir(d):
            continue
        for n in os.listdir(d):
            if n.endswith(".md"):
                out.add(f"{sb}/{n}")
                out.add(n)
    return out


def cle(s):
    return re.sub(r"[^a-z0-9-]", "-", str(s).strip().lower()).strip("-")


def echapper(s):
    return str(s).replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ").strip()


def main():
    reelles = sources_reelles()
    acceptes, refus, exemples = [], Counter(), []
    vus = set()
    par_couche = Counter()

    for couche in COUCHES:
        chemin = os.path.join(D, "triplets", f"{couche}.jsonl")
        if not os.path.exists(chemin):
            print(f"absent : {couche}.jsonl", file=sys.stderr)
            continue
        for num, ligne in enumerate(io.open(chemin, encoding="utf-8"), 1):
            ligne = ligne.strip()
            if not ligne or ligne.startswith("#"):
                continue
            try:
                r = json.loads(ligne)
            except json.JSONDecodeError as e:
                refus["json invalide"] += 1
                exemples.append((couche, num, "json", str(e)[:50])); continue

            s, v, o = cle(r.get("sujet", "")), str(r.get("verbe", "")).strip(), r.get("objet", "")
            src = str(r.get("source", "")).strip()
            typ = r.get("objet_type", "entite")

            if not s or not v or o in (None, ""):
                refus["triplet incomplet"] += 1
                exemples.append((couche, num, "incomplet", f"{s}|{v}")); continue
            if not src:
                refus["SANS SOURCE"] += 1
                exemples.append((couche, num, "sans source", f"{s} {v}")); continue
            base = src.split("#")[0].strip().lstrip("./")
            if base not in reelles and os.path.basename(base) not in reelles:
                refus["source inexistante"] += 1
                exemples.append((couche, num, "source inexistante", base[:60])); continue
            if typ == "entite" and cle(o) == s:
                refus["reflexif"] += 1
                exemples.append((couche, num, "reflexif", s)); continue

            k = (s, v, cle(o) if typ == "entite" else str(o)[:80])
            if k in vus:
                refus["doublon"] += 1; continue
            vus.add(k)

            r["_sujet"], r["_verbe"], r["_couche"] = s, v, couche
            acceptes.append(r)
            par_couche[couche] += 1

    # --- Turtle ---------------------------------------------------------
    t = ["# A'Space OS reconstitue en triplets — genere par",
         "# scripts/valider_triplets_aspace.py. NE PAS EDITER A LA MAIN.",
         "",
         "@prefix aspace: <urn:aspace:ns:> .",
         "@prefix ent:    <urn:aspace:entity:> .",
         ""]
    for r in acceptes:
        s = f"<urn:aspace:entity:{r['_sujet']}>"
        if r.get("objet_type") == "litteral":
            o = f'"{echapper(r["objet"])}"'
        else:
            o = f"<urn:aspace:entity:{cle(r['objet'])}>"
        t.append(f"{s} aspace:{r['_verbe']} {o} .")
        t.append(f"#   {echapper(r.get('phrase', ''))[:150]}")
        t.append(f"#   src: {echapper(r.get('source', ''))} [{r.get('confiance', 'moyenne')}] ({r['_couche']})")

    io.open(os.path.join(D, "triplets", "aspace-os.ttl"), "w", encoding="utf-8").write("\n".join(t) + "\n")

    # --- Rapport --------------------------------------------------------
    verbes = Counter(r["_verbe"] for r in acceptes)
    neufs = {v: n for v, n in verbes.items() if v not in VERBES_SCHEMA}
    sujets = Counter(r["_sujet"] for r in acceptes)

    print(f"ACCEPTES : {len(acceptes)}")
    print(f"REFUSES  : {sum(refus.values())}")
    for k, n in refus.most_common():
        print(f"   {n:>4}  {k}")
    for c, num, k, d_ in exemples[:12]:
        print(f"      {c}:{num} — {k} — {d_}")

    print("\nPAR COUCHE :", dict(par_couche))
    print(f"\nSUJETS DISTINCTS : {len(sujets)}")
    for s, n in sujets.most_common(12):
        print(f"   {n:>4}  {s}")
    print(f"\nVERBES : {len(verbes)} distincts, dont {len(neufs)} hors schema")
    for v, n in verbes.most_common():
        marque = "  <- neuf" if v in neufs else ""
        print(f"   {n:>4}  {v}{marque}")
    faibles = [v for v, n in neufs.items() if n < 3]
    if faibles:
        print(f"\nVERBES NEUFS SERVANT MOINS DE 3 FOIS (a trancher, non rejetes) : {faibles}")
    print(f"\n-> {os.path.join(D, 'triplets', 'aspace-os.ttl')}")


if __name__ == "__main__":
    main()

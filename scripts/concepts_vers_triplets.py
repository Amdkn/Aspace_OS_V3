"""Convertit les concepts OKF de la distillation en triplets RDF (Turtle).

POURQUOI CE SCRIPT EXISTE
Le frontmatter OKF est deja un ensemble de triplets qui s'ignore : le fichier
est le sujet, chaque cle est un predicat, chaque valeur un objet. La conversion
est donc mecanique, et n'a aucune raison de couter un appel de modele.

Ce qui reste au travail semantique — nommer les classes, hierarchiser les
types, decider quelles relations meritent un predicat propre — se fait ENSUITE,
sur ce que ce script mesure.

CHOIX D'ESPACE DE NOMS
On utilise des URN (`urn:aspace:...`) et non des IRI HTTP. Inventer
`https://aspace-os.org/ns#` reviendrait a s'approprier un domaine qui
appartient peut-etre a un tiers, et a poser une adresse qui ne resout pas.
C'est exactement le piege `placeholder.invalid` (TLD reserve, RFC 2606) deja
paye sur le SaaS Builder. Un URN est un identifiant, pas une adresse : il ne
promet aucune resolution, donc il ne ment pas.

Si un jour un domaine reel est acquis, la substitution est un sed sur le
prefixe. C'est reversible ; une fausse adresse publiee ne l'est pas.

NIVEAU DE CONFIANCE
Le champ `verified` d'OKF v0.2 se traduit en triplet, mecaniquement :
  absent                        -> aspace:nonVerifie
  acteurs non-human uniquement  -> aspace:confirmeMachine
  au moins un human:<id>        -> aspace:revuHumain
C'est la distinction qui fait tout l'interet du format ; elle doit survivre au
passage en RDF, sinon le graphe melange le mesure et le suppose.
"""

import io
import json
import os
import re
import sys
from collections import Counter
from datetime import datetime, timezone

V3 = r"C:\Users\amado\ASpace_OS_V3"
BUNDLES = [
    ("50_Distillation", ["areas", "projets", "archives", "ressources", "ontologie"]),
    ("60_Implementation_Méthodologiques", ["prompt-systeme", "autonomie-agents"]),
]
SORTIE = os.path.join(V3, "50_Distillation", "ontologie")

RE_WIKI = re.compile(r"\[\[([^\]\|#]+)")
RE_MDLINK = re.compile(r"\]\(([A-Za-z0-9_./-]+\.md)\)")


def lire_frontmatter(texte):
    """Parse le frontmatter OKF. Les listes `sources` et `verified` sont
    reconstruites a la main : pas de dependance YAML, et on ne veut pas
    interpreter de travers ce qu'on ne comprend pas."""
    if not texte.startswith("---"):
        return {}, texte
    fin = texte.find("\n---", 3)
    if fin == -1:
        return {}, texte
    bloc = texte[3:fin]
    meta, cle_courante = {}, None
    for ligne in bloc.splitlines():
        if not ligne.strip():
            continue
        if not ligne.startswith((" ", "\t", "-")) and ":" in ligne:
            cle, _, val = ligne.partition(":")
            cle, val = cle.strip(), val.strip()
            if val:
                meta[cle] = val.strip("\"'")
                cle_courante = None
            else:
                meta[cle] = []
                cle_courante = cle
        elif cle_courante and ligne.strip().startswith("-"):
            meta[cle_courante].append(ligne.strip()[1:].strip())
        elif cle_courante and isinstance(meta.get(cle_courante), list) and meta[cle_courante]:
            meta[cle_courante][-1] += " " + ligne.strip()
    return meta, texte[fin + 4:]


def acteurs(valeurs):
    """Extrait les `by:` d'une liste d'entrees `{ by: X, at: Y }`."""
    out = []
    for v in valeurs or []:
        m = re.search(r"by\s*:\s*([^,}\s]+)", v)
        if m:
            out.append(m.group(1).strip().strip("\"'"))
    return out


def niveau_confiance(meta):
    v = meta.get("verified")
    if isinstance(v, str) and v:
        v = [v]
    a = acteurs(v if isinstance(v, list) else [])
    if not a:
        return "nonVerifie"
    if any(x.startswith("human:") for x in a):
        return "revuHumain"
    return "confirmeMachine"


def echapper(s):
    return (s.replace("\\", "\\\\").replace('"', '\\"')
             .replace("\n", " ").replace("\r", " ").strip())


def liste_tags(brut):
    if not brut:
        return []
    return [t.strip() for t in str(brut).strip("[]").split(",") if t.strip()]


def main():
    os.makedirs(SORTIE, exist_ok=True)
    concepts, index_slug = [], {}

    for racine, sous in BUNDLES:
        for sb in sous:
            d = os.path.join(V3, racine, sb)
            if not os.path.isdir(d):
                continue
            for nom in sorted(os.listdir(d)):
                if not nom.endswith(".md") or nom == "index.md":
                    continue
                chemin = os.path.join(d, nom)
                with io.open(chemin, encoding="utf-8", errors="replace") as f:
                    texte = f.read()
                meta, corps = lire_frontmatter(texte)
                slug = nom[:-3]
                iri = f"urn:aspace:concept:{sb}:{slug}"
                index_slug[slug] = iri
                concepts.append({
                    "iri": iri, "slug": slug, "bundle": sb, "racine": racine,
                    "meta": meta, "corps": corps, "chemin": os.path.relpath(chemin, V3),
                })

    # --- Turtle ---------------------------------------------------------
    t = []
    w = t.append
    w("# Ontologie A'Space OS — instances, generees depuis les concepts OKF.")
    w("# Genere par scripts/concepts_vers_triplets.py — NE PAS EDITER A LA MAIN.")
    w(f"# Genere le {datetime.now(timezone.utc).isoformat()}")
    w("")
    w("@prefix aspace:  <urn:aspace:ns:> .")
    w("@prefix concept: <urn:aspace:concept:> .")
    w("@prefix kind:    <urn:aspace:kind:> .")
    w("@prefix dcterms: <http://purl.org/dc/terms/> .")
    w("@prefix rdfs:    <http://www.w3.org/2000/01/rdf-schema#> .")
    w("@prefix xsd:     <http://www.w3.org/2001/XMLSchema#> .")
    w("")

    stats = Counter()
    types_vus, tags_vus, predicats_vus = Counter(), Counter(), Counter()
    relations = 0
    liens_morts = []

    for c in concepts:
        m, w_ = c["meta"], w
        w_(f"<{c['iri']}>")
        w_("    a aspace:Concept ;")
        w_(f"    aspace:bundle \"{echapper(c['bundle'])}\" ;")
        w_(f"    aspace:fichier \"{echapper(c['chemin']).replace(chr(92), chr(47))}\" ;")

        if m.get("type"):
            ty = re.sub(r"[^A-Za-z0-9]", "", m["type"].title())
            types_vus[m["type"]] += 1
            w_(f"    aspace:kind kind:{ty} ;")
        if m.get("title"):
            w_(f"    dcterms:title \"{echapper(m['title'])}\" ;")
        if m.get("description"):
            w_(f"    dcterms:description \"{echapper(m['description'])}\" ;")
        if m.get("okf_version"):
            w_(f"    aspace:okfVersion \"{echapper(m['okf_version'])}\" ;")

        for tag in liste_tags(m.get("tags")):
            tags_vus[tag] += 1
            w_(f"    aspace:tag \"{echapper(tag)}\" ;")

        niveau = niveau_confiance(m)
        stats[niveau] += 1
        w_(f"    aspace:niveauConfiance aspace:{niveau} ;")

        for a in acteurs([m["generated"]] if isinstance(m.get("generated"), str) else m.get("generated")):
            w_(f"    aspace:generePar \"{echapper(a)}\" ;")
        v = m.get("verified")
        for a in acteurs([v] if isinstance(v, str) else v):
            w_(f"    aspace:verifiePar \"{echapper(a)}\" ;")

        for s in (m.get("sources") or []):
            mm = re.search(r"resource\s*:\s*(.+?)(?:\s+title\s*:|\s+author\s*:|\s+last_modified\s*:|$)", s)
            if mm:
                w_(f"    dcterms:source \"{echapper(mm.group(1).strip().strip(chr(34)+chr(39)))}\" ;")

        # Relations vers d'autres concepts : wikilinks et liens Markdown.
        cibles = set(RE_WIKI.findall(c["corps"]))
        cibles |= {x[:-3] for x in RE_MDLINK.findall(c["corps"])}
        for cible in sorted(cibles):
            cible = cible.strip()
            if cible in ("index", "fichier"):
                continue
            if cible in index_slug:
                w_(f"    aspace:relatedTo <{index_slug[cible]}> ;")
                relations += 1
                predicats_vus["relatedTo"] += 1
            else:
                liens_morts.append({"depuis": c["slug"], "vers": cible})

        w_("    rdfs:label \"" + echapper(m.get("title") or c["slug"]) + "\" .")
        w_("")

    chemin_ttl = os.path.join(SORTIE, "aspace-instances.ttl")
    with io.open(chemin_ttl, "w", encoding="utf-8") as f:
        f.write("\n".join(t))

    # --- Vocabulaire mesure --------------------------------------------
    vocab = {
        "genere": datetime.now(timezone.utc).isoformat(),
        "concepts": len(concepts),
        "relations_resolues": relations,
        "liens_non_resolus": len(liens_morts),
        "exemples_liens_non_resolus": liens_morts[:25],
        "niveaux_confiance": dict(stats),
        "types_utilises": types_vus.most_common(),
        "tags_utilises": tags_vus.most_common(40),
        "par_bundle": dict(Counter(c["bundle"] for c in concepts)),
    }
    with io.open(os.path.join(SORTIE, "vocabulaire_mesure.json"), "w", encoding="utf-8") as f:
        json.dump(vocab, f, ensure_ascii=False, indent=1)

    print(f"{len(concepts)} concepts -> {chemin_ttl}", file=sys.stderr)
    print(f"{relations} relations resolues, {len(liens_morts)} liens non resolus", file=sys.stderr)
    print(f"confiance : {dict(stats)}", file=sys.stderr)
    print(f"types distincts : {len(types_vus)}, tags distincts : {len(tags_vus)}", file=sys.stderr)


if __name__ == "__main__":
    main()

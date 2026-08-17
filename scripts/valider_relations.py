"""Valide relations.jsonl et genere le Turtle des relations typees.

POURQUOI CE SCRIPT EXISTE
L'agent de liaison ne modifie aucun fichier du graphe : il rend un seul
fichier de propositions. C'est ce script qui decide ce qui entre dans le
graphe, et il refuse tout ce qu'il ne peut pas verifier.

Ce partage n'est pas de la defiance de principe. Un agent qui editerait 102
fichiers a la main produirait un travail invalidable : on ne saurait pas
distinguer ce qu'il a mesure de ce qu'il a suppose, ni revenir en arriere sans
tout relire.

CE QU'IL REFUSE, ET POURQUOI
- un identifiant absent du graphe : c'est une invention, pas une relation ;
- un predicat hors schema : le vocabulaire est ferme, sinon il ne veut rien
  dire ;
- une boucle (A -> A) : ne porte aucune information ;
- un doublon exact : gonfle le compte sans rien ajouter.

Chaque refus est imprime avec sa ligne. Le compte des acceptes ET des refuses
figure dans la sortie : un validateur qui ne dirait que les acceptes laisserait
croire a une reussite totale.
"""

import io
import json
import os
import sys
from collections import Counter

V3 = r"C:\Users\amado\ASpace_OS_V3"
ONTO = os.path.join(V3, "50_Distillation", "ontologie")
ENTREE = os.path.join(ONTO, "relations.jsonl")
SORTIE = os.path.join(ONTO, "aspace-relations.ttl")

PREDICATS = {
    "appliesTo", "cites", "dependsOn", "governs", "handledBy",
    "instantiates", "pairedWith", "partOf", "refines", "seeAlso", "supersedes",
}
CONFIANCES = {"haute", "moyenne"}


def charger_identifiants():
    """Les identifiants reels, lus depuis le graphe d'instances. On ne se fie
    pas au catalogue : c'est le graphe qui fait foi."""
    ids = set()
    chemin = os.path.join(ONTO, "aspace-instances.ttl")
    with io.open(chemin, encoding="utf-8") as f:
        for ligne in f:
            if ligne.startswith("<urn:aspace:concept:"):
                ids.add(ligne.strip()[len("<urn:aspace:concept:"):-1])
    return ids


def echapper(s):
    return s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ").strip()


def main():
    if not os.path.exists(ENTREE):
        print(f"absent : {ENTREE}", file=sys.stderr)
        raise SystemExit(2)

    ids = charger_identifiants()
    print(f"{len(ids)} identifiants connus dans le graphe", file=sys.stderr)

    acceptees, refus = [], Counter()
    vus = set()
    exemples_refus = []

    with io.open(ENTREE, encoding="utf-8") as f:
        for num, ligne in enumerate(f, 1):
            ligne = ligne.strip()
            if not ligne or ligne.startswith("#"):
                continue
            try:
                r = json.loads(ligne)
            except json.JSONDecodeError as e:
                refus["json invalide"] += 1
                exemples_refus.append((num, "json invalide", str(e)[:60]))
                continue

            de, vers = r.get("de", ""), r.get("vers", "")
            pred, conf = r.get("predicat", ""), r.get("confiance", "")

            if de not in ids:
                refus["sujet inconnu"] += 1
                exemples_refus.append((num, "sujet inconnu", de)); continue
            if vers not in ids:
                refus["objet inconnu"] += 1
                exemples_refus.append((num, "objet inconnu", vers)); continue
            if pred not in PREDICATS:
                refus["predicat hors schema"] += 1
                exemples_refus.append((num, "predicat hors schema", pred)); continue
            if de == vers:
                refus["boucle"] += 1
                exemples_refus.append((num, "boucle", de)); continue
            cle = (de, vers, pred)
            if cle in vus:
                refus["doublon"] += 1
                exemples_refus.append((num, "doublon", f"{de}->{vers}")); continue
            if conf not in CONFIANCES:
                r["confiance"] = "moyenne"  # defaut prudent, pas un refus

            vus.add(cle)
            acceptees.append(r)

    # --- Turtle ---------------------------------------------------------
    t = ["# Relations typees entre concepts A'Space OS.",
         "# Genere par scripts/valider_relations.py depuis relations.jsonl.",
         "# NE PAS EDITER A LA MAIN.",
         "",
         "@prefix aspace: <urn:aspace:ns:> .",
         ""]
    for r in acceptees:
        s = f"urn:aspace:concept:{r['de']}"
        o = f"urn:aspace:concept:{r['vers']}"
        t.append(f"<{s}> aspace:{r['predicat']} <{o}> .")
        if r.get("pourquoi"):
            t.append(f"# {r['de']} --{r['predicat']}--> {r['vers']} : "
                     f"{echapper(r['pourquoi'])[:160]} [{r.get('confiance','moyenne')}]")
    with io.open(SORTIE, "w", encoding="utf-8") as f:
        f.write("\n".join(t) + "\n")

    # --- Rapport --------------------------------------------------------
    def bundle(x): return x.split(":")[0]
    transversales = [r for r in acceptees if bundle(r["de"]) != bundle(r["vers"])]
    par_bundle = Counter()
    for r in acceptees:
        par_bundle[bundle(r["de"])] += 1
        par_bundle[bundle(r["vers"])] += 1

    print(f"\nACCEPTEES : {len(acceptees)}")
    print(f"REFUSEES  : {sum(refus.values())}")
    for k, n in refus.most_common():
        print(f"   {n:>4}  {k}")
    for num, k, d in exemples_refus[:12]:
        print(f"      ligne {num} : {k} — {d}")
    print(f"\nTRANSVERSALES (entre bundles) : {len(transversales)} / {len(acceptees)}")
    print("\nPREDICATS UTILISES :")
    for p, n in Counter(r["predicat"] for r in acceptees).most_common():
        print(f"   {n:>4}  {p}")
    print("\nRELATIONS PAR BUNDLE (extremites) :")
    for b, n in par_bundle.most_common():
        print(f"   {n:>4}  {b}")
    muets = [b for b in ("areas", "projets", "archives", "ressources",
                         "ontologie", "prompt-systeme", "autonomie-agents")
             if par_bundle.get(b, 0) == 0]
    print(f"\nBUNDLES ENCORE MUETS : {muets if muets else 'aucun'}")
    print(f"\n-> {SORTIE}")


if __name__ == "__main__":
    main()

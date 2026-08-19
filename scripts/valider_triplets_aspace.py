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
import stat
import sys
from collections import Counter, defaultdict

V3 = r"C:\Users\amado\ASpace_OS_V3"
D = os.path.join(V3, "70_Onthologies")
DIST = os.path.join(V3, "50_Distillation")
# Deux passes, deux jeux de couches, deux graphes de sortie. Les melanger
# produirait un .ttl ou l'on ne saurait plus si une assertion vient de la
# distillation V2 ou de l'arborescence V3 — donc laquelle prime en cas de
# conflit. Le mode se choisit en argument.
PASSES = {
    "v2": (("tech", "life", "business"), "aspace-os.ttl"),
    "v3": (("v3-amadeus", "v3-tech", "v3-life", "v3-business"), "aspace-v3.ttl"),
    # Troisieme passe : le CONTENU reel, lu dans la V2. Les sources ne sont
    # plus des chemins V3 mais des chemins relatifs a 05_From_V2_Domains.
    "domaines": (("dom-tech", "dom-life", "dom-amadeus", "dom-business"),
                 "aspace-domaines.ttl"),
    # Vague 2 : corpus normatif, Life Wheel, Templates. Sources dans Geordi
    # au sens large, pas seulement 05_From_V2_Domains.
    "vague2": (("dom-normatif-sdd-prd", "dom-normatif-adr", "dom-life-wheel",
                "dom-templates"), "aspace-vague2.ttl"),
}

# La source reelle du contenu. La V3 n'est qu'un squelette : ses dossiers
# portent la structure, pas les documents.
DOMAINES_V2 = "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains"

# Chaque escouade de domaine couvre UNE couche. Un agent ecrit parfois son
# chemin relatif a sa couche plutot qu'a la racine des domaines : la
# correspondance etant deterministe, resoudre le prefixe n'est pas de la
# complaisance, c'est lever une reference non ambigue. Ce qui reste refuse,
# c'est ce qui ne resout NI d'une facon NI de l'autre.
COUCHE_DE = {
    "dom-tech": "10_Tech_OS",
    "dom-life": "20_Life_OS",
    "dom-amadeus": "00_Amadeus",
    "dom-business": "30_Business_OS",
    # Vague 2 : sources ailleurs dans Geordi, pas sous une couche unique.
    "dom-normatif-sdd-prd": "", "dom-normatif-adr": "",
    "dom-life-wheel": "09_Life_OS", "dom-templates": "02_Templates",
}

VERBES_SCHEMA = {
    "governs", "partOf", "dependsOn", "appliesTo", "refines", "instantiates",
    "pairedWith", "handledBy", "cites", "supersedes", "seeAlso",
}


def _sans_jonctions(racine, elaguer):
    """Parcours qui NE SUIT PAS les jonctions NTFS.

    os.walk les traite comme des dossiers ordinaires et y descend. Le canon du
    poste documente le cout : un parcours naif a deja compte 13,8 millions de
    fichiers la ou il y en avait 14 613. Geordi en porte 159 a lui seul, et
    c'est ce qui faisait boucler ce validateur.

    `os.path.islink()` ne les voit pas sous Windows. Le seul test fiable est
    l'attribut FILE_ATTRIBUTE_REPARSE_POINT.
    """
    RP = getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400)
    out = set()
    if not os.path.isdir(racine):
        return out
    pile = [racine]
    while pile:
        p = pile.pop()
        try:
            entrees = list(os.scandir(p))
        except OSError:
            continue
        for e in entrees:
            try:
                if e.is_dir(follow_symlinks=False):
                    if e.name in elaguer:
                        continue
                    try:
                        if e.stat(follow_symlinks=False).st_file_attributes & RP:
                            continue  # jonction : on ne la suit pas
                    except OSError:
                        continue
                    pile.append(e.path)
                elif e.is_file(follow_symlinks=False):
                    out.add(os.path.relpath(e.path, racine).replace(os.sep, "/"))
            except OSError:
                pass
    return out


def sources_reelles():
    """Les chemins qui existent vraiment — V3, domaines V2, et concepts distilles.

    Les trois passes n'ont pas la meme source : v2 cite des concepts de
    50_Distillation, v3 des fichiers de l'arborescence V3, domaines des chemins
    relatifs a 05_From_V2_Domains. Le validateur doit connaitre les trois,
    sinon il rejetterait comme inexistante une source parfaitement reelle."""
    ELAGUER = {"node_modules", ".git", "dist", "build", ".next", ".vercel",
               "venv", ".venv", "__pycache__", ".turbo", "coverage", ".cache",
               "openwiki", ".obsidian"}
    out = _sans_jonctions(V3, ELAGUER)
    out |= _sans_jonctions(DOMAINES_V2, ELAGUER)
    # La vague 2 cite des chemins ailleurs dans Geordi : 09_Life_OS,
    # 02_Templates, 04_From_V2_Root/_SPECS. Sans eux, des sources reelles
    # seraient rejetees.
    GEORDI = os.path.dirname(os.path.dirname(DOMAINES_V2))
    for sd in ("09_Life_OS", "02_Templates", "04_From_V2_Root",
               "03_Memory_Unified", "05_From_V2_Domains"):
        d = os.path.join(GEORDI, sd)
        if os.path.isdir(d):
            for rel in _sans_jonctions(d, ELAGUER):
                out.add(f"{sd}/{rel}")
                out.add(rel)
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
    mode = sys.argv[1] if len(sys.argv) > 1 else "v2"
    if mode not in PASSES:
        print(f"mode inconnu : {mode} (attendu : v2 ou v3)", file=sys.stderr)
        raise SystemExit(2)
    COUCHES, SORTIE_TTL = PASSES[mode]
    print(f"passe {mode} — couches {COUCHES}", file=sys.stderr)
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
            prefixe = COUCHE_DE.get(couche)
            candidats = [base, os.path.basename(base)]
            if prefixe and not base.startswith(prefixe):
                candidats.insert(1, f"{prefixe}/{base}")
            resolu = next((c for c in candidats if c in reelles), None)
            if resolu is None:
                refus["source inexistante"] += 1
                exemples.append((couche, num, "source inexistante", base[:60])); continue
            if resolu != base:
                r["source"] = resolu  # on garde le chemin qui resout, pas celui ecrit
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

    io.open(os.path.join(D, "triplets", SORTIE_TTL), "w", encoding="utf-8").write("\n".join(t) + "\n")

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
    print(f"\n-> {os.path.join(D, 'triplets', SORTIE_TTL)}")


if __name__ == "__main__":
    main()

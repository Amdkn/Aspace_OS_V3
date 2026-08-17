"""Extrait la couche ENTITES du graphe : les acteurs d'A'Space eux-memes.

POURQUOI CE SCRIPT EXISTE
Le graphe compte 102 concepts et 384 relations, mais il decrit des *documents
qui parlent* d'A'Space. Les acteurs d'A'Space — A0, les couches A1/A2/A3, Rick,
les Docteurs, les Compagnons, B1/B2/B3 — n'y sont pas des sujets. Ils sont cites
dans le texte (B2 dans 44 concepts, A0 dans 40, A3 dans 37) et invisibles pour
une requete.

Consequence concrete : on ne peut pas demander au graphe « que sait-on de A2 »,
alors que la reponse existe, eparpillee dans vingt-cinq documents.

CE QUE CE SCRIPT FAIT, ET CE QU'IL NE FAIT PAS
Il detecte les mentions et pose `aspace:mentionne`. C'est mecanique et
exhaustif : chaque entite est cherchee par ses alias, avec frontieres de mot.

Il ne dit RIEN de la hierarchie — qui gouverne qui, quelle couche opere quelle
autre. Cela demande de lire le canon, pas de compter des occurrences, et c'est
le travail de la passe semantique qui suit.

LE PIEGE DES CODES COURTS
`A0`, `A1`, `B2` sont deux caracteres. Sans frontiere de mot, `A1` matche
`A100`, `LA1`, `DATA1`. La detection utilise donc `(?<![A-Za-z0-9])CODE(?![A-Za-z0-9])`
— et chaque alias ambigu est teste avant d'entrer dans le registre.
"""

import io
import json
import os
import re
import sys
from collections import Counter, defaultdict

V3 = r"C:\Users\amado\ASpace_OS_V3"
BUNDLES = [
    ("50_Distillation", ["areas", "projets", "archives", "ressources", "ontologie"]),
    ("60_Implementation_Méthodologiques", ["prompt-systeme", "autonomie-agents"]),
]
SORTIE = os.path.join(V3, "50_Distillation", "ontologie")
GENERES = {"CATALOGUE.md", "RAPPORT.md"}

# Registre des entites. `alias` = formes ecrites reellement rencontrees.
# `nature` sert de premiere classification ; la hierarchie est le travail de
# la passe semantique, pas de ce script.
ENTITES = [
    ("a0-amadeus",     "A0 — Amadeus",              "Orchestrateur", ["A0", "Amadeus"]),
    ("a1",             "A1 — couche A1",            "Couche",        ["A1"]),
    ("a2",             "A2 — couche A2",            "Couche",        ["A2"]),
    ("a3",             "A3 — couche A3",            "Couche",        ["A3"]),
    ("rick",           "Rick — gouvernance Tech OS","Persona",       ["Rick"]),
    ("docteur",        "Les Docteurs (Cores)",      "Persona",       ["Docteur", "Doctor", "13th", "13e", "11th", "11e", "12th", "12e"]),
    ("compagnons",     "Les Compagnons",            "Collectif",     ["Compagnon", "Compagnons"]),
    ("b1",             "B1 — couche B1",            "Couche",        ["B1"]),
    ("b2",             "B2 — couche B2",            "Couche",        ["B2"]),
    ("b3",             "B3 — couche B3",            "Couche",        ["B3"]),
    ("business-os",    "Business OS",               "OS",            ["Business OS", "Business_OS", "30_Business_OS"]),
    ("life-os",        "Life OS",                   "OS",            ["Life OS", "Life_OS", "20_Life_OS"]),
    ("tech-os",        "Tech OS",                   "OS",            ["Tech OS", "Tech_OS", "10_Tech_OS"]),
    ("beth",           "Beth",                      "Persona",       ["Beth"]),
    ("morty",          "Morty",                     "Persona",       ["Morty"]),
    ("jerry",          "Jerry",                     "Persona",       ["Jerry"]),
    ("summer",         "Summer",                    "Persona",       ["Summer"]),
    ("picard",         "Picard",                    "Persona",       ["Picard"]),
    ("spock",          "Spock",                     "Persona",       ["Spock"]),
    ("data",           "Data",                      "Persona",       ["Data"]),
    ("geordi",         "Geordi",                    "Persona",       ["Geordi"]),
]


def motif(alias):
    """Frontiere de mot stricte : sans elle, A1 matche A100, LA1, DATA1."""
    return re.compile(r"(?<![A-Za-z0-9_])" + re.escape(alias) + r"(?![A-Za-z0-9_])")


MOTIFS = {cle: [motif(a) for a in alias] for cle, _, _, alias in ENTITES}


def echapper(s):
    return s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ").strip()


def main():
    docs = []
    for racine, sous in BUNDLES:
        for sb in sous:
            d = os.path.join(V3, racine, sb)
            if not os.path.isdir(d):
                continue
            for nom in sorted(os.listdir(d)):
                if not nom.endswith(".md") or nom == "index.md" or nom in GENERES:
                    continue
                with io.open(os.path.join(d, nom), encoding="utf-8", errors="replace") as f:
                    docs.append((f"{sb}:{nom[:-3]}", f.read()))

    mentions = defaultdict(list)
    compte = Counter()
    for iden, texte in docs:
        for cle, motifs in MOTIFS.items():
            n = sum(len(m.findall(texte)) for m in motifs)
            if n:
                mentions[cle].append((iden, n))
                compte[cle] += 1

    t = ["# Couche ENTITES — les acteurs d'A'Space comme sujets du graphe.",
         "# Genere par scripts/extraire_entites.py — NE PAS EDITER A LA MAIN.",
         "#",
         "# Ce fichier pose QUI existe et OU on en parle. Il ne dit rien de la",
         "# hierarchie : qui gouverne qui se lit dans le canon, pas dans un",
         "# comptage d'occurrences. Voir aspace-hierarchie.ttl.",
         "",
         "@prefix aspace: <urn:aspace:ns:> .",
         "@prefix rdfs:   <http://www.w3.org/2000/01/rdf-schema#> .",
         ""]

    for cle, label, nature, alias in ENTITES:
        iri = f"urn:aspace:entity:{cle}"
        t.append(f"<{iri}>")
        t.append("    a aspace:Entite ;")
        t.append(f"    aspace:nature aspace:{nature} ;")
        t.append(f'    rdfs:label "{echapper(label)}" ;')
        for a in alias:
            t.append(f'    aspace:alias "{echapper(a)}" ;')
        liste = sorted(mentions.get(cle, []), key=lambda x: -x[1])
        t.append(f"    aspace:nbConceptsQuiMentionnent {len(liste)} ;")
        for iden, n in liste:
            t.append(f"    aspace:mentionneDans <urn:aspace:concept:{iden}> ;")
        t[-1] = t[-1][:-1] + "."
        t.append("")

    chemin = os.path.join(SORTIE, "aspace-entites.ttl")
    with io.open(chemin, "w", encoding="utf-8") as f:
        f.write("\n".join(t))

    rapport = {
        "entites": len(ENTITES),
        "concepts_analyses": len(docs),
        "couverture": {cle: compte.get(cle, 0) for cle, _, _, _ in ENTITES},
        "jamais_mentionnees": [cle for cle, _, _, _ in ENTITES if not compte.get(cle)],
    }
    with io.open(os.path.join(SORTIE, "entites_mesure.json"), "w", encoding="utf-8") as f:
        json.dump(rapport, f, ensure_ascii=False, indent=1)

    print(f"{len(ENTITES)} entites, {len(docs)} concepts analyses -> {chemin}", file=sys.stderr)
    for cle, label, _, _ in ENTITES:
        print(f"   {compte.get(cle, 0):>4} concepts  {label}", file=sys.stderr)
    if rapport["jamais_mentionnees"]:
        print(f"\nJAMAIS MENTIONNEES : {rapport['jamais_mentionnees']}", file=sys.stderr)


if __name__ == "__main__":
    main()

"""Interroge le graphe OKF en SPARQL. Zero dependance nouvelle.

POURQUOI CE SCRIPT EXISTE
Le graphe existait depuis le 2026-08-17 — 6 fichiers Turtle, generes par
`concepts_vers_triplets.py` — et personne ne l'interrogeait. Un graphe qu'on
ne questionne pas est un fichier mort : il coute a produire et ne rend rien.

POURQUOI PAS SEMANTICA
Semantica (graph-native, MIT, 10,7k etoiles) fait tout ce qui suit, et bien
plus. Il exige aussi 42 dependances OBLIGATOIRES : torch, transformers,
spacy, opencv-python, librosa, faiss-cpu, onnxruntime — plusieurs Go de pile
deep-learning, pour un corpus de markdown sans image ni audio.

`rdflib` etait deja installe sur ce poste (7.6.0) et porte SPARQL 1.1 en
natif. C'est le meme moteur RDF dont Semantica depend. Ce script rend donc
~90 % de la valeur cherchee a 0 % du poids d'installation.

Le jour ou un besoin reel depasse SPARQL — raisonnement OWL, detection de
contradictions par SHACL, reconciliation d'entites — Semantica redevient le
bon outil. Pas avant : installer plusieurs Go pour compter des concepts
serait le meme gaspillage que les 1,3 Mo de canvasui qui ne rendaient aucun
pixel.

USAGE
  python scripts/interroger_graphe.py                 # tableau de bord
  python scripts/interroger_graphe.py --non-verifies  # ce qui reste a relire
  python scripts/interroger_graphe.py --orphelins     # concepts sans lien
  python scripts/interroger_graphe.py --sparql "SELECT ..."
"""

import glob
import os
import sys

try:
    import rdflib
except ImportError:
    print("rdflib manquant : pip install rdflib", file=sys.stderr)
    raise SystemExit(1)

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

V3 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ONTO = os.path.join(V3, "50_Distillation", "ontologie")

PREFIXES = """
PREFIX a: <urn:aspace:ns:>
PREFIX dct: <http://purl.org/dc/terms/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
"""


def charger():
    g = rdflib.Graph()
    fichiers = sorted(glob.glob(os.path.join(ONTO, "*.ttl")))
    if not fichiers:
        print(f"Aucun .ttl dans {ONTO}.", file=sys.stderr)
        print("Generer d'abord : python scripts/concepts_vers_triplets.py",
              file=sys.stderr)
        raise SystemExit(1)
    for f in fichiers:
        g.parse(f, format="turtle")
    return g, len(fichiers)


def court(v) -> str:
    """Raccourcit un IRI pour l'affichage, sans le tronquer au hasard."""
    s = str(v)
    for p in ("urn:aspace:concept:", "urn:aspace:ns:", "urn:aspace:"):
        if s.startswith(p):
            return s[len(p):]
    return s


def tableau_de_bord(g):
    print("=== confiance, par bundle ===")
    q = PREFIXES + """
    SELECT ?b ?niv (COUNT(?c) AS ?n) WHERE {
        ?c a:bundle ?b ; a:niveauConfiance ?niv
    } GROUP BY ?b ?niv ORDER BY ?b DESC(?n)"""
    total = 0
    for r in g.query(q):
        n = int(r.n)
        total += n
        print(f"  {str(r.b):18s} {court(r.niv):16s} {n:4d}")
    print(f"  {'':18s} {'TOTAL':16s} {total:4d}")

    print("\n=== types de concepts ===")
    q = PREFIXES + """
    SELECT ?k (COUNT(?c) AS ?n) WHERE { ?c a:kind ?k }
    GROUP BY ?k ORDER BY DESC(?n)"""
    for r in list(g.query(q))[:12]:
        print(f"  {int(r.n):4d}  {court(r.k)}")

    print("\n=== concepts les plus cites ===")
    q = PREFIXES + """
    SELECT ?cible (COUNT(?src) AS ?n) WHERE { ?src a:relatedTo ?cible }
    GROUP BY ?cible ORDER BY DESC(?n)"""
    for r in list(g.query(q))[:10]:
        print(f"  {int(r.n):4d}  {court(r.cible)}")


def non_verifies(g):
    """Ce qui n'a jamais ete relu par un humain, par ordre d'importance.

    L'ordre n'est pas alphabetique : un concept que dix autres citent coute
    plus cher a laisser non verifie qu'une feuille isolee. C'est la seule
    priorisation que le graphe permette sans deviner.
    """
    q = PREFIXES + """
    SELECT ?c ?titre (COUNT(?src) AS ?cites) WHERE {
        ?c a:niveauConfiance ?niv .
        FILTER(?niv != a:revuHumain)
        OPTIONAL { ?c dct:title ?titre }
        OPTIONAL { ?src a:relatedTo ?c }
    } GROUP BY ?c ?titre ORDER BY DESC(?cites) LIMIT 30"""
    lignes = list(g.query(q))
    print(f"=== {len(lignes)} concepts non revus par un humain (top 30 par citations) ===")
    for r in lignes:
        t = str(r.titre)[:58] if r.titre else court(r.c)[:58]
        print(f"  cite {int(r.cites):3d}x  {t}")
    print("\nAucun script ne peut poser le tampon `human:` a la place du proprietaire.")


def orphelins(g):
    """Concepts que rien ne cite et qui ne citent rien.

    Un concept isole n'est pas forcement mauvais — il peut etre une feuille
    legitime. Mais il est invisible depuis n'importe quel parcours du graphe,
    donc il ne sera jamais retrouve autrement qu'en le cherchant par son nom.
    """
    q = PREFIXES + """
    SELECT ?c ?titre WHERE {
        ?c a:niveauConfiance ?niv .
        OPTIONAL { ?c dct:title ?titre }
        FILTER NOT EXISTS { ?c a:relatedTo ?x }
        FILTER NOT EXISTS { ?y a:relatedTo ?c }
    } ORDER BY ?c"""
    lignes = list(g.query(q))
    print(f"=== {len(lignes)} concepts orphelins (ni cites, ni citants) ===")
    for r in lignes[:40]:
        t = str(r.titre)[:60] if r.titre else ""
        print(f"  {court(r.c):52s} {t}")
    if len(lignes) > 40:
        print(f"  … {len(lignes) - 40} autres")


def main() -> int:
    g, nb = charger()
    print(f"{len(g)} triplets, {nb} fichiers Turtle\n")

    if "--sparql" in sys.argv:
        i = sys.argv.index("--sparql")
        if i + 1 >= len(sys.argv):
            print("--sparql attend une requete.", file=sys.stderr)
            return 1
        for r in g.query(PREFIXES + sys.argv[i + 1]):
            print("  " + "  ".join(court(v) for v in r))
        return 0

    if "--non-verifies" in sys.argv:
        non_verifies(g)
    elif "--orphelins" in sys.argv:
        orphelins(g)
    else:
        tableau_de_bord(g)
    return 0


if __name__ == "__main__":
    sys.exit(main())

"""Verifie l'integrite du corpus OKF : liens morts, frontmatter, niveau de confiance.

POURQUOI CE SCRIPT EXISTE
Le canon du poste pose deux regles que rien ne verifiait mecaniquement :

  1. « Ne JAMAIS poser de lien [[nom]] vers un concept qui n'existe pas —
     verifier avant d'ecrire. Un lien mort ment a l'avenir. »
  2. « Le niveau de confiance se deduit de `verified` » — non verifie,
     confirme machine, revu humain.

Les deux tenaient par la discipline humaine. Une regle tenue par la vigilance
seule finit par ceder : c'est mesurable ici, et ce script le mesure.

CE QU'IL NE FAIT PAS, ET POURQUOI
Il ne construit pas de graphe. `concepts_vers_triplets.py` le fait deja pour
50_Distillation et 60_Implementation, et `valider_triplets_aspace.py` decide
ce qui entre dans le graphe. Ce script-ci ne fait qu'une chose : dire si le
corpus tient debout avant qu'on tente d'en extraire quoi que ce soit. Un
graphe bati sur des liens morts propagerait le mensonge au lieu de le
signaler.

Il ne corrige rien non plus. Reparer un lien mort demande de savoir ce que
l'auteur voulait dire — un script qui devinerait ferait pire que le defaut.

CE QU'IL REFUSE DE CACHER
Le compte des defauts ET le compte des fichiers sains. Un rapport qui ne
listerait que les erreurs laisserait croire que le reste a ete verifie ; un
rapport qui ne dirait que « tout va bien » ne dirait pas sur quoi il a porte.
Le bruit ecarte (fragments de code pris pour des liens) est compte a part et
affiche : un filtre silencieux est un mensonge par omission.
"""

import io
import os
import re
import sys
from collections import Counter, defaultdict

V3 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# La console Windows par defaut est en cp1252 : sans ca, un chemin comme
# `60_Implementation_Méthodologiques` sort mutile et devient inutilisable pour
# aller corriger le fichier. Un rapport qu'on ne peut pas suivre ne sert a rien.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# Dossiers hors perimetre. Ce ne sont pas des exclusions de confort :
#   - node_modules / .git : ne nous appartiennent pas ;
#   - openwiki : clone du depot amont langchain-ai/openwiki, pas notre memoire
#     (correction du 2026-08-17 inscrite au canon) ;
#   - _ARCHIVE_* : sorti du depot actif volontairement, le verifier reviendrait
#     a garder vivant ce qu'on a decide d'archiver.
EXCLUS = {
    "node_modules", ".git", "dist", "build", ".venv", "__pycache__",
    "openwiki",
    # Sortie generee par consolider_pour_review.py : chaque concept y est
    # recopie pour NotebookLM. Un defaut vu la est le meme defaut que dans sa
    # source, deja compte — le signaler deux fois gonflerait le total sans
    # rien ajouter, et corriger la copie a la main serait perdu a la prochaine
    # regeneration.
    "_REVIEW_NOTEBOOKLM",
}
EXCLUS_PREFIXE = ("_ARCHIVE_",)

RE_LIEN = re.compile(r"\[\[([^\]|#]+?)(?:[|#][^\]]*)?\]\]")

# Un `[[...]]` a l'interieur d'un bloc ou d'un span de code n'est pas un lien :
# c'est du texte cite. Mesure sur le corpus avant ce filtre : `[[:space:]]`
# (classe POSIX dans un CHANGELOG), `[[1984, 2790]]` (tableau imbrique dans un
# rapport), `[[...rest]]` (spread JS). Les compter comme liens morts rendrait
# le rapport faux, donc inutilisable — le meme piege que le selecteur de
# shot.mjs qui attrapait le mauvais bouton.
RE_BLOC_CODE = re.compile(r"```.*?```|~~~.*?~~~", re.S)
RE_SPAN_CODE = re.compile(r"`[^`\n]*`")

# Champs que le canon declare minimaux pour un concept OKF v0.2.
CHAMPS_MINIMAUX = ["type", "title", "description", "generated", "okf_version"]

# Un lien dont la cible ressemble a du code plutot qu'a un slug de concept.
# Mesure sur le corpus : `[[...rest]]` (spread JS), `[[…]]` (ellipse
# typographique dans un exemple). Les ecarter en silence donnerait un faux
# vert ; ils sont comptes et affiches sous leur propre rubrique.
def est_bruit(cible: str) -> bool:
    c = cible.strip()
    if not c:
        return True
    if c.startswith("...") or c.startswith("…") or c == "…":
        return True
    if c.startswith("<") or c.endswith(">"):  # <nom>, placeholder de gabarit
        return True
    if c.startswith(":") and c.endswith(":"):  # classe POSIX : [[:space:]]
        return True
    # Un slug de concept ne contient ni virgule ni chiffre seul : `1984, 2790`
    # est un tableau, pas un nom de fichier.
    if "," in c or re.fullmatch(r"[\d\s.eE+-]+", c):
        return True
    return False


def sans_code(texte: str) -> str:
    """Neutralise blocs et spans de code, en preservant les sauts de ligne.

    On remplace par des espaces plutot que de supprimer : les numeros de ligne
    restent justes si on veut les afficher un jour.
    """
    def blancs(m):
        return re.sub(r"[^\n]", " ", m.group(0))
    return RE_SPAN_CODE.sub(blancs, RE_BLOC_CODE.sub(blancs, texte))


def fichiers_markdown():
    """Tous les .md du corpus, hors perimetres exclus."""
    for racine, dossiers, fichiers in os.walk(V3):
        dossiers[:] = [
            d for d in dossiers
            if d not in EXCLUS and not d.startswith(EXCLUS_PREFIXE)
        ]
        for f in fichiers:
            if f.endswith(".md"):
                yield os.path.join(racine, f)


def lire(chemin: str) -> str:
    with io.open(chemin, "r", encoding="utf-8", errors="replace") as fh:
        return fh.read()


def frontmatter(texte: str):
    """Retourne le bloc frontmatter brut, ou None s'il n'y en a pas.

    Volontairement sans PyYAML : on ne lit que la presence de champs et les
    acteurs de `verified`. Importer un parseur complet pour ca ajouterait une
    dependance a un depot qui n'en a aucune.
    """
    if not texte.startswith("---"):
        return None
    fin = texte.find("\n---", 3)
    if fin == -1:
        return None
    return texte[3:fin]


def acteurs_verified(bloc: str):
    """Les acteurs listes sous `verified:`, ou None si le champ est absent.

    Distinction qui porte tout le sens du format : `verified` absent n'est pas
    la meme chose que `verified` present mais vide.
    """
    m = re.search(r"^verified:\s*(.*)$", bloc, re.M)
    if not m:
        return None
    debut = m.end()
    reste = bloc[debut:]
    # Le bloc s'arrete a la premiere cle de meme niveau (colonne 0).
    fin = re.search(r"^\w[\w_]*:", reste, re.M)
    corps = reste[: fin.start()] if fin else reste
    corps = m.group(1) + "\n" + corps
    return re.findall(r"by:\s*([^,}\s]+)", corps)


def niveau_confiance(bloc: str) -> str:
    acteurs = acteurs_verified(bloc)
    if acteurs is None or not acteurs:
        return "non_verifie"
    if any(a.startswith("human:") for a in acteurs):
        return "revu_humain"
    return "confirme_machine"


def main() -> int:
    chemins = list(fichiers_markdown())

    # Index slug -> chemins. Un slug est le nom de fichier sans .md, c'est la
    # forme que prennent les liens [[...]] mesuree sur le corpus.
    index = defaultdict(list)
    for c in chemins:
        index[os.path.splitext(os.path.basename(c))[0]].append(c)

    # Resolution en quatre etats, et non en binaire.
    #
    # Mesure du 2026-08-24 : le corpus lie souvent par PREFIXE du slug —
    # `[[b2-council-cadence]]` vise `b2-council-cadence-and-chair.md`, qui
    # existe. Un simple test d'egalite declarait 90 liens morts dont la
    # plupart resolvaient ; l'instrument accusait le mauvais coupable.
    #
    #   exact    : le slug correspond au nom de fichier
    #   prefixe  : un seul fichier commence par ce slug — resout, mais fragile
    #   ambigu   : plusieurs candidats — le lecteur ne peut pas trancher
    #   mort     : aucun candidat
    liens_morts = defaultdict(list)     # cible -> [fichiers qui la citent]
    liens_ambigus = defaultdict(list)   # cible -> [candidats]
    liens_malformes = defaultdict(list)  # cible -> [candidat reel]
    par_prefixe = 0
    bruit = Counter()
    total_liens = 0

    slugs = sorted(index)
    slugs_bas = {s.lower(): s for s in slugs}

    # De la prose glissee dans les crochets : `[[cf. b2-eight-domain-vetoes]]`.
    # La cible existe, seule la forme du lien est fautive. La classer « morte »
    # serait faux — et un rapport faux ne se corrige pas, il s'ignore.
    RE_PROSE = re.compile(r"^(cf\.?|voir|see|ref\.?)\s+", re.I)

    def resoudre(slug: str):
        if slug in index:
            return "exact", None
        nu = RE_PROSE.sub("", slug).strip()
        if nu != slug and (nu in index or nu.lower() in slugs_bas):
            return "malforme", [slugs_bas.get(nu.lower(), nu)]
        cible = nu or slug
        candidats = [s for s in slugs if s.lower().startswith(cible.lower() + "-")]
        if len(candidats) == 1:
            return ("malforme" if nu != slug else "prefixe"), candidats
        if candidats:
            return "ambigu", candidats
        return "mort", None

    concepts_okf = []
    frontmatter_incomplet = defaultdict(list)  # chemin -> [champs manquants]
    confiance = Counter()

    for chemin in chemins:
        texte = lire(chemin)
        rel = os.path.relpath(chemin, V3).replace("\\", "/")

        for m in RE_LIEN.finditer(sans_code(texte)):
            cible = m.group(1).strip()
            if est_bruit(cible):
                bruit[cible] += 1
                continue
            total_liens += 1
            # Un lien peut viser un slug ou un chemin relatif ; on normalise
            # sur le dernier segment, sans extension.
            # Surtout PAS os.path.splitext : il coupe au dernier point, donc
            # `cf. b2-eight-domain-vetoes` devenait le slug `cf`. On ne retire
            # que l'extension .md, la seule qui soit vraiment une extension.
            base = cible.replace("\\", "/").rsplit("/", 1)[-1]
            slug = base[:-3] if base.lower().endswith(".md") else base
            etat, candidats = resoudre(slug)
            if etat == "mort":
                liens_morts[cible].append(rel)
            elif etat == "ambigu":
                liens_ambigus[cible] = candidats
            elif etat == "malforme":
                liens_malformes[cible] = candidats
            elif etat == "prefixe":
                par_prefixe += 1

        bloc = frontmatter(texte)
        if bloc and "okf_version" in bloc:
            concepts_okf.append(rel)
            manquants = [c for c in CHAMPS_MINIMAUX
                         if not re.search(r"^%s:" % re.escape(c), bloc, re.M)]
            if manquants:
                frontmatter_incomplet[rel] = manquants
            confiance[niveau_confiance(bloc)] += 1

    # ── Rapport ───────────────────────────────────────────────────────────
    print("=== corpus ===")
    print(f"  fichiers markdown scannes : {len(chemins)}")
    print(f"  concepts OKF (okf_version): {len(concepts_okf)}")
    print(f"  liens [[...]] evalues     : {total_liens}")
    if bruit:
        n = sum(bruit.values())
        formes = ", ".join(sorted(bruit)[:4])
        print(f"  ecartes comme non-liens   : {n} ({formes})")

    if par_prefixe:
        print(f"  dont resolus par prefixe  : {par_prefixe}")

    print("\n=== liens morts (aucun fichier candidat) ===")
    if not liens_morts:
        print("  aucun — chaque [[cible]] resout vers un fichier reel")
    else:
        cites = sum(len(v) for v in liens_morts.values())
        print(f"  {len(liens_morts)} cibles inexistantes, citees {cites} fois")
        for cible in sorted(liens_morts)[:25]:
            source = liens_morts[cible]
            suffixe = f" (+{len(source) - 1} autres)" if len(source) > 1 else ""
            print(f"    [[{cible}]]  <- {source[0]}{suffixe}")
        if len(liens_morts) > 25:
            print(f"    … {len(liens_morts) - 25} autres cibles non listees")

    print("\n=== liens malformes (la cible existe, la forme est fautive) ===")
    if not liens_malformes:
        print("  aucun")
    else:
        print(f"  {len(liens_malformes)} — de la prose dans les crochets."
              " Corrigeables sans rien ecrire de neuf :")
        for cible in sorted(liens_malformes)[:10]:
            print(f"    [[{cible}]]  -> [[{liens_malformes[cible][0]}]]")
        if len(liens_malformes) > 10:
            print(f"    … {len(liens_malformes) - 10} autres")

    print("\n=== liens ambigus (plusieurs candidats) ===")
    if not liens_ambigus:
        print("  aucun")
    else:
        print(f"  {len(liens_ambigus)} cibles ne designent pas un fichier unique.")
        print("  Ce n'est pas un lien mort : c'est un lien que le lecteur ne")
        print("  peut pas suivre sans deviner.")
        for cible in sorted(liens_ambigus)[:15]:
            cands = liens_ambigus[cible]
            apercu = ", ".join(cands[:3])
            reste = f" (+{len(cands) - 3})" if len(cands) > 3 else ""
            print(f"    [[{cible}]]  -> {apercu}{reste}")
        if len(liens_ambigus) > 15:
            print(f"    … {len(liens_ambigus) - 15} autres")

    print("\n=== frontmatter OKF incomplet ===")
    if not frontmatter_incomplet:
        print(f"  aucun — les {len(concepts_okf)} concepts portent les champs minimaux")
    else:
        print(f"  {len(frontmatter_incomplet)} concepts sur {len(concepts_okf)}")
        for rel in sorted(frontmatter_incomplet)[:20]:
            print(f"    {rel} — manque : {', '.join(frontmatter_incomplet[rel])}")
        if len(frontmatter_incomplet) > 20:
            print(f"    … {len(frontmatter_incomplet) - 20} autres")

    print("\n=== niveau de confiance ===")
    total = sum(confiance.values()) or 1
    for niveau, libelle in [
        ("revu_humain", "revu par un humain"),
        ("confirme_machine", "confirme par machine"),
        ("non_verifie", "non verifie"),
    ]:
        n = confiance[niveau]
        print(f"  {libelle:22s} : {n:4d}  ({n * 100 // total}%)")

    # Les liens ambigus ne comptent pas comme defauts bloquants : ils
    # resolvent, mais mal. Les compter avec les morts ferait passer une gene
    # de lecture pour une rupture de chaine.
    defauts = len(liens_morts) + len(frontmatter_incomplet)
    print(f"\n{defauts} defaut(s) d'integrite — "
          f"{len(liens_ambigus)} ambiguite(s) et {len(liens_malformes)} lien(s)"
          " malforme(s) signales, non bloquants.")
    if confiance["revu_humain"] == 0 and total > 1:
        print("Aucun concept revu par un humain — le goulot reste la verification,")
        print("pas la production. Aucun script ne peut poser ce tampon.")
    return 1 if defauts else 0


if __name__ == "__main__":
    sys.exit(main())

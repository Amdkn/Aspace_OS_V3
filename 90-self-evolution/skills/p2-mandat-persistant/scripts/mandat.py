#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Le mandat survit-il a la compaction ?

POURQUOI CE SCRIPT EXISTE
    GARDE-FOU a ete reecrit 96 fois, LES SEPT CADENCES 69, MODE FABLE 60.
    Ces briefs disent tous « execute toi-meme, n'invoque personne ». Ils sont
    reecrits parce qu'ils ne TIENNENT pas : la compaction garde les faits et
    perd l'autorisation.

    Ce qui doit survivre a l'invocation ne vit pas dans le contexte. Il vit
    dans un fichier que le demarrage relit. Ce script dit lesquels, ce qu'ils
    coutent, et si l'autorisation y figure vraiment.

LA REGLE QU'IL APPLIQUE
    Une autorisation ecrite dans le fil de conversation ne compte pas. Si elle
    n'est pas dans la sortie de --verifier, elle ne survivra pas.
"""

from __future__ import annotations
import re
import sys
import unicodedata
from pathlib import Path

# La console Windows est en cp1252 et leve sur le premier caractere hors table
# (« → », « × »). Un script qui meurt en affichant son resultat est un
# instrument qui ment par omission : il a mesure juste et n'a rien rendu.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

MAISON = Path("C:/Users/amado")
V3 = MAISON / "ASpace_OS_V3"

# Ce qui est reellement charge a CHAQUE session. Ne pas y mettre les fichiers
# lus a la demande : gonfler ce compte pousserait a couper ce qu'il faut garder.
DEMARRAGE = [
    (MAISON / "CLAUDE.md", "mandat — le pourquoi (desirs, besoins, attendus)"),
    (MAISON / ".claude" / "CLAUDE.md", "memoire canonique OKF"),
    (V3 / "CLAUDE.md", "regles de travail — le comment (charge dans V3)"),
]

# Un mandat s'ecrit en ACTES. Un fichier qui n'enonce que des interdits produit
# un executant qui s'arrete -- c'est le defaut qu'on corrige, pas un detail de
# style. On cherche donc des formulations d'autorisation, pas de prohibition.
MARQUEURS = [
    (r"\bagis\b|\bexecute[sz]?\b|\bexecuter\b", "ordre d'agir"),
    # Motif elargi le 2026-08-30 : la version etroite exigeait « sans
    # demander » et rendait « introuvable » sur « ne redemande pas », qui dit
    # exactement la meme chose. Une sonde qui rate la formulation reelle accuse
    # un mandat correct -- meme famille que LinkType et que les accents.
    (r"sans (?:me )?demander|sans redemander|ne redemande|"
     r"ne (?:pas )?demander|pas a la demander|ne s'eteint pas",
     "dispense de redemander"),
    (r"une seule branche|branche defendable|defendable", "regle de tranchage"),
    (r"comment la defaire|reversib", "exigence de reversibilite"),
    (r"toi-meme|toi meme", "exigence d'execution propre"),
    (r"a sourcer|mesure|suppose", "frontiere mesure/suppose"),
]

# Les portes qui doivent RESTER. Un mandat qui les efface n'est pas un mandat
# plus fort, c'est un mandat dangereux.
PORTES = [
    (r"ca racine|autorite de certification", "CA racine"),
    (r"depot divergent|pousser sur", "push divergent"),
    (r"virement|transfert de fonds", "virement"),
    (r"supprim\w+ des donnees|suppression de donnees", "suppression de donnees"),
    (r"machine.{0,12}humain", "passage confiance machine → humain"),
]


def sans_accents(s: str) -> str:
    """DEFAUT PAYE LE 2026-08-30 : les motifs etaient non accentues face a un
    texte qui l'est. Le script rendait « introuvable » pour « comment la
    defaire », « toi-meme » et « supprimer des donnees » -- tous presents.
    Un verificateur qui rate ce qu'il cherche accuse un mandat correct."""
    s = unicodedata.normalize("NFKD", s.lower())
    return "".join(c for c in s if not unicodedata.combining(c))


def lire(p: Path) -> str | None:
    try:
        return p.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return None


def etat() -> int:
    total = 0
    manquants = 0
    print("  Ce qui est charge a chaque session :\n")
    for p, role in DEMARRAGE:
        t = lire(p)
        if t is None:
            print(f"    ABSENT  {p}")
            manquants += 1
            continue
        tok = len(t) // 4          # approximation usuelle, suffisante ici
        total += tok
        print(f"    {len(t.splitlines()):>4} l.  ~{tok:>5} tok   {p.name:14} {role}")
    print(f"\n  cout de demarrage : ~{total:,} tokens")
    print("  (le plancher d'outillage MCP s'y ajoute — voir p5-plancher-contexte)")
    return 1 if manquants else 0


def verifier() -> int:
    echecs = 0
    print("  Verification du mandat\n")

    corpus = []
    for p, role in DEMARRAGE:
        t = lire(p)
        if t is None:
            print(f"  ECHEC : fichier de demarrage absent — {p}")
            print("  Un mandat qui pointe vers un fichier disparu est pire")
            print("  qu'aucun mandat : il donne l'illusion d'une garantie.")
            echecs += 1
            continue
        corpus.append((p.name, sans_accents(t)))

    if not corpus:
        return 1

    joint = "\n".join(t for _, t in corpus)

    print("  Autorisations trouvees :")
    absents = []
    for motif, libelle in MARQUEURS:
        ou = [n for n, t in corpus if re.search(motif, t)]
        if ou:
            print(f"    OK    {libelle:34} ({', '.join(sorted(set(ou)))})")
        else:
            print(f"    --    {libelle:34} introuvable")
            absents.append(libelle)

    print("\n  Portes irreversibles (doivent rester) :")
    for motif, libelle in PORTES:
        etat_p = "OK   " if re.search(motif, joint) else "--   "
        print(f"    {etat_p} {libelle}")

    if absents:
        print(f"\n  {len(absents)} marqueur(s) d'autorisation absent(s).")
        print("  Un mandat incomplet se fait reecrire a la session suivante :")
        print("  c'est exactement la boucle P2 → P1 qu'on cherche a casser.")

    if echecs:
        print(f"\n  ECHEC : {echecs} fichier(s) de demarrage manquant(s).")
        return 1

    print("\n  Les fichiers de demarrage sont en place.")
    print("  Rappel : une autorisation ecrite dans le FIL ne compte pas.")
    print("  Si elle n'est pas ci-dessus, elle ne survivra pas a la compaction.")
    return 0


def auto_test() -> int:
    """Echoue si un fichier de demarrage manque, ou si l'ordre d'agir a
    disparu. Ces deux conditions PEUVENT survenir -- un test qui ne peut pas
    echouer ne teste rien."""
    print("  Auto-test du mandat\n")
    manquants = [p for p, _ in DEMARRAGE if lire(p) is None]
    if manquants:
        for p in manquants:
            print(f"  ECHEC : fichier de demarrage absent — {p}")
        return 1

    joint = "\n".join(sans_accents(lire(p) or "") for p, _ in DEMARRAGE)
    if not re.search(MARQUEURS[0][0], joint):
        print("  ECHEC : aucun ordre d'agir dans les fichiers de demarrage.")
        print("  Un mandat sans autorisation d'agir se fait reecrire a la")
        print("  session suivante : c'est la boucle P2 → P1.")
        return 1

    total = sum(len(lire(p) or "") // 4 for p, _ in DEMARRAGE)
    print(f"  {len(DEMARRAGE)} fichiers de demarrage presents, ~{total:,} tokens.")
    print("  L'ordre d'agir est present.")
    print("\n  OK. Detail des autorisations : mandat.py --verifier")
    return 0


def main(argv: list[str]) -> int:
    if len(argv) < 2 or argv[1] not in ("--etat", "--verifier", "--auto-test"):
        print(__doc__)
        print("  usage : mandat.py --etat | --verifier | --auto-test")
        return 2
    if argv[1] == "--auto-test":
        return auto_test()
    return etat() if argv[1] == "--etat" else verifier()


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

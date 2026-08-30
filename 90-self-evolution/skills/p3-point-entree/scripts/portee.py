#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Ce document est-il ATTEIGNABLE depuis ce qui est lu au demarrage ?

POURQUOI CE SCRIPT EXISTE
    130 rapports, 2,6 Mo. Aucun orphelin -- ils se citaient entre eux. Mais
    seuls 13 etaient atteignables en 4 sauts depuis les CLAUDE.md : les 117
    autres vivaient dans une boucle fermee que rien de lu au demarrage
    n'atteignait. Du travail paye en jetons et jamais relu.

LA DISTINCTION QUI COMPTE
    « Est-il cite ? » et « est-il atteignable ? » sont deux questions
    differentes. Une boucle fermee repond OUI a la premiere et NON a la
    seconde. Compter les liens entrants ne la detecte pas.
"""

from __future__ import annotations
import os
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

V3 = Path("C:/Users/amado/ASpace_OS_V3")
DEPARTS = [
    Path("C:/Users/amado/CLAUDE.md"),
    Path("C:/Users/amado/.claude/CLAUDE.md"),
    V3 / "CLAUDE.md",
]
EXCLUS = {"node_modules", ".git", "openwiki", "__pycache__", ".venv", "dist", "build"}
SAUTS_MAX = 4
LIVRABLES = ("RAPPORT_", "SYNTHESE_", "AUDIT_")

# Sous ce seuil, un rapport produit redevient du travail mort.
SEUIL_RAPPORTS = 95.0


def indexer() -> dict[str, Path]:
    idx: dict[str, Path] = {}
    for d, sd, fs in os.walk(V3):
        sd[:] = [x for x in sd if x not in EXCLUS and not x.startswith(".")]
        for f in fs:
            if f.endswith((".md", ".json")):
                idx.setdefault(f, Path(d) / f)
    return idx


def cites(p: Path, idx: dict[str, Path]) -> set[str]:
    try:
        t = p.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return set()
    return {m for m in re.findall(r"[\w\-.]+\.(?:md|json)", t) if m in idx}


def propager(idx: dict[str, Path]) -> dict[str, int]:
    """Parcours en largeur depuis les points de depart. La profondeur retenue
    est la PLUS COURTE : un document a 1 saut est reellement trouvable, a 4 il
    l'est en theorie."""
    vus: dict[str, int] = {}
    file: list[tuple[str, int]] = []
    for p in DEPARTS:
        file += [(n, 1) for n in cites(p, idx)]
    while file:
        nom, d = file.pop(0)
        if nom in vus or d > SAUTS_MAX:
            continue
        vus[nom] = d
        file += [(m, d + 1) for m in cites(idx[nom], idx) if m not in vus]
    return vus


def rapport() -> tuple[int, int, int, int, dict[str, int], list[str]]:
    idx = indexer()
    vus = propager(idx)
    livrables = [n for n in idx if n.startswith(LIVRABLES)]
    atteints = [n for n in livrables if n in vus]
    perdus = sorted(set(livrables) - set(atteints))
    return len(idx), len(vus), len(livrables), len(atteints), vus, perdus


def afficher() -> int:
    total, vus, nl, na, prof, perdus = rapport()
    pct_doc = 100 * vus / total if total else 0
    pct_liv = 100 * na / nl if nl else 0

    print(f"  documents indexes        : {total:,}")
    print(f"  atteignables (<= {SAUTS_MAX} sauts) : {vus:,}  ({pct_doc:.1f} %)")
    print()
    print(f"  livrables (RAPPORT_/SYNTHESE_/AUDIT_) : {nl}")
    print(f"  atteignables                          : {na}  ({pct_liv:.0f} %)")

    if perdus:
        print(f"\n  HORS DE PORTEE — {len(perdus)} livrable(s) :")
        for n in perdus[:12]:
            print(f"    {n}")
        if len(perdus) > 12:
            print(f"    (+{len(perdus) - 12} autres)")
        print("\n  Ils ne sont pas orphelins : ils se citent probablement entre")
        print("  eux. Ils sont hors de portee de ce qui est lu au demarrage.")
        print("  Les ajouter a un index DEJA atteignable, pas en creer un neuf.")
    else:
        print("\n  Tous les livrables sont atteignables.")
    return 1 if perdus else 0


def auto_test() -> int:
    _, _, nl, na, _, perdus = rapport()
    pct = 100 * na / nl if nl else 0
    print(f"  livrables atteignables : {na}/{nl}  ({pct:.1f} %)")
    print(f"  seuil                  : {SEUIL_RAPPORTS} %")
    if pct < SEUIL_RAPPORTS:
        print(f"\n  ECHEC : {len(perdus)} livrable(s) hors de portee.")
        print("  Un rapport produit et inatteignable a coute des jetons pour rien.")
        return 1
    print("\n  OK : la portee tient.")
    return 0


def main(argv: list[str]) -> int:
    if len(argv) > 1 and argv[1] == "--auto-test":
        return auto_test()
    return afficher()


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Ce livrable est-il verifie, ou seulement produit ?

POURQUOI CE SCRIPT EXISTE
    423 fichiers produits en deux vagues, 321 concepts OKF, zero echec sur 60
    lancements -- et aucun relu par un humain. Produire davantage n'aide plus :
    le goulot est la verification.

LA PORTE QU'IL NE FRANCHIT PAS
    Rien ne passe de `confiance: machine` a `confiance: humain` sans le
    proprietaire. Ce script CONSTATE le niveau, il ne le donne jamais.
"""

from __future__ import annotations
import os
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

V3 = Path("C:/Users/amado/ASpace_OS_V3")
BUNDLE = V3 / "40_Memory_Wiki_OKF"


def frontmatter(t: str) -> str | None:
    if not t.startswith("---"):
        return None
    fin = t.find("\n---", 3)
    return t[3:fin] if fin > 0 else None


def niveau(fm: str) -> str:
    """La regle OKF : le niveau se DEDUIT de `verified`, il ne se declare pas."""
    bloc = re.search(r"verified:(.*?)(?:\n\w|\Z)", fm, re.S)
    if not bloc:
        return "non verifie"
    corps = bloc.group(1)
    if not corps.strip():
        return "non verifie"
    return "revu par un humain" if "human:" in corps else "confirme par machine"


def liens_morts(t: str, connus: set[str]) -> list[str]:
    """Un lien [[nom]] vers un concept inexistant ment a l'avenir."""
    return sorted({m for m in re.findall(r"\[\[([^\]]+)\]\]", t) if m not in connus})


def concepts_connus() -> set[str]:
    noms = set()
    for d, sd, fs in os.walk(BUNDLE):
        sd[:] = [x for x in sd if not x.startswith(".")]
        for f in fs:
            if f.endswith(".md"):
                noms.add(f[:-3])
    return noms


def verifier(p: Path) -> int:
    try:
        t = p.read_text(encoding="utf-8", errors="ignore")
    except OSError as e:
        print(f"  illisible : {e}")
        return 2

    print(f"  {p.name}\n")
    fm = frontmatter(t)
    if fm is None:
        print("    pas de frontmatter — le niveau de confiance est indeterminable.")
        print("    Un livrable sans frontmatter OKF ne peut pas etre situe.")
        return 1

    n = niveau(fm)
    print(f"    confiance : {n}")
    if n == "revu par un humain":
        print("    ATTENTION : ce niveau ne peut etre pose QUE par le proprietaire.")

    morts = liens_morts(t, concepts_connus())
    if morts:
        print(f"\n    {len(morts)} lien(s) mort(s) :")
        for m in morts:
            print(f"      [[{m}]]")
        print("    Un lien vers un concept inexistant ment a l'avenir.")

    n_src = len(re.findall(r"A SOURCER", t))
    if n_src:
        print(f"\n    {n_src} « A SOURCER » restant(s) — le livrable est incomplet,")
        print("    et c'est correct tant que ce n'est pas presente comme fini.")

    return 1 if (morts or n == "non verifie") else 0


# DISTINCTION POSEE LE 2026-08-30 : quatre des six fichiers marques `human:`
# ne sont PAS des concepts -- ce sont la documentation du format elle-meme
# (Format spec, Bundle guide, Quickstart, Bundle index). Les compter comme des
# concepts relus gonflait le taux de revue humaine et masquait le vrai goulot.
#
# Un taux de verification calcule sur la mauvaise population est faux meme
# quand chaque ligne est vraie.
META = {"Format spec", "Bundle guide", "Quickstart", "Bundle index"}


def auto_test() -> int:
    if not BUNDLE.is_dir():
        print(f"  ECHEC : bundle introuvable — {BUNDLE}")
        return 1

    par_niveau: dict[str, int] = {}
    humains: list[tuple[str, str]] = []
    meta: list[str] = []
    total = 0

    for d, sd, fs in os.walk(BUNDLE):
        sd[:] = [x for x in sd if not x.startswith(".")]
        for f in fs:
            if not f.endswith(".md"):
                continue
            p = Path(d) / f
            try:
                t = p.read_text(encoding="utf-8", errors="ignore")
            except OSError:
                continue
            fm = frontmatter(t)
            if fm is None:
                continue
            mt = re.search(r"^type:\s*(.+)$", fm, re.M)
            ty = mt.group(1).strip() if mt else ""
            if ty in META:
                meta.append(f)
                continue
            total += 1
            n = niveau(fm)
            par_niveau[n] = par_niveau.get(n, 0) + 1
            if n == "revu par un humain":
                who = re.findall(r"human:([\w\-.]+)", fm)
                humains.append((f, ", ".join(who) or "(non nomme)"))

    print(f"  {total} concepts avec frontmatter")
    if meta:
        print(f"  ({len(meta)} fichiers de doc du format exclus du compte : "
              f"{', '.join(sorted(meta))})")
    print()
    for k in ("non verifie", "confirme par machine", "revu par un humain"):
        print(f"    {par_niveau.get(k, 0):>4}  {k}")

    if humains:
        print(f"\n  {len(humains)} marque(s) « revu par un humain » :")
        for f, who in humains:
            print(f"    {f}  →  {who}")
        anonymes = [f for f, w in humains if w == "(non nomme)"]
        if anonymes:
            print(f"\n  ECHEC : {len(anonymes)} human: sans identifiant.")
            print("  Un « revu par un humain » non attribuable fait passer du")
            print("  suppose pour du mesure. C'est D2 qui s'effondre.")
            return 1
    else:
        print("\n  Aucun concept revu par un humain.")
        print("  C'est le goulot P6, et il est honnetement affiche.")

    # Le chiffre qui rend P6 lisible. Sans lui, on lit « 2 concepts revus »
    # comme une bonne nouvelle au lieu d'un taux de 8 %.
    revus = par_niveau.get("revu par un humain", 0)
    pct = 100 * revus / total if total else 0
    print(f"\n  Taux de revue humaine : {revus}/{total} concepts = {pct:.0f} %.")
    print("  C'est P6 chiffre : la production depasse la verification.")
    print("\n  OK.")
    return 0


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print(__doc__)
        print("  usage : verifier.py <fichier.md> | verifier.py --auto-test")
        return 2
    if argv[1] == "--auto-test":
        return auto_test()
    return verifier(Path(argv[1]))


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

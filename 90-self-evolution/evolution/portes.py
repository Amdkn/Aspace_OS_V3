#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Les portes G1-G5. Une skill qui ne les franchit pas n'entre pas.

POURQUOI CE SCRIPT EXISTE
    Le depot hermes-agent-self-evolution fait passer chaque candidat par des
    contraintes avant acceptation. Ici les memes portes valent pour une skill
    ecrite a la main : sans quoi « ancree dans une mesure » resterait une
    intention et pas un critere.

CE QU'IL NE FAIT PAS
    G6 -- la revue humaine -- n'est pas ici et ne le sera pas. Rien ne passe
    de `confiance: machine` a `confiance: humain` sans le proprietaire.
"""

from __future__ import annotations
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

RACINE = Path(__file__).resolve().parent.parent
SKILLS = RACINE / "skills"
V3 = RACINE.parent

TAILLE_MAX = 15 * 1024
SECTIONS = ["Quand l'utiliser", "Pourquoi elle existe", "Procédure",
            "Pièges", "Vérification"]


def frontmatter(t: str) -> str:
    if not t.startswith("---"):
        return ""
    fin = t.find("\n---", 3)
    return t[3:fin] if fin > 0 else ""


def controler(d: Path) -> list[tuple[str, bool, str]]:
    """Rend (porte, passe, detail). Une porte qui ne peut pas echouer ne
    controle rien : chacune ici a un cas d'echec reel."""
    r: list[tuple[str, bool, str]] = []
    f = d / "SKILL.md"
    if not f.exists():
        return [("G0 SKILL.md", False, "absent")]

    t = f.read_text(encoding="utf-8", errors="ignore")
    fm = frontmatter(t)

    # G1 — ancrage mesure. Une skill sans repere ni source n'a pas sa place.
    rep = re.search(r"problematiques:\s*\[([^\]]*)\]", fm)
    mes = re.search(r"mesure:\s*\"?([^\"\n]+)", fm)
    src = re.search(r"source:\s*\"?([^\"\n]+)", fm)
    chiffre = bool(mes and re.search(r"\d", mes.group(1)))
    src_ok = False
    if src:
        chemin = src.group(1).split("§")[0].strip().strip('"')
        src_ok = (V3 / chemin).exists()
    ok1 = bool(rep and rep.group(1).strip()) and chiffre and src_ok
    detail = []
    if not (rep and rep.group(1).strip()):
        detail.append("pas de repere")
    if not chiffre:
        detail.append("mesure sans chiffre")
    if not src_ok:
        detail.append("source introuvable")
    r.append(("G1 ancrage mesure", ok1, ", ".join(detail) or
              f"{rep.group(1)} — source verifiee"))

    # G2 — verification executable.
    #
    # TROU BOUCHE LE 2026-08-30 : cette porte cherchait la CHAINE « --auto-test »
    # et validait un fichier qui ne compilait meme pas (SyntaxError sur un \n mal
    # echappe). Une porte qui verifie la presence d'un mot valide une promesse,
    # pas un test. On compile desormais.
    scripts = list((d / "scripts").glob("*.py")) if (d / "scripts").is_dir() else []
    avec_test, casses = [], []
    for s in scripts:
        src = s.read_text(encoding="utf-8", errors="ignore")
        try:
            compile(src, str(s), "exec")
        except SyntaxError as e:
            casses.append(f"{s.name} l.{e.lineno}")
            continue
        if "--auto-test" in src:
            avec_test.append(s)
    ok2 = bool(avec_test) and not casses
    det = f"{len(avec_test)}/{len(scripts)} script(s) avec --auto-test"
    if casses:
        det = f"NE COMPILE PAS : {', '.join(casses)}"
    r.append(("G2 test executable", ok2, det))

    # G3 — taille.
    o = f.stat().st_size
    r.append(("G3 taille <= 15 Ko", o <= TAILLE_MAX, f"{o / 1024:.1f} Ko"))

    # G4 — structure.
    manque = [s for s in SECTIONS if f"# {s}" not in t]
    r.append(("G4 structure", not manque,
              "complete" if not manque else f"manque : {', '.join(manque)}"))

    # G5 — soustraction nommee.
    sous = bool(re.search(r"remplace|retire|au lieu de|plut[oô]t que|ne doivent plus",
                          t, re.I))
    r.append(("G5 soustraction", sous,
              "nommee" if sous else "aucune soustraction — B4 non respecte"))
    return r


def main() -> int:
    dossiers = sorted(p for p in SKILLS.iterdir() if p.is_dir())
    if not dossiers:
        print(f"  aucune skill dans {SKILLS}")
        return 1

    echecs = 0
    for d in dossiers:
        res = controler(d)
        n_ok = sum(1 for _, ok, _ in res if ok)
        marque = "OK  " if n_ok == len(res) else "STOP"
        print(f"  {marque} {d.name}   {n_ok}/{len(res)}")
        for porte, ok, det in res:
            if not ok:
                print(f"         {porte} : {det}")
                echecs += 1
    print()
    if echecs:
        print(f"  {echecs} porte(s) fermee(s). Une skill qui ne les franchit")
        print("  pas n'entre pas — corriger, ou retirer la skill.")
        return 1

    print(f"  {len(dossiers)} skills, portes G1-G5 franchies.")
    print()
    print("  G6 — revue humaine — n'est pas scriptee et ne le sera pas.")
    print("  Rien ne passe de `confiance: machine` a `confiance: humain`")
    print("  sans le proprietaire. C'est le seul verrou qu'aucun script")
    print("  ne peut poser a sa place.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

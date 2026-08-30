#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Rejoue les 16 defauts mesures contre les scripts actuels.

POURQUOI CE SCRIPT EXISTE
    Un jeu d'evaluation qu'on ne rejoue pas est une archive. Celui-ci sert a
    UNE chose : verifier qu'un changement de sonde ne reintroduit pas un
    defaut deja paye.

CE QU'IL FAIT VRAIMENT
    Pour les defauts dont le correctif est verifiable dans le code, il verifie
    que le correctif est TOUJOURS la. Pour les autres, il le dit au lieu de
    faire semblant -- un validateur qui rend « 16/16 » sans rien tester serait
    exactement le defaut E11 : une porte qui valide une promesse.
"""

from __future__ import annotations
import json
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ICI = Path(__file__).resolve().parent
V3 = ICI.parent.parent
JEU = ICI / "echecs_instruments.jsonl"

# Pour chaque defaut : le fichier qui doit porter le correctif, et le motif qui
# prouve qu'il y est encore. Un defaut sans regle verifiable est declare tel.
REGLES: dict[str, tuple[str, str, str]] = {
    "E01": ("scripts/cartographier_v3.py", r"REPARSE_POINT|0x400",
            "garde de jonction NTFS"),
    "E02": ("scripts/cartographier_v3.py", r"cumul\(\)",
            "cumul du noeud au lieu du compte direct"),
    "E05": ("90-self-evolution/skills/p2-mandat-persistant/scripts/mandat.py",
            r"NFKD", "normalisation des accents"),
    "E06": ("90-self-evolution/skills/p5-plancher-contexte/scripts/plancher.py",
            r"non mesurable depuis le disque|RELEVE",
            "mesure et releve tenus separes"),
    "E07": ("90-self-evolution/skills/p4-instrument-honnete/scripts/auditer.py",
            r"reconfigure\(encoding", "sortie forcee en utf-8"),
    "E08": ("90-self-evolution/skills/p3-point-entree/scripts/portee.py",
            r"propager|SAUTS_MAX", "atteignabilite, pas liens entrants"),
    "E09": ("90-self-evolution/skills/p1-anti-rejeu/scripts/deja_vu.py",
            r"Jaccard|j >= 0\.55", "repli sur recouvrement"),
    "E10": ("90-self-evolution/skills/p2-mandat-persistant/scripts/mandat.py",
            r"ne redemande", "formulations equivalentes couvertes"),
    "E11": ("90-self-evolution/evolution/portes.py", r"compile\(src",
            "la porte compile au lieu de chercher un mot"),
    "E12": ("90-self-evolution/skills/p8-forum-agents/scripts/forum.py",
            r"reservation_active|PEREMPTION", "reservation avec peremption"),
    "E13": ("90-self-evolution/skills/p5-plancher-contexte/SKILL.md",
            r"strict-mcp-config", "les deux drapeaux MCP"),
    "E15": ("scripts/extraire_verbes.py", r"<\[\^>\]\+>",
            "forme Turtle stricte exigee"),
    "E16": ("scripts/extraire_verbes.py", r"govern|steward",
            "motifs bilingues"),
}

# Defauts sans regle statique : le correctif vit ailleurs que dans un fichier
# de ce depot. On les nomme plutot que de les compter comme passes.
HORS_PORTEE = {
    "E03": "correctif dans agent-os/desktop (hors de ce depot)",
    "E04": "sonde PowerShell abandonnee — rien a verifier statiquement",
    "E14": "geste de session (lire les fichiers indexes, pas le diff)",
}


def main() -> int:
    if not JEU.exists():
        print(f"  jeu introuvable : {JEU}")
        return 1

    cas = [json.loads(L) for L in JEU.read_text(encoding="utf-8").splitlines() if L.strip()]
    print(f"  {len(cas)} defauts mesures\n")

    tenus, rompus, non_verifiables = [], [], []
    for c in cas:
        ident = c["id"]
        if ident in HORS_PORTEE:
            non_verifiables.append((ident, HORS_PORTEE[ident]))
            continue
        if ident not in REGLES:
            non_verifiables.append((ident, "aucune regle definie"))
            continue

        rel, motif, quoi = REGLES[ident]
        f = V3 / rel
        try:
            src = f.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            rompus.append((ident, quoi, f"fichier absent : {rel}"))
            continue
        if re.search(motif, src):
            tenus.append((ident, quoi))
        else:
            rompus.append((ident, quoi, f"correctif absent de {rel}"))

    for ident, quoi in tenus:
        print(f"    OK    {ident}  {quoi}")
    for ident, quoi, det in rompus:
        print(f"    ROMPU {ident}  {quoi} — {det}")
    for ident, quoi in non_verifiables:
        print(f"    --    {ident}  non verifiable ici : {quoi}")

    print(f"\n  {len(tenus)} correctifs tenus · {len(rompus)} rompus · "
          f"{len(non_verifiables)} non verifiables")

    if rompus:
        print("\n  ECHEC : un defaut deja paye peut se rejouer.")
        print("  Restaurer le correctif — ne pas retirer la regle.")
        return 1

    print("\n  Aucun defaut connu n'est reintroduit.")
    print(f"  {len(non_verifiables)} cas restent hors de portee d'un controle")
    print("  statique, et c'est ecrit plutot que compte comme reussi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Ce qui est charge AVANT le premier mot.

POURQUOI CE SCRIPT EXISTE
    Plancher mesure : ~96k tokens d'outillage sur une fenetre de 200k, dont
    60,2k pour 195 outils MCP. Ce n'est pas qu'une ligne de facture : le
    2026-08-30 il a fait echouer un delegue DEUX fois sur « Prompt is too
    long », avant meme qu'il lise son brief.

CE QU'IL MESURE, ET CE QU'IL NE MESURE PAS
    Les fichiers sur le disque : mesure exacte. Le plancher d'outillage MCP :
    NON mesurable depuis le disque -- il depend de la session. La valeur
    affichee vient d'un releve /context date, et elle est etiquetee comme tel.
    Melanger les deux donnerait un total precis et faux.
"""

from __future__ import annotations
import json
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

MAISON = Path("C:/Users/amado")
V3 = MAISON / "ASpace_OS_V3"

DEMARRAGE = [
    MAISON / "CLAUDE.md",
    MAISON / ".claude" / "CLAUDE.md",
    V3 / "CLAUDE.md",
]

# Au-dela, le mandat coute plus qu'il ne rapporte : deplacer vers un fichier
# lu a la demande. Ce n'est pas une limite technique, c'est un arbitrage.
SEUIL_FICHIERS = 8000

# RELEVE /context du 2026-08-30, PAS une mesure de ce script.
OUTILLAGE_RELEVE = {
    "outils MCP (195)": 60_200,
    "outils systeme": 20_900,
    "prompt systeme": 6_000,
    "skills": 2_000,
}


def tokens(p: Path) -> int:
    try:
        return len(p.read_text(encoding="utf-8", errors="ignore")) // 4
    except OSError:
        return 0


def mesurer() -> int:
    print("  MESURE — fichiers sur le disque, relus a l'instant\n")
    total = 0
    for p in DEMARRAGE:
        t = tokens(p)
        total += t
        etat = f"~{t:>5} tok" if t else "   ABSENT"
        print(f"    {etat}   {p}")
    print(f"\n    total fichiers : ~{total:,} tokens")

    print("\n  RELEVE — /context du 2026-08-30, non mesurable depuis le disque\n")
    outil = sum(OUTILLAGE_RELEVE.values())
    for k, v in OUTILLAGE_RELEVE.items():
        print(f"    ~{v:>6,} tok   {k}")
    print(f"\n    plancher outillage : ~{outil:,} tokens")

    print(f"\n  Ces deux blocs ne se somment pas a l'aveugle : le premier est")
    print(f"  mesure, le second releve. Ordre de grandeur du plancher total :")
    print(f"  ~{(total + outil) // 1000}k sur une fenetre de 200k.")

    # Les serveurs MCP declares : eux sont sur le disque, donc mesurables.
    try:
        srv = json.loads((MAISON / ".mcp.json").read_text(encoding="utf-8"))
        n = len(srv.get("mcpServers", {}))
        print(f"\n  {n} serveurs MCP declares dans ~/.mcp.json.")
        print("  Chacun charge ses schemas d'outils au demarrage.")
    except (OSError, json.JSONDecodeError):
        pass

    print("\n  Pour deleguer sans payer ce plancher, les DEUX drapeaux :")
    print("    --strict-mcp-config --mcp-config '{\"mcpServers\":{}}'")
    return 0


def auto_test() -> int:
    total = sum(tokens(p) for p in DEMARRAGE)
    print(f"  cout de demarrage (fichiers) : ~{total:,} tokens")
    print(f"  seuil                        : {SEUIL_FICHIERS:,}")
    if total > SEUIL_FICHIERS:
        print(f"\n  ECHEC : depassement de {total - SEUIL_FICHIERS:,} tokens.")
        print("  Chaque ligne en trop est payee a CHAQUE session, pour toujours.")
        print("  Deplacer vers un fichier lu a la demande.")
        return 1
    marge = SEUIL_FICHIERS - total
    print(f"\n  OK : marge de {marge:,} tokens (~{marge // 12} lignes).")
    return 0


def main(argv: list[str]) -> int:
    if len(argv) > 1 and argv[1] == "--auto-test":
        return auto_test()
    return mesurer()


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

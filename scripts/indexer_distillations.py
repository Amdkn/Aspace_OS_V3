#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Rend les distillations atteignables depuis le point d'entree.

LE PROBLEME MESURE (2026-08-30)
    130 rapports de distillation existent, 2,4 Mo, produits par des agents
    delegues. Aucun n'est orphelin : ils se citent entre eux. Mais seuls **13**
    sont atteignables en 4 sauts depuis les deux `CLAUDE.md` -- les 117 autres
    vivent dans une boucle fermee que rien de ce qui est lu au demarrage
    n'atteint.

    Un document produit et inatteignable a coute des jetons pour rien. Ce n'est
    pas un probleme de rangement : c'est du travail mort.

CE QUE FAIT CE SCRIPT
    Un index unique, a UN saut du `CLAUDE.md`, qui liste chaque rapport avec sa
    date, son poids et sa premiere ligne utile. Regenerable : une liste ecrite
    a la main vieillit des le rapport suivant.
"""

from __future__ import annotations
import os, re, stat
from datetime import datetime, timezone
from pathlib import Path

RACINE = Path("C:/Users/amado/ASpace_OS_V3")
SORTIE = RACINE / "INDEX_DISTILLATIONS.md"
EXCLUS = {"node_modules", ".git", "openwiki", "__pycache__", ".venv", "dist", "build"}

# Ce qu'on indexe : les livrables d'agents delegues, pas les briefs qui les
# commandent. Un brief dit quoi faire ; un rapport dit ce qui a ete trouve.
MOTIFS = ("RAPPORT_", "SYNTHESE_", "AUDIT_")


def premiere_ligne_utile(p: Path) -> str:
    """Le titre, ou la premiere phrase reelle. On saute le frontmatter : un
    index qui affiche `---` pour cinquante entrees n'aide personne."""
    try:
        lignes = p.read_text(encoding="utf-8", errors="ignore").splitlines()
    except OSError:
        return "(illisible)"
    i = 0
    if lignes and lignes[0].strip() == "---":            # frontmatter YAML
        i = 1
        while i < len(lignes) and lignes[i].strip() != "---":
            i += 1
        i += 1
    for L in lignes[i:i + 40]:
        s = L.strip().lstrip("#").strip()
        if len(s) > 25 and not s.startswith(("|", ">", "```", "-", "*")):
            return s[:150]
    return "(pas de resume)"


def main() -> int:
    t0 = datetime.now(timezone.utc)
    trouves: list[Path] = []
    for d, sd, fs in os.walk(RACINE):
        sd[:] = [x for x in sd if x not in EXCLUS and not x.startswith(".")]
        for f in fs:
            if f.endswith(".md") and any(f.startswith(m) for m in MOTIFS):
                trouves.append(Path(d) / f)

    # Groupes par dossier parent : c'est la vague qui les a produits.
    par_vague: dict[str, list[Path]] = {}
    for p in trouves:
        rel = p.parent.relative_to(RACINE).as_posix() or "."
        par_vague.setdefault(rel, []).append(p)

    total_o = sum(p.stat().st_size for p in trouves)
    L = [
        "# Index des distillations — les rapports d'agents délégués",
        "",
        f"> Généré par `scripts/indexer_distillations.py` le "
        f"{t0.strftime('%Y-%m-%d %H:%M')} UTC. **Ne pas éditer à la main.**",
        "",
        "## Pourquoi ce fichier existe",
        "",
        f"**{len(trouves)} rapports, {total_o/1024:.0f} Ko**, produits par des agents",
        "délégués sur plusieurs vagues. Mesure du 2026-08-30 : aucun n'était",
        "orphelin — ils se citaient entre eux — mais **seuls 13 sur 130 étaient",
        "atteignables** en 4 sauts depuis les `CLAUDE.md`. Les 117 autres vivaient",
        "dans une boucle fermée que rien de ce qui est lu au démarrage n'atteignait.",
        "",
        "Un document produit et inatteignable a coûté des jetons pour rien. Cet",
        "index les ramène à **un saut** du point d'entrée.",
        "",
        f"## Les {len(par_vague)} vagues",
        "",
        "| Vague | Rapports | Poids |",
        "|---|---:|---:|",
    ]
    for v in sorted(par_vague, key=lambda x: (-len(par_vague[x]), x)):
        ps = par_vague[v]
        L.append(f"| `{v}` | {len(ps)} | {sum(p.stat().st_size for p in ps)/1024:.0f} Ko |")

    L += ["", "## Le détail", ""]
    for v in sorted(par_vague, key=lambda x: (-len(par_vague[x]), x)):
        L.append(f"### `{v}`")
        L.append("")
        for p in sorted(par_vague[v]):
            rel = p.relative_to(RACINE).as_posix()
            ko = p.stat().st_size / 1024
            date = datetime.fromtimestamp(p.stat().st_mtime).strftime("%Y-%m-%d")
            L.append(f"- [{p.name}]({rel}) — {date}, {ko:.0f} Ko — "
                     f"{premiere_ligne_utile(p)}")
        L.append("")

    L += ["## Comment vérifier que rien n'est retombé hors de portée", "",
          "```bash",
          "python C:/Users/amado/ASpace_OS_V3/scripts/indexer_distillations.py",
          "```", "",
          "Si le compte diffère d'un `find` sur `RAPPORT_*.md`, c'est l'instrument",
          "qu'il faut réparer, pas le chiffre qu'il faut ajuster.", ""]

    SORTIE.write_text("\n".join(L), encoding="utf-8")
    print(f"  {len(trouves)} rapports, {len(par_vague)} vagues, {total_o/1024:.0f} Ko")
    print(f"  ecrit : {SORTIE} ({SORTIE.stat().st_size:,} o)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Cartographie mesuree de ASpace_OS_V3 — l'arborescence profonde, comptee.

POURQUOI CE SCRIPT EXISTE
    Le `CLAUDE.md` racine donne une table de points d'entree mais aucune carte.
    Consequence mesuree : chaque session redecouvre l'arborescence a l'aveugle,
    au prix du quota, et conclut « non documente » sur ce qui existe.

    Une carte ecrite a la main vieillit et ment. Celle-ci se regenere.

GARDE DE JONCTION
    `os.path.islink()` ne voit pas les jonctions NTFS. Un parcours naif suit le
    lien et recompte la cible : 13,8 millions de fichiers la ou il y en a
    14 613. Le garde est `FILE_ATTRIBUTE_REPARSE_POINT`, pas `islink`.
"""

from __future__ import annotations
import os, stat, sys, collections
from datetime import datetime, timezone
from pathlib import Path

RACINE = Path("C:/Users/amado/ASpace_OS_V3")
SORTIE = RACINE / "CARTOGRAPHIE.md"

# Ce qui bruite sans informer. `openwiki` est un clone amont avec son propre
# .git : le compter melangerait un depot etranger au corpus.
EXCLUS = {
    "node_modules", ".git", ".venv", "venv", "__pycache__", "dist", "build",
    ".next", ".nuxt", "target", "vendor", "coverage", ".cache", "site-packages",
    ".obsidian", ".pytest_cache", ".mypy_cache", "openwiki",
}

RP = getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400)
PROFONDEUR_ARBRE = 3          # au-dela, on compte sans dessiner


def est_jonction(e) -> bool:
    try:
        return bool(e.stat(follow_symlinks=False).st_file_attributes & RP)
    except (OSError, AttributeError):
        return False


class Noeud:
    __slots__ = ("nom", "chemin", "fichiers", "octets", "enfants",
                 "md", "ttl", "jsonl", "py", "jonction")

    def __init__(self, nom: str, chemin: Path):
        self.nom, self.chemin = nom, chemin
        self.fichiers = self.octets = self.md = self.ttl = self.jsonl = self.py = 0
        self.enfants: list[Noeud] = []
        self.jonction = False

    def cumul(self) -> tuple[int, int, int]:
        """(fichiers, octets, md) de ce noeud et de toute sa descendance."""
        f, o, m = self.fichiers, self.octets, self.md
        for e in self.enfants:
            a, b, c = e.cumul()
            f += a; o += b; m += c
        return f, o, m


def parcourir(d: Path, nom: str, profondeur: int = 0) -> Noeud:
    n = Noeud(nom, d)
    try:
        entrees = list(os.scandir(d))
    except OSError:
        return n
    for e in entrees:
        try:
            if e.is_dir(follow_symlinks=False):
                if e.name in EXCLUS or e.name.startswith("."):
                    continue
                if est_jonction(e):
                    # On la SIGNALE sans la suivre : la taire ferait croire a
                    # une lacune, la suivre ferait exploser le compte.
                    j = Noeud(e.name, Path(e.path)); j.jonction = True
                    n.enfants.append(j)
                    continue
                n.enfants.append(parcourir(Path(e.path), e.name, profondeur + 1))
            elif e.is_file(follow_symlinks=False):
                n.fichiers += 1
                try: n.octets += e.stat(follow_symlinks=False).st_size
                except OSError: pass
                nm = e.name.lower()
                if   nm.endswith(".md"):    n.md += 1
                elif nm.endswith(".ttl"):   n.ttl += 1
                elif nm.endswith(".jsonl"): n.jsonl += 1
                elif nm.endswith(".py"):    n.py += 1
        except OSError:
            continue
    n.enfants.sort(key=lambda x: x.nom)
    return n


def humain(o: int) -> str:
    for u in ("o", "Ko", "Mo", "Go"):
        if o < 1024 or u == "Go":
            return f"{o:.0f} {u}" if u == "o" else f"{o:.1f} {u}"
        o /= 1024
    return f"{o:.1f} Go"


def dessiner(n: Noeud, lignes: list[str], prefixe: str = "", profondeur: int = 0):
    for i, e in enumerate(n.enfants):
        dernier = i == len(n.enfants) - 1
        branche = "`-- " if dernier else "|-- "
        if e.jonction:
            lignes.append(f"{prefixe}{branche}{e.nom}/  -> JONCTION (non suivie)")
            continue
        f, o, m = e.cumul()
        det = f"{f} fich."
        if m: det += f", {m} md"
        if o: det += f", {humain(o)}"
        lignes.append(f"{prefixe}{branche}{e.nom}/  ({det})")
        if profondeur + 1 < PROFONDEUR_ARBRE and e.enfants:
            dessiner(e, lignes, prefixe + ("    " if dernier else "|   "), profondeur + 1)
        elif e.enfants:
            sd = sum(1 for _ in e.enfants)
            lignes.append(f"{prefixe}{'    ' if dernier else '|   '}"
                          f"... {sd} sous-dossiers, non deplies")


def main() -> int:
    if not RACINE.is_dir():
        print(f"ERREUR : {RACINE} introuvable"); return 1

    t0 = datetime.now(timezone.utc)
    arbre = parcourir(RACINE, RACINE.name)
    ms = (datetime.now(timezone.utc) - t0).total_seconds()

    tf, to, tm = arbre.cumul()

    # Extensions, tous niveaux — dit ce que le corpus EST, pas ce qu'on croit.
    exts = collections.Counter()
    def compter(n: Noeud):
        exts["md"] += n.md; exts["ttl"] += n.ttl
        exts["jsonl"] += n.jsonl; exts["py"] += n.py
        for e in n.enfants:
            if not e.jonction: compter(e)
    compter(arbre)

    lignes = [
        "# Cartographie de A'Space OS V3",
        "",
        f"> Genere par `scripts/cartographier_v3.py` le "
        f"{t0.strftime('%Y-%m-%d %H:%M')} UTC, en {ms:.1f} s.",
        "> **Ne pas editer a la main** : une carte ecrite a la main vieillit et ment.",
        "> Regenerer par `python scripts/cartographier_v3.py`.",
        "",
        "## Le corpus en un coup d'oeil",
        "",
        "| | |",
        "|---|---|",
        f"| Fichiers | **{tf:,}** |",
        f"| Poids | **{humain(to)}** |",
        f"| Documents `.md` | **{exts['md']:,}** |",
        f"| Triplets `.ttl` | {exts['ttl']:,} |",
        f"| Substrat `.jsonl` | {exts['jsonl']:,} |",
        f"| Scripts `.py` | {exts['py']:,} |",
        "",
        "Exclus du compte : " + ", ".join(f"`{x}`" for x in sorted(EXCLUS)) + ".",
        "",
        "`openwiki/` est exclu volontairement : c'est un **clone amont** avec son",
        "propre `.git`, pas une partie du corpus. Le compter melangerait un depot",
        "etranger au notre.",
        "",
        "## Les etages de premier niveau",
        "",
        "| Etage | Fichiers | dont `.md` | Poids | Ce qu'il porte |",
        "|---|---:|---:|---:|---|",
    ]

    ROLES = {
        "00_Amadeus": "Ontologie V2, MEMORY_CORE, cartographie des contradictions, sessions",
        "10_Tech_OS": "Gouvernance Rick, cascade E-Myth",
        "20_Harness": "agentgateway et sources MCP",
        "20_Life_OS": "Domaines de vie migres depuis V2",
        "30_Business_OS": "Projets, blueprints, coach-os",
        "40_Memory_Wiki_OKF": "Bundle OKF v0.2 — integrations, operations, securite, learning",
        "50_Distillation": "Methode, substrat, briefs de distillation",
        "_ARCHIVE_coach-os-briefs": "Briefs archives de coach-os",
        "_INBOX": "Capture GTD, non trie",
        "_REVIEW_NOTEBOOKLM": "26 sources consolidees pour la revue humaine",
        "60_Implementation_Méthodologiques": "Verdicts du triptyque par domaine",
        "70_Onthologies": "Sujets, triplets RDF, revue",
        "80_Agent-OS": "Observabilite — tableaux de revue et schema de cadence",
        "90-self-evolution": "Skills d'auto-amelioration — une par problematique mesuree",
    "scripts": "Porte d'argent, cartographie, generateurs",
    }
    for e in sorted(arbre.enfants, key=lambda x: x.nom):
        if e.jonction:
            lignes.append(f"| `{e.nom}/` | — | — | — | **jonction, non suivie** |")
            continue
        f, o, m = e.cumul()
        lignes.append(f"| `{e.nom}/` | {f:,} | {m:,} | {humain(o)} | "
                      f"{ROLES.get(e.nom, '—')} |")
    if arbre.fichiers:
        lignes.append(f"| *(racine)* | {arbre.fichiers} | {arbre.md} | "
                      f"{humain(arbre.octets)} | fichiers de tete |")

    lignes += ["", f"## Arborescence, {PROFONDEUR_ARBRE} niveaux", "",
               "```", f"{arbre.nom}/"]
    dessiner(arbre, lignes)
    lignes += ["```", ""]

    # Les dix dossiers les plus lourds en .md, tous niveaux confondus : c'est la
    # que vit la connaissance, et ce n'est pas toujours ou on l'attend.
    plats: list[tuple[int, str]] = []
    def aplatir(n: Noeud, chemin: str):
        if n.md:
            plats.append((n.md, chemin))
        for e in n.enfants:
            if not e.jonction:
                aplatir(e, f"{chemin}/{e.nom}")
    aplatir(arbre, "")
    plats.sort(reverse=True)

    # Deux classements, parce qu'un seul mentirait. Les vidages de sessions
    # ecrasent tout en volume sans etre de la connaissance redigee : les melanger
    # ferait conclure que le corpus n'est qu'un tas de transcriptions.
    sessions = [(m, c) for m, c in plats if "sessions_md" in c]
    redige = [(m, c) for m, c in plats if "sessions_md" not in c]
    md_sessions = max((m for m, _ in sessions), default=0)

    lignes += ["## Ou vit reellement la connaissance", "",
               "Deux classements, parce qu'un seul mentirait. Les vidages de sessions",
               "ecrasent tout en volume sans etre de la connaissance **redigee**.", "",
               "### Connaissance redigee (hors sessions)", "",
               "| Dossier | `.md` |", "|---|---:|"]
    for m, c in redige[:12]:
        lignes.append(f"| `{c.lstrip('/') or '(racine)'}` | {m:,} |")

    lignes += ["", "### Vidages de sessions (matiere premiere, pas connaissance)", "",
               "| Dossier | `.md` |", "|---|---:|"]
    for m, c in sessions[:5]:
        lignes.append(f"| `{c.lstrip('/') or '(racine)'}` | {m:,} |")

    # Le cumul du nœud, pas son compte direct : les concepts vivent dans
    # operations/, integrations/, learning/... Le compte direct ne porterait
    # que index.md, OKF.md, quickstart.md — il aurait dit 0,1 % et menti.
    def trouver_okf(n: Noeud):
        if n.nom == "40_Memory_Wiki_OKF":
            return n
        for e in n.enfants:
            if not e.jonction:
                r = trouver_okf(e)
                if r:
                    return r
        return None

    noeud_okf = trouver_okf(arbre)
    okf = noeud_okf.cumul()[2] if noeud_okf else 0
    pct = 100 * okf / exts["md"] if exts["md"] else 0
    lignes += ["", "### Le point qui compte", "",
               f"Le `CLAUDE.md` designe `40_Memory_Wiki_OKF/` comme « la memoire du",
               f"poste ». Ce bundle porte **{okf} fichiers `.md` sur {exts['md']:,}**, "
               f"soit **{pct:.1f} %** du corpus.",
               "",
               "Chercher la et s'arreter, c'est manquer le reste. Le bundle est un",
               "**index de concepts consolides**, pas le corpus. Les deux tableaux",
               "ci-dessus disent ou chercher avant lui."]

    lignes += ["", "## Comment verifier que cette carte dit vrai", "",
               "```bash",
               "python C:/Users/amado/ASpace_OS_V3/scripts/cartographier_v3.py",
               "```", "",
               "Si un compte differe d'un `find` sur le corpus, c'est **l'instrument**",
               "qu'il faut reparer, pas le chiffre qu'il faut ajuster.", ""]

    SORTIE.write_text("\n".join(lignes), encoding="utf-8")
    print(f"  {tf:,} fichiers, {exts['md']:,} md, {humain(to)} — en {ms:.1f}s")
    print(f"  ecrit : {SORTIE} ({SORTIE.stat().st_size:,} o)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

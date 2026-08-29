#!/usr/bin/env python
"""
jsonl_vers_md.py — convertit les sessions Claude Code en corpus lisible.

POURQUOI CE FICHIER EXISTE

769 fichiers `.jsonl`, 971 Mo, dans `~/.claude/projects/`. C'est la trace de
tout ce qui a ete decide avec un agent depuis le debut — et c'est illisible :
un evenement JSON par ligne, avec les appels d'outils et leurs resultats qui
noient les decisions sous le bruit d'execution.

La reconstitution de la meta-ontologie des trois couches a ete demandee
plusieurs fois. Elle echouait toujours au meme endroit : **le corpus n'existait
pas.** On repartait des SDD de Geordi — qui sont une archive, pas le canon — et
on ramenait une ontologie perimee dans un depot a jour. Constate le 2026-08-13 :
`SDD-006` ne connait que 7 domaines Business alors que `src/apps/sales/` existe
depuis des semaines.

Ce script ne fait qu'une chose : rendre les 769 sessions lisibles, une par
fichier `.md`, avec les messages humains et les reponses, sans les outils.

CE QU'IL GARDE ET CE QU'IL JETTE

Garde : les messages de l'utilisateur, les reponses en texte de l'assistant.
Jette : les appels d'outils, leurs resultats, les rappels systeme, les blocs de
`thinking`, et les messages qui ne sont qu'un dump JSON.

Le ratio est de l'ordre de 1 a 20 : c'est ce qui rend le corpus analysable.

USAGE

    python jsonl_vers_md.py            # convertit tout
    python jsonl_vers_md.py --depuis 2026-07-01
"""

from __future__ import annotations
import io, json, os, sys
from datetime import datetime
from pathlib import Path

# Les sessions ne vivent pas toutes sous ~/.claude/projects : Codex, Ori et le
# depot lui-meme en portent aussi. Mesure du 2026-08-29 : 1085 + 52 + 11 + 28.
# N'en convertir qu'une source laisse le reste mourir avec la retention.
SOURCES = [
    Path("C:/Users/amado/.claude/projects"),
    Path("C:/Users/amado/.codex"),
    Path("C:/Users/amado/.ori"),
]
SORTIE = Path(__file__).resolve().parent / "sessions_md"

# CORRECTION DU 2026-08-29 — ce seuil etait a 2, avec pour motif qu'« une
# session d'un seul message n'apprend rien ». C'etait faux, et cher : sur 1085
# sessions, **954 n'ont qu'un seul message humain, dont 762 depassent 200
# caracteres**. Ce sont les briefs de delegation (« Tu es Geordi, officier
# Resources… »), c'est-a-dire l'intention elle-meme, ecrite une fois et jamais
# reprise. Le filtre a 2 les jetait toutes -- 89 % du corpus.
MIN_MESSAGES = 1
# Une session d'un seul message n'est gardee que si ce message dit quelque
# chose : « hi » ou « continue » ne sont pas une intention.
MIN_CARACTERES_SI_UNIQUE = 200
COUPE_REPONSE = 6000      # une reponse d'assistant au-dela n'ajoute que du bruit

def texte(contenu) -> str:
    if isinstance(contenu, str):
        return contenu
    if isinstance(contenu, list):
        return "\n".join(
            b.get("text", "") for b in contenu
            if isinstance(b, dict) and b.get("type") == "text"
        )
    return ""

def rejete(t: str) -> bool:
    """Bruit qui n'est pas une parole : rappels systeme, dumps, resultats."""
    t = t.strip()
    if not t:
        return True
    if t.startswith(("<system-reminder>", "Caveat:", "[{", '{"', "<local-command")):
        return True
    if "<task-notification>" in t[:200]:
        return True
    return False

def convertir(src: Path, dst: Path) -> tuple[int, int]:
    nu = na = 0
    caracteres_humains = 0
    lignes: list[str] = []
    premier = dernier = None
    with io.open(src, encoding="utf-8", errors="replace") as f:
        for ligne in f:
            try:
                e = json.loads(ligne)
            except Exception:
                continue
            ts = e.get("timestamp")
            if ts:
                premier = premier or ts
                dernier = ts
            m = e.get("message") or {}
            role = m.get("role") or e.get("type")
            t = texte(m.get("content"))
            if rejete(t):
                continue
            if role == "user":
                nu += 1
                caracteres_humains += len(t.strip())
                lignes.append(f"\n## >>> UTILISATEUR #{nu}\n\n{t.strip()}\n")
            elif role == "assistant":
                na += 1
                lignes.append(f"\n### assistant\n\n{t.strip()[:COUPE_REPONSE]}\n")
    if nu < MIN_MESSAGES:
        return 0, 0
    # Un brief unique se garde ; un « hi » isole ne se garde pas.
    if nu == 1 and caracteres_humains < MIN_CARACTERES_SI_UNIQUE:
        return 0, 0
    entete = (
        f"---\nsession: {src.stem}\nprojet: {src.parent.name}\n"
        f"debut: {premier}\nfin: {dernier}\n"
        f"messages_utilisateur: {nu}\nreponses_assistant: {na}\n---\n"
    )
    dst.parent.mkdir(parents=True, exist_ok=True)
    io.open(dst, "w", encoding="utf-8").write(entete + "".join(lignes))
    return nu, na

def main() -> int:
    depuis = None
    if "--depuis" in sys.argv:
        depuis = sys.argv[sys.argv.index("--depuis") + 1]
    fichiers: list[tuple[Path, Path]] = []
    for racine in SOURCES:
        if not racine.exists():
            print(f"  source absente, ignoree : {racine}")
            continue
        n0 = len(fichiers)
        for p in sorted(racine.rglob("*.jsonl")):
            fichiers.append((racine, p))
        print(f"  {racine.name or racine} : {len(fichiers) - n0} sessions")

    faits = vides = 0
    tot_u = tot_a = 0
    for i, (racine, src) in enumerate(fichiers, 1):
        if depuis:
            mt = datetime.fromtimestamp(src.stat().st_mtime).strftime("%Y-%m-%d")
            if mt < depuis:
                continue
        # Conserver l'arborescence relative a sa racine. La source historique
        # (~/.claude/projects) garde sa disposition a plat pour ne pas orpheliner
        # les fichiers deja produits ; les sources ajoutees sont prefixees, deux
        # outils pouvant porter le meme identifiant de session.
        rel = src.relative_to(racine).parent
        if racine.name == "projects":
            dst = SORTIE / src.parent.name / f"{src.stem}.md"
        else:
            dst = SORTIE / ("_" + racine.name.lstrip(".")) / rel / f"{src.stem}.md"
        try:
            nu, na = convertir(src, dst)
        except Exception as ex:
            print(f"  ECHEC {src.name} : {type(ex).__name__}")
            continue
        if nu == 0:
            vides += 1
        else:
            faits += 1
            tot_u += nu
            tot_a += na
        if i % 100 == 0:
            print(f"  {i}/{len(fichiers)} …")
    octets = sum(p.stat().st_size for p in SORTIE.rglob("*.md")) if SORTIE.exists() else 0
    print(f"\n  {faits} sessions converties · {vides} ecartees (moins de {MIN_MESSAGES} messages)")
    print(f"  {tot_u} messages utilisateur · {tot_a} reponses")
    print(f"  corpus : {octets // 1024 // 1024} Mo dans {SORTIE}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

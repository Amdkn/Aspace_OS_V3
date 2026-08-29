"""Inventorie TOUTES les sessions d'agent presentes sur le disque.

Pas seulement ~/.claude/projects. Pas seulement Codex. Tout.

Les sessions se sont dispersees au fil des reorganisations : copiees dans le
PARA de V2, emportees dans des dossiers `04_From_V2_Root`, laissees dans des
`_CAPTURE_`, des `_archive_`, des installations paralleles (`.codex-m3-lean`).
Une purge de retention n'a efface que `~/.claude/projects` ; tout ce qui avait
ete deplace ailleurs a survecu, y compris des mois anterieurs a la coupure.

Ce script ne convertit rien et ne supprime rien. Il LISTE, et il dit pour
chaque fichier :
  - son format (claude | codex | inconnu)
  - sa date de debut reelle, lue DANS le fichier et non sur le systeme de
    fichiers (une copie a la date de la copie, pas de la conversation)
  - son nombre de messages humains
  - sa taille

Sortie : inventaire_sessions.json, a cote de ce script.

    python inventaire_sessions.py
"""

from __future__ import annotations
import io, json, os, re, sys, time
from pathlib import Path

RACINE = Path("C:/Users/amado")
SORTIE = Path(__file__).resolve().parent / "inventaire_sessions.json"
JOURNAL = Path(__file__).resolve().parent / "inventaire_sessions.log"

# Dossiers a ne pas descendre : ils ne contiennent aucune session et coutent
# des minutes. `.codex` porte plus de 31 000 entrees de caches de paquets.
IGNORER = {
    "node_modules", ".git", ".venv", "venv", "__pycache__", "dist", "build",
    "AppData", "OneDrive", ".cache", ".npm", ".pnpm-store", "site-packages",
    ".next", ".nuxt", "target", "vendor",
}

# Une session tient rarement en moins de 2 Ko ; en dessous c'est un journal
# d'application, un fixture de test, un index.
TAILLE_MIN = 2048

# CORRECTION DU 2026-08-29 — le seul filtre de taille etait beaucoup trop
# large : 112 000 .jsonl parcourus, 88 340 « retenus », alors que les vraies
# sessions se comptent en milliers. Le reste etait des journaux d'application,
# des fixtures et des caches. Examiner 88 000 fichiers aurait pris des heures
# pour en jeter 98 %.
#
# Les deux outils nomment leurs sessions de facon reconnaissable :
#   Claude Code : <uuid>.jsonl
#   Codex       : rollout-<horodatage>-<uuid>.jsonl
# Filtrer sur le NOM avant d'ouvrir quoi que ce soit ramene le champ a ce qui
# peut etre une session. Un fichier de session porte toujours un identifiant ;
# un journal d'application porte un mot (history, state, heartbeat, gold...).
NOM_SESSION = re.compile(
    r"^(rollout-.*-)?[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\.jsonl$",
    re.I,
)


def ecrire(msg: str) -> None:
    ligne = f"{time.strftime('%H:%M:%S')}  {msg}"
    print(ligne, flush=True)
    with io.open(JOURNAL, "a", encoding="utf-8") as f:
        f.write(ligne + "\n")


def parcourir(racine: Path):
    """Parcours iteratif avec scandir : rglob s'etrangle sur les gros arbres."""
    pile = [racine]
    while pile:
        d = pile.pop()
        try:
            entrees = list(os.scandir(d))
        except OSError:
            continue
        for e in entrees:
            try:
                if e.is_dir(follow_symlinks=False):
                    if e.name in IGNORER:
                        continue
                    pile.append(Path(e.path))
                elif e.name.endswith(".jsonl") and NOM_SESSION.match(e.name):
                    yield Path(e.path), e.stat().st_size
            except OSError:
                continue


def examiner(p: Path) -> dict | None:
    """Rend la fiche d'un fichier, ou None s'il ne s'agit pas d'une session.

    On ne lit que les premieres lignes : ouvrir 380 Mo pour savoir si c'est une
    session serait absurde, et le format se reconnait des la premiere ligne.
    """
    fmt = None
    debut = None
    humains = 0
    try:
        with io.open(p, encoding="utf-8", errors="replace") as f:
            for i, ligne in enumerate(f):
                if i > 400:
                    break
                try:
                    e = json.loads(ligne)
                except Exception:
                    continue
                if not isinstance(e, dict):
                    continue
                ts = e.get("timestamp")
                if ts and not debut:
                    debut = ts
                m = e.get("message")
                if isinstance(m, dict) and m.get("role"):
                    fmt = fmt or "claude"
                    if m.get("role") == "user":
                        humains += 1
                elif e.get("type") in ("event_msg", "response_item", "session_meta"):
                    fmt = fmt or "codex"
                    pl = e.get("payload") or {}
                    if isinstance(pl, dict) and pl.get("type") == "user_message":
                        humains += 1
    except OSError:
        return None
    if not fmt:
        return None
    return {
        "chemin": str(p),
        "format": fmt,
        "debut": debut,
        "messages_humains_dans_les_400_premieres_lignes": humains,
        "octets": p.stat().st_size,
    }


def main() -> int:
    if JOURNAL.exists():
        JOURNAL.unlink()
    ecrire(f"parcours de {RACINE}")
    t0 = time.time()
    candidats = []
    vus = 0
    for p, taille in parcourir(RACINE):
        vus += 1
        if taille >= TAILLE_MIN:
            candidats.append(p)
        if vus % 500 == 0:
            ecrire(f"  {vus} .jsonl reperes, {len(candidats)} retenus, {time.time()-t0:.0f}s")
    ecrire(f"parcours fini : {vus} .jsonl, {len(candidats)} au-dessus de {TAILLE_MIN} octets")

    fiches = []
    for i, p in enumerate(candidats, 1):
        fiche = examiner(p)
        if fiche:
            fiches.append(fiche)
        if i % 200 == 0:
            ecrire(f"  examen {i}/{len(candidats)} — {len(fiches)} sessions")

    fiches.sort(key=lambda x: x.get("debut") or "")
    SORTIE.write_text(json.dumps(fiches, ensure_ascii=False, indent=1), encoding="utf-8")

    from collections import Counter
    par_mois = Counter((f.get("debut") or "?")[:7] for f in fiches)
    par_fmt = Counter(f["format"] for f in fiches)
    ecrire("")
    ecrire(f"SESSIONS TROUVEES : {len(fiches)}  ({sum(f['octets'] for f in fiches)/1048576:.0f} Mo)")
    ecrire(f"  par format : {dict(par_fmt)}")
    ecrire("  par mois (date lue dans le fichier) :")
    for m in sorted(par_mois):
        ecrire(f"     {m}  {par_mois[m]:5d}")
    ecrire(f"ecrit : {SORTIE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

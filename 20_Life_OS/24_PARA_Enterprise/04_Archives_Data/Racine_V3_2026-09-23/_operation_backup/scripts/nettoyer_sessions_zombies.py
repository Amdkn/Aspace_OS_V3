#!/usr/bin/env python3
"""
Niveau 1 — auto-nettoyage des vidages de sessions "zombies".

Regle revisee : un .md dans sessions_md/ est zombie si :
  (a) il n'est pas cite (par wikilink ou chemin) dans le bundle OKF
      (40_Memory_Wiki_OKF/),
  (b) ET il ne contient pas de triplet RDF exploitable (entite ou lien wiki).

Les sessions "consommees" (citees ailleurs, ou dont le contenu a deja ete
reinjecte dans un wiki/concept) sont preservees. Les autres sont deplacees
vers _ARCHIVE_sessions_zombies/YYYY-MM-DD/ (jamais supprimees).

Usage :
    python scripts/nettoyer_sessions_zombies.py [--dry-run]
"""

import argparse
import os
import re
import shutil
import sys
from datetime import datetime

ROOT = r"C:\Users\amado\ASpace_OS_V3"
SESSIONS = os.path.join(ROOT, "00_Amadeus", "30_MEMORY_CORE", "sessions_md")
OKF = os.path.join(ROOT, "40_Memory_Wiki_OKF")
ARCHIVE = os.path.join(ROOT, "_ARCHIVE_sessions_zombies")

# motifs qui signent une "session distillee" : lien wiki, mention explicite
WIKI = re.compile(r"\[\[([^\]]+)\]\]")
PATH_CITE = re.compile(r"(sessions_md/[A-Za-z0-9_\-./]+)")


def load_okf_corpus():
    """Renvoie l'ensemble des fragments de noms de fichiers cites par OKF."""
    cites = set()
    if not os.path.isdir(OKF):
        return cites
    for dirpath, _dirs, files in os.walk(OKF):
        for f in files:
            if not f.endswith(".md"):
                continue
            with open(os.path.join(dirpath, f), encoding="utf-8", errors="ignore") as fh:
                txt = fh.read()
            for m in WIKI.findall(txt):
                cites.add(m.strip().lower())
            for m in PATH_CITE.findall(txt):
                cites.add(os.path.basename(m).strip().lower())
    return cites


def session_key(name):
    """Cle de matching : nom de fichier sans extension, lower-case."""
    return os.path.splitext(os.path.basename(name))[0].strip().lower()


def has_wikilink_or_triplet(path):
    """Vrai si le .md contient un wikilink, un triplet, ou un frontmatter OKF."""
    try:
        with open(path, encoding="utf-8", errors="ignore") as f:
            head = f.read(20_000)  # 20 ko suffisent pour detecter
    except OSError:
        return False
    if WIKI.search(head):
        return True
    if "okf_version" in head or "triplet" in head.lower():
        return True
    if re.search(r"^---\s*$", head, re.M) and "type:" in head:
        return True
    return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    okf_cites = load_okf_corpus()
    print(f"Citations dans OKF : {len(okf_cites)} fragments")

    zombies = []
    distilles = []
    for dirpath, _dirs, files in os.walk(SESSIONS):
        for f in files:
            if not f.endswith(".md"):
                continue
            full = os.path.join(dirpath, f)
            key = session_key(f)
            cited_by_okf = key in okf_cites
            has_content = has_wikilink_or_triplet(full)
            if cited_by_okf or has_content:
                distilles.append(f)
            else:
                zombies.append(full)

    total = len(zombies) + len(distilles)
    pct = 100.0 * len(zombies) / max(1, total)
    print(f"Total .md sessions  : {total}")
    print(f"Distilles (gardes)  : {len(distilles)}")
    print(f"Zombies (a archiver): {len(zombies)}")
    print(f"Proportion          : {pct:.2f}%")

    if args.dry_run:
        for z in zombies[:10]:
            print("  zombie:", os.path.relpath(z, SESSIONS))
        if len(zombies) > 10:
            print(f"  ... et {len(zombies)-10} de plus")
        return 0

    date = datetime.now().strftime("%Y-%m-%d")
    dest = os.path.join(ARCHIVE, date)
    os.makedirs(dest, exist_ok=True)

    moved = 0
    for z in zombies:
        rel = os.path.relpath(z, SESSIONS)
        dst = os.path.join(dest, rel)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        try:
            shutil.move(z, dst)
            moved += 1
        except OSError as e:
            print("  ERR", z, e)

    print(f"Deplaces : {moved}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
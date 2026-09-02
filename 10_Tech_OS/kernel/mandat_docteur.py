#!/usr/bin/env python3
"""mandat_docteur.py — sélection de mandat pour la boucle permanente des Docteurs.

Usage: python mandat_docteur.py --layer L0|L1|L2 [--db uc.db] [--out _INBOX/mandats]

Récolte d'abord les baux expirés (uc.py reap), puis choisit UN work pending
de la couche demandée (priorité puis ancienneté), lit son ruban (tape), et
écrit un fichier de mandat prêt à être passé à un compagnon via:
  hermes -p <compagnon> chat --yolo -Q --query-file <mandat.txt>

Sortie: JSON {work_id, tape_id, tape_path, layer, compagnons, mandat_path}
Aucun candidat: JSON {candidat: null}.
"""
import argparse
import json
import sqlite3
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

COMPAGNONS = {
    "L0": {"spec": "yaz_spec_l0", "build": "ryan_build_l0", "spawn": "graham_spawn_l0",
           "review": "doctor13_review_l0"},
    "L1": {"spec": "amy_spec_l1", "build": "rory_build_l1", "spawn": "river_spawn_l1",
           "review": "doctor11_review_l1"},
    "L2": {"spec": "clara_spec_l2", "build": "nardole_build_l2", "spawn": "bill_spawn_l2",
           "review": "doctor12_review_l2"},
}

KERNEL = Path(__file__).resolve().parent


def reap():
    try:
        subprocess.run([sys.executable, str(KERNEL / "uc.py"), "reap"],
                       cwd=str(KERNEL), capture_output=True, timeout=60)
    except Exception as e:  # reap best-effort, ne bloque jamais la sélection
        print(f"reap warning: {e}", file=sys.stderr)


def pick(c, layer):
    return c.execute(
        "select id, tape_id, title, priority, attempts from work "
        "where status='pending' and layer=? "
        "order by priority desc, id asc limit 1", (layer,)).fetchone()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--layer", required=True, choices=["L0", "L1", "L2"])
    ap.add_argument("--db", default=str(KERNEL / "uc.db"))
    ap.add_argument("--out", default=str(KERNEL.parent.parent / "_INBOX" / "mandats"))
    args = ap.parse_args()

    reap()
    c = sqlite3.connect(args.db)
    c.row_factory = sqlite3.Row
    row = pick(c, args.layer)
    if row is None:
        print(json.dumps({"candidat": None, "layer": args.layer}))
        return 0

    work = dict(row)
    tape_path = None
    tape_sha = None
    if work["tape_id"]:
        t = c.execute("select path, sha256 from tape where id=?", (work["tape_id"],)).fetchone()
        if t:
            tape_path, tape_sha = t["path"], t["sha256"]

    ruban = ""
    if tape_path and Path(tape_path).exists():
        ruban = Path(tape_path).read_text(encoding="utf-8", errors="replace")

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    mandat_path = out_dir / f"mandat_w{work['id']}_{ts}.txt"
    compagnons = COMPAGNONS[args.layer]
    mandat_path.write_text(
        "MANDAT AUTONOME — aucune question possible, le ruban fait foi.\n"
        f"work_id: {work['id']}\nlayer: {args.layer}\ntitre: {work['title']}\n"
        f"tape_id: {work['tape_id']}\nruban: {tape_path or 'A SOURCER (work sans ruban)'}\n"
        f"sha256 ruban: {tape_sha or 'A SOURCER'}\nattempts: {work['attempts']}\n"
        "\n=== RUBAN φ ===\n" + (ruban or "A SOURCER — ruban absent ou manquant.") + "\n"
        "\n=== PROTOCOLE ===\n"
        f"1. claim:   python {KERNEL / 'uc.py'} claim --work {work['id']} --lease 45 --harness {compagnons['build']}\n"
        f"2. predict: python {KERNEL / 'uc.py'} predict --work {work['id']} --confiance <0.0-1.0> --note '<prediction anterieure a l acte>'\n"
        "3. build:   realiser le ruban. Un critere d'acceptation = une commande `cmd` executee avec rc.\n"
        f"4. review:  python {KERNEL / 'uc.py'} review --work {work['id']} (revue par {compagnons['review']}, preuve par critere)\n"
        f"5. done:    python {KERNEL / 'uc.py'} done --work {work['id']}\n"
        "Interdits: pas de question a l operateur (ruban incomplet = fail --work "
        f"{work['id']} --note 'ruban incomplet'). Personne ne cumule Build et Review.\n",
        encoding="utf-8")

    print(json.dumps({
        "candidat": {"work_id": work["id"], "title": work["title"], "layer": args.layer,
                     "tape_id": work["tape_id"], "tape_path": tape_path,
                     "attempts": work["attempts"]},
        "compagnons": compagnons,
        "mandat_path": str(mandat_path),
        "dispatch": f'hermes -p {compagnons["build"]} chat --yolo -Q --query-file "{mandat_path}"',
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""dlq.py — Donna, réceptionniste des erreurs.

Donna siège sous Rick. Elle reçoit ce que l'uplink des compagnons n'a pas résolu
et que le Docteur de la couche n'a pas su corriger. Elle ne répare rien : elle
**qualifie** et **escalade** au Super Uplink de Rick.

Sans elle, un échec répété reste `failed` dans un coin et personne ne le voit —
c'est exactement comme ça qu'un système autonome s'arrête sans prévenir.

    python dlq.py run [--seuil 3]     # échecs répétés -> blocked, escaladés à Rick
    python dlq.py rapport             # ce qu'il y a sur le bureau de Rick
    python dlq.py rendre --work N     # Rick a tranché : retour en file
"""
from __future__ import annotations
import argparse, json, os, re, sqlite3, subprocess, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
UC   = os.path.join(HERE, "uc.py")
DB   = os.environ.get("ASPACE_DB", os.path.join(HERE, "uc.db"))


def cx():
    c = sqlite3.connect(DB, isolation_level=None, timeout=10)
    c.row_factory = sqlite3.Row
    return c


def uc(*args) -> dict:
    p = subprocess.run([sys.executable, UC] + [str(a) for a in args],
                       capture_output=True, text=True, timeout=60)
    try:
        return json.loads(p.stdout)
    except json.JSONDecodeError:
        raise RuntimeError(f"uc.py illisible: {p.stdout[:150]}")


def dernier_motif(c, work_id: int) -> str:
    r = c.execute("SELECT payload FROM event WHERE work_id=? AND kind='failed' "
                  "ORDER BY id DESC LIMIT 1", (work_id,)).fetchone()
    if not r or not r["payload"]:
        return "motif non enregistré"
    return (json.loads(r["payload"]).get("reason") or "motif vide").strip()


def famille(motif: str) -> str:
    """Regroupe les motifs : Rick doit voir des causes, pas des lignes."""
    m = motif.lower()
    if "sans preuve" in m or "attestation" in m:      return "preuve manquante"
    if "aucun critère" in m or "aucun critere" in m:  return "ruban sans critère"
    if "exécuté en échec" in m or "execute en echec" in m: return "critère exécuté en échec"
    if "attesté en échec" in m or "atteste en echec" in m: return "critère attesté en échec"
    if "sorti sans rendre" in m:                      return "harness disparu"
    if re.search(r"error|exception|traceback", m):    return "plantage harness"
    return "autre"


def cmd_run(a):
    c = cx()
    pris = []
    for r in c.execute("SELECT id, title, layer, attempts FROM work "
                       "WHERE status='failed' AND attempts >= ? ORDER BY id", (a.seuil,)):
        motif = dernier_motif(c, r["id"])
        c.execute("UPDATE work SET status='blocked' WHERE id=?", (r["id"],))
        c.execute("INSERT INTO event(work_id,harness,kind,payload) VALUES(?,?,?,?)",
                  (r["id"], "donna", "escalade",
                   json.dumps({"vers": "rick", "tentatives": r["attempts"],
                               "famille": famille(motif), "motif": motif},
                              ensure_ascii=False)))
        pris.append({"work_id": r["id"], "title": r["title"], "layer": r["layer"],
                     "tentatives": r["attempts"], "famille": famille(motif)})
    print(json.dumps({"seuil": a.seuil, "escalades": pris}, ensure_ascii=False, indent=1))


def cmd_rapport(a):
    c = cx()
    lignes = []
    for r in c.execute("SELECT id, title, layer, attempts FROM work "
                       "WHERE status='blocked' ORDER BY id"):
        e = c.execute("SELECT payload FROM event WHERE work_id=? AND kind='escalade' "
                      "ORDER BY id DESC LIMIT 1", (r["id"],)).fetchone()
        p = json.loads(e["payload"]) if e and e["payload"] else {}
        lignes.append({"work_id": r["id"], "layer": r["layer"], "title": r["title"],
                       "tentatives": r["attempts"], "famille": p.get("famille"),
                       "motif": (p.get("motif") or "")[:180]})
    fam = Counter(l["famille"] for l in lignes)
    couche = Counter(l["layer"] for l in lignes)
    print(json.dumps({"bureau_de_rick": lignes,
                      "par_famille": dict(fam.most_common()),
                      "par_couche": dict(couche.most_common()),
                      "verdict": ("rien a arbitrer" if not lignes else
                                  f"{len(lignes)} dossier(s) attendent Rick")},
                     ensure_ascii=False, indent=1))


def cmd_rendre(a):
    c = cx()
    c.execute("UPDATE work SET status='pending', attempts=0 WHERE id=? AND status='blocked'",
              (a.work,))
    ok = c.total_changes > 0
    if ok:
        c.execute("INSERT INTO event(work_id,harness,kind,payload) VALUES(?,?,?,?)",
                  (a.work, "rick", "arbitrage",
                   json.dumps({"decision": a.note or "remis en file"}, ensure_ascii=False)))
    print(json.dumps({"ok": ok, "work_id": a.work}, ensure_ascii=False))


P = argparse.ArgumentParser(description="Donna — DLQ et Super Uplink vers Rick")
S = P.add_subparsers(dest="cmd", required=True)
p = S.add_parser("run"); p.add_argument("--seuil", type=int, default=3); p.set_defaults(f=cmd_run)
S.add_parser("rapport").set_defaults(f=cmd_rapport)
p = S.add_parser("rendre"); p.add_argument("--work", type=int, required=True)
p.add_argument("--note"); p.set_defaults(f=cmd_rendre)

if __name__ == "__main__":
    a = P.parse_args(); a.f(a)

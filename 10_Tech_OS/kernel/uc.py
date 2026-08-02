#!/usr/bin/env python3
"""uc.py — constructeur universel A'Space V3.

File de travail durable, reclamation atomique, bail expirant, registre de
predictions. C'est le plus petit organe qui permet a un agent d'en detacher
un autre sans passer par l'operateur.

    python uc.py init
    python uc.py submit  --layer L2 --title "..." [--tape chemin] [--parent N] [--priority 5]
    python uc.py claim   --harness cc --layer L2 [--lease 900]
    python uc.py predict --work N --claim "..." --confidence 0.7
    python uc.py beat    --work N --harness cc [--lease 900]
    python uc.py review  --work N
    python uc.py done    --work N
    python uc.py fail    --work N [--reason "..."]
    python uc.py score   --prediction N --outcome 1
    python uc.py reap
    python uc.py status
"""
import argparse, hashlib, json, os, sqlite3, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DB   = os.environ.get("ASPACE_DB", os.path.join(HERE, "uc.db"))


def cx():
    c = sqlite3.connect(DB, isolation_level=None, timeout=10)
    c.row_factory = sqlite3.Row
    c.execute("PRAGMA foreign_keys=ON")
    c.execute("PRAGMA busy_timeout=5000")
    return c


def log(c, work_id, harness, kind, payload=None):
    c.execute("INSERT INTO event(work_id,harness,kind,payload) VALUES(?,?,?,?)",
              (work_id, harness, kind, json.dumps(payload, ensure_ascii=False) if payload else None))


def out(obj):
    print(json.dumps(obj, ensure_ascii=False, indent=1))


# --------------------------------------------------------------- commandes
def cmd_init(a):
    with open(os.path.join(HERE, "schema.sql"), encoding="utf-8") as f:
        sql = f.read()
    c = cx(); c.executescript(sql)
    out({"ok": True, "db": DB, "tables": [r[0] for r in c.execute(
        "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")]})


def cmd_submit(a):
    c = cx(); tape_id = None
    if a.tape:
        p = os.path.abspath(a.tape)
        if not os.path.exists(p):
            out({"ok": False, "err": f"ruban introuvable: {p}"}); sys.exit(2)
        h = hashlib.sha256(open(p, "rb").read()).hexdigest()
        c.execute("INSERT INTO tape(path,sha256) VALUES(?,?) "
                  "ON CONFLICT(path) DO UPDATE SET sha256=excluded.sha256", (p, h))
        tape_id = c.execute("SELECT id FROM tape WHERE path=?", (p,)).fetchone()["id"]
    cur = c.execute("INSERT INTO work(tape_id,layer,title,priority,parent_id) VALUES(?,?,?,?,?)",
                    (tape_id, a.layer, a.title, a.priority, a.parent))
    wid = cur.lastrowid
    log(c, wid, None, "submit", {"layer": a.layer, "title": a.title, "parent": a.parent})
    out({"ok": True, "work_id": wid, "tape_id": tape_id})


def cmd_claim(a):
    """Reclamation atomique : BEGIN IMMEDIATE serialise les concurrents."""
    c = cx()
    c.execute("BEGIN IMMEDIATE")
    try:
        if a.work:                      # reclamation ciblee : un pont sait quel item il traite
            row = c.execute("SELECT id FROM work WHERE id=? AND status IN ('pending','failed')",
                            (a.work,)).fetchone()
        else:
            row = c.execute(
                "SELECT id FROM work WHERE status='pending' AND (? IS NULL OR layer=?) "
                "ORDER BY priority DESC, id LIMIT 1", (a.layer, a.layer)).fetchone()
        if not row:
            c.execute("COMMIT"); out({"ok": True, "work": None}); return
        wid = row["id"]
        c.execute("UPDATE work SET status='claimed', attempts=attempts+1 WHERE id=?", (wid,))
        c.execute("INSERT INTO claim(work_id,harness,expires_at) "
                  "VALUES(?,?,datetime('now',?)) "
                  "ON CONFLICT(work_id) DO UPDATE SET harness=excluded.harness, "
                  "claimed_at=datetime('now'), expires_at=excluded.expires_at",
                  (wid, a.harness, f"+{a.lease} seconds"))
        log(c, wid, a.harness, "claim", {"lease_s": a.lease})
        c.execute("COMMIT")
    except Exception:
        c.execute("ROLLBACK"); raise
    w = c.execute("SELECT w.*, t.path AS tape_path FROM work w "
                  "LEFT JOIN tape t ON t.id=w.tape_id WHERE w.id=?", (wid,)).fetchone()
    out({"ok": True, "work": dict(w)})


def cmd_predict(a):
    c = cx()
    cur = c.execute("INSERT INTO prediction(work_id,claim_text,confidence) VALUES(?,?,?)",
                    (a.work, a.claim, a.confidence))
    log(c, a.work, None, "predict", {"confidence": a.confidence})
    out({"ok": True, "prediction_id": cur.lastrowid})


def cmd_beat(a):
    c = cx()
    c.execute("UPDATE claim SET expires_at=datetime('now',?) WHERE work_id=? AND harness=?",
              (f"+{a.lease} seconds", a.work, a.harness))
    out({"ok": c.total_changes > 0, "work_id": a.work})


def _move(a, target):
    c = cx()
    try:
        c.execute("UPDATE work SET status=? WHERE id=?", (target, a.work))
    except sqlite3.IntegrityError as e:
        out({"ok": False, "err": str(e)}); sys.exit(3)
    if target in ("done", "failed"):
        c.execute("DELETE FROM claim WHERE work_id=?", (a.work,))
    log(c, a.work, None, target, {"reason": getattr(a, "reason", None)})
    out({"ok": True, "work_id": a.work, "status": target})


def cmd_review(a): _move(a, "review")
def cmd_done(a):   _move(a, "done")
def cmd_fail(a):   _move(a, "failed")


def cmd_attest(a):
    """Preuve, pas affirmation : un critere coche sans attestation ne compte pas."""
    c = cx()
    log(c, a.work, a.harness, "evidence",
        {"criterion": a.criterion, "ok": bool(a.ok), "note": a.note})
    out({"ok": True, "work_id": a.work, "criterion": a.criterion, "verdict": bool(a.ok)})


def cmd_evidence(a):
    c = cx()
    rows = [json.loads(r["payload"]) for r in c.execute(
        "SELECT payload FROM event WHERE work_id=? AND kind='evidence' ORDER BY id", (a.work,))]
    out({"work_id": a.work, "evidence": rows})


def cmd_score(a):
    c = cx()
    c.execute("UPDATE prediction SET outcome=?, scored_at=datetime('now') WHERE id=?",
              (a.outcome, a.prediction))
    out({"ok": c.total_changes > 0, "prediction_id": a.prediction})


def cmd_reap(a):
    """Rend a la file tout bail expire. C'est ce qui rend la panne non bloquante."""
    c = cx()
    dead = [r["work_id"] for r in c.execute(
        "SELECT work_id FROM claim WHERE expires_at < datetime('now')")]
    for wid in dead:
        c.execute("UPDATE work SET status='pending' WHERE id=? AND status='claimed'", (wid,))
        c.execute("DELETE FROM claim WHERE work_id=?", (wid,))
        log(c, wid, None, "reap", None)
    out({"ok": True, "reclames": dead})


def cmd_status(a):
    c = cx()
    st = {r["status"]: r["n"] for r in c.execute(
        "SELECT status, count(*) n FROM work GROUP BY status")}
    pr = c.execute("SELECT count(*) n, sum(outcome IS NULL) en_attente FROM prediction").fetchone()
    cal = [dict(r) for r in c.execute("SELECT * FROM v_calibration")]
    out({"db": DB, "work": st, "predictions": dict(pr), "calibration": cal})


P = argparse.ArgumentParser(description="constructeur universel A'Space V3")
S = P.add_subparsers(dest="cmd", required=True)
S.add_parser("init").set_defaults(f=cmd_init)
p = S.add_parser("submit"); p.add_argument("--layer", required=True, choices=["A0", "L0", "L1", "L2"])
p.add_argument("--title", required=True); p.add_argument("--tape"); p.add_argument("--parent", type=int)
p.add_argument("--priority", type=int, default=0); p.set_defaults(f=cmd_submit)
p = S.add_parser("claim"); p.add_argument("--harness", required=True)
p.add_argument("--work", type=int, help="reclamer un item precis (ponts, watchdogs)")
p.add_argument("--layer", choices=["A0", "L0", "L1", "L2"]); p.add_argument("--lease", type=int, default=900)
p.set_defaults(f=cmd_claim)
p = S.add_parser("predict"); p.add_argument("--work", type=int, required=True)
p.add_argument("--claim", required=True); p.add_argument("--confidence", type=float, required=True)
p.set_defaults(f=cmd_predict)
p = S.add_parser("beat"); p.add_argument("--work", type=int, required=True)
p.add_argument("--harness", required=True); p.add_argument("--lease", type=int, default=900)
p.set_defaults(f=cmd_beat)
for name, fn in (("review", cmd_review), ("done", cmd_done)):
    p = S.add_parser(name); p.add_argument("--work", type=int, required=True); p.set_defaults(f=fn)
p = S.add_parser("fail"); p.add_argument("--work", type=int, required=True)
p.add_argument("--reason"); p.set_defaults(f=cmd_fail)
p = S.add_parser("attest"); p.add_argument("--work", type=int, required=True)
p.add_argument("--criterion", type=int, required=True); p.add_argument("--ok", type=int, choices=[0, 1], required=True)
p.add_argument("--harness"); p.add_argument("--note"); p.set_defaults(f=cmd_attest)
p = S.add_parser("evidence"); p.add_argument("--work", type=int, required=True)
p.set_defaults(f=cmd_evidence)
p = S.add_parser("score"); p.add_argument("--prediction", type=int, required=True)
p.add_argument("--outcome", type=int, choices=[0, 1], required=True); p.set_defaults(f=cmd_score)
S.add_parser("reap").set_defaults(f=cmd_reap)
S.add_parser("status").set_defaults(f=cmd_status)

if __name__ == "__main__":
    a = P.parse_args(); a.f(a)

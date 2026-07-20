#!/usr/bin/env python3
"""deploy_instance.py <slug> | --verify-all
Instance coach LOCALE LEGERE (zero Docker) : 1 dossier isole = instances/<slug>/
  config.json (identite+plan) + data.db (SQLite privee: content/prospects/compliance).
IDEMPOTENT  : re-run = verify + repair, jamais de doublon, jamais d'ecrasement.
ANTIFRAGILE : --verify-all scanne toutes les instances et repare les manquants.
PERSISTANT  : tout est fichier ; survit reboot/kill ; portable VPS par simple copie."""
import sys, os, json, sqlite3, datetime

SOB  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INST = os.path.join(SOB, "instances")
SCHEMA = """
CREATE TABLE IF NOT EXISTS content(id INTEGER PRIMARY KEY, ts TEXT, kind TEXT,
  title TEXT, body TEXT, status TEXT DEFAULT 'draft');
CREATE TABLE IF NOT EXISTS prospects(id INTEGER PRIMARY KEY, ts TEXT,
  name TEXT, url TEXT, stage TEXT DEFAULT 'new');
CREATE TABLE IF NOT EXISTS compliance(id INTEGER PRIMARY KEY, ts TEXT,
  item TEXT, status TEXT DEFAULT 'todo');
"""
REQUIRED_TABLES = {"content", "prospects", "compliance"}

def deploy(slug):
    d = os.path.join(INST, slug)
    os.makedirs(d, exist_ok=True)
    actions = []
    cfg = os.path.join(d, "config.json")
    if not os.path.exists(cfg):
        with open(cfg, "w", encoding="utf-8") as f:
            json.dump({"slug": slug, "created": datetime.datetime.now().isoformat(timespec="seconds"),
                       "plan_usd_month": 1000, "status": "provisioned"}, f, indent=1)
        actions.append("config CREATED")
    else:
        actions.append("config OK")
    db = sqlite3.connect(os.path.join(d, "data.db"))
    db.executescript(SCHEMA); db.commit()
    have = {r[0] for r in db.execute("SELECT name FROM sqlite_master WHERE type='table'")}
    db.close()
    missing = REQUIRED_TABLES - have
    actions.append("data.db REPAIRED" if missing else "data.db OK")
    if missing:  # repair pass (schema is CREATE IF NOT EXISTS => rerun fixes)
        db = sqlite3.connect(os.path.join(d, "data.db")); db.executescript(SCHEMA); db.commit(); db.close()
    print(f"[{slug}] " + " | ".join(actions))
    return 0

def verify_all():
    if not os.path.isdir(INST):
        print("0 instances"); return 0
    slugs = [s for s in os.listdir(INST) if os.path.isdir(os.path.join(INST, s))]
    for s in slugs: deploy(s)
    print(f"verify-all: {len(slugs)} instance(s) verified/repaired")
    return 0

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(1)
    sys.exit(verify_all() if sys.argv[1] == "--verify-all" else deploy(sys.argv[1]))

#!/usr/bin/env python3
"""graham_checkpoint.py — checkpoint WAL + restauration sur rupture de critere.

Avant chaque execution : checkpoint WAL de uc.db (backup physique fiable).
Si un critere casse pendant l'execution : restauration depuis le checkpoint.
Chaque operation est tracee dans la table event.

    python graham_checkpoint.py save   --work N
    python graham_checkpoint.py check  --work N --criterion "<expression python sur ctx>"
    python graham_checkpoint.py restore --work N
"""
import argparse, json, os, sqlite3, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DB   = os.environ.get("ASPACE_DB", os.path.join(HERE, "uc.db"))
CKPT_DIR = os.path.join(HERE, "checkpoints")


def cx():
    c = sqlite3.connect(DB, isolation_level=None, timeout=10)
    c.execute("PRAGMA busy_timeout=5000")
    return c


def trace(c, work_id, kind, payload):
    c.execute("INSERT INTO event(work_id,harness,kind,payload) VALUES(?,?,?,?)",
              (work_id, "graham_checkpoint", kind, json.dumps(payload, ensure_ascii=False)))


def ckpt_path(work_id):
    os.makedirs(CKPT_DIR, exist_ok=True)
    return os.path.join(CKPT_DIR, f"uc_work{work_id}.db")


def cmd_save(a):
    c = cx()
    src = c.execute("PRAGMA wal_checkpoint(TRUNCATE)").fetchone()
    dest = ckpt_path(a.work)
    dst = sqlite3.connect(dest)
    c.backup(dst)
    # trace aussi DANS le checkpoint, APRES le backup : le restore efface uc.db,
    # la preuve du save doit survivre a la restauration
    trace(dst, a.work, "checkpoint_save", {"path": dest, "wal": list(src)})
    dst.commit()
    dst.close()
    trace(c, a.work, "checkpoint_save", {"path": dest, "wal": list(src)})
    print(json.dumps({"ok": True, "work_id": a.work, "checkpoint": dest,
                      "wal_busy": src[0], "wal_pages": src[1]}))


def cmd_check(a):
    """Evalue un critere. rc=0 si vrai, rc=4 si faux (rupture -> restaurer)."""
    c = cx()
    ctx = {"work_id": a.work}
    row = c.execute("SELECT status, attempts FROM work WHERE id=?", (a.work,)).fetchone()
    if row:
        ctx["status"], ctx["attempts"] = row
    ok = bool(eval(a.criterion, {"__builtins__": {}}, ctx))  # ctx controle, pas de builtins
    trace(c, a.work, "checkpoint_check", {"criterion": a.criterion, "ok": ok, "ctx": ctx})
    print(json.dumps({"ok": ok, "work_id": a.work, "criterion": a.criterion, "ctx": ctx}))
    sys.exit(0 if ok else 4)


def cmd_restore(a):
    """Restaure uc.db depuis le checkpoint — rupture de critere = retour a l'etat sain."""
    src = ckpt_path(a.work)
    if not os.path.exists(src):
        print(json.dumps({"ok": False, "err": f"checkpoint introuvable: {src}"})); sys.exit(2)
    # WAL de la base vivante purge avant restauration
    live = cx()
    live.execute("PRAGMA wal_checkpoint(TRUNCATE)")
    bak = DB + ".pre_restore"
    if os.path.exists(DB):
        with open(DB, "rb") as f, open(bak, "wb") as g:
            g.write(f.read())
    dst = sqlite3.connect(DB)
    src_conn = sqlite3.connect(src)
    src_conn.backup(dst)   # copie binaire checkpoint -> base vivante
    src_conn.close()
    dst.commit(); dst.close()
    trace(cx(), a.work, "checkpoint_restore", {"from": src, "backup": bak})
    print(json.dumps({"ok": True, "work_id": a.work, "restored_from": src}))


def main():
    ap = argparse.ArgumentParser(description="checkpoint WAL Graham")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("save");   p.add_argument("--work", type=int, required=True); p.set_defaults(f=cmd_save)
    p = sub.add_parser("check");  p.add_argument("--work", type=int, required=True)
    p.add_argument("--criterion", required=True); p.set_defaults(f=cmd_check)
    p = sub.add_parser("restore"); p.add_argument("--work", type=int, required=True); p.set_defaults(f=cmd_restore)
    a = ap.parse_args(); a.f(a)


if __name__ == "__main__":
    main()

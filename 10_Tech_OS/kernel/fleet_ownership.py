"""Fail-closed WorkGraph ownership checks for the Jules dispatcher.

No schema migration. Claims and bindings use the canonical CLI. A dispatch attempt
is durable before the network call, so a timeout cannot silently create duplicates.
"""
from __future__ import annotations
import json
import re
import sqlite3
import subprocess
import sys
from contextlib import closing, contextmanager
from pathlib import Path

HERE = Path(__file__).resolve().parent
DB = HERE / "uc.db"


@contextmanager
def dispatch_lock(path=None):
    """One fleet tick across processes; OS releases the lock after a crash."""
    lock_path = Path(path) if path else HERE / ".fleet-dispatch.lock"
    handle = lock_path.open("a+b")
    locked = False
    try:
        handle.seek(0, 2)
        if handle.tell() == 0:
            handle.write(b"0")
            handle.flush()
        handle.seek(0)
        try:
            if sys.platform == "win32":
                import msvcrt
                msvcrt.locking(handle.fileno(), msvcrt.LK_NBLCK, 1)
            else:
                import fcntl
                fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
            locked = True
        except OSError as exc:
            raise ValueError("another fleet dispatcher owns the execution lock") from exc
        yield
    finally:
        if locked:
            handle.seek(0)
            if sys.platform == "win32":
                import msvcrt
                msvcrt.locking(handle.fileno(), msvcrt.LK_UNLCK, 1)
            else:
                import fcntl
                fcntl.flock(handle.fileno(), fcntl.LOCK_UN)
        handle.close()


def connect(db_path=DB):
    c = sqlite3.connect(Path(db_path).resolve().as_uri() + "?mode=ro", uri=True, timeout=10)
    c.row_factory = sqlite3.Row
    return c


def resolve_work(issue_id, db_path=DB):
    # The existing WorkGraph uses an exact bracketed Linear identifier in titles.
    # Ambiguous/missing mappings fail closed instead of inventing a new work_id.
    if not re.fullmatch(r"[A-Z][A-Z0-9]*-[0-9]+", issue_id):
        raise ValueError("invalid Linear identifier")
    with closing(connect(db_path)) as c:
        rows = c.execute("SELECT id,status FROM work WHERE instr(title,?)>0",
                         ("[" + issue_id + "]",)).fetchall()
        if len(rows) != 1:
            raise ValueError(f"{issue_id}: expected one canonical work_id, found {len(rows)}")
        row = dict(rows[0])
        if row["status"] != "pending":
            raise ValueError(f"{issue_id}: work {row['id']} is {row['status']}, not READY")
        wid = row["id"]
        if c.execute("SELECT 1 FROM session_binding WHERE work_id=? AND status IN ('active','idle')",
                     (wid,)).fetchone():
            raise ValueError(f"{issue_id}: existing session binding must be reconciled")
        if c.execute("SELECT 1 FROM claim WHERE work_id=? AND julianday(expires_at)>julianday('now')",
                     (wid,)).fetchone():
            raise ValueError(f"{issue_id}: live owner already exists")
        if c.execute("""SELECT 1 FROM work_dependency d JOIN work w ON w.id=d.depends_on_id
                        WHERE d.work_id=? AND d.kind IN ('blocks','requires') AND w.status!='done'""",
                     (wid,)).fetchone():
            raise ValueError(f"{issue_id}: WorkGraph dependency is not done")
        latest = c.execute("""SELECT kind FROM event WHERE work_id=?
            AND kind IN ('fleet_dispatch_attempt','fleet_dispatch_resolved') ORDER BY id DESC LIMIT 1""",
                           (wid,)).fetchone()
        if latest and latest["kind"] == "fleet_dispatch_attempt":
            raise ValueError(f"{issue_id}: previous network dispatch requires reconciliation")
        return wid


def canonical(script, *args, db_path=DB):
    import os
    env = dict(os.environ, ASPACE_DB=str(db_path), PYTHONIOENCODING="utf-8")
    p = subprocess.run([sys.executable, str(HERE / script), *map(str, args)],
                       capture_output=True, text=True, encoding="utf-8", env=env, timeout=30)
    if p.returncode:
        raise RuntimeError((p.stderr or p.stdout).strip())
    return json.loads(p.stdout)


def reserve(issue_id, db_path=DB):
    wid = resolve_work(issue_id, db_path)
    claimed = canonical("uc.py", "claim", "--work", wid, "--harness", "jules",
                        "--lease", 1800, db_path=db_path)
    if not claimed.get("work") or claimed["work"]["id"] != wid:
        raise ValueError(f"{issue_id}: atomic claim lost; no dispatch")
    # Append-only event, not a direct work-state mutation.
    with closing(sqlite3.connect(db_path, timeout=10)) as c, c:
        c.execute("INSERT INTO event(work_id,harness,kind,payload) VALUES(?,?,?,?)",
                  (wid, "jules", "fleet_dispatch_attempt", json.dumps({"issue": issue_id})))
    return wid


def bind_session(work_id, session_id, db_path=DB):
    if not session_id:
        raise ValueError("provider did not return a session identity")
    return canonical("uc_workgraph.py", "bind", "--work", work_id, "--harness", "jules",
                     "--session", str(session_id), "--external-ref", str(session_id),
                     "--capability", "repo-implementation", db_path=db_path)


def require_running_owner(work_id, session_id, observation, db_path=DB):
    observed_id = str(observation.get("id") or observation.get("name") or "").removeprefix("sessions/")
    sid = str(session_id).removeprefix("sessions/")
    if observed_id != sid or observation.get("state") != "IN_PROGRESS":
        raise ValueError("fresh provider observation does not prove this session is executing")
    with closing(connect(db_path)) as c:
        owned = c.execute("""SELECT 1 FROM work w JOIN claim c ON c.work_id=w.id
            JOIN session_binding b ON b.work_id=w.id AND b.harness=c.harness
            WHERE w.id=? AND w.status IN ('claimed','running') AND c.harness='jules'
            AND julianday(c.expires_at)>julianday('now') AND b.status='active'
            AND b.ended_at IS NULL AND b.session_key IN (?,?)""",
                          (work_id, sid, "sessions/" + sid)).fetchone()
        if not owned:
            raise ValueError("no live claim and matching active session binding")
    return True


def supervisor_preflight(db_path=DB):
    with closing(connect(db_path)) as c:
        count = c.execute("""SELECT COUNT(*) FROM session_binding
            WHERE harness='jules' AND status='active'""").fetchone()[0]
        unresolved = c.execute("""SELECT COUNT(DISTINCT e.work_id) FROM event e
            WHERE e.kind='fleet_dispatch_attempt'
            AND NOT EXISTS (SELECT 1 FROM session_binding b WHERE b.work_id=e.work_id)
            AND NOT EXISTS (SELECT 1 FROM event r WHERE r.work_id=e.work_id
                AND r.kind='fleet_dispatch_resolved' AND r.id>e.id)""").fetchone()[0]
    return {"wake": bool(count or unresolved), "active_bindings": count,
            "unresolved_dispatches": unresolved}


if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--supervisor-preflight", action="store_true")
    p.add_argument("--db", default=str(DB))
    a = p.parse_args()
    if not a.supervisor_preflight:
        p.error("--supervisor-preflight required")
    print(json.dumps(supervisor_preflight(a.db)))

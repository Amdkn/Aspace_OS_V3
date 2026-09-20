#!/usr/bin/env python3
"""uc_workgraph.py — WorkGraph & Harness Capability Engine (ADR-003, KER-9).

Expose:
- Commandes WorkGraph v2 (intent, link, depend, bind, artifact, gate, goal, round, round-link, goal-review, wait, capability, graph)
- Sélecteur de capacités de harness (Harness Capability Selector via get_harnesses)
"""
import argparse, hashlib, json, os, sqlite3, sys, uuid
from enum import Enum

HERE = os.path.dirname(os.path.abspath(__file__))
DB = os.environ.get("ASPACE_DB", os.path.join(HERE, "uc.db"))

class GoalOutcome(str, Enum):
    DONE = "DONE"
    WAIT = "WAIT"
    ABANDON = "ABANDON"
    NEXT_ROUND = "NEXT_ROUND"

class WorkGraph:
    """
    WorkGraph V2 orchestration semantics.
    Implements Goal -> Round -> Work hierarchy and Goal Review,
    preserving uc.db identities and FK integrity.
    """
    def __init__(self, db_path: str):
        self.db_path = db_path

    def cx(self):
        c = sqlite3.connect(self.db_path, isolation_level=None, timeout=10)
        c.row_factory = sqlite3.Row
        c.execute("PRAGMA foreign_keys=ON")
        return c

    def create_goal(self, layer: str, title: str) -> int:
        """Create a new Goal (represented as a root work item)."""
        c = self.cx()
        try:
            cur = c.execute("INSERT INTO work(layer, title) VALUES(?, ?)", (layer, title))
            return cur.lastrowid
        finally:
            c.close()

    def create_round(self, goal_id: int) -> int:
        """Create a new Round for a given Goal."""
        c = self.cx()
        try:
            row = c.execute("SELECT layer FROM work WHERE id=?", (goal_id,)).fetchone()
            if not row:
                raise ValueError(f"Goal {goal_id} not found")
            cur = c.execute("INSERT INTO work(layer, title, parent_id) VALUES(?, ?, ?)",
                            (row['layer'], f"Round for Goal {goal_id}", goal_id))
            return cur.lastrowid
        finally:
            c.close()

    def create_work(self, round_id: int, title: str) -> int:
        """Create a new Work item (task) for a given Round."""
        c = self.cx()
        try:
            row = c.execute("SELECT layer FROM work WHERE id=?", (round_id,)).fetchone()
            if not row:
                raise ValueError(f"Round {round_id} not found")
            cur = c.execute("INSERT INTO work(layer, title, parent_id) VALUES(?, ?, ?)",
                            (row['layer'], title, round_id))
            return cur.lastrowid
        finally:
            c.close()

    def review_goal(self, goal_id: int, round_id: int, outcome: GoalOutcome, notes: str = "") -> int:
        """
        Record an independent Goal Review.
        Task completion is just evidence; only this explicit review sets the terminal outcome.
        """
        c = self.cx()
        try:
            # Verify FK logic
            goal = c.execute("SELECT id FROM work WHERE id=?", (goal_id,)).fetchone()
            if not goal:
                raise ValueError(f"Goal {goal_id} not found")
            r = c.execute("SELECT id, parent_id FROM work WHERE id=?", (round_id,)).fetchone()
            if not r:
                raise ValueError(f"Round {round_id} not found")
            if r['parent_id'] != goal_id:
                raise ValueError(f"Round {round_id} is not a child of Goal {goal_id}")

            payload = json.dumps({
                "round_id": round_id,
                "outcome": outcome.value,
                "notes": notes
            })
            cur = c.execute(
                "INSERT INTO event(work_id, harness, kind, payload) VALUES(?, 'workgraph', 'goal_review', ?)",
                (goal_id, payload)
            )
            return cur.lastrowid
        finally:
            c.close()




def db(path=None):
    target_db = path or DB
    c = sqlite3.connect(target_db, isolation_level=None, timeout=10)
    c.row_factory = sqlite3.Row
    c.execute("PRAGMA foreign_keys=ON")
    return c

def emit(x):
    print(json.dumps(x, ensure_ascii=False))

def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def get_harnesses(db_path, required_caps, min_evidence):
    try:
        c = sqlite3.connect(db_path, isolation_level=None, timeout=10)
        c.row_factory = sqlite3.Row
        query = "SELECT harness, payload FROM event WHERE kind='capability' ORDER BY id ASC"
        rows = c.execute(query).fetchall()
    except sqlite3.OperationalError:
        return []

    harness_state = {}
    for row in rows:
        harness = row['harness']
        if not harness:
            continue
        try:
            payload = json.loads(row['payload'])
        except Exception:
            continue

        cap = payload.get('capability')
        status = payload.get('status')
        ev_level = payload.get('evidence_level', 0)

        if not cap:
            continue

        if harness not in harness_state:
            harness_state[harness] = {}

        harness_state[harness][cap] = {
            'status': status,
            'evidence_level': ev_level
        }

    result = []
    for harness, caps in harness_state.items():
        ok = True
        for req_cap in required_caps:
            c_state = caps.get(req_cap)
            if not c_state:
                ok = False
                break
            if c_state['status'] != 'pass':
                ok = False
                break
            if c_state['evidence_level'] < min_evidence:
                ok = False
                break
        if ok:
            result.append(harness)

    return sorted(result)

def intent(a):
    c = db()
    k = a.key or "intent-" + uuid.uuid4().hex[:16]
    ir = None
    if a.ir:
        ir = open(a.ir, encoding="utf-8").read()
    source_hash = sha256_file(a.source) if a.source and os.path.isfile(a.source) else None
    c.execute(
        "INSERT INTO intent(intent_key,title,layer,status,source_path,verbatim_sha256,intent_ir) VALUES(?,?,?,?,?,?,?)",
        (k, a.title, a.layer, a.status, a.source, source_hash, ir),
    )
    emit({
        "intent_id": c.execute("SELECT id FROM intent WHERE intent_key=?", (k,)).fetchone()[0],
        "intent_key": k,
        "verbatim_sha256": source_hash,
    })

def link(a):
    db().execute("INSERT OR REPLACE INTO work_intent(work_id,intent_id,relation) VALUES(?,?,?)", (a.work, a.intent, a.relation))
    emit({"ok": True})

def depend(a):
    db().execute("INSERT OR REPLACE INTO work_dependency(work_id,depends_on_id,kind) VALUES(?,?,?)", (a.work, a.on, a.kind))
    emit({"ok": True})

def bind(a):
    c = db()
    key = a.session or uuid.uuid4().hex
    cur = c.execute(
        "INSERT INTO session_binding(work_id,session_key,harness,capability,external_ref,status) VALUES(?,?,?,?,?,?)",
        (a.work, key, a.harness, a.capability, a.external_ref, a.status),
    )
    emit({"binding_id": cur.lastrowid, "session_id": key, "status": a.status})

def artifact(a):
    c = db()
    digest = a.sha256
    if not digest and a.file:
        digest = sha256_file(a.file)
    uri = a.uri or (os.path.abspath(a.file) if a.file else None)
    if not uri:
        raise SystemExit("artifact requires --uri or --file")
    cur = c.execute(
        "INSERT INTO artifact(work_id,kind,uri,sha256,producer_session_id) VALUES(?,?,?,?,?)",
        (a.work, a.kind, uri, digest, a.producer_session),
    )
    emit({"artifact_id": cur.lastrowid, "work_id": a.work, "sha256": digest, "uri": uri})

def gate(a):
    c = db()
    if a.evidence_event:
        row = c.execute("SELECT id FROM event WHERE id=? AND work_id=?", (a.evidence_event, a.work)).fetchone()
        if not row:
            raise SystemExit("evidence event does not belong to work")
    verdict = a.verdict.lower()
    cur = c.execute(
        "INSERT INTO gate_decision(work_id,gate,verdict,reason,evidence_event_id,decided_by) VALUES(?,?,?,?,?,?)",
        (a.work, a.gate, verdict, a.reason, a.evidence_event, a.by),
    )
    emit({"gate_decision_id": cur.lastrowid, "work_id": a.work, "verdict": verdict})

def goal(a):
    c = db()
    key = a.key or "goal-" + uuid.uuid4().hex[:16]
    if not a.criteria:
        criteria = []
    else:
        try:
            criteria = json.loads(a.criteria)
        except json.JSONDecodeError:
            criteria = [x.strip() for x in a.criteria.split("|") if x.strip()]
    cur = c.execute(
        "INSERT INTO goal(intent_id,goal_key,title,success_criteria,status) VALUES(?,?,?,?,?)",
        (a.intent, key, a.title, json.dumps(criteria, ensure_ascii=False), a.status),
    )
    emit({"goal_id": cur.lastrowid, "goal_key": key})

def round_add(a):
    c = db()
    n = a.number
    if n is None:
        n = c.execute("SELECT COALESCE(MAX(round_no),0)+1 FROM goal_round WHERE goal_id=?", (a.goal,)).fetchone()[0]
    cur = c.execute("INSERT INTO goal_round(goal_id,round_no,status) VALUES(?,?,?)", (a.goal, n, a.status))
    emit({"round_id": cur.lastrowid, "goal_id": a.goal, "round_no": n})

def round_link(a):
    db().execute("INSERT OR IGNORE INTO round_work(round_id,work_id) VALUES(?,?)", (a.round, a.work))
    emit({"ok": True, "round_id": a.round, "work_id": a.work})

def goal_review(a):
    c = db()
    verdict = a.verdict
    c.execute(
        "UPDATE goal_round SET status='closed',review_verdict=?,review_reason=?,reviewed_at=datetime('now') WHERE id=?",
        (verdict, a.reason, a.round),
    )
    row = c.execute("SELECT goal_id FROM goal_round WHERE id=?", (a.round,)).fetchone()
    if not row:
        raise SystemExit("round not found")
    status = {"done": "done", "wait": "waiting", "abandon": "abandoned", "next_round": "active"}[verdict]
    c.execute("UPDATE goal SET status=? WHERE id=?", (status, row["goal_id"]))
    emit({"goal_id": row["goal_id"], "round_id": a.round, "verdict": verdict, "goal_status": status})

def wait(a):
    c = db()
    c.execute(
        "INSERT INTO work_wait(work_id,condition_text,wake_at,reason) VALUES(?,?,?,?) ON CONFLICT(work_id) DO UPDATE SET condition_text=excluded.condition_text,wake_at=excluded.wake_at,reason=excluded.reason",
        (a.work, a.condition, a.wake_at, a.reason),
    )
    emit({"work_id": a.work, "waiting": True, "wake_at": a.wake_at})

def capability(a):
    c = db()
    c.execute(
        "INSERT INTO harness_capability(harness,capability,evidence_level,status,evidence_ref) VALUES(?,?,?,?,?) ON CONFLICT(harness,capability) DO UPDATE SET evidence_level=excluded.evidence_level,status=excluded.status,evidence_ref=excluded.evidence_ref,checked_at=datetime('now')",
        (a.harness, a.capability, a.evidence_level, a.status, a.evidence_ref),
    )
    emit({"harness": a.harness, "capability": a.capability, "evidence_level": a.evidence_level, "status": a.status})

def graph(a):
    c = db()
    w = c.execute("SELECT * FROM v_workgraph_v1 WHERE work_id=?", (a.work,)).fetchone()
    if not w:
        emit({"ok": False, "error": "work_not_found"})
        return
    emit({
        "work": dict(w),
        "dependencies": [dict(x) for x in c.execute("SELECT * FROM work_dependency WHERE work_id=?", (a.work,))],
        "sessions": [dict(x) for x in c.execute("SELECT * FROM session_binding WHERE work_id=?", (a.work,))],
        "artifacts": [dict(x) for x in c.execute("SELECT * FROM artifact WHERE work_id=?", (a.work,))],
        "gates": [dict(x) for x in c.execute("SELECT * FROM gate_decision WHERE work_id=?", (a.work,))],
    })

def select_cmd(a):
    harnesses = get_harnesses(DB, a.require_capability or [], a.min_evidence_level)
    print(json.dumps(harnesses, indent=2))

def build_parser():
    P = argparse.ArgumentParser(description="WorkGraph & Harness Capability Engine")
    P.add_argument("--require-capability", action="append", default=None,
                   help="Required capability (selector mode)")
    P.add_argument("--min-evidence-level", type=int, default=0,
                   help="Minimum evidence level required (selector mode)")

    S = P.add_subparsers(dest="cmd", required=False)

    p = S.add_parser("intent")
    p.add_argument("--title", required=True); p.add_argument("--key"); p.add_argument("--layer")
    p.add_argument("--status", default="draft"); p.add_argument("--source"); p.add_argument("--ir")
    p.set_defaults(f=intent)

    p = S.add_parser("link")
    p.add_argument("--work", type=int, required=True); p.add_argument("--intent", type=int, required=True)
    p.add_argument("--relation", default="implements")
    p.set_defaults(f=link)

    p = S.add_parser("depend")
    p.add_argument("--work", type=int, required=True); p.add_argument("--on", type=int, required=True)
    p.add_argument("--kind", default="blocks")
    p.set_defaults(f=depend)

    p = S.add_parser("bind")
    p.add_argument("--work", type=int, required=True); p.add_argument("--harness", required=True)
    p.add_argument("--session"); p.add_argument("--capability"); p.add_argument("--external-ref")
    p.add_argument("--status", default="active", choices=["active", "idle", "closed", "failed"])
    p.set_defaults(f=bind)

    p = S.add_parser("artifact")
    p.add_argument("--work", type=int, required=True); p.add_argument("--kind", required=True)
    p.add_argument("--uri"); p.add_argument("--file"); p.add_argument("--sha256")
    p.add_argument("--producer-session", type=int)
    p.set_defaults(f=artifact)

    p = S.add_parser("gate")
    p.add_argument("--work", type=int, required=True); p.add_argument("--gate", required=True)
    p.add_argument("--verdict", required=True, choices=["PASS", "FAIL", "VETO", "WAIVE"])
    p.add_argument("--reason"); p.add_argument("--evidence-event", type=int); p.add_argument("--by")
    p.set_defaults(f=gate)

    p = S.add_parser("goal")
    p.add_argument("--title", required=True); p.add_argument("--key"); p.add_argument("--intent", type=int)
    p.add_argument("--criteria"); p.add_argument("--status", default="active", choices=["active", "waiting", "done", "abandoned"])
    p.set_defaults(f=goal)

    p = S.add_parser("round")
    p.add_argument("--goal", type=int, required=True); p.add_argument("--number", type=int)
    p.add_argument("--status", default="active", choices=["planned", "active", "review", "closed"])
    p.set_defaults(f=round_add)

    p = S.add_parser("round-link")
    p.add_argument("--round", type=int, required=True); p.add_argument("--work", type=int, required=True)
    p.set_defaults(f=round_link)

    p = S.add_parser("goal-review")
    p.add_argument("--round", type=int, required=True)
    p.add_argument("--verdict", required=True, choices=["done", "wait", "abandon", "next_round"])
    p.add_argument("--reason")
    p.set_defaults(f=goal_review)

    p = S.add_parser("wait")
    p.add_argument("--work", type=int, required=True); p.add_argument("--condition", required=True)
    p.add_argument("--wake-at"); p.add_argument("--reason")
    p.set_defaults(f=wait)

    p = S.add_parser("capability")
    p.add_argument("--harness", required=True)
    p.add_argument("--capability", required=True, choices=["START", "AUTH", "MODEL_DISCOVERY", "STREAM", "STEER", "INTERRUPT", "RESUME", "SANDBOX", "FAILURE_SIGNAL", "RECOVER"])
    p.add_argument("--evidence-level", required=True, choices=["DECLARED", "DOCUMENTED", "SYNTHETIC", "NATIVE", "CANARY"])
    p.add_argument("--status", required=True, choices=["unknown", "pass", "fail", "degraded"])
    p.add_argument("--evidence-ref")
    p.set_defaults(f=capability)

    p = S.add_parser("graph")
    p.add_argument("--work", type=int, required=True)
    p.set_defaults(f=graph)

    p = S.add_parser("select")
    p.add_argument("--require-capability", action="append", default=[])
    p.add_argument("--min-evidence-level", type=int, default=0)
    p.set_defaults(f=select_cmd)

    return P

def main():
    P = build_parser()
    a = P.parse_args()

    # Si --require-capability est passe directement au niveau racine ou cmd is None
    if a.require_capability is not None or (a.cmd is None and not hasattr(a, 'f')):
        caps = a.require_capability or []
        db_path = os.environ.get("ASPACE_DB", DB)
        harnesses = get_harnesses(db_path, caps, a.min_evidence_level)
        print(json.dumps(harnesses, indent=2))
        return

    if hasattr(a, 'f'):
        a.f(a)
    else:
        P.print_help()

if __name__ == "__main__":
    main()

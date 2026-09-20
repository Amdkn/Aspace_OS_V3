#!/usr/bin/env python3
"""uc_workgraph.py — Sélecteur de capacités de harness (Harness Capability Selector).

Implémente un sélecteur sans dépendances externes pour filtrer les harnesses
selon leurs capacités (capabilities) et un niveau de preuve minimal (EvidenceLevel).
"""
import argparse
import json
import os
import sqlite3
from enum import Enum

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
        cur = c.execute("INSERT INTO work(layer, title) VALUES(?, ?)", (layer, title))
        return cur.lastrowid

    def create_round(self, goal_id: int) -> int:
        """Create a new Round for a given Goal."""
        c = self.cx()
        row = c.execute("SELECT layer FROM work WHERE id=?", (goal_id,)).fetchone()
        if not row:
            raise ValueError(f"Goal {goal_id} not found")
        cur = c.execute("INSERT INTO work(layer, title, parent_id) VALUES(?, ?, ?)",
                        (row['layer'], f"Round for Goal {goal_id}", goal_id))
        return cur.lastrowid

    def create_work(self, round_id: int, title: str) -> int:
        """Create a new Work item (task) for a given Round."""
        c = self.cx()
        row = c.execute("SELECT layer FROM work WHERE id=?", (round_id,)).fetchone()
        if not row:
            raise ValueError(f"Round {round_id} not found")
        cur = c.execute("INSERT INTO work(layer, title, parent_id) VALUES(?, ?, ?)",
                        (row['layer'], title, round_id))
        return cur.lastrowid

    def review_goal(self, goal_id: int, round_id: int, outcome: GoalOutcome, notes: str = "") -> int:
        """
        Record an independent Goal Review.
        Task completion is just evidence; only this explicit review sets the terminal outcome.
        """
        c = self.cx()
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


def cx(db_path):
    c = sqlite3.connect(db_path, isolation_level=None, timeout=10)
    c.row_factory = sqlite3.Row
    return c

def get_harnesses(db_path, required_caps, min_evidence):
    c = cx(db_path)

    # On parcourt les événements de type 'capability' dans l'ordre chronologique
    # pour ne garder que l'état le plus récent pour chaque couple (harness, capability)
    try:
        query = "SELECT harness, payload FROM event WHERE kind='capability' ORDER BY id ASC"
        rows = c.execute(query).fetchall()
    except sqlite3.OperationalError:
        # DB or table might not exist
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

    # Deterministic JSON ordering
    return sorted(result)

def main():
    p = argparse.ArgumentParser(description="Harness capability selector")
    p.add_argument("--require-capability", action="append", default=[],
                   help="Required capability (can be specified multiple times)")
    p.add_argument("--min-evidence-level", type=int, default=0,
                   help="Minimum evidence level required")
    a = p.parse_args()

    db_path = os.environ.get("ASPACE_DB", os.path.join(os.path.dirname(os.path.abspath(__file__)), "uc.db"))

    harnesses = get_harnesses(db_path, a.require_capability, a.min_evidence_level)
    print(json.dumps(harnesses, indent=2))

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""uc_workgraph.py — Sélecteur de capacités de harness (Harness Capability Selector).

Implémente un sélecteur sans dépendances externes pour filtrer les harnesses
selon leurs capacités (capabilities) et un niveau de preuve minimal (EvidenceLevel).
"""
import argparse
import json
import os
import sqlite3

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

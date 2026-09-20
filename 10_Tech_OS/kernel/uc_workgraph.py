#!/usr/bin/env python3
"""uc_workgraph.py — Sélecteur de capacités de harness (Harness Capability Selector).

Implémente un sélecteur sans dépendances externes pour filtrer les harnesses
selon leurs capacités (capabilities) et un niveau de preuve minimal (EvidenceLevel).
"""
import argparse
import json
import os
import sqlite3
import sys

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

def compile_intent(db_path, work_id, ipbd_path, source_sha256, alignment):
    try:
        with open(ipbd_path, 'r', encoding='utf-8') as f:
            ipbd_data = json.load(f)
    except Exception as e:
        print(f"Error reading IPBD file: {e}", file=sys.stderr)
        sys.exit(1)

    intent_ir = {
        "intention": ipbd_data.get("intention", ""),
        "problematiques": ipbd_data.get("problematiques", []),
        "besoins": ipbd_data.get("besoins", []),
        "desirs": ipbd_data.get("desirs", []),
        "alignment": alignment,
        "provenance": {
            "source_sha256": source_sha256
        }
    }

    # Deterministic output preserving Amadeus verbatim intent
    intent_json = json.dumps(intent_ir, sort_keys=True, indent=2, ensure_ascii=False)

    # Record evidence using uc.py's log function if possible
    if work_id is not None:
        try:
            import uc
            c = uc.cx()
            uc.log(c, work_id, "uc_workgraph", "evidence", json.loads(intent_json))
        except ImportError:
            c = cx(db_path)
            c.execute(
                "INSERT INTO event(work_id, harness, kind, payload) VALUES(?, ?, ?, ?)",
                (work_id, "uc_workgraph", "evidence", intent_json)
            )

    return intent_json

def main():
    if len(sys.argv) > 1 and sys.argv[1] not in ["select", "intent"] and "--require-capability" in sys.argv:
        sys.argv.insert(1, "select")

    p = argparse.ArgumentParser(description="Harness capability selector and IntentIR compiler")
    sp = p.add_subparsers(dest="cmd")

    # Select command (legacy behavior)
    p_select = sp.add_parser("select", help="Select harnesses based on capabilities")
    p_select.add_argument("--require-capability", action="append", default=[],
                   help="Required capability (can be specified multiple times)")
    p_select.add_argument("--min-evidence-level", type=int, default=0,
                   help="Minimum evidence level required")

    # Intent command
    p_intent = sp.add_parser("intent", help="Compile IPBD into deterministic IntentIR")
    p_intent.add_argument("--ipbd", required=True, help="Path to IPBD JSON file")
    p_intent.add_argument("--source-sha256", required=True, help="SHA-256 of the source")
    p_intent.add_argument("--alignment", default="", help="Alignment objective")
    p_intent.add_argument("--work-id", type=int, help="Work ID to record evidence in db")

    a = p.parse_args()

    db_path = os.environ.get("ASPACE_DB", os.path.join(os.path.dirname(os.path.abspath(__file__)), "uc.db"))

    if a.cmd == "intent":
        res = compile_intent(db_path, a.work_id, a.ipbd, a.source_sha256, a.alignment)
        print(res)
    else:
        # Default to select if cmd is None (e.g. no args) or 'select'
        caps = getattr(a, 'require_capability', [])
        min_ev = getattr(a, 'min_evidence_level', 0)
        harnesses = get_harnesses(db_path, caps, min_ev)
        print(json.dumps(harnesses, indent=2))

if __name__ == "__main__":
    main()

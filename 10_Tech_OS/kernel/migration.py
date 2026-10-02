#!/usr/bin/env python3
"""Schema-evolution migration for uc.db.

ADR-0007: prediction before execution, exactly-once effect safety.
This module is intentionally ALTER-only and idempotent: every statement
uses "ADD COLUMN IF NOT EXISTS" semantics via a pre-check, so replaying
migration on an already-current database is a no-op that still emits a
durable event. It never drops or rewrites existing columns.

The live defect it closes: `uc.py wait` writes `wake_at` onto `work`,
but the production uc.db at C:/Users/amado/ASpace_OS_V3/10_Tech_OS/kernel/uc.db
was initialized from an older schema whose `work` table had no `wake_at`
column. `cmd_wait` therefore failed at runtime and the Wargame #322 cell
lost its valid runtime binding on lease expiry with no way to wake.
"""
from __future__ import annotations

import argparse
import json
import os
import sqlite3
import sys
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
DB = os.environ.get("ASPACE_DB", os.path.join(HERE, "uc.db"))

# (table, column, ddl) — additive only.
SCHEMA_EVOLUTION = [
    ("work", "wake_at", "ALTER TABLE work ADD COLUMN wake_at TEXT"),
    ("work", "institutional_owner", "ALTER TABLE work ADD COLUMN institutional_owner TEXT"),
    ("work", "correlation_id", "ALTER TABLE work ADD COLUMN correlation_id TEXT"),
    ("claim", "institutional_owner", "ALTER TABLE claim ADD COLUMN institutional_owner TEXT"),
    ("claim", "runtime_id", "ALTER TABLE claim ADD COLUMN runtime_id TEXT"),
    ("session_binding", "institutional_owner", "ALTER TABLE session_binding ADD COLUMN institutional_owner TEXT"),
    ("session_binding", "runtime_id", "ALTER TABLE session_binding ADD COLUMN runtime_id TEXT"),
    ("work_wait", "institutional_owner", "ALTER TABLE work_wait ADD COLUMN institutional_owner TEXT"),
]


def _connect() -> sqlite3.Connection:
    c = sqlite3.connect(DB, isolation_level=None, timeout=10)
    c.row_factory = sqlite3.Row
    c.execute("PRAGMA foreign_keys=ON")
    c.execute("PRAGMA busy_timeout=5000")
    return c


def _column_exists(c: sqlite3.Connection, table: str, column: str) -> bool:
    return any(r[1] == column for r in c.execute(f"PRAGMA table_info({table})"))


def apply_migration(db_path: str = DB, dry_run: bool = False) -> dict:
    global DB
    DB = db_path
    c = _connect()
    applied: list[dict] = []
    missing_tables: list[str] = []
    for table, column, ddl in SCHEMA_EVOLUTION:
        try:
            tables = {r[0] for r in c.execute(
                "SELECT name FROM sqlite_master WHERE type='table'")}
            if table not in tables:
                missing_tables.append(table)
                continue
            if _column_exists(c, table, column):
                continue
            applied.append({"table": table, "column": column, "ddl": ddl})
            if not dry_run:
                c.execute(ddl)
        except sqlite3.OperationalError as exc:
            applied.append({"table": table, "column": column, "error": str(exc)})
    result = {
        "ok": True,
        "db": DB,
        "applied": applied,
        "missing_tables": missing_tables,
        "dry_run": dry_run,
        "observed_at": datetime.now(timezone.utc).isoformat(),
    }
    if not dry_run:
        c.execute(
            "INSERT INTO event(work_id,harness,kind,payload) VALUES(?,?,?,?)",
            (None, "uc.py", "migrate", json.dumps(result, ensure_ascii=False)),
        )
    c.close()
    return result


def main() -> None:
    p = argparse.ArgumentParser(description="Additive schema-evolution migration for uc.db")
    p.add_argument("--db", default=DB)
    p.add_argument("--dry-run", action="store_true")
    a = p.parse_args()
    out = apply_migration(db_path=a.db, dry_run=a.dry_run)
    print(json.dumps(out, ensure_ascii=False, indent=1))
    sys.exit(0 if out["ok"] else 1)


if __name__ == "__main__":
    main()
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


def _connect(db_path: str) -> sqlite3.Connection:
    c = sqlite3.connect(db_path, isolation_level=None, timeout=10)
    c.row_factory = sqlite3.Row
    c.execute("PRAGMA foreign_keys=ON")
    c.execute("PRAGMA busy_timeout=5000")
    return c


def _column_exists(c: sqlite3.Connection, table: str, column: str) -> bool:
    return any(r[1] == column for r in c.execute(f"PRAGMA table_info({table})"))


def apply_migration(db_path: str = DB, dry_run: bool = False) -> dict:
    c = _connect(db_path)
    applied: list[dict] = []
    errors: list[dict] = []
    tables = {r[0] for r in c.execute(
        "SELECT name FROM sqlite_master WHERE type='table'")}
    required_tables = {table for table, _, _ in SCHEMA_EVOLUTION} | {"event"}
    missing_tables = sorted(required_tables - tables)

    if missing_tables:
        result = {
            "ok": False,
            "db": db_path,
            "applied": applied,
            "errors": errors,
            "missing_tables": missing_tables,
            "dry_run": dry_run,
            "observed_at": datetime.now(timezone.utc).isoformat(),
        }
        c.close()
        return result

    pending = [
        {"table": table, "column": column, "ddl": ddl}
        for table, column, ddl in SCHEMA_EVOLUTION
        if not _column_exists(c, table, column)
    ]
    if dry_run:
        result = {
            "ok": True,
            "db": db_path,
            "applied": pending,
            "errors": errors,
            "missing_tables": [],
            "dry_run": True,
            "observed_at": datetime.now(timezone.utc).isoformat(),
        }
        c.close()
        return result

    try:
        c.execute("BEGIN IMMEDIATE")
        for item in pending:
            c.execute(item["ddl"])
            applied.append(item)
        result = {
            "ok": True,
            "db": db_path,
            "applied": applied,
            "errors": errors,
            "missing_tables": [],
            "dry_run": False,
            "observed_at": datetime.now(timezone.utc).isoformat(),
        }
        c.execute(
            "INSERT INTO event(work_id,harness,kind,payload) VALUES(?,?,?,?)",
            (None, "uc.py", "migrate", json.dumps(result, ensure_ascii=False)),
        )
        c.execute("COMMIT")
    except sqlite3.Error as exc:
        c.execute("ROLLBACK")
        errors.append({"error": str(exc)})
        result = {
            "ok": False,
            "db": db_path,
            "applied": [],
            "errors": errors,
            "missing_tables": [],
            "dry_run": False,
            "observed_at": datetime.now(timezone.utc).isoformat(),
        }
    finally:
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
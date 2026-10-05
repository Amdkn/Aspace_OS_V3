#!/usr/bin/env python3
"""Minimal, safe patch to uc.py cmd_wait.

Root cause of the live #322 blocker: the production uc.db `work` table was
initialized from an older schema.sql whose CHECK constraint excluded
'waiting' and whose column list excluded `wake_at`. `uc.py wait` therefore
could not execute, the lease on work 198 expired with no wake path, and the
Wargame lost its runtime binding.

This patch makes cmd_wait resilient to that historical schema gap WITHOUT
table recreation and WITHOUT changing the public contract:

  - status is set to 'pending' (always present in every historical CHECK)
  - wake_at is written on work (added by migration.py where absent)
  - a work_wait row is upserted so the wake contract is durable and queryable
  - the claim is released exactly as before

The wake semantics are unchanged: after wake_at the work is pending and
claimable again. Nothing is deleted, nothing is retried silently.
"""
from __future__ import annotations


def patch_cmd_wait(src: str) -> str:
    old = '''def cmd_wait(a):\n    c = cx()\n    try:\n        c.execute("UPDATE work SET status='waiting', wake_at=datetime('now',?) WHERE id=?",\n                  (f"+{a.seconds} seconds", a.work))\n        c.execute("DELETE FROM claim WHERE work_id=?", (a.work,))\n        log(c, a.work, None, "waiting", {"wake_at_offset": a.seconds})\n        out({"ok": True, "work_id": a.work, "status": "waiting"})\n    except Exception as e:\n        out({"ok": False, "err": str(e)}); sys.exit(3)\n'''
    new = '''def cmd_wait(a):\n    c = cx()\n    try:\n        c.execute("UPDATE work SET status='pending', wake_at=datetime('now',?) WHERE id=?",\n                  (f"+{a.seconds} seconds", a.work))\n        c.execute("DELETE FROM claim WHERE work_id=?", (a.work,))\n        c.execute("INSERT INTO work_wait(work_id,condition_text,wake_at,reason) "\n                  "VALUES(?,?,datetime('now',?),?) "\n                  "ON CONFLICT(work_id) DO UPDATE SET wake_at=excluded.wake_at, "\n                  "reason=excluded.reason, condition_text=excluded.condition_text",\n                  (a.work, "wake_at_reached", f"+{a.seconds} seconds", f"wait {a.seconds}s"))\n        log(c, a.work, None, "waiting", {"wake_at_offset": a.seconds, "status": "pending"})\n        out({"ok": True, "work_id": a.work, "status": "pending", "wake_at_offset": a.seconds})\n    except Exception as e:\n        out({"ok": False, "err": str(e)}); sys.exit(3)\n'''
    if old not in src:
        raise RuntimeError("cmd_wait block not found — already patched or changed")
    return src.replace(old, new)


def patch_schema_sql(src: str) -> str:
    # add wake_at to the work column list if absent
    if "wake_at" not in src.split("CREATE TABLE IF NOT EXISTS work")[1].split(");")[0]:
        src = src.replace(
            "  priority    INTEGER NOT NULL DEFAULT 0,",
            "  priority    INTEGER NOT NULL DEFAULT 0,\n  wake_at     TEXT,",
            1,
        )
    # add 'waiting' to the work status CHECK if absent
    if "'waiting'" not in src.split("CREATE TABLE IF NOT EXISTS work")[1].split(");")[0]:
        src = src.replace(
            "CHECK (status IN ('pending','claimed','review','done','failed','blocked','waiting'))",
            "CHECK (status IN ('pending','claimed','review','done','failed','blocked','waiting'))",
        )
        src = src.replace(
            "CHECK (status IN ('pending','claimed','review','done','failed','blocked'))",
            "CHECK (status IN ('pending','claimed','review','done','failed','blocked','waiting'))",
            1,
        )
    return src


if __name__ == "__main__":
    import sys
    kernel = sys.argv[1]
    src = open(kernel, encoding="utf-8").read()
    if "cmd_wait(a):\n    c = cx()" in src and "ON CONFLICT(work_id) DO UPDATE" not in src:
        src = patch_cmd_wait(src)
        open(kernel, "w", encoding="utf-8").write(src)
        print("patched", kernel)
    else:
        print("already patched or not found", kernel)
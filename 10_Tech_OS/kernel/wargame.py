"""Wargame Continuation Protocol (Issue #321)."""
from __future__ import annotations

import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ALLOWED_OUTCOMES = {
    "NEXT_GATE",
    "CHILD_CELL_REQUIRED",
    "RECON_NEEDED",
    "CERTIFICATION_REQUIRED",
    "PROMOTE",
    "REJECT",
    "PARTIAL",
    "ESCALATE_S2",
    "ESCALATE_S1",
    "ESCALATE_A0",
}


class WargameProtocolError(RuntimeError):
    pass


def _connect(db_path: str | Path) -> sqlite3.Connection:
    con = sqlite3.connect(Path(db_path), timeout=10)
    con.row_factory = sqlite3.Row
    con.execute("PRAGMA foreign_keys=ON")
    return con


def parse_time(value: str | None) -> datetime | None:
    if not value:
        return None
    text = value.strip().replace("Z", "+00:00")
    try:
        parsed = datetime.fromisoformat(text)
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def record_outcome(
    db_path: str | Path,
    github_issue: int,
    outcome: str,
    *,
    now: datetime | None = None,
) -> dict[str, Any]:
    """Record a round outcome. The outcome MUST be one of ALLOWED_OUTCOMES."""
    if outcome not in ALLOWED_OUTCOMES:
        raise WargameProtocolError(
            f"invalid machine-readable outcome: '{outcome}'. "
            f"Must be one of {', '.join(sorted(ALLOWED_OUTCOMES))}"
        )

    current_time = (now or datetime.now(timezone.utc)).astimezone(timezone.utc)
    time_str = current_time.isoformat()

    with _connect(db_path) as con:
        # Check if the wargame exists, if not raise error or create it depending on assumption.
        # Assuming the caller expects it to exist or we just upsert it.
        # It's safer to ensure it exists first, or just upsert the basic fields.
        row = con.execute("SELECT * FROM wargame WHERE github_issue=?", (github_issue,)).fetchone()
        if not row:
            con.execute(
                """INSERT INTO wargame (github_issue, state, current_round, next_gate, created_at, updated_at)
                   VALUES (?, 'OPEN', 1, ?, ?, ?)""",
                (github_issue, outcome, time_str, time_str)
            )
            current_round = 1
        else:
            current_round = row["current_round"] + 1
            con.execute(
                """UPDATE wargame
                   SET current_round=?, next_gate=?, updated_at=?
                   WHERE github_issue=?""",
                (current_round, outcome, time_str, github_issue)
            )

        payload = {
            "github_issue": github_issue,
            "outcome": outcome,
            "round": current_round,
            "recorded_at": time_str,
        }

        con.execute(
            "INSERT INTO event(work_id, harness, kind, payload) VALUES(?, ?, ?, ?)",
            (None, "wargame.py", "wargame_outcome", json.dumps(payload)),
        )
        con.commit()

    return payload


def is_stale(
    db_path: str | Path,
    github_issue: int,
    *,
    now: datetime | None = None,
) -> bool:
    """Evaluate Wargame staleness according to the Staleness law."""
    current_time = (now or datetime.now(timezone.utc)).astimezone(timezone.utc)

    with _connect(db_path) as con:
        row = con.execute("SELECT * FROM wargame WHERE github_issue=?", (github_issue,)).fetchone()
        if not row:
            return False

        wargame = dict(row)

        if wargame["state"] != "OPEN":
            return False

        if not wargame["next_gate"]:
            return False

        stale_after_str = wargame.get("stale_after")
        if not stale_after_str:
            return False

        stale_after = parse_time(stale_after_str)
        if not stale_after or current_time <= stale_after:
            return False

        children = con.execute(
            "SELECT id, work_id FROM wargame_child WHERE parent_issue=? AND status='ACTIVE'",
            (github_issue,),
        ).fetchall()

        # Check if any active child has a live claim or binding
        for child in children:
            work_id = child["work_id"]
            if not work_id:
                continue

            # check claim
            claim_row = con.execute("SELECT expires_at FROM claim WHERE work_id=?", (work_id,)).fetchone()
            if claim_row:
                expires_at = parse_time(claim_row["expires_at"])
                if expires_at and current_time < expires_at:
                    return False # Active claim exists

            # check binding
            binding_row = con.execute(
                "SELECT id FROM session_binding WHERE work_id=? AND status IN ('active', 'idle') AND ended_at IS NULL",
                (work_id,),
            ).fetchone()
            if binding_row:
                return False # Active binding exists

        return True

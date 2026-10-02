import json
import sqlite3
from typing import Any

def donna_evaluate_dlq(motif: str, attempts: int) -> dict[str, str]:
    """
    Donna filters at least 80% of injected recovery/escalation events away from Rick.
    """
    m = motif.lower()
    if "transient" in m or "timeout" in m or "network" in m:
        return {"action": "recover", "reason": "auto-recovery via policy (transient)"}
    if "adapter bug" in m or "merge conflict" in m:
        return {"action": "recover", "reason": "local repair (technical)"}
    if "quota exhaustion" in m:
        return {"action": "recover", "reason": "alternative runtime available"}
    if "pr merge conflict" in m:
        return {"action": "recover", "reason": "local repair (technical)"}
    if "local runtime failure" in m:
        return {"action": "recover", "reason": "local runtime recovery"}
    if "repeated recoverable unknown" in m:
        return {"action": "recover", "reason": "auto-recovery via policy (recoverable)"}

    return {"action": "escalate_rick", "reason": "requires Rick arbitration"}

def rick_evaluate_escalation(issue_desc: str, irreversible: bool = False, constitutional_change: bool = False) -> dict[str, Any]:
    """
    Rick filters non-owner cases away from A0.
    A0 required only when:
    - material irreversible financial/legal commitment
    - constitutional layer/mission changes
    - system cannot infer value judgment from existing policy
    """
    if constitutional_change:
        return {"action": "escalate_a0", "reason": "constitutional layer/mission change"}
    if irreversible:
        return {"action": "escalate_a0", "reason": "irreversible financial/legal commitment"}

    return {"action": "rick_handled", "reason": "handled by Rick policy"}

def evaluate_portfolio(con: sqlite3.Connection) -> dict[str, Any]:
    """
    Evaluates current L0/L1/L2 allocation from the work table.
    """
    con.row_factory = sqlite3.Row
    rows = con.execute("SELECT layer, COUNT(*) as n FROM work WHERE status != 'done' AND layer IN ('L0', 'L1', 'L2') GROUP BY layer").fetchall()
    total = sum(r["n"] for r in rows)
    if total == 0:
        return {"L0": 0.0, "L1": 0.0, "L2": 0.0}

    alloc = {r["layer"]: float(r["n"])/total for r in rows}
    return {
        "L0": alloc.get("L0", 0.0),
        "L1": alloc.get("L1", 0.0),
        "L2": alloc.get("L2", 0.0)
    }

def rick_approve_burst(con: sqlite3.Connection, layer: str, reason: str, is_reusable_blocker: bool) -> dict[str, Any]:
    """
    Rick sets envelopes and approves burst if genuine reusable blocker.
    """
    if layer == "L0" and is_reusable_blocker:
        return {"approved": True, "reason": "reusable blocker, temporary L0 burst authorized"}
    return {"approved": False, "reason": "burst not justified by reusable blocker"}

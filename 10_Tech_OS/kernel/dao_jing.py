"""Read-only Dao -> Jing projections; no work-state or UI authority."""
import argparse
import hashlib
import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from topology_validator import HERE, load_constitution, validate_constitution, ROLES

MAX_ITEMS = 8
MAX_BYTES = 8192

def encode(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")

def parse_time(value):
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    return parsed.replace(tzinfo=timezone.utc) if parsed.tzinfo is None else parsed.astimezone(timezone.utc)

def project(db_path, role, work_id=None, *, as_of=None, constitution=None):
    doc = validate_constitution(constitution or load_constitution())
    if role not in ROLES:
        raise ValueError("Unknown role")
    if work_id is not None and (type(work_id) is not int or work_id <= 0):
        raise ValueError("work_id must be a positive integer")
    now = parse_time(as_of) if as_of else datetime.now(timezone.utc).replace(microsecond=0)
    scope = doc["projection_roles"][role]
    c = sqlite3.connect(Path(db_path).resolve().as_uri() + "?mode=ro", uri=True, timeout=5)
    c.row_factory = sqlite3.Row
    try:
        c.execute("PRAGMA query_only=ON")
        c.execute("BEGIN")
        if work_id is not None:
            condition, params = "id=?", (work_id,)
        else:
            condition = "layer IN (" + ",".join("?" for _ in scope["layers"]) + ")"
            params = tuple(scope["layers"])
        total = c.execute("SELECT count(*) FROM work WHERE " + condition, params).fetchone()[0]
        rows = c.execute("SELECT id,layer,title,status,updated_at FROM work WHERE " + condition +
                         " ORDER BY id DESC LIMIT ?", (*params, MAX_ITEMS)).fetchall()
        if work_id is not None and not rows:
            raise ValueError("Unknown work_id")
        items = []
        for w in rows:
            wid = w["id"]
            claim = c.execute("SELECT harness,expires_at FROM claim WHERE work_id=?", (wid,)).fetchone()
            bindings = c.execute("SELECT id,harness,status FROM session_binding WHERE work_id=? "
                                 "AND status='active' AND ended_at IS NULL ORDER BY id DESC LIMIT 4", (wid,)).fetchall()
            live_claim = bool(claim and parse_time(claim["expires_at"]) > now)
            matched = bool(live_claim and any(b["harness"] == claim["harness"] for b in bindings))
            artifacts = [dict(x) for x in c.execute(
                "SELECT id,kind,sha256 FROM artifact WHERE work_id=? ORDER BY id DESC LIMIT 3", (wid,))]
            gates = [dict(x) for x in c.execute(
                "SELECT id,gate,verdict FROM gate_decision WHERE work_id=? ORDER BY id DESC LIMIT 3", (wid,))]
            drift = []
            if w["status"] in ("claimed", "running") and not live_claim:
                drift.append("expired_or_missing_claim")
            if bindings and not live_claim:
                drift.append("orphan_binding")
            if live_claim and not matched:
                drift.append("missing_matching_binding")
            if w["status"] == "done" and not artifacts:
                drift.append("done_without_artifact")
            if w["status"] == "done" and (not gates or gates[0]["verdict"].lower() != "pass"):
                drift.append("done_without_passing_latest_gate")
            if w["status"] in ("done", "failed") and (claim or bindings):
                drift.append("terminal_work_has_owner")
            items.append({"work_id": wid, "layer": w["layer"], "title": w["title"][:120],
                          "status": w["status"], "updated_at": w["updated_at"],
                          "ownership": {"live_claim": live_claim, "matching_binding": matched,
                                        "executing": False, "execution_observation": "not_observed"},
                          "artifacts": artifacts, "gates": gates, "drift": drift})
        snapshot = {"role": role, "as_of": now.isoformat(), "items": items, "total": total}
        digest = hashlib.sha256(encode(snapshot)).hexdigest()
    finally:
        c.close()
    result = {"schema": "WorkGraphProjection.v1", "role": role, "tier": scope["tier"],
              "authority": "read_only", "source": "uc.db", "as_of": now.isoformat(),
              "source_snapshot_sha256": digest, "snapshot_sha256": "0"*64,
              "hash_contract": "sha256 of canonical compact sorted UTF-8 response excluding snapshot_sha256",
              "constitution_sha256": hashlib.sha256(encode(doc)).hexdigest(),
              "scope": {"home_layers": scope["layers"], "explicit_cross_core_focus": work_id is not None},
              "items": items, "omitted_count": total-len(items),
              "bounds": {"max_items": MAX_ITEMS, "max_bytes": MAX_BYTES},
              "drift_count": sum(bool(x["drift"]) for x in items)}
    while len(encode(result)) > MAX_BYTES and result["items"]:
        result["items"].pop()
        result["omitted_count"] += 1
    result["drift_count"] = sum(bool(x["drift"]) for x in result["items"])
    result["snapshot_sha256"] = hashlib.sha256(encode({key: value for key, value in result.items() if key != "snapshot_sha256"})).hexdigest()
    if len(encode(result)) > MAX_BYTES:
        raise ValueError("Projection envelope exceeds byte bound")
    return result

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--db", type=Path, default=HERE / "uc.db")
    p.add_argument("--role", choices=ROLES, default="Rick")
    p.add_argument("--work-id", type=int)
    p.add_argument("--as-of")
    args = p.parse_args()
    try:
        result = project(args.db, args.role, args.work_id, as_of=args.as_of)
    except (ValueError, sqlite3.Error, OSError) as exc:
        print(json.dumps({"ok": False, "error": str(exc)}))
        return 1
    print(encode(result).decode("utf-8"))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

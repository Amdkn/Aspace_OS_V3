#!/usr/bin/env python3
"""A'Space Machine Fabric M0 durable mutation kernel.

Clara contract implemented here:
typed capability -> policy -> operation_id -> precondition -> effect ->
durable receipt -> replay/compensation.

M0 deliberately contains no browser, UIA, process-control, or remote transport.
It uses only the Python standard library and binds HTTP to loopback.
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
import sqlite3
import sys
import tempfile
import threading
from contextlib import contextmanager
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any
from urllib.parse import unquote, urlparse

OP_SCHEMA = "aspace.machine.operation.v1"
RECEIPT_SCHEMA = "aspace.machine.receipt.v1"
HEALTH_SCHEMA = "aspace.machine.health.v1"
MANIFEST_SCHEMA = "aspace.machine.capability-manifest.v1"
POLICY_VERSION = "amf-m0-policy-v1"
ADAPTER_ID = "amf.m0.python-stdlib.fs"
TERMINAL_STATES = {"SUCCEEDED", "FAILED", "COMPENSATED", "DENIED", "DLQ"}

CAPABILITIES = {
    "machine.fs.read": {
        "schema": MANIFEST_SCHEMA,
        "capability_id": "machine.fs.read",
        "version": "0.1.0",
        "adapter": ADAPTER_ID,
        "requires_worker": False,
        "actions": [{"name": "read_text", "risk_class": "read"}],
        "health": "AVAILABLE",
    },
    "machine.fs.write": {
        "schema": MANIFEST_SCHEMA,
        "capability_id": "machine.fs.write",
        "version": "0.1.0",
        "adapter": ADAPTER_ID,
        "requires_worker": False,
        "actions": [
            {"name": "write_text", "risk_class": "reversible_write"},
            {"name": "append_text", "risk_class": "reversible_write"},
            {"name": "compensate", "risk_class": "reversible_write"},
        ],
        "health": "AVAILABLE",
    },
}


class AMFError(Exception):
    status = 400
    code = "AMF_ERROR"


class InvalidOperation(AMFError):
    code = "INVALID_OPERATION"


class OperationConflict(AMFError):
    status = 409
    code = "OPERATION_ID_FINGERPRINT_CONFLICT"


class ReceiptNotFound(AMFError):
    status = 404
    code = "RECEIPT_NOT_FOUND"


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def semantic_fingerprint(operation: dict[str, Any]) -> str:
    """Fingerprint intent, excluding transport identity and the fingerprint itself."""
    material = {
        "schema": operation.get("schema"),
        "capability": operation.get("capability"),
        "capability_version": operation.get("capability_version"),
        "action": operation.get("action"),
        "authority": operation.get("authority"),
        "precondition": operation.get("precondition"),
        "replay": operation.get("replay"),
        "payload": operation.get("payload") or {},
    }
    return hashlib.sha256(canonical_json(material).encode("utf-8")).hexdigest()


def with_fingerprint(operation: dict[str, Any]) -> dict[str, Any]:
    out = json.loads(json.dumps(operation))
    out["fingerprint"] = semantic_fingerprint(out)
    return out


def _json_or_none(raw: str | None) -> Any:
    return json.loads(raw) if raw else None


class AMFEngine:
    def __init__(self, db_path: str | Path, allowed_root: str | Path):
        self.db_path = Path(db_path).resolve()
        self.allowed_root = Path(allowed_root).resolve()
        self.allowed_root.mkdir(parents=True, exist_ok=True)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._lock = threading.RLock()
        self._init_db()

    @property
    def scope(self) -> str:
        return "fs:" + str(self.allowed_root)

    def _connect(self) -> sqlite3.Connection:
        con = sqlite3.connect(self.db_path, timeout=10)
        con.row_factory = sqlite3.Row
        con.execute("PRAGMA journal_mode=WAL")
        con.execute("PRAGMA synchronous=FULL")
        con.execute("PRAGMA foreign_keys=ON")
        con.execute("PRAGMA busy_timeout=5000")
        return con

    @contextmanager
    def _db(self):
        con = self._connect()
        try:
            yield con
            con.commit()
        except Exception:
            con.rollback()
            raise
        finally:
            con.close()

    def _init_db(self) -> None:
        with self._db() as con:
            con.executescript(
                """
                CREATE TABLE IF NOT EXISTS operations (
                    operation_id TEXT PRIMARY KEY,
                    fingerprint TEXT NOT NULL,
                    capability TEXT NOT NULL,
                    capability_version TEXT NOT NULL,
                    action TEXT NOT NULL,
                    state TEXT NOT NULL,
                    policy_decision TEXT NOT NULL,
                    policy_version TEXT NOT NULL,
                    request_json TEXT NOT NULL,
                    plan_json TEXT,
                    effect_digest TEXT,
                    receipt_json TEXT,
                    compensation_ref TEXT,
                    claimed_at TEXT NOT NULL,
                    started_at TEXT,
                    finished_at TEXT
                );

                CREATE TABLE IF NOT EXISTS events (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    operation_id TEXT NOT NULL,
                    kind TEXT NOT NULL,
                    payload_json TEXT NOT NULL,
                    created_at TEXT NOT NULL
                );

                CREATE INDEX IF NOT EXISTS idx_events_operation
                ON events(operation_id, id);
                """
            )
            columns = {
                row["name"] for row in con.execute("PRAGMA table_info(operations)").fetchall()
            }
            if "capability_version" not in columns:
                con.execute(
                    "ALTER TABLE operations ADD COLUMN capability_version TEXT"
                )
                con.execute(
                    "UPDATE operations SET capability_version='legacy-unbound' "
                    "WHERE capability_version IS NULL"
                )

    def _event(self, con: sqlite3.Connection, operation_id: str, kind: str, payload: dict[str, Any]) -> None:
        con.execute(
            "INSERT INTO events(operation_id, kind, payload_json, created_at) VALUES(?,?,?,?)",
            (operation_id, kind, canonical_json(payload), now_iso()),
        )

    def _validate_operation(self, op: dict[str, Any]) -> None:
        required = {
            "schema", "operation_id", "capability", "capability_version", "action",
            "authority", "fingerprint", "precondition", "replay",
        }
        missing = required - set(op)
        extra = set(op) - (required | {"payload"})
        if missing:
            raise InvalidOperation("missing fields: " + ", ".join(sorted(missing)))
        if extra:
            raise InvalidOperation("unexpected fields: " + ", ".join(sorted(extra)))
        if op["schema"] != OP_SCHEMA:
            raise InvalidOperation("invalid operation schema")
        if not isinstance(op["operation_id"], str) or len(op["operation_id"]) < 8:
            raise InvalidOperation("operation_id must be at least 8 characters")
        if not isinstance(op["fingerprint"], str) or len(op["fingerprint"]) < 16:
            raise InvalidOperation("fingerprint must be at least 16 characters")
        expected = semantic_fingerprint(op)
        if op["fingerprint"] != expected:
            raise InvalidOperation("fingerprint does not match canonical operation intent")
        if op["capability"] not in CAPABILITIES:
            raise InvalidOperation("unknown capability")
        expected_capability_version = CAPABILITIES[op["capability"]]["version"]
        if op["capability_version"] != expected_capability_version:
            raise InvalidOperation(
                "capability_version does not match capability manifest"
            )
        actions = {x["name"] for x in CAPABILITIES[op["capability"]]["actions"]}
        if op["action"] not in actions:
            raise InvalidOperation("action not in capability manifest")
        if op["replay"] not in {"never", "return_receipt", "retry_if_no_effect", "compensate_then_retry"}:
            raise InvalidOperation("invalid replay class")
        if not isinstance(op["precondition"], dict):
            raise InvalidOperation("precondition must be an object")
        if not isinstance(op.get("payload", {}), dict):
            raise InvalidOperation("payload must be an object")
        authority = op["authority"]
        if not isinstance(authority, dict):
            raise InvalidOperation("authority must be an object")
        if set(authority) - {"risk_class", "scopes", "approval_ref"}:
            raise InvalidOperation("unexpected authority field")
        if authority.get("risk_class") not in {"read", "reversible_write", "consequential", "privileged"}:
            raise InvalidOperation("invalid authority risk_class")
        if not isinstance(authority.get("scopes"), list):
            raise InvalidOperation("authority scopes must be an array")

    def _target_for(self, op: dict[str, Any]) -> Path:
        payload = op.get("payload") or {}
        allowed = {
            "read_text": {"path", "encoding"},
            "write_text": {"path", "text", "encoding"},
            "append_text": {"path", "text", "encoding"},
            "compensate": {"original_operation_id"},
        }[op["action"]]
        unexpected = set(payload) - allowed
        if unexpected:
            raise InvalidOperation("payload contains forbidden fields: " + ", ".join(sorted(unexpected)))

        if op["action"] == "compensate":
            original = payload.get("original_operation_id")
            if not isinstance(original, str) or not original:
                raise InvalidOperation("compensate requires original_operation_id")
            with self._db() as con:
                row = con.execute(
                    "SELECT plan_json FROM operations WHERE operation_id=?",
                    (original,),
                ).fetchone()
            if not row or not row["plan_json"]:
                raise InvalidOperation("original operation has no reversible plan")
            plan = json.loads(row["plan_json"])
            return Path(plan["target"]).resolve()

        raw = payload.get("path")
        if not isinstance(raw, str) or not raw or "\x00" in raw:
            raise InvalidOperation("payload.path must be a non-empty safe string")
        candidate = Path(raw).expanduser()
        if not candidate.is_absolute():
            candidate = self.allowed_root / candidate
        return candidate.resolve(strict=False)

    def _inside_allowed_root(self, target: Path) -> bool:
        try:
            target.relative_to(self.allowed_root)
            return True
        except ValueError:
            return False

    def evaluate_policy(self, op: dict[str, Any], target: Path) -> tuple[str, str]:
        authority = op["authority"]
        expected_risk = "read" if op["capability"] == "machine.fs.read" else "reversible_write"
        if authority["risk_class"] != expected_risk:
            return "DENY", f"risk_class must be {expected_risk}"
        if self.scope not in authority["scopes"]:
            return "DENY", "required filesystem scope missing"
        if not self._inside_allowed_root(target):
            return "DENY", "target outside allowed root"
        return "ALLOW", "bounded capability inside explicit root"

    def _receipt(
        self,
        op: dict[str, Any],
        state: str,
        policy_decision: str,
        *,
        effect_digest: str | None = None,
        evidence: list[str] | None = None,
        compensation_ref: str | None = None,
        result: Any = None,
        reconciled: bool = False,
    ) -> dict[str, Any]:
        receipt: dict[str, Any] = {
            "schema": RECEIPT_SCHEMA,
            "operation_id": op["operation_id"],
            "fingerprint": op["fingerprint"],
            "state": state,
            "capability": op["capability"],
            "capability_version": op["capability_version"],
            "adapter": ADAPTER_ID,
            "policy": {
                "decision": policy_decision,
                "policy_version": POLICY_VERSION,
            },
            "effect_digest": effect_digest,
            "evidence": evidence or [],
            "compensation_ref": compensation_ref,
            "finished_at": now_iso(),
        }
        if result is not None:
            receipt["result"] = result
        if reconciled:
            receipt["reconciled_after_restart"] = True
        return receipt

    def _persist_terminal(
        self,
        con: sqlite3.Connection,
        op: dict[str, Any],
        receipt: dict[str, Any],
        *,
        effect_digest: str | None = None,
        compensation_ref: str | None = None,
    ) -> None:
        con.execute(
            """
            UPDATE operations
            SET state=?, effect_digest=?, receipt_json=?, compensation_ref=?, finished_at=?
            WHERE operation_id=?
            """,
            (
                receipt["state"],
                effect_digest,
                canonical_json(receipt),
                compensation_ref,
                receipt["finished_at"],
                op["operation_id"],
            ),
        )
        self._event(con, op["operation_id"], "RECEIPT", receipt)

    def get_receipt(self, operation_id: str) -> dict[str, Any]:
        with self._db() as con:
            row = con.execute(
                "SELECT receipt_json FROM operations WHERE operation_id=?",
                (operation_id,),
            ).fetchone()
        if not row or not row["receipt_json"]:
            raise ReceiptNotFound(operation_id)
        return json.loads(row["receipt_json"])

    def ledger_row(self, operation_id: str) -> dict[str, Any] | None:
        with self._db() as con:
            row = con.execute(
                "SELECT * FROM operations WHERE operation_id=?",
                (operation_id,),
            ).fetchone()
        return dict(row) if row else None

    def _precondition_ok(self, op: dict[str, Any], target: Path) -> tuple[bool, str]:
        pre = op["precondition"]
        if "exists" in pre and bool(target.exists()) != bool(pre["exists"]):
            return False, "exists precondition failed"
        if "sha256" in pre:
            if not target.is_file():
                return False, "sha256 precondition requires existing file"
            current = sha256_bytes(target.read_bytes())
            if current != pre["sha256"]:
                return False, "sha256 precondition failed"
        return True, "precondition satisfied"

    def _make_plan(self, op: dict[str, Any], target: Path) -> dict[str, Any]:
        before_exists = target.is_file()
        before = target.read_bytes() if before_exists else b""
        action = op["action"]
        payload = op.get("payload") or {}
        encoding = payload.get("encoding") or "utf-8"

        if action in {"write_text", "append_text"}:
            text = payload.get("text")
            if not isinstance(text, str):
                raise InvalidOperation(f"{action} requires payload.text")
            encoded = text.encode(encoding)
            after = encoded if action == "write_text" else before + encoded
            return {
                "target": str(target),
                "mode": action,
                "encoding": encoding,
                "before_exists": before_exists,
                "before_b64": base64.b64encode(before).decode("ascii"),
                "before_sha256": sha256_bytes(before) if before_exists else None,
                "before_size": len(before),
                "expected_after_sha256": sha256_bytes(after),
                "expected_after_size": len(after),
                "after_b64": base64.b64encode(after).decode("ascii"),
            }

        if action == "compensate":
            original_id = payload["original_operation_id"]
            with self._db() as con:
                original = con.execute(
                    "SELECT state, plan_json, receipt_json FROM operations WHERE operation_id=?",
                    (original_id,),
                ).fetchone()
            if not original or not original["plan_json"]:
                raise InvalidOperation("original operation is not compensable")
            if original["state"] != "SUCCEEDED":
                raise InvalidOperation("only SUCCEEDED operations may be compensated")
            original_plan = json.loads(original["plan_json"])
            before = base64.b64decode(original_plan["before_b64"])
            return {
                "target": original_plan["target"],
                "mode": "compensate",
                "original_operation_id": original_id,
                "restore_exists": bool(original_plan["before_exists"]),
                "restore_b64": original_plan["before_b64"],
                "expected_after_sha256": sha256_bytes(before) if original_plan["before_exists"] else None,
                "expected_after_size": len(before) if original_plan["before_exists"] else 0,
            }

        raise InvalidOperation("unsupported mutation action")

    def _atomic_write(self, target: Path, data: bytes) -> None:
        target.parent.mkdir(parents=True, exist_ok=True)
        fd, raw_tmp = tempfile.mkstemp(prefix=".amf-", dir=str(target.parent))
        tmp = Path(raw_tmp)
        try:
            with os.fdopen(fd, "wb") as fh:
                fh.write(data)
                fh.flush()
                os.fsync(fh.fileno())
            os.replace(tmp, target)
        finally:
            if tmp.exists():
                tmp.unlink(missing_ok=True)

    def _apply_plan(self, plan: dict[str, Any]) -> str | None:
        target = Path(plan["target"])
        if plan["mode"] in {"write_text", "append_text"}:
            after = base64.b64decode(plan["after_b64"])
            self._atomic_write(target, after)
            return sha256_bytes(after)

        if plan["mode"] == "compensate":
            if plan["restore_exists"]:
                before = base64.b64decode(plan["restore_b64"])
                self._atomic_write(target, before)
                return sha256_bytes(before)
            if target.exists():
                target.unlink()
            return None

        raise InvalidOperation("unsupported plan")

    def _reconcile_running(
        self,
        con: sqlite3.Connection,
        op: dict[str, Any],
        row: sqlite3.Row,
    ) -> dict[str, Any]:
        plan = _json_or_none(row["plan_json"])
        if not plan:
            receipt = self._receipt(
                op, "DLQ", row["policy_decision"],
                evidence=["RUNNING operation has no durable effect plan"],
            )
            self._persist_terminal(con, op, receipt)
            return receipt

        target = Path(plan["target"])
        if plan["mode"] == "compensate" and not plan["restore_exists"]:
            matched = not target.exists()
            digest = None
        elif target.is_file():
            current = target.read_bytes()
            matched = (
                len(current) == plan["expected_after_size"]
                and sha256_bytes(current) == plan["expected_after_sha256"]
            )
            digest = sha256_bytes(current)
        else:
            matched = False
            digest = None

        if not matched:
            receipt = self._receipt(
                op, "DLQ", row["policy_decision"],
                effect_digest=digest,
                evidence=[
                    "effect truth ambiguous after restart",
                    str(target),
                    "blind replay forbidden",
                ],
            )
            self._persist_terminal(con, op, receipt, effect_digest=digest)
            return receipt

        state = "COMPENSATED" if plan["mode"] == "compensate" else "SUCCEEDED"
        compensation_ref = (
            plan.get("original_operation_id") if plan["mode"] == "compensate" else None
        )
        receipt = self._receipt(
            op,
            state,
            row["policy_decision"],
            effect_digest=digest,
            evidence=["postcondition reconciled after restart", str(target)],
            compensation_ref=compensation_ref,
            reconciled=True,
        )
        self._persist_terminal(
            con, op, receipt,
            effect_digest=digest,
            compensation_ref=compensation_ref,
        )
        if plan["mode"] == "compensate":
            self._link_compensation(con, plan["original_operation_id"], op["operation_id"])
        return receipt

    def _link_compensation(
        self,
        con: sqlite3.Connection,
        original_id: str,
        compensation_id: str,
    ) -> None:
        row = con.execute(
            "SELECT receipt_json FROM operations WHERE operation_id=?",
            (original_id,),
        ).fetchone()
        if not row or not row["receipt_json"]:
            return
        receipt = json.loads(row["receipt_json"])
        receipt["compensation_ref"] = compensation_id
        con.execute(
            "UPDATE operations SET compensation_ref=?, receipt_json=? WHERE operation_id=?",
            (compensation_id, canonical_json(receipt), original_id),
        )
        self._event(
            con,
            original_id,
            "COMPENSATION_LINK",
            {"compensation_operation_id": compensation_id},
        )

    def execute(self, operation: dict[str, Any]) -> dict[str, Any]:
        self._validate_operation(operation)
        op = operation
        op_id = op["operation_id"]

        with self._lock:
            with self._db() as con:
                existing = con.execute(
                    "SELECT * FROM operations WHERE operation_id=?",
                    (op_id,),
                ).fetchone()

                if existing:
                    if existing["fingerprint"] != op["fingerprint"]:
                        self._event(
                            con,
                            op_id,
                            "FINGERPRINT_CONFLICT",
                            {
                                "stored": existing["fingerprint"],
                                "incoming": op["fingerprint"],
                            },
                        )
                        con.commit()
                        raise OperationConflict(op_id)

                    if existing["state"] == "RUNNING":
                        return self._reconcile_running(con, op, existing)

                    if existing["state"] in TERMINAL_STATES and existing["receipt_json"]:
                        receipt = json.loads(existing["receipt_json"])
                        receipt["replayed"] = True
                        return receipt

                target = self._target_for(op)
                decision, reason = self.evaluate_policy(op, target)

                if not existing:
                    con.execute(
                        """
                        INSERT INTO operations(
                            operation_id, fingerprint, capability, capability_version,
                            action, state, policy_decision, policy_version,
                            request_json, claimed_at
                        ) VALUES(?,?,?,?,?,?,?,?,?,?)
                        """,
                        (
                            op_id,
                            op["fingerprint"],
                            op["capability"],
                            op["capability_version"],
                            op["action"],
                            "CLAIMED",
                            decision,
                            POLICY_VERSION,
                            canonical_json(op),
                            now_iso(),
                        ),
                    )
                    self._event(
                        con,
                        op_id,
                        "CLAIMED",
                        {"policy_decision": decision, "reason": reason},
                    )

                if decision != "ALLOW":
                    receipt = self._receipt(
                        op,
                        "DENIED",
                        decision,
                        evidence=[reason, str(target)],
                    )
                    self._persist_terminal(con, op, receipt)
                    return receipt

                ok, pre_reason = self._precondition_ok(op, target)
                if not ok:
                    receipt = self._receipt(
                        op,
                        "FAILED",
                        decision,
                        evidence=[pre_reason, str(target)],
                    )
                    self._persist_terminal(con, op, receipt)
                    return receipt

                if op["capability"] == "machine.fs.read":
                    data = target.read_bytes()
                    encoding = (op.get("payload") or {}).get("encoding") or "utf-8"
                    receipt = self._receipt(
                        op,
                        "SUCCEEDED",
                        decision,
                        effect_digest=sha256_bytes(data),
                        evidence=[str(target), "read-only capability"],
                        result={"text": data.decode(encoding), "bytes": len(data)},
                    )
                    self._persist_terminal(
                        con,
                        op,
                        receipt,
                        effect_digest=receipt["effect_digest"],
                    )
                    return receipt

                plan = self._make_plan(op, target)
                con.execute(
                    """
                    UPDATE operations
                    SET state='RUNNING', plan_json=?, started_at=?
                    WHERE operation_id=?
                    """,
                    (canonical_json(plan), now_iso(), op_id),
                )
                self._event(
                    con,
                    op_id,
                    "EFFECT_PLAN",
                    {
                        "target": plan["target"],
                        "mode": plan["mode"],
                        "expected_after_sha256": plan.get("expected_after_sha256"),
                        "expected_after_size": plan.get("expected_after_size"),
                    },
                )
                con.commit()

            digest = self._apply_plan(plan)

            if os.environ.get("AMF_M0_CRASH_AFTER_EFFECT_OPERATION_ID") == op_id:
                os._exit(86)

            state = "COMPENSATED" if plan["mode"] == "compensate" else "SUCCEEDED"
            compensation_ref = (
                plan.get("original_operation_id") if plan["mode"] == "compensate" else None
            )
            receipt = self._receipt(
                op,
                state,
                "ALLOW",
                effect_digest=digest,
                evidence=[
                    str(Path(plan["target"])),
                    "postcondition hash/absence observed after effect",
                ],
                compensation_ref=compensation_ref,
            )
            with self._db() as con:
                self._persist_terminal(
                    con,
                    op,
                    receipt,
                    effect_digest=digest,
                    compensation_ref=compensation_ref,
                )
                if plan["mode"] == "compensate":
                    self._link_compensation(
                        con,
                        plan["original_operation_id"],
                        op["operation_id"],
                    )
            return receipt

    def health(self) -> dict[str, Any]:
        return {
            "schema": HEALTH_SCHEMA,
            "daemon": "UP",
            "worker": "NOT_REQUIRED",
            "transport": "LOCAL",
            "capabilities": {
                key: value["health"] for key, value in CAPABILITIES.items()
            },
            "aggregate": "ONLINE",
            "profile": "M0_LOCAL_FS",
            "allowed_root": str(self.allowed_root),
            "policy_version": POLICY_VERSION,
        }


class AMFHTTPServer(ThreadingHTTPServer):
    daemon_threads = True

    def __init__(self, server_address: tuple[str, int], engine: AMFEngine):
        host, _ = server_address
        if host not in {"127.0.0.1", "::1", "localhost"}:
            raise ValueError("M0 daemon may bind only to loopback")
        super().__init__(server_address, AMFHandler)
        self.engine = engine


class AMFHandler(BaseHTTPRequestHandler):
    server: AMFHTTPServer

    def log_message(self, fmt: str, *args: Any) -> None:
        sys.stderr.write("[amf-m0] " + (fmt % args) + "\n")

    def _send(self, status: int, payload: Any) -> None:
        body = canonical_json(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _read_json(self) -> dict[str, Any]:
        length = int(self.headers.get("Content-Length", "0"))
        if length <= 0 or length > 1024 * 1024:
            raise InvalidOperation("invalid request body length")
        raw = self.rfile.read(length)
        value = json.loads(raw.decode("utf-8"))
        if not isinstance(value, dict):
            raise InvalidOperation("request JSON must be an object")
        return value

    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        if parsed.path == "/health":
            self._send(200, self.server.engine.health())
            return
        if parsed.path == "/capabilities":
            self._send(200, {"capabilities": list(CAPABILITIES.values())})
            return
        prefix = "/receipts/"
        if parsed.path.startswith(prefix):
            op_id = unquote(parsed.path[len(prefix):])
            try:
                self._send(200, self.server.engine.get_receipt(op_id))
            except AMFError as exc:
                self._send(exc.status, {"error": exc.code, "detail": str(exc)})
            return
        self._send(404, {"error": "NOT_FOUND"})

    def do_POST(self) -> None:
        parsed = urlparse(self.path)
        if parsed.path != "/operations":
            self._send(404, {"error": "NOT_FOUND"})
            return
        try:
            operation = self._read_json()
            receipt = self.server.engine.execute(operation)
            status = 403 if receipt["state"] == "DENIED" else 200
            self._send(status, receipt)
        except json.JSONDecodeError as exc:
            self._send(400, {"error": "INVALID_JSON", "detail": str(exc)})
        except AMFError as exc:
            self._send(exc.status, {"error": exc.code, "detail": str(exc)})
        except Exception as exc:
            self._send(500, {"error": "INTERNAL_ERROR", "detail": str(exc)})


def make_operation(
    operation_id: str,
    capability: str,
    action: str,
    *,
    scope: str,
    risk_class: str,
    payload: dict[str, Any],
    precondition: dict[str, Any] | None = None,
    replay: str = "return_receipt",
) -> dict[str, Any]:
    op = {
        "schema": OP_SCHEMA,
        "operation_id": operation_id,
        "capability": capability,
        "capability_version": CAPABILITIES[capability]["version"],
        "action": action,
        "authority": {
            "risk_class": risk_class,
            "scopes": [scope],
            "approval_ref": None,
        },
        "fingerprint": "",
        "precondition": precondition or {},
        "replay": replay,
        "payload": payload,
    }
    op["fingerprint"] = semantic_fingerprint(op)
    return op


def serve(args: argparse.Namespace) -> int:
    engine = AMFEngine(args.db, args.allowed_root)
    server = AMFHTTPServer(("127.0.0.1", args.port), engine)
    host, port = server.server_address[:2]
    print(
        canonical_json(
            {
                "schema": "aspace.machine.daemon-start.v1",
                "host": host,
                "port": port,
                "db": str(engine.db_path),
                "allowed_root": str(engine.allowed_root),
                "health": engine.health(),
            }
        ),
        flush=True,
    )
    server.serve_forever()
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="A'Space Machine Fabric M0")
    sub = ap.add_subparsers(dest="command", required=True)

    sp = sub.add_parser("serve")
    sp.add_argument("--db", required=True)
    sp.add_argument("--allowed-root", required=True)
    sp.add_argument("--port", type=int, default=0)
    sp.set_defaults(func=serve)

    args = ap.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())

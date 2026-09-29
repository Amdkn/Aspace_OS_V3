#!/usr/bin/env python3
"""Generate durable acceptance evidence for A'Space Machine Fabric M0."""

from __future__ import annotations

import argparse
import json
import os
import platform
import socket
import sqlite3
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen

import amf_m0 as amf


def ms(start: float) -> float:
    return round((time.perf_counter() - start) * 1000, 3)


def free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", 0))
        return sock.getsockname()[1]


def http_json(method: str, url: str, payload=None, timeout: float = 5.0):
    data = None if payload is None else json.dumps(payload).encode("utf-8")
    req = Request(url, data=data, method=method)
    if data is not None:
        req.add_header("Content-Type", "application/json")
    try:
        with urlopen(req, timeout=timeout) as resp:
            return resp.status, json.loads(resp.read().decode("utf-8"))
    except HTTPError as exc:
        body = json.loads(exc.read().decode("utf-8"))
        return exc.code, body


def wait_health(base_url: str, attempts: int = 60):
    last = None
    for _ in range(attempts):
        try:
            status, body = http_json("GET", base_url + "/health", timeout=0.25)
            if status == 200:
                return body
            last = body
        except Exception as exc:
            last = str(exc)
        time.sleep(0.05)
    raise RuntimeError(f"daemon did not become healthy: {last}")


def row_snapshot(db: Path, operation_id: str):
    con = sqlite3.connect(db)
    con.row_factory = sqlite3.Row
    try:
        row = con.execute(
            "SELECT * FROM operations WHERE operation_id=?",
            (operation_id,),
        ).fetchone()
    finally:
        con.close()
    if not row:
        return None
    data = dict(row)
    plan = json.loads(data["plan_json"]) if data.get("plan_json") else None
    return {
        "operation_id": data["operation_id"],
        "fingerprint": data["fingerprint"],
        "capability": data["capability"],
        "action": data["action"],
        "state": data["state"],
        "policy_decision": data["policy_decision"],
        "policy_version": data["policy_version"],
        "effect_digest": data["effect_digest"],
        "has_receipt": bool(data["receipt_json"]),
        "claimed_at": data["claimed_at"],
        "started_at": data["started_at"],
        "finished_at": data["finished_at"],
        "plan": (
            {
                "mode": plan.get("mode"),
                "target_name": Path(plan.get("target", "")).name,
                "expected_after_sha256": plan.get("expected_after_sha256"),
                "expected_after_size": plan.get("expected_after_size"),
            }
            if plan
            else None
        ),
    }


def event_count(db: Path, operation_id: str, kind: str) -> int:
    con = sqlite3.connect(db)
    try:
        return con.execute(
            "SELECT count(*) FROM events WHERE operation_id=? AND kind=?",
            (operation_id, kind),
        ).fetchone()[0]
    finally:
        con.close()


def operation(
    engine: amf.AMFEngine,
    operation_id: str,
    capability: str,
    action: str,
    payload: dict,
    *,
    precondition=None,
    risk_class=None,
):
    return amf.make_operation(
        operation_id,
        capability,
        action,
        scope=engine.scope,
        risk_class=risk_class or (
            "read" if capability == "machine.fs.read" else "reversible_write"
        ),
        payload=payload,
        precondition=precondition or {},
    )


def start_daemon(module_path: Path, db: Path, root: Path, port: int, env: dict):
    proc = subprocess.Popen(
        [
            sys.executable,
            str(module_path),
            "serve",
            "--db",
            str(db),
            "--allowed-root",
            str(root),
            "--port",
            str(port),
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        env=env,
    )
    startup = proc.stdout.readline().strip()
    if not startup:
        stderr = proc.stderr.read()
        raise RuntimeError(f"daemon did not emit startup receipt: {stderr}")
    return proc, json.loads(startup)


def close_proc(proc: subprocess.Popen, terminate: bool = False):
    if terminate and proc.poll() is None:
        proc.terminate()
        try:
            proc.wait(timeout=3)
        except subprocess.TimeoutExpired:
            proc.kill()
            proc.wait(timeout=3)
    if proc.stdout:
        proc.stdout.close()
    if proc.stderr:
        proc.stderr.close()


def run_evidence(out_path: Path) -> dict:
    module_path = Path(__file__).with_name("amf_m0.py")
    started_at = amf.now_iso()
    metrics = {}
    checks = {}

    with tempfile.TemporaryDirectory(prefix="amf-m0-evidence-") as td:
        base = Path(td)
        root = base / "allowed"
        root.mkdir()
        db = base / "amf.sqlite3"
        engine = amf.AMFEngine(db, root)
        port = free_port()
        base_url = f"http://127.0.0.1:{port}"

        crash_id = "amf-m0-crash-replay-0001"
        target = root / "crash-record.txt"
        crash_op = operation(
            engine,
            crash_id,
            "machine.fs.write",
            "append_text",
            {"path": str(target), "text": "only-once\n"},
            precondition={"exists": False},
        )

        env = os.environ.copy()
        env["AMF_M0_CRASH_AFTER_EFFECT_OPERATION_ID"] = crash_id
        proc, startup_1 = start_daemon(module_path, db, root, port, env)
        try:
            t0 = time.perf_counter()
            health_1 = wait_health(base_url)
            metrics["health_ms"] = ms(t0)

            t0 = time.perf_counter()
            crash_transport_error = None
            try:
                http_json("POST", base_url + "/operations", crash_op, timeout=5)
            except Exception as exc:
                crash_transport_error = type(exc).__name__
            metrics["crash_request_ms"] = ms(t0)

            proc.wait(timeout=5)
            checks["forced_crash_exit_code"] = proc.returncode
            checks["crash_transport_error"] = crash_transport_error
            checks["effect_count_after_crash"] = target.read_text().count("only-once")
            ledger_before_restart = row_snapshot(db, crash_id)
        finally:
            if proc.poll() is None:
                proc.kill()
                proc.wait(timeout=3)
            close_proc(proc)

        proc2, startup_2 = start_daemon(module_path, db, root, port, os.environ.copy())
        try:
            wait_health(base_url)

            t0 = time.perf_counter()
            status, reconciled = http_json("POST", base_url + "/operations", crash_op)
            metrics["restart_reconcile_ms"] = ms(t0)
            checks["restart_status"] = status
            checks["reconciled_after_restart"] = reconciled.get(
                "reconciled_after_restart", False
            )
            checks["effect_count_after_reconcile"] = target.read_text().count("only-once")
            ledger_after_restart = row_snapshot(db, crash_id)

            t0 = time.perf_counter()
            status, replay = http_json("POST", base_url + "/operations", crash_op)
            metrics["terminal_replay_ms"] = ms(t0)
            checks["terminal_replay_status"] = status
            checks["terminal_replay_flag"] = replay.get("replayed", False)
            checks["effect_count_after_terminal_replay"] = target.read_text().count(
                "only-once"
            )

            conflict = operation(
                engine,
                crash_id,
                "machine.fs.write",
                "append_text",
                {"path": str(target), "text": "DIFFERENT\n"},
                precondition={"exists": False},
            )
            t0 = time.perf_counter()
            conflict_status, conflict_body = http_json(
                "POST", base_url + "/operations", conflict
            )
            metrics["fingerprint_conflict_ms"] = ms(t0)
            checks["fingerprint_conflict_status"] = conflict_status
            checks["fingerprint_conflict_error"] = conflict_body.get("error")
            checks["fingerprint_conflict_events"] = event_count(
                db, crash_id, "FINGERPRINT_CONFLICT"
            )

            outside = base / "outside.txt"
            denial = operation(
                engine,
                "amf-deny-path-0001",
                "machine.fs.write",
                "write_text",
                {"path": str(root / ".." / "outside.txt"), "text": "escape"},
            )
            t0 = time.perf_counter()
            denial_status, denial_receipt = http_json(
                "POST", base_url + "/operations", denial
            )
            metrics["policy_denial_ms"] = ms(t0)
            checks["out_of_scope_status"] = denial_status
            checks["out_of_scope_receipt_state"] = denial_receipt.get("state")
            checks["out_of_scope_policy"] = (
                denial_receipt.get("policy") or {}
            ).get("decision")
            checks["outside_file_exists"] = outside.exists()

            shell_shape = operation(
                engine,
                "amf-deny-shell-001",
                "machine.fs.write",
                "write_text",
                {"path": "safe.txt", "text": "safe"},
            )
            shell_shape["payload"]["shell"] = "echo bypass"
            shell_shape["fingerprint"] = amf.semantic_fingerprint(shell_shape)
            shell_status, shell_body = http_json(
                "POST", base_url + "/operations", shell_shape
            )
            checks["shell_shape_status"] = shell_status
            checks["shell_shape_error"] = shell_body.get("error")

            comp_target = root / "compensate.txt"
            create_op = operation(
                engine,
                "amf-comp-source-0001",
                "machine.fs.write",
                "write_text",
                {"path": str(comp_target), "text": "created"},
                precondition={"exists": False},
            )
            _, create_receipt = http_json(
                "POST", base_url + "/operations", create_op
            )
            comp_op = operation(
                engine,
                "amf-compensate-0001",
                "machine.fs.write",
                "compensate",
                {"original_operation_id": create_op["operation_id"]},
            )
            t0 = time.perf_counter()
            comp_status, comp_receipt = http_json(
                "POST", base_url + "/operations", comp_op
            )
            metrics["compensation_ms"] = ms(t0)
            _, original_after_comp = http_json(
                "GET",
                base_url + "/receipts/" + create_op["operation_id"],
            )
            checks["compensation_status"] = comp_status
            checks["compensation_state"] = comp_receipt.get("state")
            checks["compensation_receipt_operation_id"] = comp_receipt.get(
                "operation_id"
            )
            checks["compensation_ref_on_original"] = original_after_comp.get(
                "compensation_ref"
            )
            checks["compensated_file_exists"] = comp_target.exists()

            health_2 = wait_health(base_url)
        finally:
            close_proc(proc2, terminate=True)

        expected = {
            "forced_crash_exit_code": 86,
            "effect_count_after_crash": 1,
            "restart_status": 200,
            "reconciled_after_restart": True,
            "effect_count_after_reconcile": 1,
            "terminal_replay_status": 200,
            "terminal_replay_flag": True,
            "effect_count_after_terminal_replay": 1,
            "fingerprint_conflict_status": 409,
            "fingerprint_conflict_error": "OPERATION_ID_FINGERPRINT_CONFLICT",
            "fingerprint_conflict_events": 1,
            "out_of_scope_status": 403,
            "out_of_scope_receipt_state": "DENIED",
            "out_of_scope_policy": "DENY",
            "outside_file_exists": False,
            "shell_shape_status": 400,
            "shell_shape_error": "INVALID_OPERATION",
            "compensation_status": 200,
            "compensation_state": "COMPENSATED",
            "compensation_receipt_operation_id": "amf-compensate-0001",
            "compensation_ref_on_original": "amf-compensate-0001",
            "compensated_file_exists": False,
        }
        assertions = {
            key: {"actual": checks.get(key), "expected": value, "pass": checks.get(key) == value}
            for key, value in expected.items()
        }
        passed = all(item["pass"] for item in assertions.values())

        evidence = {
            "schema": "aspace.machine.m0-evidence.v1",
            "mission": "#194",
            "design": "#196 / PR #201",
            "build": "#197",
            "started_at": started_at,
            "finished_at": amf.now_iso(),
            "result": "PASS" if passed else "FAIL",
            "invariant": (
                "typed capability -> policy -> operation_id -> precondition -> "
                "effect -> durable receipt -> replay/compensation"
            ),
            "fundamental_canary": (
                "mutation -> crash/restart -> replay same operation_id -> "
                "zero duplicate mutation"
            ),
            "environment": {
                "platform": platform.platform(),
                "python": sys.version.split()[0],
                "transport": "127.0.0.1 loopback",
                "policy_version": amf.POLICY_VERSION,
                "adapter": amf.ADAPTER_ID,
            },
            "startup_before_crash": startup_1,
            "health_before_crash": health_1,
            "ledger_before_restart": ledger_before_restart,
            "startup_after_restart": startup_2,
            "health_after_restart": health_2,
            "ledger_after_restart": ledger_after_restart,
            "reconciled_receipt": reconciled,
            "terminal_replay_receipt": replay,
            "checks": checks,
            "assertions": assertions,
            "metrics_ms": metrics,
            "limitations": [
                "M0 only: filesystem read/write, receipt ledger, policy, recovery, health.",
                "No Windows service installation yet; daemon is process-hosted for the M0 proof.",
                "No user-session worker, Chrome Native Messaging, UIA, process control, or remote transport.",
                "SQLite plan stores reversible before-state for bounded test-root writes; production retention/encryption policy remains a later design concern.",
            ],
            "rollback": (
                "Stop the loopback process, delete the M0 SQLite ledger/test root, "
                "and revert the Ryan M0 commits. No public listener or machine-wide "
                "service registration is installed by M0."
            ),
            "return_to": [
                "Yaz/SENSE: duplicate prevention, latency, denial and health review",
                "Graham/REMEMBER: receipt/provenance and policy/manifest version review",
                "Rory/COHERE: no false online, no authority drift, no double effect",
                "Nardole/DISPATCH: route next cell only after independent review",
                "Clara/DESIGN: CapabilityNeed only if M0 evidence reveals a contract gap",
            ],
        }

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(
        json.dumps(evidence, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return evidence


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    evidence = run_evidence(args.out)
    print(
        json.dumps(
            {
                "result": evidence["result"],
                "out": str(args.out),
                "checks": len(evidence["assertions"]),
                "metrics_ms": evidence["metrics_ms"],
            },
            indent=2,
        )
    )
    return 0 if evidence["result"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())

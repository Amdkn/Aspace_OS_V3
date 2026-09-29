#!/usr/bin/env python3
"""A'Space Harness Runtime P1-P4 substrate.

Implements the Clara #208 contract without creating a scheduler:
P1 runtime identity, P2 isolated/idempotent prepare, P3 durable process-tree
lifecycle, P4 generic harness adapter + typed receipts.

ChatGPT session state is never an input to runtime continuation.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import shutil
import signal
import sqlite3
import subprocess
import sys
import time
import uuid
from pathlib import Path
from typing import Any

CAPABILITY_ID = "machine.harness.runtime"
CAPABILITY_VERSION = "0.1.0"
POLICY_VERSION = "amf-policy-v1"
ADAPTER_VERSION = "0.1.0"

RUNTIME_SCHEMA = "aspace.runtime-fingerprint.v1"
PREPARE_SCHEMA = "aspace.runtime-prepare-receipt.v1"
EXEC_RECEIPT_SCHEMA = "aspace.harness-execution-receipt.v1"
RELEASE_SCHEMA = "aspace.capability-release.v1"

EVENT_KINDS = {
    "capability_release",
    "dispatch_envelope",
    "harness_execution_requested",
    "runtime_prepared",
    "harness_execution_started",
    "harness_observed",
    "harness_execution_receipt",
    "rory_reconcile_decision",
    "continuation_routed",
    "continuation_resolved",
}


class HarnessRuntimeError(RuntimeError):
    pass


def now_iso() -> str:
    import datetime
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def hash_paths(paths: list[str | Path]) -> str:
    rows: list[dict[str, Any]] = []
    for raw in sorted(str(Path(p).resolve()) for p in paths):
        path = Path(raw)
        if not path.exists():
            rows.append({"path": raw, "state": "missing"})
        elif path.is_file():
            rows.append({
                "path": raw,
                "state": "file",
                "size": path.stat().st_size,
                "sha256": sha256_file(path),
            })
        else:
            children = []
            for child in sorted(x for x in path.rglob("*") if x.is_file()):
                rel = child.relative_to(path).as_posix()
                children.append({
                    "rel": rel,
                    "size": child.stat().st_size,
                    "sha256": sha256_file(child),
                })
            rows.append({"path": raw, "state": "dir", "children": children})
    return "sha256:" + sha256_text(canonical_json(rows))


def hash_profile(values: dict[str, str | None]) -> str:
    normalized = {k: values.get(k) or "" for k in sorted(values)}
    return "sha256:" + sha256_text(canonical_json(normalized))


def safe_resolve(path: str | Path) -> Path:
    return Path(path).expanduser().resolve(strict=False)


def inside(root: Path, candidate: Path) -> bool:
    try:
        candidate.relative_to(root)
        return True
    except ValueError:
        return False


def process_snapshot_windows() -> dict[int, dict[str, Any]]:
    script = (
        "$ErrorActionPreference='SilentlyContinue'; "
        "@(Get-CimInstance Win32_Process | "
        "Select-Object ProcessId,ParentProcessId,Name,CommandLine | "
        "ConvertTo-Json -Compress)"
    )
    cp = subprocess.run(
        ["powershell", "-NoProfile", "-Command", script],
        text=True,
        capture_output=True,
        timeout=15,
        check=False,
    )
    if cp.returncode != 0 or not cp.stdout.strip():
        return {}
    try:
        data = json.loads(cp.stdout)
    except json.JSONDecodeError:
        return {}
    if isinstance(data, dict):
        data = [data]
    result = {}
    for row in data:
        try:
            pid = int(row.get("ProcessId"))
            result[pid] = {
                "pid": pid,
                "ppid": int(row.get("ParentProcessId") or 0),
                "name": row.get("Name"),
                "command_line": row.get("CommandLine"),
            }
        except (TypeError, ValueError):
            continue
    return result


def process_snapshot_posix() -> dict[int, dict[str, Any]]:
    cp = subprocess.run(
        ["ps", "-eo", "pid=,ppid=,comm=,args="],
        text=True,
        capture_output=True,
        timeout=10,
        check=False,
    )
    result = {}
    for line in cp.stdout.splitlines():
        parts = line.strip().split(None, 3)
        if len(parts) < 3:
            continue
        try:
            pid, ppid = int(parts[0]), int(parts[1])
        except ValueError:
            continue
        result[pid] = {
            "pid": pid,
            "ppid": ppid,
            "name": parts[2],
            "command_line": parts[3] if len(parts) > 3 else parts[2],
        }
    return result


def process_snapshot() -> dict[int, dict[str, Any]]:
    return process_snapshot_windows() if os.name == "nt" else process_snapshot_posix()


def descendants(snapshot: dict[int, dict[str, Any]], roots: set[int]) -> set[int]:
    known = set(roots)
    changed = True
    while changed:
        changed = False
        for pid, row in snapshot.items():
            if pid not in known and row["ppid"] in known:
                known.add(pid)
                changed = True
    return known


class RuntimeStore:
    def __init__(self, db_path: str | Path):
        self.db_path = safe_resolve(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._init()

    def _connect(self) -> sqlite3.Connection:
        con = sqlite3.connect(self.db_path, timeout=10)
        con.row_factory = sqlite3.Row
        con.execute("PRAGMA journal_mode=WAL")
        con.execute("PRAGMA synchronous=FULL")
        con.execute("PRAGMA busy_timeout=5000")
        return con

    def _init(self) -> None:
        con = self._connect()
        try:
            con.executescript(
                """
                CREATE TABLE IF NOT EXISTS preparations (
                    prepare_id TEXT PRIMARY KEY,
                    spec_hash TEXT NOT NULL,
                    state TEXT NOT NULL,
                    receipt_json TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL
                );
                CREATE TABLE IF NOT EXISTS executions (
                    execution_id TEXT PRIMARY KEY,
                    request_json TEXT NOT NULL,
                    adapter TEXT NOT NULL,
                    runtime_root TEXT NOT NULL,
                    cwd TEXT NOT NULL,
                    command_json TEXT NOT NULL,
                    process_group_ref TEXT NOT NULL,
                    root_pid INTEGER,
                    known_pids_json TEXT NOT NULL,
                    stdout_ref TEXT NOT NULL,
                    stderr_ref TEXT NOT NULL,
                    status_ref TEXT NOT NULL,
                    launched_at TEXT NOT NULL,
                    last_observed_at TEXT,
                    cancelled_at TEXT,
                    receipt_json TEXT
                );
                CREATE TABLE IF NOT EXISTS observations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    execution_id TEXT NOT NULL,
                    observation_json TEXT NOT NULL,
                    at TEXT NOT NULL
                );
                """
            )
            con.commit()
        finally:
            con.close()

    def get_prepare(self, prepare_id: str) -> dict[str, Any] | None:
        con = self._connect()
        try:
            row = con.execute(
                "SELECT receipt_json FROM preparations WHERE prepare_id=?",
                (prepare_id,),
            ).fetchone()
            return json.loads(row["receipt_json"]) if row else None
        finally:
            con.close()

    def put_prepare(self, prepare_id: str, spec_hash: str, receipt: dict[str, Any]) -> None:
        con = self._connect()
        try:
            con.execute(
                """
                INSERT INTO preparations(prepare_id,spec_hash,state,receipt_json,created_at,updated_at)
                VALUES(?,?,?,?,?,?)
                ON CONFLICT(prepare_id) DO UPDATE SET
                  state=excluded.state,
                  receipt_json=excluded.receipt_json,
                  updated_at=excluded.updated_at
                """,
                (
                    prepare_id,
                    spec_hash,
                    receipt["state"],
                    canonical_json(receipt),
                    receipt.get("started_at") or now_iso(),
                    now_iso(),
                ),
            )
            con.commit()
        finally:
            con.close()

    def put_execution(self, row: dict[str, Any]) -> None:
        con = self._connect()
        try:
            con.execute(
                """
                INSERT INTO executions(
                  execution_id,request_json,adapter,runtime_root,cwd,command_json,
                  process_group_ref,root_pid,known_pids_json,stdout_ref,stderr_ref,
                  status_ref,launched_at,last_observed_at,cancelled_at,receipt_json
                ) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                """,
                (
                    row["execution_id"], canonical_json(row["request"]), row["adapter"],
                    row["runtime_root"], row["cwd"], canonical_json(row["command"]),
                    row["process_group_ref"], row["root_pid"],
                    canonical_json(row["known_pids"]), row["stdout_ref"], row["stderr_ref"],
                    row["status_ref"], row["launched_at"], None, None, None,
                ),
            )
            con.commit()
        finally:
            con.close()

    def get_execution(self, execution_id: str) -> dict[str, Any]:
        con = self._connect()
        try:
            row = con.execute(
                "SELECT * FROM executions WHERE execution_id=?",
                (execution_id,),
            ).fetchone()
            if not row:
                raise HarnessRuntimeError(f"unknown execution_id: {execution_id}")
            data = dict(row)
            data["request"] = json.loads(data.pop("request_json"))
            data["command"] = json.loads(data.pop("command_json"))
            data["known_pids"] = json.loads(data.pop("known_pids_json"))
            data["receipt"] = json.loads(data["receipt_json"]) if data["receipt_json"] else None
            return data
        finally:
            con.close()

    def update_execution(self, execution_id: str, **values: Any) -> None:
        allowed = {
            "root_pid", "known_pids_json", "last_observed_at",
            "cancelled_at", "receipt_json",
        }
        if not values or set(values) - allowed:
            raise HarnessRuntimeError("invalid execution update")
        con = self._connect()
        try:
            columns = ", ".join(f"{k}=?" for k in values)
            con.execute(
                f"UPDATE executions SET {columns} WHERE execution_id=?",
                (*values.values(), execution_id),
            )
            con.commit()
        finally:
            con.close()

    def add_observation(self, execution_id: str, observation: dict[str, Any]) -> None:
        con = self._connect()
        try:
            con.execute(
                "INSERT INTO observations(execution_id,observation_json,at) VALUES(?,?,?)",
                (execution_id, canonical_json(observation), now_iso()),
            )
            con.commit()
        finally:
            con.close()


class WorkGraphEventSink:
    """Append-only bridge to the existing uc.db event table; never mutates work status."""

    def __init__(self, db_path: str | Path, harness: str = "machine.harness.runtime"):
        self.db_path = safe_resolve(db_path)
        self.harness = harness

    def emit(self, work_id: int, kind: str, payload: dict[str, Any]) -> int:
        if kind not in EVENT_KINDS:
            raise HarnessRuntimeError(f"unsupported WorkGraph event kind: {kind}")
        con = sqlite3.connect(self.db_path, timeout=10)
        try:
            exists = con.execute("SELECT 1 FROM work WHERE id=?", (work_id,)).fetchone()
            if not exists:
                raise HarnessRuntimeError(f"work_id does not exist: {work_id}")
            cur = con.execute(
                "INSERT INTO event(work_id,harness,kind,payload) VALUES(?,?,?,?)",
                (work_id, self.harness, kind, canonical_json(payload)),
            )
            con.commit()
            return int(cur.lastrowid)
        finally:
            con.close()

    def read_chain(self, work_id: int, correlation_id: str) -> list[dict[str, Any]]:
        con = sqlite3.connect(self.db_path, timeout=10)
        con.row_factory = sqlite3.Row
        try:
            rows = con.execute(
                "SELECT id,work_id,harness,kind,payload,at FROM event WHERE work_id=? ORDER BY id",
                (work_id,),
            ).fetchall()
        finally:
            con.close()
        out = []
        for row in rows:
            try:
                payload = json.loads(row["payload"] or "{}")
            except json.JSONDecodeError:
                continue
            if payload.get("correlation_id") == correlation_id:
                item = dict(row)
                item["payload"] = payload
                out.append(item)
        return out


class RuntimeInspector:
    def inspect(
        self,
        *,
        harness: str,
        harness_version: str,
        adapter: str,
        adapter_version: str,
        workspace: str,
        cwd: str | Path,
        runtime: str,
        runtime_root: str | Path | None,
        dependency_refs: list[str | Path],
        authority_scopes: list[str],
        capability_version: str = CAPABILITY_VERSION,
        policy_version: str = POLICY_VERSION,
        provider: str | None = None,
        model: str | None = None,
        worktree: str | None = None,
        credential_profile_ref: str | None = None,
        session_ref: str | None = None,
        process_group_ref: str | None = None,
        timeout_seconds: int | None = None,
        quota_profile: str | None = None,
    ) -> dict[str, Any]:
        path_hash = hash_profile({"PATH": os.environ.get("PATH")})
        proxy_hash = hash_profile({
            k: os.environ.get(k)
            for k in ("HTTP_PROXY", "HTTPS_PROXY", "ALL_PROXY", "NO_PROXY")
        })
        runtime_version = platform.python_version() if runtime == "python" else None
        body = {
            "harness": harness,
            "harness_version": harness_version,
            "adapter": adapter,
            "adapter_version": adapter_version,
            "provider": provider,
            "model": model,
            "workspace": workspace,
            "worktree": worktree,
            "cwd": str(safe_resolve(cwd)),
            "runtime": runtime,
            "runtime_version": runtime_version,
            "runtime_root": str(safe_resolve(runtime_root)) if runtime_root else None,
            "dependency_hash": hash_paths(dependency_refs),
            "path_profile_hash": path_hash,
            "proxy_profile_hash": proxy_hash,
            "credential_profile_ref": credential_profile_ref,
            "session_ref": session_ref,
            "process_group_ref": process_group_ref,
            "timeout_seconds": timeout_seconds,
            "quota_profile": quota_profile,
            "authority_scopes": sorted(set(authority_scopes)),
            "capability_version": capability_version,
            "policy_version": policy_version,
        }
        body["fingerprint"] = "sha256:" + sha256_text(canonical_json(body))
        return body


class RuntimePreparer:
    def __init__(
        self,
        store: RuntimeStore,
        owned_root: str | Path,
        inspector: RuntimeInspector | None = None,
        event_sink: WorkGraphEventSink | None = None,
    ):
        self.store = store
        self.owned_root = safe_resolve(owned_root)
        self.owned_root.mkdir(parents=True, exist_ok=True)
        self.inspector = inspector or RuntimeInspector()
        self.event_sink = event_sink

    def prepare(self, spec: dict[str, Any]) -> dict[str, Any]:
        root = safe_resolve(spec["runtime_root"])
        if not inside(self.owned_root, root):
            raise HarnessRuntimeError("runtime_root outside owned prepare root")
        safe_spec = dict(spec)
        safe_spec.pop("credential_secret", None)
        spec_hash = "sha256:" + sha256_text(canonical_json(safe_spec))
        prepare_id = spec.get("prepare_id") or "prepare:" + spec_hash.split(":", 1)[1][:24]
        prior = self.store.get_prepare(prepare_id)
        if prior and prior["state"] == "SUCCEEDED" and prior["spec_hash"] == spec_hash:
            replay = dict(prior)
            replay["replayed"] = True
            return replay

        started = now_iso()
        dependency_refs = list(spec.get("dependency_refs") or [])
        before = self.inspector.inspect(
            harness=spec["harness"],
            harness_version=spec["harness_version"],
            adapter=spec["adapter"],
            adapter_version=spec.get("adapter_version", ADAPTER_VERSION),
            workspace=spec["workspace"],
            worktree=spec.get("worktree"),
            cwd=spec["cwd"],
            runtime=spec.get("runtime", "python"),
            runtime_root=root if root.exists() else None,
            dependency_refs=dependency_refs,
            authority_scopes=spec["authority_scopes"],
            capability_version=spec.get("capability_version", CAPABILITY_VERSION),
            policy_version=spec.get("policy_version", POLICY_VERSION),
            credential_profile_ref=spec.get("credential_profile_ref"),
            timeout_seconds=spec.get("timeout_seconds"),
            quota_profile=spec.get("quota_profile"),
        )
        changed_refs: list[str] = []
        try:
            root.mkdir(parents=True, exist_ok=True)
            changed_refs.append(str(root))
            marker = root / ".aspace-runtime-owned.json"
            marker.write_text(
                json.dumps(
                    {
                        "prepare_id": prepare_id,
                        "spec_hash": spec_hash,
                        "created_at": started,
                    },
                    indent=2,
                ) + "\n",
                encoding="utf-8",
            )
            changed_refs.append(str(marker))

            if spec.get("create_venv"):
                venv_dir = root / ".venv"
                if not venv_dir.exists():
                    import venv
                    venv.EnvBuilder(with_pip=False, clear=False).create(venv_dir)
                    changed_refs.append(str(venv_dir))

            prepare_command = spec.get("prepare_command")
            if prepare_command:
                if not isinstance(prepare_command, list) or not prepare_command:
                    raise HarnessRuntimeError("prepare_command must be a non-empty argv list")
                env = os.environ.copy()
                env["ASPACE_RUNTIME_ROOT"] = str(root)
                cp = subprocess.run(
                    [str(x) for x in prepare_command],
                    cwd=str(safe_resolve(spec["cwd"])),
                    env=env,
                    text=True,
                    capture_output=True,
                    timeout=int(spec.get("timeout_seconds") or 300),
                    check=False,
                )
                if cp.returncode != 0:
                    raise HarnessRuntimeError(
                        f"prepare command failed rc={cp.returncode}: {cp.stderr[-1000:]}"
                    )

            after = self.inspector.inspect(
                harness=spec["harness"],
                harness_version=spec["harness_version"],
                adapter=spec["adapter"],
                adapter_version=spec.get("adapter_version", ADAPTER_VERSION),
                workspace=spec["workspace"],
                worktree=spec.get("worktree"),
                cwd=spec["cwd"],
                runtime=spec.get("runtime", "python"),
                runtime_root=root,
                dependency_refs=dependency_refs,
                authority_scopes=spec["authority_scopes"],
                capability_version=spec.get("capability_version", CAPABILITY_VERSION),
                policy_version=spec.get("policy_version", POLICY_VERSION),
                credential_profile_ref=spec.get("credential_profile_ref"),
                timeout_seconds=spec.get("timeout_seconds"),
                quota_profile=spec.get("quota_profile"),
            )
            receipt = {
                "schema": PREPARE_SCHEMA,
                "prepare_id": prepare_id,
                "spec_hash": spec_hash,
                "state": "SUCCEEDED",
                "fingerprint_before": before,
                "fingerprint_after": after,
                "changed_refs": changed_refs,
                "dependency_refs": [str(safe_resolve(x)) for x in dependency_refs],
                "cleanup": {
                    "kind": "delete-owned-runtime-root",
                    "runtime_root": str(root),
                },
                "started_at": started,
                "finished_at": now_iso(),
                "replayed": False,
            }
        except Exception as exc:
            receipt = {
                "schema": PREPARE_SCHEMA,
                "prepare_id": prepare_id,
                "spec_hash": spec_hash,
                "state": "FAILED",
                "fingerprint_before": before,
                "fingerprint_after": None,
                "changed_refs": changed_refs,
                "dependency_refs": [str(safe_resolve(x)) for x in dependency_refs],
                "cleanup": {
                    "kind": "delete-owned-runtime-root",
                    "runtime_root": str(root),
                },
                "error": str(exc),
                "started_at": started,
                "finished_at": now_iso(),
                "replayed": False,
            }

        self.store.put_prepare(prepare_id, spec_hash, receipt)
        if self.event_sink and spec.get("work_id") is not None:
            payload = dict(receipt)
            payload["correlation_id"] = spec.get("correlation_id")
            self.event_sink.emit(int(spec["work_id"]), "runtime_prepared", payload)
        return receipt

    def cleanup(self, receipt: dict[str, Any]) -> dict[str, Any]:
        root = safe_resolve(receipt["cleanup"]["runtime_root"])
        if not inside(self.owned_root, root):
            raise HarnessRuntimeError("cleanup root outside owned prepare root")
        if root.exists():
            shutil.rmtree(root)
        return {"state": "COMPENSATED", "removed": str(root), "at": now_iso()}


def _runner_path() -> Path:
    return Path(__file__).with_name("harness_runner.py")


class LocalCLIAdapter:
    """Real local CLI harness adapter; provider-specific adapters wrap this boundary."""

    def __init__(
        self,
        store: RuntimeStore,
        owned_root: str | Path,
        *,
        name: str = "local-cli",
        harness_version: str = "system",
        event_sink: WorkGraphEventSink | None = None,
    ):
        self.store = store
        self.owned_root = safe_resolve(owned_root)
        self.owned_root.mkdir(parents=True, exist_ok=True)
        self.name = name
        self.harness_version = harness_version
        self.inspector = RuntimeInspector()
        self.preparer = RuntimePreparer(store, self.owned_root / "prepared", self.inspector, event_sink)
        self.event_sink = event_sink

    def inspect(self, request: dict[str, Any], execution_id: str | None = None) -> dict[str, Any]:
        process_group_ref = None
        runtime_root = request.get("runtime_root")
        if execution_id:
            row = self.store.get_execution(execution_id)
            process_group_ref = row["process_group_ref"]
            runtime_root = row["runtime_root"]
        return self.inspector.inspect(
            harness=request.get("harness", self.name),
            harness_version=request.get("harness_version", self.harness_version),
            adapter=self.name,
            adapter_version=ADAPTER_VERSION,
            provider=request.get("provider"),
            model=request.get("model"),
            workspace=request["workspace"],
            worktree=request.get("worktree"),
            cwd=request["cwd"],
            runtime=request.get("runtime", "python"),
            runtime_root=runtime_root,
            dependency_refs=request.get("dependency_refs") or [],
            credential_profile_ref=request.get("credential_profile_ref"),
            session_ref=request.get("session_ref"),
            process_group_ref=process_group_ref,
            timeout_seconds=request.get("timeout_seconds"),
            quota_profile=request.get("quota_profile"),
            authority_scopes=request["authority_scopes"],
            capability_version=request.get("capability_version", CAPABILITY_VERSION),
            policy_version=request.get("policy_version", POLICY_VERSION),
        )

    def prepare(self, request: dict[str, Any]) -> dict[str, Any]:
        return self.preparer.prepare(request)

    def launch(self, request: dict[str, Any]) -> dict[str, Any]:
        execution_id = request.get("execution_id") or "hexec-" + uuid.uuid4().hex[:20]
        exec_root = self.owned_root / "executions" / execution_id
        exec_root.mkdir(parents=True, exist_ok=False)
        command = request.get("command")
        if not isinstance(command, list) or not command:
            raise HarnessRuntimeError("launch requires command argv list")
        cwd = safe_resolve(request["cwd"])
        stdout_ref = exec_root / "stdout.log"
        stderr_ref = exec_root / "stderr.log"
        status_ref = exec_root / "status.json"
        request_ref = exec_root / "request.json"
        request_ref.write_text(json.dumps(request, indent=2) + "\n", encoding="utf-8")
        runner_cmd = [
            sys.executable,
            str(_runner_path()),
            "--status", str(status_ref),
            "--cwd", str(cwd),
            "--",
            *[str(x) for x in command],
        ]
        stdout_fh = stdout_ref.open("ab", buffering=0)
        stderr_fh = stderr_ref.open("ab", buffering=0)
        try:
            kwargs: dict[str, Any] = {
                "cwd": str(cwd),
                "stdout": stdout_fh,
                "stderr": stderr_fh,
                "stdin": subprocess.DEVNULL,
                "env": os.environ.copy(),
            }
            if os.name == "nt":
                kwargs["creationflags"] = subprocess.CREATE_NEW_PROCESS_GROUP
            else:
                kwargs["start_new_session"] = True
            proc = subprocess.Popen(runner_cmd, **kwargs)
        finally:
            stdout_fh.close()
            stderr_fh.close()

        process_group_ref = f"pg:{proc.pid}"
        row = {
            "execution_id": execution_id,
            "request": request,
            "adapter": self.name,
            "runtime_root": str(safe_resolve(request.get("runtime_root") or self.owned_root)),
            "cwd": str(cwd),
            "command": command,
            "process_group_ref": process_group_ref,
            "root_pid": proc.pid,
            "known_pids": [proc.pid],
            "stdout_ref": str(stdout_ref),
            "stderr_ref": str(stderr_ref),
            "status_ref": str(status_ref),
            "launched_at": now_iso(),
        }
        self.store.put_execution(row)
        if self.event_sink and request.get("work_id") is not None:
            payload = {
                "execution_id": execution_id,
                "operation_id": execution_id,
                "correlation_id": request.get("correlation_id"),
                "process_group_ref": process_group_ref,
                "root_pid": proc.pid,
            }
            self.event_sink.emit(int(request["work_id"]), "harness_execution_started", payload)
        return {
            "execution_id": execution_id,
            "operation_id": execution_id,
            "process_group_ref": process_group_ref,
            "root_pid": proc.pid,
            "stdout_ref": str(stdout_ref),
            "stderr_ref": str(stderr_ref),
            "status_ref": str(status_ref),
            "accepted": True,
        }

    def resume(self, execution_id: str) -> dict[str, Any]:
        obs = self.observe(execution_id)
        return {
            "execution_id": execution_id,
            "resumed": obs["lifecycle_state"] in {"RUNNING", "WAITING"},
            "observation": obs,
        }

    def observe(self, execution_id: str) -> dict[str, Any]:
        row = self.store.get_execution(execution_id)
        snapshot = process_snapshot()
        known = {int(x) for x in row["known_pids"]}
        root = int(row["root_pid"]) if row["root_pid"] else None
        roots = {root} if root else set()
        live_tree = descendants(snapshot, roots | (known & set(snapshot)))
        known |= live_tree
        live = sorted(pid for pid in known if pid in snapshot)

        status_path = Path(row["status_ref"])
        status = None
        if status_path.exists():
            try:
                status = json.loads(status_path.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                status = None

        if row["cancelled_at"] and not live:
            state = "CANCELLED"
        elif status and status.get("state") == "finished":
            state = "SUCCEEDED" if int(status.get("returncode", 1)) == 0 else "FAILED"
        elif root in snapshot:
            state = "RUNNING"
        elif live:
            state = "UNKNOWN"
        else:
            state = "UNKNOWN"

        desired = self._artifact_refs(row["request"])
        obs = {
            "process_group_ref": row["process_group_ref"],
            "root_process": root,
            "children": [pid for pid in live if pid != root],
            "heartbeat_at": now_iso(),
            "lifecycle_state": state,
            "stdout_ref": row["stdout_ref"],
            "stderr_ref": row["stderr_ref"],
            "artifact_refs": desired,
        }
        self.store.update_execution(
            execution_id,
            known_pids_json=canonical_json(sorted(known)),
            last_observed_at=obs["heartbeat_at"],
        )
        self.store.add_observation(execution_id, obs)
        if self.event_sink and row["request"].get("work_id") is not None:
            payload = dict(obs)
            payload["execution_id"] = execution_id
            payload["correlation_id"] = row["request"].get("correlation_id")
            self.event_sink.emit(int(row["request"]["work_id"]), "harness_observed", payload)
        return obs

    def wait(
        self,
        execution_id: str,
        *,
        timeout_seconds: float,
        poll_seconds: float = 0.2,
        cancel_on_timeout: bool = True,
    ) -> dict[str, Any]:
        deadline = time.monotonic() + timeout_seconds
        last = self.observe(execution_id)
        while last["lifecycle_state"] in {"RUNNING", "WAITING"} and time.monotonic() < deadline:
            time.sleep(poll_seconds)
            last = self.observe(execution_id)
        if last["lifecycle_state"] in {"RUNNING", "WAITING"} and time.monotonic() >= deadline:
            if cancel_on_timeout:
                return self.cancel(execution_id)
        return last

    def _kill_pid(self, pid: int, tree: bool) -> None:
        if os.name == "nt":
            cmd = ["taskkill", "/PID", str(pid), "/F"]
            if tree:
                cmd.insert(3, "/T")
            subprocess.run(cmd, capture_output=True, text=True, check=False)
        else:
            try:
                if tree:
                    os.killpg(pid, signal.SIGKILL)
                else:
                    os.kill(pid, signal.SIGKILL)
            except (ProcessLookupError, PermissionError):
                pass

    def interrupt_root_only(self, execution_id: str) -> dict[str, Any]:
        row = self.store.get_execution(execution_id)
        root = int(row["root_pid"])
        self._kill_pid(root, tree=False)
        time.sleep(0.15)
        return self.observe(execution_id)

    def cancel(self, execution_id: str) -> dict[str, Any]:
        row = self.store.get_execution(execution_id)
        obs = self.observe(execution_id)
        known = set(int(x) for x in row["known_pids"]) | set(obs["children"])
        root = int(row["root_pid"]) if row["root_pid"] else None
        if root:
            self._kill_pid(root, tree=True)
        for pid in sorted(known, reverse=True):
            if pid != root:
                self._kill_pid(pid, tree=True)
        self.store.update_execution(execution_id, cancelled_at=now_iso())
        time.sleep(0.2)
        return self.observe(execution_id)

    def _artifact_refs(self, request: dict[str, Any]) -> list[str]:
        refs = []
        cwd = safe_resolve(request["cwd"])
        for raw in request.get("desired_artifacts") or []:
            candidate = safe_resolve(raw if Path(raw).is_absolute() else cwd / raw)
            if candidate.exists():
                refs.append(str(candidate))
        return refs

    def collect(self, execution_id: str) -> dict[str, Any]:
        row = self.store.get_execution(execution_id)
        artifacts = self._artifact_refs(row["request"])
        return {
            "execution_id": execution_id,
            "stdout_ref": row["stdout_ref"],
            "stderr_ref": row["stderr_ref"],
            "artifact_refs": artifacts,
            "status_ref": row["status_ref"] if Path(row["status_ref"]).exists() else None,
        }

    def reconcile(self, execution_id: str) -> dict[str, Any]:
        row = self.store.get_execution(execution_id)
        observation = self.observe(execution_id)
        artifacts = self._artifact_refs(row["request"])
        desired = list(row["request"].get("desired_artifacts") or [])
        status_path = Path(row["status_ref"])
        status = None
        if status_path.exists():
            try:
                status = json.loads(status_path.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                pass

        if status and status.get("state") == "finished":
            rc = int(status.get("returncode", 1))
            if rc == 0 and (not desired or len(artifacts) == len(desired)):
                effect_state = "YES"
                retry_safe = False
                recovery_hint = "effect observed; continue to Rory reconciliation"
            elif rc != 0 and not artifacts:
                effect_state = "NO"
                retry_safe = row["request"].get("replay_policy") in {
                    "same-operation", "retry-if-no-effect"
                }
                recovery_hint = "no effect observed; Rory may classify retry safety"
            else:
                effect_state = "UNKNOWN"
                retry_safe = False
                recovery_hint = "partial/ambiguous effect; route Donna before retry"
        else:
            effect_state = "UNKNOWN"
            retry_safe = False
            recovery_hint = "runtime terminal truth unavailable; route Donna before retry"

        fp_request = dict(row["request"])
        fp_request["runtime_root"] = row["runtime_root"]
        fingerprint = self.inspect(fp_request, execution_id)
        receipt = {
            "schema": EXEC_RECEIPT_SCHEMA,
            "receipt_id": "hrec-" + uuid.uuid4().hex[:20],
            "request_id": row["request"]["request_id"],
            "work_id": row["request"]["work_id"],
            "correlation_id": row["request"]["correlation_id"],
            "operation_id": execution_id,
            "runtime_fingerprint": fingerprint,
            "observation": observation,
            "effect_state": effect_state,
            "task_accepted": True,
            "resumable": bool(observation["children"]) and effect_state == "UNKNOWN",
            "retry_safe": retry_safe,
            "artifact_refs": artifacts,
            "policy_decision_ref": row["request"].get("policy_decision_ref"),
            "recovery_hint": recovery_hint,
            "finished_at": now_iso(),
        }
        self.store.update_execution(execution_id, receipt_json=canonical_json(receipt))
        if self.event_sink:
            self.event_sink.emit(
                int(row["request"]["work_id"]),
                "harness_execution_receipt",
                receipt,
            )
        return receipt


def capability_release(
    *,
    contract_ref: str,
    artifact_refs: list[str],
    acceptance_evidence: list[str],
    adapter_refs: list[str],
    rollback_ref: str,
    policy_compatibility: list[str] | None = None,
) -> dict[str, Any]:
    return {
        "schema": RELEASE_SCHEMA,
        "release_id": "rel-" + uuid.uuid4().hex[:20],
        "capability_id": CAPABILITY_ID,
        "capability_version": CAPABILITY_VERSION,
        "contract_ref": contract_ref,
        "artifact_refs": artifact_refs,
        "acceptance_evidence": acceptance_evidence,
        "policy_compatibility": policy_compatibility or [POLICY_VERSION],
        "adapter_refs": adapter_refs,
        "rollback_ref": rollback_ref,
        "published_at": now_iso(),
        "producer": "ryan-build",
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--version", action="store_true")
    args = ap.parse_args()
    if args.version:
        print(CAPABILITY_VERSION)
        return 0
    ap.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

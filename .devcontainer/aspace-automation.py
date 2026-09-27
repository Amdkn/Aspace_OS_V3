#!/usr/bin/env python3
from __future__ import annotations

import argparse
import fcntl
import json
import os
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
POLICY = json.loads((REPO_ROOT / "ASPACE_AUTOMATION_POLICY.json").read_text(encoding="utf-8"))
ROOT = Path(os.environ.get("ASPACE_WORKSPACE_ROOT", "/workspaces/aspace"))
STATE = ROOT / "workspace" / "automation"


def today_key() -> str:
    return datetime.now(timezone.utc).date().isoformat()


def ledger_path() -> Path:
    return STATE / f"{today_key()}.json"


def load_ledger() -> dict:
    p = ledger_path()
    if not p.exists():
        return {"date": today_key(), "consumed_seconds": 0.0, "runs": []}
    return json.loads(p.read_text(encoding="utf-8"))


def save_ledger(data: dict) -> None:
    STATE.mkdir(parents=True, exist_ok=True)
    ledger_path().write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def adapters() -> list[tuple[str, str]]:
    result = []
    for name, spec in POLICY["harnesses"].items():
        cmd = os.environ.get(spec["adapter_env"], "").strip()
        if cmd:
            result.append((name, cmd))
    return result


def env_for_harness(name: str) -> dict[str, str]:
    env = os.environ.copy()
    env["ASPACE_HARNESS"] = name
    env["ASPACE_REGISTRY"] = str(REPO_ROOT / "ASPACE_WORKSPACE_REGISTRY.json")
    env["ASPACE_AUTOMATION_POLICY"] = str(REPO_ROOT / "ASPACE_AUTOMATION_POLICY.json")
    env["ASPACE_WORKSPACE_ROOT"] = str(ROOT)
    env["ASPACE_LIFE_BUSINESS_MIN_SHARE"] = str(POLICY["capacity"]["life_business_min_share"])
    env["ASPACE_KERNEL_MAX_SHARE"] = str(POLICY["capacity"]["kernel_max_share"])
    env["ASPACE_MACHINE_STATE"] = POLICY["work_sources"]["machine_state"]
    env["ASPACE_HUMAN_INTENT"] = POLICY["work_sources"]["intent"]
    return env


def status() -> dict:
    ledger = load_ledger()
    budget = float(POLICY["daily_budget_seconds"])
    remaining = max(0.0, budget - float(ledger.get("consumed_seconds", 0.0)))
    return {
        "date": today_key(),
        "budget_seconds": budget,
        "consumed_seconds": ledger.get("consumed_seconds", 0.0),
        "remaining_seconds": remaining,
        "configured_adapters": [name for name, _ in adapters()],
    }


def run_daemon(cycle_timeout: int) -> int:
    STATE.mkdir(parents=True, exist_ok=True)
    lock_path = STATE / "daemon.lock"
    with lock_path.open("w") as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            print("A'Space automation daemon already active")
            return 0

        active = adapters()
        if not active:
            print("No Codespace harness adapters configured; automation budget preserved.")
            return 0

        while True:
            ledger = load_ledger()
            budget = float(POLICY["daily_budget_seconds"])
            remaining = max(0.0, budget - float(ledger.get("consumed_seconds", 0.0)))
            if remaining <= 0:
                print("Daily 4h automation budget exhausted.")
                return 0

            for name, cmd in active:
                remaining = max(0.0, budget - float(ledger.get("consumed_seconds", 0.0)))
                if remaining <= 0:
                    return 0
                started = time.monotonic()
                timeout = max(1, min(cycle_timeout, int(remaining)))
                try:
                    cp = subprocess.run(cmd, shell=True, cwd=ROOT, env=env_for_harness(name), timeout=timeout)
                    rc = cp.returncode
                except subprocess.TimeoutExpired:
                    rc = 124

                duration = time.monotonic() - started
                ledger["consumed_seconds"] = float(ledger.get("consumed_seconds", 0.0)) + duration
                ledger.setdefault("runs", []).append({
                    "harness": name,
                    "started_at": datetime.now(timezone.utc).isoformat(),
                    "duration_seconds": round(duration, 3),
                    "return_code": rc,
                })
                save_ledger(ledger)
                if rc not in (0, 124):
                    print(f"{name} adapter exited with {rc}; continuing bounded rotation.")
                time.sleep(2)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("status", "daemon"), default="status")
    parser.add_argument("--cycle-timeout", type=int, default=1200)
    args = parser.parse_args()
    if args.mode == "status":
        print(json.dumps(status(), indent=2))
        return 0
    return run_daemon(args.cycle_timeout)


if __name__ == "__main__":
    raise SystemExit(main())

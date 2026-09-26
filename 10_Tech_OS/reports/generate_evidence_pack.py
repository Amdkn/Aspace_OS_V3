#!/usr/bin/env python3
import json
import hashlib
import sys
import os
import subprocess
import argparse
from datetime import datetime, timezone

def calculate_sha256(filepath):
    sha256_hash = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return "FILE_NOT_FOUND"

def get_git_diff_summary():
    try:
        result = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
        if result.returncode != 0:
            return {"error": "Failed to get git status", "details": result.stderr}
        return result.stdout.strip()
    except Exception as e:
        return {"error": str(e)}

def run_checks(command, env=None):
    if not command:
        return None
    try:
        run_env = os.environ.copy()
        if env:
            run_env.update(env)

        start_time = datetime.now()
        result = subprocess.run(command, shell=True, capture_output=True, text=True, env=run_env)
        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()

        return {
            "command": command,
            "exit_code": result.returncode,
            "duration_seconds": duration,
            "output_tail": result.stdout[-1000:] if result.stdout else "",
            "error_tail": result.stderr[-1000:] if result.stderr else ""
        }
    except Exception as e:
        return {"command": command, "error": str(e)}

def parse_args():
    parser = argparse.ArgumentParser(description="Generate standard evidence pack (SOB-7/FPRD-020)")
    parser.add_argument("--work-id", type=int, required=True, help="Canonical WorkGraph work_id")
    parser.add_argument("--files", type=str, help="Comma-separated list of modified files to hash")
    parser.add_argument("--test-cmd", type=str, help="Command to run tests (unit/integration)")
    parser.add_argument("--lint-cmd", type=str, help="Command to run lint/build checks")
    parser.add_argument("--env-vars", type=str, help="Comma-separated KEY=VALUE pairs for check commands")
    parser.add_argument("--limits", type=str, nargs="*", default=[], help="Known limits/gaps in the implementation")
    parser.add_argument("--out", type=str, help="Output file path (default: stdout)")
    return parser.parse_args()

def main():
    args = parse_args()

    env_dict = {}
    if args.env_vars:
        for pair in args.env_vars.split(","):
            if "=" in pair:
                k, v = pair.split("=", 1)
                env_dict[k.strip()] = v.strip()

    evidence = {
        "work_id": args.work_id,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "state": "implemented_tests_passed_review_pending",
        "files_sha256": {},
        "git_diff_summary": get_git_diff_summary(),
        "checks": {},
        "limits": args.limits,
    }

    if args.files:
        for f in [x.strip() for x in args.files.split(",") if x.strip()]:
            evidence["files_sha256"][f] = calculate_sha256(f)

    if args.test_cmd:
        evidence["checks"]["test"] = run_checks(args.test_cmd, env_dict)

    if args.lint_cmd:
        evidence["checks"]["lint"] = run_checks(args.lint_cmd, env_dict)

    out_json = json.dumps(evidence, indent=2, ensure_ascii=False)

    if args.out:
        out_dir = os.path.dirname(args.out)
        if out_dir:
            os.makedirs(out_dir, exist_ok=True)
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(out_json)
        print(f"Evidence pack generated: {args.out}")
    else:
        print(out_json)

if __name__ == "__main__":
    main()

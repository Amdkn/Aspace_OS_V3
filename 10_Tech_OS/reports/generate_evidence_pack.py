import argparse
import datetime
import hashlib
import json
import subprocess
import os
from pathlib import Path

def get_file_sha256(filepath):
    if not os.path.exists(filepath):
        return None
    sha256 = hashlib.sha256()
    with open(filepath, 'rb') as f:
        while True:
            data = f.read(65536)
            if not data:
                break
            sha256.update(data)
    return sha256.hexdigest()

def get_git_diff_summary(filepath):
    try:
        # Check if we're in a git repo and if the files are tracked
        result = subprocess.run(['git', 'diff', '--stat', filepath], capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            return "Error or untracked file"
    except Exception as e:
        return str(e)

def run_command(command):
    if not command:
        return None
    try:
        # Pass env=os.environ.copy() as advised by memory
        result = subprocess.run(command, shell=True, capture_output=True, text=True, env=os.environ.copy())
        return {
            "command": command,
            "exit_code": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr
        }
    except Exception as e:
        return {
            "command": command,
            "error": str(e)
        }

def main():
    parser = argparse.ArgumentParser(description="Generate standard build/test/audit evidence pack (FPRD-020 / SOB-7)")
    parser.add_argument('--work-id', required=True, help="Work item ID")
    parser.add_argument('--files', nargs='+', default=[], help="Modified files")
    parser.add_argument('--test-command', help="Command to run tests")
    parser.add_argument('--lint-command', help="Command to run linters")
    parser.add_argument('--output', default='evidence_pack.json', help="Output JSON file")

    args = parser.parse_args()

    report = {
        "work_id": args.work_id,
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "files": {},
        "git_diff_summaries": {}
    }

    for filepath in args.files:
        report["files"][filepath] = {
            "sha256": get_file_sha256(filepath)
        }
        report["git_diff_summaries"][filepath] = get_git_diff_summary(filepath)

    if args.test_command:
        report["test_results"] = run_command(args.test_command)

    if args.lint_command:
        report["lint_results"] = run_command(args.lint_command)

    with open(args.output, 'w') as f:
        json.dump(report, f, indent=2)

    print(f"Evidence pack generated at {args.output}")

if __name__ == '__main__':
    main()

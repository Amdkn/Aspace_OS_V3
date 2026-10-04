#!/usr/bin/env python3
"""A'Space branch hygiene audit.

Read-only by default. Produces a machine-readable inventory for branch retirement.
It never deletes branches or worktrees.
"""
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path


def run(*args: str, cwd: Path | None = None) -> str:
    return subprocess.check_output(args, cwd=cwd, text=True, stderr=subprocess.STDOUT).strip()


def lines(cmd: list[str], cwd: Path) -> list[str]:
    out = run(*cmd, cwd=cwd)
    return [x for x in out.splitlines() if x.strip()]


def worktree_branches(repo: Path) -> set[str]:
    result: set[str] = set()
    for line in lines(["git", "worktree", "list", "--porcelain"], repo):
        prefix = "branch refs/heads/"
        if line.startswith(prefix):
            result.add(line[len(prefix):])
    return result


def remote_branches(repo: Path) -> list[str]:
    refs = lines(
        ["git", "for-each-ref", "--format=%(refname:short)", "refs/remotes/origin"],
        repo,
    )
    result = []
    for ref in refs:
        if ref in {"origin", "origin/HEAD", "origin/main"}:
            continue
        if ref.startswith("origin/"):
            result.append(ref[len("origin/"):])
    return result


def ancestor_of_main(repo: Path, branch: str) -> bool:
    proc = subprocess.run(
        ["git", "merge-base", "--is-ancestor", f"origin/{branch}", "origin/main"],
        cwd=repo,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return proc.returncode == 0


def patch_equivalent(repo: Path, branch: str) -> bool:
    try:
        output = run("git", "cherry", "origin/main", f"origin/{branch}", cwd=repo)
    except subprocess.CalledProcessError:
        return False
    return not any(line.startswith("+") for line in output.splitlines())


def classify_name(branch: str) -> str:
    if branch.startswith("Amdkn/"):
        return "HOME"
    if branch.startswith(("jules-", "autopublish/", "AUTO_CREATE_PR")):
        return "WORKER"
    if branch.startswith(("recover/", "backup/")):
        return "RECOVERY"
    if branch.startswith(("feat/", "fix/", "docs/", "design/", "test/", "feature/")):
        return "MISSION"
    return "OTHER"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=".")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    repo = Path(args.repo).resolve()
    run("git", "fetch", "origin", "--prune", cwd=repo)

    active = worktree_branches(repo)
    rows = []
    for branch in remote_branches(repo):
        if branch in active:
            verdict = "KEEP_ACTIVE"
        elif branch.startswith("Amdkn/"):
            verdict = "KEEP_HOME"
        elif ancestor_of_main(repo, branch):
            verdict = "RETIRE_ANCESTOR"
        elif patch_equivalent(repo, branch):
            verdict = "RETIRE_PATCH_EQUIV"
        else:
            verdict = "REVIEW_UNIQUE"
        rows.append(
            {
                "branch": branch,
                "class": classify_name(branch),
                "active_worktree": branch in active,
                "verdict": verdict,
            }
        )

    summary: dict[str, int] = {}
    for row in rows:
        summary[row["verdict"]] = summary.get(row["verdict"], 0) + 1

    payload = {"repo": str(repo), "summary": summary, "branches": rows}
    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

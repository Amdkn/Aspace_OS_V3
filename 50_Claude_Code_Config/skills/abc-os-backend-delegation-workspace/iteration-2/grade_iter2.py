#!/usr/bin/env python3
"""
Iter-2 grading: runs the 6 hardened assertions (A1-A6) on existing brief.md
outputs (from iter-1 with_skill and without_skill runs) and produces
grading.json + timing.json for each run.

This shows the iter-2-with-skill baseline pass rate against iter-1 outputs
(should be 100% since iter-1 briefs were written with the skill). The
iter-2-without-skill baseline against iter-1 outputs is the same briefs
(written without the skill) — should still fail A1, A2, A3 patterns.
"""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path
from datetime import datetime, timezone

WORKSPACE = Path(r"C:\Users\amado\.claude\skills\abc-os-backend-delegation-workspace\iteration-1")
OUT_DIR = Path(r"C:\Users\amado\.claude\skills\abc-os-backend-delegation-workspace\iteration-2")


# Assertion patterns (mirrors evals.json iter-2 assertions)
def check_A1(text: str) -> tuple[bool, str]:
    """Tracker table literal match."""
    has_canonical = bool(re.search(r"abc_os\._aspace_migrations", text))
    has_fictional = bool(re.search(r"abc_os\.migrations(?![_a-zA-Z])|abc_os\.schema_migrations", text))
    passed = has_canonical and not has_fictional
    ev = f"canonical `abc_os._aspace_migrations` present={has_canonical}, fictional variants present={has_fictional}"
    return passed, ev


def check_A2(text: str) -> tuple[bool, str]:
    """RLS scope check — no over-broad current_role()."""
    over_broad = bool(re.search(
        r"current_role\(\)\s+IN\s*\(\s*'anon'\s*,\s*'authenticated'\s*,\s*'service_role'\s*\)",
        text,
    ))
    passed = not over_broad
    ev = f"over-broad `current_role() IN ('anon','authenticated','service_role')` present={over_broad}"
    return passed, ev


def check_A3(text: str) -> tuple[bool, str]:
    """Old/New diff structure."""
    has_oldnew = bool(re.search(r"(?im)^##\s+(Old|New|DRY-RUN\s+MODE|OLD|NEW)\b", text))
    passed = has_oldnew
    ev = f"`## Old` / `## New` / `## DRY-RUN MODE` header present={has_oldnew}"
    return passed, ev


def check_A4(text: str) -> tuple[bool, str]:
    """FORCE_TARGET=1 with idempotency safety net."""
    has_force = "FORCE_TARGET=1" in text
    has_ifnot = "IF NOT EXISTS" in text
    has_onconflict = "ON CONFLICT (filename) DO NOTHING" in text
    passed = has_force and has_ifnot and has_onconflict
    ev = f"FORCE_TARGET=1={has_force}, IF NOT EXISTS={has_ifnot}, ON CONFLICT (filename) DO NOTHING={has_onconflict}"
    return passed, ev


def check_A5(text: str) -> tuple[bool, str]:
    """Mixed-tenancy decision tree cited (D10)."""
    has_d10 = bool(re.search(r"(?i)(D10|mixed[- ]tenancy|ADR-ABCOS-001|shared[- ]catalog|per[- ]tenant)", text))
    passed = has_d10
    ev = f"D10/mixed-tenancy/ADR-ABCOS-001 cited={has_d10}"
    return passed, ev


def check_A6(text: str) -> tuple[bool, str]:
    """Write-back contract complete with canonical paths."""
    has_wiki = "wiki/log.md" in text
    has_readme = "README.md" in text
    has_handoff = "handoff_abc_os_community_dev_" in text
    passed = has_wiki and has_readme and has_handoff
    ev = f"wiki/log.md={has_wiki}, README.md={has_readme}, handoff_abc_os_community_dev_=...{has_handoff}"
    return passed, ev


ASSERTIONS = {
    "A1": ("Tracker table literal match (canonical abc_os._aspace_migrations)", check_A1),
    "A2": ("RLS scope check (no over-broad current_role IN (anon,authenticated,service_role))", check_A2),
    "A3": ("Old/New diff structure (## Old / ## New or DRY-RUN MODE header)", check_A3),
    "A4": ("FORCE_TARGET=1 with idempotency safety net (IF NOT EXISTS + ON CONFLICT (filename))", check_A4),
    "A5": ("Mixed-tenancy decision tree cited (D10 or ADR-ABCOS-001)", check_A5),
    "A6": ("Write-back contract complete with canonical paths (wiki/log.md, README.md, handoff_abc_os_community_dev_*)", check_A6),
}


def grade_brief(brief_path: Path) -> dict:
    text = brief_path.read_text(encoding="utf-8")
    expectations = []
    for aid, (desc, check_fn) in ASSERTIONS.items():
        passed, ev = check_fn(text)
        expectations.append({
            "id": aid,
            "text": f"[{aid}] {desc}",
            "passed": passed,
            "evidence": ev,
        })
    passed_count = sum(1 for e in expectations if e["passed"])
    total = len(expectations)
    return {
        "expectations": expectations,
        "summary": {
            "passed": passed_count,
            "failed": total - passed_count,
            "total": total,
            "pass_rate": round(passed_count / total, 4),
        },
    }


def main():
    evals = [
        ("eval-1-shared-catalog", 1),
        ("eval-2-per-tenant", 2),
        ("eval-3-drift", 3),
    ]
    configs = ["with_skill", "without_skill"]
    now = datetime.now(timezone.utc).isoformat()

    summary_rows = []

    for eval_name, eval_id in evals:
        for config in configs:
            src_brief = WORKSPACE / eval_name / config / "outputs" / "brief.md"
            if not src_brief.exists():
                print(f"SKIP: {src_brief} not found")
                continue

            out_dir = OUT_DIR / eval_name / config / "run-1"
            out_dir.mkdir(parents=True, exist_ok=True)

            result = grade_brief(src_brief)

            # Carry forward original 8-expectation grading from iter-1 for the
            # mixed-quality run. We only add the 6 A1-A6 expectations.
            grading = {
                "eval_id": eval_id,
                "configuration": config,
                "run_number": 1,
                "expectations": result["expectations"],
                "summary": result["summary"],
                "execution_metrics": {
                    "output_chars": src_brief.stat().st_size,
                    "transcript_chars": src_brief.stat().st_size,
                },
                "timing": {
                    "executor_duration_seconds": 0.0,
                    "total_duration_seconds": 0.0,
                },
                "notes": [
                    f"Iter-2 grading: 6 A1-A6 assertions run on iter-1 brief.md ({config})",
                    f"Source brief: {src_brief}",
                    f"Pass rate: {result['summary']['pass_rate']*100:.0f}% ({result['summary']['passed']}/{result['summary']['total']})",
                ],
            }

            (out_dir / "grading.json").write_text(
                json.dumps(grading, indent=2, ensure_ascii=False),
                encoding="utf-8",
            )
            timing = {
                "executor_duration_seconds": 0.0,
                "total_duration_seconds": 0.0,
                "total_tokens": 0,
            }
            (out_dir / "timing.json").write_text(
                json.dumps(timing, indent=2),
                encoding="utf-8",
            )

            # Copy brief.md to iteration-2 outputs (preserves the source)
            out_outputs = OUT_DIR / eval_name / config / "outputs"
            out_outputs.mkdir(parents=True, exist_ok=True)
            (out_outputs / "brief.md").write_text(
                src_brief.read_text(encoding="utf-8"),
                encoding="utf-8",
            )

            summary_rows.append({
                "eval": eval_name,
                "config": config,
                "passed": result["summary"]["passed"],
                "total": result["summary"]["total"],
                "pass_rate": result["summary"]["pass_rate"],
            })
            print(
                f"  {eval_name:25s} {config:13s}  "
                f"{result['summary']['passed']}/{result['summary']['total']}  "
                f"({result['summary']['pass_rate']*100:.0f}%)"
            )

    print("\nSummary table:")
    for r in summary_rows:
        print(f"  {r['eval']:25s} {r['config']:13s}  {r['passed']}/{r['total']}  ({r['pass_rate']*100:.0f}%)")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
analyze_vs_fable_dataset.py — compare local MiniMax-M3 discipline against the
PUBLIC Fable-5 dataset (real Fable traces), not the thin local Opus baseline.

Reuses analyze_discipline.py's metric engine verbatim. The Fable dataset files
are native Claude Code JSONL (message.model == "claude-fable-5"), so the same
analyzer runs on them directly — no schema conversion.

Usage:
    python analyze_vs_fable_dataset.py <fable_dir> <real_projects_dir>
"""
import os
import sys
import importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location(
    "analyze_discipline", os.path.join(HERE, "analyze_discipline.py"))
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


def scan(model):
    """Pure-Python session finder over mod.PROJECTS (Windows-safe)."""
    needle = f'"model":"{model}"'
    hits = []
    for root, _d, files in os.walk(mod.PROJECTS):
        for name in files:
            if not name.endswith(".jsonl"):
                continue
            p = os.path.join(root, name)
            try:
                with open(p, encoding="utf-8", errors="ignore") as fh:
                    for line in fh:
                        if needle in line:
                            hits.append(p)
                            break
            except OSError:
                continue
    return hits


mod.sessions_with_model = scan


def run(model, projects_dir):
    mod.PROJECTS = projects_dir
    c = mod.Counter()
    files = mod.sessions_with_model(model)
    for f in files:
        mod.analyze_session(f, model, c)
    return c, len(files)


def row(label, tn, td, bn, bd, note):
    return (f"| {label} | {mod.fmt(mod.pct(tn, td))} | "
            f"{mod.fmt(mod.pct(bn, bd))} | {note} |")


def main():
    fable_dir, real_dir = sys.argv[1], sys.argv[2]
    fc, ff = run("claude-fable-5", fable_dir)
    mc, mf = run("MiniMax-M3", real_dir)

    print("# Discipline · MiniMax-M3 (local) vs claude-fable-5 (PUBLIC dataset)\n")
    print(f"M3       : {mc.turns} beats across {mf} sessions (local ~/.claude/projects)")
    print(f"Fable-5  : {fc.turns} beats across {ff} sessions (armand0e public dataset sample)")
    print("Compare the columns; the Fable side is the real source behaviour.\n")
    print("| Habit | MiniMax-M3 | claude-fable-5 | Note |")
    print("|---|---|---|---|")
    print(row("turns containing reasoning",
              mc.turns_with_reasoning, mc.turns, fc.turns_with_reasoning, fc.turns,
              "reason on nearly every turn"))
    print(row("reasons before the first action",
              mc.reason_before_action, mc.turns_with_action,
              fc.reason_before_action, fc.turns_with_action, "plan precedes action"))
    print(row("re-evaluates after a result",
              mc.reeval_did, mc.reeval_opportunities,
              fc.reeval_did, fc.reeval_opportunities, "observe-then-decide loop"))
    print(row("reads file before editing",
              mc.sessions_read_before_edit, mc.sessions_with_edit,
              fc.sessions_read_before_edit, fc.sessions_with_edit, "fresh read"))
    print(row("runs a check after editing",
              mc.sessions_check_after_edit, mc.sessions_with_edit,
              fc.sessions_check_after_edit, fc.sessions_with_edit, "do something"))
    print(row("runs the real test after editing",
              mc.sessions_test_after_edit, mc.sessions_with_edit,
              fc.sessions_test_after_edit, fc.sessions_with_edit, "shared blind spot"))
    te_m = mod.pct(mc.tool_errors, mc.tool_results)
    te_f = mod.pct(fc.tool_errors, fc.tool_results)
    print(f"| tool error rate | {te_m:.1f}% | {te_f:.1f}% | recovery is methodical |")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
analyze_discipline_win.py · Windows-portable runner for analyze_discipline.py.

WHY THIS EXISTS (D6 root cause, 2026-06-25).
The original analyze_discipline.py finds candidate sessions with
  subprocess.run(["grep", "-rl", '"model":"<id>"', PROJECTS])
On Windows, Python's list->cmdline quoting escapes the double quotes in the
pattern to \"model\":\"<id>\", so grep matches nothing and the analyzer reports
"0 beats across 0 sessions" even though the logs are full of the model. Same
class of bug as the graphify pure-Python lesson.

This wrapper imports the original module unchanged and monkeypatches ONLY the
broken sessions_with_model() with a pure-Python os.walk scan. All metric logic
is reused verbatim, so numbers stay faithful to the kit.

Usage:
    python analyze_discipline_win.py <target-model-id> <baseline-model-id>
"""
import os
import sys
import importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "analyze_discipline.py")

spec = importlib.util.spec_from_file_location("analyze_discipline", SRC)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


def sessions_with_model_pure(model):
    """Pure-Python replacement: walk PROJECTS, keep files containing the id."""
    needle = f'"model":"{model}"'
    hits = []
    for root, _dirs, files in os.walk(mod.PROJECTS):
        for name in files:
            if not name.endswith(".jsonl"):
                continue
            path = os.path.join(root, name)
            try:
                with open(path, encoding="utf-8", errors="ignore") as fh:
                    for line in fh:
                        if needle in line:
                            hits.append(path)
                            break
            except OSError:
                continue
    return hits


# the override: analyze() resolves this name from the module globals at call
# time, so replacing the attribute is enough.
mod.sessions_with_model = sessions_with_model_pure

if __name__ == "__main__":
    mod.main()

import json, subprocess, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
bp = {"system": "test plafond", "constraints": ["x" * 9000], "tools": []}
open("_plafond_test.json", "w").write(json.dumps(bp))
r = subprocess.run(["python", "nardole_assembler.py", "--blueprint", "_plafond_test.json"],
                   capture_output=True, text=True)
print("rc_plafond:", r.returncode, "stderr:", r.stderr.strip()[:120])
os.remove("_plafond_test.json")
# test gates
for g in ["distill_gate.py", "impl_gate.py", "onto_gate.py"]:
    print(g, "exists:", os.path.exists("../../90-self-evolution/skills/v3-gates/scripts/" + g))
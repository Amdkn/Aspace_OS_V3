import json, subprocess, sys
big = json.dumps({"system": "X", "constraints": ["a" * 9000], "tools": []})
r = subprocess.run([sys.executable, "nardole_assembler.py", "compile",
                    "--slug", "rituel-claim", "--blueprint", big],
                   capture_output=True, text=True)
print("rc:", r.returncode)
print("stderr:", r.stderr.strip()[:200])
sys.exit(0 if r.returncode != 0 else 1)

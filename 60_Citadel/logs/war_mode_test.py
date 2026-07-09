import sys
from pathlib import Path
sys.path.insert(0, r'C:\Users\amado\agent-os\citadel')

# run collector_14 first
import subprocess
r = subprocess.run([sys.executable, r'C:\Users\amado\agent-os\citadel\collectors\collector_14_warmode.py'],
                    capture_output=True, text=True, env={'PYTHONIOENCODING':'utf-8'})
print('collector_14 exit=', r.returncode)
print('stdout :', r.stdout)
print('stderr :', r.stderr[:200] if r.stderr else '(none)')

# run book_loop
import book_loop
report = book_loop.main()
print('book_loop main returned:', report)

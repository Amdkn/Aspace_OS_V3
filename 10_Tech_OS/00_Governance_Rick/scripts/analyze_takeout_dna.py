import os
from html import unescape
import re

# Resolve the complex path with the non-breaking space
base = "C:\Aspace00\Takeout"
activity_dirs = [d for d in os.listdir(base) if d.startswith("Mon")]
if not activity_dirs:
    print("Base directory not found.")
    exit(1)

mon_activite = os.path.join(base, activity_dirs[0])
app_dirs = [d for d in os.listdir(mon_activite) if d.startswith("Applications")]
if not app_dirs:
    print("Application directory not found.")
    exit(1)

source_file = os.path.join(mon_activite, app_dirs[0], "MonActivité.html")

def analyze_structure():
    with open(source_file, 'r', encoding='utf-8', errors='ignore') as f:
        # Read first 100kb to find structure
        head = f.read(100000)
    
    # Look for common Google Takeout patterns
    patterns = [
        r'class="outer-cell',
        r'class="content-cell',
        r'class="header-cell',
        r'br>[A-Z][a-z]+ \d+, \d{4}' # Date pattern
    ]
    
    print(f"File Size: {os.path.getsize(source_file) / (1024*1024):.2f} MB")
    for p in patterns:
        matches = len(re.findall(p, head))
        print(f"Pattern '{p}' matches: {matches}")

analyze_structure()

"""Read all truly_unread files, capture content signatures, verify the pattern hypothesis."""
import os, re, json
from pathlib import Path

ROOT = Path('C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise')
unread_file = Path('C:/Users/amado/ASpace_OS_V3/00_Amadeus/30_MEMORY_CORE/carto/v4_truly_unread.txt')

with open(unread_file, encoding='utf-8') as f:
    paths = [l.strip() for l in f if l.strip()]

print(f'Total paths to process: {len(paths)}')

results = []
for rel in paths:
    full = ROOT / rel
    if not full.exists():
        # Try alternative root
        full2 = Path('C:/Users/amado/ASpace_OS_V3/00_Amadeus/30_MEMORY_CORE') / rel
        if full2.exists():
            full = full2
        else:
            results.append({'rel': rel, 'status': 'NOT_FOUND'})
            continue
    try:
        text = full.read_text(encoding='utf-8', errors='replace')
        # Capture signature
        n_lines = len(text.splitlines())
        n_chars = len(text)
        # Extract squad member name
        m = re.search(r'Squad member\*\* : (\w+)', text)
        sm = m.group(1) if m else None
        m2 = re.search(r'Role\*\* : (\S+)', text)
        role = m2.group(1) if m2 else None
        m3 = re.search(r'\*\*Project\*\* : (.+)', text)
        proj = m3.group(1) if m3 else None
        m4 = re.search(r'# (.+?) \(.+\) - (.+?) / (\w+)_(\w+)_(\w+)', text)
        title = m4.group(0) if m4 else text.split('\n', 1)[0]
        results.append({
            'rel': rel, 'status': 'OK',
            'lines': n_lines, 'chars': n_chars,
            'project': proj, 'squad_member': sm, 'role': role
        })
    except Exception as e:
        results.append({'rel': rel, 'status': f'ERR:{e}'})

# Summary
by_status = {}
for r in results:
    by_status.setdefault(r['status'], []).append(r)
for k, v in by_status.items():
    print(f'{k}: {len(v)}')

# Distinct patterns
ok = [r for r in results if r['status'] == 'OK']
from collections import Counter
line_counts = Counter(r['lines'] for r in ok)
char_counts = Counter(r['chars'] for r in ok)
print('Line count distribution:')
for k, v in line_counts.most_common():
    print(f'  {k} lines: {v} files')
print('Char count distribution (top 10):')
for k, v in char_counts.most_common(10):
    print(f'  {k} chars: {v} files')

# List any non-9-line files (anomalies)
anomalies = [r for r in ok if r['lines'] != 9]
print(f'Anomalies (not 9 lines): {len(anomalies)}')
for a in anomalies[:30]:
    print(f'  {a["rel"]}  {a["lines"]} lines, {a["chars"]} chars')

# Save results
out = Path('C:/Users/amado/ASpace_OS_V3/00_Amadeus/30_MEMORY_CORE/carto/v4_read_results.json')
with open(out, 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=1, ensure_ascii=False)
print(f'Saved to {out}')

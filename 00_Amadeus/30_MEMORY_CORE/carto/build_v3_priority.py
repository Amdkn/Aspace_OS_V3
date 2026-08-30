import json
from pathlib import Path
import re

base = Path('C:/Users/amado/ASpace_OS_V3/00_Amadeus/30_MEMORY_CORE/carto')
v1 = json.load(open(base / '04_Archives_Data.json', encoding='utf-8'))
v2 = json.load(open(base / '04_Archives_Data_v2.json', encoding='utf-8'))

seen = set()
for entry in v1.get('types', []) + v2.get('types', []):
    for p in entry.get('chemins', []):
        seen.add(p)
for entry in v1.get('relations', []) + v2.get('relations', []):
    p = entry.get('chemin', '')
    if p:
        seen.add(p)
for entry in v1.get('codes', []) + v2.get('codes', []):
    p = entry.get('defini_dans', '')
    if p:
        seen.add(p)
for entry in v1.get('contradictions', []) + v2.get('contradictions', []):
    for k in ('chemin_a', 'chemin_b'):
        p = entry.get(k, '')
        if p:
            seen.add(p)

BS = chr(92)
def strip_annotation(p):
    p = re.sub(r'\s*\([^)]*\)\s*$', '', p).strip()
    p = re.sub(r'\s*�\s*\S+\s*$', '', p).strip()
    p = re.sub(r'\s+ligne\s+\d+\s*$', '', p, flags=re.IGNORECASE).strip()
    return p

# Build a set of (lowercase basename) and (lowercase last 2 components) keys
# Use ONLY seen paths that are at least 3 components long (after stripping annotation)
seen_specific = set()
seen_basenames = set()
for s in seen:
    s2 = strip_annotation(s).replace(BS, '/').lower()
    parts = s2.split('/')
    if len(parts) >= 3:
        # Last 3 components
        seen_specific.add('/'.join(parts[-3:]))
    if len(parts) >= 4:
        seen_specific.add('/'.join(parts[-4:]))
    if parts:
        seen_basenames.add(parts[-1])

print('seen specific (3-4 comp):', len(seen_specific))
print('seen basenames:', len(seen_basenames))

w2 = open(base / '04_w2_unread.txt', encoding='utf-8').read().splitlines()
w2 = [l for l in w2 if l.strip()]
print('w2 paths:', len(w2))

# First check: keep paths that match the 3-4 component specific seen list
matched = 0
unmatched = []
for w in w2:
    n = w.replace(BS, '/').lower()
    parts = n.split('/')
    short3 = '/'.join(parts[-3:]) if len(parts) >= 3 else ''
    short4 = '/'.join(parts[-4:]) if len(parts) >= 4 else ''
    bn = parts[-1]
    if short3 in seen_specific or short4 in seen_specific:
        matched += 1
    elif bn in seen_basenames:
        # basenames are too generic to mark as read — keep these as unread
        unmatched.append(w)
    else:
        unmatched.append(w)

print('matched (specific 3-4 components):', matched)
print('unread:', len(unmatched))

def depth(p):
    p = p.replace(BS, '/')
    marker = '04_archives_data/'
    if marker in p:
        sub = p.split(marker, 1)[1]
    else:
        sub = p
    return sub.count('/')

unmatched.sort(key=lambda p: (depth(p), p))

with open(base / '04_v3_priority.txt', 'w', encoding='utf-8') as f:
    for u in unmatched:
        f.write(u + '\n')
print('Wrote 04_v3_priority.txt with', len(unmatched), 'paths')

from collections import Counter
print('Depth distribution of unread:')
for d, c in sorted(Counter(depth(p) for p in unmatched).items()):
    print(f'  depth {d}: {c}')
print('Top 30 by depth (highest in tree):')
for u in unmatched[:30]:
    print(f'  d{depth(u)}', u)

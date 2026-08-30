import json
import re
from pathlib import Path
from collections import Counter

CWD = Path('C:/Users/amado/ASpace_OS_V3/00_Amadeus/30_MEMORY_CORE/carto')

def normalize_v3_path(p):
    """Normalize a v3 JSON path (relative) for comparison."""
    if not p:
        return None
    p = p.replace('\\', '/').strip()
    # Strip leading prefixes
    for prefix in [
        'C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/',
        'C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise',
        'C:/Users/amado/ASpace_OS_V3/00_Amadeus/30_MEMORY_CORE/',
        'C:/Users/amado/ASpace_OS_V3/00_Amadeus/30_MEMORY_CORE',
    ]:
        if p.startswith(prefix):
            p = p[len(prefix):]
    return p

def normalize_priority_path(p):
    """Normalize priority list absolute path."""
    if not p:
        return None
    p = p.replace('\\', '/').strip()
    for prefix in [
        'C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/',
        'C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise',
        'C:/Users/amado/ASpace_OS_V3/00_Amadeus/30_MEMORY_CORE/',
        'C:/Users/amado/ASpace_OS_V3/00_Amadeus/30_MEMORY_CORE',
    ]:
        if p.startswith(prefix):
            p = p[len(prefix):]
    return p

# Aggregate covered paths from v1+v2+v3 normalized
covered = set()
for fname in ['03_Resources_Geordi.json', '03_Resources_Geordi_v2.json', '03_Resources_Geordi_v3.json']:
    j = json.load(open(CWD / fname, encoding='utf-8'))
    for t in j.get('types', []):
        for c in t.get('chemins', []):
            n = normalize_v3_path(c)
            if n:
                covered.add(n)
    for r in j.get('relations', []):
        n = normalize_v3_path(r.get('chemin'))
        if n:
            covered.add(n)
    for cd in j.get('codes', []):
        n = normalize_v3_path(cd.get('defini_dans'))
        if n:
            covered.add(n)
    for cr in j.get('contradictions', []):
        for k in ['chemin_a', 'chemin_b']:
            n = normalize_v3_path(cr.get(k))
            if n:
                covered.add(n)

print('Covered v1+v2+v3 unique:', len(covered))

# Load priority list
with open(CWD / '03_geordi_w3_priority.txt', encoding='utf-8') as f:
    priority = [l.strip() for l in f if l.strip()]
print('Priority list size:', len(priority))

# Normalize priority paths and compare
priority_normalized = [normalize_priority_path(p) for p in priority]
priority_set = set(priority_normalized)

# Truly unread
unread_indices = [i for i, p in enumerate(priority_normalized) if p not in covered]
unread = [priority[i] for i in unread_indices]
print('Truly unread in priority:', len(unread))

# Save
with open(CWD / '03_geordi_v4_unread.txt', 'w', encoding='utf-8') as f:
    for p in unread:
        f.write(p + '\n')
print('Saved 03_geordi_v4_unread.txt')

# Distribution by top 2 folders
def top2(p):
    p = normalize_priority_path(p)
    parts = p.split('/')
    return '/'.join(parts[:2]) if len(parts) >= 2 else parts[0]

unread_top = Counter(top2(p) for p in unread)
print('Unread by top-2 folder (top 30):')
for k, v in unread_top.most_common(30):
    print(f'  {v:5d}  {k}')

# Also check for paths with weird prefixes
print('--- Sanity check: sample unread paths ---')
for u in unread[:15]:
    print(' ', u)

# How many covered paths are within priority list?
covered_in_priority = [p for p in priority_normalized if p in covered]
print('Covered paths within priority:', len(set(covered_in_priority)))

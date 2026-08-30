import json
import os
import re
from pathlib import Path

V2_ROOT = Path('C:/Users/amado/ASpace_OS_V2')
SEAU_NAME = '04_Archives_Data'

with open('carto/04_Archives_Data.json', 'r', encoding='utf-8') as f:
    w1 = json.load(f)

already_short = set()
for t in w1['types']:
    for p in t.get('chemins', []):
        already_short.add(p)
for r in w1['relations']:
    if 'chemin' in r:
        already_short.add(r['chemin'])
for c in w1['codes']:
    if 'defini_dans' in c:
        already_short.add(c['defini_dans'])
for co in w1['contradictions']:
    if 'chemin_a' in co:
        already_short.add(co['chemin_a'])
    if 'chemin_b' in co:
        already_short.add(co['chemin_b'])

def short_key(p):
    parts = p.replace('\\', '/').split('/')
    if len(parts) >= 2:
        return '/'.join(parts[-2:]).lower()
    return p.lower()

already_keys = set(short_key(p) for p in already_short)
print('total unique short keys:', len(already_keys))

# Read structure.txt and find 04_Archives_Data
all_files = []
with open('carto/structure.txt', 'r', encoding='utf-8', errors='replace') as f:
    for line in f:
        line = line.rstrip('\n')
        if not line:
            continue
        parts = line.split('\t', 1)
        if len(parts) != 2:
            continue
        seau, path = parts
        if seau == SEAU_NAME:
            all_files.append(path)

print('total 04_Archives_Data in structure:', len(all_files))

# Filter unread using key matching
unread = []
for path in all_files:
    key = short_key(path.replace(V2_ROOT.as_posix() + '/', ''))
    if key not in already_keys:
        unread.append(path)

print('unread:', len(unread))

# Save list
with open('carto/04_w2_unread.txt', 'w', encoding='utf-8') as f:
    for p in unread:
        f.write(p + '\n')

# Print first 20 by depth-priority
def depth(p):
    rel = p.replace(V2_ROOT.as_posix(), '')
    rel = rel.replace('\\', '/').lstrip('/')
    # priority = higher first
    if SEAU_NAME + '/_V3_STRUCTURE_2026-08-02' in rel:
        # Inside _V3_STRUCTURE
        rest = rel.split(SEAU_NAME + '/_V3_STRUCTURE_2026-08-02/')[1]
        # priority by directory depth
        return (1, rest.count('/'), len(rest))
    if SEAU_NAME + '/' in rel:
        rest = rel.split(SEAU_NAME + '/')[1]
        return (2, rest.count('/'), len(rest))
    return (3, 0, len(rel))

unread_sorted = sorted(unread, key=depth)
print('\nFirst 30 sorted by priority (high in tree):')
for p in unread_sorted[:30]:
    print(' ', p.replace(V2_ROOT.as_posix(), '<V2>'))

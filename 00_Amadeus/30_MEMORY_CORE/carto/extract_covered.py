import json
import re

v1 = json.load(open('04_Archives_Data.json', encoding='utf-8'))
v2 = json.load(open('04_Archives_Data_v2.json', encoding='utf-8'))
v3 = json.load(open('04_Archives_Data_v3.json', encoding='utf-8'))

covered = set()
for j in [v1, v2, v3]:
    for t in j.get('types', []):
        for c in t.get('chemins', []):
            if c and 'C:/' in c:
                # Normalize: forward slashes only, lowercase, no double slashes
                covered.add(c.replace('\\', '/'))
    for r in j.get('relations', []):
        c = r.get('chemin', '')
        if c and 'C:/' in c:
            covered.add(c.replace('\\', '/'))
    for cd in j.get('codes', []):
        c = cd.get('defini_dans', '')
        if c and 'C:/' in c:
            covered.add(c.replace('\\', '/'))
    for cr in j.get('contradictions', []):
        for k in ['chemin_a', 'chemin_b']:
            if cr.get(k) and 'C:/' in cr[k]:
                covered.add(cr[k].replace('\\', '/'))

print('Covered normalized paths:', len(covered))

# Now compare with the all paths list
all_paths = []
with open('04_v4_all_paths.txt', encoding='utf-8') as f:
    for line in f:
        parts = line.rstrip('\n').split('\t', 1)
        if len(parts) == 2:
            all_paths.append(parts[1].replace('\\', '/'))

all_set = set(all_paths)
print('Total all paths:', len(all_set))

unread = sorted(all_set - covered)
print('Unread paths:', len(unread))

with open('04_v4_unread.txt', 'w', encoding='utf-8') as f:
    for p in unread:
        f.write(p + '\n')

covered_in_all = sorted(covered & all_set)
print('Covered paths within bucket:', len(covered_in_all))
with open('04_v4_covered_in_bucket.txt', 'w', encoding='utf-8') as f:
    for p in covered_in_all:
        f.write(p + '\n')

# Sample
print('Sample covered:')
for p in list(covered_in_all)[:5]:
    print(' ', p)
print('Sample unread:')
for p in list(unread)[:5]:
    print(' ', p)

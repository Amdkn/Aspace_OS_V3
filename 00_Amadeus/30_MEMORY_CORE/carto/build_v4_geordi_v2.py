import json
from pathlib import Path

CWD = Path('C:/Users/amado/ASpace_OS_V3/00_Amadeus/30_MEMORY_CORE/carto')

# Aggregate covered paths from v1+v2+v3
all_v = set()
for fname in ['03_Resources_Geordi.json', '03_Resources_Geordi_v2.json', '03_Resources_Geordi_v3.json']:
    j = json.load(open(CWD / fname, encoding='utf-8'))
    for t in j.get('types', []):
        for c in t.get('chemins', []):
            if c:
                all_v.add(c.replace('\\', '/'))
    for r in j.get('relations', []):
        c = r.get('chemin', '')
        if c:
            all_v.add(c.replace('\\', '/'))
    for cd in j.get('codes', []):
        c = cd.get('defini_dans', '')
        if c:
            all_v.add(c.replace('\\', '/'))
    for cr in j.get('contradictions', []):
        for k in ['chemin_a', 'chemin_b']:
            if cr.get(k):
                all_v.add(cr[k].replace('\\', '/'))

print('Covered v1+v2+v3 unique:', len(all_v))

# Load priority list (where wave 3 read)
with open(CWD / '03_geordi_w3_priority.txt', encoding='utf-8') as f:
    priority = [l.strip().replace('\\', '/') for l in f if l.strip()]
print('Priority list size:', len(priority))

# Compute truly unread
unread = [p for p in priority if p not in all_v]
print('Truly unread in priority:', len(unread))

# Also check if priority items in v3 are still readable (sanity check)
in_v3 = [p for p in priority if p in all_v]
print('In v3:', len(in_v3))

# Save
with open(CWD / '03_geordi_v4_unread.txt', 'w', encoding='utf-8') as f:
    for p in unread:
        f.write(p + '\n')
print('Saved 03_geordi_v4_unread.txt')

# Distribution by top 2 folders
from collections import Counter
def top2(p):
    p = p.replace('C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/', '')
    p = p.replace('C:/Users/amado/ASpace_OS_V3/00_Amadeus/30_MEMORY_CORE/', '')
    parts = p.split('/')
    return '/'.join(parts[:2]) if len(parts) >= 2 else parts[0]

unread_top = Counter(top2(p) for p in unread)
print('Unread by top-2 folder (top 30):')
for k, v in unread_top.most_common(30):
    print(f'  {v:5d}  {k}')

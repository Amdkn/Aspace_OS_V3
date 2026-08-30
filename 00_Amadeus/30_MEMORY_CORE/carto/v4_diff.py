import json
from pathlib import Path

CWD = Path('C:/Users/amado/ASpace_OS_V3/00_Amadeus/30_MEMORY_CORE/carto')

with open(CWD / '01_Projects_Picard_v3.json', encoding='utf-8') as f:
    v3 = json.load(f)

v3_paths = set()
for t in v3.get('types', []):
    for k in ('chemins', 'chemins_resume', 'chemins_v3', 'chemins_v2', 'chemins_v2_exemples'):
        for c in t.get(k, []):
            v3_paths.add(c)

for r in v3.get('relations', []):
    v3_paths.add(r.get('chemin', ''))

print(f'Total unique paths declared in v3: {len(v3_paths)}')

def normalize(p):
    p = p.replace('\\', '/')
    for prefix in ('C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/', 'C:/Users/amado/ASpace_OS_V3/00_Amadeus/30_MEMORY_CORE/'):
        if p.startswith(prefix):
            return p[len(prefix):]
    return p

with open(CWD / '01_Projects_Picard_unread.txt', encoding='utf-8') as f:
    unread = [l.strip() for l in f if l.strip()]

unread_norm = [normalize(p) for p in unread]
v3_norm = set(normalize(p) for p in v3_paths)

truly_unread = [u for u in unread_norm if u not in v3_norm]
print(f'Paths in unread.txt: {len(unread_norm)}')
print(f'Paths in v3: {len(v3_norm)}')
print(f'Truly unread (not in v3): {len(truly_unread)}')

with open(CWD / 'v4_truly_unread.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(truly_unread))

print('--- First 50 truly unread ---')
for u in truly_unread[:50]:
    print('  ', u)

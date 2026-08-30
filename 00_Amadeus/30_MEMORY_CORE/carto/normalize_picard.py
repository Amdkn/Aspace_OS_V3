import re, json

with open('01_Projects_Picard_all_paths.txt', encoding='utf-8') as f:
    paths = [l.strip() for l in f if l.strip()]

# find the segment starting with 01_Projects_Picard
rel = []
for p in paths:
    # p may have mixed / and \
    idx = max(p.rfind('01_Projects_Picard/'), p.rfind('01_Projects_Picard\\'))
    if idx >= 0:
        segment = p[idx:].replace('\\', '/')
        rel.append(segment)

with open('01_Projects_Picard_all_rel.txt', 'w', encoding='utf-8') as f:
    for r in sorted(set(rel)):
        f.write(r + '\n')
print(f'total unique relative: {len(set(rel))}')

# now load wave 1 read set
with open('01_Projects_Picard.json', encoding='utf-8') as f:
    data = json.load(f)
seen = set()
for t in data.get('types', []):
    for c in t.get('chemins', []):
        seen.add(c.split(' (')[0].strip())
for r in data.get('relations', []):
    seen.add(r.get('chemin', '').split(' (')[0].strip())

with open('01_Projects_Picard_v1_read_rel.txt', 'w', encoding='utf-8') as f:
    for s in sorted(seen):
        f.write(s + '\n')
print(f'wave1 read paths: {len(seen)}')

# diff
unread = sorted(set(rel) - seen)
with open('01_Projects_Picard_unread.txt', 'w', encoding='utf-8') as f:
    for u in unread:
        f.write(u + '\n')
print(f'unread: {len(unread)}')

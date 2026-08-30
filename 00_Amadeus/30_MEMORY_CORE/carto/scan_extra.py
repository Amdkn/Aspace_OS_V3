import os, stat, json
from collections import Counter

ROOT = 'C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock'
PREFIX = 'C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/'
RP = getattr(stat, 'FILE_ATTRIBUTE_REPARSE_POINT', 0x400)
SKIP_DIRS = {'node_modules', '.git', 'graphify-out', 'dist', '.next'}

# Already-read paths (normalized to forward slashes)
with open('02_read.json', encoding='utf-8') as f:
    already_read = set(json.load(f))

# Structure.txt filter list (95)
with open('02_Areas_Spock_all.txt', encoding='utf-8') as f:
    structure_txt = set()
    for line in f:
        seau, p = line.strip().split('\t')
        rel = p.replace(PREFIX, '').replace('\\', '/')
        structure_txt.add(rel)

# Find ALL files (not just .md)
all_files = []
junctions = 0
for root, dirs, files in os.walk(ROOT, followlinks=False):
    dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
    try:
        attrs = os.stat(root, follow_symlinks=False).st_file_attributes
        if attrs & RP:
            junctions += 1
            continue
    except:
        pass
    for f in files:
        p = os.path.join(root, f)
        try:
            attrs = os.stat(p, follow_symlinks=False).st_file_attributes
            if attrs & RP:
                junctions += 1
                continue
        except:
            continue
        all_files.append(p.replace('\\', '/'))

# categorize
md_all = [p for p in all_files if p.endswith('.md')]
non_md = [p for p in all_files if not p.endswith('.md')]

print(f'Junctions skipped: {junctions}')
print(f'Total non-junction files: {len(all_files)}')
print(f'  .md: {len(md_all)}')
print(f'  non-.md: {len(non_md)}')
print()

# MD files categorized
read_md = []
struct_unread_md = []
nonstruct_md = []
for p in md_all:
    rel = p.replace(PREFIX, '').replace('\\', '/')
    if rel in already_read:
        read_md.append(rel)
    elif rel in structure_txt:
        struct_unread_md.append(rel)
    else:
        nonstruct_md.append(rel)

print(f'MD read (v1): {len(read_md)}')
print(f'MD unread in structure.txt: {len(struct_unread_md)}')
print(f'MD not in structure.txt: {len(nonstruct_md)}')
print()

# Group nonstruct by directory
print('=== NON-STRUCTURE-TXT MD distribution ===')
dirs = Counter()
for rel in nonstruct_md:
    parts = rel.split('/')
    if len(parts) >= 3:
        key = '/'.join(parts[1:3])
    else:
        key = parts[0]
    dirs[key] += 1
for k, n in sorted(dirs.items(), key=lambda x: -x[1])[:40]:
    print(f'  {n:4d} {k}')

print()
print('=== NON-STRUCTURE-TXT MD list (first 100) ===')
for r in nonstruct_md[:100]:
    print(f'  {r}')
if len(nonstruct_md) > 100:
    print(f'  ... ({len(nonstruct_md)-100} more)')

# Save them
with open('02_all_md.txt', 'w', encoding='utf-8') as f:
    for r in read_md: f.write('READ\t' + r + '\n')
    for r in struct_unread_md: f.write('STRUCT_UNREAD\t' + r + '\n')
    for r in nonstruct_md: f.write('EXTRA\t' + r + '\n')

import os, stat
from collections import Counter

ROOT = 'C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock'
RP = getattr(stat, 'FILE_ATTRIBUTE_REPARSE_POINT', 0x400)
SKIP_DIRS = {'node_modules', '.git', 'graphify-out', 'dist', '.next'}

md_files = []
total = 0
junctions = 0
for root, dirs, files in os.walk(ROOT, followlinks=False):
    # filter out skip dirs
    dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
    # check if root itself is a junction
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
        total += 1
        if f.endswith('.md'):
            md_files.append(p.replace('\\', '/'))

print(f'Junctions skipped: {junctions}')
print(f'Total non-junction files: {total}')
print(f'Total .md files: {len(md_files)}')
print()

dirs = Counter()
for p in md_files:
    parent = os.path.dirname(p).replace('C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/', '')
    dirs[parent] += 1
for d, n in sorted(dirs.items()):
    print(f'  {n:4d} {d}')

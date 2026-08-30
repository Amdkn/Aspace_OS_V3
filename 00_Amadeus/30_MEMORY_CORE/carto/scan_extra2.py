import os, stat, json
from collections import Counter

ROOT = 'C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock'
PREFIX = 'C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/'
RP = getattr(stat, 'FILE_ATTRIBUTE_REPARSE_POINT', 0x400)
SKIP_DIRS = {'node_modules', '.git', 'graphify-out', 'dist', '.next'}

# Already-read paths (normalized to forward slashes)
with open('02_read.json', encoding='utf-8') as f:
    already_read = set(json.load(f))

# All MD files
all_md = []
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
        rel = p.replace(PREFIX, '').replace('\\', '/')
        all_files.append(rel)
        if f.endswith('.md'):
            all_md.append(rel)

# Categorize extensions
exts = Counter()
for f in all_files:
    ext = os.path.splitext(f)[1] or '(none)'
    exts[ext] += 1
print('=== FILE EXTENSIONS ===')
for e, n in sorted(exts.items(), key=lambda x: -x[1]):
    print(f'  {n:4d} {e}')
print()

# Show non-.md extensions
print('=== NON-MD FILE EXTENSIONS ===')
non_md_exts = Counter()
for f in all_files:
    if not f.endswith('.md'):
        ext = os.path.splitext(f)[1] or '(none)'
        non_md_exts[ext] += 1
for e, n in sorted(non_md_exts.items(), key=lambda x: -x[1]):
    print(f'  {n:4d} {e}')
print()

# Non-MD files outside the-bridge (probably have ontologically relevant content)
print('=== NON-MD files outside the-bridge ===')
for f in all_files:
    if not f.endswith('.md') and 'the-bridge' not in f:
        print(f'  {f}')

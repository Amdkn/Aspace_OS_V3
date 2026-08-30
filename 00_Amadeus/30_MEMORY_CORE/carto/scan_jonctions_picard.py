import os, stat, json

ROOT = r'C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\01_Projects_Picard'

RP = getattr(stat, 'FILE_ATTRIBUTE_REPARSE_POINT', 0x400)
IGNORE_DIRS = {'node_modules', '.git', 'graphify-out', 'dist', '.next', '.turbo', '.cache', '.vercel', 'coverage'}

def is_junction(p):
    try:
        a = os.stat(p).st_file_attributes
        return bool(a & RP)
    except OSError:
        return False

jonctions = []
files_md = 0
files_total = 0
dirs_total = 0

# Walk, but do not descend into IGNORE_DIRS or junctions
for dirpath, dirnames, filenames in os.walk(ROOT, followlinks=False):
    # prune
    new_dirs = []
    for d in dirnames:
        full = os.path.join(dirpath, d)
        if d in IGNORE_DIRS:
            continue  # don't descend, don't count
        if is_junction(full):
            jonctions.append({'name': d, 'parent': dirpath})
            continue
        new_dirs.append(d)
    dirnames[:] = new_dirs

    for f in filenames:
        if f in IGNORE_DIRS:
            continue
        files_total += 1
        if f.endswith('.md'):
            files_md += 1
    dirs_total += len(dirnames)

print(json.dumps({
    'root': ROOT,
    'fichiers_total': files_total,
    'fichiers_md': files_md,
    'dirs_total': dirs_total,
    'jonctions_trouvees': len(jonctions),
    'jonctions_exemples': jonctions[:10],
}, indent=2, ensure_ascii=False))

import json, os, re, sys, collections

CARTO = r"C:\Users\amado\ASpace_OS_V3\00_Amadeus\30_MEMORY_CORE\carto"

def norm(p):
    if not p: return None
    p = p.strip().replace('\\', '/')
    p = re.sub(r'^[A-Za-z]:/', '', p)
    p = re.sub(r'^.*?03_Resources_Geordi/', '03_Resources_Geordi/', p)
    return p.rstrip('/')

covered = set()
for f in ["03_Resources_Geordi.json", "03_Resources_Geordi_v2.json"]:
    fp = os.path.join(CARTO, f)
    if not os.path.exists(fp):
        print("MISSING", f); continue
    d = json.load(open(fp, encoding='utf-8'))
    for t in d.get("types", []):
        for c in t.get("chemins", []) or []:
            n = norm(c)
            if n: covered.add(n)
    for r in d.get("relations", []):
        n = norm(r.get("chemin"))
        if n: covered.add(n)
    for c in d.get("codes", []):
        n = norm(c.get("defini_dans"))
        if n: covered.add(n)
    for c in d.get("contradictions", []):
        for k in ("chemin_a","chemin_b"):
            n = norm(c.get(k))
            if n: covered.add(n)
print("covered paths:", len(covered))

# available = structure.txt lines for seau 03
avail = []
sp = os.path.join(CARTO, "structure.txt")
with open(sp, encoding='utf-8', errors='replace') as fh:
    for line in fh:
        line = line.rstrip('\n')
        if '\t' in line:
            seau, path = line.split('\t', 1)
        else:
            continue
        if '03_Resources_Geordi' not in seau and '03_Resources_Geordi' not in path:
            continue
        avail.append(path)
print("structure.txt lines for geordi:", len(avail))

normavail = {}
for p in avail:
    n = norm(p)
    if n: normavail.setdefault(n, p)

unread = {n: p for n, p in normavail.items() if n not in covered}
print("unread:", len(unread))

# sort by depth then name
def depth(n): return n.count('/')
items = sorted(unread.items(), key=lambda kv: (depth(kv[0]), kv[0]))
with open(os.path.join(CARTO, "03_geordi_w3_unread.txt"), 'w', encoding='utf-8') as fh:
    for n, p in items:
        fh.write(p + "\n")
with open(os.path.join(CARTO, "03_geordi_w3_covered.txt"), 'w', encoding='utf-8') as fh:
    for n in sorted(covered):
        fh.write(n + "\n")
print("top-30 shallowest unread:")
for n, p in items[:30]:
    print(" ", depth(n), n)

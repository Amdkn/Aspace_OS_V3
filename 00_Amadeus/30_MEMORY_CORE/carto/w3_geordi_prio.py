import os, re, collections

CARTO = r"C:\Users\amado\ASpace_OS_V3\00_Amadeus\30_MEMORY_CORE\carto"
unread = [l.rstrip('\n') for l in open(os.path.join(CARTO,"03_geordi_w3_unread.txt"), encoding='utf-8')]

IGNORE = ('aspace-graphify-out','node_modules','/.git/','graphify-out','/dist/','/.next/','_TRASH')

def rel(p):
    p = p.strip().replace('\\','/')
    return re.sub(r'^.*?03_Resources_Geordi/', '', p)

kept=[]
for p in unread:
    r = rel(p)
    if any(x.strip('/') in r for x in IGNORE):
        continue
    kept.append((r,p))
print("after ignore filter:", len(kept))

HIGH = re.compile(r'(^|/)(00_)?(INDEX|_INDEX|INDEX_OF|CANON|ONTOLOG|TAXONOM|ARCHITECTURE|DOCTRINE|SCHEMA|CHARTER|MANIFEST|SPEC|STANDARD|MAP|RUNBOOK)', re.I)
def score(r):
    base = os.path.basename(r)
    d = r.count('/')
    s = d*10
    if HIGH.search(base): s -= 45
    if base.upper().startswith(('_INDEX','00_INDEX','INDEX')): s -= 25
    if re.search(r'(CANON|ONTOLOG|TAXONOM|ARCHITECTURE|DOCTRINE)', base, re.I): s -= 30
    if base.upper()=='README.MD': s += 5
    return s

kept.sort(key=lambda t:(score(t[0]), t[0]))
with open(os.path.join(CARTO,"03_geordi_w3_priority.txt"),'w',encoding='utf-8') as fh:
    for r,p in kept:
        fh.write(p+"\n")
print("=== top 200 priority ===")
for r,p in kept[:200]:
    print(f"{score(r):5d}  {r}")

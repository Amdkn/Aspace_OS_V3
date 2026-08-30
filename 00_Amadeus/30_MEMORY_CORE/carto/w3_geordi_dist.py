import os, re, collections

CARTO = r"C:\Users\amado\ASpace_OS_V3\00_Amadeus\30_MEMORY_CORE\carto"
unread = [l.rstrip('\n') for l in open(os.path.join(CARTO,"03_geordi_w3_unread.txt"), encoding='utf-8')]

def norm(p):
    p = p.strip().replace('\\','/')
    p = re.sub(r'^.*?03_Resources_Geordi/', '', p)
    return p

# distribution by top-2 segments
c2 = collections.Counter()
for p in unread:
    n = norm(p)
    parts = n.split('/')
    key = '/'.join(parts[:2]) if len(parts)>1 else parts[0]
    c2[key]+=1
print("=== unread by 2-level dir (top 60) ===")
for k,v in c2.most_common(60):
    print(f"{v:5d}  {k}")
print()
c1 = collections.Counter()
for p in unread:
    n = norm(p)
    c1[n.split('/')[0]]+=1
print("=== unread by 1-level dir ===")
for k,v in c1.most_common():
    print(f"{v:5d}  {k}")

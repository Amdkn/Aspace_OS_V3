import sys, re, collections
files = []
for batch in ["w3_batch1.txt","w3_batch2.txt","w3_batch3.txt","w3_batch4.txt","w3_batch5.txt","w3_batch6.txt","w3_batch7.txt","w3_batch8.txt","w3_batch9.txt","w3_batch10.txt","w3_batch11.txt"]:
    p = r"C:\Users\amado\AppData\Local\Temp\\" + batch
    try:
        for l in open(p, encoding='utf-8', errors='replace'):
            if l.startswith("### FILE:"):
                files.append(l.split("### FILE:")[1].strip())
    except: pass

print('total reads (with dupes):', len(files))
print('unique files:', len(set(files)))

c = collections.Counter()
for f in files:
    rel = f.replace("\\","/").split("03_Resources_Geordi/")[-1]
    parts = rel.split("/")
    key = parts[0] if parts else "ROOT"
    c[key]+=1
print('reads by top folder:')
for k,v in c.most_common():
    print(f'{v:5d}  {k}')

# count by 2-level
c2 = collections.Counter()
for f in set(files):
    rel = f.replace("\\","/").split("03_Resources_Geordi/")[-1]
    parts = rel.split("/")
    key = '/'.join(parts[:2]) if len(parts)>1 else parts[0]
    c2[key]+=1
print('unique files by 2-level (top 30):')
for k,v in c2.most_common(30):
    print(f'{v:5d}  {k}')

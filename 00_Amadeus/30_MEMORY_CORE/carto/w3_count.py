import sys
rs=set()
for f in ["w3_batch1.txt","w3_batch2.txt","w3_batch3.txt","w3_batch4.txt","w3_batch5.txt","w3_batch6.txt","w3_batch7.txt","w3_batch8.txt","w3_batch9.txt","w3_batch10.txt","w3_batch11.txt"]:
    p = r"C:\Users\amado\AppData\Local\Temp\\"+f
    try:
        for l in open(p, encoding='utf-8', errors='replace'):
            if l.startswith("### FILE:"):
                rel = l.split("### FILE:")[1].strip().replace("\\","/").split("03_Resources_Geordi/")[-1]
                rs.add(rel)
    except: pass
print("total unique files read in v3:", len(rs))
print("first 20:", list(sorted(rs))[:20])
print("last 20:", list(sorted(rs))[-20:])

"""Extract only the title and first paragraph of each file, for breadth over depth."""
import os, sys, re, io
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
BASE = r"C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi"
CARTO = r"C:\Users\amado\ASpace_OS_V3\00_Amadeus\30_MEMORY_CORE\carto"

n = int(sys.argv[1]) if len(sys.argv)>1 else 0
cnt = int(sys.argv[2]) if len(sys.argv)>2 else 200
lim = int(sys.argv[3]) if len(sys.argv)>3 else 20  # very shallow

paths = [l.rstrip('\n') for l in open(os.path.join(CARTO,"03_geordi_w3_priority.txt"), encoding='utf-8')]
for p in paths[n:n+cnt]:
    fp = p if os.path.isabs(p) else os.path.join(BASE, p)
    print("="*100)
    print("### FILE:", p)
    try:
        with open(fp, encoding='utf-8', errors='replace') as fh:
            for i, line in enumerate(fh):
                if i>=lim: print("   ...[truncated]"); break
                # keep only first chars if line is long
                print(line.rstrip()[:200])
    except Exception as e:
        print("   !!ERR", e)

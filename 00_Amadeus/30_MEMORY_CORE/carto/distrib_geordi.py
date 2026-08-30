import sys
from collections import Counter

with open(r'C:/Users/amado/ASpace_OS_V3/00_Amadeus/30_MEMORY_CORE/carto/03_geordi_paths.txt') as f:
    paths = [l.strip() for l in f]

c = Counter()
for p in paths:
    marker = '03_Resources_Geordi'
    i = p.find(marker)
    if i < 0:
        c['<root>'] += 1
        continue
    rest = p[i + len(marker):].replace('\\', '/').lstrip('/')
    parts = rest.split('/')
    if len(parts) > 1 and parts[0]:
        c[parts[0]] += 1
    else:
        c['<root>'] += 1

for k, v in sorted(c.items(), key=lambda x: -x[1]):
    print(f'{v:5d}  {k}')

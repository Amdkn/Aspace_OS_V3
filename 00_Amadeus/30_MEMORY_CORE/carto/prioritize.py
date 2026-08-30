import os
import re
from collections import Counter

paths = []
with open('04_v4_unread.txt', encoding='utf-8') as f:
    for line in f:
        paths.append(line.rstrip('\n'))

print(f'Total unread paths: {len(paths)}')

# Compute depth (number of components)
def depth(p):
    # Remove C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/04_Archives_Data/
    rel = p.replace('C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/04_Archives_Data/', '')
    return rel.count('/')

# Sort by depth (shallow first = high priority)
paths_sorted = sorted(paths, key=lambda p: (depth(p), p))

# Show distribution by depth
depths = Counter(depth(p) for p in paths)
for d in sorted(depths.keys()):
    print(f'  depth {d}: {depths[d]} files')

# Print shallow first
print('\nFirst 100 shallowest paths:')
for i, p in enumerate(paths_sorted[:100]):
    print(f'{i+1:3d} [d{depth(p)}] {p[len("C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/04_Archives_Data/"):]}')

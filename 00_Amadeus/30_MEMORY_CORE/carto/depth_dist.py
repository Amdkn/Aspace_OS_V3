from collections import Counter, defaultdict
depth_files = defaultdict(list)
depths = Counter()
with open('01_Projects_Picard_unread.txt', encoding='utf-8') as f:
    for line in f:
        line = line.strip().replace('\\', '/')
        if not line: continue
        if line.startswith('01_Projects_Picard/'):
            rel = line[len('01_Projects_Picard/'):]
        else:
            rel = line
        parts = [p for p in rel.split('/') if p]
        depth = len(parts)
        depths[depth] += 1
        depth_files[depth].append(line)

for d, c in sorted(depths.items()):
    print(f'depth {d}: {c} files')

for d in sorted(depth_files.keys()):
    print(f'\n--- Depth {d} sample:')
    for f in depth_files[d][:8]:
        print(' ', f)

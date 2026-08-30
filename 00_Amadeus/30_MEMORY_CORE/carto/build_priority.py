all_paths = sorted([l.strip() for l in open('02_Areas_Spock_w3_allpaths.txt', encoding='utf-8') if l.strip()])
covered = set([l.strip() for l in open('02_Areas_Spock_w3_covered.txt', encoding='utf-8') if l.strip()])
unread = [p for p in all_paths if p not in covered]
print('unread total:', len(unread))

keywords = ['INDEX','ARCHITECTURE','STANDARD','DOCTRINE','CANON','SPEC','README','MANIFEST','MAP','ONTOLOGY','TAXONOMY','SCHEMA','CHARTER','RUNBOOK']
priority = []
for p in unread:
    score = 0
    depth = len([x for x in p.replace('\\\\','/').split('/') if x])
    score += max(0, 10 - depth)
    fn = p.rsplit('/',1)[-1]
    fn_up = fn.upper()
    for kw in keywords:
        if kw in fn_up:
            score += 5
            break
    if 'CADENCE' in fn_up or 'W0' in fn_up:
        score += 1
    priority.append((score, p))
priority.sort(reverse=True)
with open('02_Areas_Spock_w3_priority.txt', 'w', encoding='utf-8') as out:
    for s, p in priority:
        out.write(f'{s:3d}\t{p}\n')
for s, p in priority[:30]:
    print(f'{s:3d}  {p}')
print('...')
print('Last 5:')
for s, p in priority[-5:]:
    print(f'{s:3d}  {p}')

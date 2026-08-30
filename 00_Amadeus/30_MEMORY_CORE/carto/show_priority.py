import json
covered = set()
for t in v2_data['types']:
    for p in t['chemins']: covered.add(p)
for r in v2_data['relations']: covered.add(r['chemin'])

priority = []
all_paths = sorted([l.strip() for l in open('02_Areas_Spock_w3_allpaths.txt', encoding='utf-8') if l.strip()])
unread = [p for p in all_paths if p not in covered]
keywords = ['INDEX','ARCHITECTURE','STANDARD','DOCTRINE','CANON','SPEC','README','MANIFEST','MAP','ONTOLOGY','TAXONOMY','SCHEMA','CHARTER','RUNBOOK']
for p in unread:
    score = 0
    depth = len([x for x in p.replace('\\\\','/').split('/') if x])
    score += max(0, 10 - depth)
    fn = p.rsplit('/',1)[-1].upper()
    for kw in keywords:
        if kw in fn:
            score += 5
            break
    if 'CADENCE' in fn or 'W0' in fn:
        score += 1
    priority.append((score, p))
priority.sort(reverse=True)
print('Files remaining:', len(unread))
print('Next 50 priority targets:')
for s, p in priority[25:75]:
    print(f'{s:3d}  {p}')

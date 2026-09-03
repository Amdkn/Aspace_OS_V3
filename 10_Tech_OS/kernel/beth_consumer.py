#!/usr/bin/env python3
"""beth_consumer.py — Le consommateur Beth-Side: pont L1 (Wheel/PARA) -> L2 (mandats Summers).

Regle de polarite (Amadou): une Area GREEN n'est pas un consommateur de compute, c'est un feu vert.
- 8/8 LD GREEN + Rocks PARA declares -> dispatch le prochain Rock en intent L2 (tape)
- 8/8 LD GREEN + 0 Rocks -> intent d'alerte carburant vers Rick (_INBOX/S1_Rick/)
- Tout LD RED -> HALT (rien ne part, l'alerte existe deja)
"""
import glob, json, os, sys, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
V3 = os.path.dirname(HERE)
WHEEL = os.path.join(V3, '20_Life_OS', '22_Wheel_Discovery')
PARA = os.path.join(V3, '20_Life_OS', '24_PARA_Enterprise', 'registre_para.json')
INBOX_RICK = os.path.join(V3, '_INBOX', 'S1_Rick')
INBOX_JERRY = os.path.join(V3, '_INBOX', 'B1_Jerry_Summers')

def wheel_states():
    out = {}
    for f in glob.glob(os.path.join(WHEEL, 'LD0*', 'state.json')):
        d = json.load(open(f, encoding='utf-8'))
        out[d.get('domain', os.path.basename(os.path.dirname(f)))] = d
    return out

def write_intent(path, body):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(body)

def main():
    states = wheel_states()
    greens = sum(1 for v in states.values() if v.get('zora_state') == 'GREEN')
    reds = [k for k, v in states.items() if v.get('zora_state') == 'RED']
    para = json.load(open(PARA, encoding='utf-8')) if os.path.exists(PARA) else {}
    rocks = para.get('projects', []) or []
    print(f'Wheel: {greens}/{len(states)} GREEN | Rocks PARA: {len(rocks)}')

    if reds:
        print(f'HALT: {len(reds)} domaines RED: {reds}. L2 bloque jusqu au retour au vert de Beth.')
        return 1

    today = datetime.date.today().isoformat()

    if not rocks:
        alert = os.path.join(INBOX_RICK, f'intent-alerte-carburant-{today}.md')
        if os.path.exists(alert):
            print('Alerte carburant deja posee aujourd hui:', alert)
            return 0
        body = f"""# INTENT: alerte-carburant-L2
**Layer:** L1->L2
**Originator:** Beth (consumer automatique)
**Date:** {today}
**Statut:** DRAFT

## Irritant reel
Les 8 domaines de la Wheel sont GREEN et en load LOW: le systeme metabolique a de la
capacite de predation disponible. MAIS le registre PARA ne contient AUCUN Rock Summers
declare (projects: 0). L2 (Clara/Nardole/Bill + Doctor 12) n a rien a manger.

## Resultat vise (mesurable)
Amadou declare au moins un Rock Summers 12WY dans le registre PARA
(24_PARA_Enterprise/registre_para.json -> projects[]), avec un critere de valeur
mesurable (ex: revenue, artefact livre, utilisateur actif).

## Contraintes non-negociables
- Chaque Rock doit avoir un critere mesurable (pas de TODO)
- Blast radius: un Rock = un cycle 12WY, pas une vision

## Definition of Done
- [ ] registre_para.json contient au moins 1 project avec critere mesurable
- [ ] Beth consumer dispatch le Rock en intent L2 au prochain tick
"""
        write_intent(alert, body)
        print(f'ALERTE CARBURANT posee: {alert}')
        return 0

    pending_rocks = [r for r in rocks if not r.get('dispatched_to_l2')]
    if not pending_rocks:
        print('Tous les Rocks sont deja dispatches en L2.')
        return 0

    rock = pending_rocks[0]
    print(f'DISPATCH L2 du Rock: {json.dumps(rock, ensure_ascii=False)[:200]}')
    slug = str(rock.get('name', 'rock')).lower().replace(' ', '-')[:40]
    out = os.path.join(INBOX_JERRY, f'intent-rock-{slug}-{today}.md')
    body = f"""# INTENT: rock-summers-{slug}
**Layer:** L1->L2
**Originator:** Beth (consumer automatique, source: PARA Rock 12WY)
**Date:** {today}
**Statut:** DRAFT

## Irritant reel
Rock Summers declare par Amadou dans PARA, GREEN sur la Wheel, en attente de
production de valeur L2 (Clara spec -> Nardole build -> Doctor 12 detach).

## Rock
{json.dumps(rock, ensure_ascii=False, indent=1)}

## Definition of Done
- [ ] Le Rock devient un work L2 dans uc.db via ruban admis au portier
- [ ] Critere de valeur du Rock atteint (preuve d'environnement)
"""
    write_intent(out, body)
    print(f'INTENT L2 pose: {out}')
    return 0

if __name__ == '__main__':
    sys.exit(main())

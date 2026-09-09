#!/usr/bin/env python3
"""beth_consumer.py — Le consommateur Beth-Side: pont L1 (Wheel/PARA) -> L2 (mandats Summers).

Regle de polarite (Amadou): une Area GREEN n'est pas un consommateur de compute, c'est un feu vert.
- 8/8 LD GREEN + Rocks PARA declares -> dispatch le prochain Rock en intent L2 (tape)
- 8/8 LD GREEN + 0 Rocks -> intent d'alerte carburant vers Rick (_INBOX/S1_Rick/)
- Tout LD RED -> HALT (rien ne part, l'alerte existe deja)
"""
import glob, json, os, sys, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
V3 = os.path.dirname(os.path.dirname(HERE))
WHEEL = os.path.join(V3, '20_Life_OS', '22_Wheel_Discovery')
PARA = os.path.join(V3, '20_Life_OS', '24_PARA_Enterprise', 'registre_para.json')
INBOX_RICK = os.path.join(V3, '_INBOX', 'S1_Rick')
INBOX_JERRY = os.path.join(V3, '_INBOX', 'B1_Jerry_Summers')
ADMIT_JERRY = os.path.join(V3, '_INBOX', '_admis', 'B1_Jerry_Summers')
REFUS_JERRY = os.path.join(V3, '_INBOX', '_refuses', 'B1_Jerry_Summers')

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
        body = f"""---
title: "Alerte carburant L2 : 0 Rock PARA declare, L2 n a rien a manger"
date: {today}
layer: L1->L2
statut: FROZEN
type: intent
originator: Beth (consumer automatique)
---

# INTENT: alerte-carburant-L2
**Layer:** L1->L2
**Date:** {today}
**Statut:** FROZEN

## Irritant reel
Les 8 domaines de la Wheel sont GREEN et en load LOW: le systeme metabolique a de la
capacite de predation disponible. MAIS le registre PARA ne contient AUCUN Rock Summers
declare (projects: 0). L2 (Clara/Nardole/Bill + Doctor 12) n a rien a manger.

## Résultat visé (mesurable)
Amadou declare au moins un Rock Summers 12WY dans le registre PARA
(24_PARA_Enterprise/registre_para.json -> projects[]), avec un critere de valeur
mesurable (ex: revenue, artefact livre, utilisateur actif).

## Contraintes non-negociables
- Chaque Rock doit avoir un critere mesurable (un chiffre, pas une intention)
- Blast radius: un Rock = un cycle 12WY, pas une vision

## Definition of Done
- [ ] registre_para.json contient au moins 1 project avec critere mesurable
- [ ] Beth consumer dispatch le Rock en intent L2 au prochain tick
"""
        write_intent(alert, body)
        print(f'ALERTE CARBURANT posee: {alert}')
        return 0

    def rock_slug(r):
        return str(r).lower().replace(' ', '-')[:40]

    # projects[] contient des strings (contrat verify_para.py: entrees mesurees sur disque).
    # Dedup sur toute la trace inbox: file vivante + _admis (intent pris en ruban)
    # + _refuses (portier) — repertoires FRERES du portier, pas enfants
    # (_INBOX/_refuses/B1_Jerry_Summers/). Sans ca, un intent refuse puis deplace
    # re-part en boucle: emit -> REFUS -> deplacement -> re-emit (incident 2026-09-04).
    dispatched = set()
    for sub in (INBOX_JERRY, ADMIT_JERRY, REFUS_JERRY):
        dispatched.update(os.path.basename(p) for p in glob.glob(os.path.join(sub, 'intent-rock-*.md')))
    pending_rocks = [r for r in rocks if not any(d.startswith(f'intent-rock-{rock_slug(r)}-') for d in dispatched)]
    if not pending_rocks:
        print('Tous les Rocks sont deja dispatches en L2.')
        return 0

    rock = pending_rocks[0]
    slug = rock_slug(rock)
    rock_md = os.path.join(os.path.dirname(PARA), '01_Projects_Picard', str(rock), 'ROCK.md')
    rock_ref = rock_md if os.path.exists(rock_md) else '(ROCK.md non trouve dans 01_Projects_Picard)'
    print(f'DISPATCH L2 du Rock: {rock}')
    out = os.path.join(INBOX_JERRY, f'intent-rock-{slug}-{today}.md')
    # Format conforme au portier (gate.py test_intent): frontmatter title, sections
    # Irritant / Resultat vise / Contraintes / DoD verifiable, statut FROZEN —
    # l'Originator (Beth, ce consumer) est la seule entite autorisee a geler.
    body = f"""---
title: "Rock {rock} dispatche en L2 : ruban admis -> work uc.db -> valeur ROCK.md"
date: {today}
layer: L1->L2
statut: FROZEN
type: intent
originator: Beth (consumer automatique, source: PARA Rock 12WY)
rock: {rock}
---

# INTENT: rock-summers-{slug}
**Layer:** L1->L2
**Date:** {today}
**Statut:** FROZEN

## Irritant reel
Rock Summers declare par Amadou dans PARA, GREEN sur la Wheel, en attente de
production de valeur L2 (Clara spec -> Nardole build -> Doctor 12 detach).

## Rock
{rock}

## Fiche Rock
{rock_ref}

## Résultat visé (mesurable)
Un work L2 existe dans uc.db pour ce Rock, issu d un ruban admis au portier,
et le critere de valeur de ROCK.md a sa preuve d environnement: verifier du
domaine rc=0 (ex: BUSINESS_OS_OK / PULSE_OK).

## Contraintes non-negociables
- Blast radius: un Rock = un cycle 12WY, pas une vision
- Loi de prediction: prediction pre-enregistree avant toute execution
- Loi de detachement: done seulement depuis review, apres preuve

## Definition of Done
- [ ] Le Rock devient un work L2 dans uc.db via ruban admis au portier
- [ ] Critere de valeur du Rock atteint (preuve d'environnement)
"""
    write_intent(out, body)
    print(f'INTENT L2 pose: {out}')
    return 0

if __name__ == '__main__':
    sys.exit(main())

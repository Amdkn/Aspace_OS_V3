---
type: Concept
title: B3 cycle — 5 scrums par semaine, une action exécutable par jour ouvré
description: La cadence B3 canonique : 5 scrums/semaine (un par jour ouvré), pas une moyenne, pas un sprint. Chaque Scrum = une action exécutable qui dépend d'un sprint B2 qui dépend d'un rock B1. Le Scrum ne se confond pas avec le ticket, ni avec le rapport. C'est le grain minimal de traçabilité B3.
tags: [b3, scrum, cadence, cycle, quotidien, action, executable, e-myth]
generated: { by: minimax-m3, at: 2026-08-19T02:55:00Z }
verified:
  - { by: process:lecture-triplets-v3, at: 2026-08-19T02:55:00Z }
  - { by: process:synthese-pulse-b3-tour-1, at: 2026-08-19T02:55:00Z }
sources:
  - id: triplet-cycle-b3
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: v3-business triplets (ligne 11 — cycle-quotidien B3)
    last_modified: 2026-08-17
  - id: triplet-dependance-scrum
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: v3-business triplets (ligne 13 — B3 dépend du sprint B2)
    last_modified: 2026-08-17
  - id: triplet-pyramide-e-myth
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: v3-business triplets (ligne 2 — cascade E-Myth 12WY → 4 sprints → 5 scrums)
    last_modified: 2026-08-17
  - id: fractal-b1b2b3
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/areas/fractal-b1b2b3-architecture.md"
    title: Le fractal B1/B2/B3 — Areas perpétuelles vs Summer's Verse datées
    last_modified: 2026-08-17
  - id: b1-cadence
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b1/b1-twelve-weeks-year-cadence.md"
    title: B1 — 12WY cadence (cœur E-Myth)
    last_modified: 2026-08-19
okf_version: "0.2"
---

# B3 cycle — 5 scrums par semaine, une action exécutable par jour ouvré

> La cadence B3 est dérivée de la cascade E-Myth : 12WY (B1) → 4
> sprints/mois (B2) → **5 scrums/semaine** (B3). Le triplet v3 ligne
> 11 est explicite : *« Chaque technicien tire 5 scrums par semaine, un
> par jour ouvré — une action exécutable, pas un plan. »* Ce concept
> pose ce qu'est un scrum, ce qu'il n'est pas, et comment il se
> rattache aux grains amont.

## Pourquoi 5, pas 7

L'amplitude n'est pas 7 (jours calendaires). C'est 5 (jours ouvrés).
Trois raisons :

1. **Cohérence avec E-Myth.** Le B2 sprint est hebdomadaire
   (lundi-d-vendredi), pas week-end inclus. Aligner B3 sur 5 garde la
   cascade **sans couture temporelle**.
2. **Lisibilité.** Un scrum = un jour ouvré = une action terminée. Si
   le B3 écrit un scrum le samedi, il a soit sauté un cycle (vendredi
   non tenu), soit fait du zèle hors-cadre.
3. **Traçabilité.** Le squad lead peut compter les scrums d'une semaine
   et savoir immédiatement si un B3 a tenu son rythme — 5/5 = tenu,
   4/5 = un écart, ≤ 3 = STOP_CONDITION à investiguer.

## Ce qu'est un scrum (et ce qu'il n'est pas)

### C'est

- **Une action exécutable**, pas un plan. *« Lancer la migration X »*
  est un scrum ; *« Préparer la migration X »* ne l'est pas.
- **Une action terminée dans la journée** (ou un `BLOCKED` /
  `AT_RISK` consigné, cf. `b3-veto-and-signal-vocabulary.md`).
- **Attachée à un sprint B2 en cours** (cf. triplet v3 ligne 13 :
  *« Le technicien dépend du sprint hebdomadaire de son VP : un scrum
  sans sprint est du geste sans cause. »*).
- **Consignée dans `SCRUMS.md`** avec : date, action, signal (ON_TRACK
  / AT_RISK / BLOCKED / DONE), preuve jointe si `DONE` (cf.
  `b3-proof-path-4-formes.md`).

### Ce n'est pas

- Un ticket JIRA / Linear (le scrum est **plus petit** — un ticket peut
  couvrir plusieurs scrums ; un scrum est l'unité quotidienne).
- Un rapport de fin de semaine (le rapport est en B2 — SPRINTS.md).
- Un stand-up meeting (le scrum est **écrit**, pas dit).
- Une moyenne (*« en moyenne 3 scrums/semaine »* n'a pas de sens —
  c'est 5 par construction).

## Le format canonique d'un scrum

Chaque entrée de `SCRUMS.md` a 6 champs :

```
SCRUM_YYYY-MM-DD
  by:      <b3-handle>
  for:     <sprint_id B2> (le sprint en cours dont dépend ce scrum)
  action:  <verbe à l'infinitif + objet, en 1 ligne>
  signal:  ON_TRACK | AT_RISK | BLOCKED | DONE
  proof:   <chemin vers la preuve si signal=DONE> | <n/a>
  notes:   <1 ligne max — uniquement si signal ≠ ON_TRACK>
```

### Critère d'action exécutable

`action` doit commencer par un **verbe d'exécution**, pas un verbe
d'intention. Verbes d'exécution acceptés : *lancer, migrer, déployer,
écrire, corriger, tester, merger, vérifier, capturer, signer, …*
Verbes d'intention refusés : *préparer, étudier, planifier, réfléchir,
discuter, voir, …*

Si le B3 ne peut pas formuler un verbe d'exécution, son action n'est
pas un scrum — c'est un sous-objectif qui doit être décomposé.

## Le rattachement au sprint (grain amont)

Le scrum dépend du sprint B2 qui dépend du rock B1 :

```
Rock B1 (mensuel)
  └── Sprint B2 (hebdomadaire, 4 par mois)
        └── Scrum B3 (quotidien, 5 par sprint)
```

Un scrum qui ne se rattache à aucun sprint actif est **du geste sans
cause** (triplet v3 ligne 13). Le B3 ne l'écrit pas — il escalade au
squad lead pour clarification.

L'inverse est aussi vrai : un sprint B2 qui n'a aucun scrum B3 sur 2
jours consécutifs signale un **blocage silencieux** (le B3 a peut-être
quitté le job). Le squad lead escalade à B2.

## La cadence en pratique : la pyramide temporelle

| Grain | Cadence | Owner | Artefact |
|---|---|---|---|
| 12WY | 3 cycles/an | B1 (Summer / Jerry) | `ROCKS.md` (1 rock/mois) |
| Sprint | 4/mois | B2 (VP / Captain) | `SPRINTS.md` (1 sprint/semaine) |
| **Scrum** | **5/semaine** | **B3 (Technicien)** | **`SCRUMS.md` (1 action/jour)** |

Cette pyramide est **non négociable** : changer la cadence d'un grain
casse la cascade. Un B3 qui veut travailler en sprints de 2 semaines
**rompt le rythme** de son B2 owner.

## Anti-patterns

1. **B3 qui batch ses scrums en fin de semaine.** *« J'ai fait 5 choses
   cette semaine »* n'est pas 5 scrums. La cadence est quotidienne, pas
   hebdomadaire.
2. **B3 qui rate un scrum sans signal.** Un jour sans scrum = `BLOCKED`
   ou `AT_RISK` consigné. Un jour sans SCRUMS.md et sans signal = drift
   silencieux, à signaler au squad lead.
3. **B3 qui fait 7 scrums/semaine.** Le 6ᵉ et le 7ᵉ sortent du cadre
   ouvré — soit le B3 fait du zèle (à signaler), soit le B2 a sous-estimé
   la charge du sprint (à arbitrer en B2, pas absorbé en silence par
   le B3).
4. **B3 qui ne signale pas un `BLOCKED` parce que « ça va passer ».**
   Cf. `b3-hole-signaling-doctrine.md` — un trou ou un blocker non
   signalé est un trou comblé en silence.

## Lien avec les 5 méthodes

| Méthode | Application à la cadence B3 |
|---|---|
| Examen préalable | Avant de rendre un scrum `DONE`, l'examen est lancé si le périmètre touche du code. Sortie jointe au SCRUM. |
| Agent relecteur | Pour les scrums qui clôturent un mini-livrable, peer-relecteur en contexte vierge. |
| Bacs à sable | Tant que le squad B3 est seul sur son périmètre, cloisonnement par brief suffit. Worktree seulement si plusieurs B3 du squad convergent. |
| Goodhart | **Le compteur de scrums n'est pas la métrique de performance.** Un B3 qui sort 5 scrums / semaine sans preuve est moins utile qu'un B3 qui sort 1 scrum `DONE` avec capture + diff. La cadence est **structurelle**, pas **productiviste**. |
| Tension Q/Q | Un scrum long avec preuve > 5 micro-scrums sans preuve. La cadence est un plancher de **traçabilité**, pas un plafond de **quantité**. |

## Source du concept

- `triplet v3 ligne 11` — *« Chaque technicien tire 5 scrums par semaine,
  un par jour ouvré — une action exécutable, pas un plan. »*
- `triplet v3 ligne 13` — *« Le technicien dépend du sprint hebdomadaire
  de son VP : un scrum sans sprint est du geste sans cause. »*
- `triplet v3 ligne 2` — *« cascade E-Myth : B1 Summers (1 rock/mois,
  3/12WY) → B2 les 8 VP (4 sprints/mois) → B3 les 53 techniciens (5
  scrums/semaine). »*
- `fractal-b1b2b3-architecture.md` §« Le fractal compounds » — le grain
  temporel Area (perpétuel) vs Project (daté) impose cette cascade.

## Liens

- [[b3-jtbd-packet-reception-checklist]] — le scrum dépend d'un packet
  JTBD reçu et accepté
- [[b3-peer-unblock-protocol]] — un scrum `BLOCKED` peut être un
  peer-unblock ouvert
- [[b3-veto-and-signal-vocabulary]] — le scrum porte un des 4 signaux
- [[b3-hole-signaling-doctrine]] — un scrum `BLOCKED` par trou de
  paquet
- [[b3-proof-path-4-formes]] — un scrum `DONE` porte une preuve
- [[fifty-three-b3-agent-roster]] — qui tient les SCRUMS.md

## Note de confiance

**Confirmé par machine.** La cadence 5/semaine est verbatim du
triplet v3 ligne 11. La cascade 12WY → 4 sprints → 5 scrums est dans
le triplet v3 ligne 2. Le rattachement scrum → sprint est dans le
triplet v3 ligne 13.

**Convergence avec B1** : le concept `b1-twelve-weeks-year-cadence.md`
pose la même cascade du côté B1. Les deux lectures (B1 amont et B3
aval) se rejoignent sur le même rythme.
---
type: Concept
title: B3 peer-unblock — l'escalader entre pairs avant d'escalader à B2
description: Le fractal B1/B2/B3 pose l'invariant : un B3 qui bloque escalade d'abord à ses pairs (squad lead, autres B3 du squad, ou cross-squad via DOFLD), pas à B2. Format canonique du peer-unblock : ping structuré, contexte, ce qui est tenté, ce qui bloque, ce qui est demandé. Anti-pattern : l'escalade B2 sans tentative de pair.
tags: [b3, peer-unblock, escalade, squad, dofld, anti-pattern, escalation-ladder]
generated: { by: minimax-m3, at: 2026-08-19T02:15:00Z }
verified:
  - { by: process:lecture-fractal-b1b2b3, at: 2026-08-19T02:15:00Z }
  - { by: process:synthese-pulse-b3-tour-1, at: 2026-08-19T02:15:00Z }
sources:
  - id: fractal-b1b2b3
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/areas/fractal-b1b2b3-architecture.md"
    title: Le fractal B1/B2/B3 — Areas perpétuelles vs Summer's Verse datées
    last_modified: 2026-08-17
  - id: omk-business-os
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/omk-business-os.md"
    title: OMK Business OS
    last_modified: 2026-08-17
  - id: triplet-pyramide-l0
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: v3-business triplets (ligne 39 — pyramide L0 ≥ L1 > L2)
    last_modified: 2026-08-17
  - id: b1-stop-conditions
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b1/b1-stop-conditions-escalier.md"
    title: B1 stop conditions et escalier canonique
    last_modified: 2026-08-19
okf_version: "0.2"
---

# B3 peer-unblock — l'escalader entre pairs avant d'escalader à B2

> L'escalier canonique du fractal est *« B3 → (peer-unblock d'abord) →
> B2 owner → B1 (Jerry/Summer) → B1 gatekeepers (Rick/Morty) → A0
> Amadeus. »* Ce concept pose le **premier échelon** : l'escalade entre
> pairs B3, **avant** que B2 ne soit sollicité.

## Pourquoi peer-unblock d'abord

Trois raisons tirées du fractal et de la doctrine Coach OS :

1. **B2 a 8 domaines à tenir.** Un B2 qui reçoit une question que les
   pairs B3 peuvent résoudre consomme sa bande passante d'arbitrage
   meso. Le B2 Council arbitre les conflits cross-domaines — pas les
   bogues tactiques qu'un autre B3 sait lever.
2. **Le squad lead a le contexte de squad.** Le `guardian_lead` /
   `squad_lead` porte la vision d'ensemble des jobs actifs dans le
   squad. Il sait si un autre B3 a déjà résolu le problème, ou si le
   reorder des jobs débloque la situation sans effort nouveau.
3. **L'inverse est plus coûteux.** Un B3 qui escalade à B2 *sans* avoir
   tenté le pair montre qu'il n'a pas cherché à s'aider du squad. Le B2
   peut refuser d'arbitrer et renvoyer au pair. Coût net : une itération
   perdue et un signal de dépendance mal placé.

## Le format canonique du peer-unblock

Un ping pair ne se rédige pas en prose libre. Il suit 5 champs, dans
cet ordre. L'ordre n'est pas décoratif — il sert à ce que le pair
puisse répondre sans aller chercher du contexte :

```
SQUAD_UNBLOCK_REQUEST
  from:    <b3-handle>  (ex. Rocket, sous Guardians of the Galaxy)
  to:      <peer-handle | squad_lead | DOFLD-pool>
  context: <job_id + état d'avancement en 1 phrase>
  tried:   <ce qui a déjà été tenté, en liste>
  blocked: <pourquoi ça bloque, en 1 phrase>
  ask:     <ce qui est demandé au pair, en 1 phrase>
```

### Critère de complétude

Si le B3 qui envoie ne peut pas remplir `tried` (rien tenté) ou `blocked`
(pas identifié), il n'a pas fini de chercher. Il **retarde** l'envoi
d'un cycle et complète les champs.

## Les 4 niveaux de pair-unblock

Du moins coûteux au plus coûteux :

| Niveau | Cible | Quand l'utiliser |
|---|---|---|
| **Pair du squad** | un autre B3 du même squad (ex. StarLord si le B3 est Rocket) | Le pair a la même doctrine et probablement le même type de blockers. |
| **Squad lead** | `guardian_lead` du packet JTBD | Le pair n'a pas le contexte d'ensemble, le squad lead l'a. |
| **Cross-squad via DOFLD** | pool B3 transverse (DOFLD = Domain-Owner-Federated Lookup Dispatch) | Le problème traverse les squads (ex. un blocker Legal qui touche un job Growth). |
| **Escalade B2 owner** | le B2 captain du domaine | Dernier recours pair : si les pairs n'ont pas résolu en 1 cycle, escalader au B2. |

Le niveau 4 n'est **pas** un pair-unblock — c'est l'escalade B2.
Chronométrer : un peer-unblock resté sans réponse pendant **1 cycle**
(scrum = 1 jour ouvré, sprint = 1 semaine) déclenche l'escalade B2.

## Le DOFLD — Domain-Owner-Federated Lookup Dispatch

Le DOFLD est l'annuaire qui permet à un B3 de trouver le bon pair
cross-squad sans connaître tous les squads. Son format :

```
DOFLD.lookup(<domaine>, <besoin>) → [<b3_handle>, <squad>, <contact>]
```

Il est tenu par **chaque squad lead** (qui publie les spécialités de
son squad) et **lu** par les autres squads. La source canonique vit
dans le packet JTBD-001 du domaine (section `supports`) et dans le
roster (`01_B3_AGENT_ROSTER.md`).

## Anti-patterns

Trois anti-patterns sont à surveiller dans `SCRUMS.md` (le B3 qui les
emploie le consigne et corrige) :

1. **Escalade B2 sans tentative pair.** Le B3 qui remonte *« bloqué sur
   X »* à B2 sans avoir listé `tried` dans son ping est en infraction. Le
   B2 peut refuser et demander le ping pair d'abord.
2. **Ping pair en prose libre.** *« Salut, j'ai un souci, tu peux
   m'aider ? »* n'est pas un ping pair. Le pair ne peut pas répondre
   sans reconstruire le contexte.
3. **Pair sollicité hors squad sans passer par DOFLD.** Un B3 qui
   contacte directement un agent d'un autre squad sans DOFLD casse la
   trace d'audit et le squad lead de l'autre squad ne voit pas la
   sollicitation.

## L'inverse : quand **ne pas** peer-unblock

Le peer-unblock a un coût (1 cycle de latency). Il ne s'applique pas
quand :

- **Le blocker est un veto.** Un B2 (Batman, Aquaman, etc.) a posé un
  veto (`hasVetoOver` dans `ORG.json`) — c'est une décision B2, pas un
  blocage technique. L'escalade directe à B2 est la bonne route.
- **Le blocker est un emergency trigger B1.** Risque Nord Star, risque
  légal, risque financier — l'escalade saute au B1 (cf.
  `b1-stop-conditions-escalier.md`).
- **Le packet est incomplet.** Le B3 ne peer-unblock pas un trou de
  paquet — il applique `b3-hole-signaling-doctrine.md` et signale à B2.

## Lien avec l'examen et le relecteur

Les 5 méthodes autonomie-agents s'appliquent **après** que le peer a
débloqué. Une fois le pair-unblock résolu, le B3 reprend son travail et
**avant** de rendre son livrable :

- lance l'examen préalable (cf. `examen-prealable.md`) ;
- joint un peer-relecteur (cf. `agent-relecteur-mandat.md`) ;
- consigne le pair-unblock dans `SCRUMS.md` (qui, quand, quoi).

## Sources

- `fractal-b1b2b3-architecture.md` §« L'escalier d'escalade (canonique) »
  — *« B3 → (peer-unblock d'abord) → B2 owner. »*
- `omk-business-os.md` §« Triptyque V4 » — la structure 8 squads / 8 B2
  qui sous-tend le DOFLD.
- `triplet v3 ligne 39` — *« La pyramide L0 ≥ L1 > L2 impose que L0 a
  autorité absolue, L1 a le veto (Beth), L2 exécute dans ces bornes. »*
  Cette règle de multiplicativité des autorités vaut aussi pour les
  pairs : un pair senior n'écrase pas un pair junior sur un scope
  qu'il ne maîtrise pas.

## Liens

- [[b3-jtbd-packet-reception-checklist]] — le paquet que le B3 essaie
  d'exécuter pendant que le pair-unblock est en cours
- [[b3-hole-signaling-doctrine]] — quand le blocker n'est pas un pair
  mais un trou dans le paquet
- [[b3-veto-and-signal-vocabulary]] — quand le blocker est un veto B2
- [[b3-proof-path-4-formes]] — ce que le B3 rend après le pair-unblock
- [[fifty-three-b3-agent-roster]] — qui sont les pairs

## Note de confiance

**Confirmé par machine.** L'escalier canonique est explicite dans le
fractal, ligne par ligne. Le format 5 champs est dérivé de la doctrine
« Liste, pas prose » du relecteur (`agent-relecteur-mandat.md`). Le
DOFLD est nommé dans le fractal et la structure OMK, sans format
canonique publié ailleurs.
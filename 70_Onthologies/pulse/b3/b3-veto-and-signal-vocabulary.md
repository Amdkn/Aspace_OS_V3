---
type: Concept
title: B3 veto and signal vocabulary — le vocabulaire B3 ↔ B2
description: Les 8 vetos B2 (un par VP, déjà documentés en triplets Coach OS), les signaux B2 → B3 (READY / NEEDS_X / BLOCKED_X par domaine), et les signaux B3 → B2 (ON_TRACK / AT_RISK / BLOCKED / DONE). Le B3 doit connaître les deux côtés : ce qu'il reçoit (la gate) et ce qu'il émet (le statut).
tags: [b3, b2, veto, signal, vocabulary, status, gate, ready, blocked, orga]
generated: { by: minimax-m3, at: 2026-08-19T02:35:00Z }
verified:
  - { by: process:lecture-triplets-v3, at: 2026-08-19T02:35:00Z }
  - { by: process:synthese-pulse-b3-tour-1, at: 2026-08-19T02:35:00Z }
sources:
  - id: triplet-vetos-b2
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: v3-business triplets (lignes 23-30 — les 8 hasVetoOver B2)
    last_modified: 2026-08-17
  - id: eight-domain-wheel
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/eight-domain-avengers-wheel.md"
    title: Eight Domain Avengers Wheel — les 8 gates READY/BLOCKED par domaine
    last_modified: 2026-08-17
  - id: triplet-cadence
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: v3-business triplets (ligne 41 — B3 interdit-combler-trou)
    last_modified: 2026-08-17
  - id: harmonization-matrix
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/areas/business-wheel-harmonization-matrix.md"
    title: Harmonisation de la wheel — pair checks et red flags
    last_modified: 2026-08-17
okf_version: "0.2"
---

# B3 veto and signal vocabulary — le vocabulaire B3 ↔ B2

> Un B3 parle à B2 dans un vocabulaire fermé. Trois couches : les
> **8 vetos B2** que le B3 doit savoir reconnaître, les **signaux B2 → B3**
> qui ouvrent / ferment les portes du domaine, et les **signaux B3 → B2**
> qui rendent compte du statut d'exécution. Sans ce vocabulaire, le B3
> ne sait pas ce qu'il peut faire, ce qu'il doit attendre, et ce qu'il
> doit dire.

## Couche 1 — Les 8 vetos B2

Chaque B2 captain tient un veto documenté dans `ORG.json` (triplets
v3 lignes 23-30). Le B3 doit connaître celui de **son** B2 owner, plus
les vetos des B2 transverse (Batman Ops, Aquaman Legal) qui peuvent
bloquer un job B3 même hors de leur squad.

| B2 | Veto (`hasVetoOver`) | Ce que le B3 doit faire |
|---|---|---|
| **Green Lantern** (People) | recrutement sans mandat | Ne pas créer de rôle / profil sans mandat écrit + critère de sortie vérifiable. |
| **Batman** (Ops) | procédure sans condition d'arrêt | Ne pas démarrer une boucle qui n'a pas de `stop_condition` écrit. |
| **Flash** (Product) | offre dépersonnalisée | Ne pas lier la valeur d'une offre à une personne nommée. |
| **Martian Manhunter** (Sales, legacy) | proposition sans reformulation | Ne pas envoyer de proposition avant reformulation validée par le client. |
| **Superman** (Growth / Brand) | promesse non tenue | Ne pas promettre publiquement ce que la delivery ne tient pas. |
| **Wonder Woman** (Finance) | dépense récurrente sans ROI | Ne pas engager de dépense récurrente sans date de revue + métrique de retour. |
| **Cyborg** (IT) | cloud-only sans sortie | Ne pas choisir un fournisseur cloud-only sans chemin de sortie documenté. |
| **Aquaman** (Legal) | engagement sans périmètre | Ne pas démarrer une prestation sans accord écrit sur périmètre + propriété du livrable. |

**Note nomenclature** : `eight-domain-avengers-wheel.md` signale que
le captain Sales **Martian Manhunter** est renommé **JohnJones** en W40
V4. Le B3 doit utiliser le nom W40 V4 dans les nouveaux packets ; les
anciens dossiers OMK portent encore l'ancien nom. **Je n'ai pas
tranché** le statut canonique de la nomenclature — c'est une dette de
gouvernance B1, pas un concept B3.

### Pourquoi le B3 doit connaître les 8, pas un seul

Le job B3 **traverse** souvent les domaines. Un B3 sous Wonder Woman
(Finance) qui touche à la donnée client doit aussi connaître le veto
Aquaman (Legal) sur les engagements. Un B3 sous Flash (Product) qui
engage un fournisseur cloud touche le veto Cyborg. Le **vocabulaire
transverse** est ce qui distingue un B3 opérationnel d'un B3
naïf.

### Quand un veto s'applique

Le veto n'est pas une option — c'est une règle d. Un B3 qui s'appr
re
à enfreindre un veto **escalade à B2** avant d'agir, pas après. Le B2
peut :
- confirmer le veto et **bloquer** le job ;
- **assouplir** le veto avec une exception documentée ;
- **déléguer** le veto à un autre B2 si le job a changé de domaine.

L'escalade prend la forme d'un ping pair (cf.
`b3-peer-unblock-protocol.md`) si le veto est connu du squad, ou d'un
ping B2 direct si le veto est nouveau pour le B3.

## Couche 2 — Les signaux B2 → B3 (gates de domaine)

Chaque B2 émet un signal de **gate** par domaine, dans un vocabulaire
fermé à 3 états (READY / NEEDS_X / BLOCKED_X). Le tableau vient de
`eight-domain-avengers-wheel.md` :

| B2 | READY | NEEDS_X | BLOCKED_X |
|---|---|---|---|
| Growth (Superman) | `GROWTH_READY` | `NEEDS_SIGNAL` | `BLOCKED_PROMISE` |
| Sales (JohnJones) | `SALES_READY` | `NEEDS_QUALIFICATION` | `BLOCKED_COMMITMENT` |
| Product (Flash) | `PRODUCT_READY` | `NEEDS_SCOPE` | `BLOCKED_DELIVERY` |
| Ops (Batman) | `LAUNCH_READY` (transverse) | — | — |
| IT (Cyborg) | `SYSTEM_READY` | `NEEDS_SYSTEM_OWNER` | `QUARANTINE` |
| Finance (Wonder Woman) | `FINANCE_READY` | `NEEDS_MODEL` | `BLOCKED_LEAKAGE` |
| People (Green Lantern) | `ASSIGNED` | `NEEDS_OWNER` | `DLQ` |
| Legal (Aquaman) | `LEGAL_READY` | `NEEDS_REVIEW` | `BLOCKED_RISK` |

**Comment le B3 les reçoit** : via le packet JTBD-001 (§« premier
experiment RICE + lead/lag indicators + build gates »), ou via un ping
B2 direct quand le statut change en cours d'exécution. Le B3 qui voit
passer sa gate de `READY` à `BLOCKED_X` **s'arrête** et escalade.

## Couche 3 — Les signaux B3 → B2 (statut d'exécution)

Le B3 émet un signal de **statut** à chaque SCRUM (cf.
`b3-cycle-scrums-five-per-week.md`). 4 états, dans un vocabulaire
fermé :

| Signal | Quand | Action B2 |
|---|---|---|
| `ON_TRACK` | Le SCRUM est dans le plan, pas de blocker | RAS — le B2 suit le SCRUM suivant. |
| `AT_RISK` | Le SCRUM dérape mais le B3 a un plan correctif | Le B2 surveille ; peut demander un ping pair ou une re-priorisation. |
| `BLOCKED` | Le SCRUM est arrêté sur un blocker (pair, veto, trou de paquet) | Le B2 arbitre — soit pair-unblock upward, soit escalation, soit intervention directe. |
| `DONE` | Le job est livré avec preuve (cf. `b3-proof-path-4-formes.md`) | Le B2 marque la gate à `READY` pour le suivant. |

**Le signal n'est pas optionnel** : un SCRUM sans signal est un
SCRUM invisible. Le squad lead et le B2 owner ne peuvent pas tenir la
wheel sans ces 4 états.

### Lien avec les pair checks et red flags

`business-wheel-harmonization-matrix.md` pose 9 pair checks et 5 red
flags. Quand un B3 émet `BLOCKED`, le B2 owner **vérifie** le pair check
du domaine adjacent. Si le pair check est rouge, l'arbitrage monte au
B2 Council — pas au B3. Le B3 ne porte pas la conversation de pair
check ; il porte le `BLOCKED` qui la déclenche.

## Anti-patterns

- **B3 qui invente son propre vocabulaire.** *« Le job est en pause »*
  n'est pas un signal — c'est de la prose. Le B3 utilise `AT_RISK` ou
  `BLOCKED` selon le cas.
- **B3 qui émet `DONE` sans preuve.** Le fractal est net : la preuve
  est **inspectable sans confiance**. Un `DONE` sans capture / log /
  diff / output reproductible est un faux `DONE`. Le B2 peut refuser
  de marquer la gate à `READY`.
- **B3 qui contourne un veto « parce que urgent »**. Le veto n'a pas
  de clause d'urgence implicite. Un veto enfreint sous pression est
  remonté à B1 par le B2 — pas digéré en silence par le B3.

## Source du concept

- `triplets v3 lignes 23-30` — les 8 `hasVetoOver` documentés en
  `ORG.json`.
- `eight-domain-avengers-wheel.md` §« Le mapping canonique » — les
  signaux READY / NEEDS_X / BLOCKED_X par domaine.
- `business-wheel-harmonization-matrix.md` §« Le B2 Council comme
  instance d'arbitrage » — le council arbitre les red flags que le B3
  déclenche par `BLOCKED`.

## Liens

- [[b3-jtbd-packet-reception-checklist]] — la gate est dans le packet
  (build gates, champ 6)
- [[b3-peer-unblock-protocol]] — quand le `BLOCKED` est pair-unblock
- [[b3-hole-signaling-doctrine]] — quand le `BLOCKED` est un trou de
  paquet, pas un blocker technique
- [[b3-cycle-scrums-five-per-week]] — chaque SCRUM porte un signal
- [[eight-domain-avengers-wheel]] — la source des 8 gates
- [[fifty-three-b3-agent-roster]] — qui est le B2 owner de chaque squad

## Note de confiance

**Confirmé par machine.** Les 8 vetos sont dans `ORG.json` (triplets
v3). Les 8 signaux READY / NEEDS_X / BLOCKED_X sont dans
`eight-domain-avengers-wheel.md`. Le vocabulaire B3 → B2 (4 états) est
dérivé du fractal (B3 rend une **preuve**, statut `DONE`) et des
pratiques Coach OS — **pas explicitement publié ailleurs**.

**Contradiction signalée sans trancher** : Martian Manhunter vs
JohnJones. Les deux noms coexistent dans le corpus. La convention
W40 V4 penche pour JohnJones, mais le canon antérieur (et l'ORG.json
Coach OS) garde Martian Manhunter.
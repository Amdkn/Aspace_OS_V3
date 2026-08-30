---
type: Concept
title: RACI par rang × tri-état — extension de la matrice aux 8 capitaines B2 (pas People seul)
description: Le `b2-pair-check-raci-by-rank.md` pose un RACI sur les 9 pair-checks canoniques en régime **normal**. Le cas d'un capitaine B2 en DORMANCE — c'est-à-dire quand A bascule temporairement parce que le captain du domaine aval est absent — n'est pas traité. Le concept `dormance-attente-active.md` (tour 2 #5) propose une tri-état DORMANT/EN_ATTENTE/ACTIF pour People, mais le RACI par rang ne pose pas la transition. Le présent concept **étend** le RACI aux **3 états** pour les **8 capitaines**, propose 4 règles de transition (auto-proclamation interdite, détection Council, consignation D4, confirmation séance), et identifie les **3 cas d'asymétrie** (Batman Ops, Superman Growth, Cyborg IT). La proposition est générique : tout capitaine B2 a une tri-état, pas seulement People.
tags: [people, green-lantern, raci, tri-etat, dormant, en-attente, actif, 8-capitaines, b2, council, doctrine-extension]
generated: { by: minimax-m3, at: 2026-08-19T07:00:00Z }
verified:
  - { by: process:lecture-b2-corpus-tour-3, at: 2026-08-19T07:00:00Z }
sources:
  - id: raci-by-rank
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-pair-check-raci-by-rank.md"
    title: RACI par rang sur les 9 pair-checks — qui est Accountable quand deux domaines se croisent
    last_modified: 2026-08-19
  - id: dormance-attente-active-tour-2
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/green-lantern/green-lantern-people-dormance-attente-active.md"
    title: "Tour 2 — People dormance vs attente vs actif"
    last_modified: 2026-08-19
  - id: b2-areas-dormants
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-areas-dormants-doctrine.md"
    title: B2 doctrine des domaines dormants
    last_modified: 2026-08-19
  - id: aquaman-dormant-tour-2
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-dormant-activation.md"
    title: "Aquaman tour 2 — doctrine dormant-activation 3 états"
    last_modified: 2026-08-19
  - id: batman-cycle-vie-tour-3
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/batman/batman-cycle-vie-procedure-ops-5-phases.md"
    title: "Batman tour 3 — cycle de vie procédure Ops en 5 phases"
    last_modified: 2026-08-19
  - id: b2-council-arbitrage-rule
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-council-arbitrage-rule.md"
    title: B2 Council — qui tranche quand deux domaines se contredisent
    last_modified: 2026-08-19
okf_version: "0.2"
---

# RACI par rang × tri-état — extension de la matrice aux 8 capitaines B2 (pas People seul)

## Le constat — un RACI sans régime de transition

Le `b2-pair-check-raci-by-rank.md` pose un RACI sur les 9 pair-checks
canoniques en régime **normal** :

| # | Pair-check | A (Accountable) |
|---|---|---|
| 1 | Growth → Sales | B2 Sales |
| 2 | Sales → Ops | B2 Ops |
| 3 | Product → Ops | B2 Ops |
| 4 | Product → IT | B2 IT |
| 5 | Finance → Growth | B2 Growth |
| 6 | Finance → Product | B2 Product |
| 7 | Legal → Growth | B2 Growth |
| 8 | Legal → Product | B2 Product |
| 9 | People → Tous | B2 captain du domaine impacté |

**Mais** : ce RACI suppose que le B2 captain en A est **disponible**.
Que se passe-t-il quand Superman (Growth) est **DORMANT** ? Le
pair-check #1 (Growth → Sales) a A = B2 Sales, mais le **C** est
B2 Growth — qui est **absent**. Le pair-check #5 (Finance → Growth)
a A = B2 Growth — qui est l'**absent lui-même**. C'est un cas
d'**escalier cassé** : l'A bascule vers qui ?

Le concept `dormance-attente-active.md` (tour 2 #5) a posé la
tri-état pour People — DORMANT / EN_ATTENTE / ACTIF — mais le RACI
par rang ne **transitionne pas** quand People change d'état. La
**règle mal ajustée #2** signalée par le rapport tour 2 *« RACI
sans dormance B1 »* reste **non traitée**.

Le présent concept propose une **extension** du RACI par rang aux
**3 états** pour les **8 capitaines B2**, pas seulement People. La
tri-état est **générique** — tout capitaine peut être DORMANT, EN
ATTENTE, ou ACTIF.

## La tri-état générique B2

| État | Conditions d'entrée | Position RACI par défaut | Comportement Council |
|---|---|---|---|
| **DORMANT** | Aucun mandate B1 actif, aucun signal en attente, cycle 12WY sans recrutement | A → bascule B1 (escalade), C → autre B2 actif, R → B3 en réserve | Hors séance sauf sollicitation |
| **EN ATTENTE** | Signal en attente (NEEDS_OWNER, sollicitation pair, escalade étage 1-2) | A → conserve, C → actif systématique, R → actif | Présent en C systématique |
| **ACTIF** | Mandate B1 actif, recrutement en cours, arbitrage Council mandate | A → conserve (par défaut), C → conserve, R → actif | Présent en A sur son mandate, C ailleurs |

**Notes** :

- En **DORMANT**, l'A d'un pair-check où le captain dormant était
  Accountable **bascule vers B1** (escalier canonique 5 échelons —
  cf. `b1-stop-conditions-escalier.md`). C'est la seule **exception**
  documentée à la règle *« A = B2 en aval »*.
- En **EN ATTENTE**, l'A **conserve** sa position, mais le C devient
  systématique (le captain est **disponible** mais **non-exécutif**).
- En **ACTIF**, le RACI par rang normal s'applique tel quel.

## Pourquoi la tri-état est générique, pas People-seule

`dormance-attente-active.md` (tour 2 #5) a posé la tri-état pour
People, avec un **cas asymétrique People × IT** (canal Forge
toujours actif). La logique est **transposable** aux 7 autres
capitaines :

- **Batman Ops** — DORMANT si aucun mandat Ops actif, EN ATTENTE si
  un pipeline runbook est en cours de validation, ACTIF sur un
  launch readiness. Cas asymétrique : Batman Ops × Batman (condition
  d'arrêt procédure — toujours actif, comme People × IT).
- **Superman Growth** — DORMANT si aucun mandat Growth (rare — la
  growth est rarement en dormance complète), EN ATTENTE sur un
  ICP à valider, ACTIF sur un launch.
- **Cyborg IT** — DORMANT si aucun système IT à gouverner (rare
  aussi), EN ATTENTE sur un audit de sécurité, ACTIF sur un
  déploiement.
- **Flash Product** — DORMANT si aucun scope actif (rare — Product
  est rarement vide), EN ATTENTE sur une discovery, ACTIF sur un
  build.
- **JohnJones Sales** — DORMANT si aucun pipeline actif, EN ATTENTE
  sur un SQL à qualifier, ACTIF sur un closing.
- **Wonder Woman Finance** — DORMANT si aucun budget à allouer (rare),
  EN ATTENTE sur une revue mensuelle, ACTIF sur un forecast.
- **Aquaman Legal** — DORMANT si aucun dossier à clore (rare — Legal
  a toujours des revues), EN ATTENTE sur un contrat à signer, ACTIF
  sur un litige.

**La tri-état est universelle** parce que la **dormance** est un
**état de cycle**, pas un **état de domaine**. Le cycle 12WY peut
rendre n'importe quel capitaine temporairement inactif — c'est la
**doctrine B2 Areas perpétuelles vs Summer's Verse datées** (cf.
`fractal-b1b2b3-architecture.md`).

## Le RACI × tri-état — tableau intégré

Extension de la matrice canonique RACI par rang avec une **colonne
état** par capitaine. Pour les 9 pair-checks, le RACI devient :

| # | Pair-check | A si ACTIF | A si EN ATTENTE | A si DORMANT |
|---|---|---|---|---|
| 1 | Growth → Sales | B2 Sales | B2 Sales | **B1** (escalade) |
| 2 | Sales → Ops | B2 Ops | B2 Ops | **B1** |
| 3 | Product → Ops | B2 Ops | B2 Ops | **B1** |
| 4 | Product → IT | B2 IT | B2 IT | **B1** |
| 5 | Finance → Growth | B2 Growth | B2 Growth | **B1** |
| 6 | Finance → Product | B2 Product | B2 Product | **B1** |
| 7 | Legal → Growth | B2 Growth | B2 Growth | **B1** |
| 8 | Legal → Product | B2 Product | B2 Product | **B1** |
| 9 | People → Tous | B2 captain impacté | B2 captain impacté | **B1** |

**Règle observée** : dès qu'un captain est DORMANT, l'A bascule à
**B1**. C'est la **seule** exception documentée à *« A = B2 en
aval »*. Elle est justifiée par le fait que B2 Council ne peut pas
**statuer** sans quorum (un captain DORMANT = 7 capitaines présents
sur 8) — l'arbitrage exige une instance supérieure.

**Note** : la bascule A → B1 en DORMANT n'est **pas** une
escalade au sens `b1-stop-conditions-escalier.md` (5 échelons).
C'est un **transfert de Accountable** par défaut, pas une
**escalade conflictuelle**. B1 statue en mode *« by default »*,
pas en mode *« arbitration »*.

## Les 4 règles de transition

La tri-état n'est pas une **auto-proclamation** : le captain ne
**décide pas** seul qu'il passe en DORMANT. Quatre règles
canoniques de transition :

### Règle 1 — Détection par un capitaine B2 ou par B1

Un changement d'état est **détecté** par :

- Le captain lui-même (par exemple, Superman Growth constate qu'il
  n'a plus de mandate Growth actif).
- Un autre captain B2 (par exemple, Batman Ops signale que Growth
  n'a pas répondu à un sollicitation depuis 30 jours).
- B1 (Summers) qui constate directement la vacance.

### Règle 2 — Consignation en journal Council

Le changement d'état est **consigné** dans le journal Council
hebdomadaire avec **horodatage**, **motif**, et **capitaine
détecteur** (qui a vu le signal). Sans consignation, le changement
n'est **pas** officiel — le captain reste dans son état précédent.

### Règle 3 — Confirmation en séance hebdomadaire

Le changement d'état est **confirmé** en séance hebdomadaire B2
Council. Le captain **concerné** est présent (ou représenté). Si
le Council refuse le changement (par exemple, le captain a un
mandate actif que la détection a manqué), l'état **reste**
inchangé.

### Règle 4 — Append-only D4

Le journal Council est **append-only** (D4). Un changement d'état
est une **ligne**, pas une **édition** d'une ligne précédente.
L'historique des transitions est reconstituable à partir du
journal — c'est la **traçabilité** de la tri-état.

## Trois cas d'asymétrie par capitaine

La tri-état générique cache des **cas asymétriques** où un captain
ne peut **jamais** être complètement DORMANT :

### Cas 1 — Batman Ops × condition d'arrêt procédure

Le veto Batman catalogue *« procédure sans condition d'arrêt »*
s'applique à **toute procédure IT/Product/Ops**, pas seulement aux
procédures Batman. Si Batman Ops est en DORMANT, le veto tient
**quand même** — Batman Ops peut bloquer une procédure sans
condition d'arrêt même en DORMANT.

**Conséquence** : Batman Ops a un **sous-état permanent** *« actif
sur le veto »*, même quand le reste est DORMANT. C'est symétrique
au People × IT (canal Forge).

### Cas 2 — Superman Growth × Brand voice

Le co-sponsorat People × Brand (concept `brand-co-sponsorat-superman.md`
tour 2 #6) implique que Superman Growth tient la **voix de marque**,
pas seulement les mandates Growth. Si Superman est DORMANT sur
Growth, il reste **C obligatoire** sur les arbitrages qui touchent
la voix de marque — un arbitrage Brand sans Superman Growth est
**incomplet**.

**Conséquence** : Superman Growth a un **sous-état permanent** *« C
sur Brand »*, même quand le reste est DORMANT. Le pair-check #9
*People × Tous* reste **incomplet** sans Superman.

### Cas 3 — Cyborg IT × runtime souveraineté

Le veto Cyborg *« fournisseur cloud-only sans chemin de sortie »*
s'applique à **toute dépendance IT**, pas seulement aux mandates
IT. Si Cyborg IT est en DORMANT, le veto tient — Cyborg peut bloquer
une dépendance sans chemin de sortie documenté.

**Conséquence** : Cyborg IT a un **sous-état permanent** *« actif
sur le veto »*, même quand le reste est DORMANT. Symétrique à
Batman Ops.

**Conclusion** : les 3 capitaines à veto **catalogue** (Batman,
Cyborg, Superman — Superman via Brand voice) ont des sous-états
permanents. Les 5 autres capitaines (Flash, JohnJones, WonderWoman,
Aquaman, Green Lantern) ont une tri-état **pure** — pas de
sous-état veto.

## Pourquoi la bascule A → B1 n'est pas une escalade

L'escalade B1 (cf. `b1-stop-conditions-escalier.md`) est **conflictuelle**
— le B2 Council ne peut pas trancher, donc Summers arbitre. La
bascule A → B1 en DORMANT est **opérationnelle** — le captain est
introuvable, donc Summers statue **par défaut**.

**Différence pratique** :

- **Escalade conflictuelle** : packet mésoperpétuel avec
  `decision: escalate_to_B1`, motif = *« veto + mandate en conflit »*.
  Summers arbitre sur le **fond**.
- **Bascule DORMANT** : consigne en journal Council avec
  `mode: dormant_transfer`, motif = *« captain A DORMANT, A bascule
  B1 »*. Summers statue **par défaut** sur la base du mandat
  existant, sans ré-ouverture du débat.

**Conséquence** : la bascule DORMANT est **plus rapide** qu'une
escalade conflictuelle, mais **moins profonde** — Summers ne
ré-ouvre pas le débat, il applique le mandat existant au contexte
DORMANT.

## Anti-pièges

- **Auto-proclamation DORMANT**. Un captain qui se proclame DORMANT
  sans consignation Council est un **acte unilatéral** qui doit
  être **refusé**. La tri-état est **Council-confirmée**, pas
  captain-auto-proclamée.
- **DORMANT par confort**. Un captain qui reste DORMANT pour
  éviter la charge Council est en **abus de dormance**. Le Council
  doit vérifier que les conditions d'entrée en DORMANT sont
  **toutes** remplies.
- **A → B1 confondu avec escalation conflictuelle**. La bascule
  DORMANT est **opérationnelle**, pas conflictuelle. Summers ne
  ré-ouvre pas le débat.
- **Sous-état permanent oublié**. Batman Ops, Cyborg IT, Superman
  Growth ont des sous-états veto / Brand. Si le captain oublie son
  sous-état, le veto catalogue **tombe** — c'est un **abandon de
  veto**, pas une dormance assumée.
- **Tri-état imposée à un captain toujours actif**. Un captain en
  ACTIF permanent (par exemple, Batman Ops sur des lancements
  continus) ne **peut pas** être forcé en EN ATTENTE par le
  Council — la tri-état est un **état de cycle**, pas une
  **contrainte organisationnelle**.

## Liens

- [[b2-pair-check-raci-by-rank]] — la matrice RACI à étendre
- [[b2-council-arbitrage-rule]] — l'instance qui confirme les transitions
- [[b2-areas-dormants-doctrine]] — la doctrine dormance B2
- [[b1-stop-conditions-escalier]] — l'escalade conflictuelle (distincte de la bascule DORMANT)
- [[dormance-attente-active]] — la tri-état People (source)
- [[aquaman-dormant-activation]] — la doctrine Aquaman (précédent)
- [[batman-cycle-vie-procedure-ops-5-phases]] — Batman Ops × condition d'arrêt
- [[brand-co-sponsorat-superman]] — People × Brand × Superman C obligatoire
- [[green-lantern-people-veto-perimetre-negatif]] — l'extension du périmètre négatif

## Note de confiance

**Reconstruit, à moitié étayé.** La tri-état générique est
**projetée** depuis la tri-état People tour 2 #5 et la doctrine
Aquaman dormant-activation. L'extension aux 8 capitaines est une
**proposition**, pas une lecture canonique. Le RACI × tri-état
(tableau intégré 9 lignes × 3 colonnes état) est **reconstitué** à
partir de la matrice canonique et de la logique de bascule A → B1
— pas cité comme bloc. Les 4 règles de transition sont **projetées**
depuis la doctrine D4 append-only et la pratique Council. Les 3 cas
d'asymétrie (Batman, Cyborg, Superman) sont **reconstitués** depuis
les concepts tour 1 + tour 2 veto et brand — pas mesurés en cycle.
La distinction bascule DORMANT vs escalade conflictuelle est
**projetée** depuis l'escalier canonique 5 échelons. Le concept est
un **draft d'extension RACI**, pas une extension adoptée.
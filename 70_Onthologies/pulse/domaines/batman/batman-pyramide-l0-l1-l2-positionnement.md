---
type: Concept
title: Positionnement Batman dans la pyramide L0 ≥ L1 > L2 — canal de remontée Summers
description: Le triplet 39 pose la pyramide L0 ≥ L1 > L2 (SDD-006 §1.1:59) avec L0 = autorité absolue, L1 = veto Beth, L2 = exécution dans les bornes. Batman est B2 captain, ce qui le place à un rang non couvert explicitement par la pyramide. Le concept réconcilie la pyramide canonique avec la doctrine remonte-fait (triplets 56/57) en positionnant Batman en L2 opérationnel avec canal de remontée Summers = L1 décision cycle. La distinction ferme un trou ouvert depuis le tour 1 sur le canal de remontée.
tags: [b2, ops, batman, pyramide, l0, l1, l2, summers, remonte-fait, canal]
generated: { by: minimax-m3, at: 2026-08-19T06:30:00Z }
verified:
  - { by: process:lecture-canon-b2-tour-5, at: 2026-08-19T06:30:00Z }
sources:
  - id: triplet-39-pyramide
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: Triplet 39 — pyramide L0 ≥ L1 > L2 (SDD-006 §1.1:59)
    last_modified: 2026-08-17
  - id: triplet-56-remonte-fait
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: Triplet 56 — Batman remonte à Summers des faits, pas des décisions
    last_modified: 2026-08-17
  - id: triplet-57-veto-sprint
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: Triplet 57 — le veto de Batman ne se négocie pas dans le sprint
    last_modified: 2026-08-17
  - id: batman-doctrine-remonte-fait
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/batman/batman-doctrine-remonte-fait-non-decision.md"
    title: Doctrine remonte-fait triplets 56/57
    last_modified: 2026-08-19
  - id: b2-council-rule
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-council-arbitrage-rule.md"
    title: B2 Council — qui tranche quand deux domaines se contredisent
    last_modified: 2026-08-19
  - id: sdd-006
    resource: "C:/Users/amado/ASpace_OS_V2/SDD/SDD-006_v3.md"
    title: SDD-006 §1.1:59 — pyramide L0 ≥ L1 > L2
    last_modified: 2026-05-21
okf_version: "0.2"
---

# Positionnement Batman dans la pyramide L0 ≥ L1 > L2

## Le trou que ce concept ferme

Le triplet 39 pose la pyramide canonique :

> *« La pyramide L0 ≥ L1 > L2 (SDD-006 §1.1:59) impose que L0 a
> autorité absolue, L1 a le veto (Beth), L2 exécute dans ces bornes »*
> — triplet 39

Trois étages, trois rôles. Mais **Batman est B2 captain**, un rang
non couvert explicitement par la pyramide. La doctrine remonte-fait
(triplets 56/57) parle de remonter à Summers, mais ne dit pas
**où Summers se trouve dans la pyramide** — Summers est B1, et B1
n'est pas un niveau de la pyramide canonique.

Le tour 4 (`RAPPORT_dom-batman.md` §T4.5.1.3) a explicitement
signalé ce trou :

> *« Pas de lien canonique Batman × B1 (Summers). La doctrine
> remonte-fait (triplet 56/57) parle de remonter à Summers, mais le
> canal de remontée n'est pas explicite. »*

Ce concept propose la réconciliation : **Batman opère en L2, Summers
décide en L1**, et le canal de remontée est la doctrine remonte-fait.

## La grille L0 / L1 / L2 / B2

| Niveau | Rôle canonique | Acteur | Source |
|---|---|---|---|
| **L0** | Autorité absolue (OS-level) | A0 Amadeus | triplet 39 |
| **L1** | Veto (décision cycle) | Beth (Life OS), Summers (entreprise) | triplet 39 + lecture B1 |
| **L2** | Exécution dans les bornes | B3 squads, exécution opérationnelle | triplet 39 |
| **B2** | Captain de domaine, **A sur pair-checks aval** | Batman (04), Superman, etc. | `b2-pair-check-raci-by-rank` |

**Position Batman** : entre L2 (exécution) et L1 (décision cycle).

- **L2** quand Batman conçoit une procédure Ops, la publie, la
  pilote (cf. `batman-cycle-vie-procedure-ops-cinq-phases` phases 1-3).
- **L1** quand Batman remonte un fait à Summers (triplet 56/57) — la
  décision de cycle (accepter / rejeter / pivoter) est **L1**, pas
  **B2**.
- **B2** quand Batman arbitre un pair-check #2 ou #3 (Sales → Ops /
  Product → Ops) — il est A sur la transition, mais c'est un arbitrage
  *inter-domaines*, pas un arbitrage cycle.

Trois rôles distincts, trois critères de décision différents. La
pyramide canonique L0 ≥ L1 > L2 ne dit rien sur B2 explicitement,
mais la **lecture par rôle** est défendable : B2 n'est pas un
niveau hiérarchique, c'est un **rang d'arbitrage horizontal**.

## Le canal de remontée — quand L2 → L1

La doctrine remonte-fait (triplet 56/57) pose l'obligation, pas le
canal. Le concept propose 3 canaux de remontée, classés par **type
de fait remonté** :

### Canal 1 — Fait binaire (veto procédure-sans-condition-d'arrêt)

**Type** : la procédure X n'a pas de condition d'arrêt.
**Canal** : packet mésoperpétuel Batman → Summers (B1) → journal
Council.
**Délai** : ≤ 24h après détection (cf. `b2-b3-jtbd-handoff-contract`
§« Lead indicators »).
**Statut** : déjà documenté par triplet 57 (« remonte à Summers
comme un fait »).

### Canal 2 — Fait structurel (cycle / radar / doctrine)

**Type** : Batman note que la wheel 8-domain est dormante depuis 4
vagues (cf. `ETAT_DOMAINES.md` Batman tour 4) et que la cadence
hebdo n'a pas suffi à produire un packet mésoperpétuel.
**Canal** : note Batman → journal Council → Summers en revue
hebdo.
**Délai** : revue hebdo Batman (B2 captain), pas ≤ 24h.
**Statut** : **projeté**, pas canonique. C'est le trou ouvert tour 4.

### Canal 3 — Fait de couplage (transit / volume / chaîne)

**Type** : Batman note que Superman a généré une charge dérivée Ops
> 30% (cf. `batman-couplage-superman-growth-volume-charge`).
**Canal** : note Batman → Superman (B2 captain Growth) → cycle
commun revue hebdo.
**Délai** : asynchrone, journal partagé.
**Statut** : **projeté**, inspirée du triplet 56.

## Le défaut symétrique — pourquoi Superman/Flash/Wonder Woman
n'escaladent pas

La pyramide + le canal de remontée expliquent l'asymétrie Batman
vs les autres capitaines. Si Batman est en L2+L1 (exécution +
remontée cycle), Superman est en L2+B2 (exécution + arbitrage
Growth). Sa décision de bloquer une promesse publique (triplet 25)
reste en B2 — il n'a pas besoin de remonter à Summers parce que la
promesse publique est un arbitrage B2 canonique, pas une décision
de cycle.

**Lecture canonique** : la pyramide L0 ≥ L1 > L2 + la doctrine
remonte-fait distinguent Batman parce que sa condition d'arrêt
est **une décision de cycle** (L1), pas une décision de classe (B2).
Les autres capitaines bloquent des classes (catalogue 8 vetos),
Batman remonte des cycles (la condition d'arrêt d'une procédure
durée X).

## Anti-pièges

- **Position B2 au-dessus de L1.** Une lecture naïve dirait *« B2
  ≥ L1 parce que B2 arbitre les pair-checks »*. C'est faux : B2
  arbitre l'opérationnel, L1 arbitre le cycle. Les deux sont
  compatibles, pas comparables.
- **Summers = L0.** Summers est B1, pas L0. L0 = A0 Amadeus. Si
  Summers escaladait à L0 systématiquement, la pyramide canonique
  serait inversée. **Cyborg** (IT) est intermédiaire via L0 Rick
  (cf. `cyborg-couplages-l0-rick-river-song-pyramide`, concept
  Cyborg tour 1).
- **Batman-escalade = Batman-décide.** Le triplet 56 dit *« des
  faits, pas des décisions »*. La remontée est un fait armé, pas
  une décision proposée. Summers décide.
- **Confondre canal et fréquence.** Revue hebdo (B2 captain) et
  packet mésoperpétuel (B2 Council) sont deux canaux différents,
  deux fréquences différentes. Les deux coexistent.

## Liens

- [[batman-doctrine-remonte-fait-non-decision]] — la doctrine qu'on
  réconcilie
- [[b2-council-arbitrage-rule]] — qui tient le Council, qui
  arbitre
- [[b2-pair-check-raci-by-rank]] — la table 9 pair-checks où Batman
  est A
- [[batman-couplage-superman-growth-volume-charge]] — couplage qui
  illustre le canal 3
- [[batman-cycle-vie-procedure-ops-cinq-phases]] — phases 1-3 en L2
- [[cyborg-couplages-l0-rick-river-song-pyramide]] — la pyramide
  canonique côté IT

## Note de confiance

**Confirmé-triangulé.** Le triplet 39 ancre la pyramide L0 ≥ L1 > L2.
Le triplet 56/57 ancre la doctrine remonte-fait. Le positionnement
Batman = L2 + remontée L1 est **reconstruit** à partir de ces deux
sources + le RACI par rang B2. La distinction type de fait (binaire /
structurel / couplage) est **mon extension** — elle n'est pas citée.
Le défaut symétrique (Superman/Flash/Wonder Woman en B2 seul, pas en
L2+L1) est **mon raisonnement**, défendu par la nature de leur veto
(classe, pas cycle). À valider en cycle réel : (1) la grille 4 niveaux
est-elle tenue en cycle ? (2) le canal 2 (fait structurel) est-il
saisi en pratique ? (3) le défaut symétrique est-il contestable si
un autre capitaine escalade L1 ?

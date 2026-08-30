---
type: Concept
title: SHADOW_ACTIVE vs CANONICAL_FROM_CANON — la doctrine de cohabitation entre projet-pilote et doctrine pérenne
description: Le domaine Finance a deux niveaux de canon : (1) la doctrine pérenne Jerry Area (`03_WONDERWOMAN_FINANCE_PRINCIPLES.md`, status CANONICAL_FROM_CANON, Areas Spock), qui pose les 25 principes F1-F25 ; (2) le projet-pilote OMK (`00_B2_DOMAIN_CONTROL_ROOM.md`, status SHADOW_ACTIVE, Projects Picard), qui pose le contrôle room opérationnel. Les deux statuts cohabitent sans se contredire — le projet est l'instantiation, la doctrine est la référence. Le projet doit migrer en ACTIVE pour aligner les deux niveaux, mais la migration n'est pas une condition d'utilisation de la doctrine.
tags: [b2, finance, shadow-active, canonical-from-canon, doctrine, projet-pilote, migration, status, co-habitation]
generated: { by: minimax-m3, at: 2026-08-19T04:55:00Z }
verified:
  - { by: process:lecture-domaine-finance-corpus, at: 2026-08-19T04:55:00Z }
sources:
  - id: spock-finance-principles
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/06_Finance_WonderWoman_Thunderbolts/03_WONDERWOMAN_FINANCE_PRINCIPLES.md"
    title: "Wonder Woman Finance Principles (v4) — status CANONICAL_FROM_CANON"
    last_modified: 2026-06-25
  - id: omk-control-room
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/B2_Business_Domains/06_Finance_WonderWoman_Thunderbolts/00_B2_DOMAIN_CONTROL_ROOM.md"
    title: OMK Finance — B2 Domain Control Room (§ status: SHADOW_ACTIVE)
    last_modified: 2026-05-27
  - id: omk-readme
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/B2_Business_Domains/06_Finance_WonderWoman_Thunderbolts/README.md"
    title: OMK Finance — README § status: SHADOW_ACTIVE
    last_modified: 2026-05-25
  - id: thunderbolts-canon
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/06_Finance_WonderWoman_Thunderbolts/B3_Squad_Thunderbolts/00_B3_SQUAD_CANON.md"
    title: Thunderbolts — Finance Squad (CANON Notion, status Active)
    last_modified: 2026-05-28
  - id: aquaman-control-room
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/B2_Business_Domains/08_Legal_Aquaman_Eternals/00_B2_DOMAIN_CONTROL_ROOM.md"
    title: Aquaman Legal — B2 Domain Control Room (§ status: SHADOW_ACTIVE)
    last_modified: 2026-05-27
  - id: omk-business-os
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/omk-business-os.md"
    title: OMK Business OS — Triptyque V4 status ACTIVE 2026-07-15
    last_modified: 2026-08-17
okf_version: "0.2"
---

# SHADOW_ACTIVE vs CANONICAL_FROM_CANON — la doctrine de cohabitation entre projet-pilote et doctrine pérenne

## Les deux statuts, deux niveaux de canon

Le domaine Finance a **deux niveaux de canon** explicites dans
le corpus, marqués par deux `status` distincts.

### Niveau 1 — Doctrine pérenne (status CANONICAL_FROM_CANON)

`03_WONDERWOMAN_FINANCE_PRINCIPLES.md` (Jerry Area, Spock, J01
Jerry_Prime_LD01_Business) :

```yaml
status: CANONICAL_FROM_CANON
guardian: Wonder Woman (A2)
squad: The Thunderbolts (Bucky Barnes, Yelena Belova, Red
  Guardian, Ghost, Taskmaster, U.S. Agent)
source_corpus: INTERNAL canon (B3 Thunderbolts squad canon +
  control room KR-5d..g) + A0 Empire/Kardashev directive
  (2026-06-02) + 5 capsules 04_Finance (Jay-Z mindset, Matt Gray
  CEO-OS, BFM solo-billionaire-IA, YC trillion markets, Money
  Radar wealth transfer) + recent v5 batch 2026-06-25
```

**Lecture** : la doctrine est **pérenne** (Areas Spock), **canonique**
(installée), et **maintenue** (mise à jour v3 → v4 → v5 sans
nouveau F-numéro). Le `source_corpus` cite **explicitement**
« INTERNAL canon » — c'est-à-dire que la doctrine est dérivée du
canon interne (Thunderbolts squad canon + control room KR), pas
d'une projection depuis Geordi (qui est vide en 04_Finance —
note explicite dans le préambule de la doctrine).

### Niveau 2 — Projet-pilote (status SHADOW_ACTIVE)

`00_B2_DOMAIN_CONTROL_ROOM.md` (OMK Picard, Projects Picard) :

```yaml
status: SHADOW_ACTIVE
updated: 2026-05-27
```

Et `README.md` du même dossier (2026-05-25) :

```yaml
status: SHADOW_ACTIVE
```

**Lecture** : le projet OMK est **pilote** (pas encore ACTIVE), et
le contrôle room est en **shadow** (utilisé pour prototyper, pas
pour exécuter).

## Les trois lectures possibles de la cohabitation

Les deux statuts cohabitent dans le corpus. Trois lectures
possibles :

### Lecture A — Le projet pilote utilise la doctrine canonique (cohérent)

- **Niveau 1 (CANONICAL_FROM_CANON)** : la doctrine pérenne est
  installée et tenue. Les KR-5d..g, les 25 principes F1-F25,
  les SOPs Finance, le squad canon Notion — tout est canonique.
- **Niveau 2 (SHADOW_ACTIVE)** : le projet-pilote OMK utilise la
  doctrine canonique pour prototyper. Le contrôle room OMK est
  une **vue projet** de la doctrine, pas une doctrine alternative.

**Cohérence** : c'est la lecture la plus défendable. Le projet
pilote s'appuie sur la doctrine installée, le contrôle room est
une **fenêtre opérationnelle** sur la doctrine. Quand OMK passe
ACTIVE, le contrôle room doit s'aligner sur la doctrine (F1-F25,
squad 6-membres, etc.).

### Lecture B — Les deux niveaux coexistent en parallèle (lecture temporelle)

- **Niveau 1** : la doctrine est **maintenue** (Areas), évolue par
  versions (v4 → v5), ne « complete » jamais.
- **Niveau 2** : le projet est **déployé** (Projects), doit
  basculer en ACTIVE à un moment donné.

**Cohérence** : le contrôle room OMK aurait dû basculer en ACTIVE
depuis 2026-05-27 — la bascule n'a jamais eu lieu. Le projet est
**techniquement bloqué** en SHADOW_ACTIVE, alors que la doctrine
a évolué en v4 (2026-06-25) puis v5 (2026-06-25). **C'est un
drift temporel** que le projet n'a pas compensé.

### Lecture C — Incohérence non encore arbitrée

Les deux statuts sont **indépendants** et **non-réconciliés**.
Tant qu'aucun arbitrage Council ne pose la lecture canonique, les
deux statuts restent en parallèle, et un lecteur du corpus ne
sait pas lequel prime.

**Cohérence** : faible. Le triplet v3 ligne 27 pose Wonder
Woman = Finance canoniquement (mapping 8-domaines), et le
cinquante-trois-roster pose Thunderbolts ~7 agents, sans
résoudre le statut SHADOW_ACTIVE du projet OMK.

## Arbitrage proposé : Lecture A canonique

**Recommandation au B2 Council** : la Lecture A est canonique.
Trois raisons :

### 1. Le source_corpus de la doctrine cite explicitement OMK

La doctrine pérenne Jerry Area cite verbatim dans son
`source_corpus` : « INTERNAL canon (B3 Thunderbolts squad canon +
**control room KR-5d..g**) ». Le control room OMK est **une
source** de la doctrine, pas une alternative. La doctrine s'appuie
sur le KR-5d..g défini dans OMK.

**Conséquence** : OMK est **subordonné** à la doctrine, pas
l'inverse. Le projet pilote est une **vue** de la doctrine.

### 2. Le squad canon Notion prime sur le squad OMK

Le squad canon Notion (2026-05-28, status Active) et la doctrine
Jerry Area (2026-06-25, status CANONICAL_FROM_CANON) sont
**concordants** sur les 6 Thunderbolts. OMK control room est
**isolé** avec sa squad 4-membres (cf.
[[wonder-woman-thunderbolts-squad-canon-arbitration]]). La
concordance Notion + Jerry Area prime sur l'isolement OMK.

### 3. Le statut SHADOW_ACTIVE est conçu pour la protraction

Le statut SHADOW_ACTIVE n'est pas un **échec de migration**, c'est
un **statut explicite de protraction** — le projet est conçu pour
être en shadow tant qu'il n'est pas validé. La doctrine
canonique est **déjà validée**. Le projet n'a pas besoin d'être
ACTIVE pour que la doctrine soit canonique.

## Le mécanisme de migration — 4 étapes

La migration du projet OMK vers ACTIVE est une action en 4 étapes :

### Étape 1 — Vérification de l'alignement

Wonder Woman vérifie que le contrôle room OMK est aligné sur la
doctrine pérenne (F1-F25, squad 6-membres, SOPs canoniques, KR-5d..g).
L'audit pose les écarts.

### Étape 2 — Migration du squad roster

OMK `00_B2_DOMAIN_CONTROL_ROOM.md` § « B3 Swarm Scope » passe de
« Red Hulk budget, Taskmaster accounting, Zemo strategy, Ghost
leak detection » aux 6 membres canoniques (Bucky, Yelena, Red
Guardian, Ghost, Taskmaster, U.S. Agent). Préservation des 4 noms
historiques dans un addendum.

### Étape 3 — Alignement des KR

Les KR-5d..g du contrôle room doivent référencer la doctrine
F1-F25, pas des métriques ad hoc. Par exemple : KR-5f « runway
≥12 mois » doit citer F1 « Runway is the survival metric ».

### Étape 4 — Bascule de status

`00_B2_DOMAIN_CONTROL_ROOM.md` status passe de `SHADOW_ACTIVE` à
`ACTIVE`, avec un packet mésoperpétuel qui consigne la migration.
Le contrôle room est désormais **opérationnel**.

## La dormance Aquaman comme précédent

Aquaman Legal a un statut analogue : `00_B2_DOMAIN_CONTROL_ROOM.md`
du domaine Legal (OMK) est aussi `SHADOW_ACTIVE` (2026-05-27), et
la doctrine Aquaman est dans le même cas que Finance. Mais
Aquaman a un statut supplémentaire : la **dormance Areas**
(cf. `b2-areas-dormants-doctrine.md`) — Aquaman steward Legal &
Compliance en état dormant tant que `00_Summers_CEO/03_Master_Agreements/`
reste vide.

**Lecture croisée** : le statut SHADOW_ACTIVE d'Aquaman est
**cohérent avec la dormance Areas** — un domaine dormant n'a pas
besoin d'un contrôle room ACTIVE. Mais Wonder Woman Finance
**n'est pas dormant** (F1 runway est toujours actif), donc le
statut SHADOW_ACTIVE du contrôle room OMK est **moins justifiable**
pour Finance que pour Legal.

C'est une asymétrie qui milite pour la **migration rapide** du
contrôle room Finance OMK vers ACTIVE.

## Anti-pièges

- **SHADOW_ACTIVE = obsolète.** Un contrôle room SHADOW_ACTIVE
  n'est pas obsolète — il est en cours de validation. Le projet
  est **vivant**, pas mort.
- **CANONICAL_FROM_CANON = figé.** Une doctrine canonique n'est
  pas figée — elle est maintenue (v3 → v4 → v5). Le terme
  « canon » désigne la **source de vérité**, pas l'absence
  d'évolution.
- **Le projet prime sur la doctrine.** La doctrine prime sur le
  projet. Le projet est une **vue** de la doctrine, pas
  l'inverse.
- **Statut lu au premier degré.** Le statut d'un fichier est un
  **état**, pas une **valeur**. Un fichier SHADOW_ACTIVE peut
  être **plus à jour** qu'un fichier CANONICAL_FROM_CANON si
  ce dernier n'est pas maintenu. La lecture du statut exige de
  croiser avec la datation et l'historique de versions.
- **Statuts comme hiérarchie de pouvoir.** Les deux statuts sont
  des **états documentaires**, pas une hiérarchie de pouvoir.
  Aucun des deux ne « commande » l'autre.

## Liens

- [[wonder-woman-finance-doctrine-f1-f25-mapping]] — les 25 principes
- [[wonder-woman-thunderbolts-squad-canon-arbitration]] — la squad canon
- [[wonder-woman-finance-frontiers]] — le périmètre Finance
- [[wonder-woman-paid-release-gate-finance]] — le gate transversal
- [[b2-areas-dormants-doctrine]] — la doctrine de dormance Aquaman

## Note de confiance

**Confirmé par machine** sur les deux statuts (lus verbatim des
frontmatter respectifs, datations 2026-05-25 / 2026-05-27 /
2026-06-25). **Confirmé** sur le subordination OMK à la doctrine
(citée verbatim dans `source_corpus`). **Reconstruit** sur la
Lecture A comme arbitrage canonique — la doctrine ne pose pas
explicitement la règle « projet subordonné à doctrine », mais
c'est cohérent avec la hiérarchie Areas > Projects. **Reconstruit**
sur la migration 4 étapes — extrapolation depuis les doctrines de
maintenance D4 append-only et de versionnement canon.
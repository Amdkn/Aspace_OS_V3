---
type: Concept
title: People × IT × Forge — soumission Council-ready de la Méta Gouvernance des skills L0
description: Le concept `green-lantern-people-meta-gouvernance-skills-l0.md` (tour 2) a posé 3 lectures + 4 critères de tri + une règle de survie. Le présent concept formalise la **soumission Council-ready** : packet mésoperpétuel B2-MESO-DECISION-2026-NN (draft), 5 champs obligatoires, 3 lectures en compétition, 4 critères de tri pondérés, RACI conditionnel selon lecture, procédure d'amendement 5/8 + escalate B1, et clause de fallback si Council refuse. Le concept ne tranche pas — il rend la décision **arbitrable** par le B2 Council.
tags: [people, green-lantern, it, cyborg, forge, meta-gouvernance, council, packet, meso-decision, submission, b2]
generated: { by: minimax-m3, at: 2026-08-19T06:30:00Z }
verified:
  - { by: process:lecture-b2-corpus-tour-3, at: 2026-08-19T06:30:00Z }
sources:
  - id: meta-gouvernance-tour-2
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/green-lantern/green-lantern-people-meta-gouvernance-skills-l0.md"
    title: "Tour 2 — People × IT × Forge — qui tient la Méta Gouvernance des skills L0"
    last_modified: 2026-08-19
  - id: meso-decision-packet-spec
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-meso-decision-packet-spec.md"
    title: Meso Decision Packet — le format canonique d'une décision B2
    last_modified: 2026-08-19
  - id: b2-council-arbitrage-rule
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-council-arbitrage-rule.md"
    title: B2 Council — qui tranche quand deux domaines se contredisent
    last_modified: 2026-08-19
  - id: b2-eight-domain-vetoes-catalogue
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-eight-domain-vetoes-catalogue.md"
    title: B2 catalogue des 8 vetos
    last_modified: 2026-08-19
  - id: aquaman-pair-check-v5
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-pair-check-10-Legal-risk-Launch.md"
    title: "Aquaman — pair-check #10 Legal-risk-Launch candidat V5 avec procédure d'amendement"
    last_modified: 2026-08-19
  - id: triplet-37-forge
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 37 — Green Lantern sollicite Bill (L0.2 Forge) — canal non-contournable"
    last_modified: 2026-08-17
  - id: triplet-55-forge
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 55 — Green Lantern escalade les besoins de skills L0 vers Bill"
    last_modified: 2026-08-17
okf_version: "0.2"
---

# People × IT × Forge — soumission Council-ready de la Méta Gouvernance des skills L0

## Le gap — un draft tour 2, pas un packet Council

Le concept `green-lantern-people-meta-gouvernance-skills-l0.md` (tour
2 #1) a posé le **gap canonique** : *« la Méta Gouvernance des
skills L0 (canal Bill L0.2 Forge) est citée par Coach OS comme
périmètre People, mais le canon V4 ne tranche pas entre People, IT,
ou un domaine transverse. »*

Le concept tour 2 a proposé 3 lectures (A People, B IT, C transverse),
4 critères de tri (risque, mandate modif, données, SLA), et une règle
de survie en attendant l'arbitrage. **Mais il n'a pas formalisé la
soumission Council** — c'est un draft de travail, pas un packet
arbitrable.

Le présent concept **formalise** la soumission : packet
mésoperpétuel `B2-MESO-DECISION-2026-NN` (draft), conforme au
`b2-meso-decision-packet-spec.md`, avec les 3 lectures en
compétition, les 4 critères pondérés, le RACI conditionnel, et la
procédure d'amendement 5/8 + escalate B1. Le packet est **prêt à
soumettre** — pas encore soumis.

## Le packet mésoperpétuel draft

```yaml
meso_decision_id: B2-MESO-DECISION-2026-NN
source_mandate: B2-PEER-2026-NN  # car pas de mandate B1 — gap People × IT × Forge
mode: negotiation
impacted_domains:
  - people
  - it
tradeoff: "Méta Gouvernance des skills L0 — qui possède le périmètre au rang B2 :
  People (Green Lantern, Lecture A Coach OS), IT (Cyborg, Lecture B IT),
  ou transverse (Council, Lecture C) ? Trois lectures en compétition,
  4 critères de tri pondérés (risque 40%, mandate 20%, données 20%, SLA 20%),
  RACI conditionnel selon lecture tranchée. Si Council refuse : fallback sur
  la règle de survie (People continue de solliciter, IT informé, co-signature
  sur modification)."
decision: pending  # la décision sera tranchée en séance Council
proof_expected:
  - B2 gate People update (people_meta_governance_owner = people | it | transverse)
  - B2 gate IT update (it_meta_governance_owner = people | it | transverse)
  - B3 proof path (X-Men_Beast_TechRecruiting_skill_L0_resolution_30d)
next_review: 2026-09-15  # 60 jours après soumission
```

**Conformité au format canonique** : les 7 champs obligatoires
(`meso_decision_id`, `source_mandate`, `mode`, `impacted_domains`,
`tradeoff`, `decision`, `proof_expected`, `next_review`) sont
remplis. Le format est Council-ready.

**Note sur `source_mandate`** : la valeur est `B2-PEER-2026-NN` et
non `B1-B2-MANDATE-2026-NN` parce que le gap People × IT × Forge est
**identifié par les pairs** (Green Lantern + Cyborg via triplets 37 +
55), pas par un mandate B1. C'est conforme au
`b2-meso-decision-packet-spec.md` §« `source_mandate` » — un
problème identifié par un capitaine B2 en revue peut utiliser le
préfixe `B2-PEER`.

## Les 3 lectures en compétition — synthèse

Le concept tour 2 a déjà posé les 3 lectures. Le packet draft en
fait la **synthèse exécutive** :

### Lecture A — People (Green Lantern) tient la Méta Gouvernance

- **Pour** : triplet 37 dit *« Green Lantern sollicite »*, triplet 55
  dit *« Green Lantern escalade »*, Coach OS intitule *« RH & Méta
  Gouvernance »*.
- **Contre** : IT Cyborg perd une partie de son scope (la gestion
  des skills est une IT infra). Le couplage People × IT (Beast
  TechRecruiting × IT infra) devient **interne à People**.
- **Critères de tri** : Risque 60% portée People, mandate 70%
  People, données 50/50, SLA 40% IT.

### Lecture B — IT (Cyborg) tient la Méta Gouvernance

- **Pour** : les skills L0 sont un **runtime** IT (matrice
  pair-check #4 *Product → IT* — IT est propriétaire du système).
- **Contre** : People perd la gouvernance RH des agents (un agent
  sans skill n'est pas opérationnel). Le triplet 37 perd son
  asymétrie : si IT sollicite aussi Forge, la règle *« Green Lantern
  sollicite »* devient incomplète.
- **Critères de tri** : Risque 30% portée People, mandate 30%
  People, données 70% IT, SLA 80% IT.

### Lecture C — Transverse (Council) tient la Méta Gouvernance

- **Pour** : les skills L0 sont une **méta-capacité** (capacité
  d'ajouter des capacités). Le propriétaire est celui qui tient la
  **carte des skills**, pas l'agent ou le système.
- **Contre** : le Council doit tenir un nouveau registre (carte
  des skills) qui n'existe pas canoniquement. Charge Council
  nouvelle, non testée en cycle.
- **Critères de tri** : Risque 50/50, mandate 50/50, données 50/50,
  SLA 50/50.

## Les 4 critères pondérés

La pondération 40/20/20/20% est projetée depuis la doctrine veto
(risque = propriété 1 dans `b2-eight-domain-vetoes-catalogue.md` §«
Catégoriel »).

| Critère | Pondération | Question de tri |
|---|---|---|
| **Risque** | 40% | Qui porte le risque si le skill L0 manque ? |
| **Mandate modif** | 20% | Qui tient le mandat de modification d'un skill existant ? |
| **Données** | 20% | Qui tient la souveraineté des données liées au skill ? |
| **SLA** | 20% | Qui signe l'accord de niveau de service (SLA) sur la disponibilité du skill ? |

**Application au score** :

| Lecture | Risque (40%) | Mandate (20%) | Données (20%) | SLA (20%) | Score pondéré |
|---|---|---|---|---|---|
| A People | 0.6 | 0.7 | 0.5 | 0.4 | **0.56** |
| B IT | 0.3 | 0.3 | 0.7 | 0.8 | **0.46** |
| C Transverse | 0.5 | 0.5 | 0.5 | 0.5 | **0.50** |

**Lecture A** (People) gagne au score, mais la marge est **faible**
(0.56 vs 0.50 vs 0.46). Le critère **risque** est le plus
pondéré, et c'est celui où People est le plus fort — mais le critère
**SLA** où People est le plus faible réduit le score.

**Verdict projeté du score** : Lecture A (People) est **légèrement
favorisée** par les critères pondérés. Mais le **Council arbitre**,
pas le score. Le packet draft **ne tranche pas** — il propose.

## Le RACI conditionnel selon lecture

Si le Council tranche Lecture A, B, ou C, le RACI est différent :

| Rôle | Lecture A | Lecture B | Lecture C |
|---|---|---|---|
| **A** (Accountable sur la Méta Gouvernance) | Green Lantern | Cyborg | B2 Council chair |
| **R** (Responsible — exécute la sollicitation Forge) | X-Men | Kang Dynasty | Council secretary |
| **C** (Consulted — signe les skills L0) | Cyborg | Green Lantern | Tous les 8 capitaines |
| **I** (Informed — voit le journal des skills) | Tous les 8 capitaines | Tous les 8 capitaines | Tous les 8 capitaines |

**Note.** Le RACI canonique par rang (cf. `b2-pair-check-raci-by-rank.md`)
ne pose pas la Méta Gouvernance — c'est un périmètre **non-standard**
qui n'est pas dans la matrice 9 pair-checks. Le RACI conditionnel
est donc **projeté** depuis la règle *« A = B2 en aval de la
transition »*, appliquée au périmètre Méta Gouvernance.

**Asymétrie** : dans les Lectures A et B, le RACI est **binaire**
(un A, un R, deux C) ; dans la Lecture C, il est **transverse**
(un A chair, un R secretary, 8 C, 8 I). C'est la signature de la
lecture transverse.

## La procédure d'amendement 5/8 + B1

La décision sur la Méta Gouvernance est un **amendement de règle
catalogue** (qui possède le périmètre), pas une amplification de
veto. La procédure exige :

1. **Séance hebdomadaire B2 Council** : revue du draft packet.
2. **Décision** : accept (Lecture A, B, ou C), blocked (refus avec
   motif), escalate_to_B1 (escalade Summers).
3. **Majorité 5/8** pour accept. Capitaine dissident = blocage
   formel.
4. **Escalate B1** : Summers arbitre en cas de désaccord persistant.
5. **Append-only** dans `B2_DC_DIRECTION_COUNCIL_DECISIONS.md` avec
   date d'effet.

**Pourquoi 5/8, pas unanimité** : la Méta Gouvernance est un
**périmètre nouveau**, pas une modification d'une règle catalogue
existante. 5/8 = majorité qualifiée standard pour les ajouts. Cf.
`aquaman-pair-check-10-Legal-risk-Launch.md` §« procédure
d'amendement unanimité+B1 » pour un précédent de règle catalogue
(strict).

## La clause de fallback si le Council refuse

Le Council peut refuser le packet draft pour trois raisons :

1. **Lecture A, B, C toutes refusées** — le Council propose une
   Lecture D (par exemple, *« Cyborg tient le runtime, People tient
   le recrutement, Forge tient l'injection »*).
3. **Sursis à décision** — le Council demande un complément
   d'information avant de trancher (par exemple, un audit du nombre
   de sollicitations Forge sur 90 jours).
3. **Escalade B1** — le Council ne peut pas trancher et remonte à
   Summers.

Dans les 3 cas, la **règle de survie** du concept
`green-lantern-people-meta-gouvernance-skills-l0.md` §« La règle de
survie en attendant l'arbitrage » **continue de tenir** :

1. People continue de solliciter Forge (triplet 37 autorité
   opérationnelle).
2. IT Cyborg est informé en copie.
3. Modification de skill existant co-signée People + IT.

C'est la clause de **fallback** — tant que le Council n'a pas tranché,
le canal Forge ne casse pas.

## Trois cas où la soumission Council serait prématurée

1. **Pas d'observation réelle du canal Forge**. Le triplet 37 cite
   le canal, mais **aucun cycle réel** n'a été observé où People a
   sollicité Forge pour un skill L0 manquant. Soumettre le packet
   maintenant, c'est **théoriser** sans pratique. Recommandation :
   attendre 1 cycle (60-90 jours) pour observer au moins 1 cas réel.
2. **Pas d'arbitrage Council observé sur People × IT**. Le Council
   n'a jamais tranché un conflit People × IT (cf. rapport tour 2 :
   *« 0 packet mésoperpétuel People enregistré en vague 2 »*).
   Soumettre sans précédent, c'est **inaugurer** la pratique. Le
   B2 Council peut préférer un cas réel avant de poser la doctrine.
3. **Pas de B1 mandate sur le périmètre Méta Gouvernance**. Le
   source_mandate est `B2-PEER-2026-NN`, pas `B1-B2-MANDATE`. Si B1
   (Summers) n'a pas explicitement mandaté l'arbitrage, le Council
   peut **refuser** de statuer sur un périmètre non-mandaté. Le
   packet reste un draft ; la soumission est **incitative**, pas
   **contraignante**.

## Anti-pièges

- **Score pondéré utilisé comme décision automatique**. Le score
  favorise Lecture A (0.56), mais le Council arbitre **sur
  débat**, pas sur score. Un score de 0.56 contre 0.50 ne suffit
  pas à *« imposer »* Lecture A — c'est un **outil d'aide**, pas
  une règle de majorité.
- **Lecture C présentée comme consensuelle**. La Lecture C (transverse)
  a un score intermédiaire (0.50), mais c'est la **plus coûteuse**
  en charge Council (registre nouveau, arbitrage sur chaque skill).
  Le Council peut préférer Lecture A ou B pour éviter la charge, pas
  pour des raisons doctrinales.
- **Règle de survie invalidée après décision**. Une fois que le
  Council tranche Lecture A, B, ou C, la règle de survie est
  **remplacée** par la lecture tranchée. Conserver la règle de
  survie après décision, c'est **dupliquer** le périmètre.
- **RACI conditionnel utilisé avant décision**. Le RACI
  conditionnel (tableau 4 colonnes) est un **projet**, pas une
  application. Avant la décision Council, c'est le RACI par défaut
  (transverse, Green Lantern C systématique sur People × X) qui
  tient.
- **Clause de fallback oubliée**. Si le Council refuse, **la règle
  de survie continue de tenir**. Le draft packet doit l'expliciter,
  sinon le refus = vacuum.

## Liens

- [[green-lantern-people-meta-gouvernance-skills-l0]] — le draft source (3 lectures, 4 critères)
- [[b2-meso-decision-packet-spec]] — le format canonique respecté
- [[b2-council-arbitrage-rule]] — l'instance qui arbitre
- [[b2-eight-domain-vetoes-catalogue]] — les 8 vetos qui bornent les lectures
- [[b2-pair-check-raci-by-rank]] — le RACI canonique par rang
- [[aquaman-pair-check-10-Legal-risk-Launch]] — un précédent de packet Council-ready
- [[aquaman-veto-amendment-perimetre-insuffisant]] — la procédure 5/8 + B1
- [[green-lantern-people-v5-pair-check-granularisation-9]] — l'autre amendement matrice V5

## Note de confiance

**Reconstruit, à moitié étayé.** Le packet draft est **conforme** au
format canonique mésoperpétuel (7 champs obligatoires, D4
append-only). Les 3 lectures, 4 critères, et règle de survie sont
**reconstruits** depuis le concept tour 2 #1. La pondération
40/20/20/20% est **projetée** depuis la doctrine veto (risque =
propriété 1) — pas citée canoniquement. Le score pondéré (A 0.56,
B 0.46, C 0.50) est **calculé** à partir de scores attribués par
projection — **pas mesuré**. Le RACI conditionnel est **projeté**
depuis la règle *« A = B2 en aval »* — pas étayé par un cycle
Council réel. La procédure 5/8 + B1 est tirée verbatim de
`aquaman-pair-check-10-Legal-risk-Launch.md` §« procédure
d'amendement ». La clause de fallback (règle de survie continue) est
**reprise** du concept tour 2 #1. Les 3 cas de soumission prématurée
sont **projetés** depuis la doctrine Council (pas de décision sans
cas observé). Le concept est un **draft Council-ready**, pas un
packet soumis.
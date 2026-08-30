---
type: Concept
title: Batman RACI I sur #4 — packet Council-ready avec co-signature Cyborg
description: Tour 3 propose Batman I (Informed) sur pair-check #4 Product→IT. La proposition doit être formalisée en packet mésoperpétuel B2-MESO-DECISION-2026-NN, conditionnée à l'accord Cyborg (A sur #4 par canon), et passer la procédure d'amendement unanimité 8/8 + B1. Packet draft Council-ready construit ici.
tags: [b2, ops, batman, raci, i-sur-4, packet, council-ready, amendement, unanimite]
generated: { by: minimax-m3, at: 2026-08-19T06:04:00Z }
verified:
  - { by: process:lecture-canon-b2-tour-4, at: 2026-08-19T06:04:00Z }
sources:
  - id: batman-raci-tour-3
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/batman/batman-raci-correction-informe-pair-check-4.md"
    title: Proposition RACI Batman I sur pair-check #4 Product→IT
    last_modified: 2026-08-19
  - id: b2-pair-raci
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-pair-check-raci-by-rank.md"
    title: RACI par rang sur les 9 pair-checks
    last_modified: 2026-08-19
  - id: b2-packet-spec
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-meso-decision-packet-spec.md"
    title: Meso Decision Packet — le format canonique d'une décision B2
    last_modified: 2026-08-19
  - id: b2-council-rule
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-council-arbitrage-rule.md"
    title: B2 Council — qui tranche quand deux domaines se contredisent
    last_modified: 2026-08-19
  - id: green-lantern-unanimite
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/green-lantern/green-lantern-v5-pair-check-granularisation-9.md"
    title: V5 pair-checks granularisation #9 — procedure amendement unanimite 8/8 + B1
    last_modified: 2026-08-19
  - id: cyborg-pair-check-4
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/cyborg/cyborg-pair-check-raci-batman-i-cyborg-a-product-it-conditional-acceptance.md"
    title: Pair-check #4 acceptation conditionnelle Cyborg
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Batman RACI I sur #4 — packet Council-ready avec co-signature Cyborg

## Le trou que Batman ferme

Tour 3 propose Batman I (Informed) sur pair-check #4 Product → IT
(cf. `batman-raci-correction-informe-pair-check-4.md`). La proposition
est triple :

1. **Visibiliser la chaîne Product → IT → Ops** que Batman subit
   comme dépendance aval.
2. **Engager Batman sans le rendre Accountable** — Batman reçoit
   la chaîne comme un flux, mais ne statue pas sur la transition
   Product → IT, qui est du ressort d'IT (Cyborg).
3. **Conditionner l'acceptation Cyborg** — la RACI V4 pose Cyborg A
   sur #4 par canon. La proposition Batman I doit obtenir
   l'acceptation explicite de Cyborg avant soumission.

Le présent packet transforme la proposition en **draft Council-ready**,
prêt à soumission B2 Council + B1, sous reserve de co-signature
Cyborg.

## Le packet draft

```yaml
meso_decision_id: B2-MESO-DECISION-2026-NN
source_mandate: B2-PEER-2026-NN
mode: negotiation
impacted_domains:
  - ops
  - it
  - product
tradeoff: "Etendre la RACI par rang sur le pair-check #4 Product→IT
  pour ajouter Batman I (Informed). Batman est aval de la chaîne
  Product→IT→Ops et veut visibiliser sa dépendance. Cyborg A reste
  A sur #4 par canon. L'extension ne modifie pas la A de Cyborg, elle
  ajoute Batman I pour symétrie aval. Co-signature Cyborg requise.
  Procedure d'amendement : unanimité 8/8 + B1."
decision: accepted
proof_expected:
  - B2 RACI update (pair-check-04.people-informed = batman)
  - B2 RACI update (chain documentation product-it-ops visible)
  - B3 proof path (1 cycle Coach OS avec Batman I observe dans le journal Council)
next_review: 2026-12-01
```

Le packet est **Council-ready** sous 3 conditions cumulatives :

1. **Co-signature Cyborg** (acceptation explicite, cf. concept Cyborg
   `cyborg-pair-check-raci-batman-i-cyborg-a-product-it-conditional-acceptance.md`).
2. **Procédure d'amendement unanime 8/8 + B1** (cf. granularisation
   Green Lantern V5, même procedure).
3. **Observation 1 cycle Coach OS** post-amendement pour valider
   l'effet (Batman I sans modifier A).

## La procédure d'amendement unanime 8/8 + B1

Cette procédure est **reconstruite** à partir de deux sources :

1. **Green Lantern V5 granularisation** :
   `green-lantern-v5-pair-check-granularisation-9` pose la procédure
   *« amendement unanime 8/8 + escalate B1 »* pour l'ajout de
   sous-pair-checks à #9 People → Tous.
2. **Doctrine Canonique d'amendement** : un amendement de la matrice
   d'harmonisation (9 → 12 par exemple) exige un vote unanime 8/8
   parce qu'il change un canon partagé. Sans unanimité, l'amendement
   est un précédent unilatéral.

**Procédure** (4 étapes) :

1. **Préparation** par le captain promoteur (Batman dans le cas #4).
   Format packet mésoperpétuel B2-MESO-DECISION-2026-NN.
2. **Co-signature** par tout captain dont la RACI est modifiée (Cyborg
   pour #4, People pour #9, etc.).
3. **Soumission** à l'assemblée B2 (8 capitaines). Vote unanime 8/8
   requis. Un seul veto = rejet.
4. **Escalade B1** pour ratification. B1 statue sur la cohérence
   North Star. Sans ratification B1, l'amendement est caduque.

## Pourquoi Batman I (et pas C)

Le RACI par rang (cf. `b2-pair-check-raci-by-rank.md`) pose 4 rôles
par pair-check. Batman sur #4 pourrait être :

- **C (Consulted)** : Batman est consulté avant la décision, son
  avis est pris en compte. Mais Batman n'a pas de voix sur la
  transition Product → IT.
- **I (Informed)** : Batman reçoit l'information après la décision,
  sans voix au chapitre. C'est la proposition retenue.

Batman **C** aurait été un sur-classement : Batman ne statue pas
sur la qualité du code (Product) ni sur la disponibilité du système
(IT). Sa dépendance aval (Ops) est un effet downstream, pas une
contribution upstream. **C** impliquerait un droit de regard que
Batman ne peut pas exercer legitmement.

Batman **I** est la position canonique pour les pair-checks où le
capitaine est dépendant sans définir. C'est le même pattern que
B1 sur tous les pair-checks (`b2-pair-check-raci-by-rank.md` §«
Pourquoi A = B2 en aval, pas B1 »).

## Le cas asymétrique : Cyborg A + Batman I sur #4

Le pair-check #4 aurait donc :

| Rôle | Captain |
|---|---|
| A (Accountable) | B2 IT (Cyborg) |
| R (Responsible) | B3 Kang Dynasty |
| C (Consulted) | B2 Product (Flash) |
| I (Informed) | B1 + **B2 Ops (Batman)** |

Batman rejoint B1 dans la colonne I. C'est une **double Informed** —
capitaine downstream + direction. La matrice resultante a 5 Informed
(B1 + Batman + B3 Avengers) au lieu de 4 (B1 + B3 Avengers).

Cas analogue : aquaman propose en tour 3 une triple signature
`Aquaman+Batman+Thena` pour la defensibilite procedure. Le pattern
est similaire : Batman apparaît comme garant aval sur un objet
dont il n'est pas A.

## La justification de la triple fenetre

Trois raisons defendable pour Batman I sur #4 :

1. **Visibiliser la chaîne Product → IT → Ops.** Sans Batman I, la
   dépendance aval d'Ops sur la qualité du système IT est invisible
   dans la RACI. Batman I rend cette dépendance lisible.
2. **Anticiper la saturation.** Quand le système IT s'effondre,
   c'est Ops qui absorbe le signal (cf. `batman-couplage-ops-it.md`).
   Batman I permet d'être alerté avant la saturation.
3. **Coherence avec le portique `LAUNCH_READY`.** Batman est A sur
   le portique final du delivery. Si Batman n'est même pas I sur
   la transition qui *précède* le delivery, sa A sur le portique
   final est en partie aveugle.

Trois raisons refus possible :

1. **Sur-couverture RACI.** I n'est pas un rôle opérationnel ; c'est
   un rôle d'observation. Multiplier les I peut créer une matrice
   illisible.
2. **B1 I suffit.** L'I de B1 couvre tous les pair-checks. Ajouter
   Batman I sur #4 sans étendre aux 7 autres pair-checks est
   sélectif.
3. **Co-signature conditionnelle Cyborg.** Cyborg a posé une
   acceptation conditionnelle (cf. concept Cyborg). Si Cyborg
   retire la condition, le packet est caduc.

## Le RACI corrigé si amendement accepté

| # | Pair-check | A | R | C | I |
|---|---|---|---|---|---|
| 4 | Product → IT | B2 IT | B3 Kang Dynasty | B2 Product | B1, B2 Ops (Batman), B3 Avengers |

**Validation contre `b2-pair-check-raci-by-rank.md`** : la matrice
canonique V4 sur #4 n'inclut pas Batman I. L'amendement proposé
étend la colonne I tout en laissant A/R/C intacts. C'est un
amendement de transparence, pas un amendement de transfert.

## Anti-pièges

- **Soumettre sans co-signature Cyborg.** Le packet est invalide
  sans la co-signature du captain dont la RACI est la plus modifiée.
- **Sauter la procedure d'amendement.** Un amendement par consensus
  mou (5/8) est un précédent invalide. La matrice est canonique,
  pas négociable par majorité.
- **Confondre I et C.** La difference I vs C est sur le **droit de
  regard avant la décision**. C est consulté avant ; I est informé
  après. Batman sur #4 regarde la conséquence aval, pas la cause
  amont — c'est I, pas C.
- **Étendre l'usage sans déclencher le 3ème tour.** La proposition
  est une **extension RACI**, pas un amendement de matrice. Les
  deux motions sont Council-ready mais diffèrentes.

## Liens

- [[batman-raci-correction-informe-pair-check-4]] — la proposition tour 3
- [[b2-pair-check-raci-by-rank]] — le RACI par rang canonique
- [[b2-meso-decision-packet-spec]] — le format packet
- [[b2-council-arbitrage-rule]] — qui tient le Council
- [[green-lantern-v5-pair-check-granularisation-9]] — la procedure d'amendement
- [[cyborg-pair-check-raci-batman-i-cyborg-a-product-it-conditional-acceptance]] — la co-signature Cyborg

## Note de confiance

**Reconstruit, à moitié étayé.** Le packet draft est Council-ready
sous 3 conditions cumulatives (co-signature, procedure amendement,
1 cycle). La procedure d'amendement unanime 8/8 + B1 est **empruntée**
à la proposition V5 granularisation Green Lantern, pas explicitement
posée pour les amendements RACIBatman. La RACI corrigée est alignée
sur la matrice canonique. Le pattern double Informed (B1 + Batman)
est projeté sur l'analogie avec la triple signature Aquaman. C'est
**une preference Batman**, pas un canon — le Council peut préférer
une motion différente.

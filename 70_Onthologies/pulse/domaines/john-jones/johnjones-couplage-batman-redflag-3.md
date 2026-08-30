---
type: Concept
title: JohnJones — couplage avec Batman (Ops) sur red flag #3, charge de livraison et risque de ré-exten
description: Le red flag #3 (Sales green, Ops/People red) déclenche quand Sales signe une opportunité qualifiée mais que Ops n'a pas la capacité de tenir la livraison ou que People n'a pas l'effectif pour la charge. Batman (Ops) est en aval sur le pair-check #2 (Sales → Ops), donc A = B2 Ops sur #2 — Batman tranche la capacité de livraison. Le couplage JohnJones×Batman sur red flag #3 documente 4 cas d'application, 3 cas d'abus, le trigger `risk_charge_livraison`, et la procédure 4 étapes. Analogue aux couplages Batman×autres-domaines posés en tour 3.
tags: [b2, johnjones, sales, batman, ops, couplage, red-flag, charge-livraison, risk]
generated: { by: minimax-m3, at: 2026-08-19T05:50:00Z }
verified:
  - { by: process:lecture-corpus-sales-tour-3, at: 2026-08-19T05:50:00Z }
sources:
  - id: harmonization-md
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/areas/business-wheel-harmonization-matrix.md"
    title: "Red flag #3 — Sales green, Ops/People red"
    last_modified: 2026-08-17
  - id: b2-harmonization-exploitable
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-harmonization-matrix-exploitable.md"
    title: Matrice d'harmonisation B2 — forme exploitable
    last_modified: 2026-08-19
  - id: b2-pair-check-raci
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-pair-check-raci-by-rank.md"
    title: RACI par rang — pair-check #2 Sales → Ops, A = B2 Ops
    last_modified: 2026-08-19
  - id: gates-et-pair-checks
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/john-jones/johnjones-gates-et-pair-checks.md"
    title: JohnJones — gates et pair-checks (#2 Sales → Ops)
    last_modified: 2026-08-19
  - id: b2-failsafe
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-failsafe-paperclip-recovery.md"
    title: B2 failsafe paperclip recovery — doctrine red flag arrêt dur
    last_modified: 2026-08-19
okf_version: "0.2"
---

# JohnJones — couplage avec Batman sur red flag #3

## Le red flag #3 — verbatim

`business-wheel-harmonization-matrix.md` §« Les 5 red flags » pose
verbatim :

> **Red flag #3 — Sales green, Ops/People red** : *« Risque de
> charge de livraison — la promesse ne pourra pas être tenue. »*

Lecture : Sales a signé (reformulation validée, opportunité
qualifiée, scope clair), mais Ops n'a pas la capacité de tenir la
livraison ou People n'a pas l'effectif pour la charge. La pression
naturelle est de pousser la signature (elle est gagnée), mais sans
capacité aval la promesse explose en rétention. **Arrêt dur**.

## Pourquoi un couplage avec Batman

Le red flag #3 met en scène **deux capitaines** :

- **JohnJones (Sales, B2 captain amont)** — il a signé. Le radar
  affiche Sales green.
- **Batman (Ops, B2 captain aval)** — il ne peut pas tenir la
  livraison. Le radar affiche Ops red. People peut aussi être red
  si l'effectif manque.

Le couplage JohnJones×Batman est **le seul** red flag où Sales est
explicitement **amont** (le déclencheur) et un autre capitaine est
**aval** (la victime). Sur les 5 red flags catalogue :

- **#1** (Product green, Ops/IT red) — Batman est aval mais JohnJones
  n'est pas impliqué.
- **#2** (Growth green, Sales red) — JohnJones est **aval** (la
  cible du blocage), Batman n'est pas impliqué.
- **#4** (Finance red + Growth/Product green) — Wonder Woman
 牵头, JohnJones aval.
- **#5** (Legal red + public-facing work) — Aquaman牵头, JohnJones
  Informed.

Le red flag #3 est donc **le seul** où JohnJones est explicitement
**amont** et Batman est **aval** — d'où le couplage.

## Le RACI sur le red flag #3

`b2-pair-check-raci-by-rank.md` pose la matrice par rang. Pour le
red flag #3 :

| Rôle | Qui | Pourquoi |
|---|---|---|
| **A** (Accountable) | **B2 Ops (Batman)** | Ops est en aval sur pair-check #2 (Sales → Ops). A = B2 en aval. C'est Batman qui tranche la capacité de livraison. |
| **R** (Responsible) | **B3 Fantastic Four** | Le squad B3 Ops tient la livraison. C'est le Responsable opérationnel de la capacité. |
| **C** (Consulted) | **B2 Sales (JohnJones)** | JohnJones est amont sur #2. Il est consulté avant la décision, pas après. |
| **I** (Informed) | **B1, B3 Illuminati** | B1 voit la décision dans le journal Council. B3 Illuminati est informé que la charge change. |

**Conséquence** : quand le red flag #3 se déclenche, **Batman
tranche**, pas JohnJones. JohnJones plaide la cause Sales (la
signature est gagnée, le client attend), Batman arbitre la capacité
Ops (peut-on tenir ?). Si Batman oppose son veto procédure-sans-condition
(cf. `b2-eight-domain-vetoes-catalogue.md` §Batman veto), la
signature est bloquée ou conditionnée.

## Les 4 cas d'application légitime

### Cas #1 — Charge Ops non calibrée

**Symptôme** : JohnJones signe une opportunité (reformulation
validée, scope clair), mais Batman n'a pas encore calibré la charge
de livraison (par exemple, le ratio supportable Ops/Product n'a pas
été posé pour ce type de scope).

**Détection** : un `SALES_COMMITMENT.md` qui précède un
`OPS_CAPACITY_CALIBRATION.md` de plus de 7 jours. Le radar affiche
Sales green, Ops red (charge > 100% sur les 30 jours suivants).

**Remède** : Batman oppose le veto procédure-sans-condition (la
procédure de signature n'a pas de condition d'arrêt écrite sur la
capacité Ops). La signature est gelée jusqu'à calibration.

### Cas #2 — Owner People absent

**Symptôme** : JohnJones signe une opportunité, mais aucun owner
People n'est assigné sur le compte. La matrice d'harmonisation #9
(People → Tous) exige un owner et une charge tenable.

**Détection** : un `SALES_COMMITMENT.md` sans `OWNER_ASSIGNMENT.md`
correspondant. Le radar affiche Sales green, People red.

**Remède** : Batman (et/ou Green Lantern People) escalade — la
signature est conditionnée à l'assignation d'un owner.

### Cas #3 — Charge dérivée non documentée

**Symptôme** : la signature déclenche une charge dérivée (support,
onboarding, monitoring) que Batman n'a pas anticipée. La charge
Ops est calibrée pour le scope nominal, pas pour le scope réel.

**Détection** : un diff entre `OPS_CAPACITY_CALIBRATION.md` (scope
nominal) et `SALES_COMMITMENT.md` (scope signé). Le radar Ops vire
au rouge après la signature.

**Remède** : Batman conditionne la livraison à un re-calibrage. La
charge dérivée est ajoutée au scope Ops.

### Cas #4 — Forecast DoctorStrange sans lien ops

**Symptôme** : DoctorStrange (Forecasting B3 Illuminati) pose un
chiffre de pipeline sans que Batman ait confirmé la capacité Ops
pour la période du forecast. Le forecast est creux — Batman ne
peut pas tenir ce qui est prévu.

**Détection** : un `FORECAST_*.md` qui ne référence pas
`OPS_CAPACITY_CALIBRATION.md`. Le radar affiche Sales green (parce
que le forecast est précis), Ops red (parce que la capacité n'est
pas calibrée pour le forecast).

**Remède** : Batman exige un co-signal DoctorStrange + Ops avant
de valider le forecast. Le forecast n'est Council-ready qu'avec
les deux signatures.

## Les 3 cas d'abus

### Abus #1 — Batman qui bloque une signature calibrée

**Symptôme** : Batman oppose son veto sur une signature Sales alors
que la capacité Ops **est** calibrée et tenable. C'est un abus de
position — Batman utilise son veto catalogue sur autre chose que sa
classe (capacité Ops).

**Détection** : un `BLOCKED_COMMITMENT.md` qui ne référence aucun
fichier de calibration Ops. Le motif est *« Ops red »* mais le
fichier Ops n'existe pas ou est à jour.

**Remède** : JohnJones escalade au B2 Council. Si Batman ne produit
pas de fichier de calibration, son veto est invalide (manque la
propriété 2 — vérifiable, cf. `b2-eight-domain-vetoes-catalogue.md`).

### Abus #2 — JohnJones qui signe sans consulter Batman

**Symptôme** : JohnJones signe une opportunité sans vérifier la
capacité Ops en amont. Le radar affiche Sales green, Ops red, mais
JohnJones argue *« j'ai signé, c'est fait »*.

**Détection** : un `SALES_COMMITMENT.md` sans trace de pair-check
#2 (Sales → Ops) dans `OPS_HANDOFF_QUEUE.md`. Batman n'a pas été
consulté avant la signature.

**Remède** : le packet mésoperpétuel Council documente l'absence de
pair-check #2. La sanction est sur la **discipline** (pair-check
manqué), pas sur le résultat. JohnJones ré-apprend la séquence
discovery → reformulation → pair-check #2 → signature.

### Abus #3 — Batman qui refuse de calibrer

**Symptôme** : Batman n'a jamais calibré la capacité Ops pour le
segment de scope en question. Il oppose son veto *« Ops red »*
sans proposer de calibration. C'est une obstruction.

**Détection** : un historique Council où Batman oppose *« Ops red »*
systématiquement sans produire de fichier de calibration.

**Remède** : escalade B1 pour forcer la calibration. Batman ne
peut pas utiliser *« Ops red »* comme un blanc-seing permanent.

## Le trigger `risk_charge_livraison`

Analogue au trigger `charge_derivee` posé par Batman en tour 3
pour le couplage Ops×Superman-Growth (cf. rapport Batman §tour 3).
Le trigger **préc** le red flag #3 — il signale une dérive
**naissante** avant que le radar n'affiche Ops red.

**Définition** : `risk_charge_livraison = (charge_ops_signée /
charge_ops_calibrée) > seuil`. Le seuil projeté est 0.7 — au-delà
de 70% de charge calibrée, le risque de dépassement est non
négligeable.

**Effet** : quand le trigger passe à 0.7, JohnJones doit consulter
Batman avant toute nouvelle signature. Si le trigger passe à 1.0,
**arrêt dur** sur les nouvelles signatures jusqu'à re-calibrage.

## La procédure 4 étapes

Quand le red flag #3 se déclenche (ou quand le trigger
`risk_charge_livraison` passe à 0.7), 4 étapes canoniques :

1. **JohnJones initie** le pair-check #2 (Sales → Ops) en
   consignant `SALES_COMMITMENT.md` + `OPS_HANDOFF_REQUEST.md`.
2. **Batman évalue** la capacité Ops dans les 48h ouvrées. Il
   produit `OPS_CAPACITY_CALIBRATION.md` avec charge signée /
   charge calibrée + projection 30/60/90 jours.
3. **Batman arbitre** : (a) signature validée telle quelle, (b)
   signature conditionnée à un re-scope ou une re-calibration, (c)
   veto procédure-sans-condition opposé, signature gelée.
4. **Packet mésoperpétuel** consigné dans
   `B2_DC_DIRECTION_COUNCIL_DECISIONS.md` avec `decision: accepted`
   / `blocked` / `escalate_to_B1`. Champs `proof_expected:` et
   `next_review:` obligatoires.

## Anti-pièges

- **JohnJones qui signe sans pair-check #2** (abus #2).
- **Batman qui bloque sans calibration** (abus #3).
- **Batman qui veto sur autre chose que la capacité Ops** (abus #1).
- **Déclencher le red flag #3 sans packet mésoperpétuel.** Le red
  flag est un **arrêt dur** (cf. `b2-failsafe-paperclip-recovery.md`
  §doctrine red flag), pas une suggestion. Sans packet, le red flag
  n'a pas de force d'arbitrage.
- **Croire que le trigger `risk_charge_livraison` suffit.** Le
  trigger **préc** le red flag. Une fois le radar Ops passé au
  rouge, c'est le red flag lui-même qui s'applique — le trigger
  n'est plus suffisant, il faut le pair-check #2 + le veto potentiel.
- **Escalader à B1 par défaut.** Le red flag #3 se résout au
  Council, pas à B1. B1 n'intervient que si Batman et JohnJones ne
  peuvent pas trancher (ce qui est rare — Batman tranche la
  capacité Ops, JohnJones consulte sur la cause Sales).

## Liens

- [[johnjones-gates-et-pair-checks]] — pair-check #2 Sales → Ops
- [[johnjones-veto-reformulation-validee]] — veto amont Sales
- [[b2-eight-domain-vetoes-catalogue]] — veto Batman procédure-sans-condition
- [[b2-harmonization-matrix-exploitable]] — règle de résolution
- [[b2-pair-check-raci-by-rank]] — RACI par rang #2
- [[b2-failsafe-paperclip-recovery]] — doctrine red flag arrêt dur
- [[b2-council-arbitrage-rule]] — qui tient le Council

## Note de confiance

**Confirmé par machine, à moitié.** Le red flag #3 verbatim est tiré
de `business-wheel-harmonization-matrix.md`. Le RACI par rang (A =
B2 Ops sur #2) est tiré verbatim de `b2-pair-check-raci-by-rank.md`.
Les 4 cas d'application et 3 cas d'abus sont **reconstruits** depuis
la pratique documentée (Coach OS + doctrine red flag) — pas étayés
par triplet canonique spécifique à Sales×Ops. Le trigger
`risk_charge_livraison` et son seuil 0.7 sont **projetés** par
analogie avec le trigger `charge_derivee` Batman×Superman — pas
étayés par triplet canonique. La procédure 4 étapes est **projetée**
depuis `b2-council-arbitrage-rule.md` §Composition et routine.

À vérifier en cycle réel : (1) Batman oppose-t-il son veto
procédure-sans-condition sur le red flag #3 ou utilise-t-il un
autre motif ? (2) Le seuil 0.7 du trigger est-il trop bas ou trop
haut ? (3) Le pair-check #2 est-il systématiquement exécuté avant
chaque signature Sales ?
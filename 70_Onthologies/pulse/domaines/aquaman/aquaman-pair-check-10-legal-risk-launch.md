---
type: Concept
title: Aquaman — pair-check #10 Legal risk → Launch, Aquaman en A direct
description: Pour les arbitrages où le risque Legal est l'enjeu principal (claim litigieuse, breach de terms, régulation sectorielle), A bascule chez Aquaman et non chez le B2 en aval de la transition. Trois cas de bascule cumulatifs, trois cas de non-bascule, procédure d'amendement matrice en unanimité + B1. Tour 3 transforme la remontée ouverte depuis tour 1 en proposition concrète.
tags: [b2, aquaman, pair-check, legal-risk, launch, red-flag-5, amendment, raci]
generated: { by: minimax-m3, at: 2026-08-19T05:00:00Z }
verified:
  - { by: process:lecture-canon-aquaman-tour-3, at: 2026-08-19T05:00:00Z }
sources:
  - id: harmonization-matrix
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-harmonization-matrix-exploitable.md"
    title: Matrice d'harmonisation B2 — forme exploitable
    last_modified: 2026-08-19
  - id: raci-by-rank
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-pair-check-raci-by-rank.md"
    title: RACI par rang sur les 9 pair-checks
    last_modified: 2026-08-19
  - id: aquaman-veto
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-veto-engagement-sans-perimetre.md"
    title: Aquaman veto engagement-sans-périmètre
    last_modified: 2026-08-19
  - id: aquaman-jtbd
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-jtbd-emit-receive.md"
    title: Aquaman catalogue JTBD émis et reçus
    last_modified: 2026-08-19
  - id: aquaman-perimetre
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-domaine-legal-perimetre.md"
    title: Aquaman domaine Legal périmètre
    last_modified: 2026-08-19
  - id: avengers-wheel
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/eight-domain-avengers-wheel.md"
    title: Eight Domain Avengers Wheel
    last_modified: 2026-08-17
okf_version: "0.2"
---

# Aquaman — pair-check #10 Legal risk → Launch, Aquaman en A direct

## Le trou dans la matrice 9 pair-checks

La matrice d'harmonisation pose **9 pair-checks canoniques** (cf.
[[b2-harmonization-matrix-exploitable]]). Deux d'entre eux placent
Aquaman en **Consulted** :

- **#7 Legal → Growth** : A = Superman (B2 en aval de la transition).
- **#8 Legal → Product** : A = Flash (B2 en aval de la transition).

**Conséquence** : si Superman ou Flash veulent pousser une *claim
litigieuse*, une *feature qui breach des terms*, ou un *launch dans
une régulation sectorielle sensible*, Aquaman émet `BLOCKED_RISK`,
mais **la décision opérationnelle reste chez le B2 en aval**.
Aquaman n'a pas le dernier mot sur ce qui *engage* l'organisation
publiquement.

Le **red flag #5** (`Legal red + public-facing work = geler les claims
et le launch`) compense en partie — il bloque les combinaisons où
Legal est explicitement rouge. Mais **le red flag #5 ne fait pas
d'Aquaman l'arbitre final** ; il *bloque*, et le Council doit ensuite
trancher qui corrige.

## La proposition : un 10ᵉ pair-check *Legal risk → Launch*

L'idée est qu'il existe une classe d'arbitrages où le risque Legal
*est* l'enjeu principal, et où **Aquaman devrait être A** sur la
décision de lancer ou de geler. Cette classe est distincte des 9
pair-checks transitionnels — c'est un pair-check **décisionnel**, pas
un pair-check de transfert.

### La question de garde

> **Le risque Legal est-il l'enjeu principal du lancement, ou un
> effet de bord ?**

Si l'enjeu principal = risque Legal → A = Aquaman.
Si l'enjeu principal = adoption / delivery / marge (et Legal = effet
de bord) → A = B2 en aval (règle des 9 pair-checks canoniques).

### Les 3 cas de bascule Aquaman A

**Cas 1 — Claim litigieuse**.
La claim publique (landing page, ad copy, press release) contient
une affirmation qui, selon Aquaman, ne peut pas être substantiée ou
risque un litige FTC / regulator. Superman peut être A *en
exécution* (timing, channel), mais pas en *décision* : la décision
de *publier ou geler* est chez Aquaman.

**Cas 2 — Breach de terms**.
La feature (Flash) ou la claim (Superman) breach un term existant
d'un contrat-cadre avec un partenaire, un client majeur, ou un
fournisseur. Aquaman est A pour statuer sur *ce qui peut ou ne peut
pas être publié*, indépendamment du timing de publication.

**Cas 3 — Régulation sectorielle émergente**.
La sortie (feature ou claim) tombe sous une régulation sectorielle
dont l'interprétation est en cours de stabilisation (par exemple RGPD
en 2018-2020, DMA en 2024-2025, AI Act en 2025-2026). Aquaman est A
pour *geler le launch* le temps que la doctrine se précise.

### Les 3 cas de non-bascule (A reste en aval)

**Non-cas 1 — Risk Legal accessoire**.
Le launch a un risque Legal *parmi d'autres* (par exemple risque
Finance, risque Ops). A reste chez le B2 en aval. Aquaman émet son
gate dans son coin, mais ne tranche pas le launch.

**Non-cas 2 — Risk Legal déjà géré en amont**.
Le risque Legal a été traité en pair-check #7 ou #8 et Aquaman a
émis `LEGAL_READY`. Le launch n'a plus de Legal risk non-couvert — A
reste chez le B2 en aval.

**Non-cas 3 — Aquaman à l'état Dormant**.
Si Aquaman est à l'état **Dormant** ou **SHADOW_ACTIVE** (cf.
[[aquaman-dormant-activation]]), il ne peut pas être A. La bascule A
vers Aquaman exige **ACTIVE**. Un projet pré-launch ne peut pas
bénéficier du pair-check #10.

## Le RACI par rang appliqué au #10

| Position | Rang | Capitaine |
|---|---|---|
| **A** (Accountable) | B2 | **Aquaman** (et non le B2 en aval) |
| **R** (Responsible) | B3 | Eternals (le squad qui produit la defensibility doc, cf. Forme 4 du catalogue) |
| **C** (Consulted) | B2 | Superman (Growth) ou Flash (Product) selon le pair-check d'origine (#7 ou #8) |
| **I** (Informed) | B1, B3 Guardians ou Avengers |

**Différence avec #7 / #8** : A *bascule* chez Aquaman. C'est
explicitement le **pattern d'exception** posé dans
[[b2-pair-check-raci-by-rank]] §« Pourquoi A = B2 en aval, pas B1 »
— l'A bascule chez le rang B2 qui est *Accountable sur le risque
spécifique*, pas le rang B2 en aval de la transition.

## La procédure d'amendement matrice

[[b2-harmonization-matrix-exploitable]] pose les 9 pair-checks comme
un **catalogue** amendable. L'amendement suit 4 étapes :

1. **Proposition** : Aquaman (via ce concept) propose l'ajout du
   pair-check #10 en B2 Council.
2. **Examen** : les 7 autres capitaines évaluent si le #10 est
   *catégoriel* (porte sur une classe d'arbitrages, pas un cas
   spécifique) et *vérifiable* (le risque Legal est l'enjeu principal
   peut être testé par un motif écrit).
3. **Vote** : unanimité des 8 capitaines requise pour amender la
   matrice. C'est la même règle que pour les autres amendements de
   catalogue (cf. [[b2-council-arbitrage-rule]] §« Les trois
   situations concrètes où le Council doit escalader »).
4. **Escalade B1 si pas d'unanimité** : si un capitaine refuse
   l'amendement, Aquaman peut escalader B1 pour réécriture. B1
   arbitre alors si le #10 doit être ajouté à la matrice officielle
   ou rejeté.

**Statut actuel** : pas d'unanimité acquise (les 7 autres capitaines
n'ont pas encore tranché). Le concept est une **proposition**,
pas une décision.

## Le couplage avec le red flag #5

Le red flag #5 (Legal red + public-facing work) et le pair-check #10
sont **complémentaires**, pas redondants :

- **Red flag #5** = arrêt dur binaire (Legal red ⇒ geler).
- **Pair-check #10** = arbitrage structuré quand l'enjeu Legal est
  l'objet même du lancement.

**Différence pratique** :

- Un Legal red sur un risque *accessoire* (par exemple risque
  privacy mineur sur une feature de login) → red flag #5 gèle le
  launch.
- Un Legal red sur un risque *principal* (claim litigieuse) →
  red flag #5 gèle, **et** pair-check #10 met Aquaman en A pour
  statuer sur la levée du gel après amendement.

**Conséquence** : Aquaman doit *connaître les deux*. Un Aquaman qui
ne déclenche que le red flag #5 sans activer le pair-check #10 fait
de l'overreach (geler un launch sans proposer de voie de levée). Un
Aquaman qui ne déclenche que le pair-check #10 sans le red flag #5
fait du漏 (accepter un risque Legal sous couvert d'arbitrage).

## Anti-pièges

- **A = Aquaman par défaut, pas par exception.** Le pair-check #10
  ne fait *pas* d'Aquaman l'A sur les pair-checks #7 et #8
  systématiquement. A = Aquaman *seulement* quand le risque Legal
  est l'enjeu principal. Un Aquaman qui s'autoproclame A sur #7 et #8
  fait de l'overreach — la décision reste chez Superman ou Flash
  pour les cas standards.
- **Pair-check #10 comme outil politique.** Si Aquaman invoque le
  #10 sur un arbitrage où l'enjeu principal *n'est pas* Legal (par
  exemple un arbitrage de pricing), le pair-check est invalidé (cf.
  règle des 3 propriétés du veto — [[aquaman-veto-engagement-sans-perimetre]]
  §Les trois propriétés canoniques).
- **Activation sans état ACTIVE.** Un Aquaman à l'état Dormant ou
  SHADOW_ACTIVE (cf. [[aquaman-dormant-activation]]) ne peut pas
  être A sur le #10 — l'activation à ACTIVE exige un livrable
  signé. Le #10 n'est *pas* un raccourci pour activer Aquaman en
  avance.
- **Décision A sans proof_expected.** Le pair-check #10, comme
  tout arbitrage B2, doit produire un packet mésoperpétuel avec
  proof_expected (cf. [[b2-meso-decision-packet-spec]] §Les champs).
  Un pair-check #10 sans proof est une *opinion*, pas un arbitrage.

## Liens

- [[b2-harmonization-matrix-exploitable]] — les 9 pair-checks
  canoniques et les 5 red flags que le #10 complète
- [[b2-pair-check-raci-by-rank]] — le RACI par rang sur lequel le
  #10 est bâti
- [[aquaman-veto-engagement-sans-perimetre]] — les 3 propriétés du
  veto qui s'appliquent au #10
- [[aquaman-jtbd-emit-receive]] — Forme 4 (defensibility doc) que
  le #10 peut déclencher
- [[aquaman-dormant-activation]] — la condition ACTIVE pour que le
  #10 puisse être activé
- [[b2-council-arbitrage-rule]] — la procédure d'amendement matrice
  (unanimité + B1)

## Note de confiance

**Reconstruit, proposé, non-arbitré.** Le #10 n'existe pas dans le
canon. La proposition est étayée par (1) le trou observé dans la
matrice 9 pair-checks (Aquaman toujours Consulted), (2) le red flag
#5 qui compense sans trancher, (3) la procédure d'amendement matrice
unanimité + B1. Les 3 cas de bascule et 3 cas de non-bascule sont
**projetés** depuis les surfaces du périmètre Legal ([[aquaman-domaine-legal-perimetre]]
§Ce que couvre le domaine) et les 4 formes émises ([[aquaman-jtbd-emit-receive]]).
Le RACI par rang appliqué au #10 est **reconstruit** par symétrie
avec le RACI des pair-checks #7 et #8. **À arbitrer en B2 Council** :
l'unanimité des 8 capitaines est-elle tenable, ou un capitaine
s'opposera-t-il par principe ? La doctrine d'amendement matrice
n'est pas testée en cycle.

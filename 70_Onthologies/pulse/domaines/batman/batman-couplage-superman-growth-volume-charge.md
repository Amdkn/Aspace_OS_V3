---
type: Concept
title: Batman × Superman — couplage invisible Growth → Ops via le volume d'attention
description: Le pair-check #1 (Growth → Sales) et le pair-check #2 (Sales → Ops) sont posés par la matrice d'harmonisation. Mais aucun pair-check ne lie Growth directement à Ops, alors que le volume d'attention Growth (MQL, demande entrante) détermine indirectement la charge Ops par le double transit Growth → Sales → Ops. Si Superman livre 1000 MQL/mois et que JohnJones en convertit 10 %, Batman encaisse 100 onboardings/mois — sans que ce couplage volumique soit thématisé.
tags: [batman, superman, growth, ops, couplage, volume, charge, mql, pair-check-invisible, b2]
generated: { by: minimax-m3, at: 2026-08-19T05:35:00Z }
verified:
  - { by: process:lecture-b2-corpus-tour-3, at: 2026-08-19T05:35:00Z }
sources:
  - id: harmonization-md
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/areas/business-wheel-harmonization-matrix.md"
    title: Harmonisation — 9 pair-checks canoniques, pas de Growth→Ops
    last_modified: 2026-08-17
  - id: avengers-wheel
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/eight-domain-avengers-wheel.md"
    title: Eight Domain Avengers Wheel — Batman émet LAUNCH_READY
    last_modified: 2026-08-17
  - id: triplet-superman-veto
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 25 — Superman bloque promesse publique non-tenable par la delivery"
    last_modified: 2026-08-17
  - id: triplet-batman-fait
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 56 — Batman remonte à Summers des faits, pas des décisions"
    last_modified: 2026-08-17
  - id: b2-pair-check-raci
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-pair-check-raci-by-rank.md"
    title: RACI par rang — Batman absent des pair-checks Growth→Sales et Growth amont
    last_modified: 2026-08-19
  - id: batman-couplage-people
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/batman/batman-couplage-people-green-lantern-owner-absent.md"
    title: Batman × Green Lantern — chaîne Batman→GL→X-Men pour l'owner
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Batman × Superman — couplage invisible Growth → Ops

## Le constat — Batman est 2 transitions en aval de Superman, sans visibilité canonique

La matrice d'harmonisation pose **9 pair-checks canoniques**
(`business-wheel-harmonization-matrix.md` §« Domain Pair Checks »).
Batman est Accountable sur les pair-checks #2 (Sales → Ops) et #3
(Product → Ops). **Batman n'apparaît sur aucun pair-check qui parte
de Superman** (Growth) — ni directement, ni en Consulted.

C'est techniquement correct : la matrice teste des **transitions
un-à-un** entre domaines adjacents. Le flux réel est :

```
Superman (Growth)
  ↓ pair-check #1 (Growth → Sales)
JohnJones (Sales)
  ↓ pair-check #2 (Sales → Ops)
Batman (Ops)
```

Batman est **deux transitions en aval** de Superman. Si la chaîne
fonctionne, Batman ne voit jamais Superman. Si la chaîne casse
(même 1 maillon), Batman encaisse le défaut sans avoir été consulté.

**Le problème** : le volume d'attention Growth (MQL, demande entrante)
conditionne la charge de livraison Ops via le double transit
Growth → Sales → Ops. Si Superman livre 1000 MQL/mois et que
JohnJones en convertit 10 %, Batman encaisse 100 onboardings/mois.
Si Batman est dimensionné pour 50, le red flag #3 (Sales green,
Ops/People red) se déclenche — ou le red flag #1 (Product green,
Ops/IT red) si la charge est étalée.

## Pourquoi la matrice ignore ce couplage

La matrice d'harmonisation teste **la cohérence d'une transition**,
pas la **capacité aval** à absorber le volume. C'est un choix de
design : la matrice est binaire (vert/rouge), pas continue (charge
relative). Un pair-check #1 vert dit *« l'attention devient-elle
opportunité qualifiée ? »* — il ne dit pas *« l'attention est-elle
dans le ratio que Ops peut absorber ? »*.

Cette omission est **assumée** par la doctrine canonique : le ratio
MQL/SQL/onboarding est un **paramètre de calibration** Sales, pas un
critère de pair-check. Le triplet 25 (Superman) dit *« bloque toute
prise de parole publique qui promet un résultat que la delivery ne
tient pas »* — la promesse publique est le garde-fou, pas la
calibration Sales.

**Conséquence** : Batman dépend de la calibration de JohnJones
(Sales) qui dépend lui-même du volume de Superman (Growth). C'est
une **chaîne de calibration** implicite, pas un pair-check. Batman
n'a pas de prise directe sur Superman.

## Le couplage réel — 3 cas où Batman remonte un volume qui n'est pas le sien

### Cas 1 — Volume d'onboarding qui dépasse la cadence Ops

Constat : Batman remonte à Summers (triplet 56) que **le nombre
d'onboardings signés par Sales ce mois dépasse la cadence Ops
planifiée**. C'est un fait, pas une décision. Summers arbitre —
soit il mandate JohnJones de ralentir la signature, soit il mandate
Green Lantern de renforcer l'effectif Ops, soit il mandate Batman
d'absorber le surplus (en dégradant un autre DoD).

**Statut canonique** : ce cas n'est pas dans la matrice. C'est un
**trou de doctrine** — Batman remonte un volume, mais aucun
pair-check ne teste la cohérence du volume.

### Cas 2 — Volume de support post-launch qui dérive après un coup Growth

Constat : Superman lance une campagne paid (triplet 25 verrou) qui
génère 500 demandes entrantes en 2 semaines. Batman (Ops) encaisse
un volume de support qui n'était pas planifié dans le DoD. Le
portique LAUNCH_READY (cf. `batman-launch-ready-portique-final-transverse.md`)
avait été posé vert sur la base d'un DoD *« supporter 50 tickets/semaine
post-launch »* — le DoD est respecté si on lit le run cost, mais pas
si on regarde la cadence support.

**Statut canonique** : la matrice teste le DoD **statique** au moment
du portique, pas la **capacité dynamique** post-launch. Superman
peut générer un volume qui sature Ops après le portique.

### Cas 3 — Volume de réclamations qui révèle un défaut de promesse

Constat : Superman promet *« onboarding en 24h »* (cf. triplet 25 —
la promesse publique est la garde). Batman livre l'onboarding en
24h, mais le **taux de réclamation** post-onboarding explose parce
que la promesse a généré des clients que le run Ops ne peut pas
tenir sur la durée. Le défaut est dans la promesse (Superman), pas
dans la livraison (Batman). Mais Batman remonte le fait, parce que
c'est lui qui voit les tickets.

**Statut canonique** : le triplet 25 dit *« promet un résultat que la
delivery ne tient pas »* — Batman peut signaler, mais c'est Superman
qui doit bloquer sa propre promesse. La doctrine remonte-fait
(triplet 56) protège Batman de l'accusation *« tu n'as pas livré »*,
mais ne lui donne pas le pouvoir de bloquer Superman.

## Le trigger proposé — alerte de charge dérivée

Pour visibiliser le couplage sans modifier la matrice, je propose un
**trigger de charge dérivée** dans le packet mésoperpétuel Batman :

```yaml
charge_derivee:
  source_volume: superman_growth
  transit_attendu: sales
  ratio_implicite: <ex: 10%>  # MQL → onboarding
  volume_mois_courant: <N>
  cadence_ops_planifiee: <M>
  ecart_pct: <(N*ratio - M) / M>
  seuil_alerte: 30%  # écart au-dessus duquel Batman remonte
  statut: vert|orange|rouge
```

**Trois propriétés du trigger** :

1. **Lecture instantanée** — Batman voit la charge dérivée sans
   avoir à recalculer la chaîne Growth → Sales → Ops.
2. **Non-bloquant** — le trigger remonte le fait (orange/rouge), il
   ne bloque pas Superman. C'est Summers qui arbitre, conformément
   à la doctrine remonte-fait.
3. **Cohérent avec les red flags** — un trigger orange préempte le
   red flag #3 (Sales green, Ops/People red). Un trigger rouge
   **est** le red flag #3 qui s'allume.

## Le contraste avec les couplages Batman × Legal / Finance / People (tour 2)

Le tour 2 a posé 3 couplages Batman × {Aquaman, Wonder Woman, Green
Lantern}. Ces couplages sont **directs** : Batman × Aquaman sur la
double porte périmètre-propriété, Batman × Wonder Woman sur la
récurrence, Batman × Green Lantern sur l'owner absent.

Le couplage Batman × Superman est **indirect** (via Sales) et
**volumique** (charge dérivée, pas blocage catalogue). C'est une
catégorie nouvelle — un couplage par transit, pas un couplage par
veto adjacent.

**Conséquence** : la matrice d'harmonisation teste les **adjacences**,
pas les **transits**. Le couplage Batman × Superman n'est pas un
défaut de la matrice — c'est un **phénomène** que la matrice ne
couvre pas par design.

## Anti-pièges

- **Batman qui bloque Superman sur la base du trigger.** Le trigger
  est une **remontée de fait**, pas un veto. Si Batman bloque
  Superman, il transgresse la doctrine remonte-fait (triplet 56).
- **Trigger confondu avec le red flag #1 ou #3.** Le trigger est un
  **précurseur** de red flag, pas un red flag. Le red flag reste
  binaire (vert/rouge sur la matrice) ; le trigger est continu
  (charge dérivée en %).
- **Batman qui pose LAUNCH_READY rouge sur la base du trigger.**
  Le portique teste des **conditions cataloguées** (veto, red flag,
  trou People, condition d'arrêt manquante — cf. concept
  launch-ready). Le trigger n'est pas une condition cataloguée —
  Batman peut remonter le fait, pas poser rouge.
- **Superman qui ignore le trigger.** Si Superman ne tient pas
  compte de la charge dérivée Ops, c'est une **transgression de
  la propriété 3 du catalogue** (non-négociable au niveau
  mésoperpétuel). Superman ne peut pas passer outre Batman sur le
  run cost, même si la chaîne n'est pas explicite.
- **Calibration Sales sans Batman.** Si JohnJones calibre son taux
  MQL/onboarding sans consulter Batman, le trigger ne s'allume
  jamais et Batman encaisse le défaut silencieusement. C'est le
  trou de calibration que la doctrine canonique n'a pas refermé.

## Liens

- [[domaine-batman-ops-perimetre-frontieres]] — le périmètre qui
  reçoit le volume transitant
- [[batman-veto-condition-arret-procedure]] — le veto qui teste la
  forme, pas le volume
- [[batman-couplage-finance-wonder-woman-recurrence]] — le couplage
  adjacent run cost
- [[batman-couplage-people-green-lantern-owner-absent]] — la chaîne
  Batman → GL → X-Men pour renforcer l'effectif
- [[batman-launch-ready-portique-final-transverse]] — le portique
  qui ne teste pas le volume
- [[b2-harmonization-matrix-exploitable]] — la matrice qui teste les
  transitions, pas les transits
- [[b2-pair-check-raci-by-rank]] — RACI Batman absent des pair-checks
  Growth amont
- [[b2-eight-domain-vetoes-catalogue]] — Superman triplet 25, Batman
  triplet 24, propriété 3 non-négociable

## Note de confiance

**Confirmé par machine pour le constat volumique.** Le fait que
Batman est 2 transitions en aval de Superman est observable dans la
matrice d'harmonisation (9 pair-checks listés, Batman sur #2 et #3
uniquement). Le triplet 25 (Superman veto) est cité verbatim. Le
triplet 56 (Batman remonte-fait) est cité verbatim.

**Reconstruit pour le trigger et les 3 cas.** Le format YAML
`charge_derivee` est **mon inférence** — le format mésoperpétuel
canonique (`b2-meso-decision-packet-spec.md`) ne pose pas ce champ.
Les 3 cas (cadence dépassée, support post-launch, réclamation
post-promesse) sont **projetés** à partir du triplet 25 et de la
doctrine remonte-fait. Le seuil d'alerte 30 % est **arbitraire** —
la matrice ne pose pas de seuil de charge dérivée.

**À arbitrer** : (1) Batman peut-il poser un trigger de charge
dérivée dans le packet mésoperpétuel, ou est-ce un overreach B2 ?,
(2) la matrice 9 pair-checks doit-elle être étendue à 12 pour
inclure les 3 transits Growth → Ops, Sales → IT, Product → People ?,
(3) la calibration MQL/onboarding est-elle un acte Sales seul, ou
un acte partagé Sales × Ops ?. Le canon ne tranche aucun des trois.

---
type: Concept
title: Batman × JohnJones — le taux de signature Sales est un multiplicateur Ops
description: Le pair-check #2 (Sales → Ops) teste la transition d'une promesse signée vers une livraison tenue. Mais le taux de signature (combien de deals signés par mois) est un multiplicateur Ops qui n'est pas posé par le pair-check. Batman encaisse le volume d'onboardings au rythme de JohnJones, sans que ce volume soit un input explicite du DoD Ops.
tags: [batman, john-jones, sales, ops, couplage, signature, onboarding, volume, multiplicateur, b2]
generated: { by: minimax-m3, at: 2026-08-19T05:50:00Z }
verified:
  - { by: process:lecture-b2-corpus-tour-3, at: 2026-08-19T05:50:00Z }
sources:
  - id: harmonization-md
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/areas/business-wheel-harmonization-matrix.md"
    title: Harmonisation — pair-check #2 Sales→Ops teste la promesse tenue, pas le volume
    last_modified: 2026-08-17
  - id: triplet-johnjones-veto
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 27 — JohnJones bloque proposition avant problème reformulé"
    last_modified: 2026-08-17
  - id: triplet-batman-veto
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 24 — Batman bloque procédure sans condition d'arrêt"
    last_modified: 2026-08-17
  - id: avengers-wheel
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/eight-domain-avengers-wheel.md"
    title: Eight Domain Avengers Wheel — JohnJones = Sales 02
    last_modified: 2026-08-17
  - id: b2-pair-check-raci
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-pair-check-raci-by-rank.md"
    title: RACI par rang — Batman A sur #2, JohnJones absent en aval
    last_modified: 2026-08-19
  - id: b2-b3-contract
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-b3-jtbd-handoff-contract.md"
    title: Contrat B2→B3 — DoD chiffré par seuil, onboarding inclus
    last_modified: 2026-08-19
  - id: batman-couplage-superman
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/batman/batman-couplage-superman-growth-volume-charge.md"
    title: Batman × Superman — couplage jumeau par le volume Growth
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Batman × JohnJones — le taux de signature Sales est un multiplicateur Ops

## Le constat — Batman hérite du débit JohnJones sans l'avoir calibré

Le pair-check #2 (Sales → Ops) teste **« les promesses peuvent-elles
être tenues répétitivement ? »** (`business-wheel-harmonization-matrix.md`).
C'est une question sur la **qualité** de la promesse (peut-on
livrer ce qu'on a signé ?), pas sur la **quantité** (combien de
promesses signe-t-on par mois ?).

Le RACI par rang place Batman A sur #2 — Batman **reçoit** la
promesse signée et **hérite** de l'engagement de livraison. Mais
Batman n'a pas d'input sur le **taux de signature** JohnJones —
c'est Sales qui décide combien de deals signer par mois.

**Conséquence** : Batman est dimensionné pour N onboardings/mois.
Si JohnJones signe plus que ce que N peut absorber, Batman encaisse
le retard. Si JohnJones signe moins, Batman a de la capacité
inutilisée. Dans les deux cas, Batman ne peut pas corriger le tir —
il remonte le fait, Summers arbitre.

## Le multiplicateur — chaque signature crée 4 charges Ops

Quand JohnJones signe un deal, Batman encaisse **4 charges
opérationnelles** qui s'additionnent au rythme des signatures :

1. **Onboarding** — chaque signature déclenche un onboarding client.
   Si JohnJones signe 50 deals/mois, Batman lance 50 onboardings.
2. **Configuration initiale** — chaque nouveau client a une
   configuration spécifique (intégration, données, permissions).
   Batman (par son B3 Fantastic Four) tient la charge de
   configuration.
3. **Support初期** — les 30 premiers jours post-signature sont
   notoirement les plus chargés en support (le client découvre
   l'outil, fait des erreurs, demande de l'aide). Batman encaisse
   un **pic** de support初期 par deal signé.
4. **Suivi de promesse** — chaque signature crée un **engagement
   contractuel** que Batman doit tracker (date de livraison, DoD,
   metric de retour). Batman tient le journal de suivi.

Ces 4 charges sont **par-deal** : un deal signé = 1 onboarding + 1
configuration + 1 pic support + 1 ligne de suivi. Si JohnJones
signe 100 deals/mois, Batman encaisse 100 onboardings + 100
configurations + 100 pics support + 100 lignes de suivi.

## Le trou canonique — Batman ne calibre pas le débit amont

Le canon ne pose pas le **débit amont** que Batman peut absorber.
Quelques points de repère partiels :

- Le triplet 10 dit *« chaque VP coupe le rock en 4 sprints
  hebdomadaires »* — c'est un rythme B2, pas un débit.
- Le triplet 13 dit *« B3 dependsOn B2-sprint »* — c'est une
  dépendance, pas un débit.
- Le concept `b2-b3-jtbd-handoff-contract.md` pose un DoD chiffré
  par seuil, mais le seuil est par livrable, pas par flux.

Aucun triplet ne pose un débit *« Batman absorbe N signatures/mois »*.
C'est un **trou canonique** que ce concept signale sans le
combler — la calibration du débit amont est un acte People (Green
Lantern mandate l'effectif) + Sales (JohnJones calibre la signature),
pas un acte Batman.

## Le couplage implicite — Batman remonte le débit, pas la qualité du deal

Conformément à la doctrine remonte-fait (triplet 56), Batman remonte
**le fait** que le débit JohnJones dépasse la capacité Ops. Trois
formes de remontée :

1. **Fait nu** — *« cette semaine, JohnJones a signé 12 deals,
   Batman a onboardé 8. Les 4 autres sont en backlog. »*
2. **Fait avec DoD** — *« le DoD Ops dit 'onboarding sous 5 jours'.
   Cette semaine, 4 onboardings ont dépassé 5 jours. »*
3. **Fait avec red flag** — *« le ratio signatures/onboardings dérive.
   Si JohnJones continue à 12 deals/semaine, le backlog onboarding
   atteint 2 semaines d'ici 3 sprints. Red flag #3 (Sales green,
   Ops/People red) prévisible. »*

**Aucune de ces trois remontées ne donne à Batman le pouvoir
d'arrêter JohnJones.** C'est Summers qui arbitre — soit il mandate
JohnJones de ralentir la signature, soit il mandate Green Lantern
de renforcer l'effectif Ops, soit il mandate Batman d'absorber
(en dégradant un autre DoD).

## Le contraste avec le veto JohnJones (triplet 27)

Le triplet 27 dit *« JohnJones bloque toute proposition envoyée
avant qu'un problème client ait été reformulé et validé par le
client »*. Le veto JohnJones est **catalogue** (classe de décision) :
*« pas de proposition avant reformulation »*.

Ce veto ne dit **rien** sur le **débit** : JohnJones peut signer
10 deals/mois ou 100 deals/mois, le veto teste la qualité de chaque
proposition, pas le volume. C'est un **angle mort** symétrique à
celui du triplet 25 (Superman) : Superman ne teste pas le volume
d'attention, JohnJones ne teste pas le volume de signatures, Batman
encaisse le volume sans veto amont.

## Le partage de juridiction — Batman × JohnJones × Green Lantern

Le couplage Batman × JohnJones sur le volume a un **3ᵉ acteur
obligatoire** : Green Lantern (People). Quand le débit Sales
sature Ops, Batman ne peut pas renforcer l'effectif seul — c'est
Green Lantern qui mandate le recrutement. C'est la chaîne canonique
déjà posée par le concept `batman-couplage-people-green-lantern-owner-absent.md` :
Batman remonte à Summers, Summers mandate Green Lantern, Green
Lantern mandate ProfessorX (triplet 33) ou Beast (triplet 34) pour
le recruiting.

**Trois arbitrages possibles** quand le débit sature :

1. **Ralentir la signature** — JohnJones calibre à la baisse. C'est
   l'arbitrage le **plus défensif** : il préserve la qualité
   (chaque signature est toujours tenue) mais réduit la croissance.
2. **Renforcer Ops** — Green Lantern mandate du recrutement. C'est
   l'arbitrage **le plus coûteux** : il prend 1-2 sprints pour
   onboarder un nouvel Ops (le lag de recrutement).
3. **Absorber en dégradant** — Batman accepte un DoD dégradé
   (onboarding sous 10 jours au lieu de 5). C'est l'arbitrage **le
   plus dangereux** : il crée une dette visible qui s'accumule.

**L'arbitrage optimal combine les 3** : ralentir légèrement +
renforcer progressivement + absorber temporairement en signalant.
C'est la doctrine canonique implicite que Summers applique quand
le cas se présente.

## Le trigger proposé — alerte de débit signature

Symétrique du trigger Batman × Superman (cf. concept
`batman-couplage-superman-growth-volume-charge.md`), je propose un
**trigger de débit signature** dans le packet mésoperpétuel Batman :

```yaml
debit_signature:
  source: johnjones_sales
  cadence_planifiee_ops: <M onboardings/mois>
  volume_mois_courant: <N signatures>
  ratio_implicite: <1.0 si 1 signature = 1 onboarding>
  ecart_pct: <(N - M) / M>
  seuil_alerte: 30%  # écart au-dessus duquel Batman remonte
  statut: vert|orange|rouge
  trigger_red_flag_3: <bool>
```

Le trigger **préempte le red flag #3** (Sales green, Ops/People
red) — c'est le même phénomène, vu côté Batman. Il rend la
dérive visible **avant** que le red flag ne s'allume.

## Anti-pièges

- **Batman qui bloque JohnJones sur le débit.** Le triplet 24 teste
  la condition d'arrêt, pas le débit. Bloquer JohnJones est un
  overreach Batman.
- **Confondre qualité et quantité.** Le veto JohnJones (triplet 27)
  teste la reformulation, pas le volume. Batman remonte le volume,
  pas la qualité des deals.
- **Débit non calibré.** Batman ne calibre pas le débit amont —
  c'est People + Sales. Si Batman impose un débit plafond, il
  empiète sur la chaîne People × Sales.
- **Batman qui absorbe sans remonter.** Si Batman absorbe le débit
  en dégradant silencieusement le DoD onboarding, il transgresse
  la doctrine remonte-fait (triplet 56). Le DoD est signé — Batman
  ne peut pas le dégrader sans consigner.
- **Renforcer Ops sans ralentir Sales.** Si Summers mandate Green
  Lantern de renforcer Ops sans ralentir JohnJones, le coût du
  recrutement est gaspillé — Batman encaisse toujours plus que ce
  qu'il ne peut absorber. Les deux bouts doivent être traités
  ensemble.
- **Lag de recrutement ignoré.** Le recrutement Ops prend 1-2
  sprints. Si Batman remonte le débit trop tard, le lag de
  recrutement ne rattrapera pas la dérive. Le trigger doit
  s'allumer **avant** que le red flag #3 ne s'allume.

## Liens

- [[domaine-batman-ops-perimetre-frontieres]] — le périmètre qui
  encaisse le débit signature
- [[batman-couplage-superman-growth-volume-charge]] — le couplage
  jumeau par le volume Growth (transit indirect)
- [[batman-couplage-people-green-lantern-owner-absent]] — la chaîne
  Batman → Green Lantern → X-Men pour renforcer Ops
- [[batman-launch-ready-portique-final-transverse]] — le portique
  qui ne teste pas le débit
- [[b2-harmonization-matrix-exploitable]] — pair-check #2 et red
  flag #3
- [[b2-pair-check-raci-by-rank]] — Batman A sur #2, JohnJones absent
  en aval
- [[b2-b3-jtbd-handoff-contract]] — DoD chiffré et onboarding inclus
- [[b2-eight-domain-vetoes-catalogue]] — JohnJones triplet 27, Batman
  triplet 24, propriété 3 non-négociable

## Note de confiance

**Confirmé par machine pour le constat de débit.** Le pair-check #2
est posé verbatim par la matrice d'harmonisation. Le triplet 27
(JohnJones veto) est cité verbatim. Le triplet 24 (Batman veto) est
cité verbatim. Le RACI par rang est posé verbatim dans
`b2-pair-check-raci-by-rank.md`.

**Reconstruit pour le trigger et le partage de juridiction.** Le
format YAML `debit_signature` est **mon inférence** — symétrique
du trigger `charge_derivee` posé pour Batman × Superman. Le seuil
d'alerte 30 % est **arbitraire** (par symétrie avec le trigger
Growth). Le partage de juridiction Batman × JohnJones × Green
Lantern (3 arbitrages : ralentir, renforcer, absorber) est **projeté**
depuis la doctrine remonte-fait et la chaîne canonique déjà posée
par `batman-couplage-people-green-lantern-owner-absent.md`.

**À arbitrer** : (1) le seuil 30 % est-il tenable, ou faut-il un
seuil variable par cycle ?, (2) Batman peut-il poser un trigger de
débit signature dans le packet mésoperpétuel, ou est-ce un overreach
?, (3) la calibration du débit signature est-elle un acte People +
Sales, ou un acte partagé Sales × Ops × People ?, (4) le lag de
recrutement Ops (1-2 sprints) doit-il être posé en DoD, ou reste-t-
il implicite ?. Le canon ne tranche aucun des quatre.

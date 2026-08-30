---
type: Concept
title: Batman × Flash — la cadence de livraison Product est un paramètre Ops implicite
description: Le pair-check #3 (Product → Ops) teste si l'artefact est supportable opérationnellement. Mais la cadence à laquelle Flash livre les artefacts (release train) est un paramètre Ops qui n'est pas posé canoniquement : Batman encaisse la charge de changelogs, support, monitoring, et onboarding documentation au rythme de Flash, sans que ce rythme soit un input explicite du DoD Ops.
tags: [batman, flash, product, ops, couplage, cadence, release-train, changelog, support, b2]
generated: { by: minimax-m3, at: 2026-08-19T05:42:00Z }
verified:
  - { by: process:lecture-b2-corpus-tour-3, at: 2026-08-19T05:42:00Z }
sources:
  - id: harmonization-md
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/areas/business-wheel-harmonization-matrix.md"
    title: Harmonisation — pair-check #3 Product→Ops teste la supportabilité, pas la cadence
    last_modified: 2026-08-17
  - id: triplet-flash-veto
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 26 — Flash bloque offre dont la valeur dépend d'une personne nommée"
    last_modified: 2026-08-17
  - id: triplet-batman-veto
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 24 — Batman bloque procédure sans condition d'arrêt"
    last_modified: 2026-08-17
  - id: b2-pair-check-raci
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-pair-check-raci-by-rank.md"
    title: RACI par rang — Batman A sur #3, Flash A sur #4 et #6
    last_modified: 2026-08-19
  - id: b2-b3-contract
    resource: "C:/Users/amadio/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-b3-jtbd-handoff-contract.md"
    title: Contrat B2→B3 — DoD chiffré par seuil, support et run inclus
    last_modified: 2026-08-19
  - id: batman-couple-ops-it
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/batman/batman-couplage-ops-it.md"
    title: Batman × Cyborg — chaîne Product→IT→Ops, red flag #1
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Batman × Flash — la cadence de livraison Product est un paramètre Ops implicite

## Le constat — Batman encaisse la cadence Flash sans qu'elle soit un input DoD

Le pair-check #3 (Product → Ops) teste **« l'artefact est-il
supportable opérationnellement ? »** (`business-wheel-harmonization-matrix.md`).
C'est une question binaire : la feature est-elle supportable oui ou
non ?

Mais la **cadence** à laquelle Flash livre les features n'est pas
testée par le pair-check. Si Flash merge 2 PR/semaine, Batman
encaisse 2 changelogs/semaine. Si Flash merge 10 PR/semaine, Batman
encaisse 10 changelogs/semaine. Le ratio 1:1 est implicite — chaque
feature livrée crée une charge Ops, mais **le multiplicateur n'est
pas posé**.

C'est un angle mort du pair-check #3. Le RACI par rang place Batman
A sur #3, donc Batman **reçoit** l'artefact et **hérite** de la
cadence. Mais Batman n'a pas d'input sur la cadence Flash — Flash est
A sur #4 (Product → IT) et #6 (Finance → Product), pas sur la
fréquence des merges.

## Les 4 charges Ops dérivées de la cadence Flash

Quand Flash livre un artefact, Batman encaisse **4 charges
opérationnelles** qui se cumulent à la cadence des merges :

1. **Changelog** — chaque feature livrée exige une note de version.
   Si Flash merge 10 PR/semaine, Batman publie 10 changelogs/semaine
   (ou 1 changelog agrégé par semaine, mais alors le support ne sait
   pas quelle feature a introduit quelle régression).
2. **Runbook mis à jour** — chaque feature qui change un comportement
   utilisateur exige une mise à jour du runbook support. Si Flash
   merge 10 features qui touchent 10 comportements, Batman met à jour
   10 sections de runbook.
3. **Monitoring** — chaque feature qui a un comportement mesurable
   exige un dashboard ou une alerte. Batman (par son B3 Fantastic
   Four) doit tenir l'observabilité, qui grossit avec chaque feature.
4. **Onboarding documentation** — chaque feature qui devient
   pertinente pour un client exige une mise à jour de l'aide en
   ligne, du guide d'onboarding, des FAQ. Batman encaisse la charge
   éditoriale.

Ces 4 charges sont **incompressibles** : on ne peut pas merger 10
features/semaine et n'en supporter que 2. Chaque feature est
opérationnalisée ou ne l'est pas — et si elle ne l'est pas, c'est
le red flag #1 (Product green, Ops/IT red) qui s'allume.

## Le ratio implicite — Batman est dimensionné pour quelle cadence ?

Le canon ne pose pas le **ratio supportable** Ops/Product. Quelques
chiffres canoniques partiels :

- Le triplet 10 dit *« chaque VP coupe le rock en 4 sprints
  hebdomadaires »* — c'est une cadence B2 vers B1, pas un ratio
  B2 vers un autre B2.
- Le triplet 11 dit *« 5 scrums par semaine, une action exécutable
  par jour »* — c'est une cadence B3 vers B2, pas un ratio B2 vers
  B2.
- Le triplet 13 dit *« B3 dependsOn B2-sprint »* — c'est une
  dépendance, pas un ratio.

Aucun triplet ne pose un ratio Ops/Product du type *« Batman peut
absorber N features/semaine »*. C'est un **trou canonique** que le
tour 1 a signalé (`RAPPORT_dom-batman.md` §5.1.4) sans le combler.

## Le couplage implicite — Batman remonte la cadence, pas la qualité

Conformément à la doctrine remonte-fait (triplet 56), Batman ne
statuera pas sur la cadence Flash. Batman remonte **le fait** que la
cadence dépasse la capacité Ops. Trois formes de remontée possibles :

1. **Fait nu** — *« cette semaine, Flash a mergé 12 PR, Batman en a
   supporté 8. Les 4 autres sont en backlog changelog. »*
2. **Fait avec DoD** — *« le DoD Ops dit 'changelog sous 24h'. Cette
   semaine, 4 changelogs ont dépassé 24h. »*
3. **Fait avec red flag** — *« le ratio features/support dérive. Si
   Flash continue à 12 PR/semaine, le backlog changelog atteint 2
   semaines d'ici 3 sprints. Red flag #1 prévisible. »*

**Aucune de ces trois remontées ne donne à Batman le pouvoir
d'arrêter Flash.** C'est Summers qui arbitre — soit il mandate
Flash de ralentir, soit il mandate Green Lantern de renforcer Ops,
soit il mandate Batman d'absorber (en dégradant un autre DoD).

## Le contraste avec le veto Flash (triplet 26)

Le triplet 26 dit *« Flash bloque toute offre dont la valeur dépend
d'une personne nommée »*. Le veto Flash est **catalogue** (classe
de décision), pas **cadence** (fréquence de livraison). C'est une
différence importante :

- **Veto catalogue** — Flash dit *« je refuse cette feature parce
  que sa valeur repose sur Pierre, qui peut partir »*. C'est un
  blocage ponctuel, sur un cas.
- **Cadence supportable** — Batman dit *« la cadence Flash génère
  une charge Ops non-planifiée »*. C'est un **constat récurrent**,
  pas un blocage ponctuel.

Les deux modes coexistent. Flash peut bloquer une feature (veto
catalogue) ET livrer à une cadence qui sature Ops (charge dérivée).
Batman remonte la cadence, mais ne peut pas bloquer la feature —
c'est Flash qui décide ce qu'il livre, à la cadence qu'il choisit.

## La procédure 4 étapes — quand Batman remonte une cadence qui dérive

Étape 1 — **Mesure**. Batman (ou MrFantastic ProcessDesign) tient
un journal des PR mergées par semaine, avec le delta backlog
changelog. La mesure est hebdomadaire, pas en temps réel — Batman
n'est pas un squad lead, il voit la tendance, pas le tick.

Étape 2 — **Seuil**. Quand le backlog changelog dépasse **1.5x la
cadence supportable** (par exemple : 1.5 semaine de retard sur 1
semaine de livraison), Batman remonte le fait. Le seuil 1.5x est
**arbitraire** — il laisse une marge pour absorber un pic sans
escalader.

Étape 3 — **Packet mésoperpétuel**. Batman consigne le fait dans un
packet avec `decision: noted`, `motif: cadence_product_derivee`,
`impacted_domains: [flash, ops, people]`. Le packet est **non-bloquant**
— c'est une information, pas un veto.

Étape 4 — **Arbitrage Summers**. Si Flash ne ralentit pas et que le
backlog continue à grossir, Summers arbitre. Batman ne peut pas
forcer Flash à ralentir — il remonte, Summers tranche.

## Anti-pièges

- **Batman qui bloque Flash sur la cadence.** Batman n'a pas le
  veto catalogue sur la cadence. Le triplet 24 (Batman veto) teste
  la **présence d'une condition d'arrêt**, pas la cadence. Bloquer
  Flash sur la cadence est un overreach Batman.
- **Confondre cadence et qualité.** Batman remonte la cadence
  (combien), pas la qualité (quoi). Le veto catalogue de Flash
  (triplet 26) teste la valeur nommage-dépendante ; Batman n'a pas
  de prise sur ce veto.
- **Ratio supportable non posé.** Le ratio Ops/Product n'est pas
  dans le canon. Si Batman impose un ratio, il l'invente. Le seuil
  1.5x est **projeté** depuis la pratique sprint (1 sprint
  d'absorption pour 1 sprint de livraison, marge 50 %).
- **Batman qui absorbe sans remonter.** Si Batman absorbe la cadence
  en silence (en dégradant silencieusement le DoD support), il
  transgresse la doctrine remonte-fait (triplet 56). Le DoD est
  signé — Batman ne peut pas le dégrader sans consigner.
- **Summers qui mandate Flash de ralentir sans renforcer Ops.** Si
  Summers mandate Flash de ralentir sans donner à Batman les moyens
  d'absorber le retard, Flash se sent étranglé et Batman continue à
  voir le backlog. C'est un arbitrage incomplet — les deux bouts de
  la chaîne doivent être traités ensemble.

## Liens

- [[domaine-batman-ops-perimetre-frontieres]] — le périmètre qui
  encaisse la cadence
- [[batman-couplage-ops-it]] — la chaîne Product→IT→Ops qui peut
  s'allumer en red flag #1
- [[batman-couplage-superman-growth-volume-charge]] — le couplage
  jumeau par le volume Growth
- [[batman-couplage-people-green-lantern-owner-absent]] — quand
  la cadence exige un renforcement People
- [[batman-launch-ready-portique-final-transverse]] — le portique
  qui ne teste pas la cadence
- [[b2-harmonization-matrix-exploitable]] — pair-check #3 et red
  flag #1
- [[b2-pair-check-raci-by-rank]] — Batman A sur #3, Flash A sur #4
- [[b2-b3-jtbd-handoff-contract]] — DoD chiffré et support inclus

## Note de confiance

**Confirmé par machine pour le constat de cadence.** Le pair-check
#3 est posé verbatim par la matrice d'harmonisation. Le triplet 26
(Flash veto) est cité verbatim. Le triplet 24 (Batman veto) est
cité verbatim. Le RACI par rang est posé verbatim dans
`b2-pair-check-raci-by-rank.md`.

**Reconstruit pour la procédure 4 étapes et le seuil 1.5x.** La
procédure 4 étapes (mesure, seuil, packet, arbitrage Summers) est
**mon inférence** à partir de la doctrine remonte-fait et du format
mésoperpétuel. Le seuil 1.5x est **arbitraire** — il n'est posé
nulle part dans le corpus. Les 4 charges Ops dérivées (changelog,
runbook, monitoring, onboarding doc) sont **projetées** à partir
du périmètre Ops (ProcessDesign, support, monitoring, onboarding).

**À arbitrer** : (1) le seuil 1.5x est-il tenable pour tous les
cycles, ou faut-il un seuil variable par cycle ?, (2) Batman peut-il
tenir un journal des PR mergées, ou est-ce un acte B3 (MrFantastic)
que Batman supervise ?, (3) le ratio supportable Ops/Product doit-
il être posé en DoD signé conjointement Batman × Flash, ou reste-t-
il implicite ?. Le canon ne tranche aucun des trois.

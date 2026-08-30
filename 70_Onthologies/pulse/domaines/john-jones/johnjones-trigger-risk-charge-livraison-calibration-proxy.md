---
type: Concept
title: JohnJones — calibration du trigger risk_charge_livraison par proxy sur Batman ops_handoff_accepted
description: Le tour 3 a posé le trigger risk_charge_livraison avec seuil 0.7 sans calibration empirique. Au 2026-08-19, 0 cas observé d'activation Batman×Sales. Plutôt que de calibrer dans le vide, ce concept propose un trigger proxy sur l'événement mesurable ops_handoff_accepted (Batman accuse réception), avec 3 paliers (0.5 confirmation, 0.7 tension, 0.85 escalation), 3 cas d'application légitime + 3 cas d'abus, et une procédure de calibration rétroactive quand un vrai cas émerge.
tags: [b2, johnjones, sales, trigger, calibration, proxy, ops_handoff_accepted, batman]
generated: { by: minimax-m3, at: 2026-08-19T06:50:00Z }
verified:
  - { by: process:lecture-corpus-sales-tour-4, at: 2026-08-19T06:50:00Z }
sources:
  - id: couplage-batman-redflag3-tour-3
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/john-jones/johnjones-couplage-batman-redflag-3.md"
    title: Couplage Batman×Sales — détection active via red flag #3
    last_modified: 2026-08-19
  - id: cycle-5-phases
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/john-jones/johnjones-cycle-de-vie-reformulation-5-phases.md"
    title: Cycle de vie reformulation-validée 5 phases — Phase 5 Activation Ops
    last_modified: 2026-08-19
  - id: batman-dormance-procedure
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/batman/batman-dormance-procedure-6e-dimension.md"
    title: Batman — dormance procédure 6e dimension
    last_modified: 2026-08-19
  - id: green-lantern-formule-charge
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/green-lantern/green-lantern-formule-charge-carte.md"
    title: Green Lantern — formule charge C(o)=Σpoids/capacité + 3 modes pondération
    last_modified: 2026-08-19
  - id: harmonization-redflags
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/areas/business-wheel-harmonization-matrix.md"
    title: Red flag #3 — Sales green, Ops/People red = risque charge de livraison
    last_modified: 2026-08-17
okf_version: "0.2"
---

# JohnJones — calibration du trigger risk_charge_livraison

## Le constat tour 3

`johnjones-couplage-batman-redflag-3.md` §« Trigger et procédure »
pose le trigger `risk_charge_livraison` avec **seuil 0.7** comme
limite de basculement vers la détection Batman×Sales du red flag #3
(Sales green, Ops/People red = risque charge de livraison). Le seuil
0.7 est **projeté** — il n'a pas été calibré sur observation.

Au 2026-08-19, le compteur Batman×Sales est **0 cas** sur 3 vagues.
Sans cas réel, calibrer 0.7 est un réglage dans le vide. La question
*« pourquoi 0.7 et pas 0.5 ou 0.85 ? »* n'a pas de réponse basée.

## L'option proxy : observer Batman côté ops_handoff_accepted

Plutôt que de calibrer dans le vide, le trigger peut s'appuyer sur un
**événement proxy mesurable** : `ops_handoff_accepted` (cf.
`johnjones-cycle-de-vie-reformulation-5-phases.md` §Phase 5
Activation Ops).

`ops_handoff_accepted` est l'événement où Batman accuse réception
d'un `OPS_HANDOFF_REQUEST.md` Sales et calibre la charge Ops
tenable. C'est un événement **binaire observable** (il se produit
ou il ne se produit pas), avec un **timestamp** et un **contenu**
(la calibration Ops).

Trois propriétés du proxy :

1. **Mesurable** — Batman consigne l'accusé dans le journal, ou le
   packet mésoperpétuel correspondant.
2. **Daté** — la fenêtre 60j du compteur empirique veto
   reformulation-validée (cf.
   `johnjones-protocole-empirique-zero-cas-procedure-remplacement.md`)
   s'applique directement.
3. **Liée** — chaque `ops_handoff_accepted` est l'aboutissement d'un
   cycle Sales Phase 5 (Activation Ops), donc une reformulation
   validée + liée qui ouvre la transition vers Ops.

Conséquence : **chaque `ops_handoff_accepted` est un cas potentiel
de calibration du `risk_charge_livraison`**. Le trigger devient
calibrable rétrospectivement.

## Trois paliers proposés

Plutôt qu'un seuil unique 0.7, trois paliers explicites avec
signification différente :

| Palier | Signification | Action Sales | Action Batman |
|---|---|---|---|
| **0.5** | Confirmation — l'accusé réception Ops arrive en 7 jours, charge Ops ≤ 70% capacité | Continue | Continue |
| **0.7** | Tension — l'accusé réception Ops arrive en 7 jours mais charge Ops entre 70% et 90% capacité, ou retard accusé 8-14 jours | Alerte Captain | Surveillance accrue |
| **0.85** | Escalation — l'accusé réception Ops tarde > 14 jours, ou charge Ops > 90%, ou Batman oppose veto procédure-sans-condition | Arbitrage Council | Pause handoff |

C'est une **gradation ternaire** au lieu d'une binarité à seuil. La
gradation permet de capturer la nuance entre *« Ops accuse et ça
passe »* (0.5) et *« Ops accuse avec peine »* (0.7) sans tomber
directement dans l'arbitrage.

## Trois cas d'application légitime

### Cas #1 — `ops_handoff_accepted` en 5 jours, charge Ops 60%

Palier 0.5 (confirmation). Cycle Sales 5 phases tient, cycle Ops 5
phases entre en Phase 1 (conception) sans dérive. Le trigger ne
s'active pas.

### Cas #2 — `ops_handoff_accepted` en 10 jours, charge Ops 75%

Palier 0.7 (tension). Le retard d'accusé réception (10 jours vs
cible 7 jours) déclenche l'alerte Captain. JohnJones ouvre un
suivi Batman×Sales sur la charge — sans arbitrage Council. Si la
tension se résout en sprint suivant, retour à 0.5.

### Cas #3 — `ops_handoff_accepted` en 18 jours, charge Ops 95%

Palier 0.85 (escalation). Le retard > 14 jours et la charge Ops >
90% déclenchent un arbitrage Council. JohnJones et Batman
co-signent un packet mésoperpétuel : motif *« handoff Ops stalled,
charge Ops saturée »* », mode = negotiation, décision =
`escalate_to_B1` si Batman ne peut pas re-scope.

## Trois cas d'abus

### Abus #1 — Activer 0.7 sur un retard de 8 jours inexpliqué

Le retard accusé réception Ops 8 jours peut être causé par un
événement sans lien (Batman en vacances, cycle Ops en dormant). Le
trigger 0.7 ne s'active pas sur le retard seul — il faut que la
charge Ops soit effectivement entre 70% et 90%.

### Abus #2 — Activer 0.85 sur une charge Ops 91% sans escalade

Le seuil 0.85 déclenche une escalation Council, pas une pause
unilatérale Sales. JohnJones qui suspend le handoff sans arbitrage
Council casse la procédure canonique (cf.
`b2-council-arbitrage-rule.md` §« Pourquoi pas B1 »).

### Abus #3 — Calibrer rétrospectivement sur des `OPS_HANDOFF_REQUEST.md` antérieurs

La calibration rétroactive est légitime **après** un vrai cas. Elle
n'est pas légitime **avant** d'avoir observé un seul cas. Un
JohnJones qui calibre 0.7 sur 5 handoffs antérieurs sans avoir
observé de cas réel est en train de fabriquer le compteur.

## La procédure de calibration rétroactive

Quand un vrai cas émerge (par exemple le cas #3 ci-dessus), la
calibration rétroactive procède en 4 étapes :

1. **Constat du cas** — JohnJones consigne le cas dans le journal
   Council avec timestamp et charge Ops mesurée.
2. **Recalcul du palier** — le cas #3 active 0.85, le palier 0.85
   est confirmé par l'observation.
3. **Mise à jour de la cible** — si le palier 0.85 s'active sur 1
   cas /60j, la cible devient *« ≥ 1 cas 0.85 /120j »* (1 cas
   tendu, pas 1 cas bloqué).
4. **Validation Council** — le packet mésoperpétuel
   `B2-MESO-DECISION-YYYY-NN` documente la calibration. Format cf.
   `b2-meso-decision-packet-spec.md`.

## Asymétrie avec les autres triggers Batman

Batman tour 4 pose le `ops_handoff_accepted` (cf.
`batman-dormance-procedure-6e-dimension.md` §« Trigger ops_handoff_accepted »)
comme événement jonction avec Sales. La symétrie est :

| Trigger | Captain sponsor | Captain aval | Seuil implicite |
|---|---|---|---|
| `risk_charge_livraison` | JohnJones (Sales) | Batman (Ops) | 0.7 projeté |
| `ops_handoff_accepted` | Batman (Ops) | JohnJones (Sales) | non posé en tour 3 |

Batman définit l'événement jonction, JohnJones doit définir le
trigger de calibration. C'est une **asymétrie de tour** : Batman a
avancé sur la jonction, JohnJones n'a pas encore calibré le trigger
qui observe la jonction.

L'option proxy résout l'asymétrie : Batman fournit l'événement
observable, JohnJones calibre le trigger qui observe l'événement.

## Anti-pièges

- **Calibrer 0.7 sans observation.** Le seuil 0.7 n'a pas de sens
  tant qu'aucun cas réel n'a été observé. La procédure de
  calibration rétroactive est la seule voie défendable.
- **Confondre calibration du trigger et création du trigger.** Le
  trigger `risk_charge_livraison` est créé tour 3 — la calibration
  est un raffinement, pas une création.
- **Activer 0.85 sur la base d'un retard seul.** Le retard
  d'accusé réception Ops n'est pas suffisant — il faut la charge
  Ops effective.
- **Suspension unilatérale du handoff Sales à 0.85.** Le seuil 0.85
  déclenche un arbitrage Council. Sales ne suspend pas seul.
- **Ignorer la formule de charge Green Lantern.**
  `green-lantern-formule-charge-carte.md` pose une formule
  C(o) = Σpoids / capacité, avec 3 modes pondération (horizon,
  criticité, couplage). La calibration `risk_charge_livraison`
  devrait à terme s'appuyer sur cette formule, pas la concurrencer.

## Liens

- [[johnjones-couplage-batman-redflag-3]] — le trigger tour 3 et
  le seuil 0.7 projeté
- [[johnjones-cycle-de-vie-reformulation-5-phases]] — Phase 5
  Activation Ops et le trigger `ops_handoff_accepted`
- [[johnjones-protocole-empirique-zero-cas-procedure-remplacement]] —
  procédure de remplacement quand 0 cas /60j
- [[batman-dormance-procedure-6e-dimension]] — symétrie Batman
  `ops_handoff_accepted`
- [[green-lantern-formule-charge-carte]] — formule charge canonique
  C(o) à terme mobilisable
- [[b2-council-arbitrage-rule]] — l'arbitrage Council pour palier 0.85
- [[b2-meso-decision-packet-spec]] — format packet mésoperpétuel
  pour la calibration

## Note de confiance

**Confirmé par machine.** Le trigger `risk_charge_livraison` et le
seuil 0.7 sont cités verbatim de
`johnjones-couplage-batman-redflag-3.md` §« Trigger et procédure ».
Le compteur 0 cas Batman×Sales sur 3 vagues est cité verbatim de
ETAT_DOMAINES vagues 1+2+3 (ligne 27 Batman tour 4). Le
`ops_handoff_accepted` est cité verbatim de
`johnjones-cycle-de-vie-reformulation-5-phases.md` §Phase 5.

Les 3 paliers (0.5, 0.7, 0.85) sont **projetés** depuis le seuil
0.7 canonique — la gradation ternaire est une construction, pas un
élément du corpus. Les 3 cas d'application légitime et les 3 cas
d'abus sont **projetés** par analogie avec la doctrine veto
catalogue (5 cas légitime / 5 cas abusif cf.
`johnjones-veto-reformulation-validee.md` §Cas concrets). La
procédure de calibration rétroactive 4 étapes est **reconstruite**
depuis la procédure de remplacement tour 4 §4 étapes.

À vérifier en cycle réel : (1) les paliers 0.5/0.7/0.85 sont-ils
réalistes ou faut-il des paliers différents ? (2) la formule de
charge Green Lantern est-elle mobilisable côté Sales ? (3) Batman
accepte-t-il la co-signature des cas 0.85 ?
---
type: Concept
title: Aquaman — antisèche, détection du veto abusif politique (4 signaux canoniques)
description: [[b2-eight-domain-vetoes-catalogue]] pose un anti-piège : « veto utilisé comme outil politique ». Cet anti-piège est une mise en garde, pas un détecteur opérationnel. Ce concept formalise **4 signaux canoniques** de veto abusif politique, **3 remèdes** par niveau de sévérité, et une procédure 5 étapes pour transformer l'anti-piège en doctrine opposable. Calqué sur la doctrine Batman « remonte à Summers des faits, pas des décisions » (triplet 56) — Aquaman doit tenir le veto, pas le politics de ses déclenchements.
tags: [b2, aquaman, veto, abus, politique, antisèche, détection, signal, doctrine, faits, decision]
generated: { by: minimax-m3, at: 2026-08-19T06:45:00Z }
verified:
  - { by: process:lecture-b2-corpus-tour-5, at: 2026-08-19T06:45:00Z }
sources:
  - id: b2-eight-domain-vetoes
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-eight-domain-vetoes-catalogue.md"
    title: Catalogue des 8 vetos B2 — anti-pièges
    last_modified: 2026-08-19
  - id: triplet-56-batman-fait
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 56 — Batman remonte à Summers des faits, pas des décisions"
    last_modified: 2026-08-17
  - id: triplet-57-batman-veto-fait
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 57 — Batman veto remonte à Summers comme un fait"
    last_modified: 2026-08-17
  - id: triplet-30-aquaman-veto
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 30 — Aquaman bloque engagement-sans-périmètre"
    last_modified: 2026-08-17
  - id: b2-council-arbitrage-rule
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-council-arbitrage-rule.md"
    title: B2 Council — qui tranche quand deux domaines se contredisent
    last_modified: 2026-08-19
  - id: aquaman-defensibility-triple-signature
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-defensibility-triple-signature.md"
    title: Aquaman — triple signature (fait-défense)
    last_modified: 2026-08-19
  - id: aquaman-veto-amendment
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-veto-amendment-perimetre-insuffisant.md"
    title: Aquaman — 2 amplifications candidates
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Aquaman — antisèche, détection du veto abusif politique

## L'anti-piège canon non-opérationnel

[[b2-eight-domain-vetoes-catalogue]] pose un anti-piège parmi
quatre :

> *« Veto utilisé comme outil politique. Le veto catalogue est un
> filet de sécurité. Un capitaine qui l'invoque pour des raisons
> personnelles (jalousie, défense de territoire) casse sa légitimité.
> Le signal : un veto qui revient systématiquement sur les mêmes
> domaines est probablement un veto politique, pas un veto catalogue. »*

L'anti-piège est une mise en garde — il ne dit pas *comment*
détecter, *qui* détecte, ou *quoi faire* quand le signal est
levé. La doctrine Batman remonte-faits (triplet 56) est l'archétype
du bon comportement B2 — Batman remonte à Summers des **faits**,
pas des décisions.

Ce concept formalise **4 signaux canoniques de veto abusif
politique** applicable à Aquaman, et transforme l'anti-piège en
doctrine opposable.

## Les 4 signaux canoniques de veto abusif politique

| # | Signal | Détection | Sévérité |
|---|---|---|---|
| 1 | **Veto systématique sur un même domaine B2**. Un Aquaman qui oppose son veto à > 60% des mandats d'un même captain B2 (par exemple Superman) sur 3+ cycles consécutifs. | Compteur annuel par captain cible. Seuil : 60%+ / 3 cycles | Élevée |
| 2 | **Veto sans motif vérifiable**. Un veto Aquaman qui n'est pas tracé dans `B2_DC_DIRECTION_COUNCIL_DECISIONS.md` avec un motif consultable par un tiers. | Audit packet Council — chaque veto tracé avec ligne `motif` non-vide. | Élevée |
| 3 | **Veto levé sans amendement**. Un veto Aquaman qui est levé sans que le mandat amendé apparaisse dans le packet Council subséquent (`decision: accepted` sans `amendement: ...`). | Audit packet — corrélation veto levé / mandat amendé. | Modérée |
| 4 | **Veto opposé sans gating input vérifié**. Un Aquaman qui oppose son veto sur un mandat sans avoir validé les gating inputs (par exemple sans avoir lu le feature spec Flash). | Audit Aquaman gate-state-update — chaque veto avec au moins 1 gating input vérifié. | Modérée |

## Les 3 niveaux de sévérité et leur remède

### Sévérité modérée (signaux 3 et 4)

**Remède** : revue trimestrielle du compteur veto par captain
sponsor + comité Aquaman self-review. Aquaman doit documenter
chaque veto levé sans amendement visible (signal 3) ou opposé
sans gating input (signal 4) dans un rapport trimestriel Council.

**Procédure** :

1. Aquaman recompte trimestriellement (T-13 sprint) les vetos
   posés.
2. Pour chaque veto levé sans amendement (signal 3) ou opposé
   sans gating input (signal 4), Aquaman note le contexte.
3. Aquaman rédige un rapport trimestriel `aquaman-veto-review-YYYY-QN`
   dans le dossier Aquaman (pas dans le journal Council — c'est
   self-review).
4. Le rapport est consultable par les autres capitaines B2 sur
   demande.

### Sévérité élevée (signaux 1 et 2)

**Remède** : revue ad hoc du Council avec motion de censure
explicite. Aquaman doit répondre de l'abus devant Council en
séance plénière.

**Procédure** :

1. Le captain cible (par exemple Superman) ou un captain pair
   (par exemple Batman) demande une motion de censure sur signal
   1 ou 2.
2. La motion est inscrite au journal Council avec motif
   (par exemple `motion: censure_aquaman, signal: 1, captain:
   superman, period: 2026-Q3`).
3. Aquaman répond en séance plénière (5/8 quorum).
4. Le Council tranche par vote majorité simple si la motion est
   fondée → Aquaman doit amender son veto, ou escalade B1 si
   l'amendement est insuffisant.

### Sévérité critique (abus persistant après censure)

**Remède** : escalade B1 pour réécriture de la règle catalogue.
Le Council ne peut pas réécrire un veto catalogue — seul B1 peut.

**Procédure** :

1. Aquaman ne modifie pas sa pratique après motion de censure
   fondée (par exemple : continue à opposer le veto dans les
   mêmes conditions 3 cycles après la motion).
2. Le captain demandeur escalade B1 avec packet
   `escalate_to_B1: aquaman_veto_politique, signals: ...`.
3. B1 tranche la réécriture de la règle catalogue.

## La procédure 5 étapes pour transformer l'anti-piège en doctrine opposable

Pour qu'Aquaman applique l'antisèche de manière systématique (pas
ad hoc), la procédure suit 5 étapes :

### Étape 1 — Pose des compteurs (Aquaman self-instrument)

Aquaman tient un compteur annuel dans son dossier Aquaman :

- `aquaman-veto-counter-YYYY.csv` avec colonnes : `packet_id`,
  `motif_category`, `captain_targeted`, `decision_date`,
  `amended` (bool), `gating_input_verified` (bool).

### Étape 2 — Recompte mensuel

Aquaman recompte à chaque Council mensuel (cf.
[[b2-council-cadence-and-chair]] §Séance hebdomadaire) :

- Total vetos posés.
- Ventilation par captain ciblé.
- Ventilation par catégorie de motif (périmètre insuffisant / IP
  non déclarée / autre).
- Taux d'amendement (signal 3).
- Taux de gating input vérifié (signal 4).

### Étape 3 — Détection seuils

Si un seuil de sévérité est franchi :

- Signal 1 (>60% même captain / 3 cycles) → sévérité élevée.
- Signal 2 (veto sans motif vérifiable) → sévérité élevée.
- Signal 3 (>30% levés sans amendement) → sévérité modérée.
- Signal 4 (>20% opposés sans gating input) → sévérité modérée.

### Étape 4 — Application du remède

Selon le niveau de sévérité (modéré / élevé / critique) :

- Modéré → revue trimestrielle Aquaman self-review.
- Élevé → motion de censure Council.
- Critique → escalade B1.

### Étape 5 — Traçabilité D4

Chaque déclenchement d'antisèche produit une ligne dans le
journal Council (`decision: antisèche_sealed, signals: ...,
remedy: ...`). La traçabilité évite que l'antisèche devienne un
outil de contre-pouvoir.

## Le test de cohérence avec les autres domaines

L'antisèche Aquaman doit être **cohérente avec celle des 7 autres
capitaines**. Batman a son antisèche via la doctrine remonte-faits
(triplet 56) : Batman qui ne remonte pas le fait mais la décision
rompt la doctrine. Wonder Woman a son antisèche via la doctrine
F19-F22 allocation (cf. concept tour 3 WW). Superman a son
antisèche via la doctrine MQL-SQL handoff (cf. concept tour 2
Superman).

**Calque** : l'antisèche Aquaman doit être calquée sur la
doctrine Batman remonte-faits.

| Batman antisèche | Aquaman antisèche |
|---|---|
| Batman remonte à Summers **des faits**, pas des décisions | Aquaman oppose un veto **sur un fait**, pas une opinion politique |
| Batman veto est remonté comme **un fait** (triplet 57) | Aquaman veto est tracé dans `B2_DC_DIRECTION_COUNCIL_DECISIONS.md` avec motif |
| Batman auto-discipline par compteur (rapport 0 cas observé) | Aquaman auto-discipline par compteur trimestriel |

**Conséquence** : l'antisèche Aquaman n'est pas un outil
nouveau — c'est un **mirror** de la doctrine Batman, appliquée à
la posture Aquaman. Le triplet 57 donne le canevas : *« Aquaman
veto remonte à Summers comme un fait »* (par symétrie avec
Batman).

## Le couplage avec la triple signature phase 5

La triple signature [[aquaman-defensibility-triple-signature]] est
un **fait-défense** : Aquaman ne peut pas politically manipuler le
veto si la triple signature est tracée, parce que Batman et Thena
sont co-signataires. La triple signature est *elle-même* une
antisèche structurelle — Batman et Thena peuvent signaler un veto
politique au moment de la signature.

**Conséquence** : un veto politique Aquaman devient *visible* au
moment de la triple signature. Batman peut refuser de signer et
escalader au Council.

## Les 3 abus que cette doctrine ne couvre pas

Trois abus possibles que l'antisèche ne détecte pas :

1. **Veto opportun**. Un Aquaman qui oppose son veto au moment
   opportun (pas systématique), pour pousser un agenda personnel
   sans qu'aucun seuil de sévérité ne soit franchi. **Détection** :
   recompte qualitatif — pas seulement quantitatif.
2. **Veto implicite**. Un Aquaman qui n'oppose pas son veto
   formellement mais qui retarde la production jusqu'à ce que le
   demandeur abandonne. **Détection** : timestamping packet +
   recompte délai review Aquaman.
3. **Veto sélectif par tier**. Un Aquaman qui oppose son veto
   seulement à certains clients / prospects (par exemple : veto
   systématique sur les clients EU, pas sur US). **Détection** :
   recompte par tier client + audit motif.

**Remède** : compléter l'antisèche par un audit annuel tier
client (S2 du calendar Aquaman).

## Anti-pièges

- **Antisèche comme outil de contre-pouvoir**. Aquaman qui utilise
  l'antisèche pour pousser un agenda personnel (par exemple :
  forcer un Superman à respecter une procédure Aquaman-spécifique
  en citant l'antisèche Batman) casse sa propre doctrine.
- **Recompte Aquaman non audité**. Un recompte fait par Aquaman seul,
  sans audit externe, ouvre la porte à un Aquaman qui sous-compte
  ses abus. Le rapport trimestriel Aquaman doit être audité par un
  captain pair (par exemple Batman) ou par le Council.
- **Seuils trop élevés**. Si les seuils (60% / 30% / 20%) sont
  trop élevés, l'antisèche ne se déclenche jamais. Si trop bas,
  elle se déclenche trop souvent et casse la pratique. **Calibration
  par cycle 12WY** : ajuster les seuils selon la pratique observée.
- **Motion de censure abusive**. Un captain (par exemple Superman)
  qui dépose une motion de censure Aquaman sans основания
  légitime (par exemple pour pousser un agenda Growth-spécifique)
  casse sa propre légitimité. La motion doit être documentée avec
  motifs vérifiables.

## Liens

- [[b2-eight-domain-vetoes-catalogue]] — l'anti-piège canon qui
  motive ce concept
- [[triplet-56]] Batman remonte-faits — l'archétype de la doctrine
  antisèche
- [[triplet-57]] Batman veto-fait — la doctrine qui ancre l'antisèche
  B2
- [[aquaman-defensibility-triple-signature]] — la triple signature
  comme antisèche structurelle
- [[aquaman-veto-amendment-perimetre-insuffisant]] — les 2
  amplifications candidates qui peuvent être l'objet d'abus
- [[aquaman-veto-amplification-ordre-canonique]] — l'ordre canonique
  qui peut être inversé abusivement
- [[b2-council-arbitrage-rule]] — le Council qui tranche les motions
  de censure
- [[b2-council-cadence-and-chair]] — la cadence Council mensuelle
  pour les motions

## Note de confiance

**Reconstruit à partir d'un anti-piège canon.**

- ✅ Anti-piège canon [[b2-eight-domain-vetoes-catalogue]] cité
  verbatim.
- ✅ Triplets 56, 57, 30 cités verbatim.
- 🟡 Les 4 signaux canoniques sont des **opérationnalisations**
  de l'anti-piège canonique. Pas de triplet canonique les ancrant
  formellement. À soumettre au Council pour adoption.
- 🟡 Les seuils (60% / 30% / 20%) sont des **projections
  pragmatiques** depuis la pratique. **Pas de calibration cycle
  réel** — à calibrer en cycle Aquaman ACTIVE.
- ❌ Non vérifié en cycle : aucun veto Aquaman réel n'a été
  observé en Vague 1+2+3+4. L'antisèche est **prospective**.
  L'**audit tier client annuel** n'est pas non plus observé.

---
type: Concept
title: Aquaman — portique d'entrée LAUNCH_READY : 4 items à vetter, 3 cas de refus
description: Quand Batman émet `LAUNCH_READY` (portique final transverse, cf. [[eight-domain-avengers-wheel]] ligne 43), Aquaman est un des inputs. Le portique Aquaman tient 4 items : contract-templates-courants, claims-safe, privacy-chain-documentée, defensibility-binder-à-jour. Trois cas de refus déclenchent un `BLOCKED_RISK` qui empêche `LAUNCH_READY` ; les autres cas bloquent par une **attente** Aquaman qui se résout avant le portique. Timing cible : T-7j avant launch.
tags: [b2, aquaman, batman, launch-ready, portique, gate, final, transverse]
generated: { by: minimax-m3, at: 2026-08-19T05:55:00Z }
verified:
  - { by: process:lecture-canon-aquaman-tour-4, at: 2026-08-19T05:55:00Z }
sources:
  - id: avengers-wheel
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/eight-domain-avengers-wheel.md"
    title: "Eight Domain Avengers Wheel — Ops LAUNCH_READY (transverse gate final), ligne 43"
    last_modified: 2026-08-17
  - id: aquaman-defensibility
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-defensibility-triple-signature.md"
    title: Aquaman triple signature — le binder de defensibilité
    last_modified: 2026-08-19
  - id: aquaman-classification
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-classification-risques-4-formes.md"
    title: Aquaman classification des risques en 4 formes et mapping gate
    last_modified: 2026-08-19
  - id: aquaman-jtbd
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-jtbd-emit-receive.md"
    title: Aquaman catalogue JTBD émis et reçus
    last_modified: 2026-08-19
  - id: batman-rapport-tour-2
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/ETAT_DOMAINES.md"
    title: "ETAT_DOMAINES — Batman tour 2 mentionne LAUNCH_READY portique final transverse"
    last_modified: 2026-08-19
  - id: harmonization-md
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/areas/business-wheel-harmonization-matrix.md"
    title: "Harmonisation de la wheel — Red flag #1 Product green Ops/IT red, #5 Legal red + public-facing"
    last_modified: 2026-08-17
okf_version: "0.2"
---

# Aquaman — portique d'entrée LAUNCH_READY : 4 items à vetter, 3 cas de refus

## Pourquoi Aquaman est un portique d'entrée, pas un portique final

La doctrine canonique pose Batman (Ops) comme **portique final transverse**
(cf. [[eight-domain-avengers-wheel]] ligne 43 : `LAUNCH_READY` = *« transverse
gate final »*). Batman signe, le produit lance. Mais Batman n'est pas omniscient
: il dépend des inputs des 7 autres capitaines pour savoir si le launch est
sûr. **Aquaman est un des inputs du portique** — un portique *d'entrée*,
c'est-à-dire un des 7 signaux que Batman agrège avant de signer le `LAUNCH_READY`.

**Conséquence** : un `BLOCKED_RISK` Aquaman **ne produit pas directement** un
`BLOCKED_LAUNCH` (réservé à Batman), mais **empêche** Batman d'émettre
`LAUNCH_READY`. Le `BLOCKED_RISK` est un veto d'input, pas un veto final.

## Les 4 items qu'Aquaman vette

### Item 1 — Contract-templates à jour

Les **clauses-types** exportées par Aquaman (NDA, terms of service, privacy
policy, IP-assignment, limitation de liability — cf. Forme 3 du catalogue
[[aquaman-jtbd-emit-receive]]) doivent être **à jour avec la dernière
régulation applicable**. Pas de clause obsolète connue par Aquaman.

**Source de vérité** : la matrice de clauses canonique maintenue par Aquaman.
Si Aquaman ACTIVE n'a pas cette matrice, l'item **échoue par défaut** —
`NEEDS_REVIEW` jusqu'à constitution.

### Item 2 — Claims safe pour publication

Toutes les **claims publiques** associées au launch (site web, brochure sales,
deck investisseurs, ABM outreach — pas l'internal comm) doivent avoir passé
la Forme 2 du catalogue JTBD Aquaman (cf.
[[aquaman-classification-risques-4-formes]] §Classe 2).

**Source de vérité** : la liste des claims signée par Superman (Growth) et
corroborée par `LEGAL_READY` Aquaman. Si une claim a `BLOCKED_RISK` Aquaman
non-amendé, l'item **échoue** — `BLOCKED_RISK` jusqu'à amendement.

### Item 3 — Privacy chain documentée

Le **chemin privacy** end-to-end (de la collecte au storage au delete) doit
être documenté pour chaque surface de données touchée par le produit lancé.
Documentation = DPI réalisée (Data Protection Impact), retention chiffrée en
jours, IAM documenté (qui accède, pourquoi, combien de temps).

**Source de vérité** : la privacy review Aquaman (Forme 1 du catalogue JTBD)
avec input Cyborg (implémentation). Si une surface n'a pas de privacy
review, l'item **échoue** — `BLOCKED_RISK` jusqu'à complétion.

### Item 4 — Defensibility binder à jour

Un **binder de defensibilité** (Forme 4 du catalogue JTBD, triple signature
Aquaman + Batman + Thena — cf. [[aquaman-defensibility-triple-signature]])
doit être **à jour** ou **proactivement déclenché** par Aquaman dans le
cadre du launch.

**Source de vérité** : `00_Summers_CEO/03_Master_Agreements/defensibility/`
ou un dossier équivalent. Si le binder n'existe pas et que la régulation
sectorielle le requiert (par exemple AI Act, RGPD extension, sector
finance/health), l'item **échoue** — `BLOCKED_RISK`.

## Les 3 cas de refus (= `BLOCKED_RISK`)

Un `BLOCKED_RISK` Aquaman sur le portique `LAUNCH_READY` est un **arrêt dur**
qui empêche Batman d'émettre `LAUNCH_READY`. Trois cas déclencheurs :

### Cas R1 — Claim non-safe irrésolue

Une claim publique associée au launch a reçu `BLOCKED_RISK` Aquaman et n'a
**pas été amendée** par Superman avant T-7j. Superman a la porte de sortie :
amender la claim (reformulation, retrait, distinction). S'il ne le fait pas,
le launch est **gelé**.

**Distinction avec le red flag #5** : `b2-harmonization-matrix-exploitable.md`
§Red flag #5 pose *« Legal red + public-facing work : geler les claims et le
launch »*. C'est **exactement** le cas R1. Aquaman le précise en lui donnant
une procédure : un portique d'entrée avec T-7j, pas un red flag détecté à
T-1.

### Cas R2 — Privacy breach non-documentée

Une surface de données touche le produit mais n'a **pas de privacy review
Aquaman** complétée. Cyborg peut livrer une implémentation privacy-correct
sans qu'Aquaman l'ait validée — c'est ce cas qui déclenche R2.

**Distinction avec le couplage Aquaman ↔ Cyborg** (cf.
[[aquaman-couplages-invisibles]] §Couplage 1) : le couplage dit *« la privacy
review Aquaman touche les choix IT »*. Le cas R2 dit *« sans review
documentée, le launch est gelé »*. Le R2 est la **conséquence portique** du
couplage non-documenté.

### Cas R3 — Binder de defensibilité manquant

Une régulation sectorielle émergente (par exemple AI Act entrant en vigueur
à T-30j du launch) impose un binder de defensibilité qui n'a pas été
initié. Le cas R3 est l'**équivalent proactif** de la Forme 4 réactive — au
lieu d'attendre un incident, Aquaman exige le binder *avant* le launch.

**Distinction avec la triple signature réactive** : la triple signature
réactive ([[aquaman-defensibility-triple-signature]] §Cas 1-4) est
*post-incident*. Le cas R3 est *pré-launch* — un binder de préparation,
pas un binder de réponse.

## Timing cible — T-7j

Le portique Aquaman vise **T-7j avant launch**. Pourquoi 7 jours ?

- T-7j laisse à Superman le temps d'amender une claim (Cas R1) — un cycle de
  relecture de 48h + un cycle de reformulation de 96h = ~6 jours.
- T-7j laisse à Cyborg le temps de compléter une privacy review manquante
  (Cas R2) — la review Aquaman prend ~3 jours, l'implémentation Cyborg
  prend ~4 jours.
- T-7j laisse à Aquaman le temps d'initier un binder proactif (Cas R3) —
  la triple signature prend ~5 jours (cf. [[aquaman-defensibility-triple-signature]]
  §Lead indicator).

**Cycle antérieur** : le portique Aquaman n'est **pas** T-1 (jour du launch) —
c'est trop tard pour amender quoi que ce soit. T-7j est l'horizon opérationnel
qui permet une réaction dans le sprint.

**Cycle postérieur** : à T-0 (jour du launch), Batman collecte les 7 inputs
(Aquaman + Superman + Flash + JohnJones + Cyborg + Wonder Woman + Green
Lantern) et émet `LAUNCH_READY` *agrégé*. Le portique Aquaman n'est qu'une
contrainte parmi d'autres — pas la seule.

## Les cas d'attente (`NEEDS_REVIEW`)

Les 4 items ci-dessus ont aussi des **cas d'attente** (`NEEDS_REVIEW`) qui ne
bloquent pas le launch mais signalent une fragilité :

- **Contract-template en cours de mise à jour** : item 1 en `NEEDS_REVIEW`,
  launch proceed avec mention *« template v(n-1) utilisée, v(n) en cours »*.
- **Claims en cours de reformulation** : item 2 en `NEEDS_REVIEW`, launch
  proceed à condition que Superman livre une `LEGAL_READY` avant T-0.
- **Privacy review en cours** : item 3 en `NEEDS_REVIEW`, launch proceed à
  condition que Cyborg + Aquaman closent la review avant T-0.
- **Binder en cours d'initiation** : item 4 en `NEEDS_REVIEW`, launch proceed
  à condition que le binder soit signé avant T+30j (post-launch acceptable
  pour le portique *transverse*, pas pour le portique Aquaman).

**Conséquence** : un portique Aquaman `NEEDS_REVIEW` n'est **pas un
`BLOCKED_RISK`** — Batman peut émettre `LAUNCH_READY` avec une mention dans
le packet mésoperpétuel.

## Anti-pièges

- **Confondre portique Aquaman et red flag matrice.** Le red flag #5 matrice
  d'harmonisation pose *« Legal red + public-facing work »* — c'est
  l'**équivalent détecté tardivement**. Le portique Aquaman T-7j est
  l'**équivalent systématique**. Les deux sont compatibles : le portique
  *devrait* éliminer le red flag avant qu'il se déclenche.
- **Confondre portique Aquaman et portique Batman.** Batman signe
  `LAUNCH_READY` transverse. Aquaman ne signe pas `LAUNCH_READY` — il émet
  un input `LEGAL_READY` ou `BLOCKED_RISK` qui est **un** des 7 inputs
  Batman. La nuance : Aquaman n'a pas le droit de bloquer un launch seul,
  il le signale.
- **Aquaman qui devient goulot d'étranglement.** Si Aquaman vette 4 items
  pour chaque launch, et que Batman lance 4 fois par an, Aquaman traite
  16 dossiers par an — c'est tenable. Mais si Batman lance 12 fois par an,
  Aquaman sature. La mitigation : pré-vetter les **clauses-types et claims
  récurrentes** une fois par sprint, pas à chaque launch.
- **Timing T-7j oublié.** Un portique Aquaman demandé à T-1j est un portique
  *théorique*. La procédure 7 jours est non-négociable ; Batman doit
  intégrer le timing dans son calendrier de launch.
- **Confondre `LEGAL_READY` Aquaman et `LAUNCH_READY` Batman.** Ce sont deux
  gates distincts. `LEGAL_READY` Aquaman ouvre la porte du portique ; c'est
  `LAUNCH_READY` Batman qui ouvre le launch.

## Liens

- [[aquaman-classification-risques-4-formes]] — les 4 classes (privacy /
  claim / IP / contract) qui sous-tendent les 4 items du portique
- [[aquaman-defensibility-triple-signature]] — la Forme 4 binder qui motive
  l'item 4
- [[aquaman-jtbd-emit-receive]] — les Formes 1-3 qui motivent les items 1-3
- [[aquaman-couplages-invisibles]] — le couplage Aquaman ↔ Cyborg qui motive
  Cas R2
- [[aquaman-veto-amendment-perimetre-insuffisant]] — le veto catalogue
  *engagement-sans-périmètre* (classe 4) qui motive Cas R1 si lié à un
  contract template
- [[eight-domain-avengers-wheel]] §Le coordinateur transverse — People
  (position transverse comparable, Batman comme transverse Ops)
- [[b2-harmonization-matrix-exploitable]] §Red flag #1 et #5 — les red flags
  que le portique Aquaman T-7j *devrait* éliminer

## Note de confiance

**Reconstruit, projeté depuis le canon.** Les 4 items sont **projetés** depuis
le périmètre Aquaman (les 7 surfaces → 4 classes → 4 items portique). Le
positionnement *« Aquaman est un portique d'entrée, pas final »* est **reconstruit**
par symétrie avec [[aquaman-couplages-invisibles]] §Position transversale
People — People est un input *transverse*, Aquaman devient un input *portique*
sur le launch. Le timing T-7j est **calibré** depuis la pratique documentée
de reformulation (48h) + implémentation (96h) + binder (5j) — **pas mesuré**.
Les 3 cas de refus sont **projetés** depuis le red flag #5 de la matrice
d'harmonisation + le couplage Aquaman ↔ Cyborg privacy + la triple signature
proactive. **À vérifier en cycle** : (1) Batman accepte-t-il le portique Aquaman
comme input *par défaut*, ou veut-il trancher seul ?, (2) T-7j tient-il sur un
cycle réel avec Superman qui presse ?, (3) les 4 items sont-ils les bons, ou
manque-t-il un 5ᵉ (par exemple : *clauses de limitation de liability* spécifique
aux juridictions du launch) ?

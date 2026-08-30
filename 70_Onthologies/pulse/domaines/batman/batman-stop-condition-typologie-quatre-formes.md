---
type: Concept
title: Batman — typologie des quatre formes canoniques de condition d'arrêt
description: Le veto Batman (procédure sans condition d'arrêt écrite) exige une forme opérable. Sans typologie, la condition d'arrêt est invérifiable — la propriété « vérifiable » du catalogue 8-vetos n'est pas tenable. Quatre formes canoniques : date+métrique, événement+métrique, owner+escalade, réversibilité. Chaque forme a un cas d'usage nominal, deux cas limites où elle devient abusive, et un couplage avec un autre veto catalogue.
tags: [batman, condition-arret, typologie, formes-canoniques, veto, verifiabilite, ops, b2]
generated: { by: minimax-m3, at: 2026-08-19T05:00:00Z }
verified:
  - { by: process:lecture-b2-corpus-tour-2, at: 2026-08-19T05:00:00Z }
sources:
  - id: triplet-batman-veto
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 24 — Batman bloque toute procédure qui n'a pas de condition d'arrêt écrite"
    last_modified: 2026-08-17
  - id: b2-vetoes
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-eight-domain-vetoes-catalogue.md"
    title: Catalogue des 8 vetos B2 — propriétés catégoriel/vérifiable/non-négociable
    last_modified: 2026-08-19
  - id: harmonization
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/areas/business-wheel-harmonization-matrix.md"
    title: Harmonisation de la wheel — DoD chiffré par seuil
    last_modified: 2026-08-17
  - id: b2-b3-contract
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-b3-jtbd-handoff-contract.md"
    title: B2 → B3 contract — bornes DoD chiffrées
    last_modified: 2026-08-19
  - id: omk-business-os
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/omk-business-os.md"
    title: OMK Business OS — doctrine D4 append-only
    last_modified: 2026-08-17
okf_version: "0.2"
---

# Batman — typologie des quatre formes canoniques de condition d'arrêt

## Le besoin — le veto est invérifiable sans typologie

Le veto Batman teste la **présence** d'une condition d'arrêt dans
une procédure (triplet 24). Pour que la propriété **« vérifiable »**
du catalogue 8-vetos (`b2-eight-domain-vetoes-catalogue.md`) soit
tenable, la condition d'arrêt doit avoir une **forme** qu'un tiers
peut ouvrir et constater.

Sans typologie, le débat *« cette procédure a-t-elle une condition
d'arrêt ? »* n'a pas de fin : un captain peut dire *« oui, c'est
"arrêter quand le client n'en veut plus" »*, un autre peut répondre
*« ce n'est pas une condition chiffrée, c'est une clause molle »*.
Le veto devient **subjectif**.

Cette page pose **quatre formes canoniques** qui couvrent
l'essentiel des procédures Ops. Une condition d'arrêt qui n'a
aucune de ces quatre formes **n'est pas une condition d'arrêt** au
sens du veto — le veto tient.

## Forme 1 — Date + métrique

**Structure** : *« la procédure P s'arrête au YYYY-MM-DD si la
métrique M passe sous le seuil S »*.

**Cas d'usage nominal** : un onboarding qui s'arrête au 2026-12-31
si le NPS post-onboarding descend sous 35 sur 100 réponses. La
date donne un horizon, la métrique donne un seuil, le seuil donne
une décision binaire.

**Cas limites abusifs** :

- *Date sans métrique* — *« la procédure s'arrête au 2026-12-31 »*
  sans seuil. C'est une date de fin, pas une condition d'arrêt.
  Équivalent à `batman-veto-condition-arret-procedure.md` §« Le
  contraste avec les autres doctrines » : *« confondre condition
  d'arrêt et date de fin »*.
- *Métrique sans date* — *« la procédure s'arrête quand le NPS
  descend sous 35 »* sans horizon. C'est une clause molle — le
  NPS peut descendre sous 35 dans 3 jours ou dans 3 ans, la
  procédure ne sait pas quand arrêter.

**Couplage** : la date relève du cycle 12WY (Summers), la métrique
relève du DoD B2. Les deux doivent être cohérentes — une date de
fin hors 12WY est une escalade B1.

## Forme 2 — Événement + métrique

**Structure** : *« la procédure P s'arrête quand l'événement E se
produit et que la métrique M dépasse le seuil S »*.

**Cas d'usage nominal** : un support qui s'arrête quand 100 tickets
résolus sont atteints **et** que le taux de réouverture dépasse 15 %
— l'événement (100 tickets) marque un volume suffisant pour juger,
la métrique (taux de réouverture) marque la qualité.

**Cas limites abusifs** :

- *Événement sans métrique* — *« la procédure s'arrête quand le
  client signe le bon de livraison »*. C'est un événement, pas une
  condition d'arrêt : il n'a pas de garde-fou qualité. Une
  procédure peut s'arrêter au mauvais moment.
- *Métrique sans événement* — *« la procédure s'arrête quand le
  NPS descend sous 35 »*. Identique à Forme 1 sans date — clause
  molle.

**Couplage** : l'événement relève de l'opérationnel (le B3 squad
constate), la métrique relève du DoD B2. Le B3 qui détecte
l'événement remonte au B2 captain — Batman arbitre le moment
d'arrêt.

## Forme 3 — Owner + escalade

**Structure** : *« la procédure P s'arrête quand l'owner O escalade
E à Batman (ou au Council), avec un seuil S d'incidents critiques »*.

**Cas d'usage nominal** : un monitoring qui s'arrête quand
HumanTorch remonte **3 incidents critiques en 7 jours**. L'owner
(HumanTorch) déclenche l'escalade, le seuil (3 incidents en 7
jours) évite l'escalade émotionnelle, Batman arbitre.

**Cas limites abusifs** :

- *Owner sans seuil* — *« la procédure s'arrête quand HumanTorch
  escalade »*. C'est une confiance aveugle en l'owner — un owner
  fatigué peut escalader au mauvais moment. Le seuil est le garde-
  fou.
- *Seuil sans owner* — *« la procédure s'arrête au bout de 3
  incidents critiques en 7 jours »*. Qui déclenche ? Le B3 squad
  n'a pas le mandat d'arrêter (triplet 41 interdit-combler-trou).
  L'owner est nécessaire pour traduire le seuil en décision.

**Couplage** : l'owner est People (Green Lantern, cf.
`batman-couplage-people-green-lantern-owner-absent.md`), le seuil
est DoD B2 (Batman). Les deux doivent être cohérents — un seuil
sans owner est inopérant, un owner sans seuil est sans mandat.

## Forme 4 — Réversibilité

**Structure** : *« la procédure P est réversible à tout moment ;
la condition d'arrêt est une décision de Summers (B1), pas un
déclencheur automatique »*.

**Cas d'usage nominal** : une procédure de veille — Batman peut
poser *« cette procédure tourne tant que Summers ne décide pas de
l'arrêter »*. La condition d'arrêt est **explicitement humaine** :
elle n'est pas un seuil automatique, c'est une décision de cycle.

**Cas limites abusifs** :

- *Réversibilité sans owner de la décision* — *« la procédure
  s'arrête quand quelqu'un décide »*. *Quelqu'un* n'est pas un
  owner. La réversibilité doit nommer qui décide.
- *Réversibilité totale sans horizon* — *« cette procédure tourne
  indéfiniment tant que Summers n'arrête pas »*. Si Summers ne
  décide jamais, la procédure tourne indéfiniment. C'est un coût
  sans contrepartie (cf. `b2-areas-dormants-doctrine.md` §« Le
  principe » pour la symétrie avec la dormance).

**Couplage** : la décision d'arrêter est B1 (Summers). Batman ne
peut pas poser une Forme 4 sans mandat B1 — c'est Summers qui
autorise la procédure à tourner indéfiniment.

## Le tableau récapitulatif

| Forme | Structure | Owner de la décision | Cas limite abusif principal |
|---|---|---|---|
| 1 — Date + métrique | horizon chiffré + seuil chiffré | Batman (B2) + Summers (cycle) | date sans métrique, ou métrique sans date |
| 2 — Événement + métrique | déclencheur observable + seuil chiffré | B3 (détection) + Batman (arbitrage) | événement sans métrique, ou métrique sans événement |
| 3 — Owner + escalade | owner nommé + seuil d'incidents | Owner People + Batman | owner sans seuil, ou seuil sans owner |
| 4 — Réversibilité | décision humaine explicite | Summers (B1) | owner de la décision non nommé, ou pas d'horizon |

## Pourquoi quatre formes, pas une seule

Quatre formes couvrent **l'essentiel des procédures Ops** :

- **Forme 1** pour les procédures à horizon défini (revue de
  trimestre, fin de projet).
- **Forme 2** pour les procédures à déclencheur opérationnel
  (support, onboarding).
- **Forme 3** pour les procédures à risque d'incident (monitoring,
 astreinte).
- **Forme 4** pour les procédures de veille ou les dormants.

Un cinquième type — *« la procédure s'arrête quand Batman décide
»* — n'est pas canonique. Batman ne décide pas, Batman remonte
(triplets 56, 57). Cette cinquième forme serait une transgression
de la doctrine remonte-fait.

## Le lien avec le DoD chiffré du contrat B2 → B3

Le contrat B2 → B3 (`b2-b3-jtbd-handoff-contract.md` §« Ce que B2
Council promet ») exige des **bornes DoD explicites avec seuil
chiffré**. Les Formes 1, 2 et 3 sont des instanciations du DoD
chiffré. La Forme 4 est l'exception — elle accepte un DoD non
chiffré en échange d'une décision humaine explicite.

**Conséquence pratique** : un JTBD packet B3 qui ne contient aucune
des quatre formes est invalide — le B2 captain refuse la livraison,
le B3 squad ne peut pas combler le trou (triplet 41).

## Anti-pièges

- **Condition d'arrêt sous forme molle.** *« Arrêter quand le moment
  sera venu »* — aucune des quatre formes. Veto tient.
- **Condition d'arrêt qui n'est pas dans la procédure.** Une
  condition d'arrêt qui vit dans un email, dans un commentaire de
  ticket, ou dans la tête d'un B3 n'est pas *« écrite »* au sens du
  veto (triplet 24). Elle doit être dans le runbook, le SOP, ou le
  packet mésoperpétuel.
- **Forme 4 sans mandat B1.** Batman ne pose pas une Forme 4 de sa
  propre initiative — Summers doit autoriser la procédure à tourner
  indéfiniment. Sinon, c'est une absence déguisée (cf.
  `b2-areas-dormants-doctrine.md`).
- **Forme 3 sans owner People.** L'owner People doit être posé par
  Green Lantern — Batman ne pose pas l'owner à la place (cf.
  `batman-couplage-people-green-lantern-owner-absent.md`).
- **Mélanger les formes sans clarifier.** Une procédure qui a une
  Forme 1 *et* une Forme 3 *et* une Forme 4 n'est pas *« mieux
  cadrée »* — elle est *« confuse »*. Une seule forme par procédure,
  sauf cas explicite documenté dans le packet mésoperpétuel.
- **Condition d'arrêt comme pouvoir personnel.** Une Forme 4
  *« arrêter quand Batman décide »* est une transgression de la
  doctrine remonte-fait. Batman remonte, il ne décide pas.

## Liens

- [[batman-veto-condition-arret-procedure]] — le veto qui exige une forme
- [[domaine-batman-ops-perimetre-frontieres]] — le périmètre Ops
- [[batman-doctrine-remonte-fait-non-decision]] — pourquoi Forme 4 n'est pas Batman-décide
- [[batman-couplage-people-green-lantern-owner-absent]] — Forme 3 et owner People
- [[batman-couplage-finance-wonder-woman-recurrence]] — date de revue Wonder Woman analogue Forme 1
- [[batman-couplage-legal-aquaman-perimetre-propriete]] — périmètre Aquaman analogue Forme 4
- [[b2-eight-domain-vetoes-catalogue]] — la propriété « vérifiable » que la typologie rend opérable
- [[b2-b3-jtbd-handoff-contract]] — le DoD chiffré qui ancre Formes 1-3

## Note de confiance

**Reconstruit, à moitié étayé.** Le triplet 24 (veto Batman) est
cité verbatim, et la propriété *vérifiable* du catalogue est
tirée verbatim. Les quatre formes canoniques sont **reconstruites**
à partir de la pratique B2 (DoD chiffré du contrat B2 → B3,
seuils des pair-checks, doctrine remonte-fait). Les cas d'usage
nominaux et les cas limites abusifs sont **projetés** à partir de
mon expérience de la structure d'un runbook Ops. Les couplages
(Forme 1 ↔ Wonder Woman date de revue, Forme 4 ↔ Aquaman périmètre,
Forme 3 ↔ People owner) sont **mon raisonnement** à partir des
trois concepts batman-*couplage-*. La conclusion *« quatre formes
couvrent l'essentiel »* est défendue comme opérable, pas comme
exhaustive. À vérifier en cycle réel : (1) une procédure Ops réelle
satisfait-elle toujours l'une des quatre formes ?, (2) Batman a-t-il
déjà opposé son veto en s'appuyant sur cette typologie ?, (3) le
canon B2 doit-il poser cette typologie explicitement (par
amplification du veto, cf. `b2-veto-amplification-cycle.md`) ?

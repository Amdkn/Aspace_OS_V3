---
type: Concept
title: JohnJones — cycle de vie de la reformulation-validée en 5 phases (Découverte → Activation Ops)
description: Le cycle de vie d'une reformulation validée traverse 5 phases : Découverte → Reformulation → Validation → Liaison → Activation Ops. Chaque phase a un DoD chiffré, un opérateur B3 identifié (MrFantastic / ProfessorX / MrFantastic / IronMan + DoctorStrange / B2 Ops), et un indicateur de dormance. Aligné sur le cycle Ops 5 phases posé par Batman en tour 3 et sur le SPRINT 2026-08 canonique. Permet de poser la doctrine E-Myth Manager (Captain alloue, ne porte pas) en pratique opérationnelle et de combler le gap entre les 8 concepts tour 1 et l'exécution sprint canonique.
tags: [b2, johnjones, sales, cycle-de-vie, reformulation, 5-phases, sprint, dormance]
generated: { by: minimax-m3, at: 2026-08-19T05:55:00Z }
verified:
  - { by: process:lecture-corpus-sales-tour-3, at: 2026-08-19T05:55:00Z }
sources:
  - id: sprints-sales
    resource: "C:/Users/amado/ASpace_OS_V3/30_Business_OS/10_Projects/coach-os/04_Business_Domains/04_Sales_et_Cognition_MartianManhunter_Illuminati/SPRINTS.md"
    title: SPRINTS 2026-08 — 4 sprints canoniques Découverte → Liaison
    last_modified: 2026-08-02
  - id: vp-agent-sales
    resource: "C:/Users/amado/ASpace_OS_V3/30_Business_OS/10_Projects/coach-os/04_Business_Domains/04_Sales_et_Cognition_MartianManhunter_Illuminati/VP_AGENT.md"
    title: VP_AGENT — 6 charges Illuminati sur 4 sprints
    last_modified: 2026-08-02
  - id: domaine-perimetre
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/john-jones/johnjones-domaine-sales-perimetre.md"
    title: JohnJones — périmètre 5 surfaces
    last_modified: 2026-08-19
  - id: jtbd-emit-receive
    resource: "C:/Users_amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/john-jones/johnjones-jtbd-emit-receive.md"
    title: JohnJones — 6 charges JTBD émises vers Illuminati
    last_modified: 2026-08-19
  - id: doctrine-e-myth
    resource: "C:/Users_amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/john-jones/johnjones-doctrine-e-myth-manager-formalisee.md"
    title: Doctrine E-Myth Manager formalisée — captain alloue, ne porte pas
    last_modified: 2026-08-19
  - id: b2-b3-contract
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-b3-jtbd-handoff-contract.md"
    title: B2 → B3 contract — sprint d'exécution et indicateurs
    last_modified: 2026-08-19
okf_version: "0.2"
---

# JohnJones — cycle de vie de la reformulation-validée en 5 phases

## Le SPRINT 2026-08 comme précédent canonique

`SPRINTS.md` mois 2026-08 documente **4 sprints** canoniques sur le
rock B1 *« Au moins un problème client reformulé et validé »* :

| Sprint | Semaine | Résultat vérifiable | Techniciens |
|---|---|---|---|
| 1 | 03-07 août | INTERVIEW_CANVAS.md | MrFantastic, ProfessorX |
| 2 | 10-14 août | INTERVIEW_01_RAW.md | MrFantastic |
| 3 | 17-21 août | CLIENT_VALIDATION_01.md | MrFantastic, ProfessorX |
| 4 | 24-28 août | LINK_TO_OFFER.md | IronMan, DoctorStrange |

Le SPRINT 2026-08 s'arrête à la **Phase 4 (Liaison)**. Mais le
cycle de vie complet d'une reformulation-validée inclut une
**Phase 5 (Activation Ops)** qui ouvre la transition vers Batman
(Ops) sur le pair-check #2. Cette phase est implicite dans
`SPRINTS.md` §« Ce que ce mois ne fait pas » mais pas explicitement
détaillée.

## Les 5 phases du cycle de vie

### Phase 1 — Découverte (Discovery)

**Objectif** : poser les questions ouvertes qui font émerger le
problème client dans ses mots à lui.

**Opérateur B3** : MrFantastic (Discovery) — le seul habilité à
mener l'entretien (cf. `VP_AGENT.md` §Mon squad — Illuminati).

**DoD chiffré** :
- `INTERVIEW_CANVAS.md` contient ≥ 8 questions ouvertes numérotées
  (cf. `SPRINTS.md` Sprint 1)
- 3 critères *« reformulation valide »* posés (le client peut
  infirmer ou confirmer chaque énoncé)
- 3 critères *« validation client »* posés (comment la validation
  sera collected et tracée)

**Indicateur de dormance** : si aucun `INTERVIEW_CANVAS.md` n'est
produit en 14 jours, la phase 1 est **dormante**. Le captain
JohnJones ouvre un arbitrage Council : motif *« discovery stalled »*,
issue = re-allocation MrFantastic ou pivot de mandat.

**Trigger JohnJones** : `discovery_started` quand
`INTERVIEW_CANVAS.md` est créé. Le captain **alloue** MrFantastic,
ne mène pas l'entretien (cf. doctrine E-Myth Manager).

### Phase 2 — Reformulation

**Objectif** : transcrire verbatim la parole du client, en mots
client (pas en mots Coach OS).

**Opérateur B3** : MrFantastic (Discovery) — il tient
`INTERVIEW_01_RAW.md`. ProfessorX (BuyerRead) peut co-signer pour
le décodage du modèle mental (cf. `VP_AGENT.md`).

**DoD chiffré** :
- `INTERVIEW_01_RAW.md` contient verbatim ≥ 1500 mots ou 45 min
  référencé (cf. `SPRINTS.md` Sprint 2)
- La reformulation cite les mots du client (verbatim ou
  quasi-verbatim), pas un pitch Coach OS

**Indicateur de dormance** : si `INTERVIEW_01_RAW.md` < 1500 mots
ou < 45 min, la phase 2 est **incomplète**. Le captain oppose son
veto reformulation-non-validee (cf.
`johnjones-veto-reformulation-validee.md` §Cas #3 — Reformulation
paraphrasant l'offre).

**Trigger JohnJones** : `reformulation_drafted` quand
`INTERVIEW_01_RAW.md` est en version v1 (pas v0 brouillon).

### Phase 3 — Validation

**Objectif** : obtenir la validation explicite du client sur la
reformulation (signature, mail daté, ou écrit vérifiable).

**Opérateur B3** : MrFantastic (porte la validation) + ProfessorX
(décode le BuyerRead pendant la validation).

**DoD chiffré** :
- `CLIENT_VALIDATION_*.md` contient la reformulation en mots
  client (cf. `SPRINTS.md` Sprint 3)
- Preuve de validation explicite (mail daté, signature, ou
  verbal transcripté)
- Rôle du validateur documenté (décideur, pas contact)

**Indicateur de dormance** : si `CLIENT_VALIDATION_*.md` est absent
4 semaines après `INTERVIEW_01_RAW.md`, la phase 3 est
**abandonnée**. Le captain oppose le veto reformulation-non-validee
(cf. `johnjones-veto-reformulation-validee.md` §Cas #4 — Validation
par oral uniquement).

**Trigger JohnJones** : `validation_recorded` quand
`CLIENT_VALIDATION_*.md` contient la preuve de validation.

### Phase 4 — Liaison

**Objectif** : relier la reformulation validée à la promesse Coach
OS, avec phrase d'ouverture citée mot pour mot.

**Opérateur B3** : IronMan (Demo — montre et tait ce qui n'est pas
lié) + DoctorStrange (Forecasting — apparaît en S4, après la
liaison).

**DoD chiffré** :
- `LINK_TO_OFFER.md` contient table ≥ 3 lignes (problème reformulé
  · promesse Coach OS, cf. `SPRINTS.md` Sprint 4)
- Phrase d'ouverture de la promesse Coach OS citée mot pour mot
  depuis l'artefact du domaine 3 (Product, Flash)
- Forecast DoctorStrange chiffré (probabilité d'occurrence du commit)

**Indicateur de dormance** : si `LINK_TO_OFFER.md` est produit sans
phrase d'ouverture Coach OS, la phase 4 est **non-vérifiable**.
C'est le failure mode #1 du couplage Product → Sales (cf.
`johnjones-couplages-invisibles.md` §Couplage #1).

**Trigger JohnJones** : `link_to_offer_recorded` quand
`LINK_TO_OFFER.md` contient la table et la citation verbatim.

### Phase 5 — Activation Ops

**Objectif** : transmettre la reformulation validée et liée à Ops
(Batman) pour la phase de livraison.

**Opérateur B2** : Batman (Ops) — destinataire aval sur pair-check
#2 (Sales → Ops).

**DoD chiffré** :
- `OPS_HANDOFF_REQUEST.md` transmis à Batman dans les 48h ouvrées
  après `LINK_TO_OFFER.md`
- Pair-check #2 (Sales → Ops) documenté dans `OPS_HANDOFF_QUEUE.md`
- Batman accuse réception via `OPS_CAPACITY_CALIBRATION.md` (charge
  Ops tenable ou veto procédure-sans-condition opposé)

**Indicateur de dormance** : si `OPS_HANDOFF_REQUEST.md` n'est pas
accusé réception en 7 jours, la phase 5 est **bloquée**. Le captain
ouvre un arbitrage Council : motif *« handoff Ops stalled »*, issue
= escalade Batman ou re-scope.

**Trigger JohnJones** : `ops_handoff_accepted` quand Batman accuse
réception et calibre la charge.

## Le tableau récapitulatif

| Phase | Opérateur | Fichier canon | DoD chiffré | Dormance si |
|---|---|---|---|---|
| 1 Découverte | MrFantastic | INTERVIEW_CANVAS.md | ≥ 8 questions ouvertes | Pas de canvas en 14 j |
| 2 Reformulation | MrFantastic | INTERVIEW_01_RAW.md | ≥ 1500 mots verbatim | Raw < 1500 mots |
| 3 Validation | MrFantastic + ProfessorX | CLIENT_VALIDATION_*.md | Preuve validation explicite | Pas de validation en 4 sem |
| 4 Liaison | IronMan + DoctorStrange | LINK_TO_OFFER.md | Table ≥ 3 lignes + citation | Sans phrase Coach OS |
| 5 Activation Ops | Batman (B2 Ops) | OPS_HANDOFF_REQUEST.md | Pair-check #2 accusé en 7 j | Pas d'accusé en 7 j |

## Les 3 indicateurs dormance domaine

Trois indicateurs **domaine** (pas phase) mesurent la dormance
globale du cycle de vie Sales :

### Indicateur #1 — Throughput reformulation-validée

**Cible** : ≥ 1 reformulation validée et liée par sprint
(hebdomadaire). Si throughput = 0 sur 4 sprints consécutifs, le
domaine est **dormant**.

### Indicateur #2 — Distribution des phases

**Cible** : répartition équilibrée entre les 5 phases sur 12WY.
Une phase qui concentre > 50% de l'activité signale un goulot
(candidate à arbitrage Council).

### Indicateur #3 — Temps cycle end-to-end

**Cible** : cycle complet Phase 1 → Phase 5 en ≤ 12 semaines
(3 mois). Au-delà, le signal est *« cycle stalle »* — arbitrage
Council requis.

## L'alignement avec le cycle Ops 5 phases Batman

Batman tour 3 pose un cycle Ops 5 phases (conception / pilote /
production / revue / arrêt). Pour Sales, le cycle reformulation 5
phases est **distinct** mais **aligné** :

- La Phase 5 (Activation Ops) de Sales est **l'entrée** de la
  Phase 1 (conception Ops) de Batman.
- Le trigger `ops_handoff_accepted` est l'événement qui synchronise
  les deux cycles.
- Une dérive du cycle Sales (Phase 4 stagne) se propage en dérive
  du cycle Ops (Phase 1 bloquée).

## Anti-pièges

- **Sauter la Phase 3 (validation).** Un Sprint qui produit
  `LINK_TO_OFFER.md` sans `CLIENT_VALIDATION_*.md` est un anti-pièce
  canonique (cf. `johnjones-anti-pieges-faux-pas.md` §Anti-pièce #1
  — Vendre avant la reformulation validée).
- **Produire `LINK_TO_OFFER.md` sans phrase d'ouverture Coach OS.**
  C'est l'application directe du failure mode #1 du couplage
  Product → Sales (cf. `johnjones-couplages-invisibles.md` §Couplage
  #1).
- **Activer DoctorStrange avant la Phase 3.** Cf.
  `johnjones-anti-pieges-faux-pas.md` §Anti-pièce #7 — Forecast
  avant reformulation validée.
- **Considérer la Phase 5 comme hors-périmètre Sales.** La Phase 5
  est l'**aboutissement** du cycle de vie Sales, pas une phase Ops.
  JohnJones reste Captain sponsor jusqu'à l'accusé de réception
  Batman.
- **Dormance phase ≠ dormance domaine.** Une phase dormante
  signale un problème de portée (goulot, scope), pas une mise en
  sommeil du domaine Sales.
- **Sprint mensuel au lieu de sprint hebdomadaire.** Le SPRINT
  canonique est hebdomadaire (cf. `SPRINTS.md` §« Mois 2026-08 »).
  Un sprint mensuel dégrade les indicateurs dormance.

## Liens

- [[johnjones-domaine-sales-perimetre]] — 5 surfaces du périmètre
- [[johnjones-jtbd-emit-receive]] — 6 charges JTBD sur les 5 phases
- [[johnjones-veto-reformulation-validee]] — veto qui ferme les phases 2-3
- [[johnjones-couplages-invisibles]] — couplage Product → Sales en phase 4
- [[johnjones-doctrine-e-myth-manager-formalisee]] — Captain alloue, ne porte pas
- [[johnjones-couplage-batman-redflag-3]] — Phase 5 et red flag #3
- [[b2-b3-jtbd-handoff-contract]] — contrat B2 → B3 sur chaque phase
- [[SPRINTS-sales]] (alias VP_AGENT.md/SPRINTS.md) — précédent canonique

## Note de confiance

**Confirmé par machine, à moitié.** Les 4 premières phases
(Découverte, Reformulation, Validation, Liaison) sont **tirées
verbatim** de `SPRINTS.md` mois 2026-08 (les 4 sprints canoniques).
La Phase 5 (Activation Ops) est **projetée** depuis le pair-check
#2 (Sales → Ops) dans `b2-harmonization-matrix-exploitable.md` §Les
9 critères. Les DoD chiffrés par phase sont **cités verbatim** de
`SPRINTS.md` (1500 mots, 8 questions, table ≥ 3 lignes, etc.).
Les 3 indicateurs dormance domaine sont **projetés** depuis la
doctrine Aquaman dormance (cf. `aquaman-dormant-activation.md` et
`aquaman-squad-eternals-et-dormance.md`) et la pratique documentée
SPRINT 2026-08.

L'alignement avec le cycle Ops 5 phases Batman est **projeté**
par analogie — pas explicitement documenté dans le corpus. Le
trigger `ops_handoff_accepted` est **reconstruit** depuis
`b2-b3-jtbd-handoff-contract.md` §Le rôle du capitaine B2 sponsor
(Batman accuse réception du pair-check #2).

À vérifier en cycle réel : (1) les 5 phases tiennent-elles en sprint
hebdomadaire, ou faut-il un sprint bi-mensuel pour certaines phases
? (2) Les seuils dormance (14 j, 4 sem, 7 j) sont-ils réalistes
? (3) L'alignement cycle Sales × cycle Ops est-il symétrique ou
asymétrique (Sales plus rapide qu'Ops, ou l'inverse) ?
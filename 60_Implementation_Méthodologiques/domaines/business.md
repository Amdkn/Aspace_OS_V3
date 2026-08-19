---
type: Playbook
title: Méthode Business OS — ce que la couche nous apprend sur la manière de travailler
description: Ce que 1335 fichiers `.md` du Business OS distillent comme manière de travailler : rituels (12WY, weekly review), garde-fous (4 boundary gates, Beth/Morty), cadences (5 niveaux hebdo→trimestriel), pièges documentés.
tags: [methode, business-os, rituels, garde-fous, cadences, pieges]
generated: { by: minimax-m3, at: 2026-08-19 }
verified:
  - { by: process:lecture-directe, at: 2026-08-19 }
sources:
  - id: B1_NORTH_STAR_CEOS_DESKTOP
    resource: "30_Business_OS/10_Projects/ceo-desktop/_doctrine/B1_Summer_Direction/01_NORTH_STAR_1Y_3Y_10Y.md"
    title: North Star — CEO's Desktop
    last_modified: "2026-06-07"
  - id: B1_12WY_COMMAND_CYCLES
    resource: "30_Business_OS/10_Projects/ceo-desktop/_doctrine/B1_Summer_Direction/02_12WY_COMMAND_CYCLES.md"
    title: 12WY Command Cycles — CEO's Desktop
    last_modified: "2026-06-07"
  - id: B1_DECISION_CHARTER_CEOS_DESKTOP
    resource: "30_Business_OS/10_Projects/ceo-desktop/_doctrine/B1_Summer_Direction/03_DECISION_CHARTER.md"
    title: Decision Charter — CEO's Desktop
    last_modified: "2026-06-07"
  - id: B2_DOMAIN_GATE_MATRIX
    resource: "30_Business_OS/10_Projects/ceo-desktop/_doctrine/B2_Business_Domains/B2_DOMAIN_GATE_MATRIX.md"
    title: B2 Domain Gate Matrix — CEO's Desktop
    last_modified: "2026-06-07"
  - id: SUMMERS_VERSE_MANIFEST
    resource: "30_Business_OS/10_Projects/ceo-desktop/_doctrine/SUMMERS_VERSE_MANIFEST.md"
    title: Summer's Verse Manifest — CEO's Desktop
    last_modified: "2026-06-07"
  - id: ADR-MESH-L2-001
    resource: "30_Business_OS/09_Blueprints/02-ADR/ADR-MESH-L2-001_tri-plateforme-doctrine.md"
    title: Doctrine Tri-Plateforme L2
    last_modified: "2026-05-27"
  - id: 7-sequences-franchise-2026-07-08
    resource: "30_Business_OS/02_Meta_Factory/outbound/7-sequences-franchise-2026-07-08.md"
    title: 7 Séquences Outbound OMK — Franchise-First
    last_modified: "2026-07-08"
  - id: HANDOFF_BETH
    resource: "30_Business_OS/10_Projects/ceo-desktop/handoffs/Beth_Alignment_Log.md"
    title: Beth — Alignment Log
    last_modified: "2026-06-07"
okf_version: "0.2"
---

# Méthode Business OS — ce que la couche nous apprend sur la manière de travailler

> **Question que cette méthode répond.** *Qu'est-ce que 1335 fichiers `.md` du Business OS distillent sur la manière de travailler ?*
>
> **Réponse en une ligne.** La doctrine du Business OS tient en **trois lois + trois rituels + trois cadences + trois pièges à éviter**. Tout le reste en découle.

## Les trois lois (cardinales)

### Loi 1 — La triade B1/B2/B3 ne se substitue pas

**B1 décide la direction** (north star, cadence, arbitrage), **B2 accepte le DoD** du domaine (gate, proof, pair-check), **B3 exécute tactique** et rapporte Lead/Lag.

**Pourquoi.** Si B1 fait du B3, le CEO hero-mode et single-point-of-failure. Si B3 fait du B2, l'exécution n'a plus de critères d'acceptation. Si B2 fait du B1, la stratégie se dilue dans le tactique. La triade est un anti-pattern de gestion.

**Référence.** `_doctrine/B1_Summer_Direction/00_B1_DIRECTION_INDEX.md` § "Operating Rule" ; `_doctrine/B2_Business_Domains/02_Sales_MartianManhunter_Illuminati/00_B2_DOMAIN_CONTROL_ROOM.md` § "Anti-Babysitting Rule".

### Loi 2 — Une information n'a qu'un propriétaire

La tri-plateforme Notion / ClickUp / Airtable sépare WHAT / WHEN-WHO / HOW-MUCH. Une donnée dupliquée entre plateformes **n'est pas une donnée** — c'est un risque de drift. Si dupliquée, c'est un pointeur (URL/ID), pas une copie.

**Pourquoi.** Trois plateformes, trois rôles sémantiques non-substituables. Le plan Free force la discipline ; la discipline force la doctrine. C'est circulaire et c'est voulu.

**Référence.** `09_Blueprints/02-ADR/ADR-MESH-L2-001_tri-plateforme-doctrine.md` §D1 et §D6.

### Loi 3 — La doctrine vit longtemps, le code vit court

Chaque projet porte une junction `_doctrine/` vers la source canonique. La doctrine se propage par junction, pas par copie. Le code change, la doctrine reste.

**Pourquoi.** Un projet peut pivoter ou être archivé sans toucher à la doctrine. Réversibilité opérationnelle. D4 append-only + D6 no-self-contradiction guard garantissent la cohérence inter-projet.

**Référence.** `_doctrine/SUMMERS_VERSE_MANIFEST.md` § "What This Project Is" ; ADR-INFRA-002 (Repo-Home Junction Law) référencé dans `CLAUDE.md`.

## Les trois rituels (non-négociables)

### Rituel 1 — Le 12-Week Year cadence

12 semaines par cycle, deux cycles par an calendaire. Le CEO's Desktop ne tourne ni en trimestre (trop long) ni en semaine (trop fin).

- **C1 (Direction Lock)** : Q3 2026 — ratifier B1 cockpit, semer la handoff queue des 8 SOB.
- **C2 (Domain Activation Prep)** : Q4 2026 — nommer les B2 managers (cible : ≥4/8), faire passer 1-2 entrées PENDING → ACCEPTED.
- **Phase 2+** : C3 (Execution Proof) → C4 (Graduation Or Archive), spec différée.

**Règle chiffrée.** Un cycle 12WY sans weekly review ou sans decision-charter entry est nommé **« dead »** ou **« theatre »** (verbatim dans `02_12WY_COMMAND_CYCLES.md`). C'est un signal d'alerte, pas une métaphore.

**Référence.** `_doctrine/B1_Summer_Direction/02_12WY_COMMAND_CYCLES.md` § "Anti-Drift Reminders".

### Rituel 2 — Le weekly review prompt

> What did B1 (A0) decide, what did B2 accept, what did B3 prove, and what remains unsafe to scale across the 8 SOB ?

Quatre questions, une fois par semaine, lues par A0 en 90 secondes. Pas un standup — un check-in d'arbitrage.

**Pourquoi.** Si A0 ne lit pas son desktop chaque semaine, le drift s'accumule et la cadence 12WY meurt. Le prompt est explicite et tient en une phrase.

**Référence.** `_doctrine/B1_Summer_Direction/02_12WY_COMMAND_CYCLES.md` § "Weekly Review Prompt".

### Rituel 3 — Le Decision Charter packet schema

Toute décision de direction B1 passe par le schema YAML :

```yaml
decision_id, date, scope, question, options, recommendation,
risk_if_wrong, reversibility,
boundary_gates: { it, finance, legal, people },   # GREEN|ORANGE|HALT|NA
beth_morty_status: GREEN|ORANGE|HALT,
b2_owner, b3_artifact_required, proof_path, next_review
```

**Règle chiffrée.** HALT si Beth/Morty rouge OU si un des 4 boundary gates est HALT. Pas d'exception.

**Référence.** `_doctrine/B1_Summer_Direction/03_DECISION_CHARTER.md` § "Escalation".

## Les trois cadences (par SOB)

Le CEO's Desktop **ne déplie pas tout à la même cadence**. Chaque SOB a sa propre horloge, fixée par le canon.

| SOB     | Cadence    | Couche Matrioshka typique | Pourquoi                              |
|---------|------------|---------------------------|---------------------------------------|
| IT      | Daily      | Rock Wheel (santé runtime) | Crash serveur = HALT, pas un récap    |
| Growth  | Weekly     | Domain Wheel              | Leading indicator                     |
| Sales   | Weekly     | Domain Wheel              | Leading indicator                     |
| Product | Weekly     | Domain Wheel              | Leading indicator                     |
| Ops     | Bi-weekly  | Domain Wheel              | Lagging de 2 sem                      |
| Finance | Monthly    | Business Wheel            | Burn + runway, granularité mensuelle suffit |
| People  | Monthly    | Business Wheel            | Charge + attrition                    |
| Legal   | Quarterly  | Business Wheel            | RGPD AI Act annuel                    |

**Règle.** Un dashboard qui force Legal en daily ou IT en hebdomadaire casse la réactivité ou noie A0. La cadence est la profondeur de dépliage.

**Référence.** `_doctrine/SUMMERS_VERSE_MANIFEST.md` § "ICP Variants — The 8 SOB Operating Modes".

## Les trois pièges documentés (à éviter)

### Piège 1 — Héroïsme A0 (no single-point-of-failure)

> A0 no longer single-point-of-failure on any domain. (`01_NORTH_STAR_1Y_3Y_10Y.md`)

**Symptôme.** A0 décide, A0 accepte, A0 exécute. Tout converge vers A0, qui sature.

**Antidote.** B2 managers nommés (≥4/8 SOB) avant Phase 2. 12WY cycles avec weekly review obligatoire. Decision Charter pour chaque décision de direction.

**Référence.** `_doctrine/B1_Summer_Direction/01_NORTH_STAR_1Y_3Y_10Y.md` § "3-Year Direction".

### Piège 2 — Vente de tuyauterie (utility-buyer)

> On ne vend pas la tuyauterie (« -90% de tokens », « RLS », « cache local ») — c'est la preuve technique, pas le désir. (`7-sequences-franchise-2026-07-08.md` § ouverture)

**Symptôme.** Le prospect négocie sur les tokens API. Il se positionne comme acheteur d'utilitaire, pas comme acquéreur de franchise.

**Antidote.** Filtre Built-to-Sell : si le client ne peut pas revendre l'OS, ce n'est pas T3-T5 (c'est T1-T2 « chasseur de rabais »). Le filtre est non-négociable.

**Référence.** `02_Meta_Factory/outbound/7-sequences-franchise-2026-07-08.md` § "Doctrine commune" #2.

### Piège 3 — Drift de plateforme (mesh-uni-directionnel violé)

> Aucun flux bidirectionnel simultané. Si bidirectionnel nécessaire, médiation **obligatoire** par Symphony bus (ADR-SYMPH-001). (`ADR-MESH-L2-001` §D5)

**Symptôme.** Une SOP Notion se retrouve mot-pour-mot dans ClickUp. Un brief Airtable crée un task ClickUp sans passer par Build_Gate. Un deal postmortem est noté dans ClickUp ET Notion sans médiation.

**Antidote.** ClickUp Custom Fields interdits en plan Free (le pattern `[SOP-L2-...]` dans le titre remplace fonctionnellement le Custom Field). Validateurs regex sur les IDs. Symphony bus obligatoire pour la bidirection.

**Référence.** `09_Blueprints/02-ADR/ADR-CK-FREE-001_clickup-free-constraints.md` §D3 ; `09_Blueprints/02-ADR/ADR-ID-001_identifiants-universels.md` §D5.

## Les trois garde-fous (anti-patterns)

### Garde-fou 1 — Les 4 boundary gates (IT, Finance, Legal, People)

> No Product-only release can be marked Business Done without the 4 boundary gates (IT, Finance, Legal, People). (`01_NORTH_STAR_1Y_3Y_10Y.md`)

**Symptôme.** Un livrable tagué « Product Done » circule sans statut sur les 4 boundary gates.

**Antidote.** Le Decision Charter force `boundary_gates.{it, finance, legal, people}` à chaque décision. HALT automatique si l'un est rouge.

### Garde-fou 2 — SOP `Active` non exercée (Build Gate)

> Règle d'or : une SOP qui ne peut pas être exécutée par un agent B3 sans clarification humaine est `Draft`, jamais `Active`. Batman refuse les SOPs floues. (`ADR-NOTION-001` §D4)

**Symptôme.** Une SOP est marquée `Active` parce qu'elle est rédigée + un Loom 5 min.

**Antidote.** Le vrai Build Gate est l'**exercice des 8 SOPs en réel** sur un onboarding client. Mettre à jour Notion `Build_Gate` field avec : "Tested via onboarding {CLIENT_ID} on {date}".

### Garde-fou 3 — B2 handoff queue PENDING infini

> A row leaves **PENDING** only when the B2 domain has accepted it and produced either PASS, CONDITIONAL, or BLOCKED with an evidence path. (`04_B2_HANDOFF_QUEUE.md`)

**Symptôme.** Les 8 lignes SOB restent PENDING cycle après cycle.

**Antidote.** Phase 1 close-out exige au moins 1 ligne avec un B2 manager nommé + au moins 1 ligne avec un statut Beth/Morty safety. Une queue 100% PENDING est un smell : **activate or archive**.

## La règle chiffrée qui résume

> Drift in cadence = drift in business. (`01_NORTH_STAR_1Y_3Y_10Y.md` § "Direction Invariants")

Si la cadence 12WY meurt, le business dérive. Si le weekly review meurt, le 12WY meurt. Si le Decision Charter meurt, les décisions dérivent. Chaque maillon tient par le suivant.

## Ce que cette méthode n'est pas

- Pas une cascade Scrum. Pas de sprint, pas de backlog grooming, pas de Scrum master.
- Pas un rituel agile. La cadence 12WY est fixe ; le kanban est ClickUp, pas un board flottant.
- Pas une métaphore. Les boundary gates sont statutés GREEN/ORANGE/HALT/NA, pas des impressions.

## Conséquence opérationnelle

Un projet qui s'aligne sur cette méthode **déroule** la triade B1/B2/B3 sur la cadence 12WY, avec un Decision Charter par décision, un Build Gate exercé par SOP, et 4 boundary gates statutés. Tout le reste est cosmétique.

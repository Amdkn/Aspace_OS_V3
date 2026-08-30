---
type: Concept
title: Squad Thunderbolts — arbitrage du canon roster entre OMK (4) et Notion/Jerry/CoachOS (6)
description: Le corpus Finance porte deux lectures incompatibles de la squad B3 Thunderbolts : (1) Notion AGENT_REGISTRY_DB canon + Jerry Area principles + Coach OS triplets — 6 membres Bucky, Yelena, Red Guardian, Ghost, Taskmaster, U.S. Agent ; (2) OMK Finance control room — 4 membres Red Hulk (budget), Taskmaster (accounting), Zemo (strategy), Ghost (leak detection). L'arbitrage proposé : la lecture 6-membres est canonique (3 sources concordantes dont Notion), la lecture 4-membres est OMK-pilote et sera migrée en V2.
tags: [b2, b3, finance, thunderbolts, squad, canon, arbitrage, omk, notion, migration]
generated: { by: minimax-m3, at: 2026-08-19T04:40:00Z }
verified:
  - { by: process:lecture-domaine-finance-corpus, at: 2026-08-19T04:40:00Z }
sources:
  - id: thunderbolts-canon-notion
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/06_Finance_WonderWoman_Thunderbolts/B3_Squad_Thunderbolts/00_B3_SQUAD_CANON.md"
    title: Thunderbolts — Finance Squad (CANON Notion)
    last_modified: 2026-05-28
  - id: spock-finance-principles
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/06_Finance_WonderWoman_Thunderbolts/03_WONDERWOMAN_FINANCE_PRINCIPLES.md"
    title: "Wonder Woman Finance Principles (v4) — squad mapping canon"
    last_modified: 2026-06-25
  - id: omk-control-room
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/B2_Business_Domains/06_Finance_WonderWoman_Thunderbolts/00_B2_DOMAIN_CONTROL_ROOM.md"
    title: "OMK Finance — B2 Domain Control Room (§ B3 Swarm Scope)"
    last_modified: 2026-05-27
  - id: triplet-v3-thunderbolts
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet v3 — Wonder Woman pairedWith Thunderbolts (Coach OS source)"
    last_modified: 2026-08-17
  - id: fifty-three-b3-agent-roster
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/fifty-three-b3-agent-roster.md"
    title: 53 B3 Agent Roster
    last_modified: 2026-08-17
okf_version: "0.2"
---

# Squad Thunderbolts — arbitrage du canon roster entre OMK (4) et Notion/Jerry/CoachOS (6)

## La divergence documentée

Le corpus Finance porte **deux lectures incompatibles** de la squad
B3 Thunderbolts :

### Lecture A — 6 membres (Notion canon + Jerry Area + Coach OS)

Trois sources concordantes :

1. **Notion AGENT_REGISTRY_DB** (`B3_Squad_Thunderbolts/00_B3_SQUAD_CANON.md`,
   id Notion `36c7e9e2-658c-81f7-a3e9-c2d65a13626f`, updated 2026-05-28,
   status Active) :

   > « Membres canoniques (6 sub-agents) :
   > Bucky Barnes (Winter Soldier) — Lead finance, discipline cashflow
   > Yelena Belova — Forecasting réaliste, scenarios pessimistes valorisés
   > Red Guardian — Reporting transparent, dashboards lisibles
   > Ghost — Cost optimization, traque les charges fantômes
   > Taskmaster — Reproductibilité processus comptables
   > U.S. Agent — Compliance fiscale, déclarations en temps »

2. **Jerry Area principles** (`03_WONDERWOMAN_FINANCE_PRINCIPLES.md`,
   v4, status CANONICAL_FROM_CANON, 2026-06-25) :

   > « Squad: The Thunderbolts (Bucky Barnes, Yelena Belova, Red
   > Guardian, Ghost, Taskmaster, U.S. Agent) »

   Le mapping principles → members est explicite dans le § « How
   the squad applies these » (Bucky = F1/F4/F11, Yelena = F2/F3,
   Red Guardian = F7/F8, Ghost = F5, Taskmaster = F9/F12, U.S.
   Agent = F10).

3. **Coach OS triplet** (`triplets/v3-business.jsonl`, source
   `coach-os/04_Business_Domains/06_Finance_et_ROI_WonderWoman_Thunderbolts/VP_AGENT.md`) :

   > « Wonder Woman (VP B2 domaine 6 — Finance & ROI) commande le
   > squad Thunderbolts (6 techniciens : BuckyBarnes, YelenaBelova,
   > RedGuardian, Ghost, Taskmaster, USAgent) »

### Lecture B — 4 membres (OMK Finance control room)

Une seule source, mais le projet OMK est explicitement identifié
comme pilote (status `SHADOW_ACTIVE`, 2026-05-27) :

`00_B2_DOMAIN_CONTROL_ROOM.md` § « B3 Swarm Scope » :

> « B3 swarm: **Red Hulk** budget, **Taskmaster** accounting,
> **Zemo** strategy, **Ghost** leak detection.
>
> Core domain surface: cost, price, margin, billing, model-usage
> and service-cost burn control. »

**Trois différences** :

| Dimension | Lecture A (Notion canon) | Lecture B (OMK) |
|---|---|---|
| Effectif | 6 | 4 |
| Lead | Bucky Barnes (cashflow discipline) | Red Hulk (budget) |
| Spécialités | cashflow, forecasting, reporting, cost-opt, accounting, compliance | budget, accounting, strategy, leak-detection |
| Statut source | Active (Notion), CANONICAL_FROM_CANON (Jerry) | SHADOW_ACTIVE (OMK) |
| Datation | 2026-05-28, 2026-06-25 | 2026-05-27 |

## L'arbitrage proposé : Lecture A canonique

**Recommandation au B2 Council** : la Lecture A (6 membres, Notion
canon) est canonique. Trois raisons :

### 1. Trois sources concordantes vs une seule

Notion + Jerry Area + Coach OS trio donnent **exactement** les
mêmes 6 noms dans le même ordre (Bucky, Yelena, Red Guardian,
Ghost, Taskmaster, U.S. Agent). Cette concordance triple est un
**signal fort de canon**.

OMK est seul avec sa liste 4-membres (Red Hulk, Taskmaster, Zemo,
Ghost). Une source isolée qui contredit trois sources concordantes
est présumée **non-canonique** par défaut — sauf si elle est plus
récente que les trois autres, ce qui n'est pas le cas ici
(2026-05-27 vs 2026-05-28/2026-06-25/2026-08-17).

### 2. Le statut SHADOW_ACTIVE de l'OMK

`00_B2_DOMAIN_CONTROL_ROOM.md` porte **status: SHADOW_ACTIVE**
(2026-05-27). Le triplet v3 note l'OMK comme « projet-pilote »
avec une version control room shadow qui sera migrée en ACTIVE.
Lecture B est une **vue pilote** d'une squad en construction,
pas la doctrine installée.

Lecture A est marquée Active dans Notion et CANONICAL_FROM_CANON
dans Jerry Area. C'est le statut de la doctrine installée.

### 3. Le mapping F-principles → members est cohérent

Le mapping Jerry Area est **testable** : chaque membre a des
principes F assignés (Bucky = F1/F4/F11, etc.), et chaque
principe F est incarné par un membre de la squad. Si on retire
un membre (par exemple Zemo « strategy »), il n'y a pas de
principe F associé dans la doctrine. La squad 6-membres est **clôt**
par le mapping F.

À l'inverse, la squad OMK 4-membres n'a pas de mapping
principes → members explicite. Red Hulk « budget » ne correspond
à aucun F1-F25. Zemo « strategy » n'apparaît dans aucun F-numéro.
Le mapping est **implicite et partiel**.

## Pourquoi l'OMK a dérivé — l'hypothèse

L'OMK est un **projet Picard** (par opposition à Jerry Area et
Coach OS qui sont des projets Areas/projet direct). Les projets
Picard sont des **instantiations** du Business OS dans des
contextes spécifiques (ici : OMK = un client). Le contrôle room
OMK a probablement été écrit par un B2 captain qui **n'avait
pas** accès à la doctrine pérenne Jerry Area, et a composé sa
squad 4-membres à partir de ses lectures Marvel — Red Hulk,
Taskmaster, Zemo, Ghost sont tous des personnages canoniques
Marvel avec des associations « finance/stratégie ».

**C'est un cas classique de drift projet vs doctrine**. Le
projet-pilote ne s'aligne pas sur la doctrine installée, et
personne n'arbitre parce que le pilote n'est pas encore passé
en ACTIVE.

## La migration nécessaire en V2

**Action attendue** : la migration de l'OMK control room vers
les 6 membres canoniques. Concrètement :

1. **OMK `00_B2_DOMAIN_CONTROL_ROOM.md`** § « B3 Swarm Scope » —
   remplacer « Red Hulk budget, Taskmaster accounting, Zemo
   strategy, Ghost leak detection » par les 6 membres Notion :
   « Bucky Barnes (cashflow), Yelena Belova (forecasting), Red
   Guardian (reporting), Ghost (cost opt), Taskmaster
   (accounting), U.S. Agent (compliance) ».
2. **Bascule du status** : SHADOW_ACTIVE → ACTIVE, avec un packet
   mésoperpétuel qui consigne la migration.
3. **Préservation des 4 noms OMK** dans un addendum historique
   pour traçabilité — pas une suppression, une migration.

**Statut canonique après migration** : la doctrine pérenne
(Jerry Area) et le projet pilote (OMK) convergent. Les 6 noms
sont canoniques.

## Cas spécial — la 7ᵉ place de Fifty-three-roster

Le concept `fifty-three-b3-agent-roster.md` (Distillation, 2026-08-17)
projette **~7 agents** par squad, soit un 7ᵉ Thunderbolts
non-nommé dans les sources lues. Cette projection vient de
l'invariant Ownerbook T1 DoD-1 : « verify: `ls .claude/agents/b3-1-*
| wc -l` ≥ 7 (X-Men squad canon) ». C'est un **seuil minimum**
(≥7), pas un compte exact.

**Lecture** : le 7ᵉ Thunderbolts pourrait être :
- Un membre **non encore institué** dans la doctrine (par exemple
  un « Ghost Rider » pour la souveraineté cloud F24 — couplage avec
  Cyborg).
- Un membre **abandonné** depuis la dernière lecture (par exemple
  « Captain Marvel » pour l'AI-Agency F23-F25).

**Recommandation** : ne pas inventer un 7ᵉ agent. Tant que la
doctrine ne nomme pas explicitement le 7ᵉ, le roster canonique
reste à 6. Toute projection est une **hypothèse à confirmer**,
pas un fait.

## Anti-pièges

- **Crois que la 7ᵉ place est obligatoire.** L'invariant ≥7 est
  un seuil, pas un compte exact. Si la doctrine en pose 6, 6 est
  canonique.
- **Ignorer la lecture OMK comme « draft ».** Le control room
  OMK est un projet actif (SHADOW_ACTIVE), pas une draft. Il
  pilote un client. La migration est nécessaire mais pas
  urgente — aucun arbitrage mésoperpétuel n'est déclenché par
  cette divergence tant qu'aucun client OMK n'utilise un
  Thunderbolts qui n'existe pas dans le canon.
- **Confondre canon et opérationnel.** Le canon dit 6. Le
  projet OMK en utilise 4. Tant que le projet OMK n'a pas
  basculé en ACTIVE, la divergence est silencieuse. La
  migration est une action de **ralliement**, pas une urgence.
- **Ajouter des membres sans doctrine.** Un capitaine B2 qui
  ajoute un 7ᵉ Thunderbolts « parce que le fifty-three-roster
  dit ≥7 » sans ancrer le membre dans un principe F-number
  produit du **bruit de roster**. La règle : tout membre de
  squad doit mapper à au moins un principe.

## Liens

- [[wonder-woman-finance-frontiers]] — le périmètre Finance
- [[wonder-woman-finance-doctrine-f1-f25-mapping]] — les 25 principes
- [[wonder-woman-finance-jtbd-emit-receive]] — les paquets JTBD émis/reçus
- [[b2-b3-jtbd-handoff-contract]] — le contrat bilatéral B2 → B3
- [[fifty-three-b3-agent-roster]] — la projection ~7 agents/squad

## Note de confiance

**Confirmé par machine** sur la divergence : 6 membres Notion/Jerry
lus verbatim, 4 membres OMK control room lus verbatim. La
recommandation d'arbitrage Lecture A canonique est **projetée** —
le corpus ne pose pas explicitement la règle « 3 sources
concordantes > 1 source isolée », mais c'est une lecture défendable
par symétrie avec la doctrine canon Living Canon (cf. `eight-domain-avengers-wheel.md`
§ « Note sur la nomenclature Sales » où le living canon
W40 V4 a absorbé l'ancien Martian Manhunter). La migration V2
est une **action attendue**, pas une action accomplie.
---
type: Method
title: Méthode Life Wheel — couche LD01-LD08 distilled
description: Ce que la couche 22_Wheel_Discovery enseigne sur la manière de travailler la Life Wheel : rituels Discovery/ZORA, garde-fous HARD SAFETY Beth, cadences H1/H3/H10/H30/H90, jauges chiffrées SDD-005, et pièges documentés (Saru H3 vs Book H1, drift owner Tilly+Spock, typo J04 Creatry).
tags: [methode, life-wheel, ld01-ld08, discovery-zora, hard-safety, jauges, pieges]
generated: { by: minimax-m3, at: 2026-08-19T04:20:00Z }
verified:
  - { by: process:read_local_v2, at: 2026-08-19T04:20:00Z }
sources:
  - id: discovery-spec
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/22_Wheel_Discovery/A2_Discovery_ZORA_Spec.md
    title: A2 Discovery Spec — Life Wheel canon
    last_modified: 2026-06-21
  - id: beth-spec
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/00_Gatekeepers_Beth_Morty/A1_Beth_Spec.md
    title: A1 Beth Spec — 5 états + seuils
    last_modified: 2026-05-20
  - id: sdd-005
    resource: ASpace_OS_V2/10_Tech_OS/12_Blueprints/01-SDD/SDD-005_life-os-l1-integration.md
    title: SDD-005 Life OS L1 Integration
    last_modified: 2026-05-20
  - id: a3-crew-specs
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/22_Wheel_Discovery/LD0X_*/A3_*_Spec.md
    title: 8 A3 specs LD01-LD08 (Book, Saru, Culber, Tilly, Stamets, Burnham, Reno, Georgiou)
    last_modified: 2026-05-20
  - id: jerry-j0x
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/J0X_*/
    title: 4 Jerry canon (J01 Prime / J02 Bio / J03 Nexus / J04 Solarpunk)
    last_modified: 2026-05-21
  - id: adr-008
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/22_Wheel_Discovery/LD01_Business_Book/30_decisions/ADR-LD01-008_coaching-loop-picard-jerry-summers.md
    title: ADR-LD01-008 Loop Engineering
    last_modified: 2026-07-05
okf_version: "0.2"
---

# Méthode Life Wheel — couche LD01-LD08 distilled

Cette méthode condense ce que la couche `22_Wheel_Discovery` enseigne sur **la manière de travailler la Life Wheel**. Elle ne re-décrit pas les concepts — pour les détails, voir `50_Distillation/domaines/life-wheel/`.

## 1. Rituels

### 1.1 Resume Protocol Discovery — toujours lire A1 avant A2

Tout agent qui ouvre un dossier Life Wheel commence par :

1. Lire `00_Gatekeepers_Beth_Morty/A1_Beth_Spec.md`.
2. Lire `00_Gatekeepers_Beth_Morty/A1_Morty_Spec.md`.
3. Lire `22_Wheel_Discovery/A2_Discovery_ZORA_Spec.md`.
4. Lire `22_Wheel_Discovery/A3_Discovery_References_Index.md`.
5. Inspecter seulement le dossier LDxx ou Baserow-export evidence nommé par le Context Pack.
6. Écrire les findings comme **evidence paths**, pas mémoire de chat.

**Pourquoi** : sans lire Beth/Morty en premier, un agent ignore les 5 états Beth (GREEN/ORANGE/RED/HALT_LD03/HALT_LD04) et peut écrire une décision qui viole un HARD SAFETY sans s'en rendre compte.

### 1.2 Sunday Uplink — revue hebdomadaire ritualisée

Le Sunday Uplink est l'unique moment de revue hebdomadaire Life OS :
- Discovery consolide le ZORA state.
- Orville compile les crew findings Ikigai.
- Chapel expose le Scorecard 12WY.

**Pourquoi** : un système sans revue hebdomadaire dérive. Les drifts LD04 cognition, LD05 isolation, LD06 bond fracture doivent être détectés **avant** qu'ils ne forcent un HALT Beth. Le Sunday Uplink est le **seul moment toléré** pour escalader à A0 (board observer passif).

### 1.3 Loop Engineering L2 — Book aggregator weekly

Book (A3 LD01) supervise en H1 weekly le triangle Picard (H10) × Jerry (B1 Lighting) × Summers (B1 Verse). À chaque tour H1 :
1. Lit le tick H10 de Picard → `<proj>/MANIFEST.md`.
2. Lit Jerry Pulse → 4 indicateurs `lights_*`.
3. Lit Summers Verse → la ligne narrative du quadrant.
4. Produit la fiche P&L hebdo.
5. Append un épisode-mémoire dans `99_meta/calendar.md`.

**Pourquoi** : Book = aggregator (PAS coach direct), conformément à `A3_Book_LD01_Spec.md` §Boundaries. Le calendar devient le **log canonique de la boucle**.

### 1.4 Beth Alignment Log — veto durable

Toute décision Beth écrit dans `Beth_Alignment_Log/`. Pas un journal de chat : un fichier canonique dans le filesystem qui survit aux compactions de contexte.

**Pourquoi** : un veto qui n'est pas écrit peut être contesté. Un veto écrit dans le filesystem est une décision traçable, reversible si Beth re-vérifie.

## 2. Garde-fous

### 2.1 HARD SAFETY — Beth veto automatic LD03 LD04

```yaml
beth_thresholds:
  LD03_minimum: 4.0
  LD04_minimum: 3.5
  multi_domain_alert: 3
```

LD03 (Culber Health) < 4.0 → `HALT_LD03` automatic. LD04 (Tilly Cognition) < 3.5 → `HALT_LD04` automatic. Cascade LD03→LD04 vérifiée à chaque Sunday Uplink.

**Pourquoi** : sans seuils chiffrés, Beth ne peut pas répondre en <5 minutes. Avec des seuils, Beth peut rejeter mécaniquement et escalader seulement les cas ambigus.

### 2.2 Context Pack obligatoire (9 champs)

```yaml
required_context_pack_fields:
  - ship
  - crew_member
  - next_action
  - framework
  - domain_impact
  - l0_skill_required
  - beth_clearance
  - evidence_paths
  - output_artifact
```

**Pourquoi** : un champ manquant = `BLOCKED_CONTEXT_PACK_INCOMPLETE`. Cette règle transforme un pipeline de bonne volonté en **protocole vérifiable**.

### 2.3 A3 ne compile JAMAIS de décision finale

Verbatim canon (`A2_Discovery_ZORA_Spec.md:66`) :
> *"The A3 domain officers never compile final Discovery reports. They provide LD01-LD08 findings; Discovery/ZORA synthesizes."*

**Pourquoi** : si un A3 publie directement un verdict, le pipeline A2/A1 est bypasse. Casser cette séparation = perdre la traçabilité.

### 2.4 Anti-paperclip Saru 1000T (3 garde-fous canon)

1. **Boundary Book LD01** — Saru ne peut pas overrider la stratégie business.
2. **AREA_STANDARD P1 Work ON not IN** — Saru ne peut déclencher B1 review que si ≥2 B2 domains en conflit (scarcity seule ne suffit pas).
3. **Musk pivot = agency over utopia** — Saru DOIT évaluer si l'intention augmente l'**agency** ou attend salvation externe.

**Pourquoi** : automatiser une idéologie sans agency check = paperclip. Le SpaceX IPO 85.7B Greenshoe est classé anti-pattern (`_etudes_cas/2026-06-15_spacex-ipo-greenshoe-85-7b.md`).

## 3. Cadences

### 3.1 Horizons canon H1/H3/H10/H30/H90 (mapping LDxx)

| Horizon | LD | A3 twin | Cadence |
|---|---|---|---|
| H1 | LD01 | Book | Weekly P&L |
| H3 | LD02 | Saru | Quarterly runway |
| H10 | LD03, LD06, LD07 | Culber, Burnham, Reno | 10-week cycle |
| H30 | LD04, LD05 | Tilly, Stamets | 30-day learning / network half-life |
| H90 | LD08 | Georgiou | Quarterly legacy |

**Pourquoi** : Karpathy H1→H90 = grille temporelle canonique. Une lecture rapide pourrait inverser Saru H1 ↔ Book H10 — **D3 nuance critique** : canon verrouille Saru H3 / Book H1.

### 3.2 Sunday Uplink = revue weekly ritualisée

Cf. §1.2. Discipline 50/30/20 (SNW load rule) impose 20% buffer-recovery — le Sunday Uplink consomme le buffer, pas l'exécution.

### 3.3 Cycle 12WY Q3 2026 (06/15 → 09/07) — Items Discovery

- **Item 1** (SOB Abdaty) → Burnham LD06 H10 Family
- **Item 3** (Auto-research IA) → Stamets LD05 mycelium network
- **Item 9** (structuration 35 A3 twins) → Discovery global
- **Item 12** (auto-amélioration) → Tilly LD04 cognition

**Pourquoi** : la cadence 12 semaines force à choisir ; Discovery supervise 4 items sur 12 du cycle Q3 2026.

### 3.4 Terrain A0 — items 1-2 hors session CC

> *"Items 1-2 = terrain A0 (hors session CC). Items 3-12 = orchestration A1/A2/A3 = scope Morty/Cerritos/Curie/Enterprise/Picard/Spock."* — `gatekeepers-readme`

**Pourquoi** : distinguer ce qui relève du board observer A0 (décisions physiques, soirées, rituels) de ce qui relève de l'orchestration scriptable CC. Confondre les deux crée des items fantômes.

## 4. Règles chiffrées connues

| Règle | Valeur | Source | Sens |
|---|---|---|---|
| LD03 minimum | 4.0 | SDD-005 / `A1_Beth_Spec.md` | Seuil Health ; en-dessous → HALT_LD03 |
| LD04 minimum | 3.5 | SDD-005 / `A1_Beth_Spec.md` | Seuil Cognition ; en-dessous → HALT_LD04 |
| multi_domain_alert | 3 | SDD-005 | ≥3 LD en alerte → escalade A0 |
| Book H1 weekly P&L | weekly | `book.twin.md` | Horizon canon Book |
| Saru H3 quarterly runway | quarterly | `saru.twin.md` | Horizon canon Saru |
| Culber H10 10-week health | 10-week | `culber.twin.md` | Horizon canon Culber |
| Tilly H30 30-day learning | 30-day | `tilly.twin.md` | Horizon canon Tilly |
| Stamets H30 network half-life | 30-day | `stamets.twin.md` | Horizon canon Stamets |
| Burnham H10 family cycle | 10-week | `burnham.twin.md` | Horizon canon Burnham |
| Reno H10 MVP build arc | 10-week | `reno.twin.md` | Horizon canon Reno |
| Georgiou H90 quarterly legacy | quarterly | `georgiou.twin.md` | Horizon canon Georgiou |
| Saru 1000T paperclip | 3 garde-fous | plan §18.3 + §22.4 | Boundary/AREA_STANDARD/Musk pivot |
| Nexus/OMK CLOS | 2026-06-20 | `A3_Saru_LD02_Spec.md` | sprint `dcc1235` SHA `8ad94d1` |
| Orbiter/ABC ACTIF | Q3 2026 | `A3_Burnham_LD06_Spec.md` | H10 Patrimoine baby-boomers |
| 4e Dormant réveil | Q4 2026 / Q1 2027 | plan §3.4 | Family/Home LD03+LD04 |
| Sunday Uplink | weekly | `Sunday_Uplink_Protocols/README.md` | Seul moment toléré escalade A0 |
| A0 board observer | passif | `a0_reasoning_map.md §4.2` | Milestones H30/H90 seulement |

## 5. Pièges documentés

### 5.1 Saru H1 vs Book H10 — inversion classique

Lecture rapide : Saru = H1 (weekly), Book = H10 (10-week). **Incorrect**.

**Canon verrouille** : Saru = H3 (quarterly), Book = H1 (weekly). Source : `saru.twin.md` + `book.twin.md` (anchors vérifiés résolus 2026-07-05).

### 5.2 Drift owner = Tilly+Spock, PAS Saru+Stamets

Plan §15.1.4 initialement mappait "Life Wheel drift → A3 Saru + Stamets". **Incorrect**.

**Canon verrouille** : drift = **Tilly (LD04) + Spock (Areas)**. Saru+Stamets restent narrow findings seulement. Source : `A2_Discovery_ZORA_Spec.md` ligne 125 (D4 close).

### 5.3 J04 typo "Creatry" vs "Creativity"

Doublon typo dans archive `_V3_STRUCTURE_2026-08-02/` :
- ✅ Vivant : `J04_Jerry_Solarpunk_LD05_LD07_LD08_Social_Creativity_Impact`
- � Mort (typo) : `J04_Jerry_Solarpunk_LD05_LD07_LD08_Social_Creatry_Impact`

**Canon = version correcte**. La typo est morte dans l'archive. Si un agent suit le doublon, il suit un lien mort.

### 5.4 Picard (corpus Geordi) vs Book (spec canon) — collision de nom

Le dossier Geordi `09_Life_OS/LD01_Business_Picard/` est nommé **Picard** (capitaine USS Enterprise, H10 projects owner), tandis que la spec canon `22_Wheel_Discovery/LD01_Business_Book/` est nommée **Book** (A3 officer Discovery, H1 weekly P&L aggregator).

**Lecture** : les deux sont canoniques, mais opèrent sur des couches différentes :
- Picard = L2 captain (PARA Projects) — twin `enterprise/picard.twin.md`
- Book = A3 officer Discovery (LD01 H1) — twin `discovery/book.twin.md`

Source : `ADR-LD01-008` ligne 38 + `ADR-LD01-009` (Book reste un Super Coach du Workflow Picard / Jerry / Summers).

### 5.5 AaaS variant Nexus ≠ Jerry J03 Nexus

Confusion fréquente : **deux concepts homonymes**.
- **J03 Jerry Nexus** = B1 captain transversal LD02+LD06 (actif, owner FIP).
- **Nexus/OMK (AaaS variant)** = Saru LD02 H3 Indépendance financière (CLOS 2026-06-20).

J03 reste actif ; Nexus/OMK est archivé. Le nom commun **Nexus** est trompeur.

### 5.6 SDD-006 énumère 7 domaines Business (obsolète sur 1 point)

`SDD-006_business-pulse-l2-pyramide.md` est ratifié, scellé, et **faux sur un point** : il énumère 7 domaines Business là où le canon en compte 8 (le 8e = John Jones / Martian Manhunter, Sales, escouade Illuminati).

**Statut** : amendement append-only en fin de fichier. Le corps reste intact parce que le fait qu'A'Space ait fonctionné à 7 domaines pendant un mois est lui-même une information.

### 5.7 Reading rapide = exclusivité A1 (PIEGE)

Plan §3.5 simplifie "Beth = Ikigai+Life Wheel+DEAL / Morty = 12WY+PARA+GTD" comme **responsabilité principale**. Lecture rapide = exclusivité. **Incorrect**.

**Canon verrouille** : Beth = veto **distribué** sur les 6 ships. Morty = routage **distribué** sur les 6 ships. Lecture Beth/Morty **en premier** prévient ce piège.

## 6. Ce que cette méthode n'est PAS

- **Pas un scoring isolé** — `state.json` est la machine à états partagée.
- **Pas une UI visuelle n8n** — la structure filesystem est lisible par TOUT harness.
- **Pas une compilation A3-only** — A3 fournit narrow findings, A2 synthétise.
- **Pas un tool-lock** sur un seul harness — CC/HA/MC/Shadow L1 lisent tous.

## 7. Raison d'être de la méthode

Le système Life Wheel existe pour servir cet objectif :
> *"Life OS is the fleet that helps A0 live, decide, recover, execute, and review without collapsing into tool maintenance."*

La méthode Life Wheel n'a de sens que si elle sert cet objectif. Toute pratique qui éloigne de cet objectif — tool hoarding, fractal creep, role collapse, conception drift — est un signal d'alerte qui doit déclencher un retour en Phase CLARIFY A0 (3 questions max).

> *"Si le scoring de cette idée prend plus de 5 minutes, c'est que l'idée n'est pas assez clarifiée. Retourne en Phase CLARIFY."*
> — `a0_reasoning_map.md §4.2`

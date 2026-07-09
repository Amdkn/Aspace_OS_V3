---
source: A0_MEMORY_CORE
date: 2026-05-17
type: baserow-database-analysis
status: ANALYZED_READ_ONLY
domain: Shadow_L1 / Life_OS / Baserow
tags: [#ShadowL1, #LifeOS, #Baserow, #ZORA, #12WY, #DatabaseAnalysis]
context7_sources:
  - /baserow/baserow
related:
  - C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\Shadow_L1\README.md
  - C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\Shadow_L1\02_life-os-baserow-schema-20260517.md
---

# Life OS Baserow Database Analysis — 2026-05-17

## Resume Executif

La base Life OS dans Baserow a change de strategie: au lieu de 8 tables separees LD01-LD08 comme hypothese initiale, elle contient actuellement une architecture plus sobre et plus relationnelle:

- une table centrale `LD 00 Life Wheel Zora`;
- une table d'execution `12WY Warp Core`;
- deux liens relationnels entre ZORA et 12WY.

Cette strategie est meilleure pour le demarrage: elle evite la fragmentation precoce et rend possible un pilotage global avant de multiplier les tables.

## Tables Detectees

| Table ID | Nom logique | Role | Rows |
|----------|-------------|------|------|
| `980285` | `LD 00 Life Wheel Zora` | Tableau de bord ZORA / Life Wheel / routage Morty | 10 |
| `980422` | `12WY Warp Core` | Rocks / intentions trimestrielles / execution 12WY | 2 |

Limite API:

- le token actuel permet de lire les champs et lignes de ces tables;
- la liste globale des tables de database n'est pas accessible par l'endpoint database;
- les deux tables ci-dessus ont ete decouvertes via table connue + champs `link_row`.

## Table 1 — LD 00 Life Wheel Zora

Table ID: `980285`

### Role

`LD 00 Life Wheel Zora` est le cockpit central de la Life Wheel. Elle contient les domaines, leur etat de sante, leur routage vers les frameworks, les couples de coordination Jerry, et les liens vers `12WY Warp Core`.

### Proprietes

| Field ID | Nom | Type | Analyse |
|----------|-----|------|---------|
| `8577455` | Nom du Domaine | text, primary | Identite du domaine |
| `8577456` | Notes | long_text | Contexte libre |
| `8577457` | Actif | boolean | Etat actif manuel |
| `8578399` | Veto Beth | boolean | Garde-fou conscience / veto |
| `8578416` | Morty Routing | single_select | Route vers le framework operant |
| `8578438` | Sante du Systeme | single_select | Signal ZORA qualitatif |
| `8578447` | Score Initial [T0] | number | Baseline debut cycle |
| `8578451` | Score Actuel | number | Mesure courante |
| `8578452` | Score Cible [T+12] | number | Objectif fin 12WY |
| `8578453` | Delta Velocite | formula | `Score Actuel - Score Initial [T0]` |
| `8578454` | Priorite du Cycle Actif | boolean | Filtre focus cycle |
| `8578542` | Jerry LD Couples Cordination | multiple_select | Couplage des domaines LD01-LD08 |
| `8578555` | Crew Discovery | single_select | A3/crew responsable par domaine |
| `8578938` | 12WY Warp Core | link_row -> `980422` | Lien vers rocks |
| `8585478` | Resume | link_row -> `980422` | Second lien vers rocks, probablement redondant ou reserve a synthese |

### Options Notables

`Morty Routing`:

- 12WY Curie
- PARA Computer
- GTD Holo Deck
- DEAL Holo Janeway
- Life Wheel Zora
- USS Orville IA/Ikigai

`Sante du Systeme`:

- En Croissance
- Stagnation / Maintenance
- Alerte (Margin Bleed / Negligence)

`Crew Discovery`:

- Book
- Saru
- Hugg
- Tilly
- Stamet
- Burnham
- Reno
- l'imperatrice

## Rows LD00 Detectees

| Row ID | Domaine | Routing | Sante | Priorite Cycle | Crew |
|--------|---------|---------|-------|----------------|------|
| `9` | LD 00 Ikigai | PARA Computer | En Croissance | true | |
| `1` | LD 01 Carriere & Business | 12WY Curie | En Croissance | true | Book |
| `2` | LD 02 Finance & Independence | GTD Holo Deck | Stagnation / Maintenance | true | Saru |
| `3` | LD 03 Sante & Bien Etre | GTD Holo Deck | Stagnation / Maintenance | true | Hugg |
| `4` | LD 04 Cognition & Formation | DEAL Holo Janeway | Alerte | true | Tilly |
| `5` | LD 05 Relation & Reseau | Life Wheel Zora | Alerte | false | Stamet |
| `6` | LD 06 Amour & Famille | USS Orville IA/Ikigai | | false | Burnham |
| `7` | LD 07 Loisir & Creativite | | | false | Reno |
| `8` | LD 08 Environment & Impact | | | false | l'imperatrice |
| `10` | LD 09 Horizons H1-H90 | | | false | |

## Table 2 — 12WY Warp Core

Table ID: `980422`

### Role

`12WY Warp Core` est la table d'execution des Rocks / intentions trimestrielles. Elle est deja reliee a `LD 00 Life Wheel Zora`, mais ses lignes ne sont pas encore peuplees.

### Proprietes

| Field ID | Nom | Type | Analyse |
|----------|-----|------|---------|
| `8578903` | Nom du Rock | text, primary | Nom actionnable du Rock |
| `8578904` | Notes | long_text | Contexte libre |
| `8578905` | Actif | boolean | Activation manuelle |
| `8578937` | Domaine ZORA | link_row -> `980285` | Lien principal vers domaine Life Wheel |
| `8578974` | Type de Vecteur | single_select | Projet vs Habitude |
| `8578999` | Statut | single_select | Backlog, Doing, Done, Off Track |
| `8579261` | Semaines d'Activation | multiple_select | W1-W13 |
| `8579267` | KPI / Regle de Succes | text | Definition of done |
| `8585465` | Score de Confiance | rating | Confiance subjective |
| `8585477` | Note Obsidian / PAR | url | Lien cortex documentaire |
| `8585479` | LD 00 Life Wheel Zora | link_row -> `980285` | Second lien vers ZORA, probablement redondant |

### Options Notables

`Type de Vecteur`:

- Projet (A une fin definie)
- Habitude (Action recurrente)

`Statut`:

- Backlog / To Do
- Active / Doing
- Done
- Paused / Off Track

`Semaines d'Activation`:

- W1 a W13

## Diagnostic Architecture

### Points Forts

1. `LD 00` joue bien le role de cockpit ZORA.
2. Les domaines LD01-LD08 existent comme records maitres, pas comme tables eparpillees.
3. `12WY Warp Core` contient deja les champs critiques: domaine, statut, semaines, KPI, confiance, lien Obsidian/PARA.
4. `Delta Velocite` existe deja comme formula.
5. Le routage Morty relie les domaines aux frameworks: 12WY, PARA, GTD, DEAL, Life Wheel, Ikigai.

### Fragilites

1. Les scores ZORA sont vides, donc `Delta Velocite` retourne `0` sans valeur analytique.
2. Tous les liens `12WY Warp Core` sont vides cote LD00.
3. `12WY Warp Core` contient deux lignes vides.
4. Il existe deux liens entre LD00 et 12WY:
   - `12WY Warp Core`;
   - `Resume`.
   Cette double relation peut devenir confuse si les roles ne sont pas separes clairement.
5. `Actif` est false partout dans LD00, alors que `Priorite du Cycle Actif` est true pour LD00-LD04.
6. Certains domaines n'ont pas encore de `Morty Routing` ni de `Sante du Systeme`.

## Recommandation Strategie

Ne pas revenir a 8 tables LD01-LD08 maintenant.

La meilleure prochaine etape est:

1. garder `LD 00 Life Wheel Zora` comme table des domaines;
2. garder `12WY Warp Core` comme table unique des Rocks;
3. peupler `12WY Warp Core` avec quelques Rocks reels;
4. lier chaque Rock a un domaine ZORA;
5. utiliser `Priorite du Cycle Actif` pour filtrer le cockpit;
6. ajouter plus tard des rollups/resumes si Baserow permissions le permettent.

## Correction Proposee Pour Les Deux Liens

Clarifier la semantique:

| Champ | Role recommande |
|-------|-----------------|
| `12WY Warp Core` | relation brute vers tous les Rocks du domaine |
| `Resume` | a renommer ou remplacer par rollup/synthese si besoin |

Si `Resume` reste un `link_row`, il risque de dupliquer `12WY Warp Core`. Preferer un vrai champ resume/rollup plus tard.

## Prochaine Action Manuelle

Dans `12WY Warp Core`, remplacer les deux lignes vides par 2 a 4 Rocks reels du cycle actif.

Minimum viable Rock:

- `Nom du Rock`;
- `Domaine ZORA`;
- `Type de Vecteur`;
- `Statut`;
- `Semaines d'Activation`;
- `KPI / Regle de Succes`;
- `Score de Confiance`;
- `Note Obsidian / PAR` si disponible.

## Preuve

Analyse realisee via API Baserow avec token masque:

- `GET /api/database/fields/table/980285/`
- `GET /api/database/rows/table/980285/?user_field_names=true&size=100`
- `GET /api/database/fields/table/980422/`
- `GET /api/database/rows/table/980422/?user_field_names=true&size=100`

Context7 consulte:

- `/baserow/baserow`

## Risques Residuals

- Le token ne permet pas de lister toute la database via endpoint database.
- D'autres tables Life OS peuvent exister mais ne pas etre decouvertables depuis les liens actuels.
- Les champs peuvent changer manuellement dans l'UI apres cette analyse.
- Les valeurs personnelles dans Baserow doivent rester hors des exports markdown si elles deviennent sensibles.

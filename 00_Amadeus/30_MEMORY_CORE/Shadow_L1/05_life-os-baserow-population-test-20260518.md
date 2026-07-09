---
source: A0_MEMORY_CORE
date: 2026-05-18
type: baserow-population-test-report
status: POPULATED
domain: Shadow_L1 / Life_OS / Baserow / 12WY
tags: [#ShadowL1, #LifeOS, #Baserow, #12WY, #PopulationTest]
context7_sources:
  - /baserow/baserow
related:
  - C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\Shadow_L1\04_life-os-baserow-12wy-architecture-analysis-20260517.md
---

# Life OS Baserow Population Test — 2026-05-18

## Resultat

Test de peuplement Baserow reussi.

Tables peuplees:

| Table | ID | Resultat |
|-------|----|----------|
| `LD00 ZORA Quarter Intent (Vision)` | `980285` | 4 domaines mis a jour |
| `The 12 Rocks (Objectifs)` | `981212` | 12 Rocks presents |
| `The Warp Core W1-W12 (Tactiques)` | `980422` | 17 tactiques W1-W4 presentes |

Verification finale:

| Table | Rows | Primary non vide |
|-------|------|------------------|
| LD00 | 10 | 10 |
| Rocks | 12 | 12 |
| Warp | 17 | 17 |

## Scope

Peuplement de test pour les domaines:

- LD01 Carriere & Business
- LD02 Finance & Independence
- LD03 Sante & Bien Etre
- LD04 Cognition & Formation

Le test a applique:

- les 3 visions/intents par domaine dans LD00;
- 3 Rocks par domaine, soit 12 Rocks;
- les tactiques W1-W4 fournies, soit 17 tactiques.

Note: le plan depasse le minimum recommande de 9 tactiques, mais il correspond au payload fourni pour le test.

## Changements Appliques

### LD00

Rows mises a jour:

- LD01
- LD02
- LD03
- LD04

Champs mis a jour:

- `Vision (Intent)`
- `Actif`
- `Priorite du Cycle Actif`
- `Statut`

### The 12 Rocks

Rocks crees ou reutilises depuis les lignes vides:

- LD01.R1 a LD01.R3
- LD02.R1 a LD02.R3
- LD03.R1 a LD03.R3
- LD04.R1 a LD04.R3

Champs principaux:

- `Nom du Rock`
- `Definition of Done (DoD)`
- `Statut`
- `Progression %`
- `LD00 ZORA Quarter Intent (Vision)`

### The Warp Core W1-W12

Tactiques W1-W4 creees ou reutilisees depuis les lignes vides.

Champs principaux:

- `Nom de la Tactique`
- `Domaine ZORA`
- `Type de Vecteur`
- `Statut`
- `Semaines d'Activation`
- `KPI / Regle de Succes`
- `The 12 Rocks (Objectifs)`

## Correction Pendant Test

Le champ primaire de `The Warp Core W1-W12` avait ete renomme en:

`Nom de la Tactique`

Le premier script utilisait encore l'ancien nom:

`Nom du Rock`

Baserow a cree/lie les tactiques, mais les titres etaient vides. Une correction a ensuite patché les 17 lignes sur le bon champ `Nom de la Tactique`.

## Non Fait

Pas encore peuple:

- `The Scorecard (Mesure)`
- `Calendar Tracker (Time Use)`
- Google Calendar
- n8n / Symphony automation

Ces tables doivent venir apres validation manuelle des Rocks/Tactiques.

## Sources Et Validation

Context7 consulte:

- `/baserow/baserow`

API Baserow utilisee, token masque:

- `GET /api/database/fields/table/{table_id}/`
- `GET /api/database/rows/table/{table_id}/?user_field_names=true`
- `PATCH /api/database/rows/table/{table_id}/{row_id}/?user_field_names=true`
- `POST /api/database/rows/table/{table_id}/?user_field_names=true`

## Risques Residuals

- Les accents ont ete neutralises sur certaines nouvelles valeurs pour garder le payload API stable.
- Les Scorecards ne sont pas encore creees, donc la mesure 12WY reste a brancher.
- Les Time Blocks ne sont pas encore relies aux tactiques.
- Le token ne garantit toujours pas la capacite a lister toute la database, seulement les tables connues.

---
source: A0_MEMORY_CORE
date: 2026-05-17
type: baserow-schema-plan
status: BLOCKED_TOKEN_SCHEMA_PERMISSION
domain: Shadow_L1 / Life_OS / Baserow
tags: [#ShadowL1, #LifeOS, #Baserow, #ZORA, #12WY]
context7_sources:
  - /baserow/baserow
related:
  - C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\Shadow_L1\README.md
  - C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\Shadow_L1\01_baserow-plane-handoff-20260517.md
---

# Life OS Baserow Schema — 2026-05-17

## Etat

La table `LD 00 Life Wheel Zora` est lisible via API, mais le token actuel ne peut pas creer de champs.

Erreur recue lors de la tentative d'ajout de colonnes:

`ERROR_NO_PERMISSION_TO_TABLE`

Conclusion:

- la lecture Baserow fonctionne;
- les lignes LD00-LD09 existent;
- la configuration schema est bloquee par permission token;
- aucune colonne n'a ete ajoutee par Codex.

## Table Detectee

| Element | Valeur |
|---------|--------|
| Database | `441861` |
| Table | `980285` |
| Role | `LD 00 Life Wheel Zora` |
| Rows | 10 |

## Lignes Maitres Detectees

| Row ID | Nom |
|--------|-----|
| 9 | LD 00 Ikigai |
| 1 | LD 01 Carrière & Business |
| 2 | LD 02 Finance & Independence |
| 3 | LD 03 Santé & Bien Être |
| 4 | LD 04 Cognition & Formation |
| 5 | LD 05 Relation & Réseau |
| 6 | LD 06 Amour & Famille |
| 7 | LD 07 Loisir & Créativité |
| 8 | LD 08 Environment & Impact |
| 10 | LD 09 Horizons H1-H90 |

## Champs Existants Detectes

| Field ID | Nom | Type | Note |
|----------|-----|------|------|
| 8577455 | Nom | text | primaire |
| 8577456 | Notes | long_text | existant |
| 8577457 | Actif | boolean | existant |

## Schema Canonique A Ajouter

Ces colonnes doivent etre ajoutees a `LD 00 Life Wheel Zora`.

| Colonne | Type Baserow vise | Fonction |
|---------|-------------------|----------|
| Code | text | ID stable: LD00, LD01, LD02... |
| Type de Domaine | single_select | Life Domain, Ikigai, Horizon |
| Statut | single_select | To Do, Doing, Done, Paused/Disconnected |
| Cycle Actif | text ou linked row future | Cycle courant: ex. H1-C3A, Q2-2026 |
| Score ZORA Actuel | number, 1 decimal | Score courant 1.0-10.0 |
| Score ZORA Cible | number, 1 decimal | Score cible 1.0-10.0 |
| Delta ZORA | number, 1 decimal | Delta manuel ou futur formula |
| Charge 12WY % | number, 0 decimal | Charge cognitive/temps pour le cycle |
| Rocks Actifs | number, 0 decimal | Nombre de rocks actifs |
| Rocks Done | number, 0 decimal | Nombre de rocks termines |
| Critere de Succes / KPI | text | Condition de validation |
| Semaines Activation | multiple_select | W1 a W12 |
| Cortex PARA | url | Lien vers Obsidian/Notion/PARA |
| Preuve SSOT | long_text | Liens de preuves et traces |

## Options Select

`Type de Domaine`:

- Life Domain
- Ikigai
- Horizon

`Statut`:

- To Do
- Doing
- Done
- Paused/Disconnected

`Semaines Activation`:

- W1
- W2
- W3
- W4
- W5
- W6
- W7
- W8
- W9
- W10
- W11
- W12

## Valeurs Initiales Recommandees

| Nom | Code | Type de Domaine | Actif | Statut |
|-----|------|-----------------|-------|--------|
| LD 00 Ikigai | LD00 | Ikigai | true | Doing |
| LD 01 Carrière & Business | LD01 | Life Domain | true | Doing |
| LD 02 Finance & Independence | LD02 | Life Domain | true | To Do |
| LD 03 Santé & Bien Être | LD03 | Life Domain | true | To Do |
| LD 04 Cognition & Formation | LD04 | Life Domain | true | To Do |
| LD 05 Relation & Réseau | LD05 | Life Domain | true | To Do |
| LD 06 Amour & Famille | LD06 | Life Domain | true | To Do |
| LD 07 Loisir & Créativité | LD07 | Life Domain | true | To Do |
| LD 08 Environment & Impact | LD08 | Life Domain | true | To Do |
| LD 09 Horizons H1-H90 | LD09 | Horizon | true | Doing |

## Relation Future LD01-LD08

Quand les `table_id` des tables de domaine LD01-LD08 seront disponibles:

1. Ajouter dans chaque table domaine une colonne `Domaine Parent` de type link-to-table vers `LD 00 Life Wheel Zora`.
2. Ajouter dans `LD 00` des rollups/resumes pour:
   - moyenne de `Score ZORA Actuel`;
   - moyenne de `Score ZORA Cible`;
   - count de rocks `Done`;
   - count de rocks actifs;
   - charge 12WY totale.
3. Creer deux vues par table domaine:
   - `Kanban Actif`, groupe par `Statut`, filtre `Cycle Actif`;
   - `Audit ZORA`, grille avec scores et delta.

## Action Requise

Dans Baserow, donner au token actuel les permissions de modification schema/table, ou creer un nouveau token avec permissions suffisantes.

Ensuite, relancer une mission Shadow L1:

`Configurer LD 00 Life Wheel Zora selon Shadow_L1/02_life-os-baserow-schema-20260517.md`

## Securite

- Aucun token n'a ete ecrit dans ce document.
- Ne pas coller le token Baserow dans le chat.
- Ne pas afficher `/home/amadeus/.hermes/.env` en brut.


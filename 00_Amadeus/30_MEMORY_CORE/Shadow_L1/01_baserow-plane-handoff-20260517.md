---
source: A0_MEMORY_CORE
date: 2026-05-17
type: shadow-l1-handoff
status: ACTIVE_BLOCKED_PLANE_AUTH
domain: Shadow_L1 / Baserow / Plane
tags: [#ShadowL1, #Baserow, #Plane, #Solaris, #W1, #Handoff]
context7_sources:
  - /baserow/baserow
  - /websites/developers_plane_so
related:
  - C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\README.md
  - C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\Shadow_L1\README.md
  - C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\Hermes Agent\12_symphony-baserow-plane-smoke-test-20260516.md
---

# Baserow / Plane Handoff — 2026-05-17

## But

Permettre a Gemini CLI et Claude Code CLI de reprendre l'integration Shadow L1 sans chercher dans Hermes Agent comme source active.

## Sources Docs

Context7 consulte le 2026-05-17:

| Service | Context7 Library ID | Usage |
|---------|---------------------|-------|
| Baserow | `/baserow/baserow` | API auth, rows API, `table_id`, `row_id`, `user_field_names` |
| Plane | `/websites/developers_plane_so` | API auth, `workspace_slug`, `project_id`, work-items |

Notes publiques retenues:

- Baserow rows API utilise `/api/database/rows/table/{table_id}/`.
- Baserow peut retourner les champs par nom avec `user_field_names=true`.
- Plane API utilise `workspace_slug` et `project_id` pour acceder aux work-items.
- Plane accepte API key via `X-API-Key` ou OAuth token via `Authorization: Bearer ...`, selon la configuration.

## Configuration Locale Connue

Chemin historique des variables Hermes:

`/home/amadeus/.hermes/.env`

Ne pas imprimer ce fichier en clair.

Variables attendues, noms seulement:

| Variable | Role | Statut |
|----------|------|--------|
| `BASEROW_DATABASE_TOKEN` | Token Baserow database/API | Present historiquement, valeur redacted |
| `PLANE_API_KEY` | Cle API Plane | Presente historiquement mais invalidee ou scope insuffisant probable |
| `PLANE_WORKSPACE_SLUG` | Workspace Plane cible | A confirmer |
| `PLANE_PROJECT_LIFE_OS` | Project id cible Life OS/Solaris | A creer/confirmer |

## Preuve Locale Connue

Ancien smoke test conserve en archive Hermes:

`Hermes Agent/12_symphony-baserow-plane-smoke-test-20260516.md`

Resume sans secrets:

| Element | Valeur |
|---------|--------|
| Source Baserow | table `955428`, row `133` |
| Ligne | `W1 - Launch Flash (Product) & Batman (Ops)` |
| Quarter | `H1-C3A : Solaris` |
| Baserow read | OK |
| Plane auth | HTTP 403 |
| Plane write | Non tente |
| Work-items crees | Aucun |

## Decomposition Solaris W1 Plane-Ready

Trois work-items prevus, non crees:

1. `[Solaris W1][R3A-La Forge] Definir les limites binaires du Content Pack`
2. `[Solaris W1][R3A-Le Portail] Creer le brief Anti-Flou obligatoire`
3. `[Solaris W1][R3A-Le Portail] Configurer BLOCKED pour brief incomplet`

Source commune:

`baserow:table/955428/row/133`

## Etat Plane

Le test precedent a recu HTTP 403 sur Plane.

Interpretation:

- la cle Plane collee precedemment doit etre consideree exposee;
- la cle peut etre invalide, disablee, mal scopee, ou non rattachee au workspace;
- le workspace/projet Plane doit etre cree ou confirme avant creation de work-items.

## Reprise Propre

1. Rotater la cle Plane exposee.
2. Creer/confirmer le workspace Plane cible.
3. Creer/confirmer le projet Plane cible pour Solaris ou Life OS.
4. Mettre les variables dans l'environnement local, pas dans markdown.
5. Tester `GET projects` ou `GET work-items` avant tout `POST`.
6. Creer les 3 work-items seulement apres auth OK.
7. Reporter les IDs Plane crees dans un log LLM Wiki ou dans un handoff Shadow L1.

## Interdits

- Ne pas coller les cles Baserow ou Plane dans un chat, fichier markdown, README, ou capsule.
- Ne pas lire `/home/amadeus/.hermes/.env` en sortie brute.
- Ne pas creer de work-items Plane si l'auth n'est pas d'abord verifiee.
- Ne pas modifier Hermes Agent sauf demande explicite d'archive.

## Risques Residuals

- Plane est probablement vide ou non initialise cote workspace/projet.
- L'ancien token Plane est expose et doit etre remplace.
- Baserow est lisible, mais les schemas/champs peuvent avoir change depuis le test.
- Les chemins WSL sont historiques; si la strategie Windows local remplace WSL, il faudra migrer les variables dans Windows User env ou un gestionnaire secret local.


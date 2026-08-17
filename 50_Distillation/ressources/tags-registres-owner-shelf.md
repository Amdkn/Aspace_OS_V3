---
type: Backend
title: TAGS — registres Owner (Star Trek) + Shelf (Doctor Who)
description: Tags obligatoires pour chaque document Geordi : Layer/Status/Owner/Strate/Purpose/Shelf + description. Owner = registre Star Trek v2 arbitré 2026-08-01 (Computer/Picard/Spock/Geordi/Data/Morty). Shelf = registre Doctor Who, scoped aux guides `00_KERNEL_OS/`.
tags: [tags, owner, shelf, star-trek, doctor-who, layer, status, strate, purpose, description]
generated: { by: minimax-m3, at: 2026-08-17T21:32:00Z }
verified:
  - { by: process:lecture-fichiers, at: 2026-08-17T21:32:00Z }
sources:
  - id: tags-md
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/00_Index/TAGS.md"
    title: "TAGS — registre Owner canon arbitré le 2026-08-01"
    last_modified: 2026-08-01
  - id: claude-md-root
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/CLAUDE.md"
    title: "CLAUDE.md — Racine Geordi"
    last_modified: 2026-08-01
  - id: resources-index
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/00_Index/RESOURCES_INDEX.md"
    title: "RESOURCES_INDEX"
    last_modified: 2026-08-01
okf_version: "0.2"
---

# TAGS — registres Owner (Star Trek) + Shelf (Doctor Who)

> Source normative pour `Owner` et `description:` non vide (critère bloquant
> d'indexation dans `RESOURCES_INDEX.md`).

## 1. Tags obligatoires (4)

| Tag | Type | Valeurs | Bloquant ? |
|---|---|---|---|
| `Layer` | obligatoire | `Local` \| `WSL` \| `VPS` | oui |
| `Status` | obligatoire | `Draft` \| `Active` \| `Deprecated` | oui |
| `Owner` | obligatoire | registre Star Trek v2 (6 valeurs) | oui |
| `Strate` | recommandé | `S0`–`S4` | non (mais conditionne `RESOURCES_INDEX.md`) |

## 2. Tags recommandés (2)

| Tag | Valeurs |
|---|---|
| `Purpose` | `PRD` \| `Guide` \| `Reference` |
| `Shelf` | registre Doctor Who (10 valeurs) |

## 3. Tag bloquant pour l'indexation

| Tag | Bloquant ? |
|---|---|
| `description` : une ligne non vide | **oui** — porte d'entrée `RESOURCES_INDEX.md` |

Sans description, la ressource n'entre pas dans le catalogue — c'est ce qui décide
de sa **récupérabilité future**.

## 4. Registre Owner (Star Trek v2)

| Owner | Domaine PARA | Fondement |
|---|---|---|
| `Computer` | Orchestration | Parent déclaré : `A2_COMPUTER_ENTERPRISE_PARA` |
| `Picard` | Projects | Spec A3 §Boundaries : « If a Resource becomes execution-critical, route a project request to Picard » |
| `Spock` | Areas | Élimination dans `next_owner` de la spec A3 |
| `Geordi` | Resources | Spec A3 : « Geordi is the Resources officer » |
| `Data` | Archives | Spec A3 : « Geordi flags duplicated or stale references for Data review » |
| `Morty` | Focus Gatekeeper | Bus `40_SYMPHONY_BUS/state.json` : `A1:Morty > A2:Computer > A3:Geordi` |

## 5. Registre Shelf (Doctor Who, scoped)

`11thDoctor` · `12thDoctor` · `13thDoctor` · `Yaz` · `Ryan` · `Graham` · `Amy` · `Rory` ·
`River` · `Clara`.

**Uniquement** sur les guides de `01_Guides/00_KERNEL_OS/` (héritage historique).

## 6. Registres abandonnés (et pourquoi)

Deux nomenclatures concurrentes circulaient et bloquaient le remplissage d'index :

- `13thDoctor | Yaz | Ryan | Graham` — anciennement dans TAGS.md
- `Doctor | Companion` — anciennement dans RESOURCES_INDEX.md

**Aucune équivalence automatique** n'est établie entre ces registres et le registre
Star Trek : les rôles ne se recouvrent pas terme à terme. Tout document portant un
`Owner` de l'ancien registre doit être ré-étiqueté à la main, en repartant de son
domaine PARA réel.

## 7. Matrice finale (8 tags au total)

| # | Tag | Type | Bloquant ? |
|---|---|---|---|
| 1 | `Layer` | obligatoire | oui |
| 2 | `Status` | obligatoire | oui |
| 3 | `Owner` | obligatoire | oui |
| 4 | `Strate` | recommandé | non |
| 5 | `Purpose` | recommandé | non |
| 6 | `Shelf` | optionnel scoped | non |
| 7 | `description` | bloquant indexation | **oui** |
| 8 | `tags` (libres) | optionnel | non |

Minimum pour entrer dans `RESOURCES_INDEX.md` : `Layer` + `Status` + `Owner` + `description`
non vides (et `Strate` recommandé pour le reroutage par strate).

## 8. Statut Constitution v1.0

L'article 5 rétrograde les ADR en jurisprudence. Le **registre Owner v2** est une
décision de gouvernance (qui fait quoi), pas une décision bloquante : il survit
sans tension à Article 6 (pas de gate anticonstitutionnel).

## Liens entrants

- `agents-md-identity-canon.md` — où loge AGENTS.md canon identité
- `a3-geordi-resources-officer.md` — le rôle Geordi défini dans la spec A3
- `rot-strates-s0-s4.md` — le tag `Strate` et la sémantique des 5 strates

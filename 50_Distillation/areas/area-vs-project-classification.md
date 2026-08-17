---
type: Concept
title: Area ≠ Project — le critère manquant
description: Ce qui distingue une Area d'un Project n'est pas la taille mais l'absence d'échéance ; toute confusion ici fait dériver Spock hors de sa juridiction et transforme une responsabilité durable en livrable jetable.
tags: [para, classification, area, project, spock, picard, doctrine]
generated: { by: minimax-m3, at: 2026-08-17T20:35:00Z }
verified:
  - { by: process:extraction-areas, at: 2026-08-17T20:35:00Z }
sources:
  - id: areas-readme
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/README.md"
    title: 02_Areas_Spock root README
    last_modified: 2026-05-21
  - id: spock-spec
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/A3_Spock_Areas_Spec.md"
    title: A3 Spock Spec - Areas
    last_modified: 2026-06-21
  - id: a1-spec
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/A1_Jerry_Areas_Spec.md"
    title: A1 Jerry Areas Spec
    last_modified: 2026-05-21
okf_version: "0.2"
---

# Area ≠ Project — le critère manquant

Le PARA Enterprise distingue quatre seaux : Projects, **Areas**, Resources, Archives. La confusion la plus coûteuse n'est pas entre Project et Resource, ni entre Archive et Area — c'est **entre Area et Project**. Un dossier Areas n'est pas un projet long : c'est un domaine **sans échéance** qu'on maintient ouvert.

## Le critère, tel qu'il est posé

`A3_Spock_Areas_Spec.md` répond en une phrase à la question « qu'est-ce qui est Area ? » :

> *Is this an ongoing responsibility or standard that must be maintained over time?*

`A1_Jerry_Areas_Spec.md` confirme côté macro :

> *Jerry is the macro business steward living inside Spock's Areas. Jerry owns business responsibility over time; Summer owns finite project execution.*

Et la `README.md` racine est sans ambiguïté :

> *Areas are not 'to-do' projects ; they are maintained systems.*

La **triade de critères** implicite :

1. **Pérennité** — la responsabilité est-elle tenue d'exister dans 12 mois ?
2. **Standard** — y a-t-il une doctrine à maintenir (seuil, gate, principe) ?
3. **Non-livrable** — l'item n'a pas de date de fin ni de définition de « done ».

Si les trois sont oui : Area. Sinon, Spock route ailleurs.

## La frontière Areas ↔ Projects (et le piège)

Le seau `02_Areas_Spock/J01_Jerry_Prime_LD01_Business/` contient 134 fichiers. Sa densité ne le rend **pas** Project — il le rend **vivant**. La doctrine canon (`README.md`, §Mission) est explicite :

> *Spock governs Areas: ongoing standards, responsibilities, and health of Life OS / Business OS domains.*
> *If work needs a finite outcome, route the action item to Picard.*

Et `A3_Spock_Areas_Spec.md` §Boundaries :

> *If the item has a deadline and deliverable, route to Picard.*
> *If the item is just reference material, route to Geordi.*

La règle implicite **pour chaque sous-dossier d'une Area** :

- Le dossier lui-même est **Area** (responsabilité durable).
- Toute action issue de ce dossier qui produit un livrable fini devient **Project** (Picard) via Cerritos (GTD).
- Toute doctrine pure sans action devient **Resource** (Geordi).

Une Area qui contient des sous-dossiers Project doit le **dire** (sinon c'est une fuite de分類 — voir concept `spock-areas-canon`). Le brief de distillation signale qu'un dossier d'Area portant une date de fin est probablement mal rangé : c'est l'application directe de cette frontière.

## Pourquoi cette distinction se perd

Trois raisons mesurées dans le corpus :

1. **Taille**. 134 fichiers semblent « projet ». Mais le PARA ne classe pas par taille, il classe par **cycle de vie**.
2. **Activité**. Une Area qui se met à jour régulièrement semble « en cours ». Une Area vivante produit des artefacts ; ce n'est pas pour ça qu'elle « finit ».
3. **Travail réel**. Les B2/B3 d'une Area produisent des preuves (KRs, gates, DoD). Ces preuves ressemblent à des livrables Project, mais elles sont des **artefacts de maintien**, pas des fins en soi.

Le test opérationnel tient en une question : *« Si je ferme ce dossier dans 6 mois, est-ce que quelque chose d'important disparaît avec lui ? »* Si oui, c'est une Area. Si non, c'est un Project qui a fini.

## Lien avec le cycle de vie

- **Area** : pas de graduation. Elle persiste ou est déclassée en Archive.
- **Project** : graduation `Gate 0 → Gate 7` (voir `project-graduation-gates.md`). Il finit en Business Done ou il meurt.
- **Resource** : consultatif, jamais pilotant.
- **Archive** : clos, conservé, hors cycle.

Une Area peut **contenir** des Projects (Summer's Verse sur la base d'une Area) mais elle n'en est pas un. C'est le sens de la métaphore du fractal (voir `fractal-b1b2b3-architecture.md`) : l'Area est la carte perpétuelle ; le Project en est une mission datée.
---
type: Decision
title: Geordi (03_Resources_Geordi) est la racine unique de la KB
description: La décision D-2026-08-01-#1 fait de `03_Resources_Geordi/` (et non V3, et non `04_Archives_Data/`) la source de vérité unique de la base de connaissance. Les archives — y compris `_V3_STRUCTURE_2026-08-02/` — ne sont qu'un héritage réversible, pas une source de canon.
tags: [kb, geordi, ressources, source-of-truth, decision, 2026-08-01, unification]
generated: { by: minimax-m3, at: 2026-08-17T23:50:00Z }
verified:
  - { by: process:lecture_concepts_archives, at: 2026-08-17T23:50:00Z }
sources:
  - id: archive-readme
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/04_Archives_Data/_V3_STRUCTURE_2026-08-02/README.md"
    title: « La source vivante » — section explicite
    last_modified: 2026-08-02
  - id: bucket-readme
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/04_Archives_Data/README.md"
    title: Mission A3 Data, ce qui est archivé et ce qui ne l'est pas
    last_modified: 2026-05-20
  - id: a3-spec
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/04_Archives_Data/A3_Data_Archives_Spec.md"
    title: Boundaries — Data does not delete by default, route active items back
    last_modified: 2026-06-21
okf_version: "0.2"
---

# Geordi (03_Resources_Geordi) est la racine unique de la KB

## Verbatim du README d'archive

> **« La source vivante »**
>
> ```
> C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\
> ```
>
> **« Point d'entrée `03_Resources_Geordi/CLAUDE.md` · index des index
> `00_Index/INDEX_OF_INDEXES.md`. Les 4 piliers de la KB : **OKF** ·
> **Wiki** · **Graphify** · **Dox**. Geordi est la racine unique de la
> KB — décision `D-2026-08-01-#1`. »**
>
> — `_V3_STRUCTURE_2026-08-02/README.md` § La source vivante

## Les 4 piliers

| Pilier | Rôle |
|---|---|
| **OKF** | format canonique des concepts (frontmatter, sources, `verified`) |
| **Wiki** | graphe de navigation entre concepts, navigation humaine |
| **Graphify** | pipeline d'extraction de graphes depuis le corpus |
| **Dox** | documentation opérationnelle, runbooks, briefs |

## Pourquoi cette décision existe

**Le déclencheur** est explicite dans le README d'archive : la V2 a
mené **les 2026-08-01 et 02** une **unification des Ressources Geordi**.
Auparavant, **deux arborescences PARA** coexistaient :

1. **Celle de V2** (la vivante, mais éclatée)
2. **Celle de V3** (un héritage, jamais réécrit)

V3 portait donc « une seconde arborescence PARA, périmée et concurrente
de celle qui fait autorité ».

**La décision D-2026-08-01-#1** tranche : Geordi (03_Resources_Geordi)
est **la racine unique de la KB**. Tout ce qui se trouve ailleurs — y
compris dans `04_Archives_Data/_V3_STRUCTURE_2026-08-02/` — est **un
héritage réversible**, pas une source de canon.

## Les trois sources possibles, classées

| Source | Statut | Rôle dans un projet RDF |
|---|---|---|
| `03_Resources_Geordi/` | **canonique** | URI primaire des entités |
| `04_Archives_Data/_V3_STRUCTURE_2026-08-02/` | héritage réversible | `aspace:archivePath` secondaire |
| `04_Archives_Data/graphify-out/graph.json` | run partiel 14/25 | `aspace:derivedFrom` après validation |

## L'effet sur le graphe RDF

Pour chaque entité, le graphe RDF devrait avoir **trois propriétés** :

```turtle
<aspace:entity/X>
    aspace:canonicalPath "_V3_STRUCTURE_2026-08-02/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/..." ;
    aspace:archivePath "_V3_STRUCTURE_2026-08-02/..." ;
    aspace:derivedFrom "graphify-out/graph.json#node_123" .
```

Le `canonicalPath` est dans Geordi, l'`archivePath` est dans le
sous-dossier d'archive pertinent, et le `derivedFrom` est la trace
d'extraction Graphify (avec sa qualité : 14/25 chunks dans le run
mesuré).

## Ce que cette décision n'est PAS

- **Ce n'est pas une décision de détruire V3**. V3 conserve 12 fichiers
  réels + ~2 600 dossiers vides (cf. `archive-v3-structure-snapshot`).
- **Ce n'est pas une décision de déplacer Geordi ailleurs**. Geordi reste
  dans le seau Resources (03), pas dans Archives.
- **Ce n'est pas une décision de figer les archives**. Les archives
  restent **réversibles** via `ARCHIVE_MANIFEST.json` (cf. ADR-SOBER-002).

## Concepts liés

- [[archive-v3-structure-snapshot-2026-08-02]] — l'application concrète de cette décision.
- [[data-role-a3-archives-officer]] — la doctrine `archive-and-document` qui s'aligne.
- [[adr-sober-002-anti-paperclip-doctrine]] — la garantie de réversibilité.
- [[graphify-burst-chunk-duplication-pattern]] — l'impact sur la désignation du chemin canonique.

---
type: Concept
title: Pourquoi 11 prédicats typés, pas un seul relatedTo
description: Le constat : 129 relations, toutes aspace:relatedTo. Le schema propose 11 prédicats typés (instantiates, appliesTo, dependsOn, partOf, refines, supersedes, pairedWith, governs, cites, handledBy, seeAlso). Chaque prédicat est illustré par au moins deux relations réelles du graphe — règle du poste : un prédicat qui ne peut pas être illustré deux fois n'a pas lieu d'être.
tags: [ontologie, predicat, relation, semantique, rdf]
generated: { by: minimax-m3, at: 2026-08-17T20:30:00Z }
verified:
  - { by: process:lecture-relations, at: 2026-08-17T20:30:00Z }
sources:
  - id: schema_ttl
    resource: C:/Users/amado/ASpace_OS_V3/50_Distillation/ontologie/aspace-schema.ttl
    title: aspace-schema.ttl
    last_modified: 2026-08-17
  - id: instances_ttl
    resource: C:/Users/amado/ASpace_OS_V3/50_Distillation/ontologie/aspace-instances.ttl
    title: 129 relations aspace:relatedTo
    last_modified: 2026-08-17
okf_version: "0.2"
---

# Pourquoi 11 prédicats typés, pas un seul `relatedTo`

Le 2026-08-17, les 129 relations du graphe sont toutes `aspace:relatedTo`.
C'est un mur blanc : aucun sens n'est porté. La requête « quels concepts sont
en tension avec d'autres » rend zéro résultat, pas parce qu'il n'y a pas de
tension, mais parce que la tension n'a pas de place dans le graphe.

## Le critère : « un prédicat sans deux illustrations n'existe pas »

Avant d'ajouter un prédicat, je vérifie qu'au moins deux relations du graphe
s'en serviraient naturellement. Sinon, le prédicat attend des relations qui
n'existent pas — c'est un embellissement de taxonomie.

Cinq prédicats ont passé ce filtre sans difficulté :

- **`aspace:instantiates`** — 8+ relations : ABC OS instancie Summer's Verse,
  53 B3 Roster instancie Eight Domain, archive-v3-snapshot instancie
  ADR-SOBER-002, Cerritos Plane instancie Cerritos GTD.
- **`aspace:dependsOn`** — 7+ relations : Summer's Verse dependsOn 12WY,
  OMK dependsOn 53 B3 Roster, Cerritos Plane dependsOn Cerritos GTD.
- **`aspace:partOf`** — 5+ relations : 53 B3 Roster partOf Eight Domain,
  Triptyque partOf OMK, graphify-burst partOf graphify-out pipeline.
- **`aspace:appliesTo`** — 6+ relations : ADR-SOBER-002 appliesTo V3 snapshot,
  B2 Harmonization Matrix appliesTo ABC OS / Alikaly / Marina / RILCOT,
  Picard Project Pattern appliesTo OMK.
- **`aspace:refines`** — 2+ relations : OMK US Market Pivot refines OMK
  Business OS (géographie), ABC Compliance Gate refines ABC OS (vue légale).

Cinq prédicats passent avec une ou deux illustrations, mais sont essentiels
pour la sémantique à venir :

- **`aspace:supersedes`** — 1 illustration claire (vocabulaire actuel vs
  legacy) + 1 potentielle (V0.5 SDD vs V0.2-V0.4 legacy). Conservé car
  « supersede » est sémantiquement distinct de « refine » (il invalide le
  précédent, ne le complète pas).
- **`aspace:pairedWith`** — 1 illustration claire (ADR-META-001 ↔
  ADR-SOBER-002) + 1 potentielle (les 4 jumeaux DEAL Dal/Rok-Tahk/Zero/Gwyn).
  Conservé car la symétrie ne peut pas s'exprimer via dependsOn.
- **`aspace:governs`** — émerge des descriptions (Constitution v1.0
  gouverne l'identité, ADR-SOBER-002 gouverne les archives). Conservé
  car la nuance « juridiction » est sémantiquement distincte d'« usage ».
- **`aspace:cites`** — au moins une illustration (Sovereignty-3-niveaux
  cite concept_adr dans ses sources). Conservé : les futurs concepts
  citeront leurs sources.
- **`aspace:handledBy`** — 1 illustration (archive-v3-snapshot handledBy
  A3 archives officer). Conservé en prévision : la sous-représentation des
  personas dans le bundle est un signal à intégrer.

Un dernier prédicat n'est pas une relation typée au sens fort — c'est un
marqueur d'extériorité :

- **`aspace:seeAlso`** — 0 illustration interne. Mais c'est le prédicat
  canonique pour les 4 liens non résolus qui pointent vers le LLM_Wiki
  amont (concept_sovereignty, entity_rick, sources/source_*). Sa raison
  d'être n'est pas dans le bundle : c'est un connecteur vers l'amont.

## Pourquoi `supersedes` n'est pas `refines`

`refines` et `supersedes` se ressemblent au premier abord. La différence :
`refines` dit « A est une variante plus étroite de B ; les deux restent
utiles ». `supersedes` dit « A invalide B ; B n'a plus de rôle actif ».

Un exemple concret : le vocabulaire actuel d'agents (A0 Amadeus / A1 Beth /
A2 Computer / A3 Data) `supersedes` le vocabulaire legacy (GravityClaw /
Rick / Doctors / IronClaw). On n'utilise plus les noms legacy ; ils sont
archivés. À l'inverse, OMK US Market Pivot `refines` OMK Business OS : les
deux restent actifs, le pivot est une spécialisation géographique du pivot
général.

Confondre les deux transformerait le graphe en un cimetière de variantes,
où aucune n'est jamais caduque. La distinction est ce qui rend la confiance
interrogeable.

## Pourquoi `governs` n'est pas `appliesTo`

`appliesTo` décrit l'usage : « B2 Harmonization Matrix appliesTo ABC OS »
signifie que la matrice a été mobilisée pour cadrer le projet ABC. `governs`
pose la juridiction : « Constitution v1.0 governs l'identité des agents »
signifie qu'aucun agent ne peut dévier de la Constitution sans escalader.

La nuance est juridique. `appliesTo` est opérationnel (comment on s'en sert) ;
`governs` est normatif (qui a autorité sur quoi). Si on les fusionne, on perd
la capacité de distinguer « la matrice a guidé le projet » de « la matrice
impose le projet » — deux phrases très différentes dans un audit.

## Ce que le schéma ne propose pas

Pas de `aspace:contradicts`. La requête Q3 le cherche, elle rendra 0 résultat.
Le graphe n'a pas encore de pôles contradiction déclarés — c'est un signal à
remonter, pas un trou à combler avec un prédicat décoratif. Le jour où une
contradiction sera documentée, le prédicat s'ajoutera à ce schéma.

Pas de `aspace:supersedes` comme symétrique de `aspace:supersededBy`. La
relation est asymétrique par nature : A supersede B signifie « A invalide B »,
pas « A est invalidé par B ». `owl:AsymmetricProperty` marque cela.

Pas de `aspace:hasInstance` non plus : l'inverse de `instantiates` peut
s'inférer par `owl:inverseOf` si jamais on en a besoin. Le schéma n'a pas
à dupliquer ce que RDFS/OWL infèrent.
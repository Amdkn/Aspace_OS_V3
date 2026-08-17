---
type: Concept
title: Les 4 liens non résolus pointent vers le LLM_Wiki amont — et c'est un signal
description: Les liens compounding-knowledge-wiki → sources/source_llm-wiki-pattern et wiki-schema-llm-wiki → concept_sovereignty, entity_rick, sources/source_gemini-takeout-2026-05 utilisent un naming systeme etranger au bundle (concept_*, entity_*, sources/source_*). Ce naming vient de l'arborescence wiki/concepts/, wiki/entities/, wiki/sources/ du LLM_Wiki V2 amont — pas du bundle distille.
tags: [ontologie, liens-non-resolus, llm-wiki, amont, sources]
generated: { by: minimax-m3, at: 2026-08-17T20:30:00Z }
verified:
  - { by: process:analyse-liens-non-resolus, at: 2026-08-17T20:30:00Z }
sources:
  - id: vocabulaire_mesure_json
    resource: C:/Users/amado/ASpace_OS_V3/50_Distillation/ontologie/vocabulaire_mesure.json
    title: exemples_liens_non_resolus
    last_modified: 2026-08-17
  - id: wiki_schema_llm_wiki_concept
    resource: C:/Users/amado/ASpace_OS_V3/50_Distillation/ressources/wiki-schema-llm-wiki.md
    title: wiki-schema-llm-wiki
    last_modified: 2026-08-17
  - id: llm_wiki_schema
    resource: C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/03_Memory_Unified/LLM_Wiki/wiki/schema.md
    title: LLM_Wiki schema (raw, amont)
    last_modified: 2026-08-17
okf_version: "0.2"
---

# Les 4 liens non résolus pointent vers le LLM_Wiki amont — et c'est un signal

Le 2026-08-17, la mesure rapporte 4 liens non résolus. Tous les quatre
partagent une propriété : ils utilisent un naming systeme étranger au bundle.

## Le naming systeme

Les cibles sont préfixées :

- `concept_sovereignty` → vit dans `LLM_Wiki/wiki/concepts/concept_sovereignty.md`
- `entity_rick` → vit dans `LLM_Wiki/wiki/entities/entity_rick.md`
- `sources/source_llm-wiki-pattern` → vit dans `LLM_Wiki/wiki/sources/source_llm-wiki-pattern.md`
- `sources/source_gemini-takeout-2026-05` → vit dans `LLM_Wiki/wiki/sources/source_gemini-takeout-2026-05.md`

Le namespace `concept_*`, `entity_*`, `sources/source_*` est la convention
de nommage de l'arborescence `LLM_Wiki/wiki/` (sous-dossiers `concepts/`,
`entities/`, `sources/`). Cette convention est documentée dans
`wiki-schema-llm-wiki` et dans le schema.md amont.

Le bundle distillé utilise un namespace différent : `urn:aspace:concept:`
plutôt que `concept_*`. Les deux ne sont pas équivalents — le bundle a son
propre système d'URI et son propre index.

## Pourquoi ces cibles existent ailleurs mais pas ici

Le bundle est une distillation : il a retenu 95 concepts jugés centraux.
Le LLM_Wiki amont en compte plus, dans une structure plus plate (un fichier
par concept, sans filtrage). Les concepts amont que le bundle n'a pas
distillés restent dans `wiki/concepts/` mais ne sont pas dans le graphe
distillé.

C'est par design. Le bundle est un sous-ensemble explicite. Si demain on
distille `concept_sovereignty` ou `entity_rick`, ils entreront dans le
graphe avec leur URI `urn:aspace:concept:ressources:sovereignty-3-niveaux`
(pour le premier) — mais ce n'est pas le cas au 2026-08-17.

## Pourquoi un prédicat dédié (`aspace:seeAlso`)

Les quatre liens auraient pu être :

1. **Supprimés** — pas de relation dans le graphe. C'est l'option la plus
   simple, mais elle perd le signal : on ne saura plus qu'il y a une
   source amont à consulter.
2. **Résolus en URI** — inventer une URI par défaut et supposer qu'elle
   pointe quelque part. C'est la solution du piege déja payé sur ce poste
   (placeholder.invalid). À éviter.
3. **Marqués comme externes** — c'est l'option `aspace:seeAlso`. La
   relation existe, elle est honnête (« il y a une source là-bas »), elle
   n'engage pas la sémantique du graphe.

J'ai retenu la troisième option. `aspace:seeAlso` est déclaré dans le schéma
avec `owl:IrreflexiveProperty` pour signaler qu'il pointe vers l'extérieur
— il n'a pas de réciproque dans le graphe interne.

## Comment traiter ces liens dans le futur

Trois voies selon la destination visée :

1. **Si la cible amont devient un concept du bundle** : remplacer
   `aspace:seeAlso` par la relation typée qui s'impose (`aspace:instantiates`,
   `aspace:cites`, etc.) et poser l'URI canonique du bundle. Le lien
   externe disparaît.
2. **Si la cible amont reste externe** : conserver `aspace:seeAlso` avec
   une note expliquant la nature externe. C'est un signal durable qu'une
   source amont existe, sans la valider.
3. **Si la source amont n'existe pas / est inventée** : supprimer le lien.
   Aucun lien vers quelque chose qui n'existe pas. Le piege
   `placeholder.invalid` a déjà coûté.

## Ce que la requête Q9 vérifie

Une conséquence mesurable : si demain une relation traverse deux bundles
(ex : `wiki-schema-llm-wiki` dans `ressources` pointant vers
`compounding-knowledge-wiki` dans `ressources` aussi), Q9 ne la voit pas
parce que les deux sont dans le même bundle. Mais si on lit
`wiki-schema-llm-wiki` dans `ressources` pointant vers un concept de
`projets`, Q9 la voit. Au 2026-08-17, Q9 rend 0 ligne. Les bundles sont
des silos ; les `seeAlso` qui les relient à l'amont ne traversent pas le
graphe interne.
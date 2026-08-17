---
type: Concept
title: Pourquoi 11 classes, pas une seule — la décomposition d'« aspace:Concept »
description: Le constat mesure : 62/95 concepts sont kind:Concept, ce qui transforme la classe en fourre-tout. La décomposition proposée distingue les concepts par engagement (Doctrine/Decision/Playbook/Pattern) et isole les artefacts (Project/Backend/Archive/Event/Relation) et les personas des concepts purs.
tags: [ontologie, classe, doctrine, artefact, modelisation]
generated: { by: minimax-m3, at: 2026-08-17T20:30:00Z }
verified:
  - { by: process:lecture-concepts, at: 2026-08-17T20:30:00Z }
sources:
  - id: vocabulaire_mesure_json
    resource: C:/Users/amado/ASpace_OS_V3/50_Distillation/ontologie/vocabulaire_mesure.json
    title: types_utilises
    last_modified: 2026-08-17
  - id: schema_ttl
    resource: C:/Users/amado/ASpace_OS_V3/50_Distillation/ontologie/aspace-schema.ttl
    title: aspace-schema.ttl
    last_modified: 2026-08-17
okf_version: "0.2"
---

# Pourquoi 11 classes, pas une seule

Le 2026-08-17, la mesure donne 11 types distincts pour 95 concepts ; l'un d'eux
(`Concept`) en couvre 62. Ce n'est pas une taxonomie, c'est un fourre-tout.

## Le critère de décomposition

Le critère qui fait bouger une classe de « concept pur » à « artefact » est
celui de la **matérialité temporelle**. Un concept pur existe indépendamment
du temps : une matrice, un cycle, un schéma de pensée — ils sont reproductibles
à l'identique. Un artefact, lui, a des frontières, des opérateurs, une date
ou un volume. Le versement V3 du 2026-08-02 a une date ; le cycle 12WY est
indéfiniment reproductible. Le premier est un `aspace:Event`, le second un
`aspace:Concept`.

Le critère qui fait bouger un concept pur à `aspace:Doctrine` est celui de
**l'engagement prescriptif**. Une doctrine est formulée comme un impératif :
« vérifier avant d'affirmer », « déplacer, ne pas supprimer », « une décision
architecturale est immuable ». Le concept pur est descriptif ; la doctrine
engage.

## Pourquoi garder `Concept` au sommet

Garder `Concept` au sommet de la hiérarchie n'est pas un aveu d'impuissance.
C'est承认 que la majorité des 95 concepts ne sont ni doctrines ratifiées, ni
artefacts datés, ni personas : ce sont des idées descriptives, des cadres, des
observations. `aspace:Concept` est la classe « par défaut, descriptive ». Les
sous-classes expriment un engagement plus précis. Un concept qui mérite
d'être promu en doctrine le devient — c'est un acte de modélisation qu'on
peut faire ou ne pas faire.

## Les 4 singletons ne sont pas un défaut

Le brief demande d'examiner les types à une seule occurrence (Vulnerability,
Pattern, Entity, Relation). Trois attitudes possibles : les fusionner dans une
classe plus peuplée, les supprimer, ou les garder. Je garde les quatre,
pour deux raisons :

1. **La rareté est un signal, pas un défaut.** Une seule `Vulnerability`
   signale qu'on n'a pas encore mesuré de failles ; ça ne dit pas que les
   failles n'existent pas. Supprimer la classe attendrait qu'on en ait
   plusieurs pour les qualifier — c'est attendre d'avoir le feu pour acheter
   un extincteur.
2. **Chaque singleton a une sémantique distincte.** Vulnerability (sécurité),
   Pattern (récurrence), Entity/persona (acteur), Relation (description de
   règle canonique) — les fusionner dans une seule classe forcerait à
   réintroduire la distinction par des sous-classes qui ne seraient que des
   doublons de classes existantes.

## Pourquoi `aspace:Persona` plutôt que `aspace:Entity`

Le bundle utilise `kind:Entity` pour un seul concept : A3 Geordi Resources
Officer — un persona. Renommer en `Persona` est plus précis. La classe
« Entity » au sens RDF est trop générique (tout est une entité RDF). Garder
« Entity » dans le schéma créerait une confusion avec le terme RDF.

## Pourquoi 11 classes et pas 50

La règle appliquée : **chaque classe doit pouvoir accueillir au moins deux
occurrences** dans un avenir proche, sinon c'est une décoration. Les 11
classes proposées couvrent toutes les occurrences des 95 concepts. Aucune
n'est décorative : chacune a au moins une occurrence immédiate (Concept : 62,
Project : 8, Backend : 9, Archive : 4, Decision : 3, Playbook : 3, Event : 2,
Doctrine : 5 = 3 Decision + 1 Pattern + 1 Doctrine ; Persona : 1,
Vulnerability : 1, Relation : 1, Pattern : 1). Aucune classe n'a été créée
« au cas où ».

## Ce qui n'a pas été décomposé

Les sous-classes de `Doctrine` (Decision, Playbook, Pattern) pourraient être
décomposées plus avant. Je n'ai pas poussé cette décomposition parce qu'elle
manquerait d'occurrences pour la justifier : Decision n'en a que 3. Ajouter
`aspace:ADR-FSD` (Functional Spec Doc) ou `aspace:ADR-INFRA` pour 1-2
occurrences chacune serait décoratif.
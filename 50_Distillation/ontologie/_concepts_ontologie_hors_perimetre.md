---
type: Concept
title: Ce que le schéma ne couvre pas — et pourquoi c'est honnête
description: Le schema couvre 11 classes, 11 predicats, 9 racines SKOS et 39 narrowers. Il ne couvre pas : les relations temporelles (avant/apres un événement), les relations quantitatives (mesure/comptage), la résolution fine des doublons projet/project, ni l'ontologie du LLM_Wiki amont. C'est une borne explicite, pas un trou.
tags: [ontologie, perimetre, schema, avenu, evolutions]
generated: { by: minimax-m3, at: 2026-08-17T20:30:00Z }
verified:
  - { by: process:limites-schema, at: 2026-08-17T20:30:00Z }
sources:
  - id: schema_ttl
    resource: C:/Users/amado/ASpace_OS_V3/50_Distillation/ontologie/aspace-schema.ttl
    title: aspace-schema.ttl — périmètre
    last_modified: 2026-08-17
okf_version: "0.2"
---

# Ce que le schéma ne couvre pas — et pourquoi c'est honnête

Un schéma qui prétend tout couvrir couvre mal. Ce concept liste les
décisions de modélisation qui ont été écartées, et pourquoi.

## Ce qui n'est pas dans le schéma

### Les relations temporelles

Aucun prédicat typé ne porte la temporalité. La requête « quels concepts
existaient avant le 2026-08-02 ? » ne peut pas être répondue avec ce
schéma. La temporalité vit dans `dcterms:source` (chemin du fichier) et
dans le nom du concept (`*-2026-08-02`), pas dans une relation typée.

**Pourquoi cette borne.** Introduire `aspace:before`, `aspace:after`,
`aspace:during` reviendrait à poser une ontologie temporelle. C'est un
projet à part entière — TIME ontology, OWL-Time, et un travail de
calage sur le corpus. Le bundle au 2026-08-17 ne porte pas de données
qui le justifient.

### Les relations quantitatives

Aucun prédicat ne porte une mesure. La requête « quels concepts pèsent
plus de 10000 mots ? » ne peut pas être répondue. Les quantifications
vivent dans les descriptions (`dcterms:description`) ou dans des
fichiers dédiés (`_substrat/`).

**Pourquoi cette borne.** Une ontologie de la mesure demanderait des
unités (mots, lignes, fichiers), des seuils, et des outils de comptage.
Le bundle n'a pas encore de workflow qui produit ces mesures de façon
récurrente.

### La résolution fine des doublons projet/project

Le SKOS expose `aspace:tag-project` avec un `skos:relatedMatch` vers
`aspace:tag-projet`. C'est un signal ; ce n'est pas une migration. Le
jour où la régénération des triplets tournera, le script pourra remplacer
`project` par `projet` dans toutes les instances. Le schéma n'a pas
prétendu le faire.

**Pourquoi cette borne.** La fusion touche les instances, pas le schéma.
C'est un acte de migration qui demande une exécution mesurée, pas un
déclaration dans le SKOS.

### L'ontologie du LLM_Wiki amont

Le LLM_Wiki a sa propre structure (concepts/, entities/, sources/,
relations/, comparisons/, syntheses/). Le schéma n'en décrit qu'un
connecteur : `aspace:seeAlso`. Tout le reste (les six types de pages,
les trois workflows ingest/query/lint, les conventions de nommage) vit
dans `wiki-schema-llm-wiki` et dans le `schema.md` amont.

**Pourquoi cette borne.** L'ontologie amont est plus riche que le
schéma distillé — c'est normal, l'amont est la source. La dupliquer ici
créerait deux sources de vérité. Le rôle du schéma est de poser les
classes que le bundle utilise, pas de répliquer celles de l'amont.

### Les classes « au cas où »

Le schéma ne crée pas `aspace:Algorithm`, `aspace:Metric`,
`aspace:Hypothesis`, `aspace:Roadmap` — des classes qui n'ont aucune
occurrence dans les 95 concepts. La règle appliquée : une classe sans
deux occurrences immédiates ou potentielles est décorative.

**Pourquoi cette borne.** Une taxonomie décorative coûte plus cher
qu'elle ne rend. Elle crée de l'attente (« il y a surely un truc à
classer là ») sans contenu. Mieux vaut l'ajouter le jour où trois
concepts se présenteront qui la justifient.

## Ce qui pourrait changer

- Si le bundle grossit à 200+ concepts, les sous-classes de `Doctrine`
  (Decision, Playbook, Pattern) pourront être décomposées (par exemple
  `aspace:ADR-FS` vs `aspace:ADR-INFRA` vs `aspace:ADR-FWK`).
- Si des relations inter-bundles apparaissent, de nouveaux prédicats
  transverses pourront s'ajouter (`aspace:crossReferencedBy` ?).
- Si des contradictions sont documentées, `aspace:contradicts` entrera
  dans le schéma — sa requête Q3 cessera de rendre vide.

Ces évolutions se font par ajouts successifs, pas par refonte. Le
schéma actuel est volontairement petit pour pouvoir grandir sans casser
ce qui existe.
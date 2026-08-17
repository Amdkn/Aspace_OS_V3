---
type: Bundle index
title: ontologie — Schema, vocabulaire, requetes, decisions de modelisation
description: Le sous-bundle de l'ontologie pose les classes, les predicats, le vocabulaire controle et les requetes qui interrogent le graphe de 95 concepts distilles.
tags: [distillation, okf, ontologie, schema, rdf, skos]
generated: { by: minimax-m3, at: 2026-08-17T20:30:00Z }
okf_version: "0.2"
---

Ce sous-bundle porte le **modele** du graphe A'Space OS : les classes
d'entites, les predicats types qui les lient, le vocabulaire controle
des tags, et les requetes qui repondent aux questions recurrentes.

Il ne decrit pas des fichiers mais des **notions**. Un type qui
n'apparait que dans un seul document n'est pas un type : c'est une
occurrence. La regle des trois occurrences vaut ici comme ailleurs.

# Files

## Schema (TTL — a parser avec rdflib)

- [aspace-schema.ttl](aspace-schema.ttl) — 11 classes, hierarchie `rdfs:subClassOf`, 11 predicats types (`instantiates`, `appliesTo`, `dependsOn`, `partOf`, `refines`, `supersedes`, `pairedWith`, `governs`, `cites`, `handledBy`, `seeAlso`) et le predicat d'information `niveauConfiance`. 125 triplets, parse sans erreur.

- [aspace-tags.ttl](aspace-tags.ttl) — Vocabulaire controle SKOS des 39 tags retenus sur 457 (regle des trois occurrences), organises en 9 racines (methode, architecture, agent-persona, artefact-type, domaine, connaissance, statut, cartographie, prompt-systeme). 275 triplets.

- [aspace-instances.ttl](aspace-instances.ttl) — **GENERE** par `scripts/concepts_vers_triplets.py`. Ne pas editer a la main. 2148 triplets, 95 sujets. La regeneration doit suivre toute modification du schema.

- [vocabulaire_mesure.json](vocabulaire_mesure.json) — **GENERE** par le script de comptage. La mesure du 2026-08-17 : 11 types, 457 tags distincts, 4 liens non resolus. Sert de point de depart aux decisions de modelisation.

## Requetes SPARQL

- [requetes.sparql](requetes.sparql) — Dix requetes commentees qui repondent a de vraies questions : ce qui n'a jamais ete relu par un humain (Q1), les concepts sans source (Q2), les contradictions declarees (Q3, vide attendu), les orphelins (Q4), la couverture par seau (Q5), la repartition par classe (Q6), l'alignement tag/classe (Q7), les predicats utilises (Q8), les liens inter-bundles (Q9, vide attendu), les tags sous le seuil (Q10).

## Concepts OKF — decisions de modelisation

Sept concepts expliquent pourquoi le schema prend la forme qu'il prend. Un schema sans ses raisons se defait au premier desaccord.

- [Pourquoi 11 classes, pas une seule](_concepts_ontologie_modele.md) — La decomposition d'`aspace:Concept` en Doctrine/Decision/Playbook/Pattern et l'isolement des Artefacts.

- [Pourquoi 11 predicats types, pas un seul relatedTo](_concepts_ontologie_predicats.md) — La regle du poste : un predicat sans deux illustrations n'existe pas. La distinction refine/supersedes, governs/appliesTo.

- [Pourquoi la regle des trois occurrences](_concepts_ontologie_seuil_tags.md) — Un tag seul n'est pas une categorie. 39 retenus sur 457, organises en 9 racines SKOS.

- [Le niveau de confiance doit etre interrogeable](_concepts_ontologie_confiance.md) — Les 95 concepts sont `confirmeMachine`, aucun n'a ete relu. C'est un fait qu'on doit pouvoir interroger, pas dissimuler.

- [Les 4 liens non resolus pointent vers le LLM_Wiki amont](_concepts_ontologie_liens_amont.md) — Le naming `concept_*`, `entity_*`, `sources/source_*` vient de l'arborescence amont, pas du bundle. Le predicat `aspace:seeAlso` est le connecteur.

- [Pourquoi urn:aspace:ns:](_concepts_ontologie_namespace.md) — Un namespace qui ne pretend rien. Pas de `https://aspace-os.org/`, pas de `placeholder.invalid`.

- [Ce que le schema ne couvre pas](_concepts_ontologie_hors_perimetre.md) — Les bornes explicites : pas de temporalite, pas de quantitatif, pas de doublons resolus, pas d'ontologie amont dupliquee.
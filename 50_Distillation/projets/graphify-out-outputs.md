---
type: Archive
title: graphify-out — Les 1208 sorties générées
description: Le tiers des fichiers .md du seau (1208 sur 2154) vit dans `graphify-out/` — sorties générées par le pipeline Graphify, pas de la connaissance écrite à la main. Distinction qui corrige l'impression "2154 fichiers = corpus entier".
tags: [archive, graphify-out, generated, substrat, comptage, correction]
generated: { by: minimax-m3, at: 2026-08-17T21:00:00Z }
verified:
  - { by: process:extraire_substrat_rdf, at: 2026-08-17T19:50:00Z }
  - { by: process:lecture_concepts_picard, at: 2026-08-17T21:00:00Z }
sources:
  - id: substrat
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/_substrat/01_Projects_Picard.jsonl"
    title: Substrat extraction JSONL — 2154 fichiers, 1208 dans graphify-out/
    last_modified: 2026-08-17
  - id: index-bundle
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/index.md"
    title: Index de la distillation — comptage 2154 .md
    last_modified: 2026-08-17
okf_version: "0.2"
---

# `graphify-out/` — Les 1208 sorties générées

## Le chiffre qui corrige une impression

Le seau `01_Projects_Picard` contient **2154 fichiers `.md`**. Mais
**1208 d'entre eux (~56%)** vivent dans `graphify-out/` — ce sont des
**sorties générées** par le pipeline Graphify, pas de la connaissance
écrite à la main. Le corpus **écrit à la main** est donc d'environ
**946 fichiers**, pas 2154.

C'est une correction de mesure : un agent qui lirait "01_Projects_Picard
= 2154 fichiers" aurait une impression fausse. Le brief de distillation
l'a explicitement signalé : "Ce chiffre doit figurer dans ton rapport".

## Structure de `graphify-out/`

Les 1208 fichiers sont rangés par `chunks/chunk_XXX/` — un découpage
en clusters probablement issus de la pipeline Graphify. Les chunks
concentrent souvent le même contenu ; c'est typique des **sorties
chunkées** où un même document source est éclaté en N vues.

**Effet observable** : la pipeline d'extraction substrat (script
`extraire_substrat_rdf.py`) produit des **doublons exacts** dans le
JSONL. Exemple : `SUPABASE_STRATEGY.md` apparaît deux fois à 6454 mots
identiques, et `picard_audit_solaris.md` deux fois à 2117 mots. Le
script d'extraction suit le chemin de fichier sans déduplication — ce
qui est correct pour un comptage brut.

## Les contenus les plus notables

| Fichier | Mots | Statut | Projet |
|---------|------|--------|--------|
| `SUPABASE_STRATEGY.md` | 6454 | DRAFT_FOR_A0_VALIDATION | Alikaly Bana Holding OS / alykaly-os-V2 |
| `drawbridge-workflow.md` | 4053 | (orig. ClaudeClaw) | — |
| `picard_audit_solaris.md` | 2117 | — | — |
| `picard_audit.md` | 1851 | — | — |
| `REBUILD_WORKFLOW.md` | 1704 | — | — |

`SUPABASE_STRATEGY.md` est le plus gros : 6454 mots, status DRAFT_FOR_A0
VALIDATION. C'est un **document client Alikaly** — peut-être un
spécifique Supabase pour la stack Alikaly. Le fait qu'il vive dans
graphify-out le marque comme **sortie**, pas comme source canonique.

## Ce que cela implique pour la distillation

Les 1208 fichiers de `graphify-out/` sont **accessibles au substrat**
mais **non prioritaires** pour la distillation sémantique. Un agent qui
s'y attaquerait lirait des dérivés, pas du canon. Le canon vit dans
les 946 fichiers écrits à la main — manifests, handovers, README,
ownerbooks, runbooks, chartes, B3 agent rosters.

## Liens

- [[summers-verse-framework]] — le canon qui se distingue de graphify-out
- [[omk-business-os]] — qui produit certains graphify-out comme SUPABASE_STRATEGY
- [[picard-project-pattern]] — autre producteur d'audit conteneurisé

## Note de confiance

**Confirmé par machine.** Le comptage 1208/graphify-out vient du script
d'extraction substrat (file `01_Projects_Picard.jsonl`, observable
directement). Le décompte manuel des doublons a été vérifié sur 3
paires identiques.

*Standing : correction de mesure documentée et intégrée au rapport.*

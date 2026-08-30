---
type: Ontology
title: Verbes — hors des quatre familles
description: Prédicats attestés que la taxonomie d'ONTOLOGIE_V2 §3 ne couvre pas. Leur existence dit que la taxonomie est incomplète.
tags: [ontologie, verbes, lacune, rdf]
generated: { by: scripts/extraire_verbes.py, at: 2026-08-30 }
verified:
  - { by: scripts/extraire_verbes.py, at: 2026-08-30 }
sources:
  - id: triplets
    resource: 70_Onthologies/**/*.ttl
    title: Les prédicats mesurés
    last_modified: 2026-08-30
okf_version: "0.2"
---

# Verbes hors des quatre familles

**53 prédicats** attestés dans le corpus que les familles *Autorité / Flux / Routage / Structure* ne couvrent pas.

Ce fichier n'est pas une décharge : c'est **la mesure de ce que la taxonomie ne dit pas encore**. Une ontologie qui range tout dans quatre cases sans reste ment sur sa propre couverture.

## Ce que cette liste établit

**`appliesTo` — 142 occurrences — est le prédicat le plus fréquent du corpus,
et il n'entre dans aucune des quatre familles.** Ce n'est pas un oubli de
classement : *appliquer une règle à un objet* n'est ni de l'autorité, ni du
flux, ni du routage, ni de la structure. C'est une **cinquième relation** que
`ONTOLOGIE_V2 §3` ne nomme pas.

Suivent `refines` (10), `enforces` (6), `compiles` (5) — même famille implicite :
la **portée normative**, ce à quoi une règle s'applique et jusqu'où.

**Couverture mesurée : 32 prédicats sur 85, soit 38 %.** Une taxonomie qui
couvre 38 % de ses données doit le dire plutôt que de ranger le reste sous
« divers ». La décision d'ajouter une cinquième famille appartient au
propriétaire : c'est un choix, pas un fait — comme les quatre dialectes de
`ONTOLOGIE_V2 §4`.

| Verbe | Occurrences |
|---|---:|
| `appliesTo` | 142 |
| `refines` | 10 |
| `enforces` | 6 |
| `compiles` | 5 |
| `maximizes` | 4 |
| `rejects` | 3 |
| `positioned` | 3 |
| `holds` | 3 |
| `halts` | 3 |
| `executes` | 2 |
| `commands` | 2 |
| `classifies` | 2 |
| `seeAlso` | 2 |
| `protects` | 2 |
| `distinguishedFrom` | 1 |
| `precedes` | 1 |
| `corriges` | 1 |
| `replaces` | 1 |
| `prioritizes` | 1 |
| `compresses` | 1 |
| `provides` | 1 |
| `translates` | 1 |
| `format` | 1 |
| `offers` | 1 |
| `differentiates` | 1 |
| `freezes` | 1 |
| `serves` | 1 |
| `limits` | 1 |
| `exchanges` | 1 |
| `runs` | 1 |
| `amends` | 1 |
| `coaching` | 1 |
| `adds` | 1 |
| `clarifies` | 1 |
| `challenges` | 1 |
| `actsAs` | 1 |
| `declare` | 1 |
| `forces` | 1 |
| `pre-served` | 1 |
| `survives` | 1 |
| `couvre` | 1 |
| `scales` | 1 |
| `unlocks` | 1 |
| `killed` | 1 |
| `jumeau-challenger` | 1 |
| `beats` | 1 |
| `constrains` | 1 |
| `projectsTo` | 1 |
| `cadence` | 1 |
| `denies` | 1 |
| `guarantees` | 1 |
| `calibrates` | 1 |
| `detects` | 1 |

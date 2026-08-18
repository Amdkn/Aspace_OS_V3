---
type: Bundle index
title: 60_Onthologies — A'Space OS reconstitue en sujet-verbe-objet
description: Le graphe RDF d'A'Space lui-meme, forme par des agents lisant la distillation. Trois couches, trois agents, un vocabulaire ferme.
tags: [ontologie, rdf, triplets, aspace, sujet-verbe-objet]
generated: {{ by: claude-opus-5, at: 2026-08-17T22:00:00Z }}
verified:
  - {{ by: process:graphe-distillation, at: 2026-08-17T21:55:00Z }}
sources:
  - id: distillation
    resource: 50_Distillation/ — 102 concepts OKF, 3 624 triplets sur six fichiers Turtle
    title: La distillation du PARA V2
    last_modified: 2026-08-17
  - id: rdf
    resource: https://www.w3.org/TR/rdf12-concepts/
    title: RDF 1.2 Concepts and Abstract Data Model
    last_modified: 2026-08-17
okf_version: "0.2"
---

# Ce que ce bundle contient, et ce qu'il n'est pas

Il porte la **reconstitution d'A'Space OS** : ce qu'A'Space est, qui y agit,
selon quelle regle — en triplets sujet-verbe-objet.

Il ne faut pas le confondre avec `50_Distillation/ontologie/`, qui porte le
graphe **mecanique** de la distillation : les 102 concepts comme sujets, leurs
metadonnees, leurs liens. Celui-la decrit des **documents**.

| | sujet du graphe | question a laquelle il repond |
|---|---|---|
| `50_Distillation/ontologie/` | les concepts distilles | « ou est-ce ecrit ? » |
| `60_Onthologies` | A'Space lui-meme | « qu'est-ce qui est vrai ? » |

Ici, les 102 concepts distilles deviennent des **sources**, plus des sujets.

# La forme d'une assertion

Chaque ligne est un triplet, et rien d'autre :

```
sujet          verbe          objet
rick           governs        replicator
life-os        hasVetoOver    business-os
picard         stewards       projets
```

Un triplet sans source n'entre pas dans le graphe. C'est la regle du poste, et
elle est appliquee par un validateur, pas par la bonne volonte : **une entree
sans source est une invention**.

# Trois couches, trois agents

| Agent | Couche | Entites principales |
|---|---|---|
| `tech` | Tech OS — le mecanisme | Rick, les Cores, les Docteurs, A0 |
| `life` | Life OS — la conscience | les gardiens PARA, A1/A2/A3, Beth, Morty |
| `business` | Business OS — l'action | B1/B2/B3, les Jerry, les Summer |

Chacun ecrit dans son propre fichier de triplets. Aucun ne peut ecraser un
autre, et la fusion est faite par script apres validation.

# Directories

- [_briefs](_briefs/) - Garde-fou, briefs par couche, lanceur.
- [triplets](triplets/) - Les assertions brutes, un fichier par couche.
- [sujets](sujets/) - Concepts OKF sur les entites d'A'Space.
- [verbes](verbes/) - Concepts OKF sur les predicats retenus.

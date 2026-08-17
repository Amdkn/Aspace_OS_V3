---
type: Bundle index
title: 50_Distillation — le PARA de la V2 distillé en ontologie
description: Point d'entrée de la distillation d'A'Space OS V2 vers des concepts OKF v0.2 et un graphe RDF. Deux temps — extraction scriptée exhaustive, puis distillation sémantique déléguée.
tags: [distillation, okf, rdf, ontologie, para, aspace-v2]
generated: { by: claude-opus-5, at: 2026-08-17T20:00:00Z }
verified:
  - { by: process:inventaire-para-v2, at: 2026-08-17T19:50:00Z }
sources:
  - id: inventaire
    resource: "scripts/inventaire_para_v2.py sur ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise — comptage sans suivre les jonctions NTFS"
    author: process:inventaire-para-v2
    last_modified: 2026-08-17
  - id: corpus
    resource: "_mesures/corpus_md.json — décompte des .md hors node_modules, .git, dist"
    author: process:inventaire-para-v2
    last_modified: 2026-08-17
  - id: rdf-concepts
    resource: https://www.w3.org/TR/rdf12-concepts/
    title: RDF 1.2 Concepts and Abstract Data Model (W3C)
    last_modified: 2026-08-17
okf_version: "0.2"
---

# Ce que ce bundle distille

Le PARA d'entreprise de la V2 —
`ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/` — vers des **concepts OKF v0.2**
organisés en OpenWiki, et vers un **graphe RDF** de l'ontologie d'A'Space OS.

Les quatre seaux, et leur gardien :

| Seau | Gardien | Ce qu'il porte |
|---|---|---|
| `01_Projects_Picard` | Picard | les projets à échéance |
| `02_Areas_Spock` | Spock | les domaines permanents |
| `03_Resources_Geordi` | Geordi | la base de connaissance |
| `04_Archives_Data` | Data | ce qui est clos mais conservé |

# La mesure qui commande tout

| | fichiers | dont `.md` utiles |
|---|---|---|
| `01_Projects_Picard` | 248 923 | **2 154** |
| `02_Areas_Spock` | 10 340 | **444** |
| `03_Resources_Geordi` | 446 152 | **48 378** |
| `04_Archives_Data` | 20 187 | **12 284** |
| **total** | **725 607** | **63 260** |

Sur 725 607 fichiers, environ 519 000 sont du `.js`, `.map`, `.ts` et `.mjs` —
des dépendances installées, pas de la connaissance. **Le corpus qui se distille,
ce sont les 63 260 `.md`**, soit 336 Mo.

**176 jonctions NTFS ont été écartées** pendant le comptage. Les suivre aurait
produit un total absurde : le canon rapporte un `os.walk` naïf qui a compté
13,8 millions de fichiers là où il y en avait 14 613.

# La méthode, en deux temps

**Aucun agent ne peut lire 63 260 fichiers.** À vingt fichiers par appel, c'est
trois mille appels, et la qualité s'effondre bien avant le quota. Prétendre le
contraire produirait un échantillon déguisé en exhaustivité.

1. **Extraction scriptée — 100 % du corpus, sans LLM.** Frontmatter, titres,
   liens, tags de chaque `.md`. C'est la matière première des triplets : le
   frontmatter donne les propriétés, les titres la hiérarchie, les liens les
   relations. Elle ne comprend rien, et c'est pourquoi elle peut tout lire.
2. **Distillation sémantique — déléguée, sur l'extraction.** Les agents
   travaillent sur l'index produit et ne lisent en profondeur que les zones
   qu'il désigne. Ce qu'ils rendent est un concept OKF v0.2, pas un résumé.

Le détail : [MÉTHODE](METHODE.md).

# Files

- [MÉTHODE](METHODE.md) - Les deux temps, ce que chacun peut et ne peut pas, et la règle qui interdit de faire passer un échantillon pour un inventaire.

# Directories

- [_mesures](_mesures/) - Les comptages bruts, avec leur date et leur portée.
- [_substrat](_substrat/) - L'extraction exhaustive, un JSONL par seau.
- [_briefs](_briefs/) - Garde-fou et briefs de délégation, un périmètre exclusif par agent.
- [ontologie](ontologie/) - Types, relations et sérialisation RDF.
- [projets](projets/) - Concepts distillés de `01_Projects_Picard`.
- [areas](areas/) - Concepts distillés de `02_Areas_Spock`.
- [ressources](ressources/) - Concepts distillés de `03_Resources_Geordi`.
- [archives](archives/) - Concepts distillés de `04_Archives_Data`.

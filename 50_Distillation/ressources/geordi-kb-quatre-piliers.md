---
type: Backend
title: Geordi KB — quatre piliers OKF/Wiki/Graphify/Dox
description: L'architecture canonique de la racine KB Geordi : quatre piliers distincts et complémentaires qui répondent à quatre classes de questions, plus un index utilitaire. La connaissance d'une question → le bon pilier.
tags: [kb, geordi, pilier, routage, okf, wiki, graphify, dox]
generated: { by: minimax-m3, at: 2026-08-17T20:35:00Z }
verified:
  - { by: process:lecture-fichiers, at: 2026-08-17T20:35:00Z }
sources:
  - id: index-of-indexes
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/00_Index/INDEX_OF_INDEXES.md"
    title: "Index des Index — Routage OKF / Wiki / Graphify / Dox + RESOURCES_INDEX"
    last_modified: 2026-08-01
  - id: geordi-kb-root
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/00_Index/GEORDI_KB_ROOT.md"
    title: "Geordi — Racine de la Knowledge Base (Second Brain PARA)"
    last_modified: 2026-08-01
  - id: okf-index
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/00_Index/OKF_INDEX.md"
    title: "OKF — Index du pilier Standard"
    last_modified: 2026-08-01
okf_version: "0.2"
---

# Geordi KB — quatre piliers OKF/Wiki/Graphify/Dox

> **Décision datée du 2026-08-01** : OKF a été oublié dans la première passe du bootstrap KB
> (la racine ne listait que Wiki/Graphify/Dox). C'est en fait le 4ᵉ pilier, et **le standard de
> format** qui définit ce qu'est un bundle mémoire valide.

## 1. Les quatre piliers

| Pilier | Question type | Format | Volume mesuré | Outil de refresh |
|---|---|---|---:|---|
| **🏷️ OKF** | « Qu'est-ce qu'un bundle valide ? Quels champs sont requis ? » | Standard de format | 1 spec canonique | bumpée par décision A0 — v0.1 figée 2026-07-02 |
| **📖 WIKI** | « Qu'est-ce que c'est ? Quel est le concept canon ? » | Bundle OKF | 1 773 pages / 319 liens dans index.md | `06_Claude_Code_Bare/bin/gen_wiki_index.py` |
| **🕸️ GRAPHIFY** | « Quels sont les liens ? Comment c'est connecté ? » | JSON graphe | 4 065 164 octets / GRAPH_REPORT.json | non mesuré localement (P3) |
| **📜 DOX** | « Quel est le contrat ? Comment doit-on se comporter ? » | Markdown append-only | 06_CC_Bare/CLAUDE.md + AGENTS.md + racine | append-only |

## 2. Algorithme de routage (cinq branches + 1 utilitaire)

```
Question sur A'Space OS V2 ?
   │
   ├─ Format / standard / conformité ?  → 🏷️ OKF      (00_Index/OKF_INDEX.md)
   ├─ Concept / définition / canon ?    → 📖 WIKI     (wiki/index.md)
   ├─ Liens / structure / graphe ?      → 🕸️ GRAPHIFY (graphify-out/graph.json)
   ├─ Loi / contrat / comportement ?   → 📜 DOX      (CLAUDE.md racine + CC_Bare/CLAUDE.md)
   ├─ Où est le fichier X ?             → 📚 INDEX    (RESOURCES_INDEX.md + TAGS.md)
   └─ Strate / rot / péremption ?        → 🕐 ROT      (wiki/ROT.md)
```

## 3. Relations entre piliers

- **OKF définit le format.** Le wiki EST un bundle OKF.
- **Wiki contient le contenu canon.**
- **Graphify consomme** des bundles OKF pour produire la structure topologique.
- **Dox consomme** des bundles OKF pour la navigation FS (index micro).
- **RESOURCES_INDEX** est l'index utilitaire tabulaire (où est quoi), pas un pilier.

## 4. Hiérarchie des sources (résolution de conflit)

Pour trancher un conflit entre deux sources, la hiérarchie canonique (CLAUDE.md racine §7) :

1. `05_From_V2_Domains/00_Amadeus/01_Identity_Core/CONSTITUTION.md` (Constitution — bloquant)
2. `06_Claude_Code_Bare/CLAUDE.md` (Dox canon long)
3. `00_Index/GEORDI_KB_ROOT.md` (manifeste racine KB)
4. `00_Index/PLAN_META_MEMOIRE_2026-08-01.md` (plan adapté)
5. `06_Claude_Code_Bare/plans/plan-meta-memoire-okf-wiki-graphify-dox.md` (plan maître)
6. `A3_Geordi_Resources_Spec.md` (spec de rôle Geordi)
7. `00_Index/TAGS.md` §v2 (registres Owner + Strate)
8. `03_Memory_Unified/LLM_Wiki/wiki/ROT.md`
9. `00_Index/INDEX_OF_INDEXES.md`
10. `00_Index/SECOND_BRAIN_PARA_MAP.md`
11. `00_Index/RESOURCES_INDEX.md`
12. `00_Index/WIKI_LINT_BRIEF.md`

## 5. Patch 2026-08-01

L'algorithme de routage comportait initialement une version à 3 piliers (Wiki/Graphify/Dox),
corrigée le 2026-08-01 par adjonction d'OKF en première branche. Voir
`OKF_INDEX.md` (passage de la racine vers `00_Index/OKF_INDEX.md`) pour le changelog complet.

## Liens entrants

- `okf-v0-1-format-standard.md` — la substance du pilier OKF
- `wiki-schema-llm-wiki.md` — la substance du pilier Wiki
- `wiki-routing-by-question.md` — le détail de l'algorithme de routage
- `second-brain-14-sous-dossiers.md` — où logent physiquement les 4 piliers

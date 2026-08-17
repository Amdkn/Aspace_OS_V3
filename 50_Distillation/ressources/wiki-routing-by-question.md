---
type: Backend
title: Wiki routing par question — 6 branches canoniques
description: Algorithme canonique de routage d'une question sur A'Space OS V2 vers le bon pilier KB (OKF/Wiki/Graphify/Dox/Index/ROT). Six branches testées et patchées (OKF ajouté 2026-08-01 en première).
tags: [routing, kb, algorithm, okf, wiki, graphify, dox, index, rot]
generated: { by: minimax-m3, at: 2026-08-17T21:29:00Z }
verified:
  - { by: process:lecture-fichiers, at: 2026-08-17T21:29:00Z }
sources:
  - id: claude-md-root
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/CLAUDE.md"
    title: "CLAUDE.md — Racine Geordi (Dox d'entrée KB)"
    last_modified: 2026-08-01
  - id: index-of-indexes
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/00_Index/INDEX_OF_INDEXES.md"
    title: "Index des Index — Routage OKF / Wiki / Graphify / Dox + RESOURCES_INDEX"
    last_modified: 2026-08-01
  - id: okf-index
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/00_Index/OKF_INDEX.md"
    title: "OKF — Index du pilier Standard"
    last_modified: 2026-08-01
okf_version: "0.2"
---

# Wiki routing par question — 6 branches canoniques

> Algorithme canonique pour router une question d'un agent A0 sur A'Space OS V2 vers
> le bon pilier KB. Patch daté du 2026-08-01 : la version initiale citait 3 piliers
> (Wiki/Graphify/Dox), corrigée pour inclure OKF comme **4ᵉ** pilier.

## 1. L'algorithme

```
Question sur A'Space OS V2 ?
   │
   ├─ Format / standard / conformité ?    → 🏷️ OKF
   │     (00_Index/OKF_INDEX.md + plan maître §2.1 ligne 40)
   │
   ├─ Concept / définition / canon ?      → 📖 WIKI
   │     (03_Memory_Unified/LLM_Wiki/wiki/index.md, 319 liens)
   │
   ├─ Liens / structure / topologie ?     → 🕸️ GRAPHIFY
   │     (graphify-out/GRAPH_REPORT.json + graph.json)
   │
   ├─ Loi / contrat / comportement ?     → 📜 DOX
   │     (CLAUDE.md racine + 06_CC_Bare/CLAUDE.md + AGENTS.md)
   │
   ├─ Où est le fichier X ?               → 📚 INDEX
   │     (RESOURCES_INDEX.md + TAGS.md)
   │
   └─ Strate / rot / péremption ?          → 🕐 ROT
         (03_Memory_Unified/LLM_Wiki/wiki/ROT.md)
```

## 2. Patch 2026-08-01 — pourquoi OKF est revenu en première branche

L'algorithme originel listait 3 piliers (Wiki/Graphify/Dox), publiés dans
`GEORDI_KB_ROOT.md` §4 et `INDEX_OF_INDEXES.md` §1.

Bug : OKF était réduit à un simple champ `okf_version` dans le frontmatter, alors
qu'OKF est **le standard de format** qui définit ce qu'est un bundle mémoire valide.
C'est le **4ᵉ pilier** au même titre que les trois autres, et il devait figurer
en première branche (la question la plus fondamentale : « mon doc est-il conforme ? »).

La correction est détaillée dans `OKF_INDEX.md` §1.

## 3. Volumes par branche

| Branche | Fichier pilier | Volume |
|---|---|---|
| **OKF** | `OKF_INDEX.md` + plan maître §2.1 | 1 spec canonique |
| **WIKI** | `wiki/index.md` | 1 773 pages · 319 liens |
| **GRAPHIFY** | `graph.json` (4 MB) + `GRAPH_REPORT.json` + `chunks/` | non mesuré localement |
| **DOX** | `CLAUDE.md` racine + `06_CC_Bare/CLAUDE.md` (8.7K tokens) + `AGENTS.md` | append-only |
| **INDEX** | `RESOURCES_INDEX.md` (porte d'entrée quasi-vide) | 5 lignes exemples |
| **ROT** | `wiki/ROT.md` (5 strates) | rot-rates S0→S4 |

## 4. Ce que le routage n'est PAS

- ❌ Pas une heuristique : c'est un arbre déterministe basé sur la classe de question.
- ❌ Pas un walk de graphe : il n'épluche pas Graphify pour décider.
- ❌ Pas un outil : c'est un algorithme mémorisable que l'agent A0 applique avant chaque
  lecture lourde.

## 5. Qui appelle cet algorithme

Trois contextes d'appel canoniques (cf. `CLAUDE.md` racine §4) :

1. **Boot session** : Geordi_boot lit GEORDI_KB_ROOT.md, PLAN, etc.
2. **Question entrante** : agent A0 décide quel(s) pilier(s) consulter.
3. **Synthèse cross-pilier** : agent recombinant (rare, car cela suppose une maîtrise déjà
   installée des 5 branches).

## 6. Tension Constitution v1.0

L'article 6 interdit les gates bloquants. Le routage n'est pas un gate (il choisit le
pilier, il n'arrête pas l'action) — il survit sans tension à la Constitution.

L'article 5 rétrograde les ADRs en jurisprudence mais l'algorithme de routage est un
**invariant** de la KB, pas une décision juridique. Il survit comme **doctrine**.

## Liens entrants

- `geordi-kb-quatre-piliers.md` — où loge l'algorithme parmi les 4 piliers
- `okf-v0-1-format-standard.md` — le pilier OKF
- `wiki-schema-llm-wiki.md` — le pilier Wiki

---
type: Concept
title: Memory Architect Kit — les 7 couches de mémoire canoniques + multi-signal retrieval
description: Kit de 2 fichiers (SKILL.md + PDF Diagram Guide) qui pose un modèle en 7 couches pour la mémoire d'un agent : Identity, Critical Context, Working Memory, Long-term Knowledge, Episodic Memory, Decay, Promotion.
tags: [templates, memory-architect, 7-layers, identity, critical-context, decay, promotion, datation]
generated: { by: minimax-m3, at: 2026-08-19T20:00:00Z }
verified:
  - { by: process:lecture_memory_architect_integral_avec_pdf, at: 2026-08-19T20:00:00Z }
sources:
  - id: memory-architect-skill
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/02_Templates/Memory Architect Kit/SKILL.md"
    title: "Memory Architect — SKILL.md (interview 4 rounds + 6 design decisions)"
    last_modified: 2026-05
  - id: memory-architect-pdf
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/02_Templates/Memory Architect Kit/Concept Walkthroughs.pdf"
    title: "Memory Architect — Diagram Guide (16 diagrams)"
    last_modified: 2026-05
okf_version: "0.2"
---

# Memory Architect Kit — 7 couches canoniques

## Périmètre

**2 fichiers seulement** :
- `SKILL.md` (~1050 lignes) — la méthode d'interview : Round 0 (speed) → Round 1 (qui es-tu) → Round 2 (quelles couches) → Round 3 (6 design decisions) → Round 4 (infra preference) → Phase 2 (recipe) → Phase 3 (dependency check) → Phase 4 (build plan) → Phase 5 (build) → Phase 6 (how it all works).
- `Concept Walkthroughs.pdf` (19 pages) — 16 diagrammes visuels ASCII des couches, concepts, et patterns.

Le brief Templates annonçait « 1 fichier » pour ce kit — sous-évaluation : c'est 2 fichiers complémentaires, pas 1 embryon ni 1 index.

## Verdict global

**`synthese-datee`** — daté sur les noms précis (MemPalace, kioku, etc.), canon sur les 7 couches et les patterns de retrieval.

## Les 7 couches (synthèse canonique)

| Couche | Charge | Chargement | Persistance | Analogie |
|---|---|---|---|---|
| **Identity** | ~100 tokens | toujours | permanente | name badge |
| **Critical Context** | ~300 tokens | toujours + ré-injecté après compaction | jusqu'au prochain update | sticky note |
| **Working Memory** | ~1-2K tokens | session | compresse en fin de session | messy desk |
| **Long-term Knowledge** | unlimited | searched, jamais bulk-loaded | indéfinie | filing cabinet |
| **Episodic Memory** | very large | archived, rarement accédée | indéfinie | journal |
| **Decay** | background process | auto | — | forgetting curve |
| **Promotion** | background process | auto (3-strike rule) | — | intern → manager |

Insight clé : « Most people need at least: Identity + Critical Context + Long-term Knowledge. The rest are optional. » → **le minimum viable est 3 couches.**

## Les 6 design decisions

Le kit impose une matrice de décisions pour configurer la mémoire :

1. **Capture** : auto (sécurité) / manual (journal) / smart filter (spam filter).
2. **Format** : Obsidian (recommandé, « two doors ») / markdown plat / database.
3. **Structure** : flat / 5-type taxonomy (facts, events, discoveries, preferences, advice — 34 % retrieval gain) / knowledge graph / spatial hierarchy (95 % recall au deepest).
4. **Retrieval** : keyword / semantic / multi-signal hybrid (70 % fewer tokens, 7K vs 25K brute force).
5. **Injection** : load all (backpack) / progressive (library card, ~400 tokens always, 10x savings) / project-aware.
6. **Lifecycle** : keep everything (archive, 96.6 % recall) / decay (brain, recent detailed, old compress) / promote (best → rule, decay the rest).

## Multi-signal retrieval (le pattern canonique)

Le diagramme « Multi-Signal Retrieval » (page 9 du PDF) montre 3 signaux combinés via **rank fusion** :

- **Semantic** (cosine similarity, top 5, threshold 0.3)
- **Keyword** (FTS5, top 5)
- **Entity** (entity linking, people/places)
- **Rank fusion** : ~7 000 tokens vs 25 000 pour brute force → 70 % fewer tokens, même accuracy.

Ce pattern est canonique et se retrouve dans plusieurs kits :
- ClaudeClaw Mission Control Kit, Pack 06 Three-Layer Memory.
- ClaudeClaw OS Blueprint Kit V2, Memory v2 (768-dim embeddings).
- The Perfect Agentic OS Kit, recipes qui agrègent Pantry → Prep → Plate.

## Daté sur

- Les noms précis des projets tiers cités (MemPalace, Beads, memsearch, claude-mem, obsidian-mind, kioku, engram, episodic-memory, memory-bank, claude-memory-compiler, CPR, memcp, cc-soul, a-mem-mcp, claudesidian, second-brain, Nemp, agentmemory, kioku-lite, supermemory) — ce sont des projets V0 dont la plupart ont changé.
- L'obsession pour la **5-type taxonomy** — A'Space V3 utilise d'autres structures (cf. `40_Memory_Wiki_OKF/`).
- La citation « Native Claude Code memory will keep improving. Any system you build needs to be designed for change. » → daté sur la maturité native de Claude Code memory.

## Trace dans V3

**Aucune directe.** Pas de référence à « Memory Architect » dans `ASpace_OS_V3/`. Mais le **modèle 7 couches** est **conceptuellement canonique** : A'Space V3 utilise déjà Identity (rôles A0/A1/A2) + Critical Context (CLAUDE.md par projet) + Long-term Knowledge (`40_Memory_Wiki_OKF/`) + Episodic Memory (sessions). Le **5-layer memory v2** de ClaudeClaw (gemini-embedding-001 + importance + salience + supersession + relevance feedback) est l'**implémentation Tier 3** de ce modèle.

## Concepts liés

- [[concept-five-cross-cutting-patterns]] — three-layer memory est l'un des patterns transversaux
- [[concept-claudeclaw-mission-control-kit]] — Pack 06 implémente le Tier 3 du modèle

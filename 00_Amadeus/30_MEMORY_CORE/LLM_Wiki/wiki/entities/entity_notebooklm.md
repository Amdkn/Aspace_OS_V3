---
source: LLM_Wiki_A0
date: 2026-05-11
type: entity
domain: L1_Life_OS / Fleet / Knowledge_RAG
tags: [#entity #NotebookLM #RAG #Knowledge_Base #AI_First #A0_Memory #Context_Retention]
---

# Entity: NotebookLM (Google's AI Research Assistant)

> notebooklm.google.com | RAG-powered knowledge base | Used by A0 for context retention

NotebookLM est l'outil **RAG (Retrieval-Augmented Generation)** pour A0 Amadeus. Il permet de conserver le contexte des conversations Gemini et de l'interroger plus tard.

---

## Usage dans A'Space OS

### Pour A0 Amadeus

A0 utilise NotebookLM pour:
1. **Conserver l'historique** des sessions Gemini (1,881 conversations en Mai 2026)
2. **Interroger le passé** — "qu'est-ce qu'on a décidé sur Solaris en Mars?"
3. **Générer des podcasts** — NotebookLM peut créer un "audio digest" des conversations
4. **Contextualiser** — fournir du contexte à Gemini CLI pour les nouvelles sessions

### Limites

> "Je veux lancer le Google Takeout pour récupérer nos echanges pour les RAG et NotebookLM."

L'aveu ici: NotebookLM seul ne suffit pas — il faut d'abord extraire les échanges du Takeout (ce qui a nécessité le parser v2).

---

## Pourquoi NotebookLM vs. Autres

| Criteria | NotebookLM | Obsidian | Notion |
|---------|-----------|---------|--------|
| RAG | ✅ Native | ⚠️ Plugin | ❌ |
| Audio summary | ✅ (podcast) | ❌ | ❌ |
| PDF import | ✅ | ✅ | ✅ |
| A'Space OS integration | ✅ (via Takeout) | ✅ (via vault) | ❌ |
| API access | Limited | ✅ (local) | ⚠️ |

---

## Dans le LLM Wiki

Le LLM Wiki (`30_MEMORY_CORE/LLM_Wiki/`) est une alternative à NotebookLM:
- **NotebookLM**: conversation-based, good for audio summaries
- **LLM Wiki**: structured, good for cross-referencing, owned by A0

**Usage recommandé:**
- NotebookLM → conversations brutes, audio digests
- LLM Wiki → entités structurées, concepts cross-domain, synthèses

---

## Stats

- **Mentions dans 2026-03**: 41
- **Mentions dans 2026-05**: 227
- **Domain**: L1 Life OS / RAG Knowledge Base
- **Source**: [[sources/source_gemini-takeout-2026-03]] | [[sources/source_gemini-takeout-2026-05]]

---



---

## Inbounds

- [[entity_notebooklm]]
*Last updated: 2026-05-11*
*Source: [[sources/source_gemini-takeout-2026-03]] | [[sources/source_gemini-takeout-2026-05]]*
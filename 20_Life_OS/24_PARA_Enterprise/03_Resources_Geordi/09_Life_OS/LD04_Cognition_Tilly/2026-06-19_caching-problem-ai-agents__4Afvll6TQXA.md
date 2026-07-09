---
title: "The Caching Problem Nobody Talks About with AI Agents"
date: 2026-06-19
source: youtube-takeout-to-lifeos + /youtube-to-para batch 2026-06-19
video_id: 4Afvll6TQXA
channel: ByteMonk
url: https://www.youtube.com/watch?v=4Afvll6TQXA
duration: 454s
ld: LD04_Cognition_Tilly
ld_owner: Tilly
status: DISTILLED_L1
---

# Caching Problem AI Agents (ByteMonk)

> **Intention** : adopter le **3-tier cache** (model/tool/session) pour réduire le coût tokens des agents A0 de **~75%**.

## 🎯 5 points clés

1. **Agent Cache (BetterDB)** : caching **3 layers** = model responses + tool results + session memory (pas juste model comme les autres).
2. **2 cache types** : exact (cache key) + similar (semantic via embeddings, threshold configurable).
3. **Valkey vs Redis** : Valkey a **vector search dans le base engine**, Redis a besoin d'un module séparé.
4. **75% hit rate réaliste** = 3/4 calls stop paying for.
5. **MCV server** : cache tune itself via coding agent (Cursor/Cloud Code) lit recommendations + applique changements.

## 📊 D11 Fable Metrics

| Métrique | Valeur |
|---|---|
| Cache layers | 3 (model/tool/session) |
| Hit rate (realistic) | 75% |
| Cross-refs Geordi | LD04 Cognition (AI efficiency) + Hermes runtime (target) |
| Actionnables A0 | 1 (ratify ADR-LD04-010 Agent Cache Doctrine) |
| D11 Fable score | TBD (run manuel 2026-06-19) |

## 🔗 Référence externe

- **ByteMonk BetterDB Agent Cache** : github.com/byte-monk/betterdb (D1 verify)
- **Valkey project** : valkey.io (D1 verify)
- **chat.betterdb.com** : chatbot public hit rate live (D1 verify)
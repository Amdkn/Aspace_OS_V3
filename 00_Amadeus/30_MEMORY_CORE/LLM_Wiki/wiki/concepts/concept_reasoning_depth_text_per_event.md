---
source: Claude Code A2 (fable-distill-aspace.py) on 2026-06-15
date: 2026-06-15
type: concept
domain: L0 Tech_OS / Fable Mindset / Reasoning
tags: [#reasoning-depth #fable #d11-metric #text-density]
---

# Reasoning Depth (Avg Text per Event)

## D1 Receipts

| Modèle | Avg text/event (chars) | Total events |
|--------|----------------------:|-------------:|
| **MiniMax-M2.7** | 54.0 | 4559 |
| MiniMax-M3 | 91.0 | 89 |
| claude-opus-4-8 | 164.0 | 2753 |
| claude-opus-4-7 | 177.0 | 2726 |
| claude-sonnet-4-6 | 122.0 | 88 |

## Definition

`avg_text_per_event` = chars total de blocs text / nombre d'events assistant.

Plus c'est élevé = plus le modèle "réfléchit" avant d'agir. Fable mindset = high reasoning depth.

## Doctrine ancrage

- **D11 Fable metric** : behavioral delta mesuré, pas prose.
- **Mark Kashet Tilly 05 l.23** : Fable = "PhD-level scientist living in your editor".

## A'Space Application

Tilly cible : >2000 chars/event = Fable discipline (depth over speed).

---
source: Claude Code A2 (fable-distill-aspace.py) on 2026-06-15
date: 2026-06-15
type: concept
domain: L0 Tech_OS / Fable Mindset / Tool Use
tags: [#tool-diversity #fable #d9.6 #discover-capabilities]
---

# Tool Call Diversity (Fable Behavioral Signature)

## D1 Receipts

Distribution des tool calls par modèle (depuis 30 sessions JSONL A'Space) :

| Modèle | Read | Edit | Write | Bash | TodoWrite | Grep | Glob |
|--------|-----:|-----:|------:|-----:|----------:|-----:|-----:|
| **MiniMax-M2.7** | 307 | 249 | 142 | 1076 | 4 | 27 | 106 |
| MiniMax-M3 | 8 | 4 | 0 | 14 | 0 | 0 | 0 |
| claude-opus-4-8 | 164 | 372 | 161 | 514 | 0 | 9 | 16 |

## Doctrine ancrage

- **D9.6 META-002** : "Discover capabilities before committing" — utiliser le bon outil pour la bonne tâche.
- **Fable discipline** : ne pas faire Edit sans Read préalable. Ne pas faire Bash sans plan.

## A'Space Application

Ratio Read:Edit optimal = 2:1 (Fable-like). Si Edit > Read, D6 root cause = on patch à l'aveugle.

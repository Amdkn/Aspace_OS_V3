---
type: Concept
title: Pyramide Déterministe à 7 Niveaux, Hooks, Webhooks et Meta-Routeur DOX
description: Architecture de résilience systémique d'A'Space OS V3 inspirée des travaux de Mark Kashef, intégrant la hiérarchie 3D-7D, les Hooks de runtime, les Webhooks d'aiguillage et la décentralisation DOX des sous-AGENTS.md.
tags: [architecture, kashef, hooks, webhooks, dox, agents-md, 7-layers, antigravity]
generated: { by: antigravity, at: 2026-09-08T05:00:00Z }
verified:
  - { by: human:amdkn, at: 2026-09-08T05:00:00Z }
sources:
  - id: kashef-agentic-patterns
    resource: "Mark Kashef — Deterministic Plumbing, Hooks & Silver Platter Patterns (YouTube YjkteijEyzQ, -WCNwxz3uoM, 7aQbN543Mec)"
    author: Mark Kashef
    last_modified: 2026-09-08
  - id: aspace-v3-canon
    resource: "A'Space OS V3 Canon & Architecture Souveraine (c:\\Users\\amado\\ASpace_OS_V3\\AGENTS.md)"
    author: human:amdkn
    last_modified: 2026-09-08
okf_version: "0.2"
---

# Pyramide Déterministe à 7 Niveaux, Hooks, Webhooks et Meta-Routeur DOX

## 1. La Pyramide à 7 Niveaux de Kashef adaptée à V3

```
      ▲
     / \     [7D] HIVEMIND & WAR ROOM : 13e Docteur / Arbitrage transversal Amadou Kone
    /---\
   / 6D  \   [6D] IDENTITÉS & SOUL FILES : CLAUDE.md / GEMINI.md / Soul.md (Air Traffic Control)
  /-------\
 /   5D    \ [5D] HOOKS & VALIDATION GATES : Coupe-circuit déterministe, Veto, Gates SSSF
/-----------\
|    4D     | [4D] CRONS & HEARTBEATS : Télémétrie 60s Yas, Tâche hebdo Distillation 50_
|-----------|
|    3D     | [3D] SKILLS & SERVEURS MCP : Ryan ADW, Tool Calling, Antigravity SDK
|-----------|
| SUBSTRAT  | [MACRO] WEBHOOKS & BROKERS : Event Log append-only uc.db (Zero Kafka lourd)
|-----------|
|  PANTRY   | [MICRO] SILVER PLATTER & MÉMOIRE : SQLite WAL, Semantica RDF Graham, OKF 0.2
└───────────┘
```

## 2. Distinction Fondamentale : Hooks vs Webhooks

1. **Webhooks (Niveau Substrat / Macro Réseau) :**
   - Rôle : Ingestion asynchrone des flux d'événements externes ou inter-systèmes (alertes de l'Observatoire Yas, triggers n8n River, webhook Git).
   - Emplacement : `10_Tech_OS/kernel/webhooks/` (ex: `yas_alert_sink.py`).
   - Principe : Ne bloque pas le runtime de l'agent. Achemine l'impulsion vers la DLQ de `uc.db`.

2. **Hooks (Niveau 5D / Micro Runtime) :**
   - Rôle : Coupe-circuit 100% déterministe dans le cycle de vie d'exécution de l'agent (Pre-Tool, Post-Build).
   - Emplacement : `10_Tech_OS/kernel/hooks/`.
   - Composants :
     - `pre_tool_guard.py` : Bloque les fuites de secrets (DLP/PII) et le "Rot Rate" de contexte obsolète (> 7 jours).
     - `silver_platter.py` : Sert un sous-contexte pré-mâché pour préserver 80% des tokens.
     - `post_build_validator.py` : Interdit tout commit si `tsc --noEmit` != 0 ou si des placeholders vides sont détectés.

## 3. Décentralisation DOX & Meta-Routeur `AGENTS.md`

Pour décharger le point d'entrée central du War Room et supprimer l'inspection répétitive de dizaines de fichiers :
- Le fichier racine [`AGENTS.md`](file:///c:/Users/amado/ASpace_OS_V3/AGENTS.md) devient le **Meta-Routeur DOX**.
- Chaque sous-dossier maître possède désormais son propre `AGENTS.md` local souverain :
  - `50_Distillation/AGENTS.md` : Le Gate inviolable d'entrée.
  - `70_Onthologies/AGENTS.md` : La vérité formelle RDF de Graham.
  - `40_Memory_Wiki_OKF/AGENTS.md` : La mémoire vivante OKF 0.2.
  - `90-self-evolution/AGENTS.md` : L'immunité adaptative anti-rejeu P1-P6.
  - `60_Implementation_Méthodologiques/AGENTS.md` : Le cadre et SOPs de fabrication.
  - `10_Tech_OS/AGENTS.md` : Plomberie, Kernel, Ryan et Yas.

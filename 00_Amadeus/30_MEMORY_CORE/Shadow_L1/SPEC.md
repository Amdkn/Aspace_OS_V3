---
source: Shadow_L1
date: 2026-05-19
type: spec
status: DRAFT_ACTIVE
domain: Shadow_L1 / Life_OS / Heartbeat
inherits: ../Shadow_L0/SPEC.md
tags: [#Spec, #ShadowL1, #LifeOS, #ClaudeCode, #MiniMax]
---

# Shadow L1 — SPEC

## 1. Purpose

Shadow L1 est la couche de **pouls Life OS** : une mesh éphémère orchestrée par
Claude Code CLI on MiniMax Token Plan, qui surveille Baserow Life OS, Plane,
Obsidian vault 20_Life_OS/, et signale les anomalies de vigilance à A0.

## 2. Non-Goals

- ❌ NE PAS prendre de décisions Life OS (Rocks, tactiques, priorités) à la place de A0
- ❌ NE PAS écrire dans Baserow/Plane/Obsidian sans signoff
- ❌ NE PAS générer de rapports auto-narrés (A0 fait les rapports, L1 prépare les checklists)
- ❌ NE PAS surveiller L2 / Business (couche distincte, mission card obligatoire pour cross-layer)

## 3. Architecture (file-based, héritée Shadow_L0)

```
Shadow_L1/
├── HEARTBEAT_PROTOCOL.md     (doctrine L1)
├── SPEC.md                   (ce fichier)
├── WORKFLOW.md               (mission lifecycle L1)
├── HEARTBEAT.md              (tasks: block)
├── README.md                 (index existant)
├── A0_inbox/                 (anomaly digests pour A0)
├── handoffs/                 (existant, instructions reprise)
└── agents/
    └── Claude_Code_CLI/
        ├── Heartbeat.md      (capsule personnalisée)
        ├── Agent.md          (identité Claude Code L1)
        ├── Tools.md          (surface capability)
        ├── Context.md        (turn pointer)
        └── memory/
            ├── inbox/        (mission cards entrantes)
            ├── outbox/       (run outputs par mission)
            ├── rejections.log
            ├── minimax-quirks.md
            └── pulse.log
```

## 4. Tick Cycle (héritage Shadow_L0 §4)

Identique à Shadow_L0 sauf surfaces PROBE et catalogue DECIDE (cf. HEARTBEAT_PROTOCOL.md §6, §7).

## 5. Routing & Fallback

Default : `Claude_Code_CLI` on MiniMax.
Fallback (per protocol §9) : `Gemini_CLI` (long context fit), puis Codex en dernier recours.

## 6. Acceptance Criteria (pour activation production)

- [ ] AC-L1-01 : `heartbeat-tick-l1.ps1` exécute un tick à blanc sans tokens consommés si `phase_enabled: false`
- [ ] AC-L1-02 : Tick supervisé manuel produit `pulse.log` entry + `outbox/` rendu propre
- [ ] AC-L1-03 : Tick détecte volontairement une anomalie L1-A01 dans dataset de test et écrit dans `A0_inbox/`
- [ ] AC-L1-04 : Fallback MiniMax→Gemini fonctionne (test : env var invalide → routing log `HEARTBEAT_ROUTE`)
- [ ] AC-L1-05 : Tick respecte `active_hours: 07:00-22:00` (test : run à 02:00 → `HEARTBEAT_SKIP_HOURS`)
- [ ] AC-L1-06 : Aucune écriture Baserow/Plane sans mission card autorisée par A0 dans `memory/inbox/`

## 7. Dependencies

| Composant | Statut |
|---|---|
| Claude Code CLI installé | ✅ |
| MiniMax Token Plan key (env `MINIMAX_API_KEY`) | ✅ |
| `ANTHROPIC_BASE_URL=https://api.minimax.io/anthropic` | ✅ (per concept_god_mode_cli_stack) |
| `BASEROW_API_TOKEN` (User scope) | ✅ partial (read-only) |
| `PLANE_API_TOKEN` | ❌ blocked 403 |
| `heartbeat-tick-l1.ps1` | ⏳ to be scaffolded |
| Windows Task Scheduler entry `ASpace-Heartbeat-L1` | ⏳ disabled |

## 8. Cross-refs

- `./HEARTBEAT_PROTOCOL.md`
- `./WORKFLOW.md`
- `../Shadow_L0/SPEC.md`
- `LLM_Wiki/wiki/concepts/concept_shadow_l1_l2_heartbeat_symphony.md`

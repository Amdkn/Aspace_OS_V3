---
source: Shadow_L2
date: 2026-05-19
type: spec
status: DRAFT_ACTIVE
domain: Shadow_L2 / Business_Pulse / Heartbeat
inherits: ../Shadow_L0/SPEC.md
tags: [#Spec, #ShadowL2, #BusinessPulse, #ClaudeCode, #MiniMax, #Production]
---

# Shadow L2 — SPEC

## 1. Purpose

Mesh éphémère 5min/24/7 orchestrée par Claude Code CLI on MiniMax Token Plan,
surveillant les surfaces business : production apps, Airtable/ClickUp pipelines,
Vercel/Hostinger/Supabase infra, MiniMax cost burn.

Émet anomaly digests + alerts H1 vers `A0_inbox/` et mission cards vers les
inbox des 8 Squads Business (`30_Business_OS/0X_<Squad>/inbox/`).

## 2. Non-Goals

- ❌ Ne PAS exécuter de rollback / deploy / DNS write sans signoff A0
- ❌ Ne PAS surveiller Life OS (couche L1)
- ❌ Ne PAS prendre de décisions Squad-level (proposition mission card uniquement)
- ❌ Ne PAS auto-enrichir Airtable (suggère `/airtable-enrich`, ne le lance pas tout seul)

## 3. Architecture

```
Shadow_L2/
├── HEARTBEAT_PROTOCOL.md
├── SPEC.md                  (ce fichier)
├── WORKFLOW.md
├── HEARTBEAT.md
├── README.md                (à enrichir, fichiers existants 00-06)
├── A0_inbox/                (alerts H1 + digests)
├── 00_picard-phase-1-summary-20260517.md  (existant)
├── 01_mcp-shadow-l2-config-20260516.md
├── 02_god-mode-cli-stack-20260516.md
├── 03..06_migration-reports-*.md
└── agents/
    └── Claude_Code_CLI/
        ├── Heartbeat.md
        ├── Agent.md
        ├── Tools.md
        ├── Context.md
        └── memory/
            ├── inbox/
            ├── outbox/
            ├── cooldown.json     (anomaly_id → expiry_ts)
            ├── pulse.log
            └── minimax-quirks.md
```

## 4. Tick Cycle

Identique à Shadow_L0 §4, avec ajout :
- **PROBE** vérifie `cooldown.json` avant de scanner une surface
- **DECIDE** applique cooldown_min de la task selon severity
- **OBSERVE** met à jour `cooldown.json` après alerte

## 5. Routing & Fallback

Default : `Claude_Code_CLI` on MiniMax (request budget tolérant ticks 5 min).
Fallback per HEARTBEAT_PROTOCOL §10.

## 6. Acceptance Criteria

- [ ] AC-L2-01 : Tick à blanc avec `phase_enabled: false` n'invoque pas le CLI
- [ ] AC-L2-02 : Tick supervisé exécute UNE task due, écrit pulse.log + cooldown.json
- [ ] AC-L2-03 : H1 alert produit fichier atomique `A0_inbox/CRITICAL-*.md`
- [ ] AC-L2-04 : Re-alerte sur même anomaly_id en cooldown → skip silencieux
- [ ] AC-L2-05 : Fallback MiniMax→Gemini fonctionne, mention `[FALLBACK_FROM=Claude_Code_CLI]` en outbox
- [ ] AC-L2-06 : Anti-spam backoff déclenché après 12 `HEARTBEAT_EXEC` consécutifs vides
- [ ] AC-L2-07 : Mission card Squad générée pour incident persistent > 30 min
- [ ] AC-L2-08 : Aucune écriture prod-mutate sans signoff (audit log dans outbox)

## 7. Dependencies

| Composant | Statut |
|---|---|
| Claude Code CLI | ✅ |
| MiniMax API key + ANTHROPIC_BASE_URL | ✅ |
| MCP vercel | ✅ |
| MCP supabase | ✅ |
| MCP hostinger-api | ✅ |
| MCP airtable | ✅ |
| MCP clickup | ✅ |
| MCP notion | ✅ |
| `heartbeat-tick-l2.ps1` | ⏳ to scaffold |
| Task Scheduler entry `ASpace-Heartbeat-L2-5min` | ⏳ disabled |
| Squad inboxes `30_Business_OS/0X/inbox/` | ⏳ to scaffold |

## 8. Cross-refs

- `./HEARTBEAT_PROTOCOL.md`
- `./HEARTBEAT.md`
- `./WORKFLOW.md`
- `../Shadow_L0/SPEC.md`
- `./02_god-mode-cli-stack-20260516.md`
- `LLM_Wiki/wiki/concepts/concept_shadow_l1_l2_heartbeat_symphony.md`

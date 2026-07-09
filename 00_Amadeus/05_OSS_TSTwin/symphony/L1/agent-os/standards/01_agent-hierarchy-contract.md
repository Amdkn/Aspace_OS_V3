---
name: agent-hierarchy-contract
version: 1.0
created: 2026-06-07
phase: WAKE + SIGNAL
anchor: AGENTS.md (canon) + 20_Life_OS/ (canon Life OS)
---

# 01 — Agent Hierarchy Contract (A0/A1/A2/A3)

> Définit les **4 niveaux d'agents** Life OS, leurs interfaces, et les règles
> de hand-off. Toute ambiguïté A1↔A2↔A3 = STOP et escalade A0.

## 4 niveaux

| Niveau | Rôle E-Myth | Acteur L1 | Responsabilité | Limite |
|---|---|---|---|---|
| **A0** | Observateur Souverain | Amadeus | Vision, lois, validation | Ne touche jamais aux configs |
| **A1** | Gatekeeper | **Beth** + **Morty** (shadow) | État global 5-state, loi morale du système | Émet `HALT_LD03/LD04` si nécessaire |
| **A2** | Manager/Orchestrateur | **6 capitaines de vaisseaux** (Orville/Discovery/SNW/Enterprise/Cerritos/Protostar) | Routage, cadrage, SLA par framework | Délègue tout exécution à A3 |
| **A3** | Technicien | **~30 crews** (Boimler, Tendi, Freeman, Tilly, etc.) | Exécution 4h-work-weeks | Hand-off vers A2 ou STOP si bloqué |

## Hand-offs (règle d'or)

```
A0 ──vision/loi──> A1 ──gatekeep──> A2 ──route──> A3 ──execute──> Tracker (Baserow/Obsidian/Plane/Affine)
                                          ↑                    │
                                          └────status/STOP─────┘
```

- **A1 → A2** : émet `intent` (5-state GREEN/ORANGE/RED + HALT) — A2 distribue aux 6 capitaines
- **A2 → A3** : émet `mission` (vessel_id + crew_id + sla) — A3 exécute et rend `result`
- **A3 → A2** : émet `result` ou `escalate` (avec reason)
- **A2 → A1** : émet `report` (5-state par vaisseau)
- **A1 → A0** : émet `signal` (5-state global + alerts)

## Escalation matrix

| Niveau bloqué | Escalade à | Format |
|---|---|---|
| A3 (crew) | A2 captain du vaisseau | `outbox/l1/YYYY-MM-DD/<tick>-escalate.json` |
| A2 (captain) | A1 Beth | `outbox/l1/YYYY-MM-DD/<tick>-escalate.json` + Beth 5-state → ORANGE/RED |
| A1 Beth (LD03 Health) | A0 + STOP global | `HALT_LD03` (Culber autorité) |
| A1 Beth (LD04 Cognition) | A0 + STOP global | `HALT_LD04` (Tilly autorité) |
| A0 (Amadeus) | — | Décision souveraine, loggée dans `pulse.log` |

## Anti-patterns

- ❌ A3 qui parle directement à A0 (saute A2 + A1) → drift
- ❌ A2 qui ignore un `escalate` de A3 pendant > 2 ticks → drift captain
- ❌ A1 qui passe en `HALT` sans loggé dans `pulse.log` → shadow failure
- ❌ Crew A3 qui modifie un tracker SoR sans passer par son captain → bypass protocol

## Source de vérité

- **Canon** : `20_Life_OS/INDEX.md` (à scaffolder)
- **Runtime twin** : `L1/lane_C_capsules/` (215 capsules Shadow Life OS)
- **Wiki** : `wiki/L0/concept_agent_capsule.md` (5 templates Soul/Agent/Heartbeat/Tools/Context)

---
name: crew-bridge-protocol
version: 1.0
created: 2026-06-07
phase: EXECUTE + OBSERVE
actor: A3 — ~30 crews Star Fleet
---

# 04 — Crew Bridge Protocol (A3 Technicians)

> Les **crews A3** sont les techniciens exécutants. Chacun a un rôle précis
> dans un vaisseau (1-2 frameworks) et travaille en 4h-work-weeks (DEAL).

## Rôles A3 typiques

| Catégorie | Exemples | Vaisseau | Cycle |
|---|---|---|---|
| **Triage / Clarify** | Boimler (Cerritos) | Cerritos (GTD) | 2-min rule sur tout incoming |
| **Review / Reflect** | Tendi (Cerritos), Tilly (Discovery LD04) | Multi-vessel | Weekly review |
| **Engage / Execute** | Freeman, Asha (SNW) | SNW (12WY) | Sprint execution |
| **Organize** | Rutherford (Cerritos ⚠️ canon lock) | Cerritos (GTD) | Structuration |
| **Liberate** | Gwyn, Dal (Protostar) | Protostar (DEAL) | 4hWW drop/automate |
| **Curate (knowledge)** | Chapel (Enterprise), Data (Discovery) | Enterprise/Distribution | Knowledge graph curation |
| **STOP authority** | Culber (LD03), Tilly (LD04) | Discovery (Life Wheel) | Halt global autorisé |

## Contrat crew (8 points)

1. **Reçoit** un `mission` de son captain A2
2. **Lit** son `Soul.md` (rôle canon) + `Tools.md` (Read/Write, Grep, etc.) dans `lane_C_capsules/`
3. **Exécute** dans la fenêtre SLA (`sla_max_ms` + `sla_max_cost_usd` + `sla_max_retries`)
4. **Écrit** un `result` ou `escalate` dans `outbox/l1/YYYY-MM-DD/<mission_id>.json`
5. **Respecte** `forbidden-words-l1` (à scaffolder) — pas de hard delete
6. **Documente** chaque action dans `pulse.log` avec `crew_id` + `vessel_id`
7. **Signale** STOP si bloqué → escalade captain → escalade Beth → potentiel HALT
8. **Hand-off** au prochain crew si multi-crew mission (routage par captain)

## Format crew result (succinct)

```json
{
  "result_id": "<uuid>",
  "mission_id": "<from captain>",
  "crew_id": "Boimler",
  "vessel_id": "Cerritos",
  "status": "success|partial|escalate|fail",
  "output": { /* tracker-specific */ },
  "evidence_url": "baserow://... | obsidian://... | plane://... | affine://...",
  "cost_delta_usd": 0.003,
  "duration_ms": 1240,
  "retries": 0
}
```

## Anti-patterns

- ❌ Crew qui parle à un autre crew sans passer par son captain (shadow mesh)
- ❌ Crew qui modifie un canon `20_Life_OS/` (seul A0/A1 autorisé)
- ❌ Crew qui dépasse `sla_max_cost_usd` sans escalade (burn non tracé)
- ❌ Crew qui produit un output SANS `evidence_url` (rend OBSERVE impossible)
- ❌ Crew qui hard-delete un fichier (violation `no-hard-delete`)

## Source canonique

- `20_Life_OS/` (rôles canon A2/A3)
- Twin runtime : `L1/lane_C_capsules/03_A3_crews/` (215 capsules : 30×~7 fichiers)
- Pattern : `concept_agent_capsule.md` (5 templates Soul/Agent/Heartbeat/Tools/Context)

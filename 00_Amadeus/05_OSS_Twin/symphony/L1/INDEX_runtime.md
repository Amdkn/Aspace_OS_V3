---
source: Shadow_Life_OS / symphony-L1 / Lane_B
date: 2026-06-07
type: index
layer: L1_Life_OS
lane: B_runtime
status: SCAFFOLD_ONLY
domain: A0_Sovereign / L1_Life_OS / Symphony_Runtime
tags: [#ShadowLifeOS #LaneB #Runtime #Symphony #Affine #Baserow #Obsidian #Plane]
---

# Lane B — Runtime Index

> **Lane B (Runtime Layer)** : 3-5 jours · specs d'orchestration, scripts, bridges, MCPs
> La runtime est ce qui **exécute** les agents des Lanes A et C.

---

## 📂 Structure cible

```
lane_B_runtime/
├── 01_routing/         # Specs Symphony (routing, transformations)
├── 02_scripts/         # Python/PS1 executors (batch, handoffs, GTD, DEAL)
├── 03_bridges/         # L0↔L1, L1↔L2, A0↔A1↔A2↔A3
├── 04_mcps/            # Serveurs MCP (par surface : Affine, Baserow, Obsidian, Plane)
└── INDEX_runtime.md
```

## 🔌 Specs Symphony existantes (à reclasser)

| Spec | Path actuel | Framework | Destination |
|---|---|---|---|
| `symphony-affine.spec.md` | `symphony/L1/symphony-affine.spec.md` | DEAL | `lane_B_runtime/01_routing/` |
| `symphony-baserow.spec.md` | `symphony/L1/symphony-baserow.spec.md` | Life Wheel / 12WY | `lane_B_runtime/01_routing/` |
| `symphony-obsidian.spec.md` | `symphony/L1/symphony-obsidian.spec.md` | PARA | `lane_B_runtime/01_routing/` |
| `symphony-plane.spec.md` | `symphony/L1/symphony-plane.spec.md` | GTD | `lane_B_runtime/01_routing/` |

## 🌉 Bridges (à scaffolder)

| Bridge | De → Vers | Use case |
|---|---|---|
| `L0_to_L1.bridge.md` | Shadow L0 → L1 Life OS | Handoff IA → agents A1 |
| `L1_to_L2.bridge.md` | L1 Life OS → L2 Business | JTBD trigger quand projet A2 Life OS devient Summer's Verse B1 |
| `A0_to_A1.bridge.md` | A0 Amadeus → A1 Beth/Morty | Intent emission, Sunday Uplink |
| `A1_to_A2.bridge.md` | A1 Beth/Morty → A2 Ships | Context Pack distribution |
| `A2_to_A3.bridge.md` | A2 Ships → A3 Crews | Domain-scoped mission assignment |
| `A3_DLQ.bridge.md` | A3 → Donna DLQ | Dead Letter Queue pour findings rejetés |

## 🛠️ Scripts (à scaffolder)

| Script | Framework | Trigger |
|---|---|---|
| `symphony_gtd_orchestrator.py` | GTD | Inbox Plane → Clarify → Organize |
| `deal_symphony_bridge.py` | DEAL | GEordi Guides → Affine DEAL drafts |
| `affine_picard_pipeline.py` | PARA | Obsidian PARA → Picard projects |
| `baserow_12wy_sync.py` | 12WY | 12WY scorecard → Baserow |
| `obsidian_wikilink_auditor.py` | PARA | Wikilink integrity check |

## 📡 MCPs (à scaffolder)

| MCP server | Surface | Status |
|---|---|---|
| `mcp-affine` | DEAL workspace | **ACTIVE** (2026-06-15) — 4 tools, 8 KB, env var `AFFINE_API_KEY` |
| `mcp-baserow` | Life Wheel / 12WY tables | **ACTIVE** (2026-06-15) — 4 tools, 6.7 KB, env var `BASEROW_API_KEY` |
| `mcp-obsidian` | PARA vault | **ACTIVE** (2026-06-15) — 6 tools, 7.5 KB, local FS (no auth) |
| `mcp-plane` | GTD workspace | **ACTIVE** (2026-06-15) — 6 tools, 7.6 KB, env var `PLANE_API_KEY` |

**2026-06-15** : 4 MCP Python servers créés en `lane_B_runtime/04_mcps/` (20 tools total, 30.5 KB, 4/4 ast.parse valid, Test Key Pragma env var strict, stub mode si no API key).

---

## 🔗 Symbiose Lane A ↔ Lane B

Chaque spec runtime pointe vers les A2 ships qu'elle orchestre dans Lane A :

```
symphony-baserow.spec.md   →   [[A2_Discovery_Spec.twin]] (Life Wheel)
                              [[A2_Curie_SNW_Spec.twin]] (12WY)
symphony-affine.spec.md    →   [[A2_HoloJaneway_Protostar_Spec.twin]] (DEAL)
symphony-obsidian.spec.md  →   [[A2_Computer_Enterprise_Spec.twin]] (PARA)
symphony-plane.spec.md     →   [[A2_HoloDeck_Cerritos_Spec.twin]] (GTD)
                              [[A2_Orville_Spec.twin]] (Ikigai planning)
```

---

## 📊 État Lane B

- **2026-06-07** : Scaffold créé. 4 specs Symphony à reclasser depuis `symphony/L1/` racine. Bridges/scripts/MCPs en plan.
- **2026-06-15** : **Phase 2 Symphony ACTIVE** — 4 MCP servers implémentés (20 tools, 30.5 KB) + 6 bridges Python wirings (1053 lines, ~44 KB, smoke tests passed : Curie_SNW routing, Discovery+LD02→Saru, HoloJaneway+automate_zero→Zero, Picard=A3 crew NOT A2). Tous syntactiquement valides (10/10 ast.parse). Anti-patterns guarded (Picard-as-A2=0, Freeman-as-A2=0, Sia=0, HoloJaneway-hyphen=0).

*Index régénéré manuellement (2026-06-07).*

---
source: Shadow_Life_OS / symphony-L1 / Lane_C
date: 2026-06-07
type: index
layer: L1_Life_OS
lane: C_capsules
status: SCAFFOLD_ONLY
domain: A0_Sovereign / L1_Life_OS / Agent_Capsule
tags: [#ShadowLifeOS #LaneC #AgentCapsule #Soul #Heartbeat]
---

# Lane C — Agent Capsules Index

> **Lane C (Agent Capsule Layer)** : 2-3 jours · capsules `Soul/Agent/Heartbeat/Tools/Context` par agent
> Template canon : `00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/agent_capsules/_TEMPLATE/`

---

## 📐 Template (5 fichiers par agent)

| Fichier | Fonction | Source template |
|---|---|---|
| `Soul.md` | Identité, ton, valeurs, interdits | `_TEMPLATE/Soul.md` |
| `Agent.md` | Mission, périmètre, responsabilités | `_TEMPLATE/Agent.md` |
| `Heartbeat.md` | Cadence, reprises, points de contrôle | `_TEMPLATE/Heartbeat.md` |
| `Tools.md` | Outils autorisés, MCP, CLI, limites | `_TEMPLATE/Tools.md` |
| `Context.md` | Mémoire locale, état courant, handoff | `_TEMPLATE/Context.md` |

## 🛡️ A1 capsules (2 agents × 5 = 10 fichiers)

- `01_A1_capsules/beth/`
- `01_A1_capsules/morty/`

## 🚀 A2 capsules (6 ships × 5 = 30 fichiers)

- `02_A2_capsules/orville/`
- `02_A2_capsules/discovery/`
- `02_A2_capsules/curie_snw/`
- `02_A2_capsules/computer_enterprise/`
- `02_A2_capsules/holodeck_cerritos/`
- `02_A2_capsules/holojaneway_protostar/`

## 🛠️ A3 capsules (35 crews × 5 = 175 fichiers)

- `03_A3_capsules/orville/` (9)
- `03_A3_capsules/discovery/` (8)
- `03_A3_capsules/snw/` (5)
- `03_A3_capsules/enterprise/` (4)
- `03_A3_capsules/cerritos/` (5)
- `03_A3_capsules/protostar/` (4)

**Total théorique** : 215 fichiers capsules.

**Phase 1 (squelette)** : A1 + A2 = 40 fichiers (template rempli à 80%).
**Phase 2** : A3 = 175 fichiers (template rempli à 50%, enrichi par usage).

---

## 🔗 Symbiose Lane A ↔ Lane C

Chaque capsule pointe vers son spec twin dans Lane A via `[[<X>_Spec.twin]]` dans `Agent.md`.

---

## 📊 État Lane C

- **2026-06-07** : Scaffold créé. Aucun agent populé. Phase 1 commence après validation A0.
- **2026-06-15** : **Phase 2 Symphony v1 twins ACTIVE** — 35 A3 twins créés (6 ships : Orville 9 / Discovery 8 / Curie_SNW 5 / Computer_Enterprise 4 / HoloDeck_Cerritos 5 / HoloJaneway_Protostar 4) en `lane_A_specs/03_A3_crews/<ship>/<name>.twin.md` (kebab-case v1.0). 35 v0 legacy twins (PascalCase, 2026-06-07) archivés dans `_TRASH_2026-06-15_legacy_v0/` (D4 no-hard-delete respecté). 70 fichiers au total (35 v1 ACTIVE + 35 v0 LEGACY). Anti-patterns guarded : Picard-as-A2=0 (Picard = A3 Projects), Freeman-as-A2=0 (Freeman = A3 Engage), Sia=0 (ZORA = A2 Discovery), HoloJaneway-hyphen=0 (Holo Janeway with space per spec L.25). LD03/LD04 hard safety domains (Culber/Tilly) avec STOP authority on Beth. Saru `scarcity_mode: absent|present|dominant` field.

*Index régénéré manuellement (2026-06-07).*

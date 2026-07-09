---
id: bridge.L0_to_L1
layer: L0_L1_bridge
status: SHADOW_ACTIVE
created: 2026-06-07
lane: B_runtime
---

# Bridge L0 → L1 — Shadow L0 IA → Life OS A1/A2

> Les Shadow L0 (Codex, Claude Code, Gemini CLI, Antigravity) injectent des findings dans la L1 Life OS via ce bridge.

## Trigger

Un Shadow L0 termine une mission qui produit un artefact durable (note Obsidian, vidéo clarifiée, deal draft, etc.).

## Flow

```
Shadow L0 Executor
  ↓ mission_result
A0 Inbox (Shadow_L0/A0_inbox/)
  ↓ sunday_uplink
Beth (A1) triage → GREEN / ORANGE / RED / HALT_LD03 / HALT_LD04
  ↓ clearance GREEN
Morty (A1) → A2 ship approprié (Orville/Discovery/Curie/Computer/HoloDeck/HoloJaneway)
  ↓ context pack
A3 crew execution
```

## Anti-patterns

- ❌ Court-circuiter Beth : aucun L0 → A3 direct
- ❌ Auto-clearance : Beth doit toujours valider un L0 input
- ❌ Drop dans Hermes Agent (dossier fermé, pas d'écriture)

---
id: bridge.A0_to_A1
layer: A0_A1_bridge
status: SHADOW_ACTIVE
created: 2026-06-07
lane: B_runtime
---

# Bridge A0 → A1 — Amadeus → Beth/Morty

> A0 (Amadeus) émet des Intents. A1 (Beth/Morty) les transforme en Context Packs exécutables.

## Trigger

A0 émet un Intent :
- Sunday Uplink (hebdomadaire)
- Mission ad-hoc (ex: `/project-init`, recherche, audit)
- Crisis escalation (LD03/LD04 alert)

## Flow

```
A0 (Amadeus)
  ↓ Intent statement (canal: chat, plan, ADR)
A1 Beth (A1) — conscience
  ↓ triage (5 états: GREEN/ORANGE/RED/HALT_LD03/HALT_LD04)
A1 Morty (A1) — executor
  ↓ Context Pack (template ContextPack.template.yml)
A2 Ship — domain owner
  ↓ ...
```

## Sunday Uplink Protocol

Hebdomadaire : A0 ↔ Beth ↔ Morty ↔ A2 captains sur l'état des 6 vaisseaux et des 8 Life Domains.

Output : `Sunday_Uplink_Protocols/YYYY-WW.md`

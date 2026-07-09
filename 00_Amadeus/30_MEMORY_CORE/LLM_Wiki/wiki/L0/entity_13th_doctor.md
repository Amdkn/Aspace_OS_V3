---
source: LLM_Wiki_A0
date: 2026-05-11
type: entity
domain: Tech_OS / L0_Infra / Doctor_Companions
tags: [#entity #13th_Doctor #L0 #A2 #Infra #Docker #Watchdog #Rick_A3]
---

# Entity: 13th Doctor (L2 — Infra Guardian)

> Canonical: `A'Space_OS_V2/10_Tech_OS/11_Infra_13th_Doctor/`

La **13th Doctor** est l'agent **A2** responsable de l'infrastructure L0 Tech OS. Elle exécutée les scripts Docker, les watchdogs, et les tâches d'infra sous la juridiction de [[entity_rick|Rick]].

---

## Role

Sous Rick (A1), la 13th Doctor est le **Manager A2** de l'infrastructure :
- Scripts Python/PS pour automation
- Docker compose, container management
- Windows watchdog (ADR-006: native PS over Docker)
- Checkpoints (TARDIS Protocol implementation)

---

## TARDIS Protocol Implementation

La 13th Doctor implémente le [[entity_tardis_protocol|TARDIS Protocol]] :
- Exécute les scripts de checkpoint avant toute purge
- Vérifie les dossiers > 100 MB avant migration
- Génère les rapports de ce qui Ne Sera Pas dans la destination

---

## Related

- **[[entity_rick]]**: 13th Doctor opère sous la juridiction de Rick
- **[[concept_nano_squads]]**: Les Doctor companions sont A3 agents sous Rick
- **[[entity_12th_doctor]]**: Sœur — Data pipelines (vs. Infra pour 13th)
- **[[entity_11th_doctor]]**: Frère — Interface/UI (vs. Infra pour 13th)

---



---

## Inbounds

- [[entity_13th_doctor]]
*Last updated: 2026-05-11*
*Source: AGENTS.md (canon)*
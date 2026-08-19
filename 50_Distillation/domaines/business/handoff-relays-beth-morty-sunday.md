---
type: Concept
title: Handoff Relays — Beth (alignement), Morty (exécution), Sunday (cadence), OpenHarness (runtime)
description: Les 4 canaux de relais du CEO's Desktop : Beth aligne, Morty exécute, Sunday cadence, OpenHarness runtime. Tous en stub Phase 1, à activer Phase 2 sur les mêmes triggers.
tags: [handoff, beth, morty, sunday, openharness, relai, cadence, alignement]
generated: { by: minimax-m3, at: 2026-08-19 }
verified:
  - { by: process:lecture-directe, at: 2026-08-19 }
sources:
  - id: HANDOFF_BETH
    resource: "30_Business_OS/10_Projects/ceo-desktop/handoffs/Beth_Alignment_Log.md"
    title: Beth — Alignment Log
    last_modified: "2026-06-07"
  - id: HANDOFF_MORTY
    resource: "30_Business_OS/10_Projects/ceo-desktop/handoffs/Morty_Global_Queue.md"
    title: Morty — Global Queue
    last_modified: "2026-06-07"
  - id: HANDOFF_SUNDAY
    resource: "30_Business_OS/10_Projects/ceo-desktop/handoffs/Sunday_Uplink_Protocols.md"
    title: Sunday — Uplink Protocols
    last_modified: "2026-06-07"
  - id: MANIFEST_CEO_DESKTOP
    resource: "30_Business_OS/10_Projects/ceo-desktop/MANIFEST.md"
    title: Manifest — ceo-desktop
    last_modified: "2026-07-13"
  - id: CLAUDE_CEO_DESKTOP
    resource: "30_Business_OS/10_Projects/ceo-desktop/CLAUDE.md"
    title: CLAUDE.md — CEO's Desktop
    last_modified: "2026-06-07"
okf_version: "0.2"
---

# Handoff Relays — Beth (alignement), Morty (exécution), Sunday (cadence), OpenHarness (runtime)

> **Une seule chose à retenir.** Le CEO's Desktop fonctionne à **4 canaux de relais** : **Beth** aligne (decisions/veto), **Morty** exécute (JTBD queue), **Sunday** cadence (weekly check-in), **OpenHarness** runtime (canal implicite). Tous en stub Phase 1 ; activation Phase 2 sur les mêmes triggers.

## Les 4 relais canoniques

| # | Canal          | Owner                       | Cadence                       | Status Phase 1 |
|---|----------------|-----------------------------|-------------------------------|----------------|
| 1 | **Beth Alignment** | A1 Beth (L1 Conscience)    | on-demand + 12WY milestone    | STUB           |
| 2 | **Morty Global Queue** | A1 Morty (L1 Execution) | continuous (queue) + Sunday review | STUB     |
| 3 | **Sunday Uplink** | A3 Sunday (cadence)         | weekly (12WY rhythm)          | STUB           |
| 4 | **OpenHarness** | A1 Rick (L0 Bedrock Sobriété) per `ADR-RICK-001` | implicit (no per-week artifact) | IMPLICIT |

## Rôle de chaque relais

### 1. Beth — Alignment

> Beth is the **alignment channel** for the CEO's Desktop. She records the A0 decisions and vetoes that shape the 12WY cycles, the domain Rocks, and the B3 JTBD acceptance criteria. Beth is the auditor of « did we stay true to the B1 direction? » (`Handoff_Beth`)

Son log est la **piste d'audit des décisions** : quand un Rock est redéfini, un drift de domaine corrigé, ou un JTBD rejeté, Beth timestamp, lie l'évidence, et surface au prochain Sunday uplink.

### 2. Morty — Execution

> Morty is the **execution channel** for the CEO's Desktop. He holds the global queue of Context Packs and dry-runs that fan out from B2 domain managers to the 8 B3 squads. (`Handoff_Morty`)

Sa queue est le **ledger in-flight** : quel JTBD est queued, en dry-run, shipped with proof, ou blocked. C'est la source de vérité pour « qu'est-ce que les 8 B3 squads font vraiment cette semaine ? »

### 3. Sunday — Uplink Protocols

> Sunday is the **cadence channel** for the CEO's Desktop. She runs the weekly uplink between A0 (Amadeus), Beth (alignment), Morty (execution), and the OpenHarness runtime. Sunday is the heartbeat. (`Handoff_Sunday`)

Ses protocoles définissent le **weekly template** : ce qui est posté, dans quel ordre, avec quels liens d'évidence, et ce qui déclenche une escalation A0. Le 12WY est son horloge.

### 4. OpenHarness — Runtime

> A fourth relay — the harness/loop channel — is implicit via OpenHarness per `ADR-RICK-001`. (`CLAUDE.md` § "4 Handoff Relays")

Pas d'artefact par semaine. C'est le runtime sous-jacent qui orchestre les 3 autres relais.

## Trigger d'activation Phase 2 (commun aux 4)

> This stub is promoted to a live log in **Phase 2**. The activation trigger is the same as Beth's and Morty's: B2 managers named for ≥4 of 8 SOB. (`Handoff_Morty`)

**Même trigger pour les 3 stubs explicites** : B2 managers named for ≥4 of 8 SOB. OpenHarness n'a pas de trigger séparé ; il est activé implicitement par le projet Phase 2.

## Le premier full 12WY cycle completed est le Phase 3 graduation gate

> The first full 12WY cycle completed is the **Phase 3 graduation gate**. (`Handoff_Sunday`)

## Pourquoi 4 canaux

- **Séparation des préoccupations.** Aligner ≠ exécuter ≠ cadencer ≠ runtime. Les 4 canaux évitent qu'un agent fasse deux métiers à la fois.
- **Continuité.** Un canal stubbé ne bloque pas les autres ; Phase 1 fonctionne sans Beth/Morty/Sunday actifs.
- **Anti-SPOF.** A0 n'est plus le seul point de défaillance — chacun des relais est un agent dédié.

## Anti-patterns

- **Activer un relais avant les triggers.** `handoffs/Beth_Alignment_Log.md` ne se peuple pas en Phase 1.
- **Confondre les canaux.** Beth consigne des décisions ; Morty consigne des JTBD ; Sunday cadence le tout. Mélanger les rôles casse la traçabilité.
- **Oublier OpenHarness.** Le canal implicite n'a pas d'artefact, mais le runtime existe. Un projet sans OpenHarness est un projet sans runtime.

## Ce que ce n'est pas

- Pas un organigramme RH. Les relais sont des **rôles d'agents**, pas des postes salariés.
- Pas des canaux de communication Slack/Discord. Le runtime est dans le dépôt, pas dans un chat tiers.

## Conséquence opérationnelle

Un projet CEO's Desktop Phase 2 sans Beth/Morty/Sunday actifs **n'est pas prêt à accepter un handoff B1** : les 4 boundary gates ne sont pas auditables sans eux.

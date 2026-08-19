---
type: Concept
title: Sunday Uplink — revue hebdomadaire ritualisée
description: Sunday Uplink = moment unique de revue hebdomadaire Life OS. Discovery consolide le ZORA state, Orville compile les crew findings Ikigai, Chapel expose le Scorecard. Seul moment toléré pour escalader à A0 (board observer passif).
tags: [sunday-uplink, revue-hebdomadaire, zora-state, chapel-scorecard, a0-escalade]
generated: { by: minimax-m3, at: 2026-08-19T04:15:00Z }
verified:
  - { by: process:read_local_v2, at: 2026-08-19T04:15:00Z }
sources:
  - id: gatekeepers-readme
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/00_Gatekeepers_Beth_Morty/Sunday_Uplink_Protocols/README.md
    title: Sunday Uplink Protocols README
    last_modified: 2026-06-21
  - id: discovery-spec
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/22_Wheel_Discovery/A2_Discovery_ZORA_Spec.md
    title: A2 Discovery Spec — Sunday Uplink mention
    last_modified: 2026-06-21
  - id: a0-reasoning-map
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/a0_reasoning_map.md
    title: A0 Reasoning Map — 5 minute test
    last_modified: 2026-04-07
okf_version: "0.2"
---

# Sunday Uplink — revue hebdomadaire ritualisée

## Énoncé canon

Le **Sunday Uplink** est l'unique moment de revue hebdomadaire de Life OS. Il consolide :
1. **Discovery/ZORA state** — synthèse des 8 LD findings du dimanche précédent.
2. **Orville/Ikigai crew findings** — compilation des 9 crew (Mercer/Grayson/Malloy/Finn + Isaac/Lamarr/Bortus/Alara/Klyden).
3. **Chapel/SNW Scorecard** — exposition des 12WY KPIs.

C'est le **seul moment toléré** pour escalader à A0 (board observer passif). En dehors du Sunday Uplink, A0 ne reçoit aucune escalade.

Source : `A1_Beth_Spec.md` (A0 board observer = milestones H30/H90 seulement) + `Sunday_Uplink_Protocols/README.md`.

## Pourquoi ritualiser

Un système sans revue hebdomadaire dérive. Les drifts LD04 cognition, LD05 isolation, LD06 bond fracture doivent être détectés **avant** qu'ils ne forcent un HALT Beth.

Le Sunday Uplink transforme :
- � Drift silencieux (les LDs dégradent sans visibilité)
- ✅ Drift surfacé (les LDs sont audités weekly)

## Cohérence Beth/Morty (5 min test)

Le Sunday Uplink respecte le **test des 5 minutes** d'A0 Reasoning Map §4.2 :
> *"Si le scoring de cette idée prend plus de 5 minutes, c'est que l'idée n'est pas assez clarifiée. Retourne en Phase CLARIFY."*

Beth peut rejeter mécaniquement et escalader seulement les cas ambigus en <5 minutes, grâce aux seuils chiffrés SDD-005 (LD03_minimum=4.0, LD04_minimum=3.5).

## AaaS 3 variants status check

Le Sunday Uplink note l'état des 3 variants AaaS + 1 dormant :
- Solaris (Book H1) — ACTIF Q3 2026
- Nexus-OMK (Saru H3) — CLOS 2026-06-20
- Orbiter-ABC (Burnham H10) — ACTIF Q3 2026
- 4e Dormant (Tilly/Culber) — dormant, réveil Q4 2026 / Q1 2027

Cohérent avec `J03_Jerry_Nexus_LD02_LD06_Finance_Family | FIP STANDARD` canon.

## Verdict distillation

`canon` — fait autorité. Source canonique : `Sunday_Uplink_Protocols/README.md` + cohérence avec `A1_Beth_Spec.md` + `a0_reasoning_map.md §4.2`.

## Pièges documentés

- **Piège 1** : escalader A0 en dehors du Sunday Uplink. **Viole la cadence A0 = board observer passif**. Sauf HARD SAFETY immédiat (LD03/LD04 RED), pas d'escalade quotidienne.
- **Piège 2** : Sunday Uplink qui dure >5 minutes. C'est le signe d'une idée mal clarifiée — retour en Phase CLARIFY.
- **Piège 3** : Sunday Uplink qui consomme le buffer 20% du cycle 12WY. Discipline 50/30/20 (SNW load rule) impose 20% buffer-recovery.

## Couplage inter-ships

Le Sunday Uplink est l'interface entre :
- Discovery (ZORA Life Wheel)
- Orville (Ikigai crew)
- SNW (12WY Scorecard)

Chacun publie son état, mais **Beth** consolide (veto distribué). Morty route ensuite vers le ship d'exécution suivant.

Source : `gatekeepers-readme` ligne 19 + plan §3.5 (triptyque BETH = Ikigai⊃Life Wheel�Muse).

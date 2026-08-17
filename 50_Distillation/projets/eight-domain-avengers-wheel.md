---
type: Concept
title: Eight Domain Avengers Wheel
description: Les 8 domaines B2 — Growth (Superman/Guardians), Sales (Martian Manhunter/Illuminati), Product (Flash/Avengers), Ops (Batman/Fantastic4), IT (Cyborg/KangDynasty), Finance (WonderWoman/Thunderbolts), People (GreenLantern/X-Men), Legal (Aquaman/Eternals) — chacun avec un B2 captain et un B3 squad Marvel.
tags: [concept, eight-domain, avengers, b2, b3, marvel, mapping]
generated: { by: minimax-m3, at: 2026-08-17T21:00:00Z }
verified:
  - { by: process:extraire_substrat_rdf, at: 2026-08-17T19:50:00Z }
  - { by: process:lecture_concepts_picard, at: 2026-08-17T21:00:00Z }
sources:
  - id: roster-omk-08-legal
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/B2_Business_Domains/08_Legal_Aquaman_Eternals/01_B3_AGENT_ROSTER.md"
    title: 01 B3 Agent Roster — Legal (Aquaman/Eternals)
    last_modified: 2026-05-27
  - id: roster-omk-04-ops
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/B2_Business_Domains/04_Ops_Batman_Fantastic4/01_B3_AGENT_ROSTER.md"
    title: 01 B3 Agent Roster — Ops (Batman/Fantastic4)
    last_modified: 2026-05-27
  - id: handover-abc
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/02 ABC OS & Child Care BOS/CERRIROS_HANDOVER.md"
    title: Handover ABC — B2 ownership domain mapping
    last_modified: 2026-05-21
okf_version: "0.2"
---

# Eight Domain Avengers Wheel

## Définition

Les **8 domaines B2** canoniques d'A'Space OS, chacun couplé à un B2
captain et à un B3 squad Marvel. Le mapping est identique dans les 4
projets Summer's Verse + OMK Business OS. Construit par analogie avec
l'univers Marvel (Avengers, X-Men, etc.), avec un B2 = "ligue" et un
B3 = "squad d'exécution".

## Le mapping canonique

| # | Domaine | B2 Captain | B3 Squad | B2 emet |
|---|---------|-----------|----------|---------|
| 01 | **Growth** | Superman | Guardians of the Galaxy | `GROWTH_READY` / `NEEDS_SIGNAL` / `BLOCKED_PROMISE` |
| 02 | **Sales** | Martian Manhunter (legacy) / JohnJones (W40 V4) | Illuminati | `SALES_READY` / `NEEDS_QUALIFICATION` / `BLOCKED_COMMITMENT` |
| 03 | **Product** | Flash | Avengers | `PRODUCT_READY` / `NEEDS_SCOPE` / `BLOCKED_DELIVERY` |
| 04 | **Ops** | Batman | Fantastic Four | `LAUNCH_READY` (transverse gate final) |
| 05 | **IT** | Cyborg | Kang Dynasty | `SYSTEM_READY` / `NEEDS_SYSTEM_OWNER` / `QUARANTINE` |
| 06 | **Finance** | Wonder Woman | Thunderbolts | `FINANCE_READY` / `NEEDS_MODEL` / `BLOCKED_LEAKAGE` |
| 07 | **People** | Green Lantern | X-Men | `ASSIGNED` / `NEEDS_OWNER` / `DLQ` |
| 08 | **Legal** | Aquaman | Eternals | `LEGAL_READY` / `NEEDS_REVIEW` / `BLOCKED_RISK` |

## Note sur la nomenclature Sales

Le captain **Martian Manhunter** (legacy) est renommé **JohnJones** en
W40 V4. Ownerbook T1 OMK l'indique explicitement :
> "B2 Sales domain control room (note: legacy naming MartianManhunter,
> W40 V4 rename JohnJones)"

C'est un signal de living canon — la nomenclature B2 capitaine évolue
quand le canon W40 change, et les nouveaux chartes/runbooks OMK portent
le nouveau nom pendant que les anciens dossiers conservent l'ancien.

## Structure de dossiers

Chaque domaine est un sous-dossier de `B2_Business_Domains/` (Summer's
Verse) ou `B2_Business_Domains/` (OMK). Il porte typiquement 4 fichiers
canoniques :

```
01_Growth_Superman_Guardians/
├── 00_B2_DOMAIN_CONTROL_ROOM.md   # Pilier B2 — readiness, Rocks
├── 01_B3_AGENT_ROSTER.md          # ~400-470 mots — liste des B3 agents
├── 02_B3_SWARM_SUPERVISION_PROTOCOL.md  # ~240 mots — protocole
└── 01_ROCK_TO_DOD_TO_JTBD_PIPELINE.md  # ~200 mots — pipeline
```

## Le coordinateur transverse — People

**People Green Lantern** est le coordinateur le plus transverse : pour
qu'une motion B3 passe à l'Ops launch readiness, People doit avoir émis
`ASSIGNED` / `NEEDS_OWNER` / `DLQ`. C'est la même règle que pour IT
(`SYSTEM_READY` / `NEEDS_SYSTEM_OWNER` / `QUARANTINE`) et Legal
(`LEGAL_READY` / `NEEDS_REVIEW` / `BLOCKED_RISK`).

## Liens

- [[b2-business-wheel-harmonization-matrix]] — les gates READY/BLOCKED par domaine
- [[fifty-three-b3-agent-roster]] — la squad 53 agents
- [[summers-verse-framework]] — la trame B1/B2/B3
- [[twelve-weeks-year-cycle]] — la cadence des Rocks B2

## Note de confiance

**Confirmé par machine.** Le mapping 8-domaines est lisible dans les 4
handover + 8 dossiers B2 dans le projet OMK. La structure 4 fichiers
canoniques par dossier est vérifiable par énumération substrat.

*Standing : mapping défini dans 5 projets, exécution B2/B3 vide.*

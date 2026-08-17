---
type: Concept
title: JTBD-001 packet grammar — la grammaire B3 canonique
description: Les packets JTBD-001 (Jobs To Be Done) sont la grammaire canonique par laquelle B3 reçoit le travail de B2 : scope, lead, ICP/VOC/painkiller hypotheses, premier experiment RICE, lead/lag indicators, build gates. Les Projects héritent de la version Area et calibrent par mode.
tags: [jtbd, b3, packet, grammar, dod, area-level, canonical]
generated: { by: minimax-m3, at: 2026-08-17T21:25:00Z }
verified:
  - { by: process:extraction-areas, at: 2026-08-17T21:25:00Z }
sources:
  - id: jtbd-growth-001
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B3_Area_Warp_Core/01_Growth_Superman_Guardians/JTBD-GROWTH-001_GUARDIANS_AAAS_GTM_PACKET.md"
    title: JTBD-GROWTH-001 — Guardians AaaS GTM Packet (Area-level)
    last_modified: 2026-05-29
  - id: superman-principles
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/01_Growth_Superman_Guardians/03_SUPERMAN_GROWTH_PRINCIPLES.md"
    title: Principes de Superman — Doctrine Growth du domaine B2-G1
    last_modified: 2026-06-25
okf_version: "0.2"
---

# JTBD-001 packet grammar — la grammaire B3 canonique

Le packet **JTBD-001** est l'unité canonique par laquelle un swarm B3 reçoit un job défini. Il est défini au niveau Area par chaque squad (8 packets canoniques, un par domaine B2 pour J01), puis **calibré** par chaque Project Picard selon son mode (Solaris/Nexus/Orbiter). Le but : que les Projects héritent de la doctrine sans la re-dériver.

## Le packet canon — section par section

Tiré de `JTBD-GROWTH-001_GUARDIANS_AAAS_GTM_PACKET.md` :

**Frontmatter obligatoire** (yaml) :

- `id` — `J01-B3-GROWTH-2026-001` (canonique, fixe)
- `jtbd_id` — même chose
- `source_rock` — le Rock B2 source (ex. `J01-B2-GROWTH-2026-01`)
- `layer` — `B3_AREA_WARP_CORE`
- `surface` — l'Area parente (ex. `Jerry Area J01 LD01 Business`)
- `scope` — `Area (perpetual doctrine — canonical reference for Picard projects)`
- `domain`, `b2_owner`, `guardian_lead`, `supports` (les autres membres du squad)
- `principles_ref` — les P# doctrines援 (ex. `[P1, P3, P5, P6, P7, P8, P9, P11, P12, P13, P14, P15, P16, P18]`)
- `evidence_grade` — `HYPOTHESIS` | `CANONICAL` | `FIELD_PROVEN` | `FIELD_INVALIDATED`
- `status` — `REVIEW_READY` | `SHIPPED` | `BLOCKED` | etc.

**Sections en prose** :

1. **Job statement** (le « when X needs Y, the squad produces Z so Superman can… »)
2. **Lead + Squad** (qui lead, qui supports, ⚠️ noter que les assignations sont indicatives ; le roster fait foi)
3. **North Star + cadre AARRR** (la NSM du domaine et la boucle prioritaire)
4. **ICP filter canonique** (3 critères de rejet + scoring)
5. **VOC** (5 pains génériques, déclinés par mode dans chaque Project)
6. **Painkiller hypotheses** (3 variants canoniques + Drax kill-gate)
7. **Premier experiment RICE + lead/lag indicators + build gates**
8. **Handoff & autorité** (ce que les Projects héritent vs ce qu'ils re-dérivent)
9. **DoD auto-check** (checklist d'acceptance avec `[ ] Acceptance <Hero>`)

## La règle DRY entre Area et Project

La phrase canonique du packet (`JTBD-GROWTH-001` §1) :

> *Picard projects héritent ce packet et calibrent par mode (Solaris/Nexus/Orbiter). Ce fichier = référence canonique, pas à dupliquer.*

C'est la même règle que le fractal B1/B2/B3 : l'Area est la source de vérité ; le Project en est une mission datée. Si un Project **re-dérive** les ICP filters ou la VOC, il a violé la doctrine Area. Si un Project **calibre** une variant painkiller Solaris sur la base de la V1/V2/V3 canonique, il a respecté la doctrine.

## L'évidence grade

L'`evidence_grade` est un signal crucial que la grammaire impose :

- **HYPOTHESIS** : synthèse doctrine ancrée sur le corpus — pas d'interviews réelles. Validation §5.
- **CANONICAL** : la doctrine a été validée par un passage antérieur et stabilisée.
- **FIELD_PROVEN** : la doctrine a passé le test du terrain (≥1 cycle de preuve).
- **FIELD_INVALIDATED** : la doctrine a été réfutée — à corriger ou retirer.

Pour `JTBD-GROWTH-001` au 2026-05-29, l'evidence_grade est `HYPOTHESIS`. C'est explicite : la doctrine est synthétisée mais pas encore field-proven. Les Projects qui en héritent **doivent** remonter leurs preuves pour faire monter l'evidence_grade.

## Le Squad Roster prime sur les tags inline

`JTBD-GROWTH-001` §0 contient un avertissement explicite :

> *⚠️ Canon Guardians : les assignations 'Guardian' ci-dessous sont indicatives. Le roster faisant foi (6 membres : Star-Lord, Gamora, Rocket, Groot, Drax, Mantis) est défini dans `B3_Squad_Guardians/01_B3_AGENT_ROSTER.md`, aligné sur le canon Notion `AGENT_REGISTRY_DB`. En cas de divergence, le roster prime.*

C'est un cas de divergence entre canon manifest (`AGENTS.md`, liste abrégée à 4 membres) et roster Notion/Doctrine (4-10 membres). Le canon lui-même tranche : **le B3 roster prime**. Cette nuance est l'open architectural item flag dans `00_L2_FRACTAL_B1B2B3_ARCHITECTURE.md` §7.

## Le DoD auto-check

Chaque packet JTBD-001 finit par une checklist d'acceptance avec un item réservé :

> *DoD auto-check (Rock J01-B2-GROWTH-2026-01)*
> *- [x] ICP filter + critères de rejet · [x] VOC 5 pains (renvoi projets) · [x] 3 painkiller variants · [x] 1 experiment RICE + lead/lag · [x] proof = artefact inspectable · [x] zéro mutation externe · [ ] **Acceptance Superman***

L'item `[ ] Acceptance <Hero>` est la **signature du hero-manager B2** qui valide que le packet est prêt à être consommé par les Projects. Tant que cet item est unchecked, le packet n'est pas canonique. C'est la même logique que les gates (Gate 2 = Product, etc.).

## Pourquoi cette grammaire existe

Sans grammaire, chaque squad invente sa propre structure, les Projects ne savent pas quoi hériter, et la doctrine se dilue. Avec la grammaire, la **traversabilité** est possible : un agent peut lire n'importe quel JTBD-001 et savoir où trouver l'ICP, la VOC, les variants, l'experiment, et la signature d'acceptance.
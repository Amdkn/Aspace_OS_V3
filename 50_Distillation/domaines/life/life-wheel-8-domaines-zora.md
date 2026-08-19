---
type: Concept
title: Life Wheel 8 Domaines LD01-LD08 — Discovery/ZORA
description: Les 8 domaines canoniques de la Life Wheel, observés par ZORA sur Baserow. Chaque LD a un A3 crew, un horizon canon, et une règle dure.
tags: [life-wheel, zora, ld01-ld08, discovery, telemetry, 8-domaines]
generated: { by: minimax-m3, at: 2026-08-19T00:00:00Z }
verified:
  - { by: process:read_local_v2, at: 2026-08-19T00:00:00Z }
sources:
  - id: discovery-spec
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/22_Wheel_Discovery/A2_Discovery_ZORA_Spec.md
    title: A2 Discovery Spec — Crew + Horizons
    last_modified: 2026-05-20
  - id: discovery-readme
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/22_Wheel_Discovery/README.md
    title: 22_Wheel_Discovery README — Doctrine verrouillée
    last_modified: 2026-06-21
  - id: discovery-references
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/22_Wheel_Discovery/A3_Discovery_References_Index.md
    title: A3 Discovery References Index
    last_modified: 2026-05-20
okf_version: "0.2"
---

# Life Wheel 8 Domaines LD01-LD08 — Discovery/ZORA

La Life Wheel est le framework **équilibre** d'A'Space OS, géré par USS Discovery via ZORA (Baserow `LD00 Life Wheel Zora`). Huit domaines (LD01-LD08), chacun avec un A3 crew, un horizon canon, et une règle dure.

## Table canon des 8 LD

| LD | Domaine | A3 crew | Horizon canon | Règle dure |
|---|---|---|---|---|
| LD01 | Career & Business | **Book** | **H1** (weekly P&L) | Book reports to Discovery, NOT Morty |
| LD02 | Finance & Independence | **Saru** | **H3** (quarterly runway) | No paid/provider changes sans A0 approval |
| LD03 | Health, Sleep, Energy | **Hugh Culber** | **H10** (10-week cycle) | **HARD SAFETY** : RED = Beth veto automatic |
| LD04 | Mind, Cognition | **Sylvia Tilly** | **H30** (30-day learning) | **HARD SAFETY** : STOP authority |
| LD05 | Relations & Social | **Paul Stamets** | **H30** (network half-life) | Isolation RED = 1-turn escalation |
| LD06 | Love, Family, Presence | **Michael Burnham** | **H10** (family cycle) | Bond fracture RED = 1-turn escalation |
| LD07 | Creativity, Leisure | **Jett Reno** | **H10** (MVP build arc) | Joy starvation = slow poison |
| LD08 | Contribution, Impact | **Philippa Georgiou** | **H90** (quarterly legacy) | Negative-reach RED = 1-turn escalation |

## D3 nuance critique (corrigée 2026-06-21)

- **Saru = H3, PAS H1** ; **Book = H1, PAS H10**. Une lecture rapide pourrait inverser. Corrigé et verrouillé dans `book.twin.md` + `saru.twin.md`.
- "Life Wheel drift" = **Tilly (LD04 Cognition) + Spock (Areas)**, PAS Saru+Stamets (correction §15.1.4 du plan).

## HARD SAFETY (cascade LD03 → LD04)

LD03 RED = **Beth veto automatic** avant routage Morty. Règle dure canon — dégradation en cascade vers Tilly/LD04. Culber est primary gravity sensor de Life OS. Verbatim canon :

> *"LD03 is primary gravity: when it degrades, L4 cognition degrades in cascade."*
> — `A3_Culber_LD03_Spec.md`

Tilly = **STOP authority** si Culber LD03 RED. Cross-check obligatoire. PAS exécution sans recovery signal.

## Sortie ZORA canon

```yaml
ship: DISCOVERY
framework: Life Wheel / ZORA
domain: LD01|LD02|LD03|LD04|LD05|LD06|LD07|LD08
zora_state: GREEN|YELLOW|RED
load_signal: low|medium|high|critical
beth_action: none|review|veto|recovery_first
morty_route: ORVILLE_IKIGAI|SNW_12WY|ENTERPRISE_PARA|CERRITOS_GTD|PROTOSTAR_DEAL
evidence_paths:
  - C:\...
```

## Pattern canon strict

```
A0 (passif) → A1 Beth (Ikigai) → A2 Discovery (ZORA) → A3 twins agrégés
    ↓
Book H1 (weekly P&L) → Saru H3 (quarterly runway) → Burnham H10 (family cycle)
    ↓
Jerry Nexus J03 (FIP = Finance Independence + Presence stability) → escalade Beth si scarcity dominant
```

Verbatim canon (A2_Discovery_ZORA_Spec.md:66) : *"The A3 domain officers never compile final Discovery reports. They provide LD01-LD08 findings; Discovery/ZORA synthesizes."*

## AaaS 3 variants — mapping LDxx

| Variant AaaS | Ancre | Horizon | Statut Q3 2026 |
|---|---|---|---|
| **Solaris** (Civilisation Kardashev Type 3) | Book LD01 | H90 Legacy 1000T Solarpunk | ACTIF |
| **Nexus (OMK)** (Société Solarpunk) | Saru LD02 | H3 Indépendance financière | CLOS 2026-06-20 |
| **Orbiter (ABC)** (OS Family Offices) | Burnham LD06 | H10 Patrimoine baby-boomers | ACTIF |
| **[4e Dormant]** | Tilly/Culber | Réveil Q4 2026 / Q1 2027 | dormant |
---
type: Concept
title: Pipeline A0→A1→A2→A3 Discovery/ZORA
description: Pattern canon strict de la cosmologie A'Space OS appliquée à Life Wheel : A0 board observer passif → A1 Beth (veto Ikigai/Life Wheel/DEAL distribué) → A2 Discovery (ZORA synthesis) → A3 twins (narrow findings). A3 ne compile JAMAIS de rapport final Discovery.
tags: [pipeline, a0-a1-a2-a3, zora, narrow-findings, no-a3-compile, context-pack]
generated: { by: minimax-m3, at: 2026-08-19T04:14:00Z }
verified:
  - { by: process:read_local_v2, at: 2026-08-19T04:14:00Z }
sources:
  - id: discovery-spec
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/22_Wheel_Discovery/A2_Discovery_ZORA_Spec.md
    title: A2 Discovery Spec — A3 never compile final reports
    last_modified: 2026-06-21
  - id: beth-spec
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/00_Gatekeepers_Beth_Morty/A1_Beth_Spec.md
    title: A1 Beth Spec — Decision Rules
    last_modified: 2026-05-20
  - id: morty-spec
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/00_Gatekeepers_Beth_Morty/A1_Morty_Spec.md
    title: A1 Morty Spec — Context Pack 9 champs
    last_modified: 2026-05-20
okf_version: "0.2"
---

# Pipeline A0→A1→A2→A3 Discovery/ZORA

## Pattern canon strict

```
A0 board observer (passif)
    ↓ intention
A1 Beth (veto distribué 6 ships) — Ikigai + Life Wheel + DEAL = responsabilité principale
    ↓ filtres alignement Beth (GREEN/ORANGE/RED/HALT_LD03/HALT_LD04)
A2 Discovery (ZORA synthesis) — compile les 8 LD findings
    ↓ narrow findings narrow only
A3 twins (Book/Saru/Culber/Tilly/Stamets/Burnham/Reno/Georgiou) — domain findings
    ↓ routage Morty si GREEN
B1 Captains (Jerry × 4) ou B2/B3 squads
    ↓ exécution terrain (CC + A0 board observer)
```

Verbatim canon (`A2_Discovery_ZORA_Spec.md` ligne 66) :
> *"The A3 domain officers never compile final Discovery reports. They provide LD01-LD08 findings; Discovery/ZORA synthesizes the Life Wheel state and sends the result to Beth or Morty."*

## A3 ne compile JAMAIS

C'est la règle cardinale. Un A3 twin (Book, Saru, Culber, etc.) fournit des **narrow findings** sur SON domaine. **Il ne synthétise pas** l'état global Life Wheel.

Pourquoi : la séparation A2/A3 garantit la **traçabilité**. Si un A3 publiait un verdict Discovery, le pipeline A2 serait bypasse. Casser cette séparation = perdre la trace de la décision.

## Context Pack obligatoire (9 champs Morty)

Tout routage Morty nécessite un **Context Pack complet** :

```yaml
required_context_pack_fields:
  - ship                    # ORVILLE_IKIGAI / DISCOVERY_ZORA / SNW_12WY / ENTERPRISE_PARA / CERRITOS_GTD / PROTOSTAR_DEAL
  - crew_member             # Picard / Una / etc.
  - next_action             # Description verbeuse de l'action
  - framework               # Domain framework
  - domain_impact           # LDxx impacté
  - l0_skill_required       # Tech OS skill si nécessaire
  - beth_clearance          # GREEN/ORANGE/RED/HALT_LD03/HALT_LD04
  - evidence_paths          # Chemins de fichiers prouvant l'état
  - output_artifact         # Ce que Morty doit produire
```

Un champ manquant = `BLOCKED_CONTEXT_PACK_INCOMPLETE`. Source : `A1_Morty_Spec.md` + `A1_Beth_Spec.md`.

## Outputs ZORA Discovery

```yaml
ship: DISCOVERY
framework: Life Wheel / ZORA
domain: LD01|LD02|LD03|LD04|LD05|LD06|LD07|LD08
zora_state: GREEN|YELLOW|RED
load_signal: low|medium|high|critical
beth_action: none|review|veto|recovery_first
morty_route: ORVILLE_IKIGAI|SNW_12WY|ENTERPRISE_PARA|CERRITOS_GTD|PROTOSTAR_DEAL
evidence_paths: [C:\...]
```

## Routage Morty (matrice 6 ships)

Plan §3.6 matrice routage 20 intentions A0 mappées → A1 → A2 → A3 → frame → commande CC.

Morty route vers :
- **ORVILLE_IKIGAI** (Beth ship meaning) — Ikigai drift
- **DISCOVERY_ZORA** (Beth ship Life Wheel) — domain drift (notre vague)
- **SNW_12WY** (Pike ship execution) — 12WY Rocks
- **ENTERPRISE_PARA** (Picard ship structure) — Projects/Areas/Resources
- **CERRITOS_GTD** (Mariner ship chaos) — Inbox capture
- **PROTOSTAR_DEAL** (Dal ship liberation) — DEAL elimination

## HARD SAFETY cascade

LD03 RED ou LD04 RED → `beth_action = recovery_first` **AVANT** routing Morty.

C'est la seule exception au routage classique. Sans recovery signal, Morty ne route pas.

## Verdict distillation

`canon` — fait autorité. Source triple : A2 Discovery Spec + A1 Beth Spec + A1 Morty Spec. Verrouillé depuis 2026-05-20.

## Pièges documentés

- **Piège 1** : A3 twin publie un rapport "Discovery final". **Viole le canon**. Recadrage immédiat.
- **Piège 2** : Context Pack incomplet. **Bloqué**. Pas d'exécution.
- **Piège 3** : LD03 RED routé vers Morty avant Beth veto. **Viole HARD SAFETY**. Beth veto automatic d'abord.
- **Piège 4** : confusion entre "responsabilité principale" et "exclusivité". Beth = Ikigai+Life Wheel+DEAL est responsabilité principale ; veto distribué sur 6 ships.

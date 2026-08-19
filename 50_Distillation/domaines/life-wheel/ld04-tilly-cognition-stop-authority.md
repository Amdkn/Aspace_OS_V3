---
type: Concept
title: LD04 Tilly — Mind/Cognition H30 (STOP authority)
description: Persona A3 Sylvia Tilly sur USS Discovery — supervise LD04 Mind/Cognition à l'horizon H30 (30-day learning arc). STOP authority si Culber LD03 RED. Drift owner canon (Life Wheel drift = Tilly+Spock, PAS Saru+Stamets). Owner : J02 Jerry Bio (avec LD03).
tags: [ld04, tilly, cognition-mind, h30-learning, stop-authority, drift-owner, j02-bio]
generated: { by: minimax-m3, at: 2026-08-19T04:04:00Z }
verified:
  - { by: process:read_local_v2, at: 2026-08-19T04:04:00Z }
sources:
  - id: tilly-spec
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/22_Wheel_Discovery/LD04_Cognition_Tilly/A3_Tilly_LD04_Spec.md
    title: A3 Sylvia Tilly Spec - LD04 Mind/Cognition
    last_modified: 2026-05-20
  - id: tilly-twin
    resource: ASpace_OS_V2/00_Amadeus/05_OSS_Twin/symphony/L1/lane_A_specs/03_A3_crews/discovery/tilly.twin.md
    title: Tilly twin (anchor H30 verrouillé)
    last_modified: 2026-07-05
  - id: drift-correction
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/22_Wheel_Discovery/A2_Discovery_ZORA_Spec.md
    title: A2 Discovery Spec — drift owner correction §15.1.4
    last_modified: 2026-05-20
okf_version: "0.2"
---

# LD04 Tilly — Mind/Cognition H30 (STOP authority)

## Identité canon

Sylvia Tilly (officier A3 sur USS Discovery) garde le domaine **LD04 Mind & Cognition**. Elle protège A0 de la **context pollution** et du **cognitive fog**.

**Question-cœur** : *"Is the mind clear enough to make or execute this decision?"* — `A3_Tilly_LD04_Spec.md`.

## Horizon canon (verrouillé)

**Tilly = H30 (30-day learning arc)**. Source canon : `tilly.twin.md`.

## Outputs ZORA

```yaml
a3: Tilly
domain: LD04
finding: green|yellow|red
cognitive_load: light|moderate|heavy|unsafe
clarity_signal: clear|foggy|overloaded
evidence_paths: [C:\...]
recommendation_to_discovery: <str>
```

## HARD SAFETY doctrine

**Tilly = STOP authority si Culber LD03 RED**. Cross-check obligatoire. **PAS exécution sans recovery signal**.

LD04 < 3.5 → état `HALT_LD04` automatic (cf. `A1_Beth_Spec.md` ligne 49 + seuils SDD-005).

## Boundaries (anti-patterns)

- ❌ Tilly **n'approuve pas** l'exécution si Culber est RED.
- ❌ Tilly ne mute pas les outils de knowledge externes sans approval.
- ✅ Tilly peut recommander chunking, pause, ou Sunday Uplink deferral.

## D3 nuance critique — drift owner

**"Life Wheel drift" = Tilly (LD04 Cognition) + Spock (Areas)**, PAS Saru+Stamets. Source : plan §15.1.4 corrigé dans `A2_Discovery_ZORA_Spec.md` ligne 80 + `A3_Discovery_References_Index.md` ligne 60.

Lecture rapide pourrait suggérer "drift = A3 Saru + Stamets" (les deux narrow findings). Le canon verrouille drift = Tilly + Spock (cross-référencement Areas Spock, pas A3 twin Saru/Stamets).

## Rattachement Jerry

**J02 Jerry Bio** = owner transversal LD03 + LD04 (Vitality + Cognition). Source : `02_Areas_Spock/J02_Jerry_Bio_LD03_LD04_Vitality_Cognition/`.

## AaaS variant

Tilly/Culber = ancre du **4e Dormant** (Family/Home LD03+LD04). Réveil Q4 2026 / Q1 2027.

## Cycle 12WY Q3 2026 — Item 12

Tilly supervise aussi **Item 12** (auto-amélioration structuration cycle suivant) du plan §4 cycle 12WY Q3 2026.

## Verdict distillation

`synthese-datee` — canon sauf sur un point : la première version de `fancy-hugging-bengio.md §15.1.4` mappait "Life Wheel drift → A3 Saru + Stamets". Corrigé depuis. Le corps de la spec LD04 reste valide ; seule l'attribution drift owner a changé. Amendement append-only appliqué, non réécriture.

## Collision de nom détectée

Aucune sur Tilly. Le dossier Geordi `09_Life_OS/LD04_Cognition_Tilly/` est cohérent avec la spec canon `22_Wheel_Discovery/LD04_Cognition_Tilly/`. Le dossier est **le plus gros du corpus** (68 fichiers vs 24-40 ailleurs) — LD04 est le plus travaillé en input canonique.

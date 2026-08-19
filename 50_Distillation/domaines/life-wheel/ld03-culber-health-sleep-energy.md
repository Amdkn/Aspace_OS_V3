---
type: Concept
title: LD03 Culber — Health/Sleep/Energy H10 (HARD SAFETY)
description: Persona A3 Hugh Culber sur USS Discovery — supervise LD03 Health/Sleep/Energy à l'horizon H10. HARD SAFETY : LD03 RED = Beth veto automatic avant routing Morty. Primary gravity sensor de Life OS (cascade vers LD04). Owner : J02 Jerry Bio (avec LD04).
tags: [ld03, culber, health-sleep-energy, h10-cycle, hard-safety, primary-gravity, j02-bio]
generated: { by: minimax-m3, at: 2026-08-19T04:03:00Z }
verified:
  - { by: process:read_local_v2, at: 2026-08-19T04:03:00Z }
sources:
  - id: culber-spec
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/22_Wheel_Discovery/LD03_Health_Culber/A3_Culber_LD03_Spec.md
    title: A3 Hugh Culber Spec - LD03 Health/Sleep/Energy
    last_modified: 2026-05-20
  - id: culber-twin
    resource: ASpace_OS_V2/00_Amadeus/05_OSS_Twin/symphony/L1/lane_A_specs/03_A3_crews/discovery/culber.twin.md
    title: Culber twin (anchor H10 verrouillé)
    last_modified: 2026-07-05
  - id: sdd-005-thresholds
    resource: ASpace_OS_V2/10_Tech_OS/12_Blueprints/01-SDD/SDD-005_life-os-l1-integration.md
    title: SDD-005 Life OS L1 Integration (LD03 cascade)
    last_modified: 2026-05-20
  - id: beth-spec
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/00_Gatekeepers_Beth_Morty/A1_Beth_Spec.md
    title: A1 Beth Spec (HALT_LD03 state)
    last_modified: 2026-05-20
okf_version: "0.2"
---

# LD03 Culber — Health/Sleep/Energy H10 (HARD SAFETY)

## Identité canon

Dr. Hugh Culber (officier A3 sur USS Discovery) garde le domaine **LD03 Health, Sleep & Energy**. LD03 est **primary gravity** : quand il dégrade, **LD04 cognition dégrade en cascade**.

**Question-cœur** : *"Is the body recovered enough for the requested execution?"* — `A3_Culber_LD03_Spec.md`.

## Horizon canon (verrouillé)

**Culber = H10 (10-week health cycle)**. Source canon : `culber.twin.md`.

## Outputs ZORA

```yaml
a3: Culber
domain: LD03
finding: green|yellow|red
recovery_signal: sufficient|strained|unsafe
beth_halt_recommended: true|false
evidence_paths: [C:\...]
recommendation_to_discovery: <str>
```

## HARD SAFETY doctrine (règle dure canon)

**LD03 RED = Beth veto automatic avant routing Morty**. Domaine rule dure — dégradation en cascade vers Tilly/LD04. Culber est primary gravity sensor de Life OS.

Verbatim canon (plan §18.1) : *"HARD SAFETY : RED = Beth veto automatic"*.

Cascade vérifiée à chaque Sunday Uplink. Pas d'exécution sans recovery signal.

## Seuils chiffrés SDD-005

```yaml
beth_thresholds:
  LD03_minimum: 4.0
  LD04_minimum: 3.5
  multi_domain_alert: 3
```

LD03 < 4.0 → état `HALT_LD03` automatic (cf. `A1_Beth_Spec.md` ligne 49).

## Boundaries (anti-patterns)

- ❌ Culber **ne rapporte pas** de scores de santé sans evidence.
- ❌ Aucun L0 skill/workflow ne peut muter les jauges ZORA santé sans evidence Culber.
- ✅ Culber peut recommander HALT à Beth.

## Rattachement Jerry

**J02 Jerry Bio** = owner transversal LD03 + LD04 (Vitality + Cognition). Source : `02_Areas_Spock/J02_Jerry_Bio_LD03_LD04_Vitality_Cognition/`. Le canon mappe J02 ↔ Codex CLI (cf. plan §18.4).

## AaaS variant

Tilly/Culber = ancre du **4e Dormant** (Family/Home LD03+LD04). Réveil Q4 2026 / Q1 2027 — dormance intentionnelle pendant Q3 2026.

## Verdict distillation

`canon` — fait autorité, rien à signaler. Source triple : `A3_Culber_LD03_Spec.md` + twin vérifié + SDD-005 (cité verbatim). Le seuil chiffré 4.0 est verrouillé depuis 2026-05-20.

## Collision de nom détectée

Aucune sur Culber. Le dossier Geordi `09_Life_OS/LD03_Health_Culber/` est cohérent avec la spec canon `22_Wheel_Discovery/LD03_Health_Culber/`.

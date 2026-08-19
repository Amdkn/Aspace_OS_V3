---
type: Concept
title: 05_OSS_Twin vs 05_OSS_TSTwin — staging figé ≠ canon vivant
description: Décision 2026-07-03 de NE PAS hard-delete TSTwin. Twin = canon vivant (run-time), TSTwin = staging figé (précédente livraison avant L0 SDD + B1 Solaris loop). MD5 distincts.
tags: [twin, tstwin, staging, canon, evolution, 2026-07-03]
generated: { by: minimax-m3, at: 2026-08-19 }
verified:
  - { by: process:lecture_v2, at: 2026-08-19 }
sources:
  - id: ALIGNMENT_TSTwin_Twin
    resource: 20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/00_Amadeus/_ALIGNMENT_TSTwin_Twin_2026-07-03.md
    title: ⚡ÉVOLUTION 2026-07-03 — TSTwin ≠ Twin
    last_modified: 2026-07-03
okf_version: "0.2"
---

# 05_OSS_Twin vs 05_OSS_TSTwin — staging figé ≠ canon vivant

## Énoncé (D1 verdict 2026-07-03)

`05_OSS_TSTwin` et `05_OSS_Twin` ne sont **PAS la même version**.
- TSTwin md5 (INDEX_capsules.md) : `270e1fbfdbcc7a3409408e1bc8c9217b`
- Twin md5 (INDEX_capsules.md) : `7c9a56875cfbcbe4c76a0f639aaa9f74`

## Action GO A0

**TRASH annulé.** TSTwin et Twin sont deux artefacts distincts volontairement conservés.

## Ce que Twin contient en exclusivité

- `L0/open-hermes-runtime.md`, `L0/SDD-010_shadow-L0-IA.md`, `L0/shadow-ai-capability-routing.md`
- `L2/symphony-airtable.spec.md` + WORKFLOW.solaris-* / WORKFLOW.growth-* / symphony-clickup.spec.md / symphony-notion.spec.md / symphony-sheets.spec.md
- `loops/b1-solaris-loop.draft.md`
- `scripts/symphony-tick-demo.{ps1,sh}`, `scripts/symphony-ui-server.py`, `scripts/ui`
- `agent-os/.claude/commands/agent-os/{discover,index,inject,plan,shape}-standards.md`
- `BRIDGE.rock-l2-to-growth.draft.md`

## Conventions

- **TSTwin** = staging figé (précédente livraison avant L0 SDD + B1 Solaris loop)
- **Twin** = canon vivant
- TSTwin sert de **miroir archivé** pour rollback ponctuel
- Twin est la source canonique des L0/L1/L2
- **Les opérations d'écriture symphony → Twin uniquement**

## Pourquoi ce n'est pas un doublon

Examinés naïvement, les deux dossiers se ressemblent (560 fichiers combinés = 74 % de la couche). Mais le pattern Twin/TSTwin = **staging/canon** est un pattern de release engineering, pas un dédoublement accidentel. Hard-delete TSTwin = perdre la capacité de rollback vers les capsules de référence (bkp prod).

## Conséquence pour les frères Tennant

- **REVERSE** : ne pas TRASH TSTwin — même s'il contient 277 fichiers apparemment obsolètes
- **NO_HARD_DELETE** : appliqué ici sur des artefacts de release engineering
- **Append-only rollover** : chaque release Twin fait grossir; TSTwin gèle

## Note méthodo

Le `README.md` de `05_OSS_Twin` est un placeholder littéral : "OSS Twin - Placeholder". Le README de `V2_OSS_Twin.md` est aussi "V2 OSS Twin - Placeholder". Ces placeholders ne sont PAS canoniques — ce sont des artefacts attendant un README complet. Le contenu canonique vit dans `symphony/`. Cette inconsistance est un signal que le dossier Twin attendait qu'un agent écrive l'index métier.

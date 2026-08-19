---
type: Concept
title: PRD-orphelin antigravity-kit-fusion — le PRD sans miroir
description: antigravity-kit-fusion_PRD.md est le seul PRD Legacy qui n'a pas de miroir dans TOTAL_Spec/PRD/. Il vit uniquement dans _SPECS/prds/ — un orphelin du dossier lowercase, qui pose la question de son statut canonique.
tags: [prd, orphelin, antigravity-kit-fusion, lowercase-prds, mirror-asymmetrique]
generated: { by: minimax-m3, at: 2026-08-19T15:35:00Z }
verified:
  - { by: process:lecture_concepts_archives, at: 2026-08-19T15:35:00Z }
sources:
  - id: prd-antigravity-direct
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/04_Archives_Data/Legacy_LifeOS_App_Specs_2026-05-22/_SPECS/prds/antigravity-kit-fusion_PRD.md"
    title: antigravity-kit-fusion_PRD.md (lu directement)
    last_modified: 2026-05-22
okf_version: "0.2"
---

# PRD-orphelin antigravity-kit-fusion — le PRD sans miroir

## Le constat d'asymétrie

`antigravity-kit-fusion_PRD.md` vit **uniquement** dans
`_SPECS/prds/` (lowercase). Il **n'a pas de pendant** dans
`TOTAL_Spec/PRD/`. Tous les autres 44 PRD V0.x ont leur miroir dans
TOTAL_Spec.

| Source | Présence |
|---|---|
| `_SPECS/prds/antigravity-kit-fusion_PRD.md` | ✅ |
| `TOTAL_Spec/PRD/antigravity-kit-fusion_PRD.md` | ❌ |
| `04_From_V2_Root/_Life-OS-2026-clone/openspec/changes/TOTAL_Spec/PRD/` | ❌ |
| `04_From_V2_Root/_Life-OS-2026-clone/openspec/changes/TOTAL_Spec/prds/` | ❌ |

## Verdict

**orphelin** — le document existe, mais son statut canonique ne peut
pas être établi par miroir. Le format lowercase (vs majuscule
`PRD/`) confirme qu'il a été classé dans le **dossier de bord** (le
portrait horizontal `_SPECS/prds/`), pas dans le **portrait
d'archive** (la verticale TOTAL_Spec).

Trois issues possibles :

1. **Canon local** : le PRD est canon dans `_SPECS/prds/`, et le
   dossier TOTAL_Spec n'a jamais été mis à jour pour l'inclure.
2. **Spécificité V0.x tardive** : ajouté après le scellé, jamais
   resynchronisé dans TOTAL_Spec.
3. **Branche morte** : doc de travail, jamais promu canon.

## Source du décompte

`find .../Legacy_LifeOS_App_Specs_2026-05-22/_SPECS/prds/` →
45 fichiers (44 V0.x + 1 antigravity).
`find .../Legacy_LifeOS_App_Specs_2026-05-22/TOTAL_Spec/PRD/` →
44 fichiers (aucun antigravity).

## Concepts liés

- [[concept-prd-chain-v0x-legacy]] — la chaîne parente.

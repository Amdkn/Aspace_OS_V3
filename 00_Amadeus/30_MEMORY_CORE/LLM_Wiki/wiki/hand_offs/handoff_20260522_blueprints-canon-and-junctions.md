---
source: backfilled 2026-06-06 (hygiene lint remediation)
date: 2026-05-22
type: handoff
domain: handoff
title: Handoff — Canon Blueprints + Junctions Aliasing
tags: [#handoff #hand_offs #backfilled]
---

# Handoff — Canon Blueprints + Junctions Aliasing

**Date :** 2026-05-22
**Émetteur :** A2 Claude Code
**Destinataires :** A2 Codex / A2 Gemini / A3 agents d'exécution
**Statut :** PRÊT pour exécution étape B (script junctions) et étape C/migration `_SPECS`

## Contexte ratifié

Deux ADRs viennent d'être ratifiés :

1. **`ADR-FWK-021`** — Canon Tripartite Blueprints L0/L1/L2 → `10_Tech_OS\12_Blueprints\02-ADR\`
2. **`ADR-FS-001`** — Junction-Based Aliasing → `10_Tech_OS\12_Blueprints\02-ADR\`

Dossiers canoniques créés :
- `10_Tech_OS\12_Blueprints\{02-ADR, 03-PRD, 04-DDD}\`
- `20_Life_OS\28_Blueprints\{01-SDD, 02-ADR, 03-PRD, 04-DDD}\`
- `30_Business_OS\09_Blueprints\{01-SDD, 02-ADR, 03-PRD, 04-DDD}\`
- `_SPECS\_INBOX\`

Junction réparée : `30_Business_OS\00_Links\alykaly-front` → `PARA\…\03_Product_Flash_Avengers\alykaly-front`

## Tâches ouvertes

### TASK 1 — ADR-FS-002 : script `Setup-ASpace-Junctions.ps1` (étape B)

Spec : créer 9 junctions sentinelles à la racine `ASpace_OS_V2\_\` :

```
biz → 30_Business_OS
para → 20_Life_OS\24_PARA_Enterprise
proj → PARA\01_Projects_Picard
area → PARA\02_Areas_Spock
res → PARA\03_Resources_Geordi
arch → PARA\04_Archives_Data
snw → 20_Life_OS\23_12WY_SNW
gtd → 20_Life_OS\25_GTD_Cerritos
deal → 20_Life_OS\26_DEAL_Protostar
```

Exigences :
- Idempotent (skip si junction existe et target correct)
- Dry-run par défaut, `-Apply` pour exécuter
- Audit (`-Audit`) qui liste toutes les junctions du tree et flag les broken
- Export PowerShell profile snippet pour `$env:ASPACE_*` + `subst B:` `P:`
- Logs vers `Shadow_L0\junctions-setup-YYYYMMDD.log`

Localisation script proposée : `10_Tech_OS\11_Scripts\Setup-ASpace-Junctions.ps1` (à confirmer avec A0)

### TASK 2 — ADR-FWK-022 : migration `_SPECS\` vers L0/L1/L2

Spec : produire mapping détaillé fichier-par-fichier des ~50 fichiers `_SPECS\` (ADR, SDD, PRD, DDD, plats racine) → leur canon de destination (L0/L1/L2), avec `git mv` ou robocopy + nettoyage. Inclut :

- Fusion `ADR/` + `adrs/` minuscule
- Fusion `PRD/` + `prds/` + `02_V1_PRD/`
- Promotion des SDDs racine vers `SDD/` puis routage L0/L1/L2
- Renommage selon convention `<TYPE>-<NAMESPACE>-<NNN>_<kebab>.md` si non conforme

### TASK 3 — Décision `00_Jerry_Business_Pulse\`

`30_Business_OS\00_Jerry_Business_Pulse\` est actuellement un dossier réel.
`20_Life_OS\24_PARA_Enterprise\02_Areas_Spock\Business_Pulse\` est aussi un dossier réel.

Question pour A0 : lequel des deux est la **source de vérité** ? L'autre doit devenir junction selon ADR-FS-001. Probable : PARA/Spock owner, Business_OS/Jerry junction.

## Références canon

- `10_Tech_OS\12_Blueprints\02-ADR\ADR-FWK-021_blueprints-canon-tripartite.md`
- `10_Tech_OS\12_Blueprints\02-ADR\ADR-FS-001_junction-based-aliasing.md`
- `Shadow_L0\02_blueprints-canon-tripartite-20260522.md`
- `Shadow_L1\06_blueprints-canon-l1-impact-20260522.md`
- `Shadow_L2\07_blueprints-canon-l2-impact-20260522.md`
- Entities : [[entity_adr_fwk_021]], [[entity_adr_fs_001]]

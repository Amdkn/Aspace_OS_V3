---
type: Concept
title: Junction-based aliasing — un owner, N vues
description: Architecture filesystem souveraine via NTFS Junctions (mklink /J). Trois couches : sentinelles `_\`, drives subst, junctions fonctionnelles. Aucune copie.
tags: [tech, filesystem, junctions, aliases, windows]
generated: { by: minimax-m3, at: 2026-08-19T12:00:00Z }
verified:
  - { by: process:read, at: 2026-08-19T12:00:00Z }
sources:
  - id: adr-fs-001
    resource: 05_From_V2_Domains/10_Tech_OS/12_Blueprints/02-ADR/ADR-FS-001_junction-based-aliasing.md
    title: ADR-FS-001 Junction-Based Aliasing
    last_modified: 2026-05-22
  - id: adr-fs-002
    resource: 05_From_V2_Domains/10_Tech_OS/12_Blueprints/02-ADR/ADR-FS-002_setup-junctions-script.md
    title: ADR-FS-002 Script Setup-ASpace-Junctions.ps1
    last_modified: 2026-05-22
  - id: adr-fs-003
    resource: 05_From_V2_Domains/10_Tech_OS/12_Blueprints/02-ADR/ADR-FS-003_business-os-sub-junctions-transverse.md
    title: ADR-FS-003 Sub-Junctions Business OS Links
    last_modified: 2026-05-22
okf_version: "0.2"
---

L'architecture filesystem souveraine repose sur **3 couches d'aliasing NTFS**, jamais sur la copie.

## Problème résolu

Sans aliasing :
- Chemins très longs (`...\24_PARA_Enterprise\01_Projects_Picard\04 Alikaly Bana Holding to LLC\B2_Business_Domains\03_Product_Flash_Avengers\02_alykaly-os-v2\` = 143 caractères).
- Risque de drift par `robocopy /MIR` 2-way.
- Agents A3 perdus entre Business OS et PARA pour un même dossier.

## Couche 1 — Sentinelles racine `_\`

Création à la racine `ASpace_OS_V2\` d'un dossier `_\` (trié en haut, agent-friendly) :

```
ASpace_OS_V2\_\
├── biz\    → 30_Business_OS\
├── para\   → 20_Life_OS\24_PARA_Enterprise\
├── proj\   → 24_PARA_Enterprise\01_Projects_Picard\
├── area\   → 24_PARA_Enterprise\02_Areas_Spock\
├── res\    → 24_PARA_Enterprise\03_Resources_Geordi\
├── arch\   → 24_PARA_Enterprise\04_Archives_Data\
├── snw\    → 20_Life_OS\23_12WY_SNW\
├── gtd\    → 20_Life_OS\25_GTD_Cerritos\
└── deal\   → 20_Life_OS\26_DEAL_Protostar\
```

Gain : `…\_\proj\` = 38 caractères vs 70+. Le Canon reste à sa place — `_\` n'est qu'une **vue**.

## Couche 2 — Drives PowerShell (`subst`)

Pour les outils CLI/agents, lettres de drive :

```powershell
subst B: C:\Users\amado\ASpace_OS_V2\30_Business_OS
subst P: C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise
```

Persistance via profil PowerShell + variables d'env portables (`$env:ASPACE_ROOT`, `$env:ASPACE_BIZ`, etc.).

## Couche 3 — Junctions fonctionnelles Business OS ↔ PARA

| Contenu | Source de vérité | Vue (junction) |
|---------|------------------|----------------|
| Projects B3 | `PARA\01_Projects_Picard\<projet>\…\` | `30_Business_OS\<secteur>\<repo>` |
| Areas B2 | `PARA\02_Areas_Spock\Business_Pulse\` | `30_Business_OS\00_Jerry_Business_Pulse\` |
| Resources B3 | `PARA\03_Resources_Geordi\` | `30_Business_OS\00_Links\res\` |
| Archives | `PARA\04_Archives_Data\` | `30_Business_OS\00_Links\arch\` |

## Règles d'or

1. **Chaque dossier n'a qu'UN propriétaire réel.** L'autre côté est toujours une junction. Aucune copie, aucun robocopy, aucun rsync 2-way.
2. **NTFS Junctions uniquement** (`mklink /J`). Symlinks (`mklink /D`) interdits sauf cross-volume justifié.
3. **`node_modules` jamais junctionnés** — watchers cassent.
4. **Variables d'environnement portables** : `$env:ASPACE_*` partout, jamais de chemin hardcodé.

## Audit

Le script `Setup-ASpace-Junctions.ps1` est **idempotent, dry-run par défaut**, supporte `-Apply`, `-Audit`, `-InstallProfile`. Audit initial 2026-05-22 : 37 junctions (toutes OK, 0 broken).

Voir aussi : [[mcp-doctrine-six]], [[vault-tier-pattern]], [[caste-doctor-who]].
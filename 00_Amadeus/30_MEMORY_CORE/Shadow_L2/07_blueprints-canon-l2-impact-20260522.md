# Shadow L2 — Impact Canon Blueprints sur Business OS

**Date :** 2026-05-22
**Niveau :** L2 Business OS (Fractal — Jerry & Summer)
**Source doctrinale :** `Shadow_L0\02_blueprints-canon-tripartite-20260522.md`

## Ce qui change pour L2

- Nouveau canon Blueprints : `30_Business_OS\09_Blueprints\` (créé vide)
- Structure : `01-SDD/ 02-ADR/ 03-PRD/ 04-DDD/`
- `00_Links\` reste le hub d'aliasing officiel — pattern existant validé
- 1 junction cassée corrigée : `00_Links\alykaly-front` repointée vers PARA (Next.js app réelle)

## Architecture confirmée (ADR-FS-001)

| Source de vérité | Vue côté Business OS |
|------------------|----------------------|
| `PARA\01_Projects_Picard\<projet>\…\<repo>\` | `<secteur>\<repo>` (junction par projet) |
| `PARA\02_Areas_Spock\Business_Pulse\` | `00_Jerry_Business_Pulse\` (à confirmer junctionnage) |
| `PARA\03_Resources_Geordi\` | `00_Links\res\` (junction unique) |
| `PARA\04_Archives_Data\` | `00_Links\arch\` (junction unique) |
| `20_Life_OS\23_12WY_SNW\` | `00_Links\snw\` (junction unique) |
| `20_Life_OS\25_GTD_Cerritos\` | `00_Links\gtd\` (junction unique) |
| `20_Life_OS\26_DEAL_Protostar\` | `00_Links\deal\` (junction unique) |

## Documents L2 à migrer (depuis `_SPECS\`)

À traiter en ADR-FWK-022 :

- `ADR-MCP-001_god-mode-cli-stack.md`
- `ADR-MEM-001_IndexedDB-Cloisonne-LD01-LD08.md`
- `ADR-NET-001_Hebergement-Multi-Couche.md`
- `ADR-AGKIT-001_Industrial_Fusion.md` (dans `adrs/` minuscule — à corriger)
- `ADR-ALA-001_ALA_Standard.md`, `ADR-ALA-002_ALA_Implementation_Resiliency.md`
- DDDs AGKIT-101..103
- SDD-006 (Business Pulse L2 Pyramide), SDD-007 (SOB Factory ICP), SDD-009 (Shadow L2 Business OS)

## Junctions à créer (couche 1 ADR-FS-001)

Pas encore créées — relèvent du script `Setup-ASpace-Junctions.ps1` (étape B). Cibles :

- `ASpace_OS_V2\_\biz\`, `_\para\`, `_\proj\`, `_\area\`, `_\res\`, `_\arch\`, `_\snw\`, `_\gtd\`, `_\deal\`

## Suivi

- Décider si `00_Jerry_Business_Pulse\` doit devenir junction vers `PARA\02_Areas_Spock\Business_Pulse\` (actuellement dossier réel — il y a redondance probable)
- Migration `_SPECS\` → `09_Blueprints\` (ADR-FWK-022)
- Exécution script junctions racine `_\` (ADR-FS-002)

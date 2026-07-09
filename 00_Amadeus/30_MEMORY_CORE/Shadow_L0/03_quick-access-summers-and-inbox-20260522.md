# Shadow L0 — Quick Access Summers Verse + Pattern `_Inbox` + Archivage Legacy Specs

**Date :** 2026-05-22
**Niveau :** L0 Tech OS
**Source doctrinale :** `12_Blueprints\02-ADR\ADR-FWK-022_quick-access-summers-and-inbox-pattern.md`

## Décisions clés

1. **`_SPECS\` + `TOTAL_Spec\` archivés** dans `PARA\04_Archives_Data\Legacy_LifeOS_App_Specs_2026-05-22\` — c'étaient des artefacts de développement d'une app Life OS abandonnée, remplacée structurellement par Shadow_L1 + Shadow_L2 + SDDs Tech_OS.
2. **Source de Vérité Business Pulse confirmée** : `PARA\02_Areas_Spock\J01_Jerry_Prime_LD01_Business\`. `30_Business_OS\` = Quick Access Layer (vue), jamais propriétaire.
3. **ADR-FWK-021 amendé** sur la mention `_SPECS\_INBOX\` (zone n'existe plus). Le reste de la doctrine tripartite L0/L1/L2 reste valide.

## Actions exécutées

| # | Action | Statut |
|---|--------|--------|
| 1 | Archive `_SPECS\` → `PARA\04_Archives_Data\Legacy_LifeOS_App_Specs_2026-05-22\_SPECS\` | OK |
| 2 | Archive `TOTAL_Spec\` → idem | OK |
| 3 | Rename 7 secteurs Business OS (mapping Marvel/DC squads aligné PARA J01) | OK |
| 4 | Robocopy `/MOVE` 04_Product_Flash racine → `04_Business_Domains\04_Product_Flash` | EN COURS (background, log `robocopy-product-flash-20260522.log`) |
| 5 | Create `30_Business_OS\00_Summers_QuickAccess\` + 6 junctions vers Picard | OK |
| 6 | Create `_Inbox\` (avec B1/B2/B3 junctions) dans 6 projets Picard | OK |
| 7 | Write ADR-FWK-022 | OK |
| 8 | Amend ADR-FWK-021 (note SUPERSEDED partial) | OK |

## Audit junctions final

Junctions créées dans cette opération :
- `30_Business_OS\00_Summers_QuickAccess\{00_Agency_aaS, 01_OMK_BOS, 02_ABC_OS, 03_RILCOT, 04_Alikaly, 05_Marina}` (6)
- `PARA\Picard\<projet>\_Inbox\{B1, B2, B3}` × 6 projets (18)
- Junctions préexistantes : 4 (dont `alykaly-front` corrigée 2026-05-22)

Total junctions Business_OS + Picard = 28

## Suivi

- **ADR-FWK-023** : fusion contenu `04_Business_Domains\<secteur>\` (Business OS) → `J01\B2_Area_Domains\<same-name>\` (PARA SoT), puis junctions
- **ADR-FS-002** : script `Setup-ASpace-Junctions.ps1` (étape B initiale)
- **Post-robocopy** : confirmer move complet `04_Product_Flash`, renommer en `03_Product_Flash_Avengers`, supprimer source racine si vide

## Références

- `12_Blueprints\02-ADR\ADR-FWK-022_quick-access-summers-and-inbox-pattern.md`
- Shadow_L1 : `07_para-source-of-truth-confirmed-20260522.md`
- Shadow_L2 : `08_business-os-quick-access-and-rename-20260522.md`

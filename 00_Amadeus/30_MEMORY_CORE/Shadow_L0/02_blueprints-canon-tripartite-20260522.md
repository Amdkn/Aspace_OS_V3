# Shadow L0 — Canon Tripartite des Blueprints + Junction Aliasing

**Date :** 2026-05-22
**Auteur :** A2 Claude Code (Architecte) sous mandat A0 Amadeus
**Niveau :** L0 Tech OS (Rick's Verse)
**Type :** Décision doctrinale ratifiée

## Résumé

Deux ADRs ratifiés simultanément, ancrés sur `AGENTS.md` + ADR-007 :

1. **ADR-FWK-021** — Canon Tripartite des Blueprints (L0/L1/L2)
2. **ADR-FS-001** — Junction-Based Aliasing for Short-Path Agent Operability

Localisation canon : `C:\Users\amado\ASpace_OS_V2\10_Tech_OS\12_Blueprints\02-ADR\`

## Décisions clés (L0)

- `_SPECS\` deprecated comme canon → devient `_SPECS\_INBOX\` (zone brouillons)
- Chaque niveau a son canon Blueprints isomorphe : `12_Blueprints\` (L0) · `28_Blueprints\` (L1) · `09_Blueprints\` (L2)
- Structure interne identique : `01-SDD/`, `02-ADR/`, `03-PRD/`, `04-DDD/`
- Convention nommage immuable : `<TYPE>-<NAMESPACE>-<NNN>_<kebab-case>.md`
- NTFS Junctions = seul mécanisme d'aliasing autorisé (jamais robocopy 2-way)
- Trois couches d'aliasing : sentinelles racine `_\`, drives subst (B:/P:), junctions sectorielles Business OS ↔ PARA

## Audit junctions (initial)

| # | Source | Cible | Statut |
|---|--------|-------|--------|
| 1 | `PARA\00_Links\30_Business_OS_Portal` | `30_Business_OS\` | OK |
| 2 | `30_Business_OS\00_Links\20_Life_OS_PARA_Portal` | `PARA\` | OK |
| 3 | `30_Business_OS\00_Links\02_alykaly-os-v2` | `PARA\…\02_alykaly-os-v2` | OK |
| 4 | `30_Business_OS\00_Links\alykaly-front` | (avant) self-ref CASSEE → (après) `PARA\…\alykaly-front` | **CORRIGEE** |

## Actions prises

1. Junction #4 réparée (delete + recreate vers PARA Next.js app)
2. Dossiers Blueprints L0/L1/L2 créés (vides, prêts à recevoir migration)
3. `_SPECS\_INBOX\` créé (zone brouillons)
4. ADR-FWK-021 + ADR-FS-001 écrits dans `12_Blueprints\02-ADR\`

## Suivi requis

- **ADR-FWK-022** (à venir) : plan de migration des 50+ fichiers `_SPECS\` vers L0/L1/L2
- **ADR-FS-002** (à venir) : script `Setup-ASpace-Junctions.ps1` (étape B de la commande A0)
- Audit junctions à reprogrammer après création couche 1 (sentinelles `_\`)

## Références

- `10_Tech_OS\12_Blueprints\02-ADR\ADR-FWK-021_blueprints-canon-tripartite.md`
- `10_Tech_OS\12_Blueprints\02-ADR\ADR-FS-001_junction-based-aliasing.md`
- Shadow_L1 : `06_blueprints-canon-l1-impact-20260522.md`
- Shadow_L2 : `07_blueprints-canon-l2-impact-20260522.md`

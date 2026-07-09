# Shadow L2 — Notion Back Office Bootstrap (Solaris Prototype)

**Date :** 2026-05-26
**Niveau :** L2 Business OS (Fractal — Jerry & Summer)
**Source doctrinale :** `30_Business_OS\09_Blueprints\02-ADR\ADR-NOTION-001_back-office-solaris-template.md`

## Décisions ratifiées

1. **Workspace unique** `Business Pulse ∞ AMADEUS` (auth MCP persistée 2026-05-26 03:38)
2. **Solaris = prototype canonique** — template clonable v1.0 vers 5 autres projets Picard
3. **Architecture 5 sections** par projet (HQ Dashboard, SOPs TVR, Hall Agents, Catalogue Produits, Coffre Légal)
4. **MASTER_SOP_DB** schema immuable 14 propriétés (cf. ADR § D4)
5. **8 portails domaines** alignés PARA J01 Marvel/DC (pas de re-naming)
6. **Pipeline** : Airtable (CRM) → Notion (SOP) → ClickUp (Action), bus = Symphony (pas N8N)
7. **Doctrine Cuisine/Salle** confirmée : Notion = back office Amadeus, client final voit l'App Next.js+Supabase

## État pré-bootstrap

- Workspace : `Business Pulse ∞ AMADEUS` (créé antérieurement, vide ou quasi)
- MCP Notion : OAuth tokens persistés, refresh_token valide
- Airtable Shadow_L2 : structuré antérieurement par A0
- ClickUp Shadow_L2 : structuré antérieurement par A0
- Notion : **vierge** (procrastination documentée)

## Mapping 8 Portails Domaines ↔ PARA J01

| Notion Portal | Owner B2 | Squad B3 | PARA J01 Path |
|---------------|----------|----------|---------------|
| 01_Growth | Superman | Guardians | `J01\B2_Area_Domains\01_Growth_Superman_Guardians` |
| 02_Sales | John Jones | Illuminati | `…\02_Sales_MartianManhunter_Illuminati` |
| 03_Product | Flash | Avengers | `…\03_Product_Flash_Avengers` |
| 04_Ops | Batman | Fantastic4 | `…\04_Ops_Batman_Fantastic4` |
| 05_IT | Cyborg | KangDynasty | `…\05_IT_Cyborg_KangDynasty` |
| 06_Finance | Wonder Woman | Thunderbolts | `…\06_Finance_WonderWoman_Thunderbolts` |
| 07_People | Green Lantern | XMen | `…\07_People_GreenLantern_XMen` |
| 08_Legal | Aquaman | Eternals | `…\08_Legal_Aquaman_Eternals` |

## Plan d'action Phase 1 (Solaris)

| Étape | Durée | Outil |
|-------|-------|-------|
| 1. Top-level page `Solaris HQ` | 5 min | Notion UI ou MCP `notion-create-pages` |
| 2. `MASTER_SOP_DB` (14 props) | 30 min | MCP `notion-create-database` |
| 3. 8 portails domaines (Linked Views) | 30 min | Notion UI (Linked DB blocks) |
| 4. `AGENT_REGISTRY_DB` | 15 min | MCP `notion-create-database` |
| 5. 3 SOPs P0 test (Ops, Sales, Finance) | 1h | Manuel |

## Dépendances ouvertes

- **ADR-SYMPH-001** (à venir) : sans Symphony, Notion ne se sync pas avec Supabase. Phase 1 reste fonctionnelle en isolation.
- **Audit Solaris stable** : critères pour bump `Template_Version: 1.0-stable` à définir avec Jerry (B1)

## Risque tracé

A0 procrastine depuis avril 2025 sur Notion alors que la doctrine est claire dans le Takeout. **Cause probable** : SaaSpocalypse (cf. Takeout `2026-05-25:15662` — "te parler de Notion, ClickUp ou Airtable en pleine SaaSpocalypse est une hérésie"). A0 et Gemini se sont eux-mêmes auto-démotivés sur ces outils SaaS.

**Antidote 2026-05-26** : Notion n'est pas l'infrastructure souveraine — c'est l'outil de rédaction. Les SOPs **vivent** ensuite dans Supabase (App Client) une fois sync. Notion = brouillon riche, pas canon final. Cette nuance débloque la procrastination.

## Références

- ADR-NOTION-001 (canon)
- ADR-FWK-022 (rename Marvel/DC)
- ADR-FS-001 (junctions)
- Gemini Takeout 2026-05 (matière doctrinale)

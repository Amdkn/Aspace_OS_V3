# Shadow L1 — Impact Canon Blueprints sur Life OS

**Date :** 2026-05-22
**Niveau :** L1 Life OS (Fleet — Beth & Morty)
**Source doctrinale :** `Shadow_L0\02_blueprints-canon-tripartite-20260522.md`

## Ce qui change pour L1

- Nouveau canon Blueprints : `20_Life_OS\28_Blueprints\` (créé vide)
- Structure : `01-SDD/ 02-ADR/ 03-PRD/ 04-DDD/`
- Junctions PARA ↔ Business OS reconnues : ce sont des aliases, **PARA reste propriétaire** des Projects/Areas/Resources/Archives
- 12WY_SNW, GTD_Cerritos, DEAL_Protostar : exposés à L2 via 3 junctions uniques (`00_Links\snw\`, `\gtd\`, `\deal\`), pas par secteur DC

## Documents L1 à migrer (depuis `_SPECS\`)

À traiter en ADR-FWK-022 :

- `ADR-FWK-012_PARA_Structure.md`
- `ADR-FWK-013_Ikigai_Structure.md`
- `ADR-FWK-014_LifeWheel_Structure.md`
- `ADR-FWK-015_12WY_Structure.md`
- `ADR-FWK-016_GTD_Structure.md`
- `ADR-FWK-017_DEAL_Structure.md`
- `ADR-V0.2.4_UILayout.md`, `ADR-V0.2.5_IkigaiDeep.md`, `ADR-V0.2.6_PARAComplete.md`
- PRDs `prds/PRD-V0.2.6..V0.2.9` (PARA, 12WY, GTD, DEAL)
- SDD-005 (`shadow-L1-life-os.md` côté L0 — à clarifier le routage)

## Conséquence PARA

PARA/Enterprise est **confirmée Source de Vérité** pour :
- Projects (Picard) — owner exclusif des B3 actifs
- Areas (Spock) — owner exclusif du Business_Pulse top-level
- Resources (Geordi) — owner exclusif templates/SOPs partagés
- Archives (Data) — owner exclusif des artefacts gelés

Business OS ne possède **rien** de ces 4 catégories — il les **expose** via junctions.

## Suivi

- Confirmer routage SDD-005 (côté L0 actuellement, contenu L1 ?)
- Migration `_SPECS\` → `28_Blueprints\` (ADR-FWK-022)

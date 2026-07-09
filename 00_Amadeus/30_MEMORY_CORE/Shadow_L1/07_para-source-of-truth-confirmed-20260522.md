# Shadow L1 — PARA confirmée Source de Vérité Universelle

**Date :** 2026-05-22
**Niveau :** L1 Life OS (Fleet — Beth & Morty)
**Source doctrinale :** `12_Blueprints\02-ADR\ADR-FWK-022_quick-access-summers-and-inbox-pattern.md`

## Confirmations majeures pour L1

1. **PARA est Source de Vérité Universelle** pour Projects, Areas, Resources, Archives
2. **Business Pulse SoT** = `02_Areas_Spock\J01_Jerry_Prime_LD01_Business\` (pas `30_Business_OS\`)
3. **Pattern `_Inbox\` dans projets Picard** = nouvelle convention pour short-path agents/scripts

## Structure J01_Jerry_Prime_LD01_Business (canon Business Pulse)

```
J01_Jerry_Prime_LD01_Business\
├── B1_Area_Direction\
├── B2_Area_Domains\         ← Les 8 secteurs Marvel/DC (canon noms longs)
│   ├── 01_Growth_Superman_Guardians\
│   ├── 02_Sales_MartianManhunter_Illuminati\
│   ├── 03_Product_Flash_Avengers\
│   ├── 04_Ops_Batman_Fantastic4\
│   ├── 05_IT_Cyborg_KangDynasty\
│   ├── 06_Finance_WonderWoman_Thunderbolts\
│   ├── 07_People_GreenLantern_XMen\
│   └── 08_Legal_Aquaman_Eternals\
├── B3_Area_Warp_Core\
└── 12WY_Area_Cadence\
```

`30_Business_OS\00_Jerry_Business_Pulse\04_Business_Domains\` doit refléter ces noms (alignement effectué 2026-05-22).

## Pattern `_Inbox` ratifié

Chaque projet Picard reçoit `_Inbox\B1`, `_Inbox\B2`, `_Inbox\B3` (junctions).

Application : 6/6 projets Picard équipés (00_Agency_aaS, 01_OMK_BOS, 02_ABC_OS, 03_RILCOT, 04_Alikaly, 05_Marina).

## Archive importante

`PARA\04_Archives_Data\Legacy_LifeOS_App_Specs_2026-05-22\` contient désormais l'historique des specs d'une app Life OS abandonnée :
- `_SPECS\` (198 fichiers — ancien inbox, jamais formalisé en canon L1/L2)
- `TOTAL_Spec\` (177 fichiers — fusion partielle)

Ces dossiers ne sont **plus consultés** comme canon. Pour archive uniquement.

## Suivi

- `ADR-FWK-023` : fusion contenu Business OS ↔ PARA J01 B2_Area_Domains
- Vérifier intégrité PARA Picard après création des 18 junctions `_Inbox` (B1/B2/B3 × 6 projets)

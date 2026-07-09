# ADR-FWK-022 — Quick Access Layer (Summers Verse) + Pattern `_Inbox` Projet

**Date de décision :** 2026-05-22
**Auteur :** A0 Amadeus + A2 Claude Code (Architecte)
**Statut :** RATIFIÉ
**Type :** Architecture Decision Record (Framework)
**Portée :** L1 PARA · L2 Business OS · Picard Summers Verse
**Ancré sur :** ADR-007 · ADR-FWK-021 · ADR-FS-001 · `AGENTS.md`
**Amende :** [ADR-FWK-021](ADR-FWK-021_blueprints-canon-tripartite.md) — annule la mention de `_SPECS\_INBOX\` (zone archivée, plus pertinente)

---

## Contexte

Suite à ADR-FWK-021 + ADR-FS-001, deux clarifications stratégiques de A0 (2026-05-22) :

1. **`_SPECS\` et `TOTAL_Spec\` ne sont PAS des canons** — ce sont les **archives** d'un ancien workflow de développement d'une **app Life OS** désormais abandonnée. Elle est remplacée structurellement par **Shadow_L1 + Shadow_L2** des SDDs du Tech_OS. → Les deux dossiers doivent vivre dans `PARA\04_Archives_Data\` (read-only, gelé).
2. **Source de Vérité Business Pulse** = `20_Life_OS\24_PARA_Enterprise\02_Areas_Spock\J01_Jerry_Prime_LD01_Business\`. `30_Business_OS\` n'est **pas** propriétaire — il est **Quick Access Layer** par-dessus PARA.
3. **Quick Access pour les projets** : `30_Business_OS\` expose les 6 projets Summers Verse (Picard) via junctions short-path, et chaque projet Picard reçoit un dossier `_Inbox\` interne avec junctions vers `B1\B2\B3` pour usage agents/scripts.

## Décision

### D1 — Statut `_SPECS\` + `TOTAL_Spec\` : ARCHIVÉS

Les deux dossiers ont été déplacés vers :

```
20_Life_OS\24_PARA_Enterprise\04_Archives_Data\Legacy_LifeOS_App_Specs_2026-05-22\
├── _SPECS\         (198 fichiers — ancien inbox)
└── TOTAL_Spec\     (177 fichiers — ancienne migration partielle)
```

Aucun de ces deux dossiers ne sert plus de canon ni d'inbox. Les **nouveaux brouillons de specs** vivent désormais dans :

- L0 : `10_Tech_OS\12_Blueprints\` (inbox = drafts directement dans le canon, statut `DRAFT` jusqu'à `RATIFIED`)
- L1 : `20_Life_OS\28_Blueprints\` (idem)
- L2 : `30_Business_OS\09_Blueprints\` (idem)

Le marqueur de maturité est désormais le champ `Statut :` dans la frontmatter du fichier, plus la localisation.

→ **Cet article annule la mention "`_SPECS\_INBOX\`" d'ADR-FWK-021.** Cette zone n'existe pas.

### D2 — Source de Vérité Business Pulse confirmée

```
SoT : 20_Life_OS\24_PARA_Enterprise\02_Areas_Spock\J01_Jerry_Prime_LD01_Business\
      ├── B1_Area_Direction\
      ├── B2_Area_Domains\       ← 8 secteurs DC/Marvel (canon noms longs)
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

`30_Business_OS\00_Jerry_Business_Pulse\04_Business_Domains\` doit s'aligner sur ces noms longs. **Alignement effectué 2026-05-22** : les 7 sous-dossiers existants ont été renommés (8e = 04_Product_Flash en cours de migration). Mapping appliqué :

| Avant (Business OS short) | Après (aligné PARA SoT) |
|---------------------------|--------------------------|
| `01_People_GreenLantern` | `07_People_GreenLantern_XMen` |
| `02_IT_Cyborg` | `05_IT_Cyborg_KangDynasty` |
| `03_Operations_Batman` | `04_Ops_Batman_Fantastic4` |
| `04_Product_Flash` (racine → migré) | `04_Product_Flash` (renommé `03_Product_Flash_Avengers` post-move) |
| `05_Growth_Superman` | `01_Growth_Superman_Guardians` |
| `06_Finance_WonderWoman` | `06_Finance_WonderWoman_Thunderbolts` |
| `07_Legal_Aquaman` | `08_Legal_Aquaman_Eternals` |
| `08_Sales_JohnJones` | `02_Sales_MartianManhunter_Illuminati` |

**Note** : le contenu des secteurs Business OS n'est **pas encore fusionné** avec `J01\B2_Area_Domains\<same-name>\`. Étape future (ADR-FWK-023) : après validation, transformer `04_Business_Domains\` en junction vers `J01\B2_Area_Domains\` une fois fusion contenu opérée.

### D3 — Quick Access Layer Summers Verse

`30_Business_OS\` n'est **pas** propriétaire de projets. Il est **vue Quick Access** :

```
30_Business_OS\00_Summers_QuickAccess\        ← Junctions vers Picard
  ├── 00_Agency_aaS\   → PARA\…\Picard\00 Agency as a Service\
  ├── 01_OMK_BOS\      → PARA\…\Picard\01 OMK Business OS\
  ├── 02_ABC_OS\       → PARA\…\Picard\02 ABC OS & Child Care BOS\
  ├── 03_RILCOT\       → PARA\…\Picard\03_RILCOT_Members_Space_OS\
  ├── 04_Alikaly\      → PARA\…\Picard\04 Alikaly Bana Holding to LLC\
  └── 05_Marina\       → PARA\…\Picard\05 marina Cleaning BOS & SOP\
```

Gain de path :
- Avant : `…\Picard\04 Alikaly Bana Holding to LLC\B2_Business_Domains\…` (75+ chars de préfixe)
- Après : `…\00_Summers_QuickAccess\04_Alikaly\B2\…` (35 chars de préfixe via _Inbox cumulé)

### D4 — Pattern `_Inbox\` dans chaque projet Picard

Chaque projet Summers Verse (Picard) reçoit un dossier `_Inbox\` interne contenant des junctions short-path vers la structure B1/B2/B3 du projet :

```
Picard\<projet>\
├── _Inbox\
│   ├── B1\ → ../B1_Summer_Direction\
│   ├── B2\ → ../B2_Business_Domains\
│   └── B3\ → ../B3_Warp_Core_Execution\
├── B1_Summer_Direction\
├── B2_Business_Domains\
├── B3_Warp_Core_Execution\
├── SUMMERS_VERSE_MANIFEST.md
└── CERRIROS_HANDOVER.md
```

Usage agents/scripts :
- `…\Picard\04 Alikaly…\_Inbox\B2\03_Product_Flash_Avengers\…` au lieu du chemin long
- Combine avec `00_Summers_QuickAccess` : `…\00_Summers_QuickAccess\04_Alikaly\_Inbox\B2\…`

**Limitation MAX_PATH** : ce pattern réduit la longueur perçue par les outils, mais reste sujet à MAX_PATH si le contenu transitif dépasse 260 chars. Pour le code de production (Next.js, etc.), continuer à utiliser le drive `subst` (`P:\`) ou `\\?\` prefix.

## Actions exécutées le 2026-05-22

1. ✅ Archivage `_SPECS\` + `TOTAL_Spec\` → `PARA\04_Archives_Data\Legacy_LifeOS_App_Specs_2026-05-22\`
2. ✅ Renommage 7 secteurs Business OS pour aligner sur PARA J01 (mapping D2)
3. ⏳ Move `30_Business_OS\04_Product_Flash\` (114K fichiers) → `…\04_Business_Domains\04_Product_Flash\` via `robocopy /MOVE` (en background — log : `Shadow_L0\robocopy-product-flash-20260522.log`)
4. ✅ Création `30_Business_OS\00_Summers_QuickAccess\` + 6 junctions vers projets Picard
5. ✅ Création `_Inbox\` + 3 junctions (B1/B2/B3) dans chaque projet Picard (6/6)

## Conséquences

### Positives
- Source de Vérité unique et claire (PARA J01 pour Business Pulse, PARA Picard pour Projects)
- Path agents/scripts réduit de 50%+ via combinaison Quick Access + `_Inbox`
- Pas de duplication de contenu, junctions partout
- Convention nommage cohérente Business OS ↔ PARA (Marvel/DC squads)
- Archive `_SPECS`/`TOTAL_Spec` préserve historique sans polluer racine

### Négatives
- Contenu Business OS `04_Business_Domains\<secteur>\` pas encore fusionné avec PARA J01 SoT (étape suivante = ADR-FWK-023)
- `_Inbox` ajoute 1 niveau aux 6 projets Picard (acceptable car compense le path long avec junctions)
- MAX_PATH peut encore frapper pour repos très imbriqués → reste recours à `subst` / `\\?\`

### Neutres
- ADR-FWK-021 mention `_SPECS\_INBOX\` est désormais obsolète (annulée par ce document). FWK-021 reste source pour la doctrine tripartite L0/L1/L2 elle-même.

## Suivi requis

- **ADR-FWK-023** : Plan de fusion contenu `30_Business_OS\…\04_Business_Domains\<secteur>\` → `PARA\J01\B2_Area_Domains\<secteur>\`, puis remplacement par junction
- **ADR-FS-002** : Script `Setup-ASpace-Junctions.ps1` (sentinelles racine `_\`, drives subst, audit)
- **Vérification post-robocopy** : confirmer move `04_Product_Flash` complet, puis renommer en `03_Product_Flash_Avengers` côté Business OS
- **Décision A0** : `00_Jerry_Business_Pulse\` (dossier hybride) doit-il à terme devenir junction vers `J01_Jerry_Prime_LD01_Business\` ? Bloqué par contenu spécifique Business OS (`02_Global_Dashboard\`, `03_Master_Agreements\`, `CEO_Directives.md`)

## Références

- [ADR-FWK-021](ADR-FWK-021_blueprints-canon-tripartite.md) — Canon Tripartite Blueprints (parent, amendé sur point `_SPECS\_INBOX`)
- [ADR-FS-001](ADR-FS-001_junction-based-aliasing.md) — Junction-Based Aliasing (corollaire opérationnel)
- `Shadow_L0\03_quick-access-summers-and-inbox-20260522.md`
- `Shadow_L1\07_para-source-of-truth-confirmed-20260522.md`
- `Shadow_L2\08_business-os-quick-access-and-rename-20260522.md`

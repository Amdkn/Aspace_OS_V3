---
auteur: S3-Amy-Social (Spec, 11e Docteur)
date: 2026-08-03
issue: ASP-931 (0f9a2ccd-780d-47da-9b79-d7b17f6dae2d)
commande_de_verification:
  - ls "C:/Users/amado/ASpace_OS_V3/20_Life_OS/**/A3_*_Spec.md" | wc -l  # → 34
  - multica agent list --output json | jq '[.[] | select(.name|startswith("A3-"))] | length'  # → 8
statut: spec_sealed — Rory peut bâtir
---

# Manifeste exact des specs A3 + arbitrage Picard

## 1. Critère d'acceptation (vérifiable)

- **34 fichiers `A3_*_Spec.md`** sur le disque, sous `ASpace_OS_V3/20_Life_OS/`.
- **8 agents A3** déjà créés dans Multica, dont **1 sans spec** (Picard, dérivé).
- **Picard est compté à part**, comme officier **dérivé** : les **34 unités canoniques
  = 34 specs disk**, et Picard complète l'équipage PARA par exclusion.
- Aucune spec n'est dupliquée ; aucun nom canonique n'a deux fichiers.

## 2. Décompte canonique par framework

| Framework | Unités canoniques | Specs sur disque |
|---|---|---|
| 21_Ikigai_Orville | 9 (4 piliers + 5 horizons) | 9 |
| 22_Wheel_Discovery | 8 (LD01 → LD08) | 8 |
| 23_12WY_SNW | 5 (Pike, Una, M'Benga, Chapel, Ortegas) | 5 |
| 24_PARA_Enterprise | **3 canoniques** (Spock, Geordi, Data) + **1 dérivé Picard** | 3 |
| 25_GTD_Cerritos | 5 (Mariner, Boimler, Rutherford, Tendi, Freeman) | 5 |
| 26_DEAL_Protostar | 4 (Dal, Rok-Tahk, Zero, Gwyn) | 4 |
| **TOTAL canonique** | **34** (35 officiers actifs en incluant Picard) | **34** |

Cohérence arithmétique : 9 + 8 + 5 + 3 + 5 + 4 = **34** ✓ (sans Picard).
Avec Picard dérivé → 35 officiers A3 actifs (dont 1 sans spec).

## 3. Manifeste exact — 34 specs sur disque

### 21_Ikigai_Orville (9)

| # | Spec | Chemin |
|---|---|---|
| 1 | A3_Ed_Mercer_Spec.md | `20_Life_OS/21_Ikigai_Orville/01_Pillars_Identity/01_Profession_Mercer/` |
| 2 | A3_Kelly_Grayson_Spec.md | `20_Life_OS/21_Ikigai_Orville/01_Pillars_Identity/02_Mission_Grayson/` |
| 3 | A3_Gordon_Malloy_Spec.md | `20_Life_OS/21_Ikigai_Orville/01_Pillars_Identity/03_Passion_Malloy/` |
| 4 | A3_Claire_Finn_Spec.md | `20_Life_OS/21_Ikigai_Orville/01_Pillars_Identity/04_Vocation_Finn/` |
| 5 | A3_Isaac_H1_Spec.md | `20_Life_OS/21_Ikigai_Orville/02_Horizons_Time/01_H1_Isaac/` |
| 6 | A3_John_Lamarr_H3_Spec.md | `20_Life_OS/21_Ikigai_Orville/02_Horizons_Time/02_H3_Lamarr/` |
| 7 | A3_Bortus_H10_Spec.md | `20_Life_OS/21_Ikigai_Orville/02_Horizons_Time/03_H10_Bortus/` |
| 8 | A3_Alara_Kitan_H30_Spec.md | `20_Life_OS/21_Ikigai_Orville/02_Horizons_Time/04_H30_Alara/` |
| 9 | A3_Klyden_H90_Spec.md | `20_Life_OS/21_Ikigai_Orville/02_Horizons_Time/05_H90_Klyden/` |

### 22_Wheel_Discovery (8)

| # | Spec | Chemin |
|---|---|---|
| 10 | A3_Book_LD01_Spec.md | `20_Life_OS/22_Wheel_Discovery/LD01_Business_Book/` |
| 11 | A3_Saru_LD02_Spec.md | `20_Life_OS/22_Wheel_Discovery/LD02_Finance_Saru/` |
| 12 | A3_Culber_LD03_Spec.md | `20_Life_OS/22_Wheel_Discovery/LD03_Health_Culber/` |
| 13 | A3_Tilly_LD04_Spec.md | `20_Life_OS/22_Wheel_Discovery/LD04_Cognition_Tilly/` |
| 14 | A3_Stamets_LD05_Spec.md | `20_Life_OS/22_Wheel_Discovery/LD05_Social_Stamets/` |
| 15 | A3_Burnham_LD06_Spec.md | `20_Life_OS/22_Wheel_Discovery/LD06_Family_Burnham/` |
| 16 | A3_Reno_LD07_Spec.md | `20_Life_OS/22_Wheel_Discovery/LD07_Creativity_Reno/` |
| 17 | A3_Georgiou_LD08_Spec.md | `20_Life_OS/22_Wheel_Discovery/LD08_Impact_Georgiou/` |

### 23_12WY_SNW (5)

| # | Spec | Chemin |
|---|---|---|
| 18 | A3_Pike_Vision_Spec.md | `20_Life_OS/23_12WY_SNW/01_Vision_Pike/` |
| 19 | A3_Una_Planning_Spec.md | `20_Life_OS/23_12WY_SNW/02_Planning_Una/` |
| 20 | A3_MBenga_Focus_Spec.md | `20_Life_OS/23_12WY_SNW/03_Focus_MBenga/` |
| 21 | A3_Chapel_Metrics_Spec.md | `20_Life_OS/23_12WY_SNW/04_Metrics_Chapel/` |
| 22 | A3_Ortegas_Execution_Spec.md | `20_Life_OS/23_12WY_SNW/05_Execution_Ortegas/` |

### 24_PARA_Enterprise (3 canoniques + 1 dérivé)

| # | Spec | Chemin | Note |
|---|---|---|---|
| 23 | A3_Spock_Areas_Spec.md | `20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/` | canonique |
| 24 | A3_Geordi_Resources_Spec.md | `20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/` | canonique |
| 25 | A3_Data_Archives_Spec.md | `20_Life_OS/24_PARA_Enterprise/04_Archives_Data/` | canonique |
| — | (Picard, pas de spec) | `20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/AGENT.md`+`SOUL.md` | **dérivé** |

### 25_GTD_Cerritos (5)

| # | Spec | Chemin |
|---|---|---|
| 26 | A3_Mariner_Capture_Spec.md | `20_Life_OS/25_GTD_Cerritos/01_Inbox_Mariner/` |
| 27 | A3_Boimler_Clarify_Spec.md | `20_Life_OS/25_GTD_Cerritos/02_Clarify_Boimler/` |
| 28 | A3_Rutherford_Organize_Spec.md | `20_Life_OS/25_GTD_Cerritos/03_Organize_Rutherford/` |
| 29 | A3_Tendi_Review_Spec.md | `20_Life_OS/25_GTD_Cerritos/04_Review_Tendi/` |
| 30 | A3_Freeman_Engage_Spec.md | `20_Life_OS/25_GTD_Cerritos/05_Engage_Freeman/` |

### 26_DEAL_Protostar (4)

| # | Spec | Chemin |
|---|---|---|
| 31 | A3_Dal_Definition_Spec.md | `20_Life_OS/26_DEAL_Protostar/01_Definition_Dal/` |
| 32 | A3_RokTahk_Elimination_Spec.md | `20_Life_OS/26_DEAL_Protostar/02_Elimination_RokTahk/` |
| 33 | A3_Zero_Automation_Spec.md | `20_Life_OS/26_DEAL_Protostar/03_Automation_Zero/` |
| 34 | A3_Gwyn_Liberation_Spec.md | `20_Life_OS/26_DEAL_Protostar/04_Liberation_Gwyn/` |

## 4. Agents A3 déjà présents dans Multica (8)

| Agent Multica | ID | Spec disk | Framework | Statut |
|---|---|---|---|---|
| A3-Pike | `0cc429a8-d842-4c96-a0d2-b7af46d25eda` | ✓ A3_Pike_Vision | SNW | OK |
| A3-Dal | `cdb5ba1d-57e7-45f6-8601-f644ae5db4d0` | ✓ A3_Dal_Definition | Protostar | OK |
| A3-Mercer | `33eefa1d-b577-48b6-87d6-b1a33fd906cc` | ✓ A3_Ed_Mercer | Orville | OK |
| A3-Mariner | `89b94d1c-eb63-49f1-a40a-26554804c22a` | ✓ A3_Mariner_Capture | Cerritos | OK |
| A3-Spock | `6d4ac0e6-7767-4a73-be11-123980610d83` | ✓ A3_Spock_Areas | PARA | OK |
| A3-Geordi | `ca301ba8-f379-48cc-95ca-e78f0e9c6e20` | ✓ A3_Geordi_Resources | PARA | OK |
| A3-Data | `73413639-fc59-4513-83f1-d3a3f952b8b3` | ✓ A3_Data_Archives | PARA | OK |
| A3-Picard | `ea5784f0-c1de-4c34-b95b-ca3785b8e5ec` | ✗ — dérivée | PARA (dérivé) | **exception** |

## 5. Specs sans agent Multica (27 — rivière de Rory)

| Framework | Manquants |
|---|---|
| Orville (8) | Grayson, Malloy, Finn, Isaac, Lamarr, Bortus, Alara, Klyden |
| Discovery (8) | Book, Saru, Culber, Tilly, Stamets, Burnham, Reno, Georgiou |
| SNW (4) | Una, M'Benga, Chapel, Ortegas |
| Cerritos (4) | Boimler, Rutherford, Tendi, Freeman |
| Protostar (3) | Rok-Tahk, Zero, Gwyn |

## 6. Arbitrage Picard — officiel

**Position tranchée par Spec (Amy) :**

> Les **34 unités A3 canoniques** correspondent aux **34 fichiers `A3_*_Spec.md`**
> sur disque. **Picard n'est pas compté dans les 34.**
> C'est un officier A3 **dérivé, non canonique** : son `AGENT.md` (`24_PARA_Enterprise/01_Projects_Picard/`)
> s'auto-déclare *« Rôle dérivé, non canonique »* et *« Aucune spec A3 pour
> Picard dans le canon V2 »*. Il complète l'équipage PARA **par exclusion** :
> Spock · Geordi · Data routent vers lui tout item porteur d'une échéance et d'un
> livrable.

**Conséquences pour le critère de fin #1 de l'issue ASP-931 :**
*« Chaque fichier `A3_*_Spec.md` possède exactement un agent Multica correspondant. »*

- Les 34 specs disk → obligation de **27 nouveaux agents** (8 specs déjà mappées à
  un agent existant : Pike, Dal, Mercer, Mariner, Spock, Geordi, Data = 7 specs ;
  Picard n'est pas dans les specs).
- Picard (officier existant `ea5784f0-c1de-4c34-b95b-ca3785b8e5ec`) reste tel quel :
  pas de spec à produire, exception documentée.

**Pour la question "34 ou 35" :** le canon V3 (README L120-132) annonce *« 34 unités A3 »*
et le décompte arithmétique du tableau (9+8+5+3+5+4) = 34. **Le compte fait foi :
34 specs = 34 unités. Picard = 35ᵉ officier, hors décompte.**

## 7. Périmètre (ce que ce manifeste NE fait PAS)

- Aucune réplique (River n'intervient pas à ce stade).
- Aucun agent créé (Rory n'intervient pas à ce stade).
- Aucune modification de `Squad-A3-Officiers` (`a1305949-30a8-4b12-8e05-781122329c8a`,
  actuellement 0 membres côté API).
- Aucun `done` prononcé. C'est un ruban **Spec** : le 11e Docteur décide du détachement.

## 8. Interdits rappelés

- Ne pas créer de spec Picard : son `AGENT.md` dit lui-même *« A remplacer dès
  qu'une spec Picard existe »* — c'est un acte de **rang bâtisseur** (Rory) ou
  **rang manager** (Docteur 11), pas de rang Spec.
- Ne pas modifier les 7 agents existants (Pike, Dal, Mercer, Mariner, Spock,
  Geordi, Data) : leurs instructions viennent déjà de leur spec respective.
- Ne pas décompter Picard dans les 34 specs : c'est précisément ce que cette
  note tranche.

---

**Spec scellé · Amy Social · 2026-08-03**
Prochaine étape : Rory (Build) — créer les 27 agents manquants depuis le §5,
sans toucher Picard, sans toucher les 7 agents existants.

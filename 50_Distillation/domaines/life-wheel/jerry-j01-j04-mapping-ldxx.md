---
type: Concept
title: J01-J04 — Les 4 Jerry et leurs LDxx
description: Quatre Jerry transversaux couvrent les 8 LDxx par bande : J01 Prime (LD01), J02 Bio (LD03+LD04), J03 Nexus (LD02+LD06 FIP), J04 Solarpunk (LD05+LD07+LD08). Couverture complète vérifiée à la source `02_Areas_Spock/J0X_*`.
tags: [jerry, j01-prime, j02-bio, j03-nexus, j04-solarpunk, fip-standard, ld-coverage]
generated: { by: minimax-m3, at: 2026-08-19T04:09:00Z }
verified:
  - { by: process:read_local_v2, at: 2026-08-19T04:09:00Z }
sources:
  - id: shadow-tools
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/00_Shadow_Tools_Guide_L1.md
    title: Shadow Tools Guide L1 — J01_Jerry_Prime_LD01_Business convention
    last_modified: 2026-06-04
  - id: jerry-j01
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/J01_Jerry_Prime_LD01_Business/README.md
    title: J01 Jerry Prime - LD01 Business README
    last_modified: 2026-05-21
  - id: jerry-j02
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/J02_Jerry_Bio_LD03_LD04_Vitality_Cognition/
    title: J02 Jerry Bio - LD03+LD04 Vitality+Cognition (dossier canon)
    last_modified: 2026-05-21
  - id: jerry-j03
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/J03_Jerry_Nexus_LD02_LD06_Finance_Family/
    title: J03 Jerry Nexus - LD02+LD06 Finance+Family (dossier canon)
    last_modified: 2026-05-21
  - id: jerry-j04
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/J04_Jerry_Solarpunk_LD05_LD07_LD08_Social_Creativity_Impact/
    title: J04 Jerry Solarpunk - LD05+LD07+LD08 (dossier canon)
    last_modified: 2026-05-21
okf_version: "0.2"
---

# J01-J04 — Les 4 Jerry et leurs LDxx

## Question de la vague

La passe précédente (vague 1) a montré que **les quatre Jerry portent des codes LD01 à LD08**. Cette vague vérifie la **correspondance Jerry → LD à la source canon**.

## Table canon J0X → LDxx

| Jerry | Couverture LD | Nom canon | Ancre / Doctrine | Source |
|---|---|---|---|---|
| **J01** | **LD01** | Jerry **Prime** (LD01 Business) | B1 captain E-Myth SYSTEMIZE ; B2 = 8 Business Wheel domains (Growth, Sales, Product, Ops, IT, Finance, People, Legal) | `J01_Jerry_Prime_LD01_Business/README.md` |
| **J02** | **LD03 + LD04** | Jerry **Bio** (LD03+LD04 Vitality+Cognition) | Primary gravity sensor ; HARD SAFETY Beth veto | `J02_Jerry_Bio_LD03_LD04_Vitality_Cognition/` |
| **J03** | **LD02 + LD06** | Jerry **Nexus** (LD02+LD06 Finance+Family) | **FIP STANDARD** = Finance Independence + Presence stability | `J03_Jerry_Nexus_LD02_LD06_Finance_Family/` |
| **J04** | **LD05 + LD07 + LD08** | Jerry **Solarpunk** (LD05+LD07+LD08 Social+Creativity+Impact) | Ancrage Solarpunk/biomimétisme (Benyus/Aberkane) ; rejette burn-out language | `J04_Jerry_Solarpunk_LD05_LD07_LD08_Social_Creativity_Impact/` |

## Couverture vérifiée

| LD | Domaine | Couverte par Jerry |
|---|---|---|
| LD01 | Career & Business | **J01** |
| LD02 | Finance & Independence | **J03** |
| LD03 | Health/Sleep/Energy | **J02** |
| LD04 | Mind/Cognition | **J02** |
| LD05 | Social/Relations | **J04** |
| LD06 | Family/Presence | **J03** |
| LD07 | Creativity/Leisure | **J04** |
| LD08 | Contribution/Impact | **J04** |

**Chaque LD est couvert par exactement un Jerry**. Aucune collision ni orphelin détecté.

## Rôle architectural des 4 Jerry

Les 4 Jerry ne sont **pas** des A3 twins — ce sont des **B1 Captains** (E-Myth SYSTEMIZE doctrine). Ils portent la **strategie Business OS** ; les A3 Discovery twins (Book/Saru/Culber/Tilly/Stamets/Burnham/Reno/Georgiou) portent la **mesure Life Wheel**.

Architecture :

```
B1 Captains (Jerry × 4) ── strategy/why ──→ A2 ships ──→ A3 Discovery twins ── measure/findings
                                  (PARA Areas Spock)         (Life Wheel LDxx)
```

C'est la raison du couplage `B1 → A2 → A3` dans le plan `fancy-hugging-bengio.md §3.6` (Matrice routage 20 intentions A0).

## Collision de nom détectée

Doublon typo dans archive `_V3_STRUCTURE_2026-08-02/` :
- ✅ Vivant : `J04_Jerry_Solarpunk_LD05_LD07_LD08_Social_Creativity_Impact`
- ❌ Mort (typo) : `J04_Jerry_Solarpunk_LD05_LD07_LD08_Social_Creatry_Impact`

Le canon est la version correcte. La typo "Creatry" est morte dans l'archive.

## Verdict distillation

`canon` — fait autorité, source canonique `02_Areas_Spock/J0X_*/README.md` + `Shadow_Tools_Guide_L1.md` ligne 287 (convention J01_Jerry_Prime_LD01_Business dans le schéma de PARA Areas).

## Pièges documentés

- **Ne pas confondre J03 = "Nexus" (transversal LD02+LD06) avec Nexus/OMK (AaaS variant Saru LD02, CLOS 2026-06-20)**. Même nom, deux concepts différents : J03 est un Jerry B1 captain (actif) ; Nexus/OMK est un AaaS variant archivé.
- **Le mapping 4-Jerry ne se voit pas dans les A3 specs LDxx**. Les A3 specs mentionnent Saru/Spock/Isaac/Klyden/Gordon/Kelly (les crew Ikigai), pas les Jerry. Le mapping J0X→LDxx est documenté dans `02_Areas_Spock/J0X_*/README.md` (Areas Spock) et `Shadow_Tools_Guide_L1.md`.

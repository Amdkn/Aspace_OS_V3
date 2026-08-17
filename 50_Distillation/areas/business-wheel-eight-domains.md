---
type: Concept
title: La wheel Business — 8 domaines B2
description: Le Business Wheel de LD01 fixe huit domaines (Growth, Sales, Product, Ops, IT, Finance, People, Legal) — chacun avec un hero-manager B2 et un squad B3. La règle "one datum, one owner" empêche la dérive produit-only et la duplication cross-domaine.
tags: [business-wheel, b2, growth, sales, product, ops, finance, people, legal, domains]
generated: { by: minimax-m3, at: 2026-08-17T20:55:00Z }
verified:
  - { by: process:extraction-areas, at: 2026-08-17T20:55:00Z }
sources:
  - id: fractal-arch
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/J01_Jerry_Prime_LD01_Business/00_L2_FRACTAL_B1B2B3_ARCHITECTURE.md"
    title: L2 Business — The B1 / B2 / B3 Fractal Architecture
    last_modified: 2026-06-02
  - id: harmonization
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/B2_BUSINESS_WHEEL_HARMONIZATION_MATRIX.md"
    title: B2 Business Wheel Harmonization Matrix
    last_modified: 2026-05-27
  - id: refs
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/Business_Pulse/L2_Business_Pulse_References_Index.md"
    title: L2 Business Pulse References Index
    last_modified: 2026-05-21
  - id: a1-spec
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/A1_Jerry_Areas_Spec.md"
    title: A1 Jerry Areas Spec
    last_modified: 2026-05-21
okf_version: "0.2"
---

# La wheel Business — 8 domaines B2

La **Business Wheel** est l'arrangement canonique des huit domaines B2 pour LD01. Chaque domaine est possédé par un hero-manager B2 et exécuté par un squad B3 — Superman/Guardians (Growth), Martian Manhunter/Illuminati (Sales), Flash/Avengers (Product), Batman/Fantastic4 (Ops), Cyborg/Kang Dynasty (IT), Wonder Woman/Thunderbolts (Finance), Green Lantern/X-Men (People), Aquaman/Eternals (Legal).

## La matrice canon

Tirée de `A1_Jerry_Areas_Spec.md` §« Business Wheel Domains For LD01 » et confirmée par `00_L2_FRACTAL_B1B2B3_ARCHITECTURE.md` §4 :

| # | Domaine | B2 (A2) | B3 squad (A3) | North Star (KRs) |
|---|---|---|---|---|
| 1 | Growth | Superman | Guardians of the Galaxy | ICP-qualified non-paid opps (KR-4a..d) |
| 2 | Sales | John Jones (Martian Manhunter) | Illuminati | conversion / pipeline→cash (KR-2a..d) |
| 3 | Product | Flash | Avengers | value: activation × retention (NPS/retention) |
| 4 | Ops | Batman | Fantastic Four | autonomie ratio (« runs without you ») |
| 5 | IT | Cyborg | Kang Dynasty | intégrité opérationnelle (KR-5a..c) |
| 6 | Finance | Wonder Woman | Thunderbolts | cash/margin/runway (KR-5d..g) |
| 7 | People | Green Lantern | X-Men | team health, capsules humaines + IA (KR-7a..d) |
| 8 | Legal | Aquaman | Eternals | protection sans friction (KR-8a..d) |

Le mode canon est **8**. La référence `L2_Business_Pulse_References_Index.md` §« Canonical Conflict Notes » note qu'« il existe des passages SDD mentionnant 7 domaines DC/Marvel » mais que la doctrine active (SDD-009 et après) tient sur **8** — c'est la version à utiliser.

## La règle « one datum, one owner »

C'est l'ADR-clef (`ADR-MESH-L2-001` référencé par `00_L2_FRACTAL_B1B2B3_ARCHITECTURE.md`) :

| Domaine | Possède |
|---|---|
| Growth | acquisition |
| Sales | conversion |
| Product | value |
| Ops | repeatability |
| IT | substrate |
| Finance | solvency |
| People | team |
| Legal | protection |

Les domaines se **pointent** les uns les autres sur les données ; ils ne les **copient** jamais. Un lead qualifié est Growth jusqu'à ce qu'il passe à Sales ; il ne devient pas un « objet partagé ». Une marge nette est Finance ; Product n'en a pas la propriété.

## Pourquoi 8 et pas 9

La même note de conflit signale un item ouvert : « Meta » reste-t-il un slot UI-only, un slot de gouvernance caché, ou un neuvième domaine ? Tant que A0 n'a pas tranché, **Meta n'est pas instantiated comme un domaine B2**. La wheel reste à 8.

## Le risque de dérive

Trois dérives classiques, mesurées dans le substrat :

1. **Product-only release** : un domaine Product livre un artefact, les sept autres ne valident rien, et le release est appelé « Business Done ». Stop condition : « No Product-only release becomes Business Done without the B2 gate matrix ».
2. **Domaine aspirateur** : un domaine (souvent Growth ou Sales) absorbe les données et les responsabilités des autres. Symptôme : double-saisie, KRs incohérents, conflits de priorité. Parade : la matrice d'harmonisation (voir `business-wheel-harmonization-matrix.md`).
3. **Domaine fantôme** : un slot existe (par exemple IT) mais personne n'est nommé. Symptôme : incidents non résolus, dette technique invisible, escalades silencieuses. Parade : B1 mandate pour combler la vacance.

## La boundary law en pratique

Le domaine **IT** est le plus souvent dérivé : « Jerry does NOT decide IT architecture — Cyborg (B2) holds it outright ». `B1_DECISION_CHARTER.md` §1 le confirme par une ligne explicite. La tentation de faire traiter IT par Jerry (pour gagner du temps) est exactement le genre de court-termisme qui crée une dette technique permanente.

## Le test de complétude

Pour valider qu'une Area Business (LD01) est mature, on vérifie que :

- Chaque domaine a un hero-manager B2 nommé (pas de slot vacant).
- Chaque B2 a un squad B3 d'au moins 4 membres.
- Chaque domaine a un North Star mesurable (au moins un KR).
- Chaque B2 peut produire une preuve mensuelle (KRs, gates, lead/lag).

Le substrat montre J01 atteint ce standard (8 domaines, 8 squads de 4–10 membres, AREA_STANDARD complet). Les autres Jerry (J02–J04) adaptent la wheel à leurs 8 domaines propres.
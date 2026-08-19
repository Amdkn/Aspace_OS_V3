---
type: Concept
title: Domain Operating Cadences — chaque SOB a sa propre horloge
description: Chaque SOB opère à une cadence propre, fixée par le canon. Growth/Sales/Product hebdo, Ops bi-hebdo, IT quotidien, Finance/People mensuel, Legal trimestriel. La cadence dicte la profondeur de dépliage Matrioshka.
tags: [cadence, sob, operating-mode, matryoshka, drift-detection]
generated: { by: minimax-m3, at: 2026-08-19 }
verified:
  - { by: process:lecture-directe, at: 2026-08-19 }
sources:
  - id: SUMMERS_VERSE_MANIFEST
    resource: "30_Business_OS/10_Projects/ceo-desktop/_doctrine/SUMMERS_VERSE_MANIFEST.md"
    title: Summer's Verse Manifest — CEO's Desktop
    last_modified: "2026-06-07"
  - id: README_CEO_DESKTOP
    resource: "30_Business_OS/10_Projects/ceo-desktop/README.md"
    title: README — CEO's Desktop
    last_modified: "2026-06-07"
  - id: MANIFEST_CEO_DESKTOP
    resource: "30_Business_OS/10_Projects/ceo-desktop/MANIFEST.md"
    title: Manifest — ceo-desktop
    last_modified: "2026-07-13"
okf_version: "0.2"
---

# Domain Operating Cadences — chaque SOB a sa propre horloge

> **Une seule chose à retenir.** Chaque SOB a une **cadence propre** : Growth/Sales/Product hebdo, Ops bi-hebdo, IT quotidien, Finance/People mensuel, Legal trimestriel. La cadence n'est pas négociée ; elle dicte la **profondeur de dépliage Matrioshka**.

## Énoncé canonique

| #  | SOB Domain | B3 Squad (Marvel)        | Cadence canon | Desktop Mode                                              |
|----|------------|--------------------------|---------------|-----------------------------------------------------------|
| 1  | Growth     | Superman / Guardians     | Weekly        | Pulse — experiment velocity, ICP drift, channel mix       |
| 2  | Sales      | Martian Manhunter / Illuminati | Weekly | Pipeline — qualified leads, conversion, handoff to Product |
| 3  | Product    | Flash / Avengers         | Weekly        | Build — shipped Rocks, JTBD proof, scope drift             |
| 4  | Ops        | Batman / Fantastic Four  | Bi-weekly     | Flow — SOP health, delivery reliability, cost per unit     |
| 5  | IT         | Cyborg / Kang Dynasty    | Daily         | Stack — runtime, deploy, security, MCP/CLI health         |
| 6  | Finance    | Wonder Woman / Thunderbolts | Monthly    | Capital — burn, margin, runway, unit economics             |
| 7  | People     | Green Lantern / X-Men    | Monthly       | Load — owner load, training, founder-mode risk            |
| 8  | Legal      | Aquaman / Eternals       | Quarterly     | Boundary — IP, terms, exposure, compliance                |

> Each mode surfaces a different facet of the same underlying data. A0 sees all 8 in one scroll; a B2 manager sees only their column plus the 4 boundaries (IT, Finance, Legal, People) that gate their work. (`SUMMERS_VERSE_MANIFEST.md` § "ICP Variants — The 8 SOB Operating Modes")

## Pourquoi cette distribution

- **Growth/Sales/Product hebdo.** Ces trois domaines sont les **leading indicators** : ils montrent la trajectoire avant les autres. Hebdo = suffisamment réactif sans noyer A0.
- **Ops bi-hebdo.** Le SOP health et la delivery reliability sont des indicateurs **lagging** : ils suivent la cadence hebdo des leading.
- **IT quotidien.** Runtime, deploy, sécurité, MCP/CLI health sont des indicateurs **temps réel** : un crash serveur = HALT immédiat, pas un récap hebdomadaire.
- **Finance/People mensuel.** Burn, marge, runway, charge, attrition sont des indicateurs **lents** : la granularité mensuelle suffit, l'inflation d'indicateurs quotidiens n'apporte rien.
- **Legal trimestriel.** IP, terms, exposition, conformité sont des indicateurs **légaux** : la cadence suit les obligations de reporting (RGPD AI Act annuel, etc.).

## Cadence × dépliage Matrioshka

Le Matrioshka Dashboard (cf. concept dédié) déplie la couche juste à la cadence juste :

| Cadence    | Couche Matrioshka dominante | Profondeur typique                                       |
|------------|------------------------------|---------------------------------------------------------|
| Daily (IT) | Rock Wheel                   | Détail : tickets ouverts, healthcheck, logs            |
| Weekly (Growth/Sales/Product) | Domain Wheel        | Métriques du SOB + Rocks actifs de la semaine           |
| Bi-weekly (Ops) | Domain Wheel          | SOP health + delivery reliability sur 2 sem            |
| Monthly (Finance/People) | Business Wheel    | Burn + runway, charge + risque surcharge              |
| Quarterly (Legal) | Business Wheel       | Exposition IP/terms/conformité, scan trimestriel        |

## Anti-patterns

- **Daily standup pour Legal.** Legal n'a aucune valeur à être daily ; trimestriel suffit.
- **Trimestriel pour IT.** IT daily est non-négociable : un serveur mort attend pas le trimestre.
- **Couche unique pour tous les SOB.** Empiler les Rocks de 8 SOB en permanence rend sourd à la cadence propre.

## Ce que ce n'est pas

- Pas un rituel Scrum. Pas de sprint, pas de backlog grooming ; juste une cadence de revue.
- Pas un calendrier de publication. La cadence dicte la profondeur d'observation, pas la fréquence d'écriture.

## Conséquence opérationnelle

Un dashboard qui ne respecte pas la cadence propre d'un SOB est **anti-pattern**. Forcer Growth en mensuel ou IT en hebdomadaire casse la réactivité ou noie A0.

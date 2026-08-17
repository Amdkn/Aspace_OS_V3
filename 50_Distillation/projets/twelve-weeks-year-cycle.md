---
type: Concept
title: 12WY Cycle (Twelve Weeks Year)
description: Cadence trimestrielle de 84 jours (12 semaines) — rythme canonique pour Rocks B2, avec Lead Indicator (lundi) et Lag Indicator (vendredi) et bloc Lead/Lag_Logs/ prévu.
tags: [concept, cycle, 12wy, cadence, lead-lag, b2, b3]
generated: { by: minimax-m3, at: 2026-08-17T21:00:00Z }
verified:
  - { by: process:extraire_substrat_rdf, at: 2026-08-17T19:50:00Z }
  - { by: process:lecture_concepts_picard, at: 2026-08-17T21:00:00Z }
sources:
  - id: b3-warp-core-readme
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/05 marina Cleaning BOS & SOP/B3_Warp_Core_Execution/README.md"
    title: B3 Warp Core Execution README — 12WY Cycle tracking template
    last_modified: 2026-05-21
  - id: handover-abc
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/02 ABC OS & Child Care BOS/CERRIROS_HANDOVER.md"
    title: Handover ABC — 4 Rocks par trimestre, max
    last_modified: 2026-05-21
  - id: manifest-rilcot
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/03_RILCOT_Members_Space_OS/SUMMERS_VERSE_MANIFEST.md"
    title: Manifest RILCOT — 12WY Rock linkage W1-W4
    last_modified: 2026-05-21
okf_version: "0.2"
---

# 12WY Cycle (Twelve Weeks Year)

## Définition

Cadence canonique de **84 jours = 12 semaines = 1 trimestre** appliquée
aux Rocks B2 et à l'exécution B3. Inspirée de la méthode *12 Week Year*
(Brian Moran). Définition, format et gabarit sont déposés dans
`B3_Warp_Core_Execution/README.md`.

## Format standard

```
12WY CYCLE: _____  |  Start: __________  |  End: __________

ROCK TRACKING
────────────────────────────────────────────────────────────
Rock # | Description | B2 Owner | Start State | End State | Deadline | Status
────────────────────────────────────────────────────────────
R1     |             |          |             |           |          |
R2     |             |          |             |           |          |
R3     |             |          |             |           |          |
R4     |             |          |             |           |          |
────────────────────────────────────────────────────────────

WEEKLY LEAD/LAG LOG
────────────────────────────────────────────────────────────
Week | Lead Indicator         | Lag Indicator        | Notes
────────────────────────────────────────────────────────────
W1   |                       |                      |
... (W12)
────────────────────────────────────────────────────────────
```

## Lead vs Lag

| Type | Définition | Exemples |
|------|-----------|----------|
| **Lead** | Forward-looking, prédictif | Pipeline entered, calls booked, proposals sent, meetings scheduled |
| **Lag** | Rear-looking, confirmé | Revenue received, contracts signed, NPS score, close rate achieved |

**Règle** : Leads lundi, Lags vendredi. **Jamais substituer Leads pour Lags.**

## Plafond de Rocks

**4 Rocks par trimestre, maximum.** Si plus de 4, "the domain has none"
(handover ABC). C'est l'anti-pattern drill-down prévenu — un B2 manager
qui veut 8 Rocks doit en abandonner 4 explicitement.

## Spécificités par projet

| Projet | W1 cadence | Notes |
|--------|-----------|-------|
| ABC | 84 jours | Standard 12WY |
| RILCOT | 84 jours | Standard 12WY |
| Alikaly | Aligné cycle légal US | W1=assessment, W2=filing, W3=transfer, W4=operational |
| Marina | **21 jours** | Le seul projet non-standard : les SOPs sont courtes par nature |
| OMK | 84 jours (Q3 2026-06-15 → 2026-09-07) | Runbook C/D respectent Phases A→H |

## Stockage prévu

`Lead_Lag_Logs/` (entrées hebdomadaires, fichier `Lead_Lag_W[#]_[YYYY-MM-DD].md`)
+ `Artifact_Proofs/` (preuves par Rock, fichier
`Artifact_[Rock#]_[BriefDescription]_[Date]`).

**Constat substrat** : ces deux sous-dossiers **n'existent pas** dans les
4 projets Summer's Verse, ni dans OMK. La structure est définie, la
pratique est absente.

## Liens

- [[summers-verse-framework]] — la trame qui porte le 12WY
- [[eight-domain-avengers-wheel]] — les 8 B2 owners qui produisent les Rocks
- [[b2-business-wheel-harmonization-matrix]] — la matrice 8-domaines qui qualifie les Rocks

## Note de confiance

**Confirmé par machine.** Le format est défini dans le README B3 (Lu
2026-05-21). Le plafond 4 Rocks est documenté dans 4 handovers identiques.
L'alignement Ownerbook T1/T2/T3 OMK (Q3 2026-06-15 → 2026-09-07) montre
que la cadence 12WY est appliquée à la production 2026-07-15.

*Standing : cadence définie, exécution Lead/Lag vide.*

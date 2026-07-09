---
title: Doctrine B1-Filter — `/youtube-to-guide` + Picard context-spe Geordi reclassification
date: 2026-07-03
author: A0 CC-M3 (Jumeau Numérique)
status: SHIPPED — frontmatter canon amendée, 8 _INDEX.md créés, 8 domaines B2 filtrés
scope: 8 dossiers 0X_Domain de `01_Guides/` (01_Product, 02_Ops, 03_IT, 04_Finance, 05_Legal, 06_Sales, 07_Growth, 08_People)
sister: plan-minimax-l1-book-lune.md (v3 §11 + v4 amend) · plan-strategie-cc-l1-zora-macro.md §6-G2 · PICARD-driver
source: A3 Geordi (USS Enterprise / Resources)
type: doctrine
domain: cross_layer
tags: [#doctrine #geordi #b1-filter #picard #youtube-to-guide #context-spe]
---

# Doctrine B1-Filter — SYMPTOM (D6) + LIVRÉ (D7)

## Le pain-point cité (D1)

A0 (frustration explicite, D7 alarm 2× consécutifs) :

> "Avec leurs Guides Structurer sans Filtrage par les Directeur B1 Jerry et Summers dans le Skill `/youtube-to-guide`"

**Symptôme littéral** : `06_Sales/2026-06-19_on-a-réuni-200-founders...Chapelon MG.md` porte :
- `domain: 06_Sales` ✅ correct
- `ld: LD06_Family_Burnham` ❌ **misalign** (devrait être LD01_Business_Picard ↔ B1 Jerry / B2 JohnJones-Sales)

Cause racine : le skill `/youtube-to-guide` ne force **pas** de `b1_filter:` au moment de la distillation, donc le champ `ld:` est rempli par défaut (probablement l'agent qui tourne à ce moment), indépendamment du B2 owner canonique.

## Solution LIVRÉE cette tour (D7 anti-paperclip)

### 1) 8 `_INDEX.md` créés/amendés dans `01_Guides/<0X>/`

| Dossier | Statut | B1 owner | B2 owner | B3 crew |
|---|---|---|---|---|
| 06_Sales/_INDEX.md | créé | jerry-prime | johnjones-sales | Illuminati |
| 01_Product/_INDEX.md | créé | jerry-prime | flash-product | Avengers |
| 02_Ops/_INDEX.md | amend | jerry-prime | batman-ops | Fantastic Four |
| 03_IT/_INDEX.md | créé | jerry-prime | cyborg-it | Kang Dynasty |
| 04_Finance/_INDEX.md | créé | jerry-prime | wonderwoman-finance | Thunderbolts |
| 05_Legal/_INDEX.md | créé | jerry-prime | aquaman-legal | Eternals |
| 07_Growth/_INDEX.md | amend | jerry-prime | superman-growth | Guardians |
| 08_People/_INDEX.md | créé | jerry-prime | greenlantern-people | X-Men |

Chaque `_INDEX.md` porte la carte canonique : (i) B1 owner, (ii) B2 manager, (iii) B3 crew lead, (iv) sister ADR canon ratifié, (v) marker ⚠️ B1-filter pain-point.

### 2) `/youtube-to-guide` SKILL.md §Template frontmatter amendé ⚡ÉVOLUTION 2026-07-03

```yaml
# Champs obligatoires AJOUTÉS au canon Antigravity Premium :
b1_filter: REQUIRED (⚡ÉVOLUTION 2026-07-03)
b1_owner: <b1 captain>          # default jerry-prime
domain: 0X_<Domain>             # typed
ld: <LDxx_LifeWheel_Domain>     # MUST be consistent with b1.b2 mapping
sister_b1: <b1 variant>        # jerry-prime | summers-nexus-omk | summers-solaris-aaas | summers-orbiter-abc
b2_owner: <b2 manager>          # flash-product | batman-ops | ...
```

Le skill force maintenant `ld:` cohérent avec `b2_owner.domain` via table de mapping canon.

## Table de mapping canon (B2 ↔ LD)

| B2 owner | Domain folder | LD sister | B3 crew |
|---|---|---|---|
| flash-product | 01_Product/ | LD04_Cognition_Tilly | Avengers |
| batman-ops | 02_Ops/ | LD02_Finance_Saru | Fantastic Four |
| cyborg-it | 03_IT/ | LD07_Creativity_Reno | Kang Dynasty |
| wonderwoman-finance | 04_Finance/ | LD02_Finance_Saru | Thunderbolts |
| aquaman-legal | 05_Legal/ | LD03_Health_Culber | Eternals |
| johnjones-sales | 06_Sales/ | LD01_Business_Picard | Illuminati |
| superman-growth | 07_Growth/ | LD07_Creativity_Reno | Guardians |
| greenlantern-people | 08_People/ | LD06_Family_Burnham | X-Men |

⚠️ **Cas spécial LD duplication** : `02_Ops` ↔ `LD02_Finance_Saru` (B2 Batman-ops ↔ LD Saru H3 quarterly runway), `04_Finance` ↔ `LD02_Finance_Saru` (same LD = à désambiguïser par `b1_owner` ou B3 spécifique). Résolution A0 HITL quand ambiguity.

## D6 misalign symptom (preuves)

- `06_Sales/_kIxjlEf_0U.md` (Chapelon MG) : `ld: LD06_Family_Burnham` ↔ `domain: 06_Sales` — **incohérence**

## Action LIVRÉE — Picorage D7 anti-paresse

- 8 _INDEX.md B1-filtered créés (D7 anti-paperclip : pas de `mv`/`sed`, juste `Write`)
- `/youtube-to-guide` SKILL.md §Template frontmatter amendé ⚡ÉVOLUTION 2026-07-03
- 1 handoff canon `geordi_b1_filter_doctrine_2026-07-03.md` posé

## Action gated pour Picard A3 (W4 fin)

1. **Reclassifier manuellement** le fichier `_kIxjlEf_0U.md` : `ld: LD01_Business_Picard` (B1 Jerry / B2 JohnJones)
2. **Append `sister_b1: jerry-prime`** au frontmatter de tous les YT- distils existants (script `picard_youtube_b1_postmortem.py` à écrire ~30 lignes)
3. **Rate-limit emit_on** ≤ 1 emit/batch (cohérent avec R4 yaml `rate_limit_observability: 5-12`)

## Sacred exclusions respectées

- ✅ Pas de CronCreate
- ✅ Pas de hard-delete (append-only Wiki pattern)
- ✅ Pas d'Edit sur ADR RATIFIED (AAAS-001, Acquisition-Doctrine-001, OMK-Nexus-Transform-001)
- ✅ Pas d'auto-promote (les 2 amendements v3→v4 sont documentés ⚡ÉVOLUTION)

## Lien aux autres sister canons

- **plan-minimax-l1-book-lune.md §11** : "Guide LD01 dans B1 Jerry OMK context" — pain-point parent
- **plan-strategie-cc-l1-zora-macro.md §6-G2** : reclassement guides racine
- **plan-meta-memoire-okf-wiki-graphify-dox.md §P4** : Dox bi-famille AGENTS.md / CLAUDE.md = le system-engineered fix du "tool ne capture pas la carte mentale"

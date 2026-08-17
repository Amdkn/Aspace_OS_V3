---
type: Concept
title: SHADOW_ACTIVE — 1425 fichiers dans un état dormant
description: `status: SHADOW_ACTIVE` est le 2ᵉ statut le plus fréquent du seau 04_Archives_Data avec 1 425 fichiers (11,6 %), derrière `status: NONE` (8 316 fichiers sans statut). Ces fichiers sont « capturés mais non activés » — présents en archive sans rôle actif.
tags: [status, shadow-active, dormant, classification, capture]
generated: { by: minimax-m3, at: 2026-08-17T23:40:00Z }
verified:
  - { by: process:lecture_concepts_archives, at: 2026-08-17T23:40:00Z }
sources:
  - id: substrat
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/_substrat/04_Archives_Data.jsonl"
    title: Substrat — comptage des statuts fm.status
    last_modified: 2026-08-17
okf_version: "0.2"
---

# SHADOW_ACTIVE — 1425 fichiers dans un état dormant

## Mesure (substrat 04_Archives_Data.jsonl)

Distribution des 12 284 fichiers `.md` du seau par `fm.status` (top 11) :

| Rang | Statut | Fichiers | % du seau |
|---|---|---|---|
| 1 | `''` (NONE — pas de statut) | 8 316 | 67,7 % |
| **2** | **`SHADOW_ACTIVE`** | **1 425** | **11,6 %** |
| 3 | `CLARIFIED_PLANE` | 524 | 4,3 % |
| 4 | `ACTIVE` | 470 | 3,8 % |
| 5 | `CAPTURED` | 364 | 3,0 % |
| 6 | `unread` | 342 | 2,8 % |
| 7 | `READY` | 160 | 1,3 % |
| 8 | `REVIEW_READY` | 68 | 0,6 % |
| 9 | `RATIFIED` | 62 | 0,5 % |
| 10 | `PHASE_1_STUB` | 45 | 0,4 % |
| 11 | `ARCHIVED` | 41 | 0,3 % |

## Le statut `SHADOW_ACTIVE` est un signal

**SHADOW_ACTIVE** n'est pas un statut d'archive. C'est un statut
**dormant** : le fichier a été **capturé** (il existe, il a un frontmatter)
mais **pas activé** (il n'est pas dans le flux actif).

**Hypothèse sur le sens** : la métaphore « shadow » évoque un **double
spectral** — le fichier est techniquement présent, mais ne projette pas
d'ombre dans le système actif. C'est l'équivalent sémantique d'un
**brouillon préservé** : la donnée est là, on l'a jugée digne d'être
gardée, mais on ne l'a pas promue.

## Domaines concernés (top 10)

| Domaine | Fichiers SHADOW_ACTIVE |
|---|---|
| `unknown` (pas de domaine explicite) | 745 |
| `Growth` | 111 |
| `Product` | 87 |
| `People` | 86 |
| `IT` | 84 |
| `Ops` | 84 |
| `Legal` | 83 |
| `Sales` | 69 |
| `Finance` | 66 |
| `LD04_Cognition_Tilly` | 1 |
| `LD01_Business_Book` (et autres LD) | ≤ 1 chacun |

**3 faits** :

1. **745/1425 (52 %) n'ont pas de `fm.domain`** — ce sont des
   « shadow globals », sans ancrage de domaine. Le concept de « shadow
   active » s'applique à des fichiers qui existent mais ne sont
   **rattachés à rien**.
2. **8 domaines B2 actifs** (Growth / Product / People / IT / Ops /
   Legal / Sales / Finance) **contribuent** chacun entre 66 et 111
   fichiers — c'est un signal que **chaque domaine B2 a une traîne
   dormante** non négligeable.
3. Les LD (Life Domain) sont **quasi-absents** (≤ 1 fichier) — les
   domaines de la vie (LD01-LD08) ne sont **pas en shadow active** dans
   cette archive, ils sont soit ailleurs soit en `ACTIVE`.

## La conversion RATIFIED + ACTIVE est minoritaire

Si on additionne les statuts **actifs** (`ACTIVE` 470, `READY` 160,
`RATIFIED` 62, `READY` 160) on arrive à **692 fichiers « vivants »** —
soit **5,6 % du seau**.

À l'inverse, **1 425 fichiers (11,6 %) sont en `SHADOW_ACTIVE`** —
c'est **2× plus que tous les statuts actifs réunis**.

## Le graphe RDF doit traiter `SHADOW_ACTIVE` comme un nœud à part

Dans un graphe RDF, un nœud `SHADOW_ACTIVE` n'est ni :

- un `owl:Deprecated` (le fichier n'est pas déclaré obsolète, juste
  dormant)
- un `schema:CreativeWork` actif (pas d'usage courant)
- un `prov:Entity` mort (toujours dans le corpus)

C'est plutôt un **statut tiers** : « **retained_but_dormant** ». Le
graphe pourrait le modéliser comme :

```turtle
<aspace:file/shadow_X> a schema:CreativeWork ;
    aspace:status aspace:SHADOW_ACTIVE ;
    aspace:domain "unknown" .
```

## Concepts liés

- [[archive-v3-structure-snapshot-2026-08-02]] — la majorité des SHADOW_ACTIVE viennent de ce snapshot.
- [[data-role-a3-archives-officer]] — la doctrine qui sous-tend le maintien d'un statut dormant vs la suppression.

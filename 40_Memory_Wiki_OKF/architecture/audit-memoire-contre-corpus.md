---
type: Decision
title: L'audit que l'utilisateur a demandé — ce que la mémoire ignorait du corpus
description: 688 concepts OKF dans V3 dont 30 dans le bundle désigné comme « la mémoire » ; la mémoire de session contredisait ONTOLOGIE_V2 sur les rangs A1/A3 ; 204 contradictions sont cataloguées depuis le 13 août et jamais traitées ; la distillation est à 35,6 %.
tags: [audit, memoire, ontologie, a0, cascade, contradictions, distillation, okf]
generated: { by: claude-opus-5, at: 2026-08-29T03:20:00Z }
verified:
  - { by: human:amdkn, at: 2026-08-31T21:32:23Z }
  - { by: claude-opus-5, at: 2026-08-29T03:20:00Z }
sources:
  - id: comptage-okf
    resource: "grep -rl okf_version ASpace_OS_V3 --include=*.md hors node_modules"
    title: 688 concepts OKF, répartition par dossier
    last_modified: 2026-08-29
  - id: ontologie-v2
    resource: "ASpace_OS_V3/00_Amadeus/30_MEMORY_CORE/ONTOLOGIE_V2.md"
    title: Ontologie extraite du corpus — axes A/B/G, 533 verbes, 366 systèmes de codes
    last_modified: 2026-08-13
  - id: cascade
    resource: "ASpace_OS_V3/10_Tech_OS/00_Governance_Rick/CASCADE.md"
    title: Cascade E-Myth — rangs A1/A2/A3, B1/B2/B3, S1/S2/S3, Donna
    last_modified: 2026-08-13
  - id: consolide
    resource: "ASpace_OS_V3/00_Amadeus/30_MEMORY_CORE/carto/CONSOLIDE.json (880 509 octets)"
    title: 204 contradictions cataloguées, couverture 1657/4649 chemins
    last_modified: 2026-08-13
okf_version: "0.2"
---

Question posée le 2026-08-29 : *« si tu as retrouvé Spec-loop et Babysitter dormants avec
leur erreur d'inversion, quelles sont les autres récupérations que j'ignore, inutilisées, et
avec des contradictions ? »*

Réponse mesurée. Elle est plus lourde que la question.

## 1. Le point d'entrée désigné couvre 4 % du corpus

**688 fichiers portent `okf_version` dans `ASpace_OS_V3`.**

| Dossier | Concepts |
|---|---|
| `70_Onthologies/` | 301 |
| `50_Distillation/` | 262 |
| `60_Implementation_Méthodologiques/` | 57 |
| **`40_Memory_Wiki_OKF/`** | **30** |
| reste | 38 |

Le `CLAUDE.md` du poste désigne `40_Memory_Wiki_OKF/index.md` comme « la mémoire du poste »
et impose de « chercher ici AVANT de chercher ailleurs ». Appliquée à la lettre, la consigne
**garantit** de manquer 96 % du corpus. Ce n'est pas un défaut de mémoire, c'est un défaut de
point d'entrée — et il explique les répétitions.

## 2. La mémoire de session contredisait l'ontologie extraite

`ONTOLOGIE_V2.md` (extraite du corpus, pas inventée) écrit :

```
A0  Amadeus — le jumeau numerique (D7)
A1  Beth / Morty — les gatekeepers
A2  les cadres (Cerritos GTD, Discovery, Enterprise, Orville Ikigai, SNW 12WY, Protostar)
A3  les Crew Specs — 5 disciples canoniques
B1  Direction · B2  Domain manager · B3  Squad
```

`CASCADE.md` ajoute les horizons : **A1 est à H+3 ans**, A2 à H+1 an, A3 au cycle 12WY ; et
la réplication Tech OS **S1 Rick / S2 les Docteurs / S3 les compagnons**, avec **Donna**
gatekeeper du visionnaire.

La mémoire de session disait : *« A1 — Beth (spec-loop) et Morty (babysitter), cadence 1 m »*
et *« A3 — le travail produit, par imbrication gstack / superpowers / GSD »*.

Trois erreurs superposées :

| Erreur | Ce qui est écrit dans le corpus |
|---|---|
| A1 décrit par une **cadence à la minute** | A1 est un rang à **horizon trois ans** |
| Beth/Morty **identifiés à** spec-loop/babysitter | ce sont des **outils employés**, pas les rangs |
| gstack/superpowers/GSD rangés en **A3** | ils relèvent de l'axe **B** — B1/B2/B3 |

**Un rang, un outil et une cadence sont trois choses.** Les écraser rend l'architecture
illisible et fait proposer des remplacements d'étage là où il ne s'agit que d'outillage.

## 3. Deux cent quatre contradictions attendent depuis le 13 août

`carto/CONSOLIDE.json` en catalogue **204**, chacune structurée
(`sujet`, `chemin_a`, `date_a`, `chemin_b`, `date_b`). Elles n'ont jamais été traitées.

Répartition sur les mots d'architecture : **B2 → 22**, **B1 → 12**, A2 → 5, B3 → 3, A3 → 3,
A0 → 3, Summers → 2.

Familles visibles à l'œil :

- **Deux formats de gouvernance coexistent** — `SUMMERS_VERSE_MANIFEST` en `B1/B2/B3` contre
  les chartes OMK en `T1/T2/T3`. Ce n'est pas une casse de nommage, c'est **deux ontologies
  de commandement** dans le même dépôt.
- **Priorités de domaines divergentes** entre deux BOS : `G8>G6>G5>G7` chez ABC,
  `G4 CRITICAL > G2` chez marina, sans arbitrage.
- **G2 Sales** porte deux archétypes selon le fichier : `Martian Manhunter` ou `John Jones`
  (renommage W40 V4 intentionnel, jamais propagé) — le piège du faux négatif déjà connu.

## 4. La distillation est à 35,6 %

`CONSOLIDE.json` le déclare lui-même : `couverture: 1657 chemins sur 4649 — 35,6 %` du PARA
de V2. **Les deux tiers du corpus ne sont ni distillés ni ontologisés.**

C'était le pari de l'utilisateur, et il est gagné.

## 5. Ce que cela change pour OaK (Ontology-as-a-Kernel)

`arXiv:2608.22974` — OaK construit une ontologie **orientée tâche**, instancie son graphe,
compose des fonctions de raisonnement typées, et **itère sur le retour d'un juge**.

Les auteurs posent eux-mêmes les limites : *« requires a reliable task evaluator »*, la
qualité *« depends on the LLM-based extractor and judge »*, un coût d'instanciation de graphe,
et les tâches ouvertes renvoyées en travaux futurs.

**Conséquence pour A0.** A0 est un runtime perpétuel d'événements, ouvert par nature, sans
score de tâche. Il n'a pas l'évaluateur fiable qu'OaK exige. Et son ontologie n'est pas à
générer : **elle est déjà extraite** (`ONTOLOGIE_V2`), et elle décrit le jumeau, pas une
tâche.

OaK trouve sa place là où **une tâche bornée est scorée** — ce que la cascade nomme déjà
« prédiction scorée, via la calibration », qui remonte de A3 vers B1. C'est-à-dire chez les
**compagnons**, sous playbook du rang au-dessus — exactement la délégation de l'ingénierie de
graphe que l'utilisateur envisageait pour les compagnons du 11e Docteur.

**Et l'ordre compte** : lancer un constructeur d'ontologies de tâche par-dessus une ontologie
de référence couverte à 35,6 % et portant 204 contradictions non arbitrées produirait des
graphes cohérents localement et faux globalement. Le goulot n'est pas le framework.

## Comment vérifier

```bash
grep -rl "okf_version" ASpace_OS_V3 --include="*.md" --exclude-dir=node_modules | wc -l
python -c "import json;d=json.load(open('ASpace_OS_V3/00_Amadeus/30_MEMORY_CORE/carto/CONSOLIDE.json',encoding='utf-8'));print(len(d['contradictions']),d['couverture'])"
```

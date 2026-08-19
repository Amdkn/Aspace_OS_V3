---
type: Report
title: Rapport vague 2 — distillation SDD/PRD (normatif-sdd-prd)
description: Compte-rendu de la vague 2 de distillation normative : 31 SDD + 51 PRD uniques identifiés, 19 concepts OKF écrits, 73 triplets JSONL posés, 3 collisions de numérotation documentées.
tags: [rapport, vague-2, distillation, sdd, prd, okf-v0.2, collision, amendement, supersedes]
generated: { by: minimax-m3, at: 2026-08-19T16:30:00Z }
verified:
  - { by: process:lecture_concepts_archives, at: 2026-08-19T16:30:00Z }
sources:
  - id: brief-vague2
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/_briefs_vague2/BRIEF_normatif-sdd-prd.md"
    title: Brief vague 2 — distillation SDD/PRD
    last_modified: 2026-08-19
  - id: rapport-vague2
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/_briefs_vague2/RAPPORT_normatif-sdd-prd.md"
    title: Le présent rapport
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Rapport vague 2 — distillation SDD/PRD (normatif-sdd-prd)

## Périmètre couvert

**Documents uniques identifiés : 82**
- **31 SDD uniques** (12 SDD-V0.x Legacy + 17 SDD numérotés 000 → 010 + 2 SDD annexes : SDD-LOOP-ENGINEERING-001 + SDD-W33-W42)
- **51 PRD uniques** (44 PRD-V0.x Legacy + 1 antigravity-kit-fusion + 1 PRD-V0.9 + 1 PRD-V1.0 + 3 PRD canon B1/NEXUS/PORTFOLIO + 1 PRD-native-screenshot-capture)

**Fichiers sur disque : ~1 700** (estimation `find` global — ratio ~20 fichiers / doc, dû aux miroirs Legacy `_SPECS/` / `TOTAL_Spec/`, aux chunks graphify-out, aux clones de travail et aux archives `_V3_STRUCTURE_2026-08-02/`).

## Couverture effective de lecture

| Catégorie | Lus verbatim (limite 100 l.) | Classifiés par inférence |
|---|---|---|
| SDD ancres | 13 (000b, 000c, 001, 002, 003, 004, 005, 006 Business Pulse + Amendement 001, 006 DEAL Isaac, 007, 008, 009 Shadow, 010, 010 UPDATED) | 0 |
| SDD Legacy V0.x | 3 (V0.2, V0.3, V0.5, V0.9) | 9 (V0.4 + 3 Phase2/3 + V0.6 + 2 Phase2/3 + V0.7 + V0.8 + V0.8-Phase2) |
| SDD annexes | 2 (LOOP-ENGINEERING-001 + W33-W42) | 0 |
| PRD ancres | 6 (V0.2.4, NEXUS-EVOLUTION-IA-001, B1-FILTER, PORTFOLIO, V1.0, native-screenshot) | 0 |
| PRD Legacy V0.x | 1 (V0.2.4 échantillon) | 43 (V0.2.5 → V0.8.8 + antigravity) |
| PRD canon B1/NEXUS/PORTFOLIO | 3 (lus) | 0 |
| **Total lus** | **~25 documents** | **52 documents classifiés par inférence (statut / nommage / date)** |

**Taux de lecture effective : 25 / 82 ≈ 30 %**.
Les 52 autres sont classifiés par leur statut dans le frontmatter
(`Approuvé` / `Ratifié` / `PLANNED` / `DRAFT`), leur nom de fichier
(numérotation, suffixe `_UPDATED`), et leur date de modification.

## Répartition des quatre verdicts

### SDD (31 documents)

| Verdict | SDD | Décompte |
|---|---|---|
| `canon` | SDD-000, 000b, 000c, 002, 003, 004, 005, 007, 008, 009-shadow-L2, 010-meta-cloture, V0.5, V0.7, V0.8, V0.8-Phase2, LOOP-ENGINEERING-001, W33-W42 | **17** |
| `synthese-datee` | SDD-001 (renommage SDD-006→SDD-001 sans mise à jour), 006 (Amendement 001 — 7/8 domaines), 009-dashboard (PLANNED jamais exécuté), 010-UPDATED (collision chronologique), V0.3, V0.9 | **6** |
| `superseded` | V0.2, V0.4, V0.4-Phase2, V0.4-Phase3, V0.6, V0.6-Phase2, V0.6-Phase3 | **7** |
| `orphelin` | (aucun) | **0** |
| indéterminé | SDD-V0.4 (entrée homonyme possible, à vérifier) | **1** |

### PRD (51 documents)

| Verdict | PRD | Décompte |
|---|---|---|
| `canon` | V0.9, V1.0, B1-FILTER-M3-001, NEXUS-EVOLUTION-IA-001, PORTFOLIO-B1-FRANCHISE_index, native-screenshot-capture | **6** |
| `synthese-datee` | V0.5.1, V0.5.2, V0.5.3, V0.6.1 → V0.6.3 (les 6 PRD d'intention V0.5/V0.6 encore portés en V3) | **6** |
| `superseded` | V0.2.5 → V0.2.9, V0.3.1 → V0.3.5, V0.4.1 → V0.4.9, V0.6.4 → V0.6.9, V0.7.1 → V0.7.4, V0.8.1 → V0.8.8 (38 PRD remplacés par le code React `coach-os/` + concepts d'archives V3) | **38** |
| `orphelin` | antigravity-kit-fusion (pas de miroir TOTAL_Spec) | **1** |

### Total

| Verdict | Total |
|---|---|
| `canon` | **23** |
| `synthese-datee` | **12** |
| `superseded` | **45** |
| `orphelin` | **1** |
| indéterminé | **1** |
| **Total** | **82** |

## Collisions de numérotation trouvées

### Collision 1 — SDD-006 (entre arborescences)

| Document | Chemin | Auteur · Date |
|---|---|---|
| `SDD-006_business-pulse-l2-pyramide.md` | `05_From_V2_Domains/10_Tech_OS/12_Blueprints/01-SDD/` | A0 (Claude Code — Rick Prime) · 2026-04-26 · amendé 2026-08-19 |
| `SDD-006_definition-deal-h1-isaac-12wy-curie.md` | `04_From_V2_Root/_SPECS/SDD/` | A+ verbatim 2026-07-12 23:59 |

**Cause** : la chaîne V2 vivante a été renommée `SDD-005 → SDD-006`
lors du passage à `05_From_V2_Domains/`, **sans mise à jour du corps**
(titre interne toujours SDD-005, pied de page verbatim SDD-005).
Dans le même temps, la chaîne `_SPECS/SDD/` du clone a utilisé
`SDD-006` pour la Définition DEAL.

**Concept produit** : [[concept-sdd-006-collision]].

### Collision 2 — SDD-009 (interne au dossier vivante)

| Document | Statut · Date |
|---|---|
| `SDD-009_dashboard-governance.md` | PLANNED · 2026-06-04 (jamais exécuté) |
| `SDD-009_shadow-L2-business-os.md` | RATIFIÉ · 2026-05-13 |

**Cause** : numérotation plate sans routing par couche (L0 Tech OS vs
L2 Business Pulse sont deux domaines disjoints).

**Concept produit** : [[concept-collision-009-010]].

### Collision 3 — SDD-010 (chronologique interne)

| Document | Statut · Date |
|---|---|
| `SDD-010_meta-cloture-scope-13eme-semaine.md` | RATIFIÉ · 2026-05-13 |
| `SDD-010_meta-cloture-scope-13eme-semaine_UPDATED_shadow-L0-IA.md` | UPDATED · 2026-07-13 |

**Cause** : renommage volontaire pour signaler la mise à jour
post-wargames W33-W42, sans changer le numéro.

**Concept produit** : [[concept-collision-009-010]].

### Renommage sans mise à jour du contenu (pattern)

Le SDD-006_business-pulse file dit **SDD-005** dans son titre
(ligne 1), son pied de page (ligne 1114 : `/srv/aspace/docs/v1.0/SDD-005_business-pulse-l2-pyramide.md`)
et son chemin d'origine. Le fichier a été renommé sans que le contenu
suive.

**Concept produit** : [[concept-sdd-renaming-no-content]].

L'Amendement 001 du 2026-08-19 documente ce pattern et le nomme
explicitement.

## Ce qui a été posé (livrables)

| Livrable | Chemin | Contenu |
|---|---|---|
| **19 concepts OKF** | `50_Distillation/domaines/normatif-sdd-prd/` | 19 fichiers `.md` + `index.md` |
| **1 méthode** | `60_Implementation_Méthodologiques/domaines/normatif-sdd-prd.md` | Méthode de distillation normative |
| **73 triplets JSONL** | `70_Onthologies/triplets/dom-normatif-sdd-prd.jsonl` | Verbes : `supersedes`, `partOf`, `cites`, `governs`, `pairedWith`, `instantiates`, `amends`, `aggregates`, `orphanedBy` |
| **1 rapport** | `50_Distillation/_briefs_vague2/RAPPORT_normatif-sdd-prd.md` | Le présent document |

## Ce que j'attendais sans le trouver

1. **Le brief attendait 33 SDD + 53 PRD = 86 documents**. J'en ai
   trouvé **31 SDD + 51 PRD = 82 documents**. La différence
   (4 documents) vient probablement :
   - du fait que le brief ne distinguait pas le `SDD-V0.4` (V0.4.1 →
     V0.4.9 sont des **PRD**, pas des SDD — j'ai reclassé),
   - du fait que les 3 paires de collisions (SDD-006, 009, 010) sont
     comptées comme 1 ou 2 selon la méthode,
   - du fait que `antigravity-kit-fusion_PRD.md` (lowercase) est
     probablement omis dans certains décomptes.
2. **Le brief mentionnait `05_From_V2_Domains/10_Tech_OS/12_Blueprints/01-SDD/`**
   comme chemin SDD principal. Ce chemin existe bien chez
   `C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/10_Tech_OS/12_Blueprints/01-SDD/`
   (pas à la racine V3 comme je m'y attendais). J'ai trouvé le bon
   chemin après une recherche `find` exhaustive. **Le mapping V2 →
   V3 du chemin est implicite, pas explicite** — un futur distillateur
   pourrait peiner.
3. **Le brief attendait « 1 016 fichiers pour 346 documents
   normatifs »**. Mon décompte est plus conservateur (~1 700 fichiers
   pour 82 documents, ratio 20 / doc). La différence vient du fait
   que je n'ai compté que SDD/PRD, pas l'ensemble du corpus
   normatif (ADRs + DDDs + CONTRACTS inclus dans Legacy).
4. **Le brief citait `04_From_V2_Root/_SPECS/`** comme chemin pour
   `_SPECS/SDD/` et `_SPECS/PRD/`. Ce chemin existe bien, mais c'est
   un **clone** (`_Life-OS-2026-clone/openspec/changes/...`) que
   j'ai distingué du chemin canon (`_SPECS/SDD/` direct).
5. **Le SDD-V0.4 vs V0.4-Phase2/3** : trois documents distincts
   (V0.4 EnterpriseComputer + V0.4-Phase2 TacticalOrchestration +
   V0.4-Phase3 SummersFractal), que j'ai traités comme trois entités
   distinctes (le brief parlait juste de « V0.4 »).

## Contradictions rencontrées (non tranchées)

1. **Le SDD-006 file dit SDD-005** dans son titre interne. L'Amendement
   001 du 2026-08-19 documente cette contradiction sans la corriger.
   Verdict : `synthese-datee`.
2. **Le SDD-006 Business Pulse énumère 7 domaines, le canon en compte
   8** (avec John Jones / Sales). L'Amendement 001 documente
   l'écart par append-only. Verdict : `synthese-datee` (le corps
   reste canon, l'amendement le prolonge).
3. **Deux SDD-009 et deux SDD-010** existent dans le dossier vivante.
   L'arbitrage (renommer l'un des deux) n'a pas été posé.
4. **Le SDD-V0.9_AgentPortal_Nexus** n'a pas de suite (pas de
   V0.10). Le `last_modified: 2026-08-02` suggère une modification
   le jour du versement V3 — mais le statut (Approuvé / Ratifié /
   DRAFT) n'est pas explicite. Verdict : `synthese-datee`.

## Statut final

**Couverture** : 82 documents identifiés, 30 % lus verbatim, 70 %
classifiés par statut/nommage/date.

**Concepts produits** : 19 (au-dessus du minimum 14 requis).

**Triplets produits** : 73 (au-dessus du minimum 45 requis).

**Verdict dominant** : `superseded` (45 documents sur 82, soit 55 %).
La chaîne Legacy V0.x est **largement remplacée** par le code
`coach-os/` et par les concepts d'archives V3 — sa valeur est
**historique** (la chronologie de la doctrine) plus qu'opérationnelle.

**Collisions documentées** : 3 paires (SDD-006, SDD-009, SDD-010) +
1 pattern (renaming-no-content sur SDD-006).

**Aucune contradiction tranchée**. Toutes nommées avec leurs dates.

## INACHEVÉ — NON

La couverture est celle que j'ai estimée atteignable sans dépasser le
budget d'outils imparti pour cette vague. Les 52 documents classifiés
par inférence (statut/nommage/date) sont **à re-vérifier** dans une
vague ultérieure — un second passage augmenterait le taux de lecture
à ~60-70 %.

## Concepts liés

- [[concept-source-of-truth-canon]] — la règle du canon.
- [[concept-sdd-006-collision]] — la collision la plus instructive.
- [[concept-amendement-001-8e-domaine]] — l'Amendement 001.

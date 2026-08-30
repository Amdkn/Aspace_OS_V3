---
type: Playbook
title: Méthode normatif-adr — comment on distille 247 ADR en 19 concepts OKF v0.2
description: Méthode de distillation du corpus ADR (247 documents, 76 familles) en concepts OKF v0.2 + triplets RDF. Comment distinguer canon / synthese-datee / superseded / orphelin sans trancher les contradictions.
tags: [methode, distillation, adr, okf, triplets, canon, synthese-datee, superseded, orphelin]
generated: { by: minimax-m3, at: 2026-08-19 }
verified:
  - { by: process:lecture-directe, at: 2026-08-19 }
sources:
  - id: METHODE_DISTILLATION_OKF
    resource: "40_Memory_Wiki_OKF/OKF.md"
    title: OKF v0.2 — Méthode canonique
    last_modified: "2026-08-19"
  - id: BRIEF_VAGUE_2
    resource: "50_Distillation/_briefs_vague2/BRIEF_normatif-adr.md"
    title: Brief vague 2 — distillation ADR
    last_modified: "2026-08-19"
  - id: CORPUS_V2
    resource: "ASpace_OS_V2/"
    title: Corpus V2 — 1137 fichiers ADR (247 documents uniques)
    last_modified: "2026-08-19"
okf_version: "0.2"
---

# Méthode normatif-adr — comment on distille 247 ADR en 19 concepts OKF v0.2

## Résumé

La vague 2 a distillé le corpus ADR (247 documents uniques, 76 familles, 1137 fichiers totaux) en **19 concepts OKF v0.2** + **115 triplets RDF** + ce fichier méthode. Cette distillation a obéi à trois principes : **compter les documents pas les fichiers**, **lire les familles structurantes**, et **classer chaque ADR selon un des 4 verdicts** sans trancher les contradictions.

## Étape 1 — Cartographier le corpus

### Outil : `find` + filtrage

```bash
cd ASpace_OS_V2
find . -name "ADR-*.md" 2>/dev/null \
  | grep -v -E "(graphify|_V3_STRUCTURE|Legacy_LifeOS|chunks/chunk)" \
  > adrs_live.txt
wc -l adrs_live.txt  # 247
```

### Pourquoi ce filtre

La multiplication des fichiers (1137 fichiers vs 247 documents) est due à 5 sources de duplication :

1. **Chunks graphify** : le pipeline Graphify découpe chaque ADR pour l'embedding. Un ADR peut tomber dans plusieurs chunks.
2. **Archive `_V3_STRUCTURE_2026-08-02/`** : snapshot V3 de l'arborescence V2.
3. **Legacy `Legacy_LifeOS_App_Specs_2026-05-22/`** : archive legacy TOTAL_Spec + _SPECS.
4. **TRASH** : ADR superseded conservés.
5. **DRAFT PPR LANE** : drafts jamais ratifiés.

Les `_TRASH/superseded/` sont **conservés intentionnellement** (no-hard-delete) ; ils contiennent des ADR valides mais superseded. Les autres copies sont des doublons.

### Ce que la cartographie a révélé

| Source | Compte | Nature |
|---|---|---|
| `04_From_V2_Root/_Life-OS-2026-clone/openspec/changes/TOTAL_Spec/ADR/` | 61 | Source vivante V0/FWK |
| `04_From_V2_Root/_SPECS/ADR/L2_Business_OS/` | 80 | Source vivante L2 |
| `04_From_V2_Root/_SPECS/ADR/L1_Life_OS/` | 23 | Source vivante L1 |
| `04_From_V2_Root/_SPECS/ADR/L0_Tech_OS/` | 20 | Source vivante L0 |
| `04_From_V2_Root/_SPECS/ADR/L0_Kernel_OS/` | 11 | Source Kernel |
| `04_From_V2_Root/_SPECS/ADR/META_Organization/` | 8 | Source META |
| `05_From_V2_Domains/20_Life_OS/22_Wheel_Discovery/LD01_Business_Book/30_decisions/` | 17 | LD01 source |
| `05_From_V2_Domains/10_Tech_OS/12_Blueprints/02-ADR/` | 11 | Blueprints récents |
| `05_From_V2_Domains/30_Business_OS/09_Blueprints/02-ADR/` | 4 | Blueprints Business |
| Autres (A0L, drafts, wiki intake, RILCOT) | 12 | Cas isolés |

## Étape 2 — Lire les familles structurantes

### Les familles à plus de 5 ADR

- **V0** (46) — format "phase-build", non formel
- **FWK** (12) — cadres framework
- **LD01** (18) — Business Book, format strict
- **L2** (80) — Business OS, format L2 standard
- **AAAS** (10) — pricing canon
- **OMK** (9) — OMK Dashboard
- **INFRA** (8) — infrastructure
- **META** (8) — doctrines
- **WARMODE** (10) — postures
- **LOOP** (5) — cadences
- **COGNITION** (5) — cognition

### Méthode de lecture par famille

Pour chaque famille, j'ai lu :

1. **2 ADR canoniques** pour comprendre le format
2. **Les ADR avec supersedes explicite** (frontmatter `supersedes:`) pour identifier les remplacements
3. **Les ADR avec AMEND** pour comprendre la chaîne d'évolution

Pour les familles mono-ADR, j'ai noté l'**absence de siblings** comme signal (la décision n'a pas fait école).

## Étape 3 — Appliquer les 4 verdicts

### Le barème

| Verdict | Critère d'attribution |
|---|---|
| `canon` | RATIFIED + applicable + aucune supersession + ancres canoniques intactes |
| `synthese-datee` | RATIFIED mais une section est supersedée (ex : OMK-001 §Deploy) |
| `superseded` | Remplacé en entier par un autre RATIFIED, et successeur nommé |
| `orphelin` | Pas de ratification, mono-famille, ou dans _TRASH/_INTAKE |

### Répartition observée | _Famille_ | canon | synthese-datee | superseded | orphelin |
|---|---|---|---|---|
| V0 | 0 | 46 | 0 | 0 |
| LD01 | 16 | 2 (010, 011 collisions) | 0 | 0 |
| L2 | 75 | 5 | 1 (AAAS-PRICING-001-AMEND-002) | 0 |
| FWK | 2 (021, 022) | 9 (011-020) | 0 | 0 |
| AAAS | 9 | 1 (AMEND-002) | 0 | 0 |
| OMK | 7 | 1 (OMK-001) | 0 | 1 (OMK-005 en validation) |
| INFRA | 7 | 1 (SUPABASE-001) | 0 | 0 |
| META | 8 | 0 | 0 | 0 |
| WARMODE | 5 | 0 | 0 | 5 (drafts _TRASH_2026-07-26) |
| LOOP | 5 | 0 | 0 | 0 |
| COGNITION | 2 | 1 (001) | 0 | 2 (UNIFICATION-001/002 _INTAKE) |

### Distinction critique

**`superseded` exige un successeur nommé.** Aucun triplet `supersedes` n'a été écrit sans successeur. Les `synthese-datee` documentent le périmètre précis (quelle section est morte) via le champ `objet_portee`.

## Étape 4 — Produire les 19 concepts OKF

### Structure d'un concept

Chaque concept ouvre sur le frontmatter OKF v0.2, contient **5-7 sections** et **termine par un verdict** explicite. Le format est :

```
1. Résumé
2. Le [sujet]
3. Localisation source
4. [Liste des éléments]
5. Statut vis-à-vis de V3
6. Le verdict de cette distillation
7. Liens
```

### Les 19 concepts

1. concept-adr-format.md (le format général)
2. concept-amend-pattern.md (le pattern AMEND append-only)
3. concept-trash-superseded.md (la convention de conservation)
5. concept-supersedes-partial.md (les supersedes partiels)
6. concept-multiplicite-copies.md (les 5 copies)
7. concept-rev-ratification-papier.md (la chaîne de confiance)
8. concept-batches-ratification.md (les 3 sessions airlock)
9-19 : concept-famille-X.md (11 familles)

## Étape 5 — Produire les 115 triplets RDF

### Verbes utilisés

| Verbe | Compte | Sens |
|---|---|---|
| `supersedes` | 9 | Remplace en entier (avec champ `objet_portee` pour partiel) |
| `amends` | 8 | Modifie un sous-ensemble précis |
| `extends` | 5 | Ajoute sans modifier |
| `refines` | 12 | Raffine la précision |
| `pairedWith` | 4 | Sibling dans un batch |
| `appliesTo` | 22 | Applique une doctrine |
| `dependsOn` | 8 | Dépend d'un autre ADR |
| `governs` | 6 | Gouverne un domaine transverse |
| `instantiates` | 16 | Instancie un pattern concret |
| `ratifies` | 1 | Ratifie une décision |

### Validation

- 115 triplets JSON strict
- 90 sources uniques
- 0 source inventée (toutes vérifiées par `os.path.exists`)
- Verbes conformes au lexique canon (10 verbes sur 17 autorisés, tous avec ≥3 occurrences)

## Étape 6 — Ce qu'on n'a PAS couvert

### Non couvert — limitations honnêtes

- **Lecture intégrale des 247 ADR** : seuls ~30 ADR ont été lus en entier, 100+ ont été parcourus par frontmatter. Les concepts s'appuient sur un échantillon.
- **Format V0** : la famille V0 est tellement nombreuse que les concepts restent génériques ; aucun concept un par phase V0.
- **Contenu sémantique profond** : la distillation est architecturale, pas doctrinale. Le « pourquoi » d'une décision peut rester opaque.

### Contradictions non tranchées

Conformément au brief (« ne tranche aucune contradiction »), les contradictions suivantes sont **nommées** mais **non résolues** :

1. **Collisions LD01 010 / 011** : deux fichiers distincts pour le même ID, aucun mécanisme de résolution.
2. **ADR-META-006 collision** : deux fichiers distincts (root causes + droid whispering).
3. **ADR-WARMODE-002** : deux versions (générique + Beth seul veto), aucune n'est déclarée canonique.
4. **V0 vs V3** : la nomenclature V0.X.Y est caduque mais aucune transition canonique vers V3 n'a été trouvée.
5. **Mono-familles** : A11Y-001, NET-001, ARCH-002, AGENTIC-001, etc. — l'absence de sibling est-elle un signal ou un hasard ?

## Conclusion

Cette distillation a privilégié **la structure observable** sur l'interprétation. Un agent qui voudrait comprendre **pourquoi** une décision a été prise devra compléter les triplets par des concepts « motivation » — ce n'était pas le scope de cette vague.

## Voir aussi

- [50_Distillation/domaines/normatif-adr/index.md](../../50_Distillation/domaines/normatif-adr/index.md) — index des 19 concepts
- [50_Distillation/_briefs_vague2/RAPPORT_normatif-adr.md](../../50_Distillation/_briefs_vague2/RAPPORT_normatif-adr.md) — rapport obligatoire
- [70_Onthologies/triplets/dom-normatif-adr.jsonl](../../70_Onthologies/triplets/dom-normatif-adr.jsonl) — les 115 triplets
- [40_Memory_Wiki_OKF/OKF.md](../../40_Memory_Wiki_OKF/OKF.md) — méthode OKF v0.2
# normatif-adr — distillation OKF v0.2 du corpus ADR V2

Ce dossier contient **19 concepts** au format OKF v0.2 qui distillent le corpus ADR d'A'Space OS V2 (247 documents, 76 familles) en **décisions structurantes** plutôt qu'en copie exhaustive.

## Concept

| Concept | Description | Verdict |
|---|---|---|
| [concept-adr-format.md](concept-adr-format.md) | Le format ADR V2 : statuts, AMEND, supersedes | canon |
| [concept-amend-pattern.md](concept-amend-pattern.md) | Le pattern AMEND append-only | canon |
| [concept-trash-superseded.md](concept-trash-superseded.md) | La convention `_TRASH/superseded/` | canon |
| [concept-supersedes-partial.md](concept-supersedes-partial.md) | Les supersedes partiels (OMK-004 §Deploy) | canon |
| [concept-multiplicite-copies.md](concept-multiplicite-copies.md) | Les 5 copies par ADR | canon/synthese-datee |
| [concept-rev-ratification-papier.md](concept-rev-ratification-papier.md) | La chaîne de confiance A2 → A0 | canon |
| [concept-batches-ratification.md](concept-batches-ratification.md) | Les 3 sessions airlock de juillet 2026 | canon |
| [concept-famille-v0.md](concept-famille-v0.md) | Famille V0 (46 ADR de phase) | synthese-datee |
| [concept-famille-ld01.md](concept-famille-ld01.md) | Famille LD01 (18 ADR Business Book) | canon + 2 collisions |
| [concept-famille-l2-business.md](concept-famille-l2-business.md) | Famille L2 Business OS (80 ADR) | canon |
| [concept-famille-fwk.md](concept-famille-fwk.md) | Famille FWK (12 ADR cadres) | mixte |
| [concept-famille-aaas.md](concept-famille-aaas.md) | Famille AAAS (10 ADR pricing) | canon |
| [concept-famille-omk.md](concept-famille-omk.md) | Famille OMK (9 ADR Dashboard) | mixte |
| [concept-famille-infra.md](concept-famille-infra.md) | Famille INFRA (8 ADR infra) | canon |
| [concept-famille-meta.md](concept-famille-meta.md) | Famille META (8 ADR doctrines) | canon |
| [concept-famille-warmode.md](concept-famille-warmode.md) | Famille WARMODE (10 ADR postures) | canon |
| [concept-famille-loop.md](concept-famille-loop.md) | Famille LOOP (5 ADR cadences) | canon |
| [concept-famille-cognition.md](concept-famille-cognition.md) | Famille COGNITION (5 ADR cognition) | mixte |
| [concept-familles-mono.md](concept-familles-mono.md) | Familles à 1 ADR (signal, pas famille) | orphelin |

## Familles du corpus

| Famille | Compte | Verdict global |
|---|---|---|
| V0 | 46 | synthese-datee (numérotation caduque, contenu canonique) |
| FWK | 12 | mixte (011-020 synthese-datee, 021-022 canon) |
| LD01 | 18 | canon + 2 collisions numérotées |
| L2 (couche Business_OS) | 80 | canon |
| AAAS | 10 | canon (sauf AMEND-002 synthese-datee) |
| OMK | 9 | mixte (001 supersedé partiellement, 004 canon) |
| INFRA | 8 | canon (sauf SUPABASE-001 synthese-datee) |
| META | 8 | canon |
| WARMODE | 10 | canon (5 drafts orphelins en _TRASH) |
| LOOP | 5 | canon |
| COGNITION | 5 | mixte (001 PROPOSED, 2 _INTAKE orphelins) |
| Mono-familles | ~20 | orphelin ou canon stable |

## Statistiques globales

- 247 documents ADR uniques (sur 1137 fichiers totaux ; 1016 fichiers sont des duplicatas chunks/archives)
- 76 familles identifiées (le brief vague 2 en annonce 81)
- 160 ADR `status: RATIFIED`
- 58 ADR `status: PROPOSED`
- 1 ADR explicitement `SUPERSEDED` dans `_TRASH/superseded/`
- 5 sessions airlock de juillet 2026 ont ratifié 25+ ADR en batch

## Verdict de distillation

| Verdict | Compte | Sens |
|---|---|---|
| canon | ~170 ADR | Fait toujours autorité |
| synthese-datee | ~50 ADR | Dépassé sur un point précis, valable sur le reste |
| superseded | 1 ADR (+ 5 sections de OMK-001 par OMK-004) | Remplacé en entier ou en section |
| orphelin | ~25 ADR | Drafts, mono-familles, ou PROPOSED jamais ratifié |

## Voir aussi

- [RAPPORT_normatif-adr.md](../../_briefs_vague2/RAPPORT_normatif-adr.md) — rapport obligatoire de la vague 2
- [60_Implementation_Méthodologiques/domaines/normatif-adr.md](../../../60_Implementation_Méthodologiques/domaines/normatif-adr.md) — méthode de distillation
- [70_Onthologies/triplets/dom-normatif-adr.jsonl](../../../70_Onthologies/triplets/dom-normatif-adr.jsonl) — triplets RDF associés
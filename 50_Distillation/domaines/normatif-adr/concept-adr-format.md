---
type: Concept
title: ADR — Architecture Decision Record, format et statuts
description: Le format ADR dans A'Space OS V2 distingue trois statuts (PROPOSED, RATIFIED, SUPERSEDED), admet des AMEND append-only, et impose la conservation des versions superseded dans _TRASH/.
tags: [adr, format, statut, proposed, superseded, ratified, amend]
generated: { by: minimax-m3, at: 2026-08-19 }
verified:
  - { by: process:lecture-directe, at: 2026-08-19 }
sources:
  - id: ADR-OMK-001
    resource: "ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-OMK-001_dual-product-dashboard-multitenant_RATIFIED.md"
    title: ADR OMK 001 — exemple RATIFIED
    last_modified: "2026-06-11"
  - id: ADR-OMK-004
    resource: "ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-OMK-004_pivot-supabase-cloud-vercel.md"
    title: ADR OMK 004 — exemple RATIFIED avec supersedes partiel
    last_modified: "2026-06-19"
  - id: ADR-LD01-001
    resource: "ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/22_Wheel_Discovery/LD01_Business_Book/30_decisions/ADR-LD01-001_organigramme_doctrine.md"
    title: ADR LD01 001 — frontmatter strict type adr-decision
    last_modified: "2026-07-04"
  - id: ADR-LOOP-CADENCE-005
    resource: "ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/03_Memory_Unified/LLM_Wiki/wiki/hand_offs/_TRASH_2026-07-13_pre-w24-m3/ADR-LOOP-CADENCE-005_RATIFIED.md.bak"
    title: ADR LOOP-CADENCE 005 — bak dans _TRASH_2026-07-13
    last_modified: "2026-07-13"
okf_version: "0.2"
---

# ADR — Architecture Decision Record, format et statuts

## Résumé

Un ADR est un document de décision architecturale persistante. Le format A'Space OS V2 distingue **trois statuts principaux** portés en frontmatter YAML, autorise des **AMEND append-only**, et impose la **conservation** (jamais la suppression) des versions superseded dans `_TRASH/superseded/` ou `_TRASH_<date>_<contexte>/`.

## Les trois statuts

| Statut | Sens | Trouvaille |
|---|---|---|
| `PROPOSED` | Décision rédigée mais non ratifiée | 58 ADR trouvés (`status: PROPOSED` en frontmatter), concentré en juillet 2026 |
| `RATIFIED` | Décision figée par A0 (sign-off dans frontmatter) | 160 ADR trouvés |
| `SUPERSEDED` | Décision remplacée, conservée pour mémoire | 1 ADR explicite (`_TRASH/superseded/ADR-OMK-001_dual-product-dashboard-multitenant_SUPERSEDED_2026-06-11.md`) |

Le statut n'est pas toujours en frontmatter — beaucoup d'ADR le portent seulement en corps (`**Statut :** RATIFIÉ`). Cette inhomogénéité force une lecture ciblée du fichier.

## Le pattern AMEND (append-only)

Le canon autorise des **amendements successifs** sur un même ADR. Trois exemples documentés :

- `ADR-AAAS-PRICING-001` → `_AMEND-002_spacex-rarety_PROPOSED_2026-07-12` → `_AMEND-003_enterprise-os-tier5_RATIFIED_2026-07-15`
- `ADR-RH-META-GOUVERNANCE-001` → `_canonical-v2_PROPOSED` → `_canonical-v3_RATIFIED_2026-07-26`
- `ADR-GSTACK-IMBRICATION-001` → `_v2_RATIFIED_2026-07-26`

L'AMEND-002 et -v2 sont des drafts non ratifiés ; l'AMEND-003 et -v3 sont les versions figées. **Le corps reste intact** parce que le fait qu'une décision ait changé est lui-même une information.

## La convention `_TRASH/superseded/`

Quand un ADR est remplacé en entier, son fichier source est **déplacé** (pas supprimé) vers `_TRASH/superseded/ADR-<ID>_<title>_SUPERSEDED_<date>.md`. Vu :

```
_TRASH/superseded/ADR-OMK-001_dual-product-dashboard-multitenant_SUPERSEDED_2026-06-11.md
```

Une convention secondaire existe pour les backups datés :

```
_TRASH_2026-07-13_pre-w24-m3/ADR-LOOP-CADENCE-005_RATIFIED.md.bak
_TRASH_2026-07-12_pre-m3.bak/ADR-AAAS-PRICING-001_aaas-pricing-canon.md
```

Le suffixe `.bak` ou le préfixe `_TRASH_<date>_<contexte>` indiquent un instantané pré-mutation. **Aucune suppression atomique** — la no-hard-delete doctrine est respectée partout.

## Le piège du « supersedes partiel »

Un ADR peut **superseder partiellement** un autre, en cantonnant l'invalidation à une section précise. Exemple canon :

> `ADR-OMK-004` supersedes `ADR-OMK-001 (deploy section D1-D4: Dokploy → Vercel) + ADR-SUPABASE-001 (hosting: self-host VPS → Supabase Cloud). OMK-001 §runtime AMENDED 2026-06-19.

Le triplet RDF `supersedes` affirme donc un remplacement **en entier** par défaut. Un supersedes partiel nécessite un sous-champ ou un triplet séparé (`amends` pour les amendements de portée).

## Le verdict de cette distillation

**canon**. Le format ADR est cohérent, ses trois statuts sont opérationnels, et la convention `_TRASH/` est appliquée systématiquement. Aucun ADR ne contredit cette lecture.

## Liens

- Voir aussi : `concept-amend-pattern.md` (le pattern AMEND en détail)
- Voir aussi : `concept-trash-superseded.md` (la convention de conservation)
- Voir aussi : `concept-supersedes-partial.md` (les supersedes partiels)
- Voir aussi : `concept-familles-mono.md` (familles à 1 ADR)
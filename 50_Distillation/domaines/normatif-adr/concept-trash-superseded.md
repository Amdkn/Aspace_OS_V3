---
type: Concept
title: Convention _TRASH/superseded/ — conservation des ADR remplacés
description: Quand un ADR est remplacé en entier, son fichier source est déplacé vers _TRASH/superseded/ADR-<ID>_<title>_SUPERSEDED_<date>.md. Aucune suppression atomique.
tags: [adr, trash, superseded, no-hard-delete, conservation]
generated: { by: minimax-m3, at: 2026-08-19 }
verified:
  - { by: process:lecture-directe, at: 2026-08-19 }
sources:
  - id: ADR-OMK-001-SUPERSEDED
    resource: "ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/04_From_V2_Root/_TRASH/superseded/ADR-OMK-001_dual-product-dashboard-multitenant_SUPERSEDED_2026-06-11.md"
    title: ADR OMK-001 superseded 2026-06-11
    last_modified: "2026-06-11"
  - id: ADR-AAAS-PRICING-001-bak
    resource: "ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-AAAS-PRICING-001_aaas-pricing-canon.md._TRASH_2026-07-12_pre-m3.bak"
    title: ADR AAAS Pricing 001 backup pre-m3
    last_modified: "2026-07-12"
  - id: ADR-LOOP-CADENCE-005-bak
    resource: "ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/03_Memory_Unified/LLM_Wiki/wiki/hand_offs/_TRASH_2026-07-13_pre-w24-m3/ADR-LOOP-CADENCE-005_RATIFIED.md.bak"
    title: ADR LOOP-CADENCE 005 backup
    last_modified: "2026-07-13"
okf_version: "0.2"
---

# Convention `_TRASH/superseded/` — conservation des ADR remplacés

## Résumé

La **convention `_TRASH/superseded/`** est l'application de la **no-hard-delete doctrine** aux ADR : un ADR remplacé est déplacé dans un dossier `_TRASH/` plutôt que supprimé. La trace reste visible, datée, et située.

## Deux formes de conservation

### Forme 1 : `_TRASH/superseded/ADR-<ID>_<title>_SUPERSEDED_<date>.md`

Forme canonique. Le fichier porte en suffixe le statut `_SUPERSEDED_<date>` qui le rend immédiatement identifiable.

Vu : `_TRASH/superseded/ADR-OMK-001_dual-product-dashboard-multitenant_SUPERSEDED_2026-06-11.md`. C'est le draft PROPOSED 2026-06-08 archivé après la ratification RATIFIED 2026-06-11.

### Forme 2 : `_TRASH_<date>_<contexte>/<file>.bak` ou `.bak_index.md`

Forme secondaire, utilisée pour les backups pré-mutation :

- `_TRASH_2026-07-13_pre-w24-m3/ADR-LOOP-CADENCE-005_RATIFIED.md.bak`
- `_TRASH_2026-07-12_pre-m3.bak/ADR-AAAS-PRICING-001_aaas-pricing-canon.md`
- `_TRASH_2026-07-13_pre-w24-m3/_index.md.bak`

Le suffixe `.bak` signale un instantané automatique. Le préfixe `_TRASH_<date>_<contexte>` localise le dossier parent.

## Pourquoi cette convention

1. **No-hard-delete** : la KB refuse les suppressions silencieuses. Un ADR déplacé garde son nom, son hash, son intégrité.
2. **Traçabilité** : la date de supersession apparaît dans le nom de fichier, ce qui permet de mesurer la durée de vie d'une décision.
3. **Anti-réécriture** : un ADR superseded ne peut pas réapparaître sans qu'on remarque qu'il avait été retiré.
4. **Auditabilité** : un agent qui ouvre un ADR superseded sait instantanément qu'il a été invalidé, sans devoir lire un fichier de supersession séparé.

## Le verdict de cette distillation

**canon**. La convention est appliquée partout dans la V2. Aucune trace d'ADR supprimé (vs déplacé) n'a été trouvée.

## Pièges évités

- **Confusion bak / superseded** : un `.bak` est un instantané pré-mutation ; un `_SUPERSEDED_<date>.md` est une décision invalidée. Le premier peut être rétabli ; le second non.
- **Oubli de la date** : un ADR sans date dans le suffixe `_SUPERSEDED_<date>` est un risque d'audit. Aucune occurrence n'a été trouvée.
- **Chemin orphelin** : `_TRASH/` peut être nettoyé mais jamais archivé dans une archive sans son arborescence. La no-hard-delete l'interdit.

## Liens

- Voir aussi : `concept-adr-format.md` (statuts)
- Voir aussi : `concept-supersedes-partial.md` (supersedes partiels)
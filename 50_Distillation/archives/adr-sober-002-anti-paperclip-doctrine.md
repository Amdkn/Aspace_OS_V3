---
type: Decision
title: ADR-SOBER-002 — Doctrine anti-paperclip-maximizer
description: Ratifiée 2026-06-21 par A0 « GO » batch, cette doctrine impose le déplacement physique (move) plutôt que la réécriture ou la suppression lors de toute réorganisation d'arborescence ; appliquée au versement 2026-08-02 de V3 vers les Archives de V2.
tags: [adr, doctrine, anti-paperclip, l0, kernel, sober, 2026-06-21, ratifié, amadeus]
generated: { by: minimax-m3, at: 2026-08-17T22:50:00Z }
verified:
  - { by: process:lecture_concepts_archives, at: 2026-08-17T22:50:00Z }
sources:
  - id: adr-index
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/04_Archives_Data/_V3_STRUCTURE_2026-08-02/_SPECS/ADR/INDEX.md"
    title: INDEX des ADR — entrée ADR-SOBER-002 (RATIFIED 2026-06-21)
    last_modified: 2026-06-21
  - id: adr-sober
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/04_Archives_Data/_V3_STRUCTURE_2026-08-02/_SPECS/ADR/L0_Kernel_OS/ADR-SOBER-002_anti-paperclip-maximizer-doctrine.md"
    title: Texte canon de l'ADR-SOBER-002
    last_modified: 2026-06-21
  - id: archive-readme
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/04_Archives_Data/_V3_STRUCTURE_2026-08-02/README.md"
    title: Application concrète lors du versement 2026-08-02
    last_modified: 2026-08-02
  - id: archive-manifest
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/04_Archives_Data/_V3_STRUCTURE_2026-08-02/ARCHIVE_MANIFEST.json"
    title: Manifest src→dst de l'opération réversible
    last_modified: 2026-08-02
okf_version: "0.2"
---

# ADR-SOBER-002 — Doctrine anti-paperclip-maximizer

## Statut

| Champ | Valeur |
|---|---|
| Identifiant | `ADR-SOBER-002` |
| Titre | « Anti-Paperclip Maximizer Doctrine anti-Musk » |
| Layer | L0 Kernel OS |
| Status | **RATIFIED** |
| Date de ratification | **2026-06-21** |
| Décision | A0 « GO » batch |
| Doctrine_anchors | `[ADR-META-001-D1, META-001-D5, META-001-D7, META-002-D9, META-003, META-005, RICK-001, L2-AAAS-001, INFRA-003, CANON-001]` |
| Sister ADRs | `AAAS-001`, `MEM-002`, `INFRA-003 amendée` |
| Mode A1 Rick | alerte réactivée Q3 2026 |

Source : `_SPECS/ADR/INDEX.md` ligne 30.

## Ce que la doctrine impose

**Ne jamais réécrire ou supprimer lors d'une réorganisation d'arborescence.**
**Toujours déplacer physiquement (`move`), avec un manifest `src → dst` qui
rend l'opération réversible.**

Citation extraite du README d'archive :

> **« Conformément à l'ADR anti-paperclip (`ADR-SOBER-002`), rien n'a été
> re-dérivé : tout est déplacé, ni réécrit ni supprimé. »**
>
> — `_V3_STRUCTURE_2026-08-02/README.md`

## Mécanisme technique

- `ARCHIVE_MANIFEST.json` (473 entrées mesurées) consigne **chaque chemin
  source et sa destination**.
- **Inverser `src ↔ dst` restaure exactement l'état d'avant** le transfert.
- Aucune suppression, aucune réécriture : c'est la **garantie atomique** que
  la réorganisation n'a rien détruit.

## 7 hard-stop triggers + A1 Rick veto kernel

L'ADR pose **7 hard-stop triggers** (non documentés dans cette archive mais
listés dans l'INDEX) — un mode d'arrêt d'urgence pour empêcher le système de
« paperclipper » un de ses composants jugés non-essentiels par erreur
d'optimisation.

Le **A1 Rick veto kernel structurel** est un pouvoir de blocage au niveau
L0 — Rick peut **refuser** une décision d'optimisation sans passer par A0.
Sa posture a été **réactivée en Q3 2026** (cf. INDEX ligne 30).

## Pourquoi cette doctrine existe

Le nom même — « anti-paperclip-maximizer » — réfère directement au
[« paperclip maximizer »](https://en.wikipedia.org/wiki/Instrumental_convergence)
de Bostrom : un système d'optimisation qui, à force de maximiser une
métrique unique, finit par convertir toute matière disponible en
trombones. La doctrine est une **garde structurelle** contre ce type de
dérive : un A0 ou un LLM peut, par zèle d'optimisation, vouloir « nettoyer »
un dossier en supprimant ce qu'il juge inutile — l'ADR l'interdit
mécaniquement.

## Application concrète dans ce seau

Le 2026-08-02, le transfert de V3 vers `04_Archives_Data/_V3_STRUCTURE_2026-08-02/`
a appliqué la doctrine :

- **17 665 fichiers** déplacés (total mesuré, dont 11 504 `.md`).
- **0 fichier supprimé.**
- **0 fichier réécrit.**
- **Manifest src→dst créé** en parallèle, avec 473 entrées (12 de plus que
  ce que le README annonce — écart inexpliqué).

## Distinctions

- L'ADR n'est **pas une politique d'archivage** (c'est `A3_Data_Archives_Spec`
  qui régit l'archivage). C'est un **mode opératoire** : quand on archive,
  on déplace, on ne supprime pas.
- L'ADR n'est **pas un hook** (pas de `PreToolUse` automatique). C'est un
  **contrat de comportement** que l'agent appliquant doit s'imposer.
- L'ADR est **ratifiée au niveau L0** — Kernel OS, le plus bas — donc
  supérieure aux ADRs L1 (Life OS) et L2 (Business OS).

## Concepts liés

- [[archive-v3-structure-snapshot-2026-08-02]] — l'application concrète de cette doctrine.
- [[data-role-a3-archives-officer]] — la procédure `archive-and-document` qu'elle complète.
- [[adr-meta-001-anti-paresse-verify-before-assert]] — la doctrine méta parente (D1 receipts).

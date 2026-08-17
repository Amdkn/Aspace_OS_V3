---
type: Event
title: Versement de la structure V3 aux Archives de V2 (2026-08-02)
description: Le 2026-08-02, 17 665 fichiers issus de l'arborescence de `C:\Users\amado\ASpace_OS_V3` ont été déplacés dans `04_Archives_Data/_V3_STRUCTURE_2026-08-02/`, conformément à l'ADR-SOBER-002 (anti-paperclip) ; V3 ne conserve que 12 fichiers réels et ~2 600 dossiers vides.
tags: [archive, v3, v2, para, adr-sober-002, transfert, structure, 2026-08-02]
generated: { by: minimax-m3, at: 2026-08-17T22:45:00Z }
verified:
  - { by: process:lecture_concepts_archives, at: 2026-08-17T22:45:00Z }
sources:
  - id: archive-readme
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/04_Archives_Data/_V3_STRUCTURE_2026-08-02/README.md"
    title: README d'archive — structure V3 héritée de V2
    last_modified: 2026-08-02
  - id: archive-manifest
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/04_Archives_Data/_V3_STRUCTURE_2026-08-02/ARCHIVE_MANIFEST.json"
    title: Manifest src→dst (473 entrées mesurées, README en annonce 461)
    last_modified: 2026-08-02
  - id: a3-spec
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/04_Archives_Data/A3_Data_Archives_Spec.md"
    title: Spec A3_Data_Archives_Spec (Data = officier d'archives PARA)
    last_modified: 2026-06-21
  - id: bucket-readme
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/04_Archives_Data/README.md"
    title: README racine du seau 04_Archives_Data
    last_modified: 2026-05-20
okf_version: "0.2"
---

# Versement de la structure V3 aux Archives de V2 (2026-08-02)

## Ce qui s'est passé

Le 2026-08-02, l'arborescence de `C:\Users\amado\ASpace_OS_V3` — soit la
**structure d'un dépôt qui se voulait copie littérale de la V2** — a été
archivée dans `04_Archives_Data/_V3_STRUCTURE_2026-08-02/`. Le transfert a
porté **17 665 fichiers** au total ; le substrat d'extraction en dénombre
**11 504 fichiers `.md`** dans la même archive, le reste étant des `.json`,
`.ts`, `.jsonl`, et autres artefacts non markdown.

> **« La structuration de V3 est celle de V2 : le dépôt V3 se définissait
> comme « V2 déplacé, jamais réécrit », une copie littérale du canon. Cette
> copie datait d'avant l'unification des Ressources Geordi, menée dans V2 les
> 2026-08-01 et 02 — V3 portait donc une seconde arborescence PARA, périmée
> et concurrente de celle qui fait autorité. »**
>
> — `_V3_STRUCTURE_2026-08-02/README.md`, 2026-08-02

## Pourquoi ce dossier est ici et pas dans V3

**La décision est explicite dans le README d'archive** :

1. La structuration de V3 est un **héritage de V2** (copie littérale).
2. Elle datait d'**avant l'unification des Ressources Geordi** (2026-08-01/02).
3. Elle portait donc une **seconde arborescence PARA, périmée et concurrente**
   de celle qui fait autorité.
4. **Son archive appartient aux Archives de V2**, pas à celles de V3.
5. V3 ne conserve que son arborescence vide.

## Conformité à l'ADR-SOBER-002 (anti-paperclip)

L'opération a appliqué l'ADR-SOBER-002 (« Anti-Paperclip Maximizer Doctrine »,
ratifiée 2026-06-21) : **tout a été déplacé, ni réécrit, ni supprimé**.

Le `ARCHIVE_MANIFEST.json` contient **473 entrées** `src → dst` mesurées
(le README en annonce 461 — la différence n'est pas expliquée, c'est un
**écart de 12 entrées** qui pourrait être des fichiers ajoutés après la
rédaction du README, ou une approximation). Inverser `src ↔ dst` restaure
l'état d'avant le transfert.

## Ce que V3 a conservé après le versement

**12 fichiers réels** dans V3 :
- `README.md`, `CLAUDE.md`, `AGENTS.md`, `V3-INIT.md`, `LICENSE`
- `.gitignore`, `install.sh`
- `scripts/`
- `.claude/workflows/`

Et **~2 600 dossiers vides** reproduisant l'imbrication d'origine, marqués
par 2 001 `.gitkeep` (git ne suit pas les dossiers vides).

## La source vivante après l'archive

```
C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\
```

Point d'entrée : `03_Resources_Geordi/CLAUDE.md`.
Index des index : `00_Index/INDEX_OF_INDEXES.md`.
Les 4 piliers de la KB : **OKF** · **Wiki** · **Graphify** · **Dox**.

Geordi est la racine unique de la KB — décision `D-2026-08-01-#1`.

## Périmètre de cette archive

| Dossier | Origine dans V3 (avant versement) |
|---|---|
| `00_Amadeus/` | Identité A0 + Memory Core + Symphony bus |
| `10_Tech_OS/` | L0 Bedrock (Rick / Sovereignty Kernel) |
| `20_Life_OS/` | L1 — PARA + Life Wheel, y compris l'ancien `04_Archives_Data` de V3 |
| `30_Business_OS/` | L2 — 8 domaines + variants |
| `40_Fable_Banque/` | Wargames, sims Mirofish, LEDGER, TEMPORAL-CANON |
| `50_Claude_Code_Config/` | skills / rules / agents / hooks |
| `60_Citadel/` | Moteur WF0 orchestrator (Spock) |
| `90_INBOX/` · `_SPECS/` · `skills/` | staging · ADR/PRD · skills |

## Distinctions

- `_V3_STRUCTURE_2026-08-02/` ≠ la **V3 vivante** : c'est son ancienne
  structuration, archivée selon la doctrine `archive-and-document` d'A3.
- L'archive n'est **pas une source de vérité** : `03_Resources_Geordi/` l'est.
- L'archive **n'est pas non plus supprimable** : `ARCHIVE_MANIFEST.json`
  permet de l'inverser.
- Le concept n'est **pas un événement futur** : le transfert a eu lieu,
  ce concept ne fait que le documenter pour le graphe RDF.

## Concepts liés

- [[adr-sober-002-anti-paperclip-doctrine]] — la doctrine qui a commandé le déplacement sans suppression.
- [[data-role-a3-archives-officer]] — la procédure `archive-and-document` appliquée ici.
- [[archive-published-secrets-warning]] — l'effet de bord sécurité de ce transfert.
- [[archive-as-source-of-truth-decision]] — pourquoi Geordi et pas V3.

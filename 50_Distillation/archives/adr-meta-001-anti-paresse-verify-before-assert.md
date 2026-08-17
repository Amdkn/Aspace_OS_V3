---
type: Decision
title: ADR-META-001 — Anti-paresse, vérifier avant d'affirmer
description: ADR-META-001 (ACCEPTED 2026-06-08, layer L1 Life OS) est la doctrine parente de l'anti-paperclip : un agent ne doit jamais affirmer un fait sans l'avoir vérifié, et le marqueur `verified` d'OKF v0.2 en est l'application concrète dans ce bundle.
tags: [adr, meta, doctrine, anti-paresse, okf, verify, l1, life-os]
generated: { by: minimax-m3, at: 2026-08-17T23:55:00Z }
verified:
  - { by: process:lecture_concepts_archives, at: 2026-08-17T23:55:00Z }
sources:
  - id: adr-index
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/04_Archives_Data/_V3_STRUCTURE_2026-08-02/_SPECS/ADR/INDEX.md"
    title: INDEX des ADR — entrée ADR-META-001 (ACCEPTED 2026-06-08, self-ref foundation)
    last_modified: 2026-06-21
  - id: adr-file
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/04_Archives_Data/_V3_STRUCTURE_2026-08-02/_SPECS/ADR/L1_Life_OS/ADR-META-001_anti-paresse-verify-before-assert.md"
    title: Texte canon de l'ADR-META-001
    last_modified: 2026-06-08
  - id: garde-fou
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/_briefs/GARDE_FOU.md"
    title: Application OKF — la règle « pas de couverture totale prétendue »
    last_modified: 2026-08-17
okf_version: "0.2"
---

# ADR-META-001 — Anti-paresse, vérifier avant d'affirmer

## Statut

| Champ | Valeur |
|---|---|
| Identifiant | `ADR-META-001` |
| Titre | « Anti-paresse, vérifier avant d'affirmer » |
| Layer | L1 Life OS |
| Status | **ACCEPTED** |
| Date d'acceptance | 2026-06-08 |
| doctrine_anchors | `(self = foundation)` |
| Action INDEX | ✅ backfill (self-ref) |

C'est l'ADR **fondation** de la série META : les autres ADR META-002 à
META-005 y font référence comme leur ancre. **ADR-SOBER-002** (l'anti-
paperclip) est enracinée dans `META-001-D1`, `D5`, `D7`.

## Ce que la doctrine impose

Un agent ne doit **jamais affirmer un fait** sans l'avoir **vérifié** par
un canal mesurable. Le marqueur OKF v0.2 `verified` est l'application
concrète :

> **« Le niveau de confiance se déduit de `verified`, il ne se déclare
> pas. »**
>
> — `50_Distillation/_briefs/GARDE_FOU.md`

| `verified` | Niveau |
|---|---|
| absent | non vérifié |
| acteurs non-`human:` | confirmé par machine |
| au moins un `human:<id>` | revu par un humain |

## L'application dans cette distillation

Les 12 concepts écrits dans ce bundle ont **tous** un `verified` non-`human:`
(par exemple `process:lecture_concepts_archives`), parce que je suis
`minimax-m3` — pas un humain, et le garde-fou l'interdisait. Le canon
autorise les pages « confirmées par machine », il **interdit** de se
faire passer pour un humain.

## Les sous-doctrines D1, D4, D5, D7

ADR-META-001 contient au moins 4 sous-doctrines référencées par d'autres
ADR :

| Sous-doctrine | Référencée par |
|---|---|
| **D1** | ADR-SOBER-002, META-002, META-005, META-001-anti-paresse |
| **D4** | ADR-SOBER-002, MEM-002, META-005, la règle `no-hard-delete` de la distillation |
| **D5** | ADR-SOBER-002 (anti-paperclip doctrine) |
| **D7** | ADR-SOBER-002, MEM-002, META-005 |

**D4 = append-only** est la plus directement visible ici : cette
distillation ne supprime aucun concept écrit, ne réécrit aucun concept
écrit par un autre agent (périmètre strict), et tout concept est ajouté
à l'index du sous-bundle après écriture.

## La citation anti-paresse (intention)

Le nom « anti-paresse » est explicite : la doctrine s'attaque au
réflexe d'un LLM qui **prétend avoir mesuré** ce qu'il n'a pas mesuré.
C'est l'inverse de l'**hallucination confiante** : ce n'est pas le fait
qui est faux, c'est la **prétention de vérification** qui est fallacieuse.

Le garde-fou de la distillation le formule ainsi :

> **« Une couverture partielle déclarée vaut mieux qu'une couverture
> totale prétendue — et c'est la seule des deux qui soit utilisable
> ensuite. »**

## Concepts liés

- [[adr-sober-002-anti-paperclip-doctrine]] — la sœur cadette qui s'ancre dans META-001.
- [[data-role-a3-archives-officer]] — la procédure A3 qui exige la documentation avant archivage.
- [[archive-v3-structure-snapshot-2026-08-02]] — application concrète des deux doctrines combinées.

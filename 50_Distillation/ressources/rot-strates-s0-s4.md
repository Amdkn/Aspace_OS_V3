---
type: Backend
title: Rot-rates S0→S4 — politique de péremption par strate
description: Doctrine de péremption des cinq strates mémoire (S0 Identité → S1 Court terme → S2 Travail → S3 Long terme → S4 Méta), créée 2026-08-01 pour rendre le rot opérable ligne par ligne dans RESOURCES_INDEX.md.
tags: [rot, péremption, strates, s0, s1, s2, s3, s4, fresh, kb-hygiene]
generated: { by: minimax-m3, at: 2026-08-17T20:56:00Z }
verified:
  - { by: process:lecture-fichiers, at: 2026-08-17T20:56:00Z }
sources:
  - id: rot-md
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/03_Memory_Unified/LLM_Wiki/wiki/ROT.md"
    title: "ROT — Rot-rates et politiques de péremption par strate"
    last_modified: 2026-08-01
  - id: plan-meta-memoire
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/00_Index/PLAN_META_MEMOIRE_2026-08-01.md"
    title: "Plan Méta-Mémoire 2026-08-01"
    last_modified: 2026-08-01
okf_version: "0.2"
---

# Rot-rates S0→S4 — politique de péremption par strate

> **Source normative** : `00_Index/PLAN_META_MEMOIRE_2026-08-01.md` §3.1.
> **Doctrine** : une strate sans rot-rate déclaré est une strate invisible pour la revue.
> Ce fichier rend le rot **opérable** ligne à ligne : la colonne `Revue` de
> `RESOURCES_INDEX.md` en dérive directement.

## 1. Tableau des 5 strates

| Strate | Nom complet | Rot-rate | Remède à l'échéance | Indicateur de freshness |
|---|---|---|---|---|
| **S0** | Identité | 1× / cycle 12WY (≈ 12 sem) | Relecture + bump `revue_at:` | `revue_at:` dans frontmatter |
| **S1** | Court terme | continu — compaction au seuil | `hand_offs/` append-only ; daily notes → S2 après 7 j sans mouvement | `wiki/log.md` mtime + `hand_offs/` mtime médian |
| **S2** | Travail | ≤ 7 j sans mouvement = signal | Promotion S3 si règle des 3 OU tag `_STALE_<date>` + route `04_From_V2_Root/` si hors scope | `find wiki/_CAPTURE_2026-08-01/ -mtime +7` |
| **S3** | Long terme (canon réutilisable) | revue hebdo (7 j) | Bump `revue_at:` + check `description:` non vide + check `Strate: S3` | `git log -1 --format=%ai` + parse `revue_at:` |
| **S4** | Méta (index) | par écriture — régénéré, jamais édité à main | `bin/gen_wiki_index.py` pour `wiki/index.md` ; table dans `RESOURCES_INDEX.md` bumpée à chaque promotion S3→S4 | mtime de `RESOURCES_INDEX.md` + diff compte lignes vs run précédent |

## 2. Règles de transition entre strates

```
S1 hand_off / daily note
   │ (1) réutilisable hors session ?
   ▼
S2 fiche de travail    ── si 7 j sans mouvement → tag _STALE_<date>
   │ (2) règle des 3 OU désignation A0
   ▼
S3 page de canon       ── si revue hebdo manquée 2× consécutives → flag pour re-tagging
   │ (3) frontmatter complet (type + description + timestamp + tags)
   ▼
S4 entrée d'index      ── si non référencée pendant 90 j → candidat _TRASH_<date>
```

**Descente interdite** : S3 → S2 n'existe pas. Une page S3 périmée part en
`_TRASH_<date>/` (D4, zéro hard-delete).

## 3. Cardinalités mesurées

| Strate | Sous-dossiers Geordi | Volume |
|---|---|---|
| S0 | `06_CC_Bare/CLAUDE.md` + AGENTS.md + memory/MEMORY.md | quelques fichiers |
| S1 | `wiki/hand_offs/` (350) + daily notes (4) | ~354 fiches |
| S2 | `wiki/_CAPTURE_2026-08-01/` (13) + `_INTAKE/` + memory agent (35) | ~50 |
| S3 | `01_Guides/` + `02_Templates/` + `wiki/{L0,concepts,entities,J01-J04}/` + CC_Bare/canon + `09_Life_OS/` | > 16 000 |
| S4 | `00_Index/` + `wiki/index.md` + `wiki/ROT.md` + CC_Bare/CLAUDE_INDEX + `graphify-out/` (1 195) | < 1 210 |
| hors strate | `04_From_V2_Root/` + `05_From_V2_Domains/` + 07/08/09_Batch2 + Cerritos + Youtube | **23 082** |

## 4. Tension avec la Constitution v1.0

**Article 5** de la Constitution rétrograde les doctrines en jurisprudence. Mais
l'idée d'un **rot opérable** reste essentielle : une KB sans rot retombe en friche.
La résolution canonique : le rot S3 hebdo survit comme **bonne pratique d'ingénierie**
(rotation manuelle), pas comme gate bloquant (qui serait anticonstitutionnel, Article 6).
Pour S0, A+ re-confirme la lecture à chaque cycle 12WY.

## Liens entrants

- `second-brain-14-sous-dossiers.md` — où logent physiquement les strates
- `constitution-aspace-v1.md` — Article 5/6 redéfinissent le statut du rot
- `geordi-kb-quatre-piliers.md` — où est l'index RESOURCES_INDEX.md (pilier INDEX)

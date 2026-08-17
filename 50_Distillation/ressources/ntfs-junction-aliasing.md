---
type: Concept
title: NTFS Junction Aliasing (ADR-FS-001) — short-path operability
description: Doctrine filesystem : PARA/Enterprise est source de vérité unique ; exposition via NTFS junctions (jamais copies). Trois couches d'aliasing (sentinelles racine `_\`, drives subst B:/P:, junctions sectorielles). Interdictions explicites (pas de robocopy /MIR).
tags: [ntfs-junction, aliasing, para-fs, short-path, agent-operability, adr-fs-001]
generated: { by: minimax-m3, at: 2026-08-17T21:03:00Z }
verified:
  - { by: process:lecture-fichiers, at: 2026-08-17T21:03:00Z }
sources:
  - id: adr-fs-001-entity
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/03_Memory_Unified/LLM_Wiki/wiki/entities/entity_adr_fs_001.md"
    title: "ADR-FS-001 — Junction-Based Aliasing"
    last_modified: 2026-05-22
  - id: junctions-map-2026-08-02
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/00_Index/JUNCTIONS_MAP_2026-08-02.md"
    title: "Cartographie des jonctions NTFS — 2026-08-02"
    last_modified: 2026-08-02
  - id: synthesis-infra-ceo-2026-06-05
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/03_Memory_Unified/LLM_Wiki/wiki/syntheses/synthesis_session_2026-06-05_infra-ceo-dashboard.md"
    title: "Distillation de session — Infra + CEO Dashboard + Orchestration (2026-06-04 → 06-05)"
    last_modified: 2026-06-05
okf_version: "0.2"
---

# NTFS Junction Aliasing (ADR-FS-001) — short-path operability

> Première décision du namespace `FS` (Filesystem), ratifiée 2026-05-22.
> Établit comment A'Space expose une couche profonde (PARA/Enterprise source-of-truth)
> via des **raccourcis filesystem** sans dupliquer les données.

## 1. Quatre règles

1. **PARA/Enterprise est source de vérité unique** pour Projects/Areas/Resources/Archives.
2. **Business OS expose ces données via NTFS Junctions** (jamais copies).
3. **Trois couches d'aliasing** : sentinelles racine `_\`, drives subst (`B:`, `P:`),
   junctions sectorielles.
4. **Interdictions** : `robocopy /MIR` 2-way, `mklink /D` non justifié, junction vers
   `node_modules`.

## 2. Trois couches d'aliasing

```
Couche 1 — sentinelles racine
C:\Users\amado\ASpace_OS_V2\04_From_V2_Root_\area  → junction vers 02_Areas_Spock
C:\Users\amado\ASpace_OS_V2\04_From_V2_Root_\para  → junction vers racine PARA
C:\Users\amado\ASpace_OS_V2\04_From_V2_Root_\proj  → junction vers 01_Projects_Picard

Couche 2 — drives subst
B: → un sous-ensemble Business
P: → un sous-ensemble Projects

Couche 3 — junctions sectorielles
05_From_V2_Domains/30_Business_OS/10_Projects/<proj>/_doctrine
   → 24_PARA_Enterprise/01_Projects_Picard/<proj>
```

## 3. Pourquoi : operability + MAX_PATH

Le problème MAX_PATH Windows (260 caractères) casse les builds : `solaris-aaas/.next` =
262 > 260. La solution ADR-INFRA-002 (Repo-Home / Junction Law) : les repos qui buildent
vivent court (`30_Business_OS\<court>`), la doctrine reste profonde, **junction relie**.

Homes `10_Projects/<p>/apps/<role>` = 71–77 chars ; + `.next` (~101) = ~178 < 260. ✓

## 4. Audit initial + correction

Audit initial (2026-05-22) : 4 jonctions existantes, 1 corrigée :
- `alykaly-front` self-ref → PARA Next.js réel.

## 5. Jonctions dans Geordi (mesure 2026-08-02)

Geordi héberge **159 jonctions NTFS** classifiées en 10 catégories (voir
`geordi-junctions-map-159`). Les plus structurantes pour l'architecture A'Space :

- **intra_g** (16) : duplication intra-G (à dédupliquer par `realpath`)
- **cross_para_*** (25) : `05_From_V2_Domains/<proj>/_doctrine → 01_Projects_Picard/<proj>`
- **external_*** (36) : franchissement hors ASpace_OS_V2 (vendor memory)

## 6. Pièges filesystem (D6 doctrinaux)

- `os.rmdir` uniquement pour détruire une jonction — **pas** `shutil.rmtree`,
  **pas** `rm -rf`, **pas** `Remove-Item -Recurse`. Ces outils suivent la jonction
  et détruisent la cible.
- `os.walk` naïf **suit** les jonctions → compte plusieurs fois le volume physique.
  Pour 1 195 md sous `06_CC_Bare/memory/lifeos-03-geordi` (cible = `graphify-out`),
  si suivi naïf = dédoublement.
- `os.path.islink()` ne détecte **pas** les jonctions NTFS. Utiliser
  `stat.FILE_ATTRIBUTE_REPARSE_POINT` (0x400) sur `os.DirEntry.stat(follow_symlinks=False)`.
- `find` sous git-bash **ne traverse pas** les reparse points. Utiliser `ls` ou le chemin réel.

## 7. Relation à la souveraineté

Niveau 1 infra (Trust Zone) + Niveau 2 code (ADR-FS-001) = souveraineté filesystem.
Les jonctions sont l'**outillage** ; la doctrine est l'**invariance** (PARA = SSOT).

## Liens entrants

- `sovereignty-3-niveaux.md` — niveau 1 (Trust Zone) + niveau 2 (ADR-FS-001)
- `geordi-junctions-map-159.md` — les 159 jonctions réelles dans Geordi
- `constitution-aspace-v1.md` — Article 5 rétrograde les ADR en jurisprudence ; FS-001 survit comme bonne pratique d'ingénierie

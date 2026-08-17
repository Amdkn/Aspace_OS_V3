---
type: Playbook
title: Geordi — cartographie des 159 jonctions NTFS
description: Carte exhaustive des 159 jonctions sous `03_Resources_Geordi` au 2026-08-02, classifiées en 10 catégories de risque (dead/trash/external_home_dot/external_appdata/external_other/intra_g/cross_para_*). Trois classes de danger concrètes pour la migration V3.
tags: [ntfs-junction, junctions-map, cartographie, migration, v3, security, fs]
generated: { by: minimax-m3, at: 2026-08-17T21:13:00Z }
verified:
  - { by: process:lecture-fichiers, at: 2026-08-17T21:13:00Z }
sources:
  - id: junctions-map-2026-08-02
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/00_Index/JUNCTIONS_MAP_2026-08-02.md"
    title: "Cartographie des jonctions NTFS — 2026-08-02"
    last_modified: 2026-08-02
  - id: fix-kb-2026-08-02
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/00_Index/FIX_KB_2026-08-02.md"
    title: "FIX KB — 2026-08-02"
    last_modified: 2026-08-02
okf_version: "0.2"
---

# Geordi — cartographie des 159 jonctions NTFS

> Mesure 2026-08-02. Détection via `stat.FILE_ATTRIBUTE_REPARSE_POINT` (0x400) sur
> `os.DirEntry.stat(follow_symlinks=False)`. Extraction cible via `fsutil reparsepoint query`.

## 1. Chiffres clés

| Métrique | Valeur |
|---|---|
| **Total jonctions détectées** | **159** |
| Cible existante | 79 (49,7 %) |
| Cible dans G (intra-arbre) | 17 |
| Cible hors G | 142 |

Découverte : le brief Geordi annonçait 47 jonctions (11 `04` + 36 `05`).
Le scan exhaustif en trouve **112 supplémentaires**, dont 91 dans `06_Claude_Code_Bare`
(mémoires graphify-out par app/projet).

## 2. Répartition par sous-dossier

| Sous-dossier | Jonctions |
|---|---:|
| `06_Claude_Code_Bare` | 91 |
| `05_From_V2_Domains` | 36 |
| `07_From_Home_Root_2026-08-01` | 16 |
| `04_From_V2_Root` | 11 |
| `03_Memory_Unified` | 5 |

## 3. Classification par catégorie de risque

| Catégorie | Compte | Cible typique | Risque principal |
|---|---:|---|---|
| `dead` | 61 | chemin supprimé / appdata nettoyé | Fragilité, pas de boucle |
| `trash_jct` | 21 | `AppData\Local\Temp\staging\*` | Mort, ignoré par tout parcours |
| `external_home_dot` | 26 | `.claude`, `.codex`, `.cursor`, `.antigravity*` | Franchissement hors ASpace_OS_V2 |
| `external_appdata` | 8 | `AppData\Roaming\AionUi\*`, `AppData\Local\Temp\*` | Lecture config utilisateur / staging |
| `external_other` | 2 | `agent-os`, `30_Business_OS` hors PARA | Cible externe diverse |
| `intra_g` | 16 | `03_Resources_Geordi\graphify-out`, `_CAPTURE_*` | **Boucle de duplication** |
| `cross_para_01_Projects_Picard` | 19 | `01_Projects_Picard\*` | Franchissement PARA + duplication |
| `cross_para_02_Areas_Spock` | 2 | `02_Areas_Spock*` | idem |
| `cross_para_04_Archives_Data` | 3 | `04_Archives_Data*` | idem |
| `cross_para_root` | 1 | `24_PARA_Enterprise` lui-même | idem |

## 4. Trois classes de danger concrètes pour la migration V3

### 4.1 Boucle de duplication du corpus (`intra_g`, 16 juncs)

`06_Claude_Code_Bare/memory/lifeos-03-geordi` → `03_Resources_Geordi/graphify-out`
(1 195 md). Un `os.walk` qui suit compte 2×.

Multiplicateur intra-G : si toutes les 16 vivantes suivies, ~1 800+ md rejoués sur la passe.

### 4.2 Franchissement de frontière PARA (`cross_para_*`, 25 juncs)

`05_From_V2_Domains/30_Business_OS/10_Projects/omk/_doctrine → 01_Projects_Picard/01-omk-business-os`
(137 md). Si suivi, la couche **Resources** aspire **Projects** ; le modèle PARA rompu.

Cas le plus lourd : `06_Claude_Code_Bare/memory/lifeos-01-picard → 01_Projects_Picard/graphify-out`
(1 208 md). 1 208 fichiers de Projects indexés comme Resources.

### 4.3 Franchissement de la frontière ASpace_OS_V2 (`external_*`, 36 juncs)

`06_Claude_Code_Bare/memory/app-.codex → C:\Users\amado\.codex\graphify-out` (2 822 md).
Mémoire globale de l'agent Codex, pas de Geordi. Total aspiré : ~6 400 md sur ces 10 juncs.
Avec `gstack` (168) et `superpowers` (81), on monte à ~6 650 md — **quasi l'intégralité
du wiki Geordi (1 774 md), double**.

## 5. Recommandation pour la migration V3

Un outil qui traverse G doit **impérativement** :

1. **Détecter** chaque entrée via `FILE_ATTRIBUTE_REPARSE_POINT` avant de descendre.
2. **Indexer la jonction** (chemin + cible) **sans suivre** dans le walk principal.
3. **Dédupliquer** par `os.path.realpath` après walk.
4. **Classifier** chaque jonction ; `cross_para_*` et `external_*` déclenchent une revue
   explicite avant migration.

Sans ces 4 garde-fous, le walk franchit 3 frontières : intra-G, PARA, ASpace_OS_V2.

## 6. Action déjà prise (Tache C, FIX_KB_2026-08-02)

- `_from_coaching_premium` (jonction morte ciblant `30_Business_OS\10_Projects\omk` sans
  le segment `20_Life_OS\24_PARA_Enterprise\`) retirée par `os.rmdir`.
- 81 autres jonctions mortes restent documentées (non retirées par le brief).

## Liens entrants

- `ntfs-junction-aliasing.md` — la doctrine d'aliasing
- `sovereignty-3-niveaux.md` — niveau 1 (Trust Zone) maintient la souveraineté
- `fix-kb-2026-08-02.md` (in `50_Distillation/archives/` ou future) — la passe qui a produit cette carte

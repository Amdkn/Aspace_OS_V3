---
type: Concept
title: PARA 4 niveaux — Enterprise (Projects/Areas/Resources/Archives)
description: Structure d'information canonique USS Enterprise. 4 niveaux de rangement — Projects (active), Areas (ongoing), Resources (reference), Archives (completed).
tags: [para, enterprise, projects, areas, resources, archives, obsidian]
generated: { by: minimax-m3, at: 2026-08-19T00:00:00Z }
verified:
  - { by: process:read_local_v2, at: 2026-08-19T00:00:00Z }
sources:
  - id: snw-spec
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/23_12WY_SNW/A2_Curie_SNW_Spec.md
    title: A2 Curie SNW Spec — Triptyque MORTY
    last_modified: 2026-05-20
  - id: protostar-readme
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/26_DEAL_Protostar/README.md
    title: 26_DEAL_Protostar README — Data supervises DEAL
    last_modified: 2026-06-21
  - id: beth-spec
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/00_Gatekeepers_Beth_Morty/A1_Beth_Spec.md
    title: A1 Beth Spec — Anti-patterns
    last_modified: 2026-05-20
okf_version: "0.2"
---

# PARA 4 niveaux — Enterprise (Projects/Areas/Resources/Archives)

PARA est le framework **structure d'information** d'A'Space OS, géré par USS Enterprise (Computer) via Obsidian. Quatre niveaux de rangement, chacun avec un rôle canon.

## Les 4 niveaux

| Niveau | Rôle | Sortie typique |
|---|---|---|
| **Projects** (P) | Active, time-bounded, livrable observable | Warp Core tactics, Rock decomposition |
| **Areas** (A) | Ongoing, responsabilité continue | LD01-LD08 (Life Wheel domains) |
| **Resources** (R) | Reference, thèmes d'intérêt | BIBLIOGRAPHY par LD |
| **Archives** (Arch) | Completed, inactive, dormant | Blueprints DEAL durables, Muse records |

## 4 A3 crew canon

| A3 | Niveau | Rôle |
|---|---|---|
| **Picard** | Projects | Strategy / Project ownership H10 |
| **Spock** | Areas | Logic / Areas ownership H10 |
| **Geordi** | Resources | Engineering / Resources ownership |
| **Data** | Archives | Memory / Archives ownership — **supervise opérationnellement DEAL** |

## Position dans le triptyque MORTY

PARA est **imbriqué DANS 12WY** par les 5 disciplines SNW (Pike/Una/Chapel/M'Benga/Ortegas) qui structurent Projects/Areas/Resources/Archives. DEAL est **imbriqué DANS PARA** parce que les blueprints durables Protostar sont routés vers Enterprise/Archives.

```
12WY (Curie SNW) ⊃ PARA (Enterprise Computer) ⊃ DEAL (Holo Janeway Protostar)
```

## A3 Data = chef d'orchestre DEAL (correction §3.1)

D3 nuance canon : **DEAL ⊂ PARA ⊂ 12WY** (imbrication poupée russe triptyque Morty, plan §3.1). A3 **Data** (`20_Life_OS/24_PARA_Enterprise/04_Archives_Data/`, parent A2 Computer Enterprise) supervise **opérationnellement** Holo-Janeway A2 DEAL et **libère A1 Beth (Ikigai Centrée) de la supervision opérationnelle de Protostar**. A1 Beth conserve le **veto d'alignement Ikigai** ; A3 Data porte la **supervision DEAL courante**.

## Beth — relation à PARA

Beth lit `20_Life_OS/24_PARA_Enterprise/` (Obsidian PARA) comme surface canonique — voir `A1_Beth_Spec.md` table "Inputs Beth Reads". Beth bloque :

- L2 business work bypasse PARA et 12WY.
- Un outil devient system of record sans handoff documenté.

## AREA_STANDARD P1 Work ON not IN

D3 nuance critique (plan §18.3) — règle de sarumétrie : Saru LD02 ne peut déclencher B1 review que si **≥2 B2 domains en conflit** (scarcity seule ne suffit pas). Cette règle AREA_STANDARD distingue "travailler ON" (sur) un projet de "travailler IN" (dans) un système.

## Acceptance Criteria

- **Handoff contexte** : un dossier projet reste dans Projects tant que Computer/Picard ne l'a pas marqué prêt pour DEAL (cf. `A3_Dal_Definition_Spec.md` ligne 47).
- **Dureé du blueprint** : un blueprint DEAL durable va dans Archives canon.
- **Cross-tool orchestration** : Symphony = `00_Amadeus/05_OSS_Twin/symphony` ; suit l'adapter spec.
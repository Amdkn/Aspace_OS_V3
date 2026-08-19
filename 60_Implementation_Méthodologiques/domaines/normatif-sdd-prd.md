---
type: Methodology
title: Méthode de distillation normative SDD/PRD V2 → V3
description: Le protocole suivi pour transformer les 31 SDD + 51 PRD uniques du corpus V2 (12 SDD V0.x + 17 SDD numérotés + 2 SDD annexes + 44 PRD V0.x + 7 PRD hors-chaîne) en 19 concepts OKF v0.2, en classant chaque document selon les quatre verdicts (canon / synthese-datee / superseded / orphelin) et en nommant les collisions de numérotation.
tags: [methode, distillation, okf-v0.2, sdd, prd, canon, synthese-datee, superseded, orphelin, collision, append-only]
generated: { by: minimax-m3, at: 2026-08-19T16:05:00Z }
verified:
  - { by: process:lecture_concepts_archives, at: 2026-08-19T16:05:00Z }
sources:
  - id: okf-format
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/40_Memory_Wiki_OKF/OKF.md"
    title: Format OKF v0.2 (frontmatter, niveaux de confiance)
    last_modified: 2026-08-02
  - id: brief-vague2
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/_briefs_vague2/BRIEF_normatif-sdd-prd.md"
    title: Brief vague 2 — distillation SDD/PRD
    last_modified: 2026-08-19
  - id: amendement-001-canon
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/10_Tech_OS/12_Blueprints/01-SDD/SDD-006_business-pulse-l2-pyramide.md (lignes 1118-1184)"
    title: Amendement 001 — exemple canon d'append-only
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Méthode de distillation normative SDD/PRD V2 → V3

## Périmètre

**31 SDD uniques** + **51 PRD uniques** = **82 documents normatifs** à
classifier et à distiller, sur les ~1 700 fichiers total du corpus
(ratio 20 fichiers / doc, dû aux miroirs Legacy `_SPECS/` /
`TOTAL_Spec/`, aux chunks graphify-out, aux clones de travail, et aux
archives `_V3_STRUCTURE_2026-08-02/`).

## Quatre verdicts (définition)

Chaque document reçoit **un seul** verdict parmi :

| Verdict | Sens | Décision attendue |
|---|---|---|
| `canon` | fait toujours autorité, rien à signaler | conserver tel quel |
| `synthese-datee` | dépassé sur **un point précis**, valable sur le reste | nommer le point, conserver le reste |
| `superseded` | remplacé **en entier**, par quoi | nommer le successeur (lien mort interdit) |
| `orphelin` | ne se rattache à rien, statut indéterminable | documenter l'absence de rattachement |

Un verdict `superseded` sans successeur nommé est un **lien mort** —
la distillation refuse de l'écrire.

## Étapes suivies

### Étape 1 — Localisation des copies canoniques

La règle posée par l'Amendement 001 (verbatim, lignes 1172-1184) est
l'ancre : **la copie vivante sous `05_From_V2_Domains/` fait foi**.

Pour chaque document, j'ai donc identifié :

- Le **chemin canon** (`05_From_V2_Domains/10_Tech_OS/12_Blueprints/01-SDD/`
  pour les SDD numérotés, `04_Archives_Data/Legacy_LifeOS_App_Specs_2026-05-22/_SPECS/`
  pour les Legacy).
- Les **copies miroirs** (`TOTAL_Spec/`, graphify-out/chunks, archives
  `_V3_STRUCTURE_2026-08-02/`).
- Les **collisions** (deux fichiers sous le même numéro ou dont le
  nom contredit le titre interne).

### Étape 2 — Lecture des ancres

J'ai lu en verbatim (limite 100 lignes quand volumineux) :

- **SDD-006_business-pulse** (l'amendement 001 in extenso)
- **SDD-V0.5_SovereignConstitution** (le pivot « Livre des Lois »)
- **SDD-006_definition-deal-h1-isaac-12wy-curie** (la collision)
- **SDD-V0.3_EngineRoom** (un échantillon Legacy)
- **SDD-V0.9_AgentPortal_Nexus** (l'isolat post-V3)
- **SDD-000b_agent-bootstrap** + **SDD-000c_aspace-core**
- **SDD-001_solarpunk-kernel-core**
- **SDD-005_life-os-l1-integration** + **SDD-006** (Pyramide L0/L1/L2)
- **SDD-007_sob-factory-icp-variants**
- **SDD-008_shadow-L1-life-os** + **SDD-009_shadow-L2-business-os**
- **SDD-010_meta-cloture-scope-13eme-semaine**
- **SDD-LOOP-ENGINEERING-001** + **SDD-W33-W42_fable_aspace_wargames**
- **PRD-NEXUS-EVOLUTION-IA-001** + **PRD-V0.2.4_UILayout**

J'ai **recoupé** les SDD Legacy avec leurs concepts d'archives déjà
publiés (`sdd-sovereign-constitution-v05.md`,
`legacy-lifeos-app-specs-evolution.md`).

### Étape 3 — Application des verdicts

Chaque verdict suit une règle de décision explicite :

#### `canon`

> Le document est cité comme référence par d'autres docs distillés OU
> porte un statut explicite « Approuvé » / « Ratifié » / « ACTIF » ET
> aucun de ses énoncés n'est contredit par la V3.

Exemples : SDD-000 (Constitution Rick's Verse), SDD-007 (SOB Factory),
SDD-V0.5 (Sovereign Constitution), SDD-LOOP-ENGINEERING-001.

#### `synthese-datee`

> Le document est canon **sauf** sur un point précis nommé — souvent
> un décompte (7 domaines vs 8) ou un statut (PLANNED jamais exécuté).

Exemples :

- **SDD-006 Business Pulse** : canon sauf sur le décompte « 7
  domaines » — l'Amendement 001 (2026-08-19) ajoute John Jones /
  Martian Manhunter / Sales / Illuminati comme 8e. Le **corps**
  reste intact (append-only).
- **SDD-009 Dashboard** : `PLANNED` (jamais exécuté). Le statut est
  conservé pour traçabilité.

#### `superseded`

> Le document est remplacé **en entier** par un autre, et le successeur
> est nommément cité.

Exemples :

- **SDD-V0.4** EnterpriseComputer → remplacé par SDD-001 Solarpunk
  Kernel Core (la chaîne V0.x est la pré-verticale, la chaîne
  numérotée est la post-verticale).
- **PRD-V0.2.4 à PRD-V0.8.8** : ~38 sur 44 sont supersedés par le
  code React de `coach-os/` et par les concepts d'archives V3.

#### `orphelin`

> Le document existe, mais ne se rattache à aucun cycle de ratification
> ni à aucun miroir TOTAL_Spec.

Exemple unique : **antigravity-kit-fusion_PRD.md** (dans `_SPECS/prds/`,
absent de `TOTAL_Spec/PRD/`).

### Étape 4 — Frontmatter OKF v0.2

Chaque concept est écrit au format OKF v0.2 :

- `type: Concept` (ou `Project`, `Methodology`)
- `title:` (lisible, sert de hook d'indexation)
- `description:` (UNE phrase — c'est le critère d'indexation)
- `tags:` (≥ 3)
- `generated: { by: minimax-m3, at: ISO 8601 }`
- `verified:` (au moins `process:lecture_concepts_archives` — pas
  d'acteur `human:` car l'agent n'est pas humain)
- `sources:` (≥ 1 chemin réel, lisible — un validateur le vérifie)
- `okf_version: "0.2"`

### Étape 5 — Liens `[[concept-…]]`

Les liens entre concepts utilisent la convention `[[concept-slug]]`.
Aucun lien n'est posé vers un fichier qui n'existe pas. Les
vérifications sont faites avant écriture.

### Étape 6 — Triplets JSONL

Le verbe central est **`supersedes`**. Trois autres verbes sont
employés :

- `governs` : un SDD en régule un autre
- `partOf` : un SDD appartient à une chaîne
- `cites` : un SDD cite un autre comme référence

Chaque triplet porte une `source` vérifiable (un chemin réel) et un
niveau de confiance (`haute` pour les lectures verbatim, `moyenne`
pour les recoupements, `basse` pour les inférences).

## Limites assumées

1. **Lecture non exhaustive** : 31 SDD + 51 PRD = 82 documents. J'en
   ai lu verbatim **~20** (les ancres, les collisions, et un
   échantillon par chaîne). Les autres ont été **classifiés par
   nommage, par date, et par statut dans le frontmatter** —
   classification **non vérifiée**.
2. **Pas d'arbitrage** : je n'ai tranché aucune contradiction. Les
   deux versions sont nommées avec leurs dates, sans en élire une.
3. **Pas d'écriture V2** : tous les amendements restent append-only
   dans la V2 (canon respecté). Aucune modification.
4. **Pas de `human:` dans les acteurs vérifiés** : les pages sont
   toutes « confirmées par machine » (niveau 1 OKF), jamais « revues
   par un humain » (niveau 2).

## Source de la méthode

Cette méthode **est elle-même un concept OKF** (`type: Methodology`),
distinct des concepts de fond. Elle peut être citée par d'autres
distillations du même corpus.

## Concepts liés

- [[concept-source-of-truth-canon]] — la règle du canon sous-jacente.
- [[concept-sdd-006-collision]] — la collision la plus instructive.

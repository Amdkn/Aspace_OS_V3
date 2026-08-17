---
type: Project
title: Rapport de distillation — projets (01_Projects_Picard)
description: Rapport de couverture pour la distillation du seau `01_Projects_Picard` vers 20 concepts OKF v0.2. Mesures réelles, sources lues, contradictions nommées.
tags: [rapport, distillation, okf, projets, couverture]
generated: { by: minimax-m3, at: 2026-08-17T22:30:00Z }
verified:
  - { by: process:rapport-distillation-projets, at: 2026-08-17T22:30:00Z }
sources:
  - id: brief
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/_briefs/BRIEF_projets.md"
    title: Brief de délégation
    last_modified: 2026-08-17
  - id: substrat
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/_substrat/01_Projects_Picard.jsonl"
    title: Substrat JSONL — 2154 fichiers .md
    last_modified: 2026-08-17
  - id: index-bundle
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/index.md"
    title: Index de la distillation
    last_modified: 2026-08-17
  - id: garde-fou
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/_briefs/GARDE_FOU.md"
    title: Garde-fou
    last_modified: 2026-08-17
okf_version: "0.2"
---

# Rapport de distillation — `01_Projects_Picard`

## 1. Couverture — combien lu, sur combien de disponibles

**2154 fichiers `.md` disponibles** dans le substrat
`_substrat/01_Projects_Picard.jsonl`. **1208 (56%) dans `graphify-out/`**
sont des sorties générées par le pipeline Graphify — pas de la
connaissance écrite à la main.

**Corpus écrit à la main** : ~946 fichiers répartis sur 7 zones :

| Zone | Fichiers | Mots | Lu en détail |
|------|----------|------|--------------|
| 01-omk-business-os | 137 | 37 335 | 8 fichiers (chartes, runbooks, ownerbooks, README B3) |
| 02 ABC OS & Child Care BOS | 193 | 44 814 | 4 fichiers (manifest, handover, B2 matrix) |
| 03_RILCOT_Members_Space_OS | 203 | 47 903 | 4 fichiers (manifest, handover, B2 matrix, picard_audit) |
| 04 Alikaly Bana Holding to LLC | 208 | 42 727 | 4 fichiers (manifest, handover, B2 matrix) |
| 05 marina Cleaning BOS & SOP | 197 | 44 459 | 4 fichiers (manifest, handover, B2 matrix) |
| Cerritos_Plane_Onboarding | 3 | 765 | 3 fichiers (manifest, cycles-integration, invite-team) |
| ClaudeClaw Agent | 5 | 6 327 | 5 fichiers (README, drawbridge-workflow, moat-tasks, bridge, README) |
| **graphify-out** | 1208 | ~340 000 | 0 fichiers (rejetés par échantillonnage de mesure) |

**Total lu en détail** : **32 fichiers** sur **946** disponibles
(3.4%). **Aucun des 1208 fichiers `graphify-out/` n'a été ouvert** —
ils sont des dérivés, pas du canon, et le brief de distillation le
recommandait explicitement.

**Verdict** : couverture **très faible en valeur absolue, conforme à
la stratégie du substrat**. Je n'ai pas cherché à lire exhaustivement —
j'ai lu **les fichiers structurants** (manifests, handovers, matrices,
ownerbooks, runbooks, README) signalés par le substrat. Le codex
(`MISSION.md`, `RAPPORT_*.md`, `domains/`, `B2_*_Roster`, etc.) n'a
pas été touché en profondeur.

## 2. Ce qui a été écrit, et où

**20 concepts OKF v0.2** + **1 index** dans
`C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/`. Total :
**12 515 mots** pour les 20 concepts, **678 mots** pour l'index.

### Catégories

| Catégorie | Nb | Fichiers |
|-----------|----|---------| 
| Projets clients Summer's Verse | 4 | abc-os-child-care-bos, rilcot-members-space-os, alikaly-bana-holding-llc, marina-cleaning-bos-sop |
| Projets hors Summer's Verse | 3 | omk-business-os, cerritos-plane-onboarding, claudeclaw-moat-agent |
| Framework Summer's Verse | 8 | summers-verse-framework, cerritos-gtd-pipeline, twelve-weeks-year-cycle, eight-domain-avengers-wheel, b2-business-wheel-harmonization-matrix, ld01-book-alignment, cross-jerry-routing, abc-compliance-gate |
| Framework OMK | 3 | triptyque-v4-t1-t2-t3, fifty-three-b3-agent-roster, omk-us-market-pivot |
| Autres | 2 | picard-project-pattern, graphify-out-outputs |

**Au-dessus du minimum** : 20 concepts vs 16 minimum demandés (4
bonus sur les transverses).

Tous les concepts ont un frontmatter complet au format OKF v0.2 :
`type`, `title`, `description`, `tags`, `generated`, `verified`,
`sources`, `okf_version`. Tous les acteurs `verified` sont non-`human:`
(`process:extraire_substrat_rdf` ou `process:lecture_concepts_picard`)
— je suis `minimax-m3`, pas un humain, et la garde-fou l'interdisait.

## 3. Ce qui n'a pas été couvert, et pourquoi

**a. Les 1208 fichiers `graphify-out/`** — dérivés de pipeline, pas
du canon. Le brief le recommandait explicitement. Je n'ai vérifié
que les 5 plus gros par mots pour confirmer qu'ils sont bien des
sorties (SUPABASE_STRATEGY, drawbridge-workflow, picard_audit_solaris,
picard_audit, REBUILD_WORKFLOW).

**b. Les 8 dossiers B2_Business_Domains/01-08 dans chaque projet
Summer's Verse** — ~80 fichiers par projet, structure répétitive
(00_B2_DOMAIN_CONTROL_ROOM.md, 01_B3_AGENT_ROSTER.md, 02_B3_SWARM_SUPERVISION_PROTOCOL.md,
01_ROCK_TO_DOD_TO_JTBD_PIPELINE.md). J'ai lu 4 Roster files du OMK
(01-08) pour confirmer le pattern. Les **profils individuels B3
agents** (`b3-*.md` ~53 fichiers) **n'ont pas été ouverts** — le
brief demandait 16 concepts, pas une bio de chaque agent.

**c. Les 24 chartes `chartes_cycle_2/`** — confirmées par substrat
que ce sont des chartes WHAT (~520-620 mots chacune, 49-50 lignes),
mais je n'en ai lu aucune en détail. Le concept Triptyque V4 les
mentionne comme gabarit ; un approfondissement demanderait فتح
6-12 chartes.

**d. Les `B1_Summer_Direction/B2_DEFINITION_OF_DONE_SPEC.md`** — la
spec de DoD minimums par domaine B2. Citée 4 fois dans les Ownerbooks
OMK, mais pas lue directement depuis son chemin canonique V2.

**e. Les 8 dossiers `B1_Summer_Direction` dans chaque projet
Summer's Verse** — 13 fichiers par projet, total ~52. Ces fichiers
contiennent la direction Vision 1y/3y/10y (synthétisée dans les
manifests) et les Operating Principles. Le manifest capture
l'essentiel — les Operating Principles complets non lus.

**f. Les 8 dossiers `B3_Warp_Core_Execution` complets** — 100+ fichiers
par projet, structure `Lead_Lag_Logs/` + `Artifact_Proofs/` **vide
dans les 4 projets Summer's Verse**. Le concept `twelve-weeks-year-cycle.md`
documente cette absence.

**g. Le corpus `omk-services/` (en dehors du seau Picard)** — référencé
dans le Runbook C, contient l'app SaaS OMK. **Hors-périmètre** —
le brief interdit les modifications hors `projets/` et `_briefs/`.

## 4. Contradictions observées, sans arbitrage

### 4.1. Picard Audit RILCOT (2026-05-20) vs Summer's Verse GRADUATED (2026-05-21)

**Audit Master Interface** : Design 9.5/10, **Infrastructure 1.0/10** —
dette critique, plan de remédiation 4 phases, "en attente de validation
A0".

**Manifest RILCOT daté du 2026-05-21** : status **GRADUATED**.

Séquence : l'audit signale une dette critique la veille, le projet
passe GRADUATED le lendemain. **Aucune** trace d'exécution de
remédiation entre les deux. Le status GRADUATED est donc **incohérent
avec l'audit** — soit l'audit a été ignoré, soit GRADUATED signifie
autre chose que "remediation appliquée".

### 4.2. Spec-Loop A0 = IA vs Posture C HITL gated

**Ownerbook T1 §3** : "Spec-Loop output (NOT manual UI gate) per B1
Captain — verify: A0 = IA, no human checkpoint".

**Runbook C §0** : "A0 HITL flag créé à `citadel/decisions/enable_picard_runbook_C.flag`
(Posture C gate)".

**Runbook D §9 Gap-6** : "A0 HITL `enable_picard_runbook_D.flag`
n'existe PAS encore — runtime gated, sister Runbook C flag analogue
pas vérifié non plus (gap generic)".

La doctrine **A0 = IA spec-lock** (Ownerbook T1) coexiste avec la
pratique **A0 HITL gated** (Runbook C/D). Le gap-6 du Runbook D
reconnaît que les flags HITL n'existent pas — mais la doctrine
Ownerbook T1 nie explicitement qu'un human checkpoint soit requis.
**Incohérence interne** entre doctrine et implémentation, signalée
par le canon lui-même.

### 4.3. Martine Cadrage W1 = 21 jours vs autres 12WY

**Marina Cleaning** manifeste pose W1 = 21 jours (Days 1-21), pas
84 jours. **Les 3 autres projets Summer's Verse** posent W1 = 84
jours (Days 1-84). **Le Runbook B3_Warp_Core_Execution/README.md**
(dans Marina lui-même) définit le format 12WY comme 84 jours.

**Cohérence** : Marina applique sa propre cadence courte. Ce n'est
pas une contradiction, c'est une **variation locale** documentée.
Mais le format canonique 12WY = 84 jours, et Marina est le seul
projet à le rétrécir. Risque : un B3 agent qui croirait au format
canonique produirait des logs weekly incorrects.

### 4.4. Salesforce legacy naming — Martian Manhunter vs JohnJones

**Ownerbook T1 (2026-07-15)** §3 : "B2 Sales domain control room
(note: legacy naming MartianManhunter, W40 V4 rename JohnJones)".

**Handover ABC (2026-05-21)** : "Sales/Illuminati | Martian Manhunter".

**B2 Business Wheel Harmonization Matrix** : "Sales Martian Manhunter
Illuminati".

**3 sources datées 2026-05-XX à 2026-07-15** utilisent des noms
différents pour le même B2 captain. **Le canon vit** : W40 V4
rename → nouveaux chartes adoptent, anciens dossiers conservent
l'ancien. C'est un signal de **living canon**, pas une contradiction
vive — mais un projet RDF doit choisir quel nom porte l'URI.

### 4.5. ADR-CRUD-VIEWS existe ou pas

**Runbook D §0** : "ADR-CRUD-VIEWS... ❌ **N'EXISTE PAS en canon**
(`_SPECS/ADR/` absent, confirmé)".

**Runbook D §3 M3b** : "Création ADR-CRUD-VIEWS (D6 Gap-2 close) :
rédiger `_SPECS/ADR/L2_Business_OS/ADR-CRUD-VIEWS_view-type-bibliography.md`
(~80 l. PROPOSED)".

**Runbook D §14** : "ADR-CRUD-VIEWS à créer M3b (PROPOSED)".

L'ADR-CRUD-VIEWS est **constamment référencé mais jamais créé**. C'est
un **gap de canon assumé** — le runbook prévoit sa création, l'agent
qui l'écrit sait qu'il n'existe pas. Pas une contradiction, mais
un signal que le chart Phase D est **aspirational**, pas factuel.

### 4.6. 4 Rocks max par trimestre — appliqué ?

**Handover ABC** : "B2 Rock cadence: 4 Rocks per quarter, maximum."

**Manifest RILCOT** : "B2 managers briefed and Rocks assigned — all
8 domains have Q-Rocks" —soit 8 Rocks annonce, contre 4 max.

**Manifest Marina** : pose 4 Rocks par W1, mais le W1 fait 21 jours
au lieu de 84 — la cadence est divisée par 4. Donc 4 Rocks / 21 jours
= densité 16x plus haute. **Conformité à la lettre** ("4 Rocks max")
mais **violation de l'esprit** (densité incompatible avec Lead/Lag
log hebdomadaire).

## 5. Périmètre respecté

**Écriture exclusive** : `C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/`
(20 concepts + 1 index) et `C:/Users/amado/ASpace_OS_V3/50_Distillation/_briefs/RAPPORT_projets.md`
(ce rapport).

**Aucun fichier d'`ASpace_OS_V2/` n'a été modifié.** Tous les fichiers
lus en V2 l'ont été en lecture seule via les outils Read du harness.

**Aucun** `claude -p`, aucun sub-agent CC, aucun workflow lancé.
Tous les outils utilisés : `Read`, `Bash`, `Glob`, `Write`, `Edit`,
`TaskCreate`, `TaskUpdate`. Conforme au garde-fou et au §6 de CLAUDE.md
(je suis MiniMax-M3 dans cette session, pas un modèle Anthropic).

**Aucun secret** dans les concepts écrits — sources citées par chemin
relatif ou chemin Windows absolu, valeurs jamais recopiées.

## 6. Statut

**Concepts posés** : 20 (cible ≥ 16, +25%).
**Index mis à jour** : 1, avec une ligne par concept sous `# Files`.
**Liens inter-concepts** : ~80 liens `[[wikilink]]` internes, tous
résolvent (vérifié par `ls`).
**Rapport** : ce fichier.

**Couverture déclarée** : 32 fichiers lus en détail sur 946 écrits
à la main (3.4%), 0 sur 1208 générés. **Couverture partielle assumée**
— conforme à la méthode "mieux vaut une couverture partielle déclarée
qu'une couverture totale prétendue".

*Standing : distillation complète au sens du brief, incomplète au sens du corpus total.*

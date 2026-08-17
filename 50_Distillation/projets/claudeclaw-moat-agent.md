---
type: Project
title: ClaudeClaw Moat Agent
description: Scaffold Vite + React + TypeScript avec le workflow Drawbridge (Moat extension Chrome pour annotations UI) — projet de test/expérimentation, embryonnaire, statut réel non graduation.
tags: [projet, scaffold, drawbridge, moat, vite, react, annotation, embryo]
generated: { by: minimax-m3, at: 2026-08-17T21:00:00Z }
verified:
  - { by: process:extraire_substrat_rdf, at: 2026-08-17T19:50:00Z }
  - { by: process:lecture_concepts_picard, at: 2026-08-17T21:00:00Z }
sources:
  - id: workflow-canon
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/ClaudeClaw Agent/.moat/drawbridge-workflow.md"
    title: Drawbridge Workflow — Complete Rules (2026-03-30)
    last_modified: 2026-03-30
  - id: readme-claudeclaw
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/ClaudeClaw Agent/README.md"
    title: README Vite template (212 mots, 2026-03-29)
    last_modified: 2026-03-29
  - id: moat-tasks-md
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/ClaudeClaw Agent/.moat/moat-tasks.md"
    title: Moat tasks (échantillon)
    last_modified: 2026-03-30
okf_version: "0.2"
---

# ClaudeClaw Moat Agent

## Synthèse

**Scaffold Vite + React + TypeScript** stocké dans le seau `01_Projects_Picard`
sous le nom `ClaudeClaw Agent`, contenant un **workflow Drawbridge**
complet pour le **Moat Chrome extension** (annotation UI → code).
Embryonnaire — 5 fichiers .md, sans graduation formelle. Daté
2026-03-29 à 2026-03-30.

## Trois questions — ce qu'il visait, ce qui a été livré, ce qui ne l'a pas été

**Ce qu'il visait.** Expérimenter un pont entre **annotations UI
métier** (designers qui cliquent sur des éléments dans Chrome) et
**code applicatif** (implémentation automatique des modifications).
Stack : Vite + React + TypeScript côté front, Moat extension côté
Chrome, et un agent qui orchestre le flux.

**Ce qui a été livré.**
- README scaffold (212 mots) — template Vite + React + TS officiel
- `.moat/drawbridge-workflow.md` (4053 mots) — la doctrine complète
  du workflow
- `.moat/README.md` (735 mots) — la doc utilisateur Moat
- `.moat/bridge.md` (1133 mots) — la commande `/bridge` qui orchestre
- `.moat/moat-tasks.md` (194 mots) — une liste de tâches

**Le workflow Drawbridge** définit trois modes d'exécution :
- **Step mode** (default, incrémental avec approval) — pour 1-5 tâches
- **Batch mode** (groupé par composant/sélecteur) — pour 6+ tâches
- **YOLO mode** (autonomous, sans approval) — risk-on, jamais auto-sélection

**Ce qui ne l'a pas été.** Le projet **n'est pas gradué** — il
s'arrête à l'état scaffold. Aucun fichier projet (index.html, App.tsx)
n'est personnalisé au-delà du template. Aucun `moat-tasks-detail.json`
exploité n'apparaît dans le corpus visible. C'est un **chantier de
test/expérimentation**, pas un projet livré.

## Le workflow en bref

Pour chaque tâche, le contrat est **3 opérations** (vs 6+ naïves) :

```
OP 1 — Batch Start : JSON status → "doing" + announce +  TODO in_progress
OP 2 — Implementation : edit code
OP 3 — Batch Complete : JSON status → "done" + markdown [x] + TODO completed
```

Lifecycle obligatoire : `to do → doing → done` (jamais `to do → done`).
Les transitions invalides (`done → doing`, `to do → failed`) sont
rejetées explicitement.

## Différence avec les autres projets

| Caractéristique | ClaudeClaw | Summer's Verse ×4 | OMK Business OS |
|-----------------|------------|-------------------|-----------------|
| Frontmatter status | aucun | `GRADUATED` | `ACTIVE` |
| B1/B2/B3 split | absent | présent | présent (T1/T2/T3) |
| Artefacts Lead/Lag | non | oui (vide) | oui (vide) |
| Doctrine propre | cycle `to do/doing/done` | 12WY + Lead/Lag | 12WY + D4/D6 + Spec-Loop |
| Cadence | par tâche | 84 jours | 84 jours |

**ClaudeClaw n'est pas un projet Picard canonique.** C'est un test
d'outillage — il pose la question "comment Docker un workflow d'annotation
UI ?" sans la résoudre.

## Note de confiance

**Confirmé par machine.** 5 fichiers .md lus, structure vérifiée. La
différence avec les projets Summer's Verse est lisible par absence de
status GRADUATED et absence de structure B1/B2/B3. L'orchestrateur
"3 ops" est explicite dans le workflow mais aucun exemple concret n'est
tracé dans le corpus.

*Standing : embryonnaire, scaffold non personnalisé, workflow défini non exécuté.*

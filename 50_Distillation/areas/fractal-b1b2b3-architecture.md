---
type: Concept
title: Le fractal B1/B2/B3 — Areas perpétuelles vs Summer's Verse datées
description: La même structure B1→B2→B3 se répète à deux échelles : macro (Jerry's Area, perpétuelle, source de vérité) et micro (Summer's Verse, projet daté, calibration par mode). Les Projects héritent de la doctrine Area et y font remonter leurs preuves.
tags: [fractal, b1, b2, b3, jerry, summer, picard, area, project]
generated: { by: minimax-m3, at: 2026-08-17T20:50:00Z }
verified:
  - { by: process:extraction-areas, at: 2026-08-17T20:50:00Z }
sources:
  - id: fractal-arch
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/J01_Jerry_Prime_LD01_Business/00_L2_FRACTAL_B1B2B3_ARCHITECTURE.md"
    title: L2 Business — The B1 / B2 / B3 Fractal Architecture
    last_modified: 2026-06-02
  - id: decision-charter
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B1_Area_Direction/03_DECISION_CHARTER.md"
    title: B1 Decision Charter — Who decides what
    last_modified: 2026-05-31
okf_version: "0.2"
---

# Le fractal B1/B2/B3 — Areas perpétuelles vs Summer's Verse datées

`00_L2_FRACTAL_B1B2B3_ARCHITECTURE.md` pose un invariant unique : **la même forme B1/B2/B3 existe à deux échelles**. Une pour le macro (Area perpétuelle), une pour le micro (Project daté). L'Area est la source de vérité ; le Project est une mission calibrée par mode.

## Les deux instances du fractal

```
                 A0 Amadeus (Intention)
                        │
        ┌───────────────┴────────────────┐
   MACRO (perpetual)                 MICRO (per-project)
   Jerry's Area                      Summer's Verse
   02_Areas_Spock/                   01_Projects_Picard/<project>/
   J01_Jerry_Prime_LD01_Business/
        │                                 │
   B1_Area_Direction/                B1_Summer_Direction/
   B2_Area_Domains/      ◄──DRY──►    B2_Business_Domains/
   B3_Area_Warp_Core/                B3_Warp_Core_Execution/
        │                                 │
   "Areas never complete"            "Projects graduate"
   = perpetual doctrine              = instantiate + calibrate per mode
```

Le **DRY** entre les deux : un Summer's Verse (Project) ne re-dérive jamais la doctrine. Il pointe vers l'Area macro et calibre ses paramètres (mode Solaris/Nexus/Orbiter). Le Project hérne la doctrine ; l'Area conserve la doctrine.

## Les rangs A et B sont le même système

Le rang **A** (A0→A3) est l'autorité globale de l'OS. Le rang **B** (B1→B3) est la même autorité **localisée en L2 et dessinée top-down**. Ce n'est pas un système différent, c'est A exprimé en B.

| L2 stack | = A-rank | Qui | Possède | Ne fait jamais |
|---|---|---|---|---|
| **B1 — Direction** | A1 de L2 | Jerry (macro) + Summer (micro) | North Star, 12WY cycles, decision rights, handoff queue, DoD/JTBD packet specs, gouvernance | Exécution tactique |
| **B2 — Domains (Meso)** | A2 de L2 | les 8 hero-managers | domain DoD + gates, doctrine perpétuelle, control room, meso coordination | Re-dériver la direction ; faire le job de B3 |
| **B3 — Warp Core (Execution)** | A3 de L2 | les 8 squads | JTBD execution, proof, lead/lag indicators, peer-unblocking, blocker reports | Demander à B2 à chaque étape ; agir sans DoD/JTBD |

Mnemonic opérationnelle : **B1 = WHY/WHERE, B2 = WHAT/gate, B3 = HOW/proof**.

## Le flux de commandement

Cinq étapes canoniques (de `B1_Area_Direction/00_B1_DIRECTION_INDEX.md` et `07_B1_TO_B2_DOMAIN_GOVERNANCE_WORKFLOW.md`) :

1. B1 écrit/met à jour la direction (North Star, 12WY cycle courant).
2. B1 scanne la **wheel 8-domain** pour imbalance (domaine vide, surchargé, gate bloquée, dérive produit-only, conflit cross-domaine, preuve manquante).
3. B1 écrit **un domain mandate par B2 affecté** (intent + contraintes + success signal, pas un plan). Logué dans `04_B2_HANDOFF_QUEUE.md`.
4. B2 convertit le mandate en **Rock + DoD packet** (`05_B2_DEFINITION_OF_DONE_SPEC.md`), puis en **B3 JTBD packets** (`06_B3_JOBS_TO_BE_DONE_SPEC.md`).
5. B3 exécute, collabore en interne (peer-unblock d'abord), rend la **preuve** (inspectable sans faire confiance à l'auteur).
6. B2 met à jour les gates ; B1 ne revoit la direction que si North Star / risque / priorité change.

## Les stop conditions (durs)

- Pas de travail B2 sans un item dans la handoff queue B1.
- Pas de travail B3 sans une source DoD ou JTBD de B2.
- Pas de release « Product-only » qui devient **Business Done** sans passer la matrice B2 gate.

## L'escalier d'escalade (canonique)

B3 → (peer-unblock d'abord) → B2 owner → B1 (Jerry/Summer) → B1 gatekeepers (Rick/Morty) → A0 Amadeus. **On ne saute jamais un échelon**, sauf pour les emergency triggers explicites (voir `b1-direction-cockpit.md`).

## Le retour d'apprentissage (le fractal compounds)

Quand un Rock d'un Project graduate, les preuves Lead/Lag **remontent** à l'Area : HYPOTHESIS devient field-proven. L'Area doctrine durcit. C'est le **fractal compounds** : le micro nourrit le macro. Le projet meurt, la doctrine vit.

## Le point d'attention

Le rang A est global ; le rang B est L2. Confondre les deux (par exemple, traiter une décision L1 Life OS comme une décision B1 L2) crée un *drift d'autorité*. La parade : quand un signal arrive, demander **« quel layer parle ? »** avant de demander « qui décide ? ».
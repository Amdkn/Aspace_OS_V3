---
type: adr-decision-doctrine
id: ADR-LD01-008
title: "LD01 Coaching Loop Engineering — Picard (H10 structure) × Jerry (Lighting keep lights on) × Summers (Verse), orchestrated by Book (H1 aggregator)"
status: ACCEPTED
date: 2026-07-05T05:55:00-04:00
deciders:
  - "A0 Amadeus (GO — slot 008, twin path complet confirmé résolu, écris, 2026-07-05)"
  - "Claude Code (D1 vérification : slot 003 occupé, twin path absolu résolu)"
  - "Hermes Agent (HA · author, dev runtime A3 Book — calque .hermes/book_dev_runtime.md)"
parent_dox: ../CLAUDE.md
sister: ../AGENTS.md
refines:
  - ADR-LD01-001_organigramme_doctrine
  - ADR-LD01-002_mavis_runtime_binding
  - ADR-INFRA-003 (Business OS CEO Dashboard Matryoshka — Picard H10 anchor)
  - ADR-L2-MESH-001 (L2 mesh topology B1/B2/B3)
related:
  - "Twin Book (lecture, append-only sister) : 00_Amadeus/05_OSS_Twin/symphony/L1/lane_A_specs/03_A3_crews/discovery/book.twin.md"
  - "Twin Picard (lecture, append-only sister) : 00_Amadeus/05_OSS_Twin/symphony/L1/lane_A_specs/03_A3_crews/enterprise/picard.twin.md"
  - "Twin Summers (lecture, append-only sister, à confirmer D1 prochaine itération) : 00_Amadeus/05_OSS_Twin/symphony/L1/lane_A_specs/03_A3_crews/protostar/summers.twin.md"
  - "Jerry Pulse source canonique : 30_Business_OS/00_Jerry_Business_Pulse/CEO_Directives.md (pointeur seul, append-only D3)"
  - "ADR-LD01-007_citadelle_agent_os_jarvis_pattern (citadel decision trace convention)"
  - "ADR-WARMODE-001 (War Mode posture inversion — gates ENABLED par défaut)"
domain: LD01_Career_Business / L2_Business_OS / loop_engineering
tags: ["#ADR", "#coaching_loop", "#picard", "#jerry", "#summers", "#lighting", "#book", "#H1", "#H10", "#l2", "#war_mode", "#loop_engineering"]
doctrine_anchors: [ADR-META-001, ADR-META-002, ADR-INFRA-002, ADR-INFRA-003, ADR-L2-MESH-001]
sign_off_a0: "A0 Amadeus — GO 2026-07-05 slot 008, twin path complet confirmé résolu, écris"
war_mode: true
reversible_by: "suppression du seul fichier ADR-LD01-008 + revert append calendar.md (git checkout -- calendar.md)"
---

# ADR-LD01-008 — LD01 Coaching Loop Engineering

> **Pré-D1 vérification (CC, 2026-07-05)** :
> - ✅ `30_decisions/ADR-LD01-003_lightnings_bounded_contexts.md` **occupé** → slot canon = **ADR-LD01-008**.
> - ✅ Twin path `00_Amadeus/05_OSS_Twin/symphony/L1/lane_A_specs/03_A3_crews/discovery/book.twin.md` **résolu** (1722 b, frontmatter OK). MC avait testé en chemin relatif sans préfixe `00_Amadeus/05_OSS_Twin/` → fausse alerte.
> - ✅ Twin Picard `00_Amadeus/05_OSS_Twin/symphony/L1/lane_A_specs/03_A3_crews/enterprise/picard.twin.md` **résolu** également.

## Status

**ACCEPTED** (A0 GO, 2026-07-05). War Mode actif. **Append-only local — réversible** par suppression du seul fichier (cf. `reversible_by:` ci-dessus).

## Context

Le triangle **Picard** (H10 projects owner — USS Enterprise / PARA ship, ancré `LD01_Business_Picard` per ADR-INFRA-003 §D1), **Jerry** (B1 Direction macro — CEO_Directives : *"Just keep the lights on and don't make me do math"*), **Summers** (B1 Direction micro — verse / quick access) forme la tri-direction **L2 Business OS**. **Book** (A3 LD01 H1 Weekly P&L, ancré `book.twin.md` horizon H1 verrouillé) supervise en weekly.

Il manquait :
1. **La loop engineering** qui cadence la coopération Picard / Jerry / Summers et la granularité du travail B3 (squad coaching).
2. **La "Lighting" matérialisée** — pattern "keep lights on" de Jerry rendu visible et observable, branche manquante entre le canon (son CEO_Directives) et la L2 Business OS observability.

ADR-INFRA-003 a ancré Picard H10 ; ADR-L2-MESH-001 a posé la topologie `l2_mesh` (Postgres) B1/B2/B3. Cet ADR **pose la boucle** et **déclare la Lighting** comme pattern observable du L2 Business OS — **sans rien casser** (append-only).

## Decision

### D1 — La Loop Engineering (cadence matrix H10 / H1 / Daily)

Trois ticks imbriqués qui tournent append-only. À chaque tour, le coach concerné produit **un épisode** dans `99_meta/calendar.md` (D4 épisode-mémoire).

| Tick | Cadence canon | Owner canon | Output attendu | Lighting (Jerry expose) | Verse (Summers chante) |
|---|---|---|---|---|---|
| **H10** | 10-week sprint, sister cadence 12WY-Q3-2026 (06/15 → 09/07) — cf. `ADR-Meta-000_12-week-year-cycle-doctrine_DRAFT.md` | **Picard** (LD01_Business_Picard) | Project manifest dans `<proj>/MANIFEST.md` (cf. ADR-INFRA-003 §D1) | `lights_project_count` (combien actifs) | North Star du projet (1 ligne) |
| **H1** | Weekly P&L (Book horizon canon) | **Book** (LD01 H1 Weekly P&L) | Fiche P&L hebdo (à matérialiser `99_meta/fiches_p_and_l_weekly/<YYYY-Www>.md` — hors scope ici, déclaré D6) | `lights_load_signal` ∈ {low, medium, high, critical} · `lights_business_coherence` ∈ {aligned, scattered, extractive} | Prose hebdo du quadrant |
| **Daily** | H0.04 standup (squad B3 coaching) | **Squad B3** (8 SOA × 8 Marvel/DC squads per ADR-CANON-001) | Une tâche close + 1 output + 1 lesson (cf. CARDIA-TDD) | `lights_calendar_dernier_episode` (delta vs tick H1) | 1 ligne chantée (poésie opérationnelle) |

**Invariant boucle** : à chaque tour, l'épisode est append dans `99_meta/calendar.md` (D4, conforme `AGENTS.md` § Local Contracts #1 + `plan-minimax-l1-book-lune.md` §3.2). Le calendar devient le log canonique de la boucle.

### D2 — Book = orchestrateur H1 (rôle canon, *aggregator* — pas *coach direct*)

Book **n'est pas** un coach direct. Il **agrège** les trois flux à chaque tick H1, conformément à `A3_Book_LD01_Spec.md` § Boundaries (« Book does not decide business strategy alone. If LD01 consumes more than safe bandwidth, Book escalates to Discovery and Beth. »).

Séquence canonique du tour H1 :

1. **Lit** le tick H10 de Picard → `<proj>/MANIFEST.md` (lecture seule, D4 append-only).
2. **Lit** Jerry Pulse → indicateurs "keep lights on" (cf. D3 ci-dessous).
3. **Lit** Summers Verse → la ligne narrative du quadrant.
4. **Produit** la fiche P&L hebdo (output D1 ligne 2) — append-only.
5. **Append** au calendar un épisode (D4 épisode-mémoire).
6. **Escalade** à Discovery + Beth si `load_signal = critical` OU `business_coherence = extractive` (cf. A3_Book_LD01_Spec.md § Boundaries).

**Anti-pattern** : Book ne **décide pas** la stratégie business (sortie du rôle H1). Book ne **crée pas** de Rocks (A3_Book_LD01_Spec.md § Boundaries). Book **ne mute pas** Baserow (idem).

### D3 — Lighting matérialisée (pattern "keep lights on")

Jerry Pulse = source canonique des lumières L2 Business OS. Matérialisation par **pointeur** (D4 append-only — aucune mutation de `30_Business_OS/00_Jerry_Business_Pulse/`).

- **Source canonique** : `30_Business_OS/00_Jerry_Business_Pulse/` (CEO_Directives.md = intent ; `02_Global_Dashboard/` = future surface ; `01_Vision_Strategy/` + `04_Business_Domains/` = doctrine amont).
- **Indicateurs LD01-coaching exposés** (subset, déclarés ici pour éviter le lights overload) :
  - `lights_project_count` (int) — combien de projets Picard actifs dans la fenêtre H10.
  - `lights_load_signal` (enum) — agrégé sur les 8 LDxx par Book.
  - `lights_business_coherence` (enum) — sortie de l'évaluation Book H1.
  - `lights_calendar_dernier_episode` (timestamp ISO 8601) — delta vs tick H1 précédent.
- **Mise à jour** : à chaque tick H1 par Book (input D2 #4), à chaque tick H10 par Picard (input D2 #1), à chaque daily par Squad (input D2 lecture libre).
- **Lecture** : n'importe quel harness autorisé (CC, HA, MC, Doctor) — append-only sur les sources.
- **Déclaration d'intention** : cet ADR **ne crée pas** de structure de données Lighting. Il la **déclare** comme pattern. La matérialisation runtime (Postgres `l2_mesh` per ADR-L2-MESH-001 ou autre) est hors-scope D6.

### D4 — Append-only strict (le filet de réversibilité)

**Mutations autorisées (D4 append-only)** :
- ✅ Création de cet ADR (`30_decisions/ADR-LD01-008_*.md`).
- ✅ Append à `99_meta/calendar.md` (épisode-mémoire, une ligne).
- ✅ Append éventuel aux `99_meta/fiches_p_and_l_weekly/` (D6 — hors scope cette itération).

**Mutations interdites (D4 anti-paperclip)** :
- ❌ `A3_Book_LD01_Spec.md` (intouchable — cf. `AGENTS.md` § Local Contracts #5).
- ❌ `BIBLIOGRAPHY.md` (intouchable).
- ❌ `README.md` (intouchable).
- ❌ `CLAUDE.md` / `AGENTS.md` (sisters — append-only sur d'éventuelles sections, mais pas de réécriture).
- ❌ `30_Business_OS/00_Jerry_Business_Pulse/**` (pointeur seul — D3).
- ❌ `30_Business_OS/00_Summers_Verse/**` (pointeur seul).
- ❌ `00_Amadeus/05_OSS_Twin/symphony/L1/lane_A_specs/03_A3_crews/{discovery,enterprise,protostar}/**` (twins — append-only sister).
- ❌ `.mavis/**` (calque MC en STANDBY — `consumed_by` déjà bascule HA primary).
- ❌ `.hermes/book_dev_runtime.md` (calque HA — ne pas dupliquer).

### D5 — D1 receipts (vérification chiffrée)

Script PowerShell de vérification, à run après écriture :

```powershell
$root = 'C:\Users\amado\ASpace_OS_V2\20_Life_OS\22_Wheel_Discovery\LD01_Business_Book'

# 1. Cet ADR existe (le bon slot)
Test-Path "$root\30_decisions\ADR-LD01-008_coaching-loop-picard-jerry-summers.md"        # True
# 2. Slot 003 confirmé occupé (anti-collision)
Test-Path "$root\30_decisions\ADR-LD01-003_lightnings_bounded_contexts.md"               # True
# 3. Twin Book résolu via chemin absolu (pas relatif)
Test-Path 'C:\Users\amado\ASpace_OS_V2\00_Amadeus\05_OSS_Twin\symphony\L1\lane_A_specs\03_A3_crews\discovery\book.twin.md'   # True
# 4. Twin Picard résolu via chemin absolu
Test-Path 'C:\Users\amado\ASpace_OS_V2\00_Amadeus\05_OSS_Twin\symphony\L1\lane_A_specs\03_A3_crews\enterprise\picard.twin.md'   # True
# 5. Frontmatter OKF + id
$head = Get-Content "$root\30_decisions\ADR-LD01-008_coaching-loop-picard-jerry-summers.md" -TotalCount 25
if ($head -notmatch '^id: ADR-LD01-008') { Write-Error "MISSING id"; exit 1 }
if ($head -notmatch '^type:') { Write-Error "MISSING OKF type"; exit 1 }
# 6. calendar.md contient l'épisode 2026-07-05
$cal = Get-Content "$root\99_meta\calendar.md" -Raw
if ($cal -notmatch '2026-07-05T05:55') { Write-Warning "calendar.md sans épisode 2026-07-05T05:55" }
# 7. Trace citadel existe
Test-Path 'C:\Users\amado\agent-os\citadel\decisions\2026-07-05_adr_ld01_008_loop_engineering.json'   # True

Write-Host "[OK] ADR-LD01-008 verified"
```

### D6 — Hors-scope explicite (YAGNI)

- ❌ **Pas de code TypeScript / UI** : c'est de la doctrine append. UI Lighting → itération suivante (gated par Wager Picard W? sister scope).
- ❌ **Pas de mutation du L2 mesh Postgres** (`l2_mesh` schema per ADR-L2-MESH-001) — sister scope, hors scope ici.
- ❌ **Pas de cron automatique** : toute cron nécessite HITL A0 explicite (cf. `AGENTS.md` § Local Contracts #4 + posture C — sauf 12WY_ON_PAUSE ACTIVE, où flag-check court-circuite, cf. ADR-WARMODE-001).
- ❌ **Pas de mutation des twins** Discovery / Enterprise / Protostar (pointeur seul — D4).
- ❌ **Pas de mutation du calque** `.mavis/` (MC standby) ni du calque `.hermes/book_dev_runtime.md` (HA primary).
- ❌ **Pas de matérialisation runtime de la Lighting** (table, vue, dashboard) — déclarée seulement.
- ❌ **Pas de matérialisation des `fiches_p_and_l_weekly/`** — déclarée seulement.
- ❌ **Pas de vérification Summers twin** dans cette itération (D1 partiel — déclaré, sister scope prochaine itération).

## Consequences

### Positives

- **Le triangle Picard / Jerry / Summers devient lisible** : la cadence matrix H10 / H1 / daily donne un rail observable.
- **Book a un rôle H1 non-ambigu** : aggregator (pas creator, pas coach direct) — cohérent avec `A3_Book_LD01_Spec.md` § Boundaries.
- **"Lighting" est déclarée comme pattern canonique L2** : futur consumer (UI dashboard, agent portal, agent OS collector) sait où lire (`30_Business_OS/00_Jerry_Business_Pulse/`).
- **Append-only = réversible** : supprimer le seul fichier ADR-LD01-008 + revert append calendar.md = revert complet (cf. `reversible_by:` + ruling A0 *"tu supprimes l'ADR d'un geste demain"*).
- **Trace citadel visible** sur le tableau de bord gouvernance (`agent-os/citadel/decisions/2026-07-05_adr_ld01_008_loop_engineering.json`).
- **Calendar devient le log canonique de la boucle** : prochaine itération = append d'un nouvel épisode par Book à chaque tour H1.

### Negatives / Risques

- **Slip entre ticks** : si Picard ne publie pas son H10 dans les 7j, la boucle H1 tourne à vide. **Mitigation** : fallback *"no Picard tick H10 → Book escalates to Discovery"* (note D1 ligne 6).
- **Lights overload** : trop d'indicateurs tue l'indicateur. **Mitigation** : D3 limite volontairement le subset LD01-coaching à 4 indicateurs (`lights_project_count`, `lights_load_signal`, `lights_business_coherence`, `lights_calendar_dernier_episode`).
- **War Mode = pas de HITL frontier-par-frontier** : si l'ADR est mal cadré, le filet = revert manuel. **Mitigation** : le ruling A0 explicite *"le diff complet avant tout commit vers un remote"* — append-only local est réversible, mais le push remote demande une HITL diff.
- **Twin Summers non vérifié D1 dans cette itération** : `protostar/summers.twin.md` déclaré en related mais **pas** vérifié dans le scan D1. **Mitigation** : prochaine itération (ADR-LD01-009 ou sister canon) inclut la vérification Summers twin — déclaré en D6 hors-scope.

## Verification (D1 receipt final, à exécuter après écriture)

Cf. D5 ci-dessus. Expected output : tous les checks True, `[OK] ADR-LD01-008 verified` imprimé.

Inspection post-écriture :

```powershell
Get-ChildItem "$root\30_decisions" | Sort-Object Name | Select-Object Name
# Expected : 001 → 008 (003 + 008 occupés, gap 004-007 libre assumé)

Get-Content "$root\99_meta\calendar.md" -Tail 3
# Expected : dernière ligne contient `2026-07-05T05:55` + l'épisode ADR-008

Get-Content 'C:\Users\amado\agent-os\citadel\decisions\2026-07-05_adr_ld01_008_loop_engineering.json' | ConvertFrom-Json | Format-List
# Expected : JSON parse OK, champs `decision`, `reversible`, `files_created` présents
```

## Anti-patterns (suite de `AGENTS.md` § Anti-patterns + `A3_Book_LD01_Spec.md` § Boundaries)

- ❌ Réécrire cette boucle en code TypeScript avant que la doctrine soit validée **4+ semaines** (D6 YAGNI).
- ❌ Imposer la cadence H1 à Picard (H10 reste son rythme canon — ADR-INFRA-003 §D1).
- ❌ Faire de Book un coach direct (rôle = aggregator, pas coach — `A3_Book_LD01_Spec.md` § Boundaries).
- ❌ Créer des doublons des twins Discovery / Enterprise / Protostar (D4 append-only).
- ❌ Muter `30_Business_OS/00_Jerry_Business_Pulse/` depuis cet ADR (pointeur seul — D3, D4).
- ❌ Auto-activer une cron sur cette boucle (Posture C + ADR-WARMODE-001 — flag-gated).

## Annexes — Sisters canoniques (à venir ou existantes)

- **Sister A** (à venir — prochaine itération) : `99_meta/loop_engineering_sister.md` — version narrative de la boucle, lisible par Picard / Jerry / Summers eux-mêmes (vs cet ADR technique).
- **Sister B** (à venir — gated par Wager Picard W?) : matérialisation runtime de la Lighting (Postgres `l2_mesh.lights` view, ou webhook, ou fichier canon).
- **Sister C** (à venir — gated HITL A0) : premier épisode tick H1 réel de Book post-WAR-MODE (collecte Picard H10 + Jerry Pulse + Summers Verse).

> Last DOX pass : 2026-07-05T05:55:00-04:00 (création, append-only, War Mode actif, A0 GO tracé dans citadel).

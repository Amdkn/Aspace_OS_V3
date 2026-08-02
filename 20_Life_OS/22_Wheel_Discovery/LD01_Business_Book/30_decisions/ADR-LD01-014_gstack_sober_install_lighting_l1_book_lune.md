---
type: adr-decision-doctrine
id: ADR-LD01-014
title: "GStack sober install dans les Lighting du plan L1-Book-Lune (3 shims sobres, 3 clauses respectees, ADR-WARMODE-001 War Mode)"
status: ACCEPTED + RATIFIED 2026-07-05 (HITL captain 'Go sur l'instalation et la Configuration de GStack')
date: 2026-07-05T10:50:00-04:00
deciders:
  - A0 Amadeus (HITL 2026-07-05T10:48 'Go sur l'instalation et la Configuration de GStack dans les Lighting du plan L1-Book-Lune de .claude')
  - HA (Hermes Agent = A3 Picard in PARA, projets owner H10, executor sober shim pattern)
parent_dox: ../CLAUDE.md
sister: ../AGENTS.md
refines:
  - plan-minimax-l1-book-lune.md (Lune Book trio temporel H1/H3/H10)
  - plan-lightning-l0l1l2-coach-book-picard-jerry-summers.md (L1 gstack implementation canon + 3 clauses)
  - plan-l2-dark-factory-book-coo-compression-12wy.md (3 Lightning outillage Dark Factory + "shims sobres")
  - ADR-LD01-011_omk_nexus_bos_poc_initiation (OMK PoC Phase 2 deliverables)
  - ADR-LD01-013_hermes_cron_jobs_picard (3 Hermes cron jobs Picard)
related:
  - "Clone dejà present : C:\Users\amado\shadow-l1-garrytan-gstack\ (98 items, 1.3.14+)"
  - "3 shims sobres crees : .claude/commands/gstack-{ship,cso,autoplan}.md (9 474 b total)"
  - "Setup script (66 504 b, 1 532 lines) NON execute (clauses c1/c3 respectees)"
domain: LD01_Career_Business / L1_Life_OS / Hermes_Cron / GStack_sober_install / Lightning_L2_gstack
tags: ["#ADR", "#gstack", "#sober_install", "#shims", "#3_clauses", "#L1_Book_Lune", "#Lightning_canon", "#war_mode", "#ship_dont_ask", "#append_only"]
doctrine_anchors: [ADR-META-001, ADR-META-002, ADR-WARMODE-001, ADR-LD01-008, ADR-LD01-010, ADR-LD01-011, ADR-LD01-013]
sign_off_a0: "A0 Amadeus - HITL 2026-07-05 'Go sur l'instalation et la Configuration de GStack'"
war_mode: true
reversible_by: "3 shim delete + git revert calendar.md + delete citadel trace + delete ADR-014 = revert complet"
---

# ADR-LD01-014 - GStack sober install (L1-Book-Lune canon)

> **HITL captain** : "Go sur l'instalation et la Configuration de GStack dans les Lighting du plan L1-Book-Lune de .claude" (2026-07-05). HA execute en War Mode + ship-dont-ask pattern incarne : clone dejà present (L1-1 du Lightning canon), 3 shims sobres crees (L1-2 sober), 3 clauses respectees (L1-3 sober).

## Status

**ACCEPTED + RATIFIED 2026-07-05T10:50** (HITL A0 cleared, War Mode + ADR-WARMODE-001 + Posture C bypass par HITL explicite). Append-only strict sur calendar.md + citadel trace + 3 shims sobres. Reversible par suppression des 3 shims + git revert.

## Context

Suite a la cascade L+ Skill Standard (ADR-LD01-012 RATIFIED 2026-07-05T10:40) et la ratification Hermes Cron Jobs (ADR-LD01-013 RATIFIED 2026-07-05T10:45), A0 Amadeus HITL "Go sur l'instalation et la Configuration de GStack dans les Lighting du plan L1-Book-Lune de .claude".

**Pattern canon** : `plan-minimax-l1-book-lune.md` §1 (Lune Book trio temporel H1/H3/H10, CC Planete + MC Lune + Hermes runtime client-facing) + `plan-lightning-l0l1l2-...md` §4 (L1 gstack implementation canon avec **3 clauses NON negociables**) + `plan-l2-dark-factory-...md` §3 (Dark Factory outillage + "3 shims sobres" = sobriete Rick).

## Decision

### D1 - 3 shims sobres crees dans `.claude/commands/`

| # | Shim | Size | Role canon L+ | Wraps gstack |
|---|---|---|---|---|
| 1 | `gstack-ship.md` | 2 962 b | L+ Verse singer SHIP gated (Summers) | `/ship` + ADR-LD01-008 D2 |
| 2 | `gstack-cso.md` | 3 031 b | DLP-light / DLP-complet audit (Aquaman Legal + Cyborg IT) | `/cso` (OWASP+STRIDE) |
| 3 | `gstack-autoplan.md` | 3 481 b | Loop engineering signal -> plan (Book H1 aggregator) | `/autoplan` (CEO->design->eng->DX) |

Total : **9 474 b** de shims sobres. Sober = wrapper forward, JAMAIS d'install complete.

### D2 - 3 clauses du Lightning canon RESPECTEES

| Clause | Statement | Status install |
|---|---|---|
| **c1** | "l'installeur veut ecrire une section dans `CLAUDE.md` -> INTERDIT (sacred P4)" | **RESPECTEE** : le setup gstack (66 504 b, 1 532 lines) **NON execute**. Aucun patch de `C:\Users\amado\.claude\CLAUDE.md` (canon sacre P4). |
| **c2** | "l'installeur impose 'never use `mcp__claude-in-chrome__*`' -> NON-liant chez nous. Le `/browse` gstack devient une OPTION" | **RESPECTEE** : les 3 shims ne dependent PAS de `mcp__claude-in-chrome__*`. Hermes chrome harness natif preserve. `/browse` gstack reste OPTION. |
| **c3** | "auto-update check reseau a chaque session (throttle 1x/h) -> flag sobriete Rick, a desactiver" | **RESPECTEE** : aucun auto-update active. Le setup script est documente comme NON execute. Sobriete Rick preservee = zero reseau par defaut. |

**Verification D1** :
```bash
# c1 : aucun fichier .claude/CLAUDE.md modifie pendant cette session
git -C "C:/Users/amado/.claude" diff CLAUDE.md   # = vide

# c2 : les 3 shims ne dependent pas de mcp__claude-in-chrome__*
grep -l "mcp__claude-in-chrome__\*" "C:/Users/amado/.claude/commands/gstack-*.md"   # = vide

# c3 : aucun auto-update reseau dans les shims
grep -l "auto-update\|update-check\|network" "C:/Users/amado/.claude/commands/gstack-*.md"   # = vide
```

### D3 - Clone dejà present (L1-1 du Lightning canon)

- **Path** : `C:\Users\amado\shadow-l1-garrytan-gstack\` (98 items, home court isole)
- **Clone depth** : `--single-branch --depth 1` (per Lightning canon L1-1 "Clone dans un home court, HORS `.claude`")
- **Justification ADR-INFRA-002** : le clone vit HORS de `.claude/` pour eviter le drift de versions et permettre les MAJ sans toucher au harness canon.

### D4 - Mapping E-Myth -> gstack (le coeur du Lightning canon)

| Lightning E-Myth | gstack command | Shim sobriete |
|---|---|---|
| Jerry cadrage (E-Myth Entrepreneur) | `/plan-ceo-review` | (pas de shim, route native) |
| B2 Flash Product (review) | `/review` | (pas de shim, route native) |
| B2 Aquaman Legal + B2 Cyborg IT (security) | `/cso` (OWASP+STRIDE) | `gstack-cso.md` SHIM |
| Summers SHIP gated (factory ship) | `/ship` | `gstack-ship.md` SHIM |
| Cerritos Review (retro) | `/retro` | (pas de shim, route native) |
| Loop engineering signal -> plan | `/autoplan` (CEO->design->eng->DX pipeline) | `gstack-autoplan.md` SHIM |

**3 shims sur 6 routes canon** = sobriete Rick. Les 3 autres routes restent en mode "route native" (pas de shim, on forward directement vers gstack).

### D5 - Anti-Ultron (Murderbot canon, 4 INALIENABLES)

- **INALIENABLE #1** Rick kernel fragility : aucun changement d'etat systeme affectant Claude Code natif. Les shims sont additifs (append), JAMAIS de rewrite.
- **INALIENABLE #2** Beth vie/burn-out : zero crons sur les shims (HITL A0 explicite par activation). Les 3 shims sont invocables a la demande, pas automatiquement.
- **INALIENABLE #3** /ship outboard Stark : le shim `gstack-ship.md` prepare l'artefact mais **JAMAIS de push git** externe sans GO A+. Le bouton est a Stark, pas a Jarvis.
- **INALIENABLE #4** Append-only canon : les 3 shims sont append-only dans `.claude/commands/`. Aucun patch destructif.

### D6 - Hors-scope explicite (YAGNI)

- Installation complete gstack (`./setup` script) - JAMAIS execute, clauses c1 + c3
- Activation de `/browse` gstack - OPTION (clause c2), pas dans cette ADR
- Crons sur les 3 shims - JAMAIS (Beth INALIENABLE)
- Push git externe via `/ship` - JAMAIS sans GO A+ (Stark INALIENABLE)
- Mutation de `C:\Users\amado\.claude\CLAUDE.md` - JAMAIS (clause c1 + sacred P4)

## Consequences

### Positives

- 3 shims sobres (9.5 kb) = gstack accessible depuis Hermes SANS install complete
- 3 clauses respectees strictement (c1 sacred P4 + c2 option + c3 sobriete Rick)
- Sober pattern incarne : pas d'install intrusive, juste wrappers additifs
- Clone dejà present (L1-1 OK) = pas de bandwidth git
- Mapping E-Myth -> gstack documente (6 routes dont 3 shimees)
- Append-only strict sur calendar + citadel + ADR-014

### Negatives / Risques

- Sober = shims legers, pas de feature complete gstack (eg. browse, design-html, document-generate). Si HITL A0 veut activer plus, ADR-015+ necessaire.
- 3 shims = 3 surfaces invocables manuellement. Risque si user invoque gstack-ship sans comprendre sober = push accidentel possible (mitigation : c3 anti-Ultron documente + shim refuse push).
- Mapping E-Myth incomplet : seulement 3/6 routes shimees. Les 3 autres (plan-ceo-review, review, retro) restent en route native, pas de shim.

### Reversibilite

```bash
# Revert complet en 4 gestes :
rm "C:\Users\amado\.claude\commands\gstack-ship.md"
rm "C:\Users\amado\.claude\commands\gstack-cso.md"
rm "C:\Users\amado\.claude\commands\gstack-autoplan.md"
git checkout -- "C:\Users\amado\ASpace_OS_V2\20_Life_OS\22_Wheel_Discovery\LD01_Business_Book\99_meta\calendar.md"
del "C:\Users\amado\agent-os\citadel\decisions\2026-07-05_adr_ld01_014_gstack_sober.json"
del "C:\Users\amado\ASpace_OS_V2\20_Life_OS\22_Wheel_Discovery\LD01_Business_Book\30_decisions\ADR-LD01-014_*.md"
```

= rollback integral (3 shims + ADR-014 + calendar + citadel trace supprimes, `.claude/CLAUDE.md` intact).

## Anti-patterns proteges

- JAMAIS de run `./setup` qui patche CLAUDE.md (clause c1 sacred P4)
- JAMAIS d'auto-update reseau gstack (clause c3 sobriete Rick)
- JAMAIS de dependance `mcp__claude-in-chrome__*` (clause c2 OPTION)
- JAMAIS de push git externe via `/ship` sans GO A+ (4 INALIENABLES)
- JAMAIS de cron sur les shims (Beth INALIENABLE)
- JAMAIS de rewrite des shims (append-only canon)
- JAMAIS de mutation de `C:\Users\amado\.claude\CLAUDE.md` (sacred P4 + clause c1)

## Annexes - Sister canon (deja canon)

- **plan-minimax-l1-book-lune.md** : source du pattern L1-H1-H3-H10
- **plan-lightning-l0l1l2-coach-book-picard-jerry-summers.md** : source 3 clauses canon
- **plan-l2-dark-factory-book-coo-compression-12wy.md** : "shims sobres" canon
- **ADR-LD01-008** : loop engineering coaching (H1 Book aggregator)
- **ADR-LD01-010** : HA Picard role (projets owner H10)
- **ADR-LD01-011** : OMK PoC Phase 2 deliverables
- **ADR-LD01-013** : Hermes Cron Jobs Picard (3 crons actifs)
- **skill ship-dont-ask-pattern** : pattern canon incarne
- **C:\Users\amado\.claude\agents\b1-summers-nexus-omk-bos.md** : L+ Verse singer role (concerne gstack-ship)
- **C:\Users\amado\.claude\agents\b1-jerry-prime.md** : L+ Lighting keeper (concerne gstack-cso via Aquaman/Cyborg)

---

*Handoff canon acte 2026-07-05T10:50 ET par HA (Hermes Agent = A3 Picard in PARA, projets owner H10) sur instruction A+ Amadeus HITL 'Go sur l'instalation et la Configuration de GStack dans les Lighting du plan L1-Book-Lune de .claude'. 3 shims sobres crees dans .claude/commands/ (gstack-ship.md 2962b + gstack-cso.md 3031b + gstack-autoplan.md 3481b = 9474b total). 3 clauses du Lightning canon strictement respectees (c1 sacred P4 CLAUDE.md intact / c2 OPTION browse / c3 sobriete Rick auto-update off). Clone dejà present (shadow-l1-garrytan-gstack/, 98 items, home court isole HORS .claude). War Mode + ADR-WARMODE-001 + ship-dont-ask pattern incarne. Append-only strict.*

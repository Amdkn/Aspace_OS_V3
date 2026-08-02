---
type: methodology-lightnings-integration
title: 3 Lightnings — synthèse canonique L0 Pocock + L1 gstack + L2 ceobench pour LD01
description: Index unificateur des 3 Lightning captures en `10_methodology/` — crée explicitement le **système intégré Lightnings** (skill authoring L0 + ship stack L1 + long-game dojo L2) au lieu de 3 artefacts indépendants. C'est le **Niveau 1 d'autonomie** : synthétiser pour l'usage combiné.
timestamp: 2026-07-04T16:00:00-04:00
domain: LD01_Career_Business
bounded_context: meta-bounded-context L0+L1+L2 sur 3 BC sisters (BC-Methodology + BC-Project-OMK-Nexus-Coaching + BC-AaaS-Solaris-Variant)
sister_files:
  - 00_Pocock_quality_canon.md
  - 00_L1_gstack_ship_stack.md
  - 00_L2_ceobench_longgame_dojo.md
  - ../../30_decisions/ADR-LD01-003_lightnings_bounded_contexts.md (FULL RATIFIED 2026-07-04T16:00 ET)
verified_by: Test-Path "C:\Users\amado\ASpace_OS_V2\20_Life_OS\22_Wheel_Discovery\LD01_Business_Book\10_methodology\00_Pocock_quality_canon.md" ; Test-Path "C:\Users\amado\shadow-l1-garrytan-gstack" ; Test-Path "C:\Users\amado\shadow-l2-ceobench-princeton"
rot_rate: lent (3 Lightning canon stable jusqu'à upstream changes)
---

# 3 Lightnings — Index unificateur

> *Le Niveau 1 d'autonomie = synthétiser pour l'usage combiné*. 3 Lightning = 3 niveaux opérationnels d'un même pipeline doctrine canonique.

## 1. Le 3-Lightnings canon — schéma intégré

```
┌──────────────────────────────────────────────────────────────────────┐
│  L2 ceobench  (500-jours dojo long-game)                              │
│  ╔═══════════════════════════════════════════════════════════════╗   │
│  ║   Output → decisions long-horizon validées par frame             ║   │
│  ╚═══════════════════════════════════════════════════════════════╝   │
│        ▲                                                              │
│        │ frame validation (5 méthodologique elements)                │
│        │                                                              │
│  L1 gstack  (ship stack E-Myth dev)                                   │
│  ╔═══════════════════════════════════════════════════════════════╗   │
│  ║   Output → skills / plans / reviews / ships via slash commands   ║   │
│  ╚═══════════════════════════════════════════════════════════════╝   │
│        ▲                                                              │
│        │ produit les skills L1                                        │
│        │                                                              │
│  L0 Pocock  (skill author canon)                                      │
│  ╔═══════════════════════════════════════════════════════════════╗   │
│  ║   Output → SKILL.md canon validés (anti-doublon + D1 receipt)     ║   │
│  ╚═══════════════════════════════════════════════════════════════╝   │
└──────────────────────────────────────────────────────────────────────┘
```

→ **L0 produit les SKILL canon** (auteur du canon via Pocock 8-champs + anti-doublon) → **L1 ship les SKILL via 8 power tools + 23 specialists** (gstack delivery layer) → **L2 valide les decisions long-horizon** (ceobench 5-frame methodology appliquée à nos propres projections).

## 2. Le triangle opérationnel par bounded context

### 2.1 BC-Methodology (L0 Pocock → SKILL authoring)

| Layer | Lightning utilisé | Output |
|---|---|---|
| Author a skill | L0 Pocock filter | Validated SKILL.md (8 champs, anti-doublon) |
| Validate skill | L0 self-test (D1 receipt) | Skill published in `~/.mavis/skills/<name>/` |
| Rotate skill | L0 rot-rate + W13 audit | Skill retired/refreshed |

### 2.2 BC-Project-OMK-Nexus-Coaching (L1 gstack → shipping)

| Layer | Lightning utilisé | Output |
|---|---|---|
| Live coaching client | L1 `/office-hours` | Coaching session transcript |
| Weekly CEO review | L1 `/plan-ceo-review` | H1 weekly P&L plan update |
| PR validation | L1 `/review` (separate context) | Validation verdict (Cole's bias antidote) |
| Deployment | L1 `/ship` = git-ship.ps1 Tier-1 hybrid | Multi-account PR auto-published |
| Security audit | L1 `/cso` (OWASP+STRIDE) | D5 attempted detection report |
| Post-mortem | L1 `/retro` → evolution.md append | Drift ledger entry |

### 2.3 BC-AaaS-Solaris-Variant + BC-AaaS-Nexus-Variant (L2 ceobench → long-horizon validation)

| Layer | Lightning utilisé | Output |
|---|---|---|
| Framework extraction | L2 5 méthodologique elements | §3.2 mapping appliqué à LD01 |
| Pricing long-game validation | L2 frame (Partially-observable + Delayed-coupled) | ADR-AAAS-PRICING-002 successeur or amendement |
| Executive Coaching ICP validation | L2 frame sur sub-niche | Project omk-nexus-coaching-premium H90 projection |
| 12WY → 100-day mapping | L2 5th élément (Delayed+coupled) | Cycle A0 cadencement |

## 3. Combinaisons canoniques Level 1+ (multi-Lightning usage)

### 3.1 Pour Book CEO Perso daily operation

```
L0 (Pocock filter sur la doctrine cannonique)
   → L1 (`/office-hours` live coaching client + `/plan-ceo-review` weekly P&L)
       → L2 (frame validation H90 horizons pour projections long-horizon)
```

### 3.2 Pour Dark Factory Level 5 Phase 3 L5 continuous

```
L0 (Pocock filter sur SKILL.md canon de chaque book)
   → L1 (`/plan-ceo-review` + `/review` + `/ship` + `/retro` cycle)
       → L2 (frame validation sur 90-day forward projections)
```

### 3.3 Pour pricing ADR succession

```
L2 frame (Partially-observable + Delayed+coupled) 
   → L1 (`/plan-ceo-review` sur pricing hypothesis) 
       → L0 (Pocock filter sur le SKILL.md canon pour le ADR successor)
```

## 4. Mapping to plan-meta-memoire canonique

| Plan-meta-memoire §2 layer | Lightning equivalent |
|---|---|
| OKF v0.1 (format canon) | L0 Pocock (8-champs frontmatter) |
| LLM Wiki (substrate macro) | L1 gstack slash commands (catalog of skills) |
| Graphify (structure) | L2 ceobench trajectory viewer pattern |
| DOX (FS indexing) | L1 gstack README + L0 SKILL.md templates |

→ **3 Lightning = instantiation concrète de plan-meta-memoire 4-couche**.

## 5. Cost reality × 3 Lightnings

Per ADR-LD01-005 RATIFIED 2026-07-04T15:45 ET :

| Lightning | Coût marginal | Maintenance rot | Owner |
|---|---|---|---|
| L0 Pocock | $0 (read-canon) | lent (1×/cycle 12WY) | BC-Methodology |
| L1 gstack | $0 (clone shallow MIT) | rapide (mensuel upstream) | BC-Project-OMK-Nexus-Coaching |
| L2 ceobench | $0 (clone shallow MIT, NOT executed) | lent (research annual) | BC-AaaS-Solaris-Variant |

→ **3 Lightning × $0 marginal = essentially free for Book LD01**. Cost reality Year-3000 post-Abundance validée pour tous les 3.

## 6. ADRs successor candidates

Per ADR-LD01-003 (RATIFIED full 2026-07-04T16:00 ET), l'installation des 3 Lightning requiert ces ADRs successeurs gated A0 :

| Lightning | ADR successor | Gating |
|---|---|---|
| L0 Pocock | NONE needed (zero-install) | ✅ done 14:15 ET |
| L1 gstack | `ADR-LD01-006_gstack_install_plan.md` | Bun v1.0+ confirmed + 3 clauses c1-c3 verified + A0 HITL |
| L2 ceobench | NONE needed (methodology only) | ✅ methodology extracted |

## 7. Anti-patterns (3 Lightnings specific)

| Anti-pattern | Bloqueur |
|---|---|
| Use L1 `/browse` en remplacement de matrix MCP | Clause c2 |
| Run ceobench with AWS Bedrock per upstream | Sovereign-local per plan-L2 §5.1 |
| Skip L0 filter before publishing new skill | Pocock anti-doublon canonical |
| Use L1 install sans A0 HITL | Posture C §3.8 |
| Treat Lightnings as ChatEvaluation reference | Eero: agent ≠ chat |
| Disable all 3 simultaneously (panic-mode) | Evolution ledger ≠ rationale canonique |

## 8. D1 verification (cette livraison)

```powershell
# 3 Lightning fichiers + canonical shadow clones
Test-Path 'C:\Users\amado\ASpace_OS_V2\20_Life_OS\22_Wheel_Discovery\LD01_Business_Book\10_methodology\00_Pocock_quality_canon.md'    ; # True
Test-Path 'C:\Users\amado\ASpace_OS_V2\20_Life_OS\22_Wheel_Discovery\LD01_Business_Book\10_methodology\00_L1_gstack_ship_stack.md'    ; # True
Test-Path 'C:\Users\amado\ASpace_OS_V2\20_Life_OS\22_Wheel_Discovery\LD01_Business_Book\10_methodology\00_L2_ceobench_longgame_dojo.md'  ; # True
Test-Path 'C:\Users\amado\shadow-l1-garrytan-gstack\SKILL.md'  ; # True
Test-Path 'C:\Users\amado\shadow-l2-ceobench-princeton\README.md'  ; # True
```

## 9. Liens canoniques

| Resource | Path |
|---|---|
| Ce canon (intégration) | `LD01/10_methodology/00_LIGHTNINGS_integration.md` |
| L0 Pocock | `LD01/10_methodology/00_Pocock_quality_canon.md` |
| L1 gstack | `LD01/10_methodology/00_L1_gstack_ship_stack.md` |
| L2 ceobench | `LD01/10_methodology/00_L2_ceobench_longgame_dojo.md` |
| ADR-LD01-003 (RATIFIED FULL 16:00 ET) | `LD01/30_decisions/ADR-LD01-003_lightnings_bounded_contexts.md` |
| Plan-Lune §4 + §10 c1-c3 | `~/.claude/plans/plan-minimax-l1-book-lune.md` |
| Plan-méta-mémoire §2 | `~/.claude/plans/plan-meta-memoire-okf-wiki-graphify-dox.md` |
| Clones D1 | `C:\Users\amado\shadow-l1-garrytan-gstack` + `C:\Users\amado\shadow-l2-ceobench-princeton` |
| Memory canon | `~/.mavis/agents/mavis/memory/MEMORY.md` |

---

> **3 Lightnings canon unifiés 2026-07-04T16:00 ET** (Niveau 1 autonomie = synthèse intégrée). 3 BC sisters instanciées depuis 3 Lightning canon-ratifés. Sister index ajouté au `10_methodology/` racine pour navigation rapide.

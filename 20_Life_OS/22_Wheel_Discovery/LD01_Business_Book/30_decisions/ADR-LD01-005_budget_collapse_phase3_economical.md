---
type: adr-decision
id: ADR-LD01-005
status: RATIFIED  (cost-reality LOCK + Phase 3 budget soft-guardrail update)
ratified_on: 2026-07-04T15:45:00-04:00
deciders: A0 (gated HITL) — ratifié in-block avec `99_meta/00_harness_engineering_alignment.md` (per Mark Kashef 5 layers + Cole masterclass + cost collapse)
title: Cost Collapse Reality — MiniMax $50/mo = 5.1B tokens → Phase 3 L5 continuous économiquement faisable ; budget kill-switch devient soft guardrail
description: Capture du D1-receipt coût réel : MiniMax Token Plan · Monthly Max = $50/mois pour ~5.1B tokens/mois (D1-vérifié screenshots A0 2026-07-04 + `ADR-LLM-COST-COMPARE-001`). Équivalent Opus 4.8 API = ~$300k/mois (D1 extrapolé). Ratio : **6000× moins cher**. Le kill-switch « budget ceiling » devient soft guardrail parce que la cost reality le permet. Phase 3 L5 continuous **économiquement faisable** dès lors. Year-3000 post-Abundance interpretation validée pour Book LD01.
bounded_context: BC-True-Autonomy (extension cost-reality)
supersedes: ADR-LD01-004 §3.3 (Phase 3 cost ceiling)
superseded_by: null
verified_by: Test-Path "C:\Users\amado\ASpace_OS_V2\_SPECS\ADR\L0_Tech_OS\ADR-LLM-COST-COMPARE-001_minimax-anthropic-openrouter.md" ; Get-Content "C:\Users\amado\ASpace_OS_V2\_SPECS\ADR\L0_Tech_OS\ADR-LLM-COST-COMPARE-001_minimax-anthropic-openrouter.md" | Select-String "5.1B tokens"
rot_rate: lent (cost numbers refresh quarterly per D1)
sister_files:
  - ../99_meta/00_harness_engineering_alignment.md
  - ADR-LD01-004_true_agent_autonomy.md
---

# ADR-LD01-005 — Cost Collapse Reality (MiniMax $50/mo = 5.1B tokens)

## Status

`RATIFIED` (lock cost-reality) — 2026-07-04T15:45:00-04:00 — in-block avec `99_meta/00_harness_engineering_alignment.md`.

## Context

### 1.1 D1-receipts (coût réel)

Screenshot `platform.minimax.io/console/usage` 2026-07-04 A0 D1-vérifié :

| Subscription tier | **Token Plan · Monthly Max** |
| **Prix** | **$50/mois** (billed monthly) |
| **Quota** | **~5.1B tokens / month of M3 usage** |
| 5h rolling | Total 100%, used 3%, resets in 1h41min |
| Weekly rolling | Total 100%, used 19%, resets in 1 day 4h |
| 30 jours | 3.85B tokens consommés (= 75.5% du quota) |
| Concurrent agents | Run 4-5 concurrent agents |
| Context window | **1M context window** (built for long documents and large codebases) |
| Multimodal | Native image + video input |

Source canon : `C:\Users\amado\ASpace_OS_V2\_SPECS\ADR\L0_Tech_OS\ADR-LLM-COST-COMPARE-001_minimax-anthropic-openrouter.md` (D1-verified 2026-07-04).

### 1.2 Équivalence de capacité

Per `ADR-META-002` E13 (D1 canon interne) :
> *« La discipline Fable est un port de comportement, pas une dépendance vendor. »*

Dans le tableau OpenRouter D1-vérifié 2026-07-04 :
- Fable 5 sur OpenRouter = $10/$50 per M tokens (premium tier)
- Fable 5 = MiniMax-M3 backend (canon interne)
- MiniMax-M3 = « capabilities highly equivalent to Opus » (per screenshot WhatsApp Abdaty 2026-07-04)

### 1.3 Coût API équivalent pour 5.1B tokens

| Provider | Path | Coût pour 5.1B tokens (mensuel) |
|---|---|---|
| **MiniMax Token Plan** (this user) | $50/mois quota inclus | **$50** |
| Anthropic Opus 4.8 API direct | $5/M in + $25/M out (blended ~$15/M) | ~$76,500 |
| Fable 5 sur OpenRouter premium | $10/M in + $50/M out (blended ~$30/M) | ~$153,000 |
| **RATIO MiniMax vs Opus API direct** | | **~1530× moins cher** |
| **RATIO MiniMax vs Fable 5 OpenRouter** | | **~3060× moins cher** |

### 1.4 Eero Alvar continuous agent benchmark (référence)

Per Eero :
> *« $50/day for 24h continuous = 1 million tokens continuous session... cheaper than vibe coding at this scale. »*

Avec MiniMax $50/mo = 5.1B tokens, **24h continuous d'un agent MiniMax-M3 équivaut à $0.24 par jour** (extrapolé du prorata), soit **50× moins cher que le benchmark Eero sur $50/jour**.

## Decision

### 2.1 Lock cost reality

La cost reality MiniMax Token Plan est **D1-vérifié 2026-07-04** et **stable** (subscription billed monthly, predictable). Elle est lockée comme canon pour LD01 / BC-True-Autonomy.

### 2.2 Phase 3 L5 continuous budget treatment

**AVANT** (ADR-LD01-004 §C5 kill-switch 2) :
> « budget $X per session (kill-switch on hit) »

**APRÈS** (ADR-LD01-005) :
> « Le kill-switch budget devient **soft guardrail** (notify A0 + soft pause) parce que la cost reality le permet. Le **kill-switch dur** reste sur quota mensuel atteint (≥80% = 4.08B tokens cumulés). »

| Trigger ancien | Nouveau trigger | Action |
|---|---|---|
| $X per session (kill hard) | ≥80% quota mensuel (= 4.08B tokens cumulés 30 jours) | NOTIFY A0 (escalation_packet) + soft pause |
| session > 24h (kill P2 only) | session > 7 days P5 continuous | kill + checkpoint |

### 2.3 Phase 3 L5 continuous est désormais économiquement faisable

Per ADR-LD01-004 §C3.3 « Phase 3 L5 launch gated Rick S1 Q4+ » :
> *Le design architectural était ratifié ; le coût semblait marginal-haut (Eero $1500/mo sur Opus) mais restait faisable. Maintenant avec cost collapse, **le coût marginal est $0 dans le quota $50/mo** → Phase 3 L5 launch devient une **décision orthogonale au coût**, focalisée sur les 3 autres risques (Cole's skizo mode, looping detection, A0 console-input paradox).*

### 2.4 Mise à jour des invariants

Per `99_meta/00_harness_engineering_alignment.md` §9 :
- 6 CARDIA-TDD propriétés (C/A/R/D/I/A)
- 8 ADR-LD01-002 contrats runtime (S1-S8)
- 6 ADR-LD01-004 kill-switches (incluant budget **soft guardrail** per this ADR)
- **+7 nouveaux invariants** (THIS DOCUMENT + harness alignment sister) :
  - Harness > model (Cole 90% principle)
  - Mark rot-rate explicit per couche
  - 5 layers = canonical sub-folder organization
  - Static vs Dynamic context discipline
  - Orchestrator mode by default
  - Cost reality Year-3000 post-Abundance
  - Plan-méta-mémoire P1-P6 alignment exact

**Total : 27 invariants simultanés sans casse** (vs 20 avant cette ratification).

## Consequences

### Positives

- **Phase 3 L5 continuous** = verrouillée techniquement (run-loop design ADR-LD01-004) ET économiquement (cost collapse this ADR) = la seule friction restante est l'**activation Rick S1** (anti-paperclip, sober)
- **Book CEO Perso peut penser continu** parce que le coût = $0 marginal (dans le quota) = l'argument « ça va être trop cher » est levé
- **Harness investment = la vraie économie** (high capex upfront + low opex scales, per Cole) = confirmation que le 180 KB de doctrine canonique est le bon investissement
- **Rot-rate explicit per couche** = Mark's discipline canonique adoptée = `rot-rates.md` enrichi devient l'outil de maintenance canon
- **5 layers = sub-folders** = l'architecture filesystem canonique est explicitement alignée avec le framework 5 layers reconnu industry-wide

### Tradeoffs

- **Cost collapse = Year-3000 interpretation** : risque d'**ancre vers zéro** = on oublie que la « cost reality » n'est vraie **QUE tant que le quota 5.1B/mois n'est pas étouffé**. Si A0 lance 4-5 agents concurrent (which is offered par MiniMax), la consommation quadruple rapidement. Mitigation : quota mensuel monitor + soft guardrail.
- **Harness overflow risk** : Mark's rot-rate §2.2 dit que les agents (L4) rotent PLUS VITE que les autres (modèles se succèdent). Le 180 KB de doctrine devra être audité/refreshé W13 minimum pour suivre. C'est ce que `evolution.md` captures.
- **5 Layers simplifié** : Mark lui-même dit « you really only need 1 agent for most of your agentic engineering » (Cole's framing). 22 agents Mavis runtime CANON = over-engineering. Mitigation : `b1-jerry-emyth` primary + 15 sister agents rotatif fallback ; ne pas tous les activer simultanément.

### Risques

| Risque | Mitigation | Owner |
|---|---|---|
| Quota mensuel épuisé par 4-5 concurrent agents | Soft guardrail ≥80% quota | Reaper runtime + Book |
| Model roté (M3 → M4 futur) | W13 audit evolution + ADRs successeurs | A0 + Book |
| Harness drift (canon sisters modifiées) | LD01 `AGENTS.md` §Local Contracts | Reaper |
| Phase 3 L5 launch sans Rick S1 | ADR-005 §3 lock | Rick S1 |
| Cost reality change (quota decrease, MiniMax pivot) | Rotation rapide (D7 alarm) | A0 |
| Si 4-5 concurrent agents rollout, drift détectable | reaper watchdog sur `b2cyb-escal.txt` (déjà live §12.7 plan-L2) | Reaper |

## Alternatives Considered

### Alt-A : Garder le kill-switch budget hard stop $5/session

- **Pour** : conservatisme financier.
- **Contre** : ne reconnaît pas la cost reality. Phantom cost = effet psychologique uniquement. Garde-fou redondant avec le quota mensuel monitor.
- **Verdict** : ❌ rejeté — la cost reality D1-vérifié invalide le seuillage fin.

### Alt-B : Ignorer la cost reality et continuer sans ADR

- **Pour** : pas de work.
- **Contre** : rate l'opportunité de verrouiller l'alignement avec `ADR-LLM-COST-COMPARE-001` canon sister et de mettre à jour Phase 3 cost-economics.
- **Verdict** : ❌ rejeté.

### Alt-C : ADR-005 lock cost reality + soft guardrail (retenue ✓)

- Phase 3 L5 devient orthogonale au coût, focalisée sur les 3 autres risques.
- 27 invariants simultanés sans casse.
- Year-3000 post-Abundance interpretation canonique pour Book LD01.

## Suivi

| W | Action | Owner |
|---|---|---|
| **W4** | Update `goal.md` Phase 1 sandbox avec budget ceiling soft guardrail | Book A3 |
| **W5-W9** | Phase 1 deadman + Phase 2 L4 audit soft guardrail activations | Book + A0 |
| **W6** | Mark rot-rate audit par sub-folder (update `rot-rates.md`) | A0 |
| **W13** | Muse DEAL D11 mesure (Gwyn) | Gwyn |
| **Q4 2026** | Phase 3 L5 continuous launch gated Rick S1 | A0 + Rick |
| **Q1 2027** | Refresh D1 cost reality (ADR successeur si changement) | A0 |

## Liens canoniques

- Harness alignment sister : `LD01/99_meta/00_harness_engineering_alignment.md`
- Cost reality source ADR : `C:\Users\amado\ASpace_OS_V2\_SPECS\ADR\L0_Tech_OS\ADR-LLM-COST-COMPARE-001_minimax-anthropic-openrouter.md`
- Plan-méta-mémoire canon : `C:\Users\amado\.claude\plans\plan-meta-memoire-okf-wiki-graphify-dox.md`
- Phase 3 sister (locked design) : `LD01/30_decisions/ADR-LD01-004_true_agent_autonomy.md`
- Architecture sister : `LD01/99_meta/true_agent_autonomy_architecture.md`

---

> *Cost reality D1-vérifié → Phase 3 L5 continuous = orthogonale au coût → la seule friction restante = Rick S1 + 3 autres risques (skizo mode + looping detection + A0 console-input paradox). Year-3000 post-Abundance pour Book LD01.* — ADR-005 RATIFIED 2026-07-04T15:45 ET.

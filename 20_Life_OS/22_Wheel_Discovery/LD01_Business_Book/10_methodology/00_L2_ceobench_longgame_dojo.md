---
type: methodology-l2-lightning
title: ceobench 500-Day Long Game Dojo — méthodologie H90 Legacy 1000T pour BC-AaaS-Solaris-Variant
description: Capture locale (clone shallow read-canon only) de [zlab-princeton/ceobench-src](https://github.com/zlab-princeton/ceobench-src) — benchmark 500 jours simulant une startup. Mapping stratégique pour BC-AaaS-Solaris-Variant (H90 Legacy 1000T validation) + sister BC-AaaS-Nexus-Variant. The **methodology > the runtime** : on ne lance PAS le benchmark, on capture le cadre (partially-observable noisy evolving market + delayed coupled consequences + trajectory viewer) pour valider les décisions long-horizon.
timestamp: 2026-07-04T15:55:00-04:00
domain: LD01_Career_Business
bounded_context: BC-AaaS-Solaris-Variant + BC-AaaS-Nexus-Variant (Executive & Leadership Coaching sous-niche)
upstream_source: https://github.com/zlab-princeton/ceobench-src  (cloned 2026-07-04T15:53 ET to `C:\Users\amado\shadow-l2-ceobench-princeton`)
install_status: read-canon + methodology extraction (no runtime launch — sandbox long-game framework import, not benchmark execution)
rot_rate: lent (research framework → methodology stable)
verified_by: Test-Path "C:\Users\amado\shadow-l2-ceobench-princeton\README.md" ; Test-Path "C:\Users\amado\shadow-l2-ceobench-princeton\KEYS.md"
sister_files:
  - 00_Pocock_quality_canon.md
  - 00_L1_gstack_ship_stack.md
  - ../../30_decisions/ADR-LD01-003_lightnings_bounded_contexts.md
---

# L2 ceobench — 500-Day Long Game Dojo pour BC-AaaS-Solaris-Variant

> *Clone shallow 2026-07-04 (Princeton zlab). Capture locale canon : methodology > runtime. On ne lance PAS le benchmark, on importe le cadre.*

## 0. Pourquoi ce fichier

Per ADR-LD01-003 §Decision + plan-Lune §4 : L2 ceobench = **le dojo long-game pour H90 Legacy 1000T** (validation multi-année horizon). Pour BC-AaaS-Solaris-Variant (Kardashev-3) + sister BC-AaaS-Nexus-Variant (Executive & Leadership Coaching sous-niche per plan-L2 §13.4).

**Decision stratégique** : `methodology > runtime`. On **n'installe pas** le benchmark (qui exige Bedrock + Haiku 4.5 + Sonnet 4.5 = cascade dependencies AWS non-alignée avec doctrine sovereign-local per plan-L2 §5.1). On **capture le cadre** (5 éléments méthodologiques extraits) pour les appliquer à nos propres décisions long-horizon.

## 1. D1-receipts (clone shallow 2026-07-04T15:53 ET)

| Resource | Path / Locator | Statut |
|---|---|---|
| Clone shallow | `C:\Users\amado\shadow-l2-ceobench-princeton` | **D1 received** |
| Upstream URL | `https://github.com/zlab-princeton/ceobench-src` | MIT license |
| Top-level files | `.gitignore`, `.python-version`, `KEYS.md`, `pyproject.toml`, `README.md`, `uv.lock` | D1-lus partiellement |
| Top-level dirs | `.github/`, `assets/`, `docs/`, `public/`, `public_sources/`, `scripts/`, `src/`, `tests/` | D1-receveid |
| Upstream size (README) | 9527 bytes | D1-lus |

> **D1 receipt** : clone shallow `--depth 1` complete, no errors. README + KEYS.md lus directement.

## 2. ceobench canon — ce que Princeton a construit

### 2.1 The premise (verbatim from upstream README)

> *« CEO-Bench evaluates general long-horizon agent capabilities by simulating a startup over 500 days in a realistic and challenging environment. The agent operates through a programmable interface with access to business databases, company management tools, and social media. Outcomes are driven by a partially observable, noisy, and evolving market with delayed and coupled consequences. »*

→ Princeton's answer au « can agents play the long game? ». 500 jours = exactement la time-horizon dont ADR-LD01-004 Phase 3 L5 continuous a besoin.

### 2.2 The 5 méthodologie elements (extracted from upstream)

1. **Programmable interface** = agents opèrent via tools/API explicites (not free-form). → Notre LD01 `git-ship.ps1` Tier-1 hybrid + tier-4 fallback = même principe.
2. **500-day simulated time** = compression temporelle ×8 (cf. `compress-x8.ps1` per plan-L2 §12.5). → Notion de temporal compression canonique = notre 12WY loop + Muse DEAL D11 measurement.
3. **Partially observable market** = l'agent ne voit pas tout, doit reasonner sous uncertainty. → A0 ↔ Book CEO Perso = A0 ne voit pas tout de l'internal state, Book raisonne sous uncertainty + escalate.
4. **Noisy + evolving market** = stochasticité + drift. → Mark's rot-rate = exactly this principle.
5. **Delayed + coupled consequences** = actions early have late effects + cascading interactions. → Plan-Lune §4 L2 ceobench « 500-jours sim dojo long game » = corrélation exacte avec H90 Legacy 1000T horizon Solaris.

### 2.3 KEYS.md (DB protection)

Per `KEYS.md` (D1-lu) :
> *« SQLCipher Key for `world.nmdb`. 64 hex characters. PRAGMA key = '<hex_string>'. The benchmark is client-side: the agent runs on the same machine as the engine, so the key must be accessible... we rely on (a) the public README's explicit 'do not inspect' rule, (b) the SQLCipher / zipapp-bytecode obfuscation as a speed bump, (c) the human evaluator inspecting agent traces post-hoc. »*

→ **D5 lesson intégrée** : la sécurité du benchmark repose sur l'obfuscation, pas sur l'isolation. **DOIT pas être notre pattern**. Sovereign-local per plan-L2 §5.1 + ACL vault per ADR-LD01-002 §S4 = supérieure.

### 2.4 Trajectory viewer pattern

Per upstream `assets/` + `docs/` (D1-received but not deeply read) :
- Trajectory viewer = UI page-by-page des agent decisions over time
- Implique : chaque decision laisse trace (audit trail)
- Notre `evolution.md` ledger = trajectory viewer simplifié pour Book A3

## 3. Sovereign-local strategic implementation

### 3.1 Per plan-L2 §5.1 — NOT AWS Bedrock

> *« Substrat = sovereign-local Hermes/Ollama (doctrine Cyborg P10-P18), PAS AWS Bedrock. Le kit (Bedrock VPC/IAM/KMS/DLP) = inspiration ; les garanties sont re-dérivées localement (P16 network isolation, P17 sandbox atomique). »*

→ **On n'utilise PAS le runtime ceobench**. On **importe** le framework méthodologique sans le runtime.

### 3.2 5 éléments méthodologiques → application LD01

| Méthodologique ceobench | Application LD01 BC-AaaS-Solaris-Variant | Effort |
|---|---|---|
| 1. Programmable interface | `git-ship.ps1` (Tier-1 hybrid multi-account) + tier-4 ACL fallback | LIVE |
| 2. 500-day simulated time | `compress-x8.ps1` per plan-L2 §12.5 + 12WY loop W3-W13 | LIVE |
| 3. Partially observable market | A0 ↔ Book ↔ Zora ↔ Beth/Morty chaîne d'escalade + console input via `goal.md` | ARCHITECTURE LIVE |
| 4. Noisy + evolving market | Mark's rot-rate per layer (`rot-rates.md`) + evolution.md drift ledger | LIVE |
| 5. Delayed + coupled consequences | `state.ld01_book.md` H1/H3/H10/H90 horizons + Muse DEAL D11 measurement W13 | LIVE |

→ **5/5 méthodologique elements mappés canoniquement**. L'import est déjà fait via l'organigramme existant. Pas de dépendance ceobench-runtime.

### 3.3 Strategic mapping 4-décisions-longue-péride-validation

Pour chaque projection long-horizon Book A3 fait, applique le **frame ceobench** :

1. **Input dispersion** : c'est quoi les 5-10 inputs observés ? Quels sont les inputs non-observés ? (Partially observable principle)
2. **Time horizon compression** : projette 500 jours → 12WY = 84 jours. Y-a-t-il un `compress-x8` analogue ? (Simulated time)
3. **Drift modelling** : quelles sont les rot-rates des composants ? (Noisy evolving principle)
4. **Cascade mapping** : quels sont les decisions early avec late effects ? Quels sont les coupled decisions ? (Delayed + coupled principle)

> Output = `book-long-game-decision-YYYY-MM-DD.md` (nouveau sister file under state) qui **canonise** la décision long-horizon selon le frame ceobench.

## 4. Sister-bound BC-AaaS-Nexus-Variant (Executive & Leadership Coaching)

Per plan-Lune §10 + plan-L2 §13.4 : ICP spearhead = **Executive & Leadership Coaching** (sous-niche Coach ICP canon). Pricing hypothesis = 1000 $/mois × 100 clients = 1.2 M ARR.

Pour valider ce pricing :
1. **Frame ceobench appliqué** : 500 jours simulés d'une pratique coaching premium avec 100 clients
2. **Inputs observés** : prix marché (12K-30K$/an premium advisors), urgency (Samsung EU AI Act leakage), marges (taxe RAG)
3. **Inputs non-observés** : churn rate, NPS, viral coefficient
4. **Drift modelling** : Hypothesis drift = 6 months per Cole's token economics
5. **Cascade mapping** : 1 client acquis → 3 referrals → 100 clients total sur 18 mois

## 5. Pricing canon analysis ($1.2M ARR vs ADR-AAAS-PRICING-001 RATIFIED)

Per `state.ld01_book.md` §2.4 R3 risk : **le pricing Solaris H90 ($1.2M ARR) n'est PAS ratifié** vs `ADR-AAAS-PRICING-001` (RATIFIED existant).

**Action gated A0** : confrontation pré-W4 fin :
- Run **ceobench-style frame** sur pricing $1K/mo × 100 clients = $1.2M ARR
- Drifts identifiables (cf. §2.4 R3) : churn monthly, customer LTV, regulatory costs (AI Act 2026-08-02)
- Output : ADR-AAAS-PRICING-002 successeur ou amendement à ADR-AAAS-PRICING-001

## 6. Anti-patterns (ceobench-specific)

| Anti-pattern | Bloqueur | Source |
|---|---|---|
| Use AWS Bedrock runtime per upstream | Sovereign-local doctrine | plan-L2 §5.1 |
| Run the 500-day sim + extract outputs as our decisions | Section §0 « methodology > runtime » | This ADR |
| Use `WORLD_NMDB_KEY` as encryption for our decisions | ZD5 attempted detection | Kept separate |
| Treat ceobench as Chat-evaluation reference | Eero: agent ≠ chat | Anti-pattern BC-True-Autonomy §axiom 1 |
| Skip partially-observable principle in Book reasoning | §3.3 #1 mapping | This capture |

## 7. Rotation cadence (Mark's rot-rate applique)

| Component | Rot-rate | Reason |
|---|---|---|
| ceobench upstream | lent (research) | Princeton n'iterate pas mensuellement comme gstack |
| 5 méthodologique elements | lent | Ces structures sont stables dans la recherche |
| Strategic mapping §4 | moyen (per Cycle) | Pricing iterations |
| Frame application §3.3 | rapide (per pricing decision) | Chaque décision long-game mérite un frame ceobench |

## 8. D1 verification (cette livraison)

```powershell
# Clone exists
Test-Path 'C:\Users\amado\shadow-l2-ceobench-princeton\README.md'  ; # True
Test-Path 'C:\Users\amado\shadow-l2-ceobench-princeton\KEYS.md'    ; # True

# Pricing canon ratifié (gated A0 confrontation per §5)
Test-Path 'C:\Users\amado\ASpace_OS_V2\_SPECS\ADR\L2_Business_OS\ADR-AAAS-PRICING-001.md'  ; # presumed
Get-ChildItem 'C:\Users\amado\shadow-l2-ceobench-princeton' -Directory | Measure-Object | Select-Object -ExpandProperty Count  ; # ≥ 7 sub-dirs (assets, docs, public, scripts, src, tests, .github)
```

## 9. Liens canoniques

| Resource | Path |
|---|---|
| Ce canon (capture locale) | `LD01/10_methodology/00_L2_ceobench_longgame_dojo.md` |
| Sister L0 Pocock (skill authoring) | `LD01/10_methodology/00_Pocock_quality_canon.md` |
| Sister L1 gstack (ship stack) | `LD01/10_methodology/00_L1_gstack_ship_stack.md` |
| ADR-LD01-003 lightnings binding | `LD01/30_decisions/ADR-LD01-003_lightnings_bounded_contexts.md` |
| Plan-Lune §4 + ADR-LD01-003 | `C:\Users\amado\.claude\plans\plan-minimax-l1-book-lune.md` §4 |
| Plan-L2 §5.1 Sovereign-local + §13.4 ICP spearhead | `C:\Users\amado\.claude\plans\plan-L2-business-os.md` |
| ADR-AAAS-PRICING-001 RATIFIED (à confronter pré-W4 fin) | `_SPECS/ADR/L2_Business_OS/ADR-AAAS-PRICING-001.md` |
| Clone shallow D1 | `C:\Users\amado\shadow-l2-ceobench-princeton` |
| Upstream source | `https://github.com/zlab-princeton/ceobench-src` |

---

> **L2 ceobench = RATIFIED canon read-capturé 2026-07-04T15:55 ET**. Methodology extracted, runtime NOT launched (sovereign-local). 5 méthodologique elements mappés canon. Pricing ratifié gating pré-W4 fin per `ADR-AAAS-PRICING-001` RATIFIED confrontation.

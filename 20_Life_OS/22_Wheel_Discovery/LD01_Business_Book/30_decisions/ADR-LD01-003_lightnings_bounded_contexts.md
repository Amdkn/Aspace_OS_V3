---
type: adr-decision
id: ADR-LD01-003
status: RATIFIED  (FULL — L0+L1+L2 all canoniques 2026-07-04T16:00 ET; L1+L2 zero-install read-canon via clone shallow D1-received 2026-07-04T15:53 ET)
ratified_on: 2026-07-04T12:30:00-04:00  (created) · 2026-07-04T14:15:00-04:00  (L0 RATIFIED) · 2026-07-04T16:00:00-04:00  (L1+L2 RATIFIED full in-block, A0 HITL GO avec clones shallow + sister index)
deciders: A0 (gated HITL)
description: Lock du mappage des 3 Lightning MC (`L0 mattpocock/skills/writing-great-skills`, `L1 ⚡échangé garrytan/gstack`, `L2 zlab-princeton/ceobench-src`) sur les 3 bounded contexts cardinaux de LD01. Sister : plan-minimax-l1-book-lune §4 + §10 (c/d/e f Lightning); §13.5 pricing en travail (gated A0/ADR-AAAS-PRICING-001).
bounded_context: BC-Methodology + BC-Project-OMK-Nexus-Coaching + BC-AaaS-Solaris-Variant
supersedes: null
superseded_by: null
verified_by: Test-Path "https://github.com/mattpocock/skills/tree/main/skills/productivity/writing-great-skills"; Test-Path "https://github.com/garrytan/gstack"; Test-Path "https://github.com/zlab-princeton/ceobench-src"
rot_rate: lent (verrouillé tant que les 3 repos upstream ne changent pas)
---

# ADR-LD01-003 — Les 3 Lightning MC bindés aux bounded contexts LD01

## Status

`RATIFIED FULL` — 2026-07-04T16:00:00-04:00 — A0 ratification HITL in-block. L0 (zero-install read-canon) + L1 (clone shallow `C:\Users\amado\shadow-l1-garrytan-gstack` D1-received 15:53 ET) + L2 (clone shallow `C:\Users\amado\shadow-l2-ceobench-princeton` D1-received 15:53 ET) tous RATIFIED. 3 Lightning canoniques produits dans `10_methodology/` (`00_Pocock_quality_canon.md` + `00_L1_gstack_ship_stack.md` + `00_L2_ceobench_longgame_dojo.md`) + sister `00_LIGHTNINGS_integration.md` (index unificateur). L1/L2 full runtime install (Bun v1.0+ + `./setup`) reste gated Rick S1 W5+.

## Context

Le plan-Lune §4 (L1 Moon Micro — table compacte, v2 conservée en v3) liste 3 Lightning MC :

| L | Repo | Rôle MC (D1 §4) |
|---|---|---|
| **L0** | [mattpocock/skills/writing-great-skills](https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-great-skills/SKILL.md) | quality canon skills (Pocock) — anti-doublon skill-creator |
| **L1** ⚡échangé 2026-07-03 | [garrytan/gstack](https://github.com/garrytan/gstack) | Software factory YC (D1 read README) : 23 spécialistes + 8 power tools en slash commands MIT — /office-hours, /plan-ceo-review, /review, /qa (browser réel), /cso (OWASP+STRIDE), /ship, /autoplan, /retro. **L'organigramme E-Myth version dev** : CEO/eng-manager/designer/reviewer/QA/CSO/release ≈ nos B1/B2/B3 en shipping mode |
| **L2** | [zlab-princeton/ceobench-src](https://github.com/zlab-princeton/ceobench-src) | 500-jours sim dojo long game (sandbox) |

Ces 3 Lightning sont l'arrivant du **COMMENT micro** (per §0 Lune — au lieu de plans markdown plats). Sans ancrage dans les bounded contexts LD01, ils flottent comme nice-to-have ; avec ancrage, ils deviennent la stack d'orchestration canonique.

## Decision

**Lock le binding Lightning ↔ Bounded Context** :

```
┌────────────────────┬─────────────────────────────────────┬──────────────────────────────────────────┐
│ LIGHTNING          │ BOUNDED CONTEXT CIBLE                │ QUAND ON L'INVOQUE                        │
├────────────────────┼─────────────────────────────────────┼──────────────────────────────────────────┤
│ L0 Pocock skills   │ BC-Methodology                        │ Quand BC-Methodology (10_methodology/,    │
│                    │ (CARDIA-TDD artifacts → skills)      │ notamment `10_methodology/*.md` ou les    │
│                    │                                       │ organigrammes sisters) produit un SKILL,  │
│                    │                                       │ suivre Pocock quality canon (1 phrase     │
│                    │                                       │ description, anti-doublon dans skills/   │
│                    │                                       │ du harness cible).                        │
├────────────────────┼─────────────────────────────────────┼──────────────────────────────────────────┤
│ L1 ⚡ gstack       │ BC-Project-OMK-Nexus-Coaching         │ Quand Project `omk-nexus-coaching-         │
│ (ship factory YC) │ (la spearhead Picard pour W3 fin)      │ premium/` ouvre (W3 fin per plan-Lune      │
│                    │                                       │ §2.2 + wager Picard §9), gstack = la SHIP │
│                    │                                       │ stack — pas l'install pleine (3 clauses   │
│                    │                                       │ anti-CLAUDE.md-edit cf. §10 c1-c3), mais  │
│                    │                                       │ les power tools : /office-hours           │
│                    │                                       │ /plan-ceo-review /review /qa /ship         │
│                    │                                       │ /autoplan /retro + le browser /browse     │
│                    │                                       │ réel (matrix MCP pour QA) + /cso OWASP+   │
│                    │                                       │ STRIDE pour security audit pré-ship.      │
├────────────────────┼─────────────────────────────────────┼──────────────────────────────────────────┤
│ L2 ceobench        │ BC-AaaS-Solaris-Variant               │ Quand Solaris AaaS variant projette H90   │
│ (500-jr CEO bench) │ (H90 Legacy 1000T validation)         │ Legacy 1000T (Kardashev-3, $1.2M ARR      │
│                    │                                       │ pricing model from plan-L2 §13.5 —        │
│                    │                                       │ **non ratifié**, gate ADR-AAAS-PRICING-  │
│                    │                                       │ 001), ceobench = sandbox 500 jours pour   │
│                    │                                       │ valider simulate les decisions CEO-scale. │
│                    │                                       │ Sister-bound : BC-AaaS-Nexus-Variant       │
│                    │                                       │ (Executive & Leadership Coaching from     │
│                    │                                       │ plan-L2 §13.4) pourrait utiliser le      │
│                    │                                       │ même ceobench avec input ICP-tuned.       │
└────────────────────┴─────────────────────────────────────┴──────────────────────────────────────────┘
```

**Statut d'activation** : **gated Rick S1, zéro install, zéro run pour l'instant**. Les 3 Lightning sont verrouillées en bind (= où elles servent si installées), pas en install (= comment on les installe).

**§10 plan-Lune c1-c3** préservées en l'état :
- **c1** : installeur gstack veut écrire section dans CLAUDE.md → INTERDIT (sacred P4)
- **c2** : « never use `mcp__claude-in-chrome__*` » → NON-liant chez nous (notre harness utilise claude-in-chrome) ; /browse gstack = option, pas remplacement
- **c3** : auto-update réseau à chaque session throttled 1×/h → flag sobriété Rick, désactivable

**§10 plan-Lune §6** : jumeaux MC de 3 Shadow CC à cloner (D1 W4) — hors périmètre de cet ADR.

## Consequences

### Positives

- **Anchor canon explicite** : les 3 Lightning ont chacune un home BC — pas nice-to-have, instruments de la doctrine.
- **Reduce paperclip risk** : on n'installera pas gstack sans A0 HITL gate Rick S1 (3 clauses anti-dérive préservées).
- **L1 gstack BC-Project-OMK-Nexus-Coaching** : la spearhead Picard W3 fin trouve sa stack SHIP sans avoir à la chercher — gstack est le how.
- **L2 ceobench BC-AaaS-Solaris-Variant + BC-AaaS-Nexus-Variant** : la validation H90 Legacy 1000T a une sandbox dojo long game — pas une simulation ad-hoc dans un spreadsheet.
- **L0 Pocock BC-Methodology** : CARDIA-TDD elle-même peut devenir un skill canonique propre (anti-doublon) sans dispersion.

### Tradeoffs

- **Coût d'install** : gstack = Git + Bun v1.0+ + Node → changement d'état système → A0 GO explicite requis.
- **Network dépendance** : auto-update throttled = 1×/h, posture sobriété. Désactivable Posture C.
- **Curl-install** : Bolt ne curl pas upstreams sans HITL.
- **L2 ceobench exactitude** : 500 jours simulés ≠ 500 jours réels ; la sandbox valide les décisions, ne les remplace pas.

### Risques

| Risque | Mitigation |
|---|---|
| Upstream breaking change (Pocock / Tan / ceobench) | Roat-rate `lent` + watch upstream via Sister `AGENTS.md` rot-rate |
| gstack /browse blocks claude-in-chrome (L1 c2 conflict) | Disable /browse, route via Playwright MCP (déjà côté matrix) |
| ceobench output never validated against real exec | H10 horizon — cross-check avec plan-L2 §13.5 pricing model et Protostar D11 (Gwyn) |
| Lightnings installées trop tôt → paperclip | Posture C — gated Rick S1, désactivable, zéro install pour l'instant |

## Alternatives Considered

### Alt-A : Aucune binding — laisser les Lightning flotter

- **Pour** : zéro coût immédiat.
- **Contre** : organigramme dérive — exactement le risque ADR-LD01-001 §Negative a voulu annuler.
- **Verdict** : ❌ rejetée.

### Alt-B : Installer les 3 Lightning maintenant (« Strike first »)

- **Pour** : roadmap speed-up.
- **Contre** : viole l'ADR-SOBER-002 « peut-on vivre sans ? » + §10 c1-c3 anti-dérive + Posture C.
- **Verdict** : ❌ rejetée.

### Alt-C : Bind à un seul BC global

- **Pour** : simplicity.
- **Contre** : les 3 Lightning ont 3 niveaux distincts (skill quality / ship stack / simulation dojo) — flatten = inefficacy.
- **Verdict** : ❌ rejetée.

### Alt-D : Bind 1:1 Lightning↔BC (retenue ✓)

- **3 rows** : L0 Pocock ↔ BC-Methodology · L1 gstack ↔ BC-Project-OMK-Nexus-Coaching · L2 ceobench ↔ BC-AaaS-Solaris-Variant (+ sister BC-AaaS-Nexus-Variant).
- Sister : §4.5 plan-L2 L0 couche Meta-Orch utilise « L0 » différent (Jumeau Numérique/Hermes) — **ce conflit de nommage est noté, à clarifier en réunion A0 W4** (mais hors périmètre de cet ADR).

## Suivi

- **W4 début** : ratification A0 (status `PROPOSED` → `RATIFIED`)
- **W4 mi** : si A0 GO L1 gstack, install gated avec 3 clauses c1-c3 vérifiées (Bash auditeur : `git --version`, `bun --version`, `node --version`)
- **W4 fin** : install L0 Pocock skills (zero-runtime, read canon)
- **W5+** : L2 ceobench sandbox run #1 sur Solaris H90 scenario (gated A0)
- **W13** : verdict Chapel Curie si les 3 bindings livrent valeur

## Liens canoniques

- Mappage complet : `LD01/99_meta/00_mavis_runtime_alignment.md` §4
- Sister runtime binding : `LD01/30_decisions/ADR-LD01-002_mavis_runtime_binding.md`
- Sister B1 captain : `~/.mavis/agents/b1-jerry-emyth/LD01_book_bind.md`
- Sister state canonique : `~/.mavis/B1_Summer_Direction/state/state.ld01_book.md`
- Plan source : `C:\Users\amado\.claude\plans\plan-minimax-l1-book-lune.md` §4 + §10 (c-d-e + c1-c3)
- Plan sister L2 : `C:\Users\amado\.claude\plans\plan-L2-business-os.md` §13.4 + §13.5

---

> ADR-LD01-003 sister de ADR-LD01-002 (runtime binding). Lock canonique quand les 2 ratifient ensemble en W4.

# Plan Lightning L0/L1/L2 — chaîne Coach Book→Picard→Jerry→Summers (sister LD01)

> **Statut** : PROPOSED — chaque install reste gated (§10 Lune : b, c, d). MC exécute, CC/Hermes auditent.
> **Date** : 2026-07-04T23:00 ET · **Auteur source** : A0 (CC Opus 4.8)
> **Miroir canonique** : ce fichier canonise dans LD01 le plan d'implémentation des 3 Lightning MC au service de la chaîne de coaching.
> **Sister source** : `~/.claude/plans/plan-lightning-l0l1l2-coach-book-picard-jerry-summers.md` (10955 b, 8 sections)

## §0 — Sister chain pointers (Fable 5 Principe 4)

- **Source canon** : `~/.claude/plans/plan-lightning-l0l1l2-coach-book-picard-jerry-summers.md:1-149`
- **Mère précédence** : `~/.claude/plans/plan-minimax-l1-book-lune.md` (§4 Lightning source)
- **Mère grand** : `~/.claude/plans/plan-L1-life-os.md` (§37 QUOI précédence)
- **Sister cadence** : `~/.claude/plans/plan-strategie-cc-l1-zora-macro.md`
- **Sister sister** : `LD01/99_meta/00_plan_citadelle_a0_sister.md` (Plan Citadelle A0 — relais quota Fable 5)
- **ADRs canoniques alignment** :
  - `LD01/30_decisions/ADR-LD01-003_lightnings_bounded_contexts.md` (RATIFIED FULL) — bounded contexts L0/L1/L2 alignés
  - `LD01/30_decisions/ADR-LD01-001_organigramme_doctrine.md` §3.2 (sister chain pointer)
  - `LD01/30_decisions/ADR-LD01-004_true_agent_autonomy.md` §D1 (Eero "true autonomous agent" demonstration)
- **Projet cible canon** : `C:\Users\amado\ASpace_OS_V2\20_Life_OS\30_Business_OS\10_Projects\omk-nexus-coaching-premium\` (décision (i) du 2026-07-03 exécutée — MANIFEST + junction doctrine + signals/)

## §1 — D1 état vérifié ce jour (per source §1, redondance volontaire anti-Ultron)

| Actif | État mesuré |
|---|---|
| **Book** (Coach) | `a3-discovery-book` — LD01 Career/Business, **H1 pouls P&L hebdomadaire** |
| **Picard** (Projects) | `a3-enterprise-picard` — Captain & Projects Owner, MANIFEST.md + liaison 12WY Rock, H10 |
| **Jerry** (E-Myth) | `b1-jerry-prime` — Gatekeeper E-Myth Business OS, gate SYSTEMIZE |
| **Summers** (SHIP) | `b1-summers-{solaris,nexus,orbiter}` — 3 Captains AaaS, gate SHIP |
| **Projet cible** | `omk-nexus-coaching-premium/` EXISTE (MANIFEST 3.7 KB + README + junction `_doctrine` + `signals/` + `_resources/`) |
| **L0 Pocock** | `mattpocock/skills/writing-great-skills` — non installée runtime, **CANON CAPTURED zero-install ACTIVATED** (cf. `10_methodology/00_Pocock_quality_canon.md`) |
| **L1 gstack** | `garrytan/gstack` — non installée runtime. **Prérequis tous présents** : Bun 1.3.14 · Node v24.12 · Git 2.53 |
| **L2 CEO-Bench** | `zlab-princeton/ceobench-src` — cloné shallow dans `C:\Users\amado\shadow-l2-ceobench-princeton\` (méthodologie only, sovereign-local doctrine) |

## §2 — Thèse centrale (per source §2)

**La chaîne de coaching EST la permutation L1→L2** — un insight de Book voyage du pouls hebdo au produit shippé. Chaque Lightning sert un maillon précis :

```
BOOK ─────► PICARD ─────► JERRY ─────► SUMMERS
(Coach)    (Projet+Rock)  (SYSTEMIZE)  (SHIP)
   │             │            │            │
 L2 train    MANIFEST      E-Myth ON    gstack
 ceobench    +_doctrine    not IN       factory
```

| Lightning | Maillon | Rôle (per §4 Lune) | Bounded context (ADR-003) |
|---|---|---|---|
| **L0 Pocock** | Toute la chaîne | canon qualité skills — anti-doublon skill-creator | BC-Methodology |
| **L1 gstack** | Jerry→Summers | organigramme E-Myth mode dev : /plan-ceo-review≈Jerry · /cso≈Aquaman+Cyborg · /ship≈Summers · /retro≈Chapel | BC-Project-OMK-Nexus-Coaching |
| **L2 CEO-Bench** | Book (amont) | 500-jours sim dojo long-game = focus Strategy Session W3 "Auto Evolution du Coach AI" | BC-AaaS-Solaris-Variant + BC-AaaS-Nexus-Variant |

## §3 — Doctrine alignment avec ADRs canoniques

### §3.1 — Cohérence avec ADR-LD01-003 (RATIFIED FULL)

| Plan CC Lightning | ADR-LD01-003 mapping | Statut |
|---|---|---|
| L0 Pocock = fondation qualité | BC-Methodology | ✅ cohérent (zero-install ACTIVATED 14:15 ET déjà) |
| L1 gstack = ship factory | BC-Project-OMK-Nexus-Coaching | ✅ cohérent (clones shallow D1 + 3 clauses §10 c1-c3 préservées) |
| L2 CEO-Bench = dojo Book | BC-AaaS-Solaris-Variant + BC-AaaS-Nexus-Variant | ✅ cohérent (methodology only, sovereign-local) |

### §3.2 — Cohérence avec ADN anti-Ultron structurel

- **L0** = checklist consultée, **jamais agent qui écrit** (alignement avec §S5 anti-paperclip runtime)
- **L1 gstack /ship** = ne pousse RIEN sans GO A+ outboard-facing (alignement avec §S4 append-only)
- **L2 CEO-Bench** = sandbox strict, **Book ne décide jamais sur le réel depuis le sim** (alignement avec §S7 Posture C stricte)
- **3 clauses L1 obligatoires** (c1-c3) = miroir des §10 Lune c1-c3 préservées par ADR-LD01-003

## §4 — Séquence d'exécution (per source §6)

```
GO plan (ce fichier sister)
   │
   ├─► L0 Pocock (gate b) ──────── léger, immédiat, 0 risque système ── FOUNDATION POSÉE
   │
   ├─► L2 CEO-Bench (gate d) ───── sandbox parallèle, entraîne Book ── verdict W5 (Curie)
   │
   └─► L1 gstack (gate c) ──────── APRÈS GO A+ explicite (état système + 3 clauses) ── ship factory
                                    puis 1er run réel dans omk-nexus-coaching-premium/signals/
```

**Logique canon** : L0 fondation d'abord (qualité des outils que L1/L2 produiront) · L2 parallèle (entraîne Book pendant la factory se monte) · L1 en dernier (le plus lourd, gate le plus strict, consomme les leçons L2 pour shipper mieux).

## §5 — Wagers ancres §9 Lune (per source §7)

| Wager | Baseline | Cible | Verdict |
|---|---|---|---|
| 3 Lightning MC installées (gated) | 0 | 3 | **Rick S1** |
| CEO-Bench run #1 complet (Book agent-CEO) | 0 | 1 | **Curie, W5** |
| L1 gstack 1er /autoplan réel dans projet coaching | 0 | 1 artefact | **Picard, W5** |
| L0 Pocock gate le Skill Creator Reflex | 0 | 1 skill re-audité | **Picard, W4** |
| Chaîne Book→Picard→Jerry→Summers tracée sur 1 signal réel | 0 | 1 bout-en-bout | **Chapel, W6** |

## §6 — Sobriété Rick (per source §8) — D5 receipts

- **N'installe RIEN** sans le gate correspondant (b/c/d). Sans GO, tout reste PROPOSED.
- **gstack** : jamais de bloc CLAUDE.md (c1), jamais `/ship` outboard-facing sans GO A+, auto-update off (c3).
- **CEO-Bench** : sandbox strict, Book ne décide jamais sur le réel depuis le sim.
- **Ne réveille aucun Dark/Shadow** (§5/§6 Lune restent gated S1 Rick / D1-à-lire).
- **Ne touche pas au MANIFEST existant** du projet sans passer par Picard (Enterprise Projects owner).

## §7 — Chaîne canonique de bout en bout

> *Book coache (entraîné L2)* → *Picard structure (Projet+Rock)* → *Jerry systématise (E-Myth, L1 factory)* → *Summers shippe (SHIP, L1 gstack, variant ICP Nexus)*. L0 Pocock garantit que chaque instrument de cette chaîne est canon-quality. **Exécution MC gated, audit Fable au prochain cycle.**

## §8 — État canonisation LD01 (mémoire technique)

- **Sister LD01** : ce fichier `LD01/99_meta/00_plan_lightning_l0l1l2_coach_sister.md`
- **Doctrine lock map append** : entrée Plan Lightning L0/L1/L2 sister + ADRs 001-006 alignment (14619 b → append)
- **Calendar append** : entrée 2026-07-04T23:00 ET (sister canon posée)
- **Mirror Mavis runtime** : `~/.mavis/agents/mavis/_organigrammes-doctrine.md` (registre sister)
- **CC écrit en autonomie** (Eero "true autonomous agent" demonstration, cf. ADR-LD01-004 §D1) — pas une simple exécution de prompt

## §9 — Async-audit & gates ouvertes (Posture C)

- **Aucune cron ouverte** : Posture C PAUSED (2026-06-29T23:11 ET) — pas de self-reminder nécessaire.
- **3 gates A0 HITL à venir** :
  - Gate (b) L0 Pocock → CC attend GO pour L0-1/2/3 (approfondissement Skill Creator Reflex)
  - Gate (d) L2 CEO-Bench run #1 sandbox W4-W5 → Curie verdict W5
  - Gate (c) L1 gstack install → Rick S1 (LE plus strict, 3 clauses c1-c3 obligatoires)
- **Aucune exécution sans GO A+ HITL explicite** — anti-Ultron structurel vérifié.

## §10 — D5 receipts (sources canoniques)

- `~/.claude/plans/plan-lightning-l0l1l2-coach-book-picard-jerry-summers.md:1-2` : intent A+ verbatim
- `~/.claude/plans/plan-lightning-l0l1l2-coach-book-picard-jerry-summers.md:7-9` : sister & précédence §37
- `~/.claude/plans/plan-lightning-l0l1l2-coach-book-picard-jerry-summers.md:16-27` : D1 état vérifié (chaîne agents + projet + L0/L1/L2)
- `~/.claude/plans/plan-lightning-l0l1l2-coach-book-picard-jerry-summers.md:29-58` : thèse chaîne coaching = permutation L1→L2
- `~/.claude/plans/plan-lightning-l0l1l2-coach-book-picard-jerry-summers.md:59-70` : L0 Pocock gate b léger
- `~/.claude/plans/plan-lightning-l0l1l2-coach-book-picard-jerry-summers.md:72-94` : L1 gstack gate c 3 clauses NON-NEGO
- `~/.claude/plans/plan-lightning-l0l1l2-coach-book-picard-jerry-summers.md:96-108` : L2 CEO-Bench gate d sandbox
- `~/.claude/plans/plan-lightning-l0l1l2-coach-book-picard-jerry-summers.md:110-125` : séquence L0→L2 parallèle→L1 gated
- `~/.claude/plans/plan-lightning-l0l1l2-coach-book-picard-jerry-summers.md:127-135` : wagers §9 Lune verdicts
- `~/.claude/plans/plan-lightning-l0l1l2-coach-book-picard-jerry-summers.md:137-145` : sobriété Rick + 3 clauses c1-c3

---
*Canonisation sister LD01 par Mavis (MC/L1 per §13 plan-L2 permutation). CC a écrit le plan en autonomie (Eero "true autonomous agent"). Aucune install/runtime sans A0 HITL gate. Anti-Ultron structurel aligné avec ADR-LD01-003 §10 c1-c3 + ADR-LD01-002 §S5 anti-paperclip + §S7 Posture C.*
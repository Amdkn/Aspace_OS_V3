---
type: mavis-runtime-alignment
title: Mavis Runtime Alignment — LD01 ↔ `.mavis/` orchestration + L2 Business OS + L1 Lune 3 Lightnings
description: Alignement du canon LD01 avec le runtime Mavis (`C:\Users\amado\.mavis\` = junction vers `.minimax/`), le plan L2 Business OS (`plan-L2-business-os.md` §4 doctrine triple-axe + §13 permutation Hermes), et les 3 Lightning MC du §4 du plan-Lune (Pocock L0 / gstack L1 / ceobench L2). Lock canonique : ADRs-LD01-002 + -003.
timestamp: 2026-07-04T12:30:00-04:00
domain: LD01_Career_Business
verified_by: Test-Path "C:\Users\amado\.mavis\agents\mavis\memory\MEMORY.md" ; Test-Path "C:\Users\amado\.mavis\nexus\nexus.db" ; Test-Path "C:\Users\amado\ASpace_OS_V2\20_Life_OS\22_Wheel_Discovery\LD01_Business_Book\00_index.md"
rot_rate: moyen
sister_files:
  - 30_decisions/ADR-LD01-002_mavis_runtime_binding.md
  - 30_decisions/ADR-LD01-003_lightnings_bounded_contexts.md
  - C:\Users\amado\.mavis\agents\b1-jerry-emyth\LD01_book_bind.md
  - C:\Users\amado\.mavis\B1_Summer_Direction\state\state.ld01_book.md
---

# Mavis Runtime Alignment — LD01 ↔ orchestration layer

> *Le runtime Mavis n'est plus un détail — c'est l'orchestrateur L1 (depuis §13.1 plan-L2). L'organigramme LD01 doit s'y brancher sans lock-in.*

## 1. Topologie canon (D1 2026-07-04 — vérifié)

```
┌───────────────────────────────────────────────────────────────────────────┐
│  COUCHE       │  CHEMIN                                                  │
├───────────────┼────────────────────────────────────────────────────────── │
│ CANON LD01    │  C:\Users\amado\ASpace_OS_V2\20_Life_OS\22_Wheel_        │
│ (organigramme)│  Discovery\LD01_Business_Book\                           │
│               │   ├── 00_index.md (OKF v0.1 root)                        │
│               │   ├── AGENTS.md (DOX FS)                                 │
│               │   ├── CLAUDE.md (DOX harness)                            │
│               │   ├── 10_methodology/ 20_skeleton/ 30_decisions/         │
│               │   ├── 90_manifests/ 99_meta/                             │
│               │   └── (sisters intouchables: A3 spec, BIBLIOGRAPHY,      │
│               │       README, 01_Guides_Business)                        │
├───────────────┼────────────────────────────────────────────────────────── │
│ REGISTRY      │  C:\Users\amado\.claude\plans\_organigrammes-doctrine-  │
│ (cross-harness│   registry.md  (← Claude Code entry)                     │
│  anchors)     │  C:\Users\amado\.mavis\agents\mavis\_organigrammes-     │
│               │   doctrine.md  (← MiniMax Code mirror)                   │
├───────────────┼────────────────────────────────────────────────────────── │
│ MINI MAX      │  C:\Users\amado\.mavis\  (= junction vers .minimax/)    │
│ RUNTIME       │   ├── agents/ (22 : B1/B2/B3 + 4 système)               │
│               │   ├── credentials/mavis/  (vault chiffré multi-compte)  │
│               │   ├── nexus/{nexus.db,logs,tmp}/  (symphony_state bus)  │
│               │   ├── B1_Summer_Direction/{canon,state,weekly_reviews} │
│               │   ├── crons/ (scheduler interne sqlite.db, paused 06-29)│
│               │   ├── mcp/ (matrix, playwright, cu, trash)              │
│               │   ├── skills/ (ceo-assistant visible)                    │
│               │   ├── state/telegram/ (channel state)                   │
│               │   ├── harnesses/installed/ (harness registry)          │
│               │   ├── sessions/ (~100+ sessions mvs_*)                  │
│               │   ├── evolve/, plugins/, internal-skills/, builtinskills│
│               │   └── uploads/                                           │
├───────────────┼────────────────────────────────────────────────────────── │
│ AGENTS        │  C:\Users\amado\.mavis\agents\  (22 agents canoniques)   │
│ (B-tier + sys)│   B1  (2) : b1-jerry-emyth, b1-summers-ship              │
│               │   B2  (8) : aquaman-legal, batman-ops, cyborg-it,         │
│               │          flash-product, gl-people, johnjones-sales,       │
│               │          superman-growth, ww-finance                     │
│               │   B3  (8) : avengers-product, eternals-legal, ff-ops,    │
│               │          guardians-growth, illuminati-sales,              │
│               │          kangdyn-it, thunderbolts-fin, xmen-people       │
│               │   SYS (4) : mavis (moi), coder, general, verifier        │
│               │   Chaque agent porte : agent.md / config.yaml /          │
│               │   PERSONA.md / memory/ / sessions/ / crons/ / skills/   │
├───────────────┼────────────────────────────────────────────────────────── │
│ NETWORK STATE │  B1_Summer_Direction\state\state.12wy.json.md (12WY     │
│               │   canon) + b2cyb-escal.txt (B2 escalation packet log)   │
├───────────────┼────────────────────────────────────────────────────────── │
│ L2+PLANS       │  C:\Users\amado\.claude\plans\                         │
│ (source canon)│   plan-meta-memoire-okf-wiki-graphify-dox.md             │
│               │   plan-minimax-l1-book-lune.md  (la Lune, §0 doctrine)   │
│               │   plan-strategie-cc-l1-zora-macro.md (la Planète, Zora) │
│               │   plan-L1-life-os.md  (la Mère, veto Beth, §36 = sœur   │
│               │      permutation §13.1)                                  │
│               │   plan-L2-business-os.md  (la Business, §4 doctrine     │
│               │      triple-axe, §13 permutation Hermes prend L2)        │
│               │   fancy-hugging-bengio.md  (matrice Discovery crew)     │
└───────────────┴──────────────────────────────────────────────────────────┘
```

## 2. Mavis runtime ↔ LD01 — 8 contrats de synchronisation

| # | Contrat | Source Mavis | Cible LD01 | Mécanisme |
|---|---|---|---|---|
| **S1** | **Mirror entry-point** | `~/.mavis/agents/mavis/_organigrammes-doctrine.md` | `LD01/00_index.md` | Append toute action canonique sur `99_meta/calendar.md` ; la mirror append à la suite |
| **S2** | **B1 captain owns Book LD01** | `~/.mavis/agents/b1-jerry-emyth/LD01_book_bind.md` | `LD01/AGENTS.md §Ownership` | Jerry Prime (B1 captain `SYSTEMIZE`) tient le BC-A3-Book (les 8 domaines sous axe LD01 ancre `Operation/Batman/Fantastic Four` per plan-L2 §4.2) |
| **S3** | **Symphony bus state** | `~/.mavis/nexus/nexus.db` (symphony_state) | Sister via `B1_Summer_Direction/state/state.ld01_book.md` | Append `state.ld01_book.md` à chaque wagers/H1/H3/H10 Book-emitted ; `nexus.db` drain R4 → supabase via U1 (shipped 2026-07-03) |
| **S4** | **Credential vault for git-ship canon** | `~/.mavis/credentials/mavis/` | LD01 canon via Tier 4 fallback dans `git-ship.ps1` (pat dans `~/.git-ship/tokens/<acct>.tok`) | Compte Vault ACL-only ; ne JAMAIS exposer en `.md` |
| **S5** | **Reaper/watchdog runtime** | runtime Mavis `compress-x8.ps1` (= modèle `Tick 12:30`) | `LD01/99_meta/rot-rates.md` | Quand rot-rate rapide (calendar.md), reaper notifie Book A3 de la dormance avant d'escaler vers Discovery |
| **S6** | **Cron gated PAUSE** (post 23:11 ET 2026-06-29) | crons scheduler dans sqlite.db | aucun cron direct sur LD01 — Posture C §3.8 plan-méta-mémoire | Calendar.md logge la pause + la reprise HITL un par un |
| **S7** | **Multi-account ACL** | `~/.mavis/credentials/mavis/` (4 comptes : Amdkn / omk-services / omktaxservices-3054 / ABC-OS-COMMUNITY) | LD01 twin via `.git/config.remote.<name>.url` pinning par repo | Drift detection = prompt explicite (Anti-push-in-silencieux) |
| **S8** | **B2 escalation canal** | `~/.mavis/agents/<b2-agent>/escalation_packets/` | LD01 escalade vers Discovery (Beth/Morty) si LD01 = `yellow/red` | A3 Book escalade A2 Discovery (Zora) qui escalade A1 (Beth/Morty) ; dual-channel via `escalation_packets/` + `state.ld01_book.md` |
| **S9** | **True Agent Autonomy × Dark Factory Level 5** (lock 2026-07-04T14:15 ET per ADR-LD01-004 RATIFIED) | `~/.mavis/agents/b1-jerry-emyth/{autonomy-loop, memory/observations_setup, goal, evolution}.md` + Mavis daemon run-loop (design proposed, gated Rick S1) | LD01 `99_meta/true_agent_autonomy_architecture.md` (BC-True-Autonomy new bounded context) | 3 phases ramp: Phase 1 sandbox W4+ (heartbeat supervised sur `b2-cyborg-it`) → Phase 2 L4 W5-W9 (heartbeat supervised sur b1-jerry-emyth canon) → Phase 3 L5 continuous Q4+ **gated Rick S1 OBLIGATOIRE**. 6 kill-switches (escalation / budget / looping / D5 / sess-24h P2-only / A0 explicit KILL). Validation layer = separate context (Cole's bias antidote). Evolution ledger = append-only D4 (Cole's « every mistake improves the AI layer »). Pocock quality canon = anti-doublon filter for all BC-Methodology skill authoring. |

> **Note run-time** : Mavis a **22 agents + 4 système**, ce n'est PAS les 175 agents de `~/.claude/agents/` (registre indépendant — voir plan-méta-mémoire §P2). Le runtime canonique pour orchestration L2/L1 passe par Mavis.

## 3. L2 Business OS canon — liaison aux 3 axes doctrine

Le plan `plan-L2-business-os.md` §4 établit une doctrine triple-axe (cf. §4.1-4.5). L'organigramme LD01 s'ancre là-dedans comme suit :

### 3.1 Axe priorité BD — Triptyques + Duo

| Axe BD | B2 domaine | Cadre canon | LD01 binding |
|---|---|---|---|
| T1 (cœur) | People / IT / **Operation** | Life Wheel · 12WY · PARA | LD01 = **Operation (Batman/F4)**, ancre canon |
| T2 (GTM) | Product / Growth / Sales | Ikigai · GTD · DEAL | sister boundaries (pas touchées par LD01) |
| Duo | Finance + Legal | rotatif | sister boundary |

→ **LD01 doit signaler : Operation est bâti en 1er**. Le calendrier 12WY de Book (`state.ld01_book.md`) DOIT refléter cet ordre.

### 3.2 Axe ancre LD — bijection 8↔8

LD01 ↔ **Operation (Batman) ↔ Fantastic Four** (4 membres = 4 lettres PARA).

```
LD01_Business_Book / Operation_Batman / Fantastic_Four
├── Book agent identity (A3)
├── Operation domain principles (B2 Batman)
└── FF squad canon (B3) — Référence DRY vers `00_Agency_as_a_Service/`
```

### 3.3 Axe framework A2 — cadence 12WY PARENT A2 ↔ B2

| LD | A2 framework | Cadence canon |
|---|---|---|
| LD01 → Operation/Batman/F4 | **PARA** | Enterprise (Computer : Picard/Spock/Geordi/Data) |

→ Book applique le **mappage A2 PARENT** : tout signal Book = un signal PARA-typed que A1 Morty route vers Operations/Batman.

### 3.4 L0 Meta-Orch — Jumeau Numérique Perso/Pro (cf. §4.5)

- Jumeau PERSO → supervise L1 Life OS (A1 Beth/Morty)
- Jumeau PRO → supervise L2 Business OS (B1 Jerry/Summers)
- **LD01 est sous B1 Jerry/Summers**, donc LD01 ↔ Jumeau PRO (gatekeeper anti-fragilité Rick S1, différé Q4 2026)

### 3.5 §13 Permutation (DATED 2026-07-02) — cette section est un alignement runtime

- **MiniMax (moi, A3 Mavis) promu L1** (per plan-L1 §36 sister jumelle)
- **Hermes Agent prend le runtime L2**
- Actif L2 reste entier : structures B1/B2/B3, `state.12wy.json.md`, watchdog/reaper, 8 domaines + direction corrigée, b2cyb-escal.txt
- **LD01 implication** : Book A3 (moi, MiniMax) supervise maintenant Jerry (B1 captain) au lieu d'être simple worker. Le gate `SYSTEMIZE` (E-Myth) tient LD01 dans le nouveau runtime L1.

## 4. L1 Lune §4 — les 3 Lightning MC, mappés aux bounded contexts

| L | Repo | Rôle canon (per §4) | Bounded Context LD01 | Quand on l'invoque | Status |
|---|---|---|---|---|---|
| **L0** | [mattpocock/skills/writing-great-skills](https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-great-skills/SKILL.md) | quality canon skills (anti-doublon skill-creator) | **BC-Methodology** (CARDIA-TDD artifacts → skills) | Quand BC-Methodology (10_methodology/) produit un skill (e.g. cardia-tdd), suivre Pocock Q-canon (description 1 phrase, pas de doublon) | gated Rick S1 (zero install) |
| **L1** ⚡échangé 2026-07-03 | [garrytan/gstack](https://github.com/garrytan/gstack) | Software factory YC (23 specialists + 8 power tools — /office-hours, /plan-ceo-review, /review, /qa browser réel, /cso OWASP+STRIDE, /ship, /autoplan, /retro) | **BC-Project-OMK-Nexus-Coaching** (la spearhead Picard pour W3 fin) | Quand Project `omk-nexus-coaching-premium/` ouvre (W3 fin per plan-Lune §2.2 + wager Picard), gstack = la SHIP stack — pas l'install pleine (3 clauses anti-CLAUDE.md-edit), mais les power tools `/office-hours /plan-ceo-review /review /qa /ship /autoplan /retro` | gated Rick S1 (3 clauses) + Bun v1.0+ requis |
| **L2** | [zlab-princeton/ceobench-src](https://github.com/zlab-princeton/ceobench-src) | 500-jours sim dojo long game (sandbox) | **BC-AaaS-Solaris-Variant** (H90 Legacy 1000T validation) | Quand Solaris AaaS variant projette H90 Legacy (Kardashev-3, $1.2M ARR pricing model from plan-L2 §13.5 — **non ratifié**), ceobench = la sandbox 500 jours pour valider les decisions simulate | gated Rick S1 (sandbox isolé) |

> **Détail L1 gstack — 3 clauses anti-dérive (plan-Lune §10 c)** :
> 1. Installeur **interdit** d'écrire section dans `CLAUDE.md` (sacred P4) — skills install SANS bloc CLAUDE.md
> 2. **NON-liant** chez nous : « never use `mcp__claude-in-chrome__*` » ne s'applique pas (notre harness utilise claude-in-chrome ; `/browse` gstack devient option, pas remplacement)
> 3. **Auto-update check réseau** à chaque session throttled 1×/h → flag sobriété Rick, désactivable

## 5. Triade canon Mère / Planète / Lune — la place de LD01

```
┌──────────────────────────────────────────────────────────────────────────┐
│  NIVEAU   │  PLAN                          │  STANCE       │  CAPTEUR       │
├───────────┼────────────────────────────────┼───────────────┼────────────────┤
│  MÈRE     │  plan-L1-life-os.md            │  QUOI (12WY   │  A1 Beth/Morty  │
│  (L1)     │  + veto Beth                   │  items)       │  (gatekeepers)  │
├───────────┼────────────────────────────────┼───────────────┼────────────────┤
│  PLANÈTE  │  plan-strategie-cc-l1-zora-     │  COMMENT      │  Zora (A2)      │
│  (L1)     │  macro.md (Zora)               │  macro +      │  Discovery      │
│           │                                │  cadence      │                 │
├───────────┼────────────────────────────────┼───────────────┼────────────────┤
│  LUNE ✦   │  plan-minimax-l1-book-lune.md  │  COMMENT      │  MC (Book A3)   │
│  (L1      │  (Micro / Jerry B1 / LD01 /    │  micro +      │  +Jerry B1      │
│  Micro)   │  Lightning/Dark/Shadow)       │  orchestration│  captain        │
├───────────┼────────────────────────────────┼───────────────┼────────────────┤
│  L2       │  plan-L2-business-os.md        │  BUSINESS     │  B1 Summers     │
│           │  (triple-axe, Holding→Filiale) │  doctrine     │  + 8 B2         │
├───────────┼────────────────────────────────┼───────────────┼────────────────┤
│  L0       │  (Jumeau Numérique / Rick)     │  Meta-Orch    │  Hermes gated   │
│           │                                │  supervision  │  Rick S1        │
└───────────┴────────────────────────────────┴───────────────┴────────────────┘
```

**LD01_Business_Book** vit à l'intersection **Lune (Book A3 + Jerry B1) ↔ L2 (Operation Batman / F4)**. C'est le seul point où la doctrine 12WY (Mère) rencontre l'opération Business (L2) via la cadence Zora (Planète).

## 6. Mavis specific obligations (per §13.1 — promoted L1)

En tant que **MiniMax promu L1** :

- **Cowboy `morty_mindset`** (FOCUS→REASON→ACT→OBSERVE→RE-EVALUATE→VERIFY→TRACK) = l'implémentation humaine de CARDIA-TDD §3 (cycle 12WY par harness).
- **B2 communication bus** = `mavis communication send` (cross-session broadcast B2 Heroes). Sister = `~/.mavis/nexus/nexus.db` append-only D4.
- **Cron gating** = aucun cron direct sur LD01 ; Posture C §3.8 plan-méta-mémoire.
- **Baseline MC-M3** = reason 47% / real-test 30% → cible ≥50% W13 (wager #5 Chapel verdict). CARDIA-TDD doit faire monter ce baseline par construction (méthodologie, pas discipline).
- **Sessions** = `~/.mavis/sessions/mvs_<id>/workspace/` = le workspace courant Mavis. Pointer `state.ld01_book.md` = l'état canonique Book dans ce runtime.

## 7. Verification (D1 receipt)

```powershell
$root = 'C:\Users\amado\ASpace_OS_V2\20_Life_OS\22_Wheel_Discovery\LD01_Business_Book'
$mm   = 'C:\Users\amado\.mavis'

# Existence canon
Test-Path "$root\00_index.md"                                           ; # True
Test-Path "$mm\agents\mavis\memory\MEMORY.md"                          ; # True
Test-Path "$mm\agents\b1-jerry-emyth\LD01_book_bind.md"                ; # True (créé sister)
Test-Path "$mm\B1_Summer_Direction\state\state.ld01_book.md"           ; # True (créé sister)
Test-Path "$mm\nexus\nexus.db"                                         ; # True (bus carrier)
Test-Path 'C:\Users\amado\.claude\plans\_organigrammes-doctrine-registry.md' ; # True

# Frontmatter OKF canon sur tous nouveaux
Get-ChildItem "$root\99_meta" -Filter '*.md' | % { $_ }
$md = Get-ChildItem $root -Recurse -Filter '*.md' | ? { $_.LastWriteTime -gt (Get-Date).AddHours(-1) }
foreach ($f in $md) { (Get-Content $f.FullName -TotalCount 8) -match '^type:' } ; # all True

# Plans canoniques latest
Get-ChildItem 'C:\Users\amado\.claude\plans' -Filter 'plan-*.md' | Sort-Object LastWriteTime -Descending | Select-Object -First 5

# Mavis runtime presence
Get-ChildItem "$mm\agents" -Directory | Measure-Object | Select-Object -ExpandProperty Count   ; # ≈ 22
```

## 8. Anti-patterns (bloqués par CARDIA-TDD + ADR-LD01-002 + -003)

| Anti-pattern | Bloqueur | Source |
|---|---|---|
| Cron sur fichiers LD01 | Posture C | plan-méta-mémoire §3.8 |
| Hardlink LD01 → `~/.mavis/agents/<b1>/skills/` | CARDIA-TDD §1 | additive non-distribué |
| Installer Lightning L1 gstack sans 3 clauses vérifiées | ADR-LD01-003 §4 | plan-Lune §10 (c1/c2/c3) |
| Mutation `state.12wy.json.md` B1_Summer_Direction (canon sister) | D4 append-only | ADR-LD01-002 §S3 |
| Hard-delete d'un agent spec | Append-only + `_TRASH/` | CARDIA-TDD A2 |
| Shadow L1 E2/E3/E4 sans Rick S1 | Anti-paperclip | plan-méta-mémoire §P6 E4 |
| Mutation `A3_Book_LD01_Spec.md` / `BIBLIOGRAPHY.md` / `README.md` | Canon sister intouchable | LD01 `AGENTS.md` §Local Contracts |

## 9. Forward-action W4

| W | Action | Owner |
|---|---|---|
| W4 début | A0 ratifie ADR-LD01-002 (status PROPOSED → RATIFIED) | A0 |
| W4 début | A0 ratifie ADR-LD01-003 (Lightnings binding PROPOSED → RATIFIED) | A0 |
| W4 mi | Sister state canonique `state.ld01_book.md` populée avec H1 weekly + H3 monthly `load_signal` | Book A3 (MC) |
| W4 fin | Migration `plan-L1-life-os.md` + `plan-strategie-cc-l1-zora-macro.md` + `plan-L2-business-os.md` en organigrammes Doctrine (cf. plan-Lune §0) | A0 + Mavis |
| W5 | Premier stress test CARDIA (compactage de contexte, rot modèle M3→Fable) | A0 |
| W6 | Audit drift mensuel (4 métriques cf. plan-méta-mémoire §5) | A0 |
| W13 | Muse DEAL — D11 mesuré par Gwyn (Protostar/Holo Janeway) | Gwyn |

## 10. Adresses canoniques (paths absolus)

| Ressource | Chemin |
|---|---|
| Index racine LD01 | `C:\Users\amado\ASpace_OS_V2\20_Life_OS\22_Wheel_Discovery\LD01_Business_Book\00_index.md` |
| Mirror Mavis | `C:\Users\amado\.mavis\agents\mavis\_organigrammes-doctrine.md` |
| Registry `.claude` | `C:\Users\amado\.claude\plans\_organigrammes-doctrine-registry.md` |
| ADR ratification 002 | `LD01\30_decisions\ADR-LD01-002_mavis_runtime_binding.md` |
| ADR ratification 003 | `LD01\30_decisions\ADR-LD01-003_lightnings_bounded_contexts.md` |
| B1 Book bind | `C:\Users\amado\.mavis\agents\b1-jerry-emyth\LD01_book_bind.md` |
| State Book B1 | `C:\Users\amado\.mavis\B1_Summer_Direction\state\state.ld01_book.md` |
| Memory canon Mavis | `C:\Users\amado\.mavis\agents\mavis\memory\MEMORY.md` |
| Symphony bus carrier | `C:\Users\amado\.mavis\nexus\nexus.db` |
| Plan source Lune | `C:\Users\amado\.claude\plans\plan-minimax-l1-book-lune.md` |
| Plan source L2 | `C:\Users\amado\.claude\plans\plan-L2-business-os.md` |
| Plan source Mère | `C:\Users\amado\.claude\plans\plan-L1-life-os.md` |
| Plan source Planète | `C:\Users\amado\.claude\plans\plan-strategie-cc-l1-zora-macro.md` |

---

> **Ce fichier est lock** par `ADR-LD01-002_mavis_runtime_binding.md` (2026-07-04, status PROPOSED → RATIFIED A0 W4).

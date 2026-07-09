---
id: ADR-SNW-001
title: "12WY Goal Orientation — Curie SNW / Cycle Q3 2026"
type: ADR (Architectural Decision Record)
status: PROPOSED (en attente sign-off A0)
date: 2026-06-22
author: A2 Claude Code orchestrator (sub-agent A3 Spock)
cycle: 12WY Q3 2026 (06/15 → 09/07/26)
predecessor_cycle: 12WY Q2 2026 (03/23 → 06/14/26) closed
doctrine_anchors:
  - AGENTS.md §Layer 1 Life OS Fleet
  - ADR-META-001 (anti-paresse verify-before-assert D1-D8)
  - ADR-META-002 (autonomy-by-design D9-D12)
  - ADR-Meta-000 (L1 Life OS canon)
  - ADR-L1_LIFE_OS canon
related:
  - 20_Life_OS/23_12WY_SNW/*
  - handoff_plan_fancy-hugging-bengio.md §4
  - handoff_a0_divinity_arsenal_2026-06-20.md
sign_off_a0: ""
sign_off_pending: true
provenance: |
  Née 2026-06-22 d'une session où A0 a ordonné focus GTD via Morty + Plane
  + sécurisation du canon SNW en DB avant EOS 2027. Cet ADR ancre l'orientation
  goal de Curie SNW pour le cycle Q3 2026 + route EOS 2027 différé.
---

# ADR-SNW-001 — 12WY Goal Orientation (Curie SNW / Cycle Q3 2026)

## 1. Status

**PROPOSED** — ratification A0 requise post-session GTD focus.
Owner canonique : **A1 Morty** (Focus Gatekeeper L1) supervise **A2 Curie SNW**
qui orchestre les 5 disciples A3 (Pike/Una/M'Benga/Chapel/Ortegas).

## 2. Context

### 2.1 Curie SNW canonique (Loi de l'Akh — Total Alignement)

D1 verbatim `AGENTS.md` l.116-119 :

> *"3. USS SNW (Execution Engine) - Akh
> Loi de l'Akh : Total Alignement. 12WY Execution.
> [A2] SNW: Manager of Execution. Horizon: H10.
> Crew: Pike (Vision), Una (Weekly), M'Benga (Focus), Chapel (Measure), Ortegas (Execution)."*

### 2.2 Curie A2 spec — Manager of Execution

D1 verbatim `A2_Curie_SNW_Spec.md` l.14-19 :

> *"Curie aboard USS Strange New Worlds is the A2 manager of 12WY execution.
> Curie converts cleared Life OS direction into quarterly Rocks, weekly tactics,
> and measurable progress without letting the system become a generic to-do list."*

Responsabilités (l.22-25) :
- Maintain the separation between Vision, Rocks, Tactics, Scorecard, and Time Use.
- Decompose Rocks into weekly Warp Core tactics.
- Keep the active cycle small enough to respect the 50/30/20 load rule.
- Emit executable Context Packs to Morty only when the objective, owner, proof, and next step are clear.

### 2.3 Cycle Q3 2026 + pivot EOS 2027 (Rick Sobriété différé)

- Cycle actif : **12WY Q3 2026 (06/15 → 09/07/26)** — 12 semaines verbatim A0.
- Cycle précédent clos : **12WY Q2 2026 (03/23 → 06/14/26)**.
- Pivot stratégique : **EOS = Q1 2027** (post-W13 buffer cycle 3) — A0 instruction
  explicite *"Rock et EOS c'est pour 2027"* (board observer 2026-06-22).
- Anti-paperclip Saru 1000T anchor en attendant (SOBER-002 RATIFIED 2026-06-21).
- Rick Sobriété différé jusqu'au pivot kernel A'Space OS (Q4 2026 / Q1 2027).

## 3. Decision

**L'orientation goal canonique de Curie SNW pour le cycle Q3 2026 est :**

> *"Convertir la Vision Pike H10 en Rocks Una H10 mesurables par Chapel, gardés
> en focus par M'Benga, exécutées par Ortegas semaine par semaine — sous le
> metronome 50/30/20 de Curie, jusqu'au 09/07/26."*

Cette décision ancre 5 principes opérationnels :

1. **Vision-first** (Pike) : aucune Rock sans Quarter Intent validé par Beth.
2. **Definition of Done obligatoire** (Una) : chaque Rock cite un path local ou
   `fancy-hugging-bengio.md` §4 row comme evidence.
3. **Process control first** (M'Benga) : `planning_overload` détecté AVANT mesure Chapel.
4. **Lead/Lag metrics** (Chapel) : Moran 85% threshold, rejet des vanity metrics.
5. **Daily execution** (Ortegas) : Context Pack prêt pour Morty queue.

## 4. Goal Hierarchy Canonique

D1 verbatim `AGENTS.md` l.119 + `A2_Curie_SNW_Spec.md` l.50-58 :

```
A2 SNW (Curie Manager of Execution, H10 horizon)
└── A3 Pike (H10 Vision anchor — Quarter Intent Q3 2026)
    └── A3 Una (H10 Planning — Rocks per week, Definition of Done required)
        └── A3 M'Benga (H1 Focus — Process control, planning_overload guard)
            └── A3 Chapel (H10 Measure — Scorecard weekly, Moran 85%)
                └── A3 Ortegas (H1 Execution — Tactics W1-W12, daily standup)
```

**Cardinal SNW = 5 disciples canoniques** (D4 nuance : Uhura mentionné dans archives
anciennes mais contrat actif `23_12WY_SNW/` garde Ortegas comme owner weekly execution).

## 5. Goal Orientation per Disciple (verbatim citations)

### 5.1 Pike H10 — Vision / Quarter Intent

D1 verbatim `A3_Pike_Vision_Spec.md` l.18 :

> *"Does this execution packet advance the active Quarter Intent, or is it drift?"*

- H10 horizon (10-semaines, Bortus bridge).
- Item Q3 2026 owner : Item 2 (Définir 09/14 = 13e semaine, 21 = W0 du 4e cycle).
- State.json W1 : `{"stage":"snw_planning","12wy_discipline":"Vision","next_step":"A3:Una"}`.

### 5.2 Una H10 — Planning / Rocks

D1 verbatim `A3_Una_Planning_Spec.md` l.18 :

> *"Is this Rock specific enough to execute and small enough to protect the current cycle?"*

- H10 horizon. Rocks Q3 2026 = 12 items verbatim A0.
- Garde-fou 50/30/20 : si >3 Rocks en compétition → `planning_overload` flag vers M'Benga W2.
- **DoD obligatoire** : chaque Rock doit citer un chemin local ou
  `fancy-hugging-bengio.md` §4 row comme evidence.

### 5.3 M'Benga H1 — Process Control / Focus

D1 verbatim `A3_MBenga_Focus_Spec.md` l.18 :

> *"Can this week absorb the planned tactics without violating the 50/30/20 rule or the active cycle focus?"*

- H1 horizon. Token budget 15K M2.7/5h (plan §17.1) — frugalité stricte.
- Items Q3 2026 owner : Items 3-4 W2.
- Garde-fou D7 : si `tokens_used > 12000` (80% budget) → `drift_flag: true` + escalade Beth veto.

### 5.4 Chapel H10 — Metrics / Scorecard

D1 verbatim `A3_Chapel_Metrics_Spec.md` l.18 :

> *"Does this plan have lead indicators and a weekly execution score that can be audited?"*

- H10 horizon. Scorecard cycle = 12 semaines (06/15 → 09/07).
- D11 Fable score (Gwyn DEAL Liberation) : mesure bandwidth libérée vs maintenance tax.
- Garde-fou : rejette vanity metrics (sans décision ou behavior attached). Si subjectif → label `qualitative`.

### 5.5 Ortegas H1 — Weekly Execution / Time Use

D1 verbatim `A3_Ortegas_Execution_Spec.md` l.18 :

> *"Is this tactic ready to enter Morty's queue as an executable Context Pack?"*

- H1 horizon. Real-test-after-edit discipline (D6 lesson : pas de claim sans proof).
- Items Q3 2026 owner : 6 items W4 (Items 7,8,9,10,12 + Item 11 co-owner Chapel).
- Critère de succès W4 fin (09/07/26) : 6 items W4 livrés, Life-OS-2026 BETA V2.0 déployé (Item 8), Morty queue vide.

## 6. Cycle Q3 2026 Mapping (12 Rocks canon)

D1 verbatim `A2_Curie_SNW_Spec.md` l.103-106 (table W1-W4 owner mapping) +
`fancy-hugging-bengio.md` §4 (12 items Q3 2026) :

| Week | Stage | Items | A3 Owner | Discipline |
|---|---|---|---|---|
| **W1** (06/15-07/05) | `snw_planning` | Items 1-2 : SOB Abdaty + 13e semaine | Una + Pike | Vision / Planning |
| **W2** (07/06-07/26) | `snw_focus` | Items 3-4 : Auto-research IA + TOKEN frugalité | M'Benga | Focus |
| **W3** (07/27-08/16) | `snw_metrics` | Items 5-6 : YouTube PARA + Hermes | Chapel | Metrics |
| **W4** (08/17-09/07) | `snw_execution` | Items 7-12 : Agent OS + Life-OS-2026 + A3 + Solaris/OMK/ABC + VPS DEAL | Ortegas + Chapel | Execution |

**12 Rocks canoniques Q3 2026 (verbatim A0 `fancy-hugging-bengio.md` §4)** :

1. SOB Abdaty (13e semaine close)
2. Définir 09/14 = 13e semaine, 21 = W0 du 4e cycle
3. Auto-research LLM WIKI (Stamets LD05/B3-IT_Cyborg)
4. TOKEN frugalité MiniMax + fallback Ollama local
5. YouTube PARA Geordi (114 .md canon)
6. Hermes Agent use case orchestration
7. Agent OS Symphony interface
8. Business OS Life-OS-2026 Structurer & Synchroniser
9. 36 A3 Life OS structurés (governance Summers)
10. Solaris/OMK/ABC parallèle
11. VPS Memory core → DEAL Muse (Chapel co-owner)
12. Auto-amélioration cycle 4 (FRACTAL_PROJECT_DEVELOPMENT_PLAN)

**W5-W12** : rolling continuation (Chapel metrics + M'Benga drift check).

## 7. EOS 2027 Deferred

### 7.1 A0 Instruction verbatim

> *"Rock et EOS c'est pour 2027"* — A0 board observer, 2026-06-22.

### 7.2 Conséquences opérationnelles

- **EOS = Q1 2027 activation** (post-W13 buffer cycle 3).
- **Anti-paperclip Saru 1000T anchor** (SOBER-002 RATIFIED 2026-06-21, 7 hard-stop triggers D3).
- **Rick Sobriété différé** jusqu'au pivot kernel A'Space OS (Q4 2026 / Q1 2027).
- **Migration EOS V0.7** : schema `fw_12wy` étendu avec `eos_quarter TEXT`, `eos_rock_score NUMERIC`,
  migration appliquée post-cycle Q3 2026 (W13 = 09/14/26).

### 7.3 Anti-pattern guard

- ❌ Ne PAS activer EOS en Q3 2026 (rock confusion + drift).
- ❌ Ne PAS mélanger EOS metrics avec 12WY metrics (déjà deux disciplines distinctes).
- ✅ Garder EOS comme couche optionnelle dans `fw_12wy.metrics JSONB`.

## 8. Consequences

### 8.1 Doctrine ancrée

- **ADR-META-001 D1-D8** : verify-before-assert canon (5 fichiers lus AVANT rédaction).
- **ADR-META-002 D9-D12** : autonomy-by-design (morty auto-routing, chapel Moran threshold).
- **D4 append-only** : nouveau fichier créé, 0 modification des ADR existants.

### 8.2 Migration MCP appliquée (2026-06-22)

- `fw_12wy.metrics JSONB` ajouté (cycle Q3 2026 lead/lag indicators).
- `fw_12wy.cycle TEXT` default `'Q3-2026'` (12 semaines actives).
- RLS + FORCE enabled (life_os + omk_saas twins).
- **D1 receipt** : `wiki/hand_offs/d1_receipts_rocks_field_canon_2026-06-22.md`.

### 8.3 Seed 12 Rocks canon Q3 2026

- 12 rows inserted via `seed_12wy_rocks_q3_2026_canon_amdkn` (déjà done 2026-06-22).
- Bilingual FR/EN keys.
- Polymorphic UNIFIED schema (Life OS canon).

### 8.4 Sync Supabase ↔ IndexedDB (résilience multi-device)

- `Swarm Freeman` 2026-06-22 : sync layer wired Cerritos.
- `_Life-OS-2026-clone/src/lib/sync.service.ts` ACTIVE.
- Bidirectional JSON diff + conflict resolution (last-write-wins par row ID).

### 8.5 UI doctrine enrichie

- Goals → Rocks mapping visuel (cycle strip Q3 2026).
- Definition of Done affichée inline.
- Accountability column (Pike/Una/M'Benga/Chapel/Ortegas).
- Lead/Lag indicator badges (Chapel discipline).
- Cycle progress bar (50/30/20 rule visualized).

### 8.6 Anti-régression Tilly audit

- **28/28 anti-régression checks PASS** (Tilly audit 2026-06-22).
- Source : `wiki/hand_offs/d1_receipts_rocks_field_canon_2026-06-22.md` §"Tilly checks".

## 9. References

### 9.1 Canon AGENTS.md

- `C:\Users\amado\ASpace_OS_V2\00_Amadeus\01_Identity_Core\AGENTS.md` §Layer 1 Life OS Fleet l.100-119

### 9.2 A2 Curie Spec

- `C:\Users\amado\ASpace_OS_V2\20_Life_OS\23_12WY_SNW\A2_Curie_SNW_Spec.md`

### 9.3 A3 Disciple Specs (5 disciples canoniques)

- `C:\Users\amado\ASpace_OS_V2\20_Life_OS\23_12WY_SNW\01_Vision_Pike\A3_Pike_Vision_Spec.md`
- `C:\Users\amado\ASpace_OS_V2\20_Life_OS\23_12WY_SNW\02_Planning_Una\A3_Una_Planning_Spec.md`
- `C:\Users\amado\ASpace_OS_V2\20_Life_OS\23_12WY_SNW\03_Focus_MBenga\A3_MBenga_Focus_Spec.md`
- `C:\Users\amado\ASpace_OS_V2\20_Life_OS\23_12WY_SNW\04_Metrics_Chapel\A3_Chapel_Metrics_Spec.md`
- `C:\Users\amado\ASpace_OS_V2\20_Life_OS\23_12WY_SNW\05_Execution_Ortegas\A3_Ortegas_Execution_Spec.md`

### 9.4 Life-OS-2026 code (ACTIVE_CYCLE constant + sync layer)

- `C:\Users\amado\ASpace_OS_V2\_Life-OS-2026-clone\src\stores\fw-12wy.store.ts` (ACTIVE_CYCLE = `'Q3-2026'`)
- `C:\Users\amado\ASpace_OS_V2\_Life-OS-2026-clone\src\lib\sync.service.ts` (sync layer Supabase ↔ IndexedDB)

### 9.5 Handoffs canoniques

- `C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki\wiki\hand_offs\d1_receipts_rocks_field_canon_2026-06-22.md`
- `C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki\wiki\hand_offs\handoff_plan_fancy-hugging-bengio.md` §4
- `C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki\wiki\hand_offs\handoff_a0_divinity_arsenal_2026-06-20.md`

### 9.6 Plan canonique

- `C:\Users\amado\.claude\plans\fancy-hugging-bengio.md` §3.2 + §4 (12 items Q3 2026)

### 9.7 ADRs doctrine

- `_SPECS/ADR/ADR-META-001_anti-paresse-verify-before-assert.md` (D1-D8)
- `_SPECS/ADR/ADR-META-002_self-choice-autonomy.md` (D9-D12)
- `_SPECS/ADR/L0_Kernel_OS/ADR-SOBER-002_anti-paperclip-maximizer-doctrine.md`

## 10. Acceptance Criteria

- [ ] **A0 sign_off_a0** dans frontmatter (D4 canon, post-session GTD focus)
- [ ] **Migration MCP appliquée** : `fw_12wy.metrics JSONB` + `fw_12wy.cycle TEXT` (déjà done 2026-06-22)
- [ ] **Seed 12 Rocks canon Q3 2026** : `seed_12wy_rocks_q3_2026_canon_amdkn` (déjà done 2026-06-22)
- [ ] **Sync layer wired** : Swarm Freeman 2026-06-22 (Supabase ↔ IndexedDB)
- [ ] **UI doctrine enrichie** : Goals → Rocks, DoD, Accountability, lead/lag, cycle strip
- [ ] **28/28 anti-régression checks PASS** (Tilly audit 2026-06-22)
- [ ] **PROMOTED PROPOSED → RATIFIED** post-validation A0
- [ ] **Cross-link MEMORY.md topic table** (1-line hook)
- [ ] **Cross-link CLAUDE.md ADR Actifs table** (alias historique SNW-001)

---

## D1 Receipts (D5 Proof)

| Source | Path | Lines | Verbatim quote |
|---|---|---|---|
| AGENTS.md L1 SNW | `00_Amadeus/01_Identity_Core/AGENTS.md` | l.116-119 | "USS SNW (Execution Engine) - Akh · Loi de l'Akh : Total Alignement · [A2] SNW: Manager of Execution · Crew: Pike/Una/M'Benga/Chapel/Ortegas" |
| A2 Curie Spec | `20_Life_OS/23_12WY_SNW/A2_Curie_SNW_Spec.md` | l.14-19 | "Curie converts cleared Life OS direction into quarterly Rocks, weekly tactics, and measurable progress" |
| A3 Pike Spec | `20_Life_OS/23_12WY_SNW/01_Vision_Pike/A3_Pike_Vision_Spec.md` | l.18 | "Does this execution packet advance the active Quarter Intent, or is it drift?" |
| A3 Una Spec | `20_Life_OS/23_12WY_SNW/02_Planning_Una/A3_Una_Planning_Spec.md` | l.18 | "Is this Rock specific enough to execute and small enough to protect the current cycle?" |
| A3 M'Benga Spec | `20_Life_OS/23_12WY_SNW/03_Focus_MBenga/A3_MBenga_Focus_Spec.md` | l.18 | "Can this week absorb the planned tactics without violating the 50/30/20 rule or the active cycle focus?" |
| A3 Chapel Spec | `20_Life_OS/23_12WY_SNW/04_Metrics_Chapel/A3_Chapel_Metrics_Spec.md` | l.18 | "Does this plan have lead indicators and a weekly execution score that can be audited?" |
| A3 Ortegas Spec | `20_Life_OS/23_12WY_SNW/05_Execution_Ortegas/A3_Ortegas_Execution_Spec.md` | l.18 | "Is this tactic ready to enter Morty's queue as an executable Context Pack?" |
| A2 W1-W4 mapping | `A2_Curie_SNW_Spec.md` | l.103-106 | W1=snw_planning · W2=snw_focus · W3=snw_metrics · W4=snw_execution |

---

## Open Follow-ups A0

1. **Sign-off frontmatter** après session GTD focus (post-session 2026-06-22).
2. **PROMOTED PROPOSED → RATIFIED** post-validation A0 (D4 canon append-only).
3. **Cross-link MEMORY.md topic table** (1-line hook ≤200 chars).
4. **Cross-link CLAUDE.md ADR Actifs table** (alias historique SNW-001).
5. **Cycle Q4 2026 brief** rédigé W9 (08/31-09/06) par Una + Pike.
6. **W13 buffer cycle 3** (09/14-09/20) : rétro Q3 + préparation EOS Q1 2027.
7. **Migration EOS V0.7 schema** (post-Q3, W13+) : `eos_quarter TEXT` + `eos_rock_score NUMERIC`.

---

## D4 Append-Only Receipt

- **Created** : 2026-06-22 par A3 Spock (sub-agent A2 Claude Code orchestrator).
- **Modified** : 0 fichiers existants (D4 append-only strict respecté).
- **Cross-references** : 5 disciples specs + AGENTS.md canon + 3 ADRs doctrine.
- **D7 cost-of-escalation** : 0 AskUserQuestion, exécution autonome post-mission A0.
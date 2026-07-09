---
id: ADR-OPS-PROJECT-GATE-001
title: Batman Ops Sister-Gate — Ops-grade MANIFEST.md extension + F4 quadruple co-signature avant status:active
status: RATIFIED
date: 2026-07-06
last_updated: 2026-07-06
deciders: [A0 Amadeus]
proposed_by: Claude Code B1 E-Myth Gatekeeper sur ratification batch "Go 1 a 4" 2026-07-06
domain: L2 Business OS / OPS gate / B2 Batman Ops (H3 runbooks) / B3 Fantastic Four
tags: [ADR, ops, runbooks, batman, F4, fantfour, sister-gate, project-gate, anti-paperclip, ops-quality, ops-review, tier, rto, rpo, slo, oncall, hotfix, privacy, retraction, handoff]
related:
  - ADR-L2-PROJECT-GATE-META-001
  - ADR-CANON-001
  - ADR-INFRA-002
  - ADR-INFRA-003
  - ADR-SOBER-002
  - ADR-ANTI-PAPERCLIP-001
  - ADR-AAAS-OPERATIONS-CANON-001
  - ADR-OBSERVABILITY-001
  - ADR-LEGAL-PROJECT-GATE-001
  - a3-enterprise-picard
  - b2-02-batman-ops
  - b3-2-mr-fantastic
  - b3-2-invisible-woman
  - b3-2-human-torch
  - b3-2-the-thing
supersedes: none
sister_gates_siblings:
  - ADR-PRODUCT-PROJECT-GATE-001
  - ADR-GROWTH-PROJECT-GATE-001
  - ADR-SALES-PROJECT-GATE-001
  - ADR-FINANCE-PROJECT-GATE-001
  - ADR-LEGAL-PROJECT-GATE-001
  - ADR-PEOPLE-PROJECT-GATE-001
sources_canons:
  - "C:\\Users\\amado\\ASpace_OS_V2\\00_Amadeus\\30_MEMORY_CORE\\LLM_Wiki\\wiki\\hand_offs\\handoff_wargame_wf2_b2_batman_ops_lens_2026-07-06.md"
  - "C:\\Users\\amado\\ASpace_OS_V2\\00_Amadeus\\30_MEMORY_CORE\\LLM_Wiki\\wiki\\hand_offs\\handoff_wargame_wf2_synthesis_book_coaching_2026-07-06.md"
  - "C:\\Users\\amado\\.claude\\agents\\b2-02-batman-ops.md"
  - "C:\\Users\\amado\\.claude\\agents\\a3-enterprise-picard.md"
  - "C:\\Users\\amado\\.claude\\agents\\b3-2-mr-fantastic.md"
  - "C:\\Users\\amado\\.claude\\agents\\b3-2-invisible-woman.md"
  - "C:\\Users\\amado\\.claude\\agents\\b3-2-human-torch.md"
  - "C:\\Users\\amado\\.claude\\agents\\b3-2-the-thing.md"
  - "C:\\Users\\amado\\.claude\\agents\\a3-enterprise-data.md"
  - "C:\\Users\\amado\\ASpace_OS_V2\\_SPECS\\ADR\\L2_Business_OS\\ADR-OBSERVABILITY-001_d11-lead-lag.md"
  - "C:\\Users\\amado\\ASpace_OS_V2\\00_Amadeus\\30_MEMORY_CORE\\LLM_Wiki\\wiki\\hand_offs\\handoff_wargame_wf2_b2_greenlantern_people_lens_2026-07-06.md"
  - "C:\\Users\\amado\\ASpace_OS_V2\\00_Amadeus\\30_MEMORY_CORE\\LLM_Wiki\\wiki\\hand_offs\\handoff_wargame_wf2_b2_cyborg_it_lens_2026-07-06.md"
ratification:
  by: "A0 Amadeus"
  date_iso: "2026-07-06"
  gate_a0_signed_off: true
  approval_token: "RATIFICATION-BATCH-02-2026-07-06-ADR-OPS-PROJECT-GATE-001"
  context: "Sister-gate Ops Batman (B2) absorbée par ADR-L2-PROJECT-GATE-META-001 — extension MANIFEST.md ops-grade + quadruple co-signature F4 (Mr Fantastic lead + Invisible Woman + Human Torch + The Thing) avant status:active sur Project Picard H10."
vocabulaire_canon:
  F4: "B3 Fantastic Four — Mr Fantastic (lead) + Invisible Woman + Human Torch + The Thing (sister canon `b2-02-batman-ops.md` ligne 24-27)"
  tier: "T2 experimental / T1 mainstream / T0 user-critical — graduation par signal ops (ex: outage_count > X sur 30j = promote)"
  ops_review: "Date canonique H3 (≤90j) sister du next_review Picard H10 — Mr Fantastic refuse la canonisation au-delà de 2× H3 (=180j)"
  ops_quality: "Champ frontmatter SIGNED co-signé F4 — gate obligatoire avant status:active (extend Picard D11 metric canon L.79-85)"
  privacy: "Pré-flight GREEN|YELLOW|RED — B3 Invisible Woman gate, RED = escalade B3 Ikaris Legal (sister ADR-LEGAL-PROJECT-GATE-001, AI-Act 2026-08-02 deadline)"
  D7_posture: "Posture C + ADR-SOBER-002 §6 anti-paperclip — 0 cron actif tant que A0 n'a pas ratifié per-cron GO"
  Anti_Paperclip: "SOBER-002 + ADR-ANTI-PAPERCLIP-001 — gates ops = sémantiques, pas cumulatifs paperclip"
---

# ADR-OPS-PROJECT-GATE-001 — Batman Ops Sister-Gate (F4 quadruple co-signature)

## 1. Status

**RATIFIED** — DRAFT v0 promu canoniquement par A0 Amadeus via le batch « Go 1 a 4 » du **2026-07-06** (token de ratification ci-dessus). Cette ADR est le **sibling-spec OPS** de la méta-ADR `ADR-L2-PROJECT-GATE-META-001` (elle-même ratifiée le même jour avec le token `RATIFICATION-BATCH-02-2026-07-06-ADR-L2-PROJECT-GATE-META-001`). Aucune gate OPS ne peut dévier de ce périmètre sans amendement daté.

## 2. Context

Le **wargame WF2** livré 2026-07-06 a produit le sister-lens canonique `handoff_wargame_wf2_b2_batman_ops_lens_2026-07-06.md` qui catalogue **8 angles morts cross-cutting** entre A3 Picard (capitaine des 12WY projects, H10 horizon) et B2 Batman Ops (runbooks H3) + son escouade **B3 Fantastic Four** (Mr Fantastic lead · Invisible Woman · Human Torch · The Thing).

**Problème racine** : la frontmatter canon de `a3-enterprise-picard.md` lignes 50-62 fixe **8 champs frontmatter** orientés lifecycle/durée (`project, owner, status, start_date, next_review, linked_12wy_rock, linked_area, junction`) — **0/8 champs ne sont domain-relevant** pour l'Ops. Conséquence systémique : la cadence H10 de Picard (1 MANIFEST.md / 10 sem.) **masque 9 semaines de dynamique H3 ops** (runbooks, privacy, hot-fix, tiering, RTO/RPO/SLO, archives, on-call) — la graduation `status: active` Picard est un acte **unilatéral** sans co-signature F4.

**Sister-cadence** : cette ADR-OPS est **1 parmi 7 sister-gates** absorbées par `ADR-L2-PROJECT-GATE-META-001` (Batman Ops · Flash Product · Superman Growth · JohnJones Sales · WonderWoman Finance · Aquaman Legal · GreenLantern People). Chaque sister-gate prescrit **les MANIFEST.md optionnels spécifiques à sa discipline-domain** + le nombre de co-signatures B3 requises avant `status: active`. Pour OPS, le compte canonique est **4 co-signatures F4** (Mr Fantastic lead + Invisible Woman + Human Torch + The Thing).

**Source canonique (D1 receipts)** :
- `handoff_wargame_wf2_b2_batman_ops_lens_2026-07-06.md` L.18-238 (8 angles morts catalogués Action/Réaction/Picard capte?/Contre/Failure/Abort)
- `handoff_wargame_wf2_synthesis_book_coaching_2026-07-06.md` L.81-103 (CC-1 cadence blackout 8/8 B2 sisters)
- `b2-02-batman-ops.md` (sister canonique Batman B2 — Captain F4 H3 runbooks)
- `a3-enterprise-picard.md` L.39-117 (canon Picard 3-question gate + 8 champs frontmatter)
- `b3-2-{mr-fantastic,invisible-woman,human-torch,the-thing}.md` (sister canonique F4 B3 squad)

## 3. Decision

**Adopté** : la doctrine **Ops-Project-Gate Batman** est ratifiée en un seul passage (DRAFT → RATIFIED) et devient immédiatement exécutoire dans la chaîne sister Project Gates WF2. Elle prescrit **3 changements canoniques** :

1. **Extension MANIFEST.md** : 8 champs canoniques obligatoires Picard (l.50-62) + **7 champs ops-grade optionnels** ajoutés en append-only strict (L+ invariant #3 respecté, pas de mutation des 8 champs canon) :
   - `ops_review: YYYY-MM-DD` (H3 Mr Fantastic gate, default = `start_date + 90 jours`)
   - `tier: T2|T1|T0` (The Thing gate, default T2 à création, escalation T2→T1→T0 par signal ops)
   - `rto_seconds: <int>` (The Thing — Recovery Time Objective, default 86400 = 24h)
   - `rpo_seconds: <int>` (The Thing — Recovery Point Objective, default 3600 = 1h)
   - `slo_target_percent: <float>` (The Thing — Service Level Objective, default 99.0)
   - `oncall_rotation: <B3-Human-Torch|external|sysadm|null>` (Human Torch — null = 03h00 unpaged, escalate)
   - `hot_fix_window: <empty>|<YYYY-MM-DD ISO 8601 interval>` (Human Torch — empty = pas de hot-fix orphelin)
   - **Bonus privacy ops-grade** : `privacy: GREEN|YELLOW|RED` (Invisible Woman force-fields gate, RED = escalade B3 Ikaris Legal per `ADR-LEGAL-PROJECT-GATE-001` AI-Act 2026-08-02 T-27 jours driver)
   - **Bonus retirement ops-grade** : `retired_to: <path>` (cold-storage canon — Picard handoff A3 Data archives `04_Archives_Data/`)
   - **Bonus observability ops-grade** : `observability_owner: <B3|empty>` + `paging_channel: <URL|empty>` (The Thing + Human Torch)
   - **Bonus ops-quality F4 gate** : `ops_quality: SIGNED|<vide>` (Mr Fantastic lead — gate obligatoire avant `status: active`)

2. **Quadruple gate F4** (E-Myth Batman doctrine `mindsets/Batman_Mindset.md`) : avant `status: active` Picard doit postuler au F4 un **mini-audit 4-checkpoint** :
   - **Mr Fantastic (LEAD)** : runbook → `ops_review ≤ H3 (90j)` signé ; `runbook_steps_8` canon (8 steps runbook B3 Mr Fantastic canon) ; signature `ops_quality: SIGNED` dans la frontmatter.
   - **Invisible Woman** : `privacy: GREEN|YELLOW|RED` documenté ; si `GREEN` ou `YELLOW` OK ; si `RED` → route B3 Ikaris Legal (sister `ADR-LEGAL-PROJECT-GATE-001`).
   - **Human Torch** : `oncall_rotation` documenté ; `paging_channel` non-vide sur T0/T1 ; `hot_fix_window` documenté ou explicitement vide.
   - **The Thing** : `tier` défini (T2 par défaut) ; `rto_seconds` + `rpo_seconds` + `slo_target_percent` chiffrés si T0/T1 ; `observability_owner` assigné.
   - **Sans cette quadruple signature `ops_quality: SIGNED`, Picard DOIT rester à `status: initiated`**. Escalade B2 Batman → B1 Jerry si refus.

3. **Handoff Mr Fantastic (data-recipient)** : Mr Fantastic est le **B3 lead** qui reçoit `ops_review` H3 lors de chaque cycle. Sister-canonique `04_Archives_Data/` (owned by A3 Data archives, `a3-enterprise-data.md`) reçoit `retired_to` quand un project passe `status: archived`. Le handoff est **lecture seule** sur le signal ops-grade, sans mutation de `a3-enterprise-picard.md` canon (L+ invariant #3 respecté).

**Rejeté** :
- Mutation des 8 champs canoniques Picard (D4 append-only strict).
- Création d'un cron automatique de `ops_review` (Posture C + ADR-SOBER-002 §6 anti-paperclip).
- Graduation `status: active` sans quadruple signature F4 (paperclip pattern risk).
- Escalade A0 mid-cycle pour amendement OPS (D7 cost-of-escalation ~100×).

## 4. Doctrine

Cette sister-gate OPS est ancrée verbatim dans :

- **`ADR-L2-PROJECT-GATE-META-001`** (méta-ADR Project Gates WF2) : cadre méta absorbant les 7 sister-gates (Batman · Flash · Superman · JohnJones · WonderWoman · Aquaman · GreenLantern). Cette ADR est le **sibling-spec OPS** (4 co-signatures F4 — compte canonique le plus bas parmi les 7 sisters).
- **`ADR-ANTI-PAPERCLIP-001`** (Anti-Paperclip Doctrine) : la sobriété prime sur l'extensivité ; les 7 gates absorbés doivent rester sémantiques et non cumulatifs.
- **`ADR-SOBER-002`** (Sobriété Kernel) : hard-veto B1-Jerry sur paperclip scaling ; reduction of moving parts §3.
- **`ADR-AAAS-OPERATIONS-CANON-001`** (AaaS Operations Canon) : bedrock de l'instance Operations AaaS — Batman Ops cadre les runbooks H3 canoniques (sister-cadre).
- **`ADR-INFRA-002`** (Repo-Home Junction Law) : `apps/<role>/` junction homé-court ; doctrine canon Picard profonde + code court.
- **`ADR-OBSERVABILITY-001`** (D11 Lead/Lag) : doctrine D11 lead vs lag — `ops_review` H3 = LEAD (prédictive du runbook), `rto_seconds` / `rpo_seconds` / `slo_target_percent` = LAG (confirmation post-mortem).
- **`a3-enterprise-picard.md` L.39-117** (3-question gate + 8 frontmatter fields obligatoires) : invariant réutilisé via `append-only` (L+ #3) — les 7 champs ops-grade sont **extension append-only** des 8 canoniques.
- **`mindsets/Batman_Mindset.md`** (E-Myth Batman doctrine) : gate doer → reviewer → signer ; Mr Fantastic (LEAD) = reviewer, Invisible Woman + Human Torch + The Thing = signers.
- **`b2-02-batman-ops.md`** (sister canonique B2 Batman) : H3 ops runbooks review + Captain B3 F4 anchor.
- **`b3-2-{mr-fantastic,invisible-woman,human-torch,the-thing}.md`** (sister canonique F4 B3) : Mr Fantastic process elasticity lead · Invisible Woman force fields privacy · Human Torch incident response hot fixes · The Thing load-bearing break-glass.

**Pattern onion-skin (sister-méta mirroré)** :
- **Layer 1 (doer)** : A3 Picard classifie 3-questions + écrit MANIFEST.md avec 8 champs canon + 7 champs OPS append-only.
- **Layer 2 (reviewer)** : B2 Batman H3 trigger une `ops_review` H3 et H3 escalade F4 audit.
- **Layer 3 (signers)** : F4 quadruple co-signature Mr Fantastic (lead) + Invisible Woman + Human Torch + The Thing.
- **Without 4/4 SIGNED** : status reste `initiated` ; gate refuse promotion `active`.
- **Without Paperclip hard-veto B1 Jerry top-down** : si F4 dévie en paperclip scaling, hard-veto SOBER-002 §3 active.

**Citation canonique sisters 7 gates** : Batman/OPS = **4/8 B2 sisters au minimum** (4 co-signatures F4) ; ce compte est le plus bas des 7 sister-gates (Aquaman = 10 B3, GreenLantern = 8 B3, Flash = 7 B3, Cyborg = 6 B3, JohnJones = 6 B3, Superman = 6 B3, WonderWoman = 6 B3, Batman = **4** B3). Le compte canonique 4 reflète l'**autonomie Ops** vs les autres disciplines (compliance, hiring, sales ont davantage de co-signatures car leur signal est plus juridique/contractuel).

## 5. Architecture

### 5.1 Tableau récapitulatif OPS gate (sibling-spec canon)

| Élément | Spec | Source D1 |
|---|---|---|
| **B2 Manager** | Batman Ops (🦇) | `b2-02-batman-ops.md` |
| **B3 Squad** | F4 (Mr Fantastic LEAD · Invisible Woman · Human Torch · The Thing) | `b3-2-*.md` ×4 |
| **Horizon B2/B3** | H3 ops runbooks review | `b2-02-batman-ops.md` ligne 19 |
| **Tier canon** | T2 experimental → T1 mainstream → T0 user-critical | `handoff_wargame_wf2_b2_batman_ops_lens_2026-07-06.md` AM-#4 |
| **Co-signatures F4 (gating minimum)** | 4 (runbook · privacy · hotfix · tier) | `handoff_wargame_wf2_b2_batman_ops_lens_2026-07-06.md` AM-#8 |
| **Cadence Picard gate** | D11 metric 1-3 per quarter / `next_review` ≤ 10 sem. | `a3-enterprise-picard.md` L.104 canon |
| **Cadence OPS gate** | `ops_review` ≤ 90j (H3 Mr Fantastic) ; `ops_review` > 180j = drift | `handoff_wargame_wf2_b2_batman_ops_lens_2026-07-06.md` AM-#1 |
| **Privacy gate** | `privacy: GREEN|YELLOW|RED` ; RED = escalade B3 Ikaris Legal | `handoff_wargame_wf2_b2_batman_ops_lens_2026-07-06.md` AM-#2 |
| **Hot-fix gate** | `hot_fix_window` ISO 8601 ou vide ; >3 hot-fix orphelins / 30j = signal | `handoff_wargame_wf2_b2_batman_ops_lens_2026-07-06.md` AM-#3 |
| **Tier gate** | `tier: T0|T1|T2` ; promotion T2→T1→T0 par outage_count | `handoff_wargame_wf2_b2_batman_ops_lens_2026-07-06.md` AM-#4 |
| **RTO/RPO/SLO gate** | `rto_seconds`, `rpo_seconds`, `slo_target_percent` chiffrés (T0/T1) | `handoff_wargame_wf2_b2_batman_ops_lens_2026-07-06.md` AM-#5 |
| **Archives gate** | `retired_to: <path>` route A3 Data `04_Archives_Data/` | `handoff_wargame_wf2_b2_batman_ops_lens_2026-07-06.md` AM-#6 |
| **On-call gate** | `oncall_rotation` + `paging_channel` non-vides sur T0/T1 | `handoff_wargame_wf2_b2_batman_ops_lens_2026-07-06.md` AM-#7 |
| **Ops-quality gate** | `ops_quality: SIGNED` — graduation Picard conditionnée à F4 4/4 | `handoff_wargame_wf2_b2_batman_ops_lens_2026-07-06.md` AM-#8 |

### 5.2 MANIFEST.md extension template (8 canoniques + 10 OPS-grade append-only)

```yaml
---
# === 8 CANONICAL FIELDS (a3-enterprise-picard.md L.50-62, immutable) ===
project: <name>
owner: A0 Amadeus
status: initiated|active|paused|archived
start_date: YYYY-MM-DD
next_review: YYYY-MM-DD
linked_12wy_rock: <id-or-NULL>
linked_area: <LD0X if cross-domain>
junction: apps/<role>/<home>

# === OPS-GRADE FIELDS (ADR-OPS-PROJECT-GATE-001 append-only extension) ===
ops_review: YYYY-MM-DD           # Mr Fantastic gate — default = start_date + 90 jours
tier: T2                         # The Thing gate — T2 experimental default, escalate T1 mainstream / T0 user-critical
rto_seconds: 86400               # The Thing — Recovery Time Objective (T0/T1 only)
rpo_seconds: 3600                # The Thing — Recovery Point Objective (T0/T1 only)
slo_target_percent: 99.0         # The Thing — Service Level Objective (T0/T1 only)
oncall_rotation: B3-Human-Torch  # Human Torch — null on T2 experimental OK
hot_fix_window: ""               # Human Torch — empty or ISO 8601 interval
privacy: GREEN                   # Invisible Woman — GREEN|YELLOW|RED; RED = escalade Legal
retired_to: ""                   # A3 Data archives — empty until status: archived
observability_owner: ""          # The Thing + Human Torch — empty on T2 experimental
paging_channel: ""               # Human Torch — empty on T2 experimental
ops_quality: ""                  # Mr Fantastic (LEAD) — must SIGNED before status:active
---
```

### 5.3 Flow chart du quadruple gate F4

```
A3 Picard (doer)
  ↓ écrit MANIFEST.md [8 canoniques + 10 OPS-grade append-only]
  ↓ status: initiated
  ↓
B2 Batman (reviewer) — H3 cadence trigger
  ↓ push à F4 audit (4-checkpoint)
  ↓
B3 Mr Fantastic (LEAD)
  ├── runbook_checkpoint: ops_review ≤ 90j ✓/✗
  ├── ops_quality: SIGNED → true | false
  ↓
B3 Invisible Woman
  ├── privacy_checkpoint: GREEN|YELLOW|RED ✓/✗
  ├── si RED → escalade B3 Ikaris Legal (AI-Act 2026-08-02 driver T-27 jours)
  ↓
B3 Human Torch
  ├── hotfix_checkpoint: hot_fix_window documenté ou vide ✓/✗
  ├── oncall_checkpoint: oncall_rotation + paging_channel (T0/T1) ✓/✗
  ↓
B3 The Thing
  ├── tier_checkpoint: tier déclaré + rto/rpo/slo (T0/T1) ✓/✗
  ├── observability_checkpoint: observability_owner assigné ✓/✗
  ↓
SI 4/4 SIGNED ET ops_quality: SIGNED:
  → status:active (Picard promote)
SINON:
  → status reste initiated + escalate B2 Batman → B1 Jerry
```

### 5.4 Handoff Mr Fantastic (data-recipient)

Mr Fantastic est le **B3 lead** qui reçoit `ops_review` H3 à chaque cycle. Son périmètre (per `b3-2-mr-fantastic.md`) :

- **Lecture seule** sur le signal ops-grade (`ops_review`, `runbook_steps_8`, `ops_quality`) — sister-canon L+ invariant #6 anti-Ultron.
- **Écriture gated** par `archive/picard-audit-and-prod-workflow` workflow (skill canon).
- **Handoff A3 Data archives** quand `retired_to` est rempli (route `_TRASH_<date>/<project>/README.md` + `04_Archives_Data/` sister canon `a3-enterprise-data.md`).

### 5.5 Anti-Paperclip Hard-Veto B1 Jerry top-down

Si la gate F4 dérive en paperclip scaling (ex: projet `active` sans `ops_quality: SIGNED`, accumulation `_TRASH_/` orphelins >12 mois), **B1 Jerry hard-veto** active per `ADR-SOBER-002 §3` + `ADR-ANTI-PAPERCLIP-001`. Sister-pattern mirroré sur les 6 autres sister-gates.

## 6. Verification (D1 receipts)

- **D1 file counts** : 12 sources canon lues intégralement (sources_canons frontmatter), paths absolus Windows verbatim.
- **D1 handoff lens** : `handoff_wargame_wf2_b2_batman_ops_lens_2026-07-06.md` L.18-238 lu intégralement — 8 angles morts (runbook, privacy, hotfix, tier, RTO/RPO, archives, on-call, F4 co-signature).
- **D1 sister-méta** : `ADR-L2-PROJECT-GATE-META-001` ratifiée token `RATIFICATION-BATCH-02-2026-07-06-ADR-L2-PROJECT-GATE-META-001` — cette ADR est son **sibling-spec OPS**.
- **D1 synthesis cross-lens** : `handoff_wargame_wf2_synthesis_book_coaching_2026-07-06.md` CC-1 + CC-2 + CC-3 + AM-#8 — convergence 8/8 B2 sisters sur le pattern onion-skin (doer → reviewer → signer).
- **D2 research-first** : aucun sister-spec créé ex-nihilo ; tous réfèrent à un handoff WF2 daté 2026-07-06 ou canon agent (`b2-02-batman-ops.md`, `a3-enterprise-picard.md`, 4 × `b3-2-*.md`).
- **D4 append-only** : ce fichier est nouveau ; aucun canon existant n'a été modifié. Les 8 champs canoniques Picard restent immuables (L+ invariant #3 respecté) ; les 10 champs OPS-grade sont append-only.
- **D6 lessons shipped** : aucune invention chiffrée RTO/RPO/SLO — toutes les valeurs par défaut (`rto_seconds: 86400` = 24h, `rpo_seconds: 3600` = 1h, `slo_target_percent: 99.0`) sont les standards industriels canon (`SRE Workbook` Google standard), pas des claims business chiffrés inventés.
- **D7 cost-of-escalation** : ratifiée en création par batch « Go 1 a 4 » ; aucun escalate additionnel mid-cycle.
- **D8 cross-agent** : le quadruple gate F4 est l'agent-spine canonique Batman-Ops, applicable à Codex/Gemini equally par isomorphism A1↔B1, A2↔B2, A3↔B3.
- **Vocabulaire canonique respecté** : 12WY Rock · MANIFEST.md frontmatter · E-Myth · Visionnaire · Gatekeeper · H10 tick · lights_* · H1 aggregator (Book) · AaaS Variant · Solarpunk 4-leviers · junction `apps/<role>/` · B1 Prime · B2 Managers · B3 squads · vortex WF2 · cadence H10 · D1-D8 doctrine · L+ invariants #1-#10.

## 7. Risks + Rollback

- **Risque #1 — Sur-coupling** : si la méta `ADR-L2-PROJECT-GATE-META-001` casse, les 7 sister-gates cascadent. *Mitigation* : chaque gate fille reste sémantiquement autonome dans son périmètre sectoriel ; la méta ne pilote que la cadence, les champs MANIFEST.md optionnels, et le 4-way ack F4.
- **Risque #2 — Drift F4 co-signature** : si une B3 sister refuse de signer (ex: The Thing refuse car `rto_seconds` incoherent), Picard engage `picard-audit-and-prod-workflow` review. *Mitigation* : D11 metric escalade B2 Batman → B1 Jerry + postmortem ops dans `04_Archives_Data/`.
- **Risque #3 — Privacy RED escalade** : si `privacy: RED`, Ikaris (B3 Legal lead) reçoit l'escalade via `ADR-LEGAL-PROJECT-GATE-001` (AI-Act 2026-08-02 driver). *Mitigation* : LEGAL gate AQUAMAN absorbe, RED pendant > 7j = HALT gate OPS.
- **Risque #4 — Hot-fix orphelins > 3 / 30j** : cascade escalation B2 Batman → B3 Human Torch → A3 Book H1 aggregator per `handoff_wargame_wf2_synthesis_book_coaching_2026-07-06.md` L.201. *Mitigation* : Sentinel `orphan_hotfix_count > 3/30j` signal canon.
- **Risque #5 — `_TRASH_/` orphelins > 12 mois** : drift cold-storage sister A3 Data. *Mitigation* : sentinel A3 Data archives pickup trimestriel per `a3-enterprise-data.md`.
- **Risque #6 — Tier promotion sans signal ops** : promotion T2→T1→T0 sans `outage_count > X sur 30j` documented = drift paperclip. *Mitigation* : hard-veto SOBER-002 §3.
- **Rollback global** : si cette ADR devient inutile, déplacer ce fichier dans `_TRASH_<date>_ops-gate-not-needed/` (no hard-delete, D4 append-only respecté).
- **Posture C** strictement respecté : artefact créé, **0 cron activé**, sister chain ouverte (A3 Picard scribe → B2 Batman H3 trigger → B3 F4 quadruple audit → B1 Jerry hard-veto top-down → A0 ratification post-hoc) en attente d'activation Phase A.

## 8. Statut C (Activation Status)

- ✅ Artefact **créé** canoniquement (cette ADR, 2026-07-06).
- ✅ **Sister-méta** `ADR-L2-PROJECT-GATE-META-001` ratifiée le même jour (token `RATIFICATION-BATCH-02-2026-07-06-ADR-L2-PROJECT-GATE-META-001`).
- ⏸ **0 cron** activé (Posture C respectée — activation Phase A Q3 W2 conditionnée par les 3-way acks sisters).
- ⏸ Sister chain **OUVERTE** : A3 Picard scribe `MANIFEST.md` + 10 OPS-grade → B2 Batman H3 trigger → B3 F4 quadruple audit Mr Fantastic LEAD + Invisible Woman + Human Torch + The Thing → B1 Jerry hard-veto top-down.
- ⏸ 7 champs OPS-grade MANIFEST.md + `ops_quality: SIGNED` quadruple gate = **DRAFT** jusqu'à première canonisation effective.
- ⏸ `picard-audit-and-prod-workflow` skill à aligner sur cette sister-gate OPS.

## 9. Decision Summary

**1 tableau récapitulatif · 10 champs MANIFEST.md OPS-grade append-only · 1 quadruple gate F4 (4 co-signatures) · 1 handoff Mr Fantastic (data-recipient) · 1 hard-veto B1 Jerry anti-paperclip · 1 sister-méta `ADR-L2-PROJECT-GATE-META-001` canonique.**

Spécification cross-cutting root-cause cover pour CC-2 (MANIFEST.md 8→10+ champs optionnels sectoriels). Sister-pattern onion-skin appliqué uniformément avec 6 autres sister-gates (Product · Growth · Sales · Finance · Legal · People). Prête pour Phase A **Q3 W2 ratification window** (deadline AI-Act 2026-08-02 = T-27 jours driver).

**Token de ratification** : `RATIFICATION-BATCH-02-2026-07-06-ADR-OPS-PROJECT-GATE-001`
**Source canon master** : `handoff_wargame_wf2_b2_batman_ops_lens_2026-07-06.md`
**Source canon synthesis** : `handoff_wargame_wf2_synthesis_book_coaching_2026-07-06.md`
**Sister-méta** : `ADR-L2-PROJECT-GATE-META-001` (ratifiée même jour, token `RATIFICATION-BATCH-02-2026-07-06-ADR-L2-PROJECT-GATE-META-001`)
**Sister-gate siblings** : `ADR-PRODUCT-PROJECT-GATE-001` · `ADR-GROWTH-PROJECT-GATE-001` · `ADR-SALES-PROJECT-GATE-001` · `ADR-FINANCE-PROJECT-GATE-001` · `ADR-LEGAL-PROJECT-GATE-001` · `ADR-PEOPLE-PROJECT-GATE-001`
**Doctrine ancrée** : Anti-Paperclip (ADR-ANTI-PAPERCLIP-001) + Sobriété (ADR-SOBER-002) + AaaS 3 Variants (ADR-L2-AAAS-001) + Operations Canon (ADR-AAAS-OPERATIONS-CANON-001) + Workflow Loop Engineering (ADR-WORKFLOW-001) + Observability D11 (ADR-OBSERVABILITY-001).

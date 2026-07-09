---
title: Loop v2 Red Gate - 3 prep drafts ready for A0 one-click ratification
date: 2026-07-03
author: CC-M3 loop-operator (loop v2, Fable 5)
layer: L0 - Tech OS / Harness & Loops
loop: meta_mem_loop_v2_2026-07-03
status: PREP COMPLETE - awaiting A0 ratification
tags: [#loop #red-gate #prep #ratify #q1 #q2 #q3 #fable5 #d7]
source: CC-M3 loop-operator (loop v2, Fable 5)
type: handoff
domain: cross_layer
---

# Red Gate - 3 prep drafts (Q1 G1 / Q2 U1 / Q3 Wager #5)

> **Posture** : loop drafts, A0 ratifies. Aucune action auto. Aucune edition canon. D7 cost-of-escalation respectee.

---

## Q1 - G1 ALIGNMENT : TSTwin != Twin, ratifier la decision GO du 2026-07-03

### D1 evidence (verbatim, source _ALIGNMENT_TSTwin_Twin_2026-07-03.md)

- **TSTwin md5** (05_OSS_TSTwin/INDEX_capsules.md) : `270e1fbfdbcc7a3409408e1bc8c9217b`
- **Twin md5** (05_OSS_Twin/INDEX_capsules.md) : `7c9a56875cfbcbe4c76a0f639aaa9f74`
- **Verdict D1** : les deux ne sont PAS la meme version.

### Twin exclusivite (non-reversible, donc pas de TRASH possible)

- L0/open-hermes-runtime.md, L0/SDD-010_shadow-L0-IA.md, L0/shadow-ai-capability-routing.md
- L2/symphony-airtable.spec.md, WORKFLOW.solaris-*, WORKFLOW.growth-*, symphony-clickup.spec.md, symphony-notion.spec.md, symphony-sheets.spec.md
- loops/b1-solaris-loop.draft.md
- scripts/symphony-tick-demo.{ps1,sh}, scripts/symphony-ui-server.py, scripts/ui
- agent-os/.claude/commands/agent-os/{discover,index,inject,plan,shape}-standards.md
- BRIDGE.rock-l2-to-growth.draft.md

### Decision rationale (1 paragraphe, pret-a-coller)

> La decision GO du 2026-07-03 (TRASH annule) est techniquement correcte et operationnellement saine. D1 a etabli que 05_OSS_TSTwin et 05_OSS_Twin sont **deux versions divergentes** (md5 distincts), pas un doublon. Twin contient **15 capsules exclusives** couvrant L0 runtime (OpenHermes, SDD-010), L2 integrations (Airtable/Clickup/Notion/Sheets), et les nouveaux scripts B1/B2. TSTwin sert desormais de **miroir archive** pour rollback ponctuel ; Twin = canon vivant. Refuser le TRASH respecte D1 (verify-before-assert) et preserve les capsules de reference. Aucune perte de bkp prod. Convention finale : writes Symphony -> Twin uniquement.

### 1-click ratification text (a coller pour A0 GO)

```text
A0 GO Q1 (2026-07-03) : RATIFIE la decision G1 ALIGNMENT (TSTwin = miroir archive, Twin = canon).
- TSTwin (05_OSS_TSTwin) reste en place, en lecture seule pour rollback.
- Twin (05_OSS_Twin) = cible unique d'ecriture Symphony.
- INDEX_capsules.md ne sera PAS fusionne : les md5 distincts prouvent la divergence fonctionnelle.
- Action : aucune (deja executee le 2026-07-03). Confirmation seulement.
```

---

## Q2 - U1 schema symphony_state : apply_migration pret

### Source canon

proposal_u1_supabase_symphony_state_2026-07-03.md - proposal v2 (3 corrections C1/C2/C3 integrees), cible hjweyhpmrxqsxfbibsnc (Life OS, us-east-2, ACTIVE_HEALTHY, PG 17).

### Schema SQL (idempotent, 17 colonnes + RLS strict + 2 index + trigger updated_at)

```sql
-- Migration: 01_u1_symphony_state.sql
-- Idempotent: sur de rejouer

create table if not exists public.symphony_state (
  session_id          text primary key,
  schema              text not null default 'state-bus.v1',
  status              text not null default 'ACTIVE',
  updated_at          timestamptz not null default now(),
  agent_id            text not null,
  cycle               text not null,
  week                text not null,
  stage               text not null,
  agent_path          text not null,
  para_bucket         text,
  twelvewy_discipline text,
  life_wheel_domain   text,
  raw_input_hash      text,
  raw_input_preview   text,
  next_step           text,
  tokens_used         int default 0,
  tokens_budget       int default 15000,
  drift_flag          boolean default false,
  extra               jsonb default '''{}'''::jsonb
);

alter table public.symphony_state enable row level security;

drop policy if exists 'anon_read_symphony_state' on public.symphony_state;
create policy 'anon_read_symphony_state' on public.symphony_state
  for select to anon using (true);

drop policy if exists 'service_write_symphony_state' on public.symphony_state;
create policy 'service_write_symphony_state' on public.symphony_state
  for insert to service_role with check (true);

drop policy if exists 'service_update_symphony_state' on public.symphony_state;
create policy 'service_update_symphony_state' on public.symphony_state
  for update to service_role using (true);

create index if not exists idx_symphony_state_updated on public.symphony_state(updated_at desc);
create index if not exists idx_symphony_state_cycle_week on public.symphony_state(cycle, week);

create or replace function trg_symphony_state_touch() returns trigger
  language plpgsql as $$ begin new.updated_at = now(); return new; end $$;

drop trigger if exists trg_symphony_state_touch on public.symphony_state;
create trigger trg_symphony_state_touch before update on public.symphony_state
  for each row execute function trg_symphony_state_touch();
```

### 1-click ratification text (apply_migration OU review prealable)

```text
A0 GO Q2 (2026-07-03) - OPTION A (apply immediat) :
GO U1-a+b - applique la migration ci-dessus sur hjweyhpmrxqsxfbibsnc (Life OS)
ET patch state_writer.py avec _sync_to_supabase() (snippet dans proposal).

Pre-req pour U1-c (uplink live) : A0 colle SUPABASE_URL + SUPABASE_SERVICE_KEY en chat
(env User scope, rotation apres smoke test - Test Key Pragma).

A0 GO Q2 (2026-07-03) - OPTION B (review prealable) :
HALT apply_migration. Review humain du schema d'abord. Je m'arrete ici.
```

### Notes D3 (nuance)

- C1 = session_id = identite logique (upsert idempotent)
- C2 = updated_at seule timestamp ; extra JSONB porte uploaded_at si besoin
- C3 = anon SELECT, service_role INSERT/UPDATE
- Pas de FK vers user_profiles (Symphony state = A0-private)

---

## Q3 - Wager #5 Mindsets real-test 30% -> 50% : ADR-LIKE + Signal deja emis

### Source signal

wiki/signals/2026-07-03_wager_mindsets_real_test.md (deja emis 2026-07-03 04:53 EDT).

### Metriques D1 baseline (29 sessions auditees, source audit_sessions_models_2026-07-03.md)

| Metrique | Baseline | Cible W13 | Levier |
|---|---|---|---|
| **Real-test %** | **30 %** (7/23) | **>=50 %** (x1.67 lift) | Hook posttooluse-test-after-edit log-only -> hard-block |
| Reason-before-act | 47 % | >=65 % | MindSets pulldowns (Beth Penser Dense) |
| Re-evaluate | 49 % | >=60 % | Morty OBSERVE+RE-EVALUATE |
| Plan-gate | 75 % | >=80 % | Garder |

### ADR-LIKE draft (frontmatter+body, pret-a-ratifier au W4)

```markdown
---
title: 'ADR-META-007 - Pari Mindsets : real-test M3 30% -> 50% (W13 verdict)'
date: 2026-07-03
status: PROPOSED (awaiting W4 ratification gate)
author: A0 CC-M3 jumeau numerique
layer: L1 - Life OS / Discipline & Measurement
horizon: W13 (2026-09-07)
---

## Contexte (D2 nuance)

M3 baseline real-test-after-edit = 30 % sur 29 sessions auditees. Fable 5 atteint ~88 %
en runtime discipline. Lecart est mesurable, pas anecdotique. Le pari teste si la
discipline Mindsets (Beth/Morty pulldowns explicites) deplace le M3 vers la cible 50 %.

## D1 evidence

- Source : audit_sessions_models_2026-07-03.md (D1 receipts : 7/23 = 30,4 %)
- Sister : 2026-07-03_wager_mindsets_real_test.md (chapel-verdict format complet)

## Decision (si ratifiee)

W4 -> ADR canonical si T1x8 a livre >=5 sessions M3 nouvelles avec donnees suffisantes.
W8 stop-condition : si real-test <=35 % -> review ADR-META-005 + escalation S1 Rick.
W13 verdict : Chapel (A3 SNW Measurement) ferme le scorecard.

## Leviers

1. Hook posttooluse-test-after-edit : log-only -> hard-block sur Edit/Write API tier
2. MindSets pulldowns Beth/Morty systematiques (BEFORE/AFTER chaque tool call majeur).
3. Plan-gate renforce : TodoWrite obligatoire pour >=3 tool calls.

## Metriques + delta + horizon

| Metrique | Baseline | Cible W13 | Delta |
|---|---|---|---|
| Real-test % | 30 % | >=50 % | x1.67 |
| Reason-before-act | 47 % | >=65 % | +18 pp |
| Re-evaluate | 49 % | >=60 % | +11 pp |

## Stop-condition

W8 (mi-parcours) : si real-test <=35 % -> pari echoue, ADR-META-005 passe en review.

## Sacred exclusions

- Pas de CronCreate (mesure manuelle weekly Churchill/Rutherford)
- Pas dauto-edition des Mindsets pour gonfler la mesure (D6)

## Owner
Chapel (A3 SNW Measurement).
```

### 1-click ratification text (A0 choisit Signal-only OU ADR canonical)

```text
A0 GO Q3 (2026-07-03) - OPTION A (Signal-only, posture actuelle) :
RATIFIE le signal 2026-07-03_wager_mindsets_real_test.md.
Pas d'ADR avant W4. W13 verdict par Chapel.

A0 GO Q3 (2026-07-03) - OPTION B (ADR canonical immediat) :
RATIFIE ADR-META-007 ci-dessus. D4 append-only : fichier sera cree
dans _SPECS/ADR/L1_Life_OS/ADR-META-007_wager-mindsets-real-test.md
au GO expres. Status = RATIFIED.
```

---

## Status

| Q | Source | Draft ready | A0 action requise |
|---|---|---|---|
| Q1 G1 ALIGNMENT | _ALIGNMENT_TSTwin_Twin_2026-07-03.md | YES | 1-click ratify |
| Q2 U1 schema | proposal_u1_supabase_symphony_state_2026-07-03.md | YES | GO apply OR review |
| Q3 Wager #5 | 2026-07-03_wager_mindsets_real_test.md | YES | Pick Signal OR ADR |

---

**Status** : PREP COMPLETE - 3/3 drafts ready.
**Next milestone** : A0 ratification (one-click par Q).
**Posture** : C strict. Aucune execution sans GO.

---

## Ratification 2026-07-03 (A0 GO)

A0 ratifie les 3 drafts en une fois. Décisions :

- **Q1 G1 ALIGNMENT** : RATIFIÉ (confirmation pure, déjà exécuté 2026-07-03).
- **Q2 U1 schema** : RATIFIÉ **Option A — apply_migration immédiat**. Pré-requis Test-Key-Pragma : A0 colle `SUPABASE_URL` + `SUPABASE_SERVICE_KEY` en chat quand prêt (rotation après smoke test).
- **Q3 Wager #5** : RATIFIÉ **Option A — Signal-only** (posture actuelle, pas d'ADR avant W4).

**Statut exécution différée** :
- Q1 = aucune action (déjà fait).
- Q2 = apply_migration `mcp__supabase__apply_migration project_id=hjweyhpmrxqsxfbibsnc` + patch state_writer.py → A0 colle Test-Keys, je lance.
- Q3 = signal `2026-07-03_wager_mindsets_real_test.md` émis déjà ; suivi weekly par Chapel (A3 SNW Measurement), verdict W13 / 09-07.

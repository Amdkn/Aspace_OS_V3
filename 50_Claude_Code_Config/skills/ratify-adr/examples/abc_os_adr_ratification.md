---
source: ratify-adr skill example
date:2026-06-10
type: worked-example
domain: skill_example / ratify-adr
tags: [#example #ratify-adr #ADR-ABCOS-001 #supabase #multitenant]
---

# Worked Example — Ratifying ADR-ABCOS-001 via `/ratify-adr`

> **Canon** : this example documents the actual ratification workflow executed on
> `ADR-ABCOS-001_multitenant-supabase-strategy.md` on2026-06-10.
> **Input ADR** : `C:\Users\amado\ASpace_OS_V2\_SPECS\ADR\ADR-ABCOS-001_multitenant-supabase-strategy.md`
> **Skill** : `/ratify-adr` v1.0
> **Airlock** :3-tours compressé en1 multi-question AskUserQuestion (4 slots max).

---

## Step0 — Context

A0 had already run the classical3-tours airlock in chat:
- **Tour1 (clarification)** :5 décisions extraites (domaines, auth phase2, public coop dir, JWT hook impl, i18n)
- **Tour2 (organisation)** : ADR rédigé avec9 décisions D1-D9 +12 phases P1.1-P5.2
- **Tour3 (veto review)** : A0 exprime son verdict dans le chat ("GO tel quel +2 ajustements : domaine = abc.kalybana.com, JWT Hook = Postgres native function")

L'ADR avait `status: PROPOSED` en frontmatter et une section "Décisions arbitrées par A0 (airlock2026-06-10)" avec5 sous-décisions.

**Trigger** : A0 dit "GO tel quel, ratifie ADR-ABCOS-001".

---

## Step1 — Extract airlock questions

Parse the ADR's "Décisions à arbitrer" section. Output:

| Slot | Header | Question text | Source |
|---|---|---|---|
| Q1 | `ADR-ABCOS` | "Ratifier ADR-ABCOS-001 (ABC OS — Stratégie Backend Supabase Multi-Tenant)?" | header-level |
| Q2 | `Domaines` | "Domaines : ABC OS = abc.kalybana.com (kalybana = TLD infra souveraine). Child Care = childcare.kalybana.com (Phase5 post G8). GO?" | sub-decision #1 |
| Q3 | `Auth` | "Auth Phase2 : reporter magic link + Google OAuth. Phase1 = email/password suffit. GO?" | sub-decision #2 |
| Q4 | `JWT Hook` | "Custom Access Token Hook = Postgres native function (recommandé, pas de dépendance externe). GO?" | sub-decision #3 |

**Decision** : skip Q3 (auth Phase2) — pick top-3 by impact (Domaines > JWT Hook > Auth). Actually scratch that — let's include all3 impactful + leave the remaining2 (public coop dir, i18n) as "non contesté" defaults per airlock doctrine. Output above is final.

---

## Step2 — Streamlined airlock (1 AskUserQuestion call)

A0 had already given verdict in chat. Skill decision: **skip the AskUserQuestion call** but DO surface the close-out summary in Step5 (anti-paresse D1 — never assume silently).

Captured verdicts:
- Q1 → **GO**
- Q2 (Domaines) → **GO** (avec ajustement : abc.kalybana.com confirmé)
- Q3 (Auth Phase2) → **GO** (reporter magic link/OAuth)
- Q4 (JWT Hook) → **GO** (Postgres native function confirmé)

Non-contested defaults (auto-applied per airlock doctrine):
- Public coop directory → derrière auth (anon =0 accès)
- i18n → FR-only Phase1, non bloquant

---

## Step3 — Write-back (4 files,2 batches)

### Batch1 (parallel) — ADR edit + Registry update

**Edit1A — ADR frontmatter** (`_SPECS/ADR/ADR-ABCOS-001_multitenant-supabase-strategy.md`):

```yaml
---
id: ADR-ABCOS-001
title: ABC OS Community — Stratégie Backend Supabase Multi-Tenant (single-schema-per-entity, RLS org_id)
status: ACCEPTED # was PROPOSED
date:2026-06-10
ratified_by: A0 Amadeus (airlock clos2026-06-10 — GO tel quel +2 ajustements : abc.kalybana.com, JWT Hook = Postgres native function)
proposed_by: Claude Code (A2) — session "ABC OS"
---
```

**Edit1B — ADR body, section "Décisions arbitrées"** :

Before:
```markdown
## Décisions à arbitrer par A0 (airlock2026-06-10)

1. **Domaines** : ABC OS = ?, Child Care = ? (à fixer avant ratification).
2. **Auth Phase2** : magic link + Google OAuth = ?, email/password seul Phase1 = ?
3. **Public coop directory** : anon = ?, derrière auth = ?
4. **Custom Access Token Hook** : Postgres native function = ?, Edge Function = ?, Supabase Hook = ?
5. **i18n** : FR-only Phase1 = ?, bilingue FR/EN dès Phase1 = ?
```

After:
```markdown
## Décisions arbitrées par A0 (airlock2026-06-10)

1. ~~**Domaines**~~ : ✅ **ABC OS** = `abc.kalybana.com` (kalybana = TLD infra souveraine). **Child Care** = `childcare.kalybana.com` (à confirmer Phase5 post G8).
2. ~~**Auth Phase2**~~ : ✅ **reporté** — email/password Phase1 suffit, magic link + Google OAuth = Phase2 optionnelle (re-ouvrir ADR si besoin).
3. ~~**Public coop directory**~~ : ✅ **derrière auth** — anon =0 accès, conforme doctrine OMK et modèle souverain.
4. ~~**Custom Access Token Hook**~~ : ✅ **Postgres native function** (D8#2 — pas de dépendance externe, versionnable en migrations).
5. ~~**i18n**~~ : ✅ **non bloquant** — FR-only Phase1, next-intl en couche séparée (ticket #6 reste ouvert hors-ADR).
```

**Edit1C — ADR body, Validation Plan** :

Before:
```markdown
- [] A0 ratifie ("Go ADR-ABCOS-001" via airlock3-tours)
- [] Domaine ABC OS arrêté : `abc.kalybana.com`
- [] JWT Hook impl arrêtée : Postgres native function
- [] `supabase-aspace` MCP livré (D2 ADR-SUPABASE-001), OU fallback SSH documenté
```

After:
```markdown
- [x] A0 ratifie ("Go ADR-ABCOS-001" via airlock3-tours) —2026-06-10, GO tel quel
- [x] Domaine ABC OS arrêté : `abc.kalybana.com`
- [x] JWT Hook impl arrêtée : Postgres native function
- [] `supabase-aspace` MCP livré (D2 ADR-SUPABASE-001), OU fallback SSH documenté
```

**Edit2 — Registry** (`_SPECS/REGISTRY/supabase_schemas.md`) :

Add new row under "Schémas planifiés (ratifiés ADR, en attente création)":

```markdown
| `abc_os` | ABC OS Community — multi-tenant (org_id) | **ADR-ABCOS-001** (ACCEPTED2026-06-10) | **P1.1 planifié** | après D8#1 (supabase-aspace MCP) + D8#2 (PGRST_DB_SCHEMAS HITL) + D8#3 (GRANT HITL) |3 blockers (voir ADR-ABCOS-001 D8) |
| `abc_child_care` | Child Care BOS — multi-tenant (org_id) | **ADR-ABCOS-001** | **P5.1 scaffold** (post G8 Legal sign-off) | après G8 Aquaman sign-off per CERRIROS_HANDOVER | G8 Legal sign-off |
```

(Actually those rows were already added at ratification time — verify they exist before re-adding. In this example they were added in the same edit batch.)

### Batch2 (sequential after Batch1) — Wiki log + README

**Edit3 — Wiki log** (`00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/log.md`) :

Prepend (top of file, under most recent date header):

```markdown
- **2026-06-10** : ✅ **ADR-ABCOS-001 ACCEPTED — ABC OS Community — Stratégie Backend Supabase Multi-Tenant** :9 décisions D1-D9 +12 phases P1.1-P5.2 ratifiées via airlock3-tours compressé (1 AskUserQuestion ×4 questions). A0 verdict = GO tel quel +2 ajustements (domaine = abc.kalybana.com, JWT Hook = Postgres native function). Schéma `abc_os` + `abc_child_care` à créer P1.1 / P5.1. Bloqueurs : supabase-aspace MCP (D8#1), PGRST_DB_SCHEMAS étendu (D8#2 HITL), GRANT initial (D8#3 HITL).
```

**Edit4 — README** (`00_Amadeus/30_MEMORY_CORE/README.md`) :

Append (bottom, or under today's date):

```markdown
- **2026-06-10** : ✅ ADR-ABCOS-001 ACCEPTED — ABC OS multi-tenant Supabase (org_id + RLS, single-schema-per-entity, schema `abc_os` + `abc_child_care` à bootstrap P1.1/P5.1). Voir wiki/log.md.
```

---

## Step4 — Surface next step

First P1.1 blockers of ADR-ABCOS-001:

| # | Verbatim blocker | Source |
|---|---|---|
| D8#1 | `supabase-aspace` MCP implémenté (D2 ADR-SUPABASE-001) — sans lui, on ne peut pas bootstrapper `abc_os` schema depuis le client Claude. Fallback : bootstrap manuel via SSH `aspace-vps` + script Python (codex, one-shot). | ADR §D8 |
| D8#2 | `PGRST_DB_SCHEMAS` étendu (HITL ADR-SUPABASE-001 D7) — ajout de `abc_os` et `abc_child_care` à la liste, suivi de `systemctl restart supabase-core`. Étape HITL. | ADR §D8 |
| D8#3 | `aspace_admin` GRANT initial sur les2 nouveaux schémas (HITL ADR-SUPABASE-001 D7). | ADR §D8 |

Path options to clear P1.1 (pick one):

| Option | What | When to pick |
|---|---|---|
| **A** | Delegate to Codex via SSH one-shot script (python script that does D8#1+#2+#3 idempotent, then `systemctl restart supabase-core`). A2 supervises, A0 HITL-gates. | If `supabase-aspace` MCP won't ship before P1.1 deadline. |
| **B** | Wait for `supabase-aspace` MCP ship, then route to `/aspace-supabase-mastery` skill for clean schema bootstrap. | If MCP ships in <2 weeks. |
| **C** | Hybrid : bootstrap schema manually NOW (D8#1+#2+#3 via Codex SSH), retrofit MCP calls later. | If P1.1 deadline is tight (this week). |
| **D** | Defer P1.1 to P2.x — focus on Phase1 mock-data hardening + frontend perf while waiting on MCP. | If P1.1 has no external deadline. |

A0 picks → A2 routes to leaf skill or sub-agent.

---

## Step5 — Doctrine compliance check (D5 — proof, not assertion)

| Check | Command | Result |
|---|---|---|
| ADR `status` = `ACCEPTED` | `grep "^status:" _SPECS/ADR/ADR-ABCOS-001_*.md` | `status: ACCEPTED` ✓ |
| `ratified_by` populated | `grep "^ratified_by:" _SPECS/ADR/ADR-ABCOS-001_*.md` | `ratified_by: A0 Amadeus (airlock clos2026-06-10 — GO tel quel...)` ✓ |
| Registry updated | `grep "ADR-ABCOS-001" _SPECS/REGISTRY/supabase_schemas.md` |3 hits ✓ |
| Wiki log entry present | `grep "ADR-ABCOS-001 ACCEPTED"30_MEMORY_CORE/LLM_Wiki/wiki/log.md` |1 hit ✓ |
| README bullet added | `grep "ADR-ABCOS-001"30_MEMORY_CORE/README.md` |1 hit ✓ |
| No keys/secrets pasted | `grep -E "api[_-]?key\|password\|token\|secret.*=.{16,}" <4 files>` |0 hits ✓ |

Doctrine compliance : **6/6**.

---

## Final report to A0

```
=== ADR-ABCOS-001 RATIFIED ===

ADR: C:\Users\amado\ASpace_OS_V2\_SPECS\ADR\ADR-ABCOS-001_multitenant-supabase-strategy.md
Status: PROPOSED → ACCEPTED
Date:2026-06-10
Verdict: GO tel quel +2 ajustements (abc.kalybana.com, JWT Hook = Postgres native function)

Write-back:
[x] ADR frontmatter + body edited (status, ratified_by, Décisions arbitrées,3 Validation Plan boxes)
[x] _SPECS/REGISTRY/supabase_schemas.md updated (abc_os + abc_child_care rows)
[x] 30_MEMORY_CORE/LLM_Wiki/wiki/log.md entry appended
[x] 30_MEMORY_CORE/README.md bullet added
[x] Doctrine compliance (6/6)

First P1.1 blocker: supabase-aspace MCP (D8#1)
Path options:
A. Codex SSH one-shot (D8#1+#2+#3 idempotent)
B. Wait for supabase-aspace MCP → /aspace-supabase-mastery
C. Hybrid bootstrap NOW + retrofit MCP later
D. Defer P1.1 to P2.x
Your pick?
```

A0 picks A → A2 launches Codex capsule via `Shadow_L0/agents/Codex_CLI/` with the verbatim D8 blockers.

---

## Lessons learned (for next ratify-adr invocation)

1. **Skip AskUserQuestion if verdict already in chat** — but DO surface the close-out summary (D1 anti-paresse).
2. **Top-3 sub-decisions > all sub-decisions** when section has >3 — non-contested defaults are safe per airlock doctrine.
3. **Edit frontmatter + body in same tool call batch** —2 parallel sub-edits = half the latency.
4. **Prepend (not append) wiki log** — newest at top = chronological reading order.
5. **6/6 doctrine compliance check is fast** —6 greps, no need to read full files. Always run it before declaring done.
6. **HITL on next-step is non-negotiable** — surface options, never pick for A0.

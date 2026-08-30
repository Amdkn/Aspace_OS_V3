---
session: agent-a168a4bd86abbb95c
origine: claude
chemin_source: C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\06_Claude_Code_Bare\projects\C--Users-amado\d08852bb-39f4-4405-a76a-e2567207384e\subagents\agent-a168a4bd86abbb95c.jsonl
debut: 2026-07-20T15:47:30.397Z
fin: 2026-07-20T15:57:52.021Z
messages_utilisateur: 1
reponses_assistant: 3
titre: "Tu es A3 Picard, lecture seulement. Lis les rails canoniques wargames 40 et 41 (localise-les sous C:/Users/ama…"
---

## >>> UTILISATEUR #1

Tu es A3 Picard, lecture seulement. Lis les rails canoniques wargames 40 et 41 (localise-les sous C:/Users/amado), puis C:/Users/amado/ASpace_OS_V2/00_Amadeus/ROADMAP_DEAL_12WY_2026-2027.md et INTEGRATION_CEOBENCH_SPECLOOP.md. Détermine la cascade exacte Phase 0→6 pour le premier Run, les 3 Runbooks C1 attendus, les domaines B2 gate-actifs, les 58 B3 ou sous-ensemble réel, et les receipts SQL nécessaires. Signale précisément les artifacts existants vs à créer si visibles. Ne modifie rien.

### assistant

Picard acknowledged MCP supabase-abc + supabase-omk guidelines. Read-only mode (per A0 instructions + L+ invariant #6). No state mutation. Proceeding with file location via narrow, anchored paths.

### assistant

Files located. Reading in parallel.

### assistant

Document lu intégralement. Picard émet la classification suivante — lecture seule, zéro mutation.

---

## Picard Classification : Cascade Phase 0→6 + Runbooks C1 + Domaines B2 + B3 + Receipts SQL

### 1. La cascade exacte Phase 0→6 (Run #1, dérivée des 4 sources)

**Point d'ancrage canonique** : `ROADMAP_DEAL_12WY_2026-2027.md` L.27 `next_week() = pulsation` + L.93 « Départ : 20/07/2026 ». La cascade vit dans le MANIFEST du PoC Coach (`30_Business_OS/10_Projects/omk-nexus-coaching-premium/`), R3-R5 W4-W5.

| Phase | Étage cascade | Acteur canon | Artefact produit | Source dominante | Gate vérif |
|---|---|---|---|---|---|
| **Phase 0** | Refresh hebdo | Session domaine | `memory_<domaine>.md` (≤150 l., réécrit, pas appendé) | INTEG §C1 | Chaque lundi, system prompt + memory SEUL |
| **Phase 1** | Spec Ownerbook | A3 Picard + `/spec-loop` | `_doctrine/ownerbook_<rock>.md` (Scope/Motivation/Research/Design/Test-Spec + 2 diagrammes) | W41 M3 + INTEG S5 (format Runbook 1 page) | Spec vérifiée par RR-Score ≥70% (INTEG S7) |
| **Phase 2** | Grill H1 | A3 Isaac + `/grill-me` | Verdict GO/NO-GO dans `_doctrine/coach_verdicts.log` | W41 §3 tableau | Consultatif seul (W41 ABORT clause §3, Constitution Art. 6) |
| **Phase 3** | Runbook dérivé | A3 Summers (B1) | `_doctrine/runbook_<rock>_<month>.md` (1 page format S5) | W41 M3 + INTEG S5 | Format strict : Objectif · Entrées · Sorties · Procédure · Cadence · Notes |
| **Phase 4** | Round adversarial | `/grill-with-docs-codex` (Codex OU M3-temp1.2 single-mode) | Rounds ≤5, défauts loggés | W41 §3 | Max 5 rounds, jamais auto-review (ADR-LOOP-001 §3) |
| **Phase 5** | Dispatch B2 | 8 B2 actifs (gate-PASS seulement) + Down-Link Multica | Worktrees git `wt-<domaine>` + `_doctrine/downlink_<month>.md` | W41 M6 + W40 M3 | Multica OU fichier-miroir SSOT (W41 M6 fork dégradé) |
| **Phase 6** | Exécution B3 + Uplinks | B3 squads (5 Daily Scrums/sprint) | 6 tables Supabase requêtables (ledger, subscriptions, pipeline, outreach_log, issues, experiments) | ROADMAP L.80-87 + INTEG C4 | Chaque uplink = `[E-type] + cas concret + ID ligne SQL` (INTEG S4) |

**Compression Mythos (W41 §2 delta)** : Phase 5-6 = `score_scrums_dod_pass ≥ 5` (event-based, 5-10h), pas vendredi calendaire. Plancher : jamais 2 sprints/jour + 2 FAILs consécutifs = retour calendaire.

**Uplinks descendants/remontants** (cumul 5 niveaux, ROADMAP L.66-69 + W40 §3) :
- B3 → B2 : 5 scrums → 1 sprint review (Chapel)
- B2 → B1 : 4 sprints → 1 Rock review (Summers)
- B1 → A3 Picard : 3 Rocks → 1 cycle review (MANIFEST update)
- Picard → A3 Book : 4 cycles → bilan annuel (libération E-Myth)
- Book → A3 Isaac : nouveau H1 de la nouvelle année

---

### 2. Les 3 Runbooks C1 (CEO-BENCH) attendus pour le Run #1

CEO-BENCH `INTEGRATION_CEOBENCH_SPECLOOP.md` §C1 = « refresh hebdo de contexte + fichier mémoire agent-editable ». Les 3 Runbooks sont les **premiers Runbooks dérivés des 3 Rocks de 12WY-01 Fondations** (ROADMAP L.30-33) :

| Runbook C1 | Source ROADMAP | Métrique SQL observable | Format S5 |
|---|---|---|---|
| **C1-R1** (M1 Fondations) | R1 « Instance AaaS déployable en 1 commande (Docker + Supabase RLS) sur VPS » | `SELECT count(*) FROM instances WHERE status='live' >= 1` | Objectif : ≥1 instance live · Entrées : spec R1 MANIFEST · Sortie : `instances.status='live'` · Procédure : déployeur 1 cmd · Cadence : mensuel · Notes : RLS Supabase |
| **C1-R2** (M2 Fondations) | R2 « Pipeline : 100 coachs contactés, 10 démos, 3 signés » | `SELECT count(*) FROM subscriptions WHERE mrr>=1000 >= 3` | Objectif : 3 subs MRR≥1000 · Entrées : segment ICP Coach premium ($7.5-25K, ADR-NEXUS-NICHE-001 RATIFIED) · Sortie : deltas `outreach_log`/`subscriptions` · Procédure : pipeline AAARR Superman/GotG · Cadence : mensuel · Notes : spending 90% ciblé C7 |
| **C1-R3** (M3 Fondations) | R3 « Onboarding automatisé + facturation récurrente sans intervention » | `SELECT sum(mrr) FROM subscriptions WHERE status='active' >= 10000` | Objectif : sum MRR ≥10K · Entrées : clients signés R2 · Sortie : `daily_cash` solde ≥2 mois burn (C5) · Procédure : onboarding Flash/Avengers · Cadence : mensuel · Notes : zéro intervention owner |

**Runbook transverse obligatoire** : `_doctrine/forecast.md` (INTEG C3) — Summers écrit chaque lundi : `MRR prévu J+28 + pipeline prévu`. Erreur >50% = signal re-scope, pas jugement.

**Memory files C1 associés** : `memory_product_flash.md` · `memory_growth_superman.md` · `memory_ops_batman.md` (les 3 domaines gate-PASS W40 M4) + dormant `memory_legal_aquaman.md` · `memory_finance_wonderwoman.md` (déclencheur d'activation : 1er contrat coach signé).

---

### 3. Domaines B2 gate-actifs (déduit W40 M4 + INTEG C8)

| B2 | Squad B3 | Triptyque | Mission (W40 §2) | Gate W4 | Statut Run #1 |
|---|---|---|---|---|---|
| **Flash Product** | Avengers | T1 Build | Agency as a Service (le produit EST l'agence agentique livrable) | **PASS** | ACTIF (Ownerbook R2 ci-dessus) |
| **Superman Growth** | GotG | T2 Value | AAARR (Awareness→Acquisition→Activation→Revenue→Referral) | **PASS** | ACTIF (Ownerbook R2 ci-dessus) |
| **Batman Ops** | Fantastic 4 | T1 Build | SOP & Skills (chaque process = un SOP, chaque SOP répété = un skill) | **PASS** | ACTIF (soutien ops R1+R2) |
| JohnJones Sales | Illuminati | T2 Value | 100M Offers (Hormozi) | CONDITIONAL | À activer R2 W2 |
| WonderWoman Finance | Thunderbolts | T2 Value | 1-Person / 1-Billion Company | DORMANT (déclencheur : 1er MRR entrant) | Pas de scrums tant que R2 < 1 sub |
| Cyborg R&D | Kang Dynasty | T3 Foundation | Veille externe structurée (YouTube → `/youtube-to-B1filter` → Last30days) | CONDITIONAL | 1 sweep mensuel max ≤3 améliorations (W40 M6) |
| Aquaman Legal | Eternals | T3 Foundation | 365 Conformité par Conception (AI-Act Pilier 5 audité 2026-07-15) | DORMANT (déclencheur : 1er contrat coach signé) | En attente |
| GreenLantern RH | X-Men | T1 Build | RH Agentique (recruter/former des agents autant que des humains) | PASS (matrice RH Goal-Keeper

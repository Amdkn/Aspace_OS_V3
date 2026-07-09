# ============================================================================
# Symphony /loop B1 SOLARIS — DRAFT — Pilot AaaS Solaris (Book + Saru)
# ----------------------------------------------------------------------------
# Statut    : Shadow A0 — DRAFT — hors-canon SDD, hors-Airlock (veto 90j respecté)
# Date      : 2026-06-23 · Auteur : Claude Code (A0 jumeau) sur intention A0.
# Hérite    : ADR-L2-AAAS-001 (AaaS 3 Variants) +
#             concept_l2_fractal_b1b2b3 (B1=WHY/WHERE · B2=WHAT/gate · B3=HOW/proof) +
#             Fable × Auto-Research (4-step loop: Capture→Process→Persist→Loop) +
#             /loop vs /routine doctrine (2026-06-23 : /loop=Business OS, /routine=Life OS)
# ----------------------------------------------------------------------------
# ⚠ NE PAS ACTIVER avant levée du veto 90j + accord A0 explicite.
# ⚠ /loop ≠ /routine : /loop = Business OS exploration itérative (Karpathy-style,
#   frugalité MiniMax 2.7) ; /routine = Life OS déterministe récurrent (harness planifié).
# ⚠ Frontière inchangée : Symphony lit, l'agent écrit. Pas d'auto-création de records.
# ============================================================================

## 1. Pourquoi B1 SOLARIS d'abord

Solaris AaaS = **1er variant canoniquement ACTIF** des 3 AaaS (Solaris/Nexus/Orbiter),
car **Life-OS-2026** (`https://life-os-2026-liart.vercel.app/`) tourne déjà en prod
(deploy `dpl_88Mguo2imTBktN6JjE3YcxZopZ2U`, SHA `b933e4e41849a323c63504e2ecea36b71c8759e5`,
12WY Q3 2026 cycle 06/15 → 09/07). Solaris est l'endroit où **l'intent A0 rencontre la
mesure réelle** (revenus Airtable + runway Supabase). C'est le point d'entrée frugal
du loop Business OS.

> **Trace canon** : `wiki/hand_offs/handoff_life_os_deploy_v1_0_2026-06-17.md` +
> `wiki/hand_offs/handoff_life_os_apps_seeded_2026-06-17.md`.

## 2. Routing B1 / B2 / B3 (matrice D6)

```
A0 (intentions, méta-chat jumeau)
   │  émet intention business
   ▼
A1 Beth (Ikigai Lock, gatekeeper L1)
   │  Ikigai verdict : GO / NO-GO / DRIFT
   ▼
A2 Discovery Zora (Life Wheel, LD01-LD08 domains)
   │  H3 horizon scan : LD01 Business sector current vs target
   ▼
A3 Saru (LD02 Finance, H3 quarterly runway captain)
   │  capitaine exécutif Solaris : Book (LD01 H1) + Saru (LD02 H3)
   ▼
SOLARIS AaaS — B1 Book (WHY/WHERE) + B2 Saru (WHAT/gate) + B3 squad (HOW/proof)
   │  Net: weekly P&L pulse (Book H1) + quarterly runway review (Saru H3)
   ▼
Plane issue append (12WY Rock L2 weekly scorecard)
   │
   ▼
Notion decision log (AGO-DECISION-DB) + A0 weekly outbox (D10)
```

**Distinction fractal L2 ↔ L1** :
- **Macro** (perpétuel) : `02_Areas_Spock/J01_Jerry_Prime_LD01_Business/` — doctrine Solaris.
- **Micro** (par cycle) : `01_Projects_Picard/Life-OS-2026/` — calibre Solaris (actif).
- Nexus OMK = calibre différent (par projet), Orbiter ABC = autre calibre.

## 3. Les 4 étapes du /loop (Fable × Auto-Research)

### 3.1 CAPTURE (lecture seule, frugal)

Sources **read-only** :
- **Airtable 🦸 Leads & Audits** : `appmWf5Xm7w9Ae0ky` / table `tblj0xmSXLH4Xsd8c`
  (leads inbound, status, conversion rate — la matière première Book H1).
- **Airtable 💸 Sales Pipeline** : à découvrir via `meta/bases`/`meta/tables` au 1er run.
- **Supabase Life OS `fw_life_wheel`** : `current` vs `target` score LD01_LD02 (8 LDxx sectors).
- **Supabase Life OS `fw_12wy`** : Rocks L2 tagged (cycle 12WY Q3 2026, semaines W1-W12).
- **Plane project `79df867c-06b5-4e61-b3f1-68aa886c39a3`** : tickets actifs, status, cycle tags.

Pas d'écriture à ce stade. Si capture échoue (réseau, 5xx, schema drift) → **stop, log,
escalade Donna DLQ** (cf. `SUPERVISION.symphony-hermes.draft.md` §4.1).

### 3.2 PROCESS (compute, sans écrire)

- **A3 Saru (LD02 H3)** calcule : runway delta, burn rate weekly, MRR trend.
- **A3 Book (LD01 H1)** calcule : weekly revenue, lead→conversion funnel delta,
  nouveaux leads (🦸 Leads & Audits), 12WY Rocks completed this week.
- **A3 Saru check Sobriété** : tokens consommés ≤ budget cycle (frugalité MiniMax 2.7).

Output = **Plan d'observation** (in-memory, jamais persisté en auto).

### 3.3 PERSIST (write, gated)

Écritures **explicites et tracées** :
- **Plane issue append** : commentaire hebdo sur Rock L2 actif
  (idempotent, format `W{n} Book+Saru weekly pulse : {chiffres}`).
- **Notion AGO-DECISION-DB** : ligne décision si Saru détecte drift > seuil (≥10%).
- **Wiki handoff** : `wiki/hand_offs/loop_pulse_<YYYY-WW>.md` si décision structurante.

**Pas d'auto-création de records** — la doctrine "Symphony lit, l'agent écrit" tient.
L'agent (Saru/Book) écrit, après **gate B2** (vérification DoD=JBD par Beth A1).

### 3.4 LOOP (re-arm)

- Cron `*/7 days` (H1 horizon per Book doctrine), avec **jitter ±90 min**
  (évite pic fixe 09:00 — D6 lesson anti-stampede herd).
- ScheduleWakeup fallback si cron cassé.
- Si 3 loops consécutifs sans drift détecté → escalate Beth (peut-être sur-cadence).
- Si 3 loops consécutifs avec drift > 20% → escalate Donna DLQ → A0 (D10 outbox).

## 4. SLA triade (SDD-009, par loop)

| Dimension | Cible | Gate |
|---|---|---|
| **Temporel** | ≤ 5 min par cycle (capture→persist) | timeout hard 10 min, kill + Donna |
| **Financier** | ≤ 200 tokens MiniMax 2.7 / cycle (≈ $0.001) | budget hebdo $0.05 ; alerte si > 70% |
| **Qualitatif** | ≥ 95% champs calculés non-NaN | si > 5% NaN → fail-fast + Donna |

## 5. Ce que ce /loop N'EST PAS (frontières)

- ❌ Pas de bi-sync Airtable ↔ Supabase (interdit base spec §10.3, cf. `BRIDGE.rock-l2-to-growth.draft.md` §4).
- ❌ Pas d'auto-création de Rock depuis un lead, ni de lead depuis un Rock.
- ❌ Pas de duplication de chiffre : revenue vit dans Airtable, runway dans Supabase.
- ❌ Pas de notification A0 sauf drift > seuil (D10 outbox = exception, pas norme).
- ❌ Pas de premium Anthropic sauf gate Beth (Rick A1 Sobriété différé Q4 2026).

## 6. Activation (différée, A0-gated)

Pré-requis avant toute activation :
1. **Levée du veto 90j** Symphony (cf. `SUPERVISION.symphony-hermes.draft.md` §0).
2. **Sign-off A0** sur ce draft en chat (verbatim "GO loop B1 Solaris").
3. **Airtable MCP + ClickUp MCP câblés et fonctionnels** post-CC-restart.
   A0 doit installer les packages npm (`airtable-mcp-server`, `clickup-mcp-server`)
   et redémarrer CC pour activer (D6 #4 tool registry STATIC).
4. **Tests 1 semaine en dry-run read-only** (Phase 0 — observe only).
5. **Validation 3 semaines d'usage continu** (critère MUSE SDD-008) avant canonisation.

Tant que ces 5 conditions ne sont pas réunies, ce fichier reste une **carte**, pas un connecteur.

## 7. Premier run cible (post-activation)

W3 / 2026-06-23 → 2026-06-29 : capture initiale = state actuel Life-OS-2026 +
Airtable amd account + Supabase fw_life_wheel. Baseline = T0. Pas d'écriture.

W4 / 2026-06-30 → 2026-07-06 : premier cycle PROCESS (Saru + Book compute).
Premier append Plane (commentaire non-décisionnel sur Rock L2).

W5 / 2026-07-07 : revue mi-cycle, validation A0, décision continue/adjust/kill.

---

*Loop draft — Shadow A0 — /loop B1 Solaris AaaS — 2026-06-23 — hors-canon, ne pas activer.*
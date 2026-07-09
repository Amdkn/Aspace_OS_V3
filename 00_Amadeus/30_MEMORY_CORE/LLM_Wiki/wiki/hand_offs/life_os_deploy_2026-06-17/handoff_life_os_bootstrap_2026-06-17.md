---
source: LLM_Wiki_A0
date: 2026-06-17
type: handoff
domain: Life_OS / L1 — Tech infrastructure
tags: [#handoff #life_os #bootstrap #supabase #A0_HITL]
---

# Handoff — Life OS Bootstrap V1.0 (2026-06-17)

> **Statut** : 16 tables SQL prêtes. **BLOQUÉ** sur anon key 401.
> **A0 HITL** : choisir entre 2 options (clé fresh OU paste manuel SQL Editor).

---

## TL;DR (A0)

| # | Question | Réponse D1 |
|---|----------|------------|
| 1 | Projet Supabase `hjweyhpmrxqsxfbibsnc` est-il vivant ? | **OUI** — Cloudflare Cleveland edge répond, sb-project-ref correct |
| 2 | Pourquoi 401 sur 4 endpoints ? | **Clé anon rotatée** (`UNAUTHORIZED_INVALID_API_KEY`) |
| 3 | Schéma canon 16 tables prêt ? | **OUI** — `life_os_bootstrap_v1_0.sql` (295 lignes, paste-ready) |
| 4 | DDL de base existe dans le repo cloné ? | **NON** — root cause confirmée (cf §D6) |
| 5 | Action immédiate requise A0 ? | **OUI** — choisir option A ou B (§H) |

---

## D1 — Receipts schema canon

### Source de vérité (3 fichiers D1 lus)

| Fichier | Lignes | Ce qu'il dit |
|---------|--------|--------------|
| `C:\Users\amado\AppData\Local\Temp\life-os-2026-clone\REALITY_MAP.md` | 514 | Modèle canon. L.190 = UNIFIED schema (id, title, metrics, type, updated_at, created_at). L.178-191 = 16 noms canon. |
| `C:\Users\amado\AppData\Local\Temp\life-os-2026-clone\supabase\schema_migration.sql` | 61 | V1.0 — ajoute user_id + RLS aux 16 tables. L.14-15 = noms V1.0 Vercel. |
| `C:\Users\amado\AppData\Local\Temp\life-os-2026-clone\supabase\memory_migration.sql` | 49 | ADR-003 — assign user_id=admiral après first signup. |

### 16 noms canon (D1 verbatim, schema_migration.sql L.14-15)

```
COUCHE 2 — Domaines de vie (8) :
  ld01_business      (Book / Biz)          — Discovery A3 Book
  ld02_finance       (Saru / Balance)      — Discovery A3 Saru
  ld03_health        (Culber / Hospital)   — Discovery A3 Culber
  ld04_cognition     (Tilly / Mind)        — Discovery A3 Tilly
  ld05_environment   (Stamets / Network)   — Discovery A3 Stamets
  ld06_relationships (Burnham / DEAL)      — Discovery A3 Burnham
  ld07_emotions      (Reno / Maintenance)  — Discovery A3 Reno
  ld08_purpose       (Georgiou / Moat)     — Discovery A3 Georgiou

COUCHE 3 — Frameworks transversaux (6) :
  fw_para            (FolderRoot)
  fw_ikigai          (Target)
  fw_life_wheel      (Compass)
  fw_12wy            (CalendarRange)
  fw_gtd             (Inbox)
  fw_deal            (Zap)

COUCHE 1 — OS Shell + Agents (2) :
  sys_agent_veto
  sys_shell_routing
```

### UNIFIED schema (D1 verbatim, REALITY_MAP.md L.190)

```sql
-- Chaque table contient (identique sur les 16) :
id         uuid          PRIMARY KEY DEFAULT gen_random_uuid()
title      text          NOT NULL    DEFAULT ''
metrics    jsonb                     DEFAULT '{}'::jsonb
type       text
updated_at timestamptz               DEFAULT NOW()
created_at timestamptz               DEFAULT NOW()
```

**D3 nuance** : differentiation framework (PARA / Ikigai / Wheel / 12WY / GTD / DEAL) se fait **côté application** (LD-Router, IndexedDB). Pas de schéma Postgres par framework.

---

## D3 — Nuance : `src/constants.ts` ≠ V1.0 table names

`src/constants.ts` (LD mapping, L.154-163) utilise une **sémantique Discovery A3** :

| Discovery A3 | src/constants.ts | V1.0 table name |
|---|---|---|
| Book | LD01 Business Sector | `ld01_business` |
| Saru | LD02 Finance (Balance) | `ld02_finance` |
| Culber | LD03 Health (Hospital) | `ld03_health` |
| Tilly | LD04 Cognition (Mind) | `ld04_cognition` |
| Stamets | LD05 Social (Network) | `ld05_environment` |
| Burnham | LD06 Family (DEAL) | `ld06_relationships` |
| Reno | LD07 Play (Maintenance) | `ld07_emotions` |
| Georgiou | LD08 Impact (Moat) | `ld08_purpose` |

**Décision** : bootstrap SQL utilise les **V1.0 table names** (source schema_migration.sql), pas les Discovery A3 names. Le mapping sémantique vit dans `src/constants.ts` au runtime.

---

## D6 — Root cause investigation

### RC1 : Aucun DDL de base dans le repo

```
$ Grep "CREATE TABLE" path=C:\Users\amado\AppData\Local\Temp\life-os-2026-clone
→ 1 file : supabase/schema_migration.sql
  (mais c'est RLS only, pas de CREATE TABLE — vérifié ligne par ligne)
```

**Conséquence** : `supabase db push` ne peut rien appliquer (`[db.migrations].schema_paths = []` dans config.toml). `seed.sql` référencé mais absent.

**Fix** : `life_os_bootstrap_v1_0.sql` généré (295 lignes, 16 CREATE TABLE + 16 trigger + 32 index + 1 verify block).

### RC2 : Anon key 401 sur 4 endpoints

| Endpoint | HTTP | sb-error-code | sb-project-ref | sb-gateway-version |
|----------|------|---------------|----------------|---------------------|
| `GET /rest/v1/` | 401 | `UNAUTHORIZED_INVALID_API_KEY` | `hjweyhpmrxqsxfbibsnc` ✅ | `1` ✅ |
| `GET /rest/v1/ld01_business?select=id&limit=1` | 401 | idem | idem | idem |
| `GET /auth/v1/health` | 401 | idem | idem | idem |
| `GET /rest/v1/?apikey=...` (variante 1) | 401 | idem | idem | idem |

**Headers annexes** : `Server: cloudflare` ✅ · `CF-RAY: a0cf6c93df6e250e-CLE` (Cleveland edge = projet **JOIGNABLE**).

**Conclusion D6** : projet **vivant et joignable**, mais la clé anon partagée est **rotatée ou révoquée**. Pas un projet paused.

---

## F — Fichier bootstrap généré

**Path** : `C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki\wiki\hand_offs\life_os_deploy_2026-06-17\life_os_bootstrap_v1_0.sql`

**Stats** : 295 lignes · 16 CREATE TABLE · 16 trigger `set_updated_at` · 32 index (type + created_at DESC) · 1 verify block (DO $$ ... table_count = 16).

**Reprise manuelle recommandée** :

1. Ouvrir Supabase SQL Editor sur `hjweyhpmrxqsxfbibsnc.supabase.co`
2. Coller le contenu de `life_os_bootstrap_v1_0.sql`
3. Run (F5) — vérifier message `✅ Life OS V1.0 bootstrap : 16 tables créées (attendu : 16)`
4. Coller ensuite `supabase/schema_migration.sql` (user_id + RLS + user_profiles + handle_new_user trigger)
5. Après premier signup, coller `supabase/memory_migration.sql` (assign user_id=admiral à toutes les rows)

---

## H — A0 HITL : 2 options

### Option A — Paste new anon key (Test Key Pragma)

Tu colles la nouvelle clé anon (format `eyJ...`) en chat. Je :
1. Set env var `SUPABASE_ANON_KEY_NEW` (User scope Windows)
2. Smoke test : `curl https://hjweyhpmrxqsxfbibsnc.supabase.co/rest/v1/ld01_business?select=id&limit=1 -H "apikey: $env:SUPABASE_ANON_KEY_NEW"`
3. Si 200 → apply le bootstrap SQL via `mcp__supabase__apply_migration` programmatically
4. Capture preuve (count tables = 16) et log dans ce handoff

**Coût** : 2-3 min · 1 HITL (le paste) · 0 erreur manuelle.

### Option B — Paste manuel SQL Editor (no API)

Tu ouvres Supabase SQL Editor, colles `life_os_bootstrap_v1_0.sql`, F5. Tu me colles ici :
- Le message `✅ Life OS V1.0 bootstrap : 16 tables créées` (si succès)
- OU l'erreur exacte (si échec)

Je continue avec `schema_migration.sql` (idem) puis `memory_migration.sql` (après first signup).

**Coût** : 5-10 min · 3 HITL (3 paste) · risque typo plus haut.

### Recommandation (D7 cost-of-escalation)

→ **Option B** : tu as déjà l'UI ouverte, le SQL est petit (295 lignes), aucun risque de pollution du log par des vraies clés. L'option A est utile seulement si tu veux scripter le déploiement complet (CD/CI) plus tard.

---

## Post-bootstrap (séquentiel, manuel)

| Étape | Quand | Source | Notes |
|-------|-------|--------|-------|
| 1. Bootstrap 16 tables | **maintenant** | `life_os_bootstrap_v1_0.sql` (paste-ready) | Vérifier msg 16 tables |
| 2. Auth + RLS | après étape 1 | `supabase/schema_migration.sql` (61 lignes) | Crée user_profiles + handle_new_user() |
| 3. Memory continuity | après premier signup | `supabase/memory_migration.sql` (49 lignes) | user_id=admiral assigné à toutes rows |
| 4. Test e2e | après étape 3 | Browser → sign up → CRUD sur ld01_business | D1 receipt de bout en bout |

---

## Anti-pattern guard (D1-D8)

- **D1** : 6 receipts gathered this turn (3 fichiers canon lus, 4 endpoints testés, 295 lignes SQL générées, 2 mapping tables, 4 headers HTTP)
- **D2** : 2 sources canon lues AVANT génération SQL (REALITY_MAP + schema_migration)
- **D3** : 1 nuance ancrée (constants.ts vs V1.0 table names — pas de confusion)
- **D4** : handoff en append-only, ancien schema_migration.sql untouched
- **D5** : verify block dans le SQL (`IF table_count != 16 THEN RAISE EXCEPTION`)
- **D6** : 2 root causes (no DDL + key 401) avec sources identifiées
- **D7** : 2 options offertes à A0, recommandation non-escalante (Option B)
- **D8** : pas de modification de fichiers legacy ; juste création handoff + bootstrap SQL

---

## Related

- Bootstrap SQL : `life_os_bootstrap_v1_0.sql` (ce dossier)
- schema_migration.sql : `C:\Users\amado\AppData\Local\Temp\life-os-2026-clone\supabase\schema_migration.sql`
- memory_migration.sql : `C:\Users\amado\AppData\Local\Temp\life-os-2026-clone\supabase\memory_migration.sql`
- REALITY_MAP.md : `C:\Users\amado\AppData\Local\Temp\life-os-2026-clone\REALITY_MAP.md`
- Prior handoff: `wiki/hand_offs/handoff_business_os_resumption_2026-06-16.md`
- D6 doctrine : `_SPECS/ADR/ADR-META-001_anti-paresse-verify-before-assert.md`

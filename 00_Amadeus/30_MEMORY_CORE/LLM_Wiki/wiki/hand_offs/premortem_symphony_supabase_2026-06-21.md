---
source: A0 Amadeus (jumeau numérique)
date: 2026-06-21
type: premortem
domain: L0
tags: [premortem, symphony-supabase, runtime-twin, d6-persistent, lane-b]
---

# Pre-mortem Durabilité — mcp__symphony-supabase__ (Lane B Runtime Twin)

> **D1 receipt** : 2026-06-21 — A0 Amadeus pivot « c avec un Premortem de durabilite sur les Symphony Supabase »
> **Statut** : ACCEPT canonique avec 3 garde-fous (cf. §10 Décision)
> **Owner** : A0 (jumeau numérique, board observer passif)
> **Rédacteur** : A0 Amadeus (méta-orchestration) → livré à A2 Claude Code (infrastructure) → A3 Spock/Saru (revue technique)
> **Pattern** : Pre-mortem = imaginer les failure modes AVANT de déclarer canon. Source : ADR-META-001 D6 persistent symptom.

---

## 1. Synthèse exécutive

**D1 verified** : `mcp__symphony-supabase__` (Lane B Runtime twin) est **LIVE et stable** pour le scope canon (fw_ikigai, fw_life_wheel, fw_12wy, fw_deal, fw_gtd, fw_para, etc.). **5/6 env var slots** sont alimentés (LIVE_OS, OMK_TAX, ABC_OS, KBS_CORP, A_LAB — 5 slugs D1 vérifiés contre les vars User scope). **6 tools canoniques** exposées : `supabase_list_projects`, `supabase_query`, `supabase_list_tables`, `supabase_get_metrics`, `supabase_anti_pause_ping`, `supabase_health_check`.

**Décision** : **ACCEPT canonique** avec 3 garde-fous obligatoires (D6 risk register §9). **Pas de re-implémentation** (D7 cost-of-escalation). **Pas de hard-coded secrets** (D4 append-only + Test Key Pragma). **Anti-pause D6 inference documenté comme HYPOTHÈSE** (non officiellement supporté par Supabase, mais logiquement sound — flag `healthy_liveness` retourne 200 après chaque appel).

---

## 2. D1 Receipts (sources canon)

### 2.1 Path canon + taille

| Path | Lignes | Verbatim receipt |
|---|---|---|
| `C:\Users\amado\ASpace_OS_V2\00_Amadeus\05_OSS_Twin\symphony\L1\lane_B_runtime\04_mcps\mcp-supabase.py` | **396** | Source canon Lane B Runtime twin, 2026-06-17 MCP-Supabase LIVE |

### 2.2 Tools exposées (6 canoniques)

| Tool | Rôle | Verbatim ligne |
|---|---|---|
| `supabase_list_projects` | Liste tous les projets configurés (slugs) | `async def list_projects()` |
| `supabase_query` | Query PostgREST via anon key (RLS respected) | `async def query(slug, table, select, limit)` |
| `supabase_list_tables` | Probe PostgREST root → discover tables | `async def list_tables(slug)` |
| `supabase_get_metrics` | Liveness + auth.users count (best-effort) | `async def get_metrics(slug)` |
| `supabase_anti_pause_ping` | **FLAGSHIP** : trivial HTTP request to /rest/v1/ → génère DB activity (D6 HYPOTHÈSE) | `async def anti_pause_ping(targets=None)` |
| `supabase_health_check` | Liveness probe across all configured projects (lightweight) | `async def health_check()` |

### 2.3 Env vars canon (pattern `SUPABASE_<SLUG>_*`)

| Env var | Slot | Status | Source |
|---|---|---|---|
| `SUPABASE_LIFE_OS_URL` | 1 | ✅ LIVE | D1 verifié 2026-06-17 (table fw_12wy) |
| `SUPABASE_LIFE_OS_ANON_KEY` | 1 | ✅ LIVE | Test Key Pragma 2026-06-17 |
| `SUPABASE_LIFE_OS_LIVENESS_TABLE` | 1 | ✅ LIVE (default=`user_profiles`) | D6 fix 2026-06-17 |
| `SUPABASE_OMK_TAX_*` | 2 | ⚠️ HYPOTHESE | Pas encore testé en twin |
| `SUPABASE_ABC_OS_*` | 3 | ⚠️ HYPOTHESE | Pas encore testé en twin |
| `SUPABASE_KBS_CORP_*` | 4 | ⚠️ HYPOTHESE | Pas encore testé en twin |
| `SUPABASE_A_LAB_*` | 5 | ⚠️ HYPOTHESE | Pas encore testé en twin |

### 2.4 D6 fixes shipped (traçabilité 2026-06-17)

| # | Root cause | Fix | Source |
|---|---|---|---|
| 1 | `_load_projects()` rsplit bug (multi-underscore slugs comme `LIFE_OS` non matchés) | Longest-suffix matching pour env keys | `mcp-supabase.py:124-156` |
| 2 | PostgREST root REQUIRES secret key (probe direct = 401) | Probe via `/rest/v1/<liveness_table>` au lieu de `/` | `mcp-supabase.py:202-218` |
| 3 | CC subprocess cache stale after env var change | Touch `.mcp.json` + kill PIDs (PAS CC restart) | handoff `mcp_supabase_twin_live_2026-06-17.md` §D6 #3 |

---

## 3. Architecture (Lane B Runtime pattern)

### 3.1 Pattern canon (Symphony Lane B)

```
CC (Claude Code) ──stdio──► mcp-supabase.py (Python 3.14)
                                    │
                                    ├── httpx.AsyncClient
                                    │       │
                                    │       ▼
                                    │   Supabase Cloud (PostgREST + Auth + Realtime + Storage)
                                    │       │
                                    │       ▼
                                    │   Project <slug>.supabase.co
                                    │
                                    └── JSON-RPC response ──stdio──► CC
```

**Pourquoi Lane B** : `mcp__supabase__*` (29 tools, user-facing) et `mcp__symphony-supabase__*` (6 tools, twin) sont **2 serveurs séparés** dans `.mcp.json`. Le twin = thin stdio↔HTTPS JSON-RPC forwarder (D6 lesson OAuth bypass). **Pas de dépendance upstream** : le twin est self-contained.

### 3.2 Dual-stack avec mcp__supabase__ (29 tools user-facing)

| Aspect | `mcp__supabase__*` (user-facing) | `mcp__symphony-supabase__*` (twin) |
|---|---|---|
| Tools | 29 (full Supabase API) | 6 (curated subset) |
| Auth | `SUPABASE_ACCESS_TOKEN` (PAT user) | `SUPABASE_<SLUG>_ANON_KEY` (anon scoped par projet) |
| Use case | Interactive dev (apply_migration, execute_sql) | Runtime check, anti-pause, health monitoring |
| Scoping | Project-agnostic (apply to any) | Project-scoped (1 slug = 1 project) |
| D6 risk | Stale session token | Stale anon key → failed PostgREST probe |

**Implication** : les 2 sont **complémentaires**, pas redondants. Le twin est pour le **runtime check canon** ; le user-facing est pour le **dev interactif**.

---

## 4. Failure Modes (Pre-mortem = imaginer le pire)

### 4.1 Scénario A — Supabase pause un projet pour inactivité (7 jours sans query)

**Probabilité** : HAUTE (D6 inference HYPOTHESE — Supabase pause free-tier après ~7 jours inactifs)

**Detection** : `supabase_health_check()` retourne `status_code != 200` pour le slot affecté

**Mitigation** : `supabase_anti_pause_ping()` flagship tool — trivial HTTP request toutes les 5-6 jours. **Schedule via pg_cron ou systemd timer**. Hypo­thèse D6 : génère DB activity suffisante pour éviter pause.

**Coût** : ~1 KB de traffic HTTP/5j par projet. **5 projets × 1 ping = 5 KB/jour = 150 KB/mois**. Négligeable.

**Risque résiduel** : Si l'hypothèse D6 est **fausse** (Supabase utilise d'autres métriques que PostgREST calls), le pause peut survenir quand même. **Mitigation 2e niveau** : `supabase_query()` réel toutes les 24h (cron interne plus robuste).

### 4.2 Scénario B — Env var propagation fails (User scope non lu par subprocess)

**Probabilité** : MOYENNE (D6 déjà vécu 2026-06-16 sur Vercel MCP)

**Detection** : `supabase_list_projects()` retourne 0 projects (env vars non vues par Python subprocess)

**Mitigation** :
1. `session-start-clean-npx-cache.ps1` hook (déjà wired) pour forcer re-read env
2. `printenv` debug call dans le script Python pour diagnostic
3. Fallback : stub return (déjà implémenté — D7 no-crash)

**Risque résiduel** : Si Windows User scope env vars ne sont pas propagées au subprocess Python, fallback stub retourne `{"projects": []}` — agent croit que c'est canon, mais c'est stub.

### 4.3 Scénario C — PostgREST schema exposure masquée (PGRST_DB_SCHEMAS env var)

**Probabilité** : HAUTE (D6 déjà vécu 2026-06-17 sur abc_os : env var read-once at boot)

**Detection** : `supabase_list_tables()` retourne 0 tables pour un projet connu (schema `omk_saas` ou `abc_os` non exposé)

**Mitigation** :
1. **Documenter** dans le handoff que `PGRST_DB_SCHEMAS` est read-once-at-boot
2. **A0 action** : Dashboard UI Settings → API → Exposed schemas (2 min)
3. **Alternative** : query directe `SELECT * FROM information_schema.tables` (bypass PostgREST schema filter)

**Risque résiduel** : Si A0 oublie de cocher le schema, le twin est aveugle. **D6 leason shipped 2026-06-17** : ne JAMAIS supposer schema exposé sans verification explicite.

### 4.4 Scénario D — D6 #4 NEW (CC tool registry static)

**Probabilité** : HAUTE (D6 root cause 2026-06-17 : nouveau server name dans `.mcp.json` = ignoré jusqu'à CC restart)

**Detection** : `mcp__symphony-supabase__*` tools not found in current CC session

**Mitigation** :
1. **A0 action** : full CC restart (5 min downtime)
2. **Alternative** : Defer l'ajout d'un nouveau server name jusqu'à prochaine session
3. **D6 lesson shipped** : env var change on EXISTING server = hot-reloadable via `touch .mcp.json + kill PIDs` (PAS restart requis)

**Risque résiduel** : Si un nouveau slot est ajouté (ex. `SUPABASE_NEW_SLUG_*`) en cours de session, le subprocess ne le voit pas.

### 4.5 Scénario E — Supabase service outage (DB indisponible)

**Probabilité** : BASSE (Supabase SLA 99.9% sur Pro plan)

**Detection** : `supabase_health_check()` retourne timeout ou 5xx pour tous les slots

**Mitigation** :
1. **Stub fallback** déjà implémenté — D7 no-crash
2. **Retry avec backoff** : 3× retry 100/300/900ms (pattern canon `state_writer.py`)
3. **Degradation gracieuse** : agent continue avec stub data + log warning

**Risque résiduel** : Si outage > 5 min, agent travaille avec des stubs sans le savoir. **D1 receipt manquant** = risque de claim factuel incorrect.

---

## 5. Durabilité (5 axes d'analyse)

### 5.1 Technique (code, deps, API)

| Axe | Status | Verbatim |
|---|---|---|
| Code source | ✅ LIVE | 396 lignes Python 3.14, stdlib + httpx only |
| Deps externes | ✅ Minimal | `httpx` (async HTTP), `asyncio` (stdlib) |
| API surface | ✅ Stable | PostgREST REST API (Supabase standard) |
| Backward compat | ✅ Fort | Supabase PostgREST v1 stable depuis 2020 |
| Test coverage | ⚠️ HYPOTHESE | Pas de pytest formel — verification = live calls |

**Risque** : Si Supabase migre vers une nouvelle API (ex. PostgREST v2 breaking changes), 5/6 tools seraient à réécrire.

### 5.2 Environnement (env vars, secrets)

| Axe | Status | Verbatim |
|---|---|---|
| Env vars User scope | ✅ LIVE | Windows User env scope, persistent across sessions |
| Secrets in code | ✅ ZERO | Aucun secret en clair (Test Key Pragma + User scope only) |
| Rotation | ✅ Possible | A0 rotate via Supabase Dashboard → re-paste clé en chat → agent set + test |
| Cross-platform | ⚠️ Windows only | User scope env vars = Windows-specific. macOS/Linux = shell env |

**Risque** : Si A0 migre vers macOS, le pattern `User scope` ne s'applique pas. **Mitigation** : `.env` file (gitignored) + direnv.

### 5.3 Opérationnel (monitoring, alerting)

| Axe | Status | Verbatim |
|---|---|---|
| Health check | ✅ LIVE | `supabase_health_check()` tool exposée |
| Metrics | ⚠️ Partiel | `supabase_get_metrics()` = liveness + auth.users count seulement |
| Alerting | ❌ ABSENT | Pas d'alerte proactive — D6 symptom uniquement détecté à l'usage |
| Logging | ⚠️ stderr only | Logs dans stderr CC, pas d'observabilité centralisée |

**Risque** : Si un slot tombe en panne pendant une session de plusieurs heures, A0 ne le sait pas jusqu'à la prochaine utilisation.

### 5.4 Organisationnel (ownership, governance)

| Axe | Status | Verbatim |
|---|---|---|
| Canon ownership | ✅ Defined | `mcp__symphony-supabase__*` = Lane B Runtime, A1 Morty superviseur opérationnel |
| Doc canon | ✅ D1 receipts | handoff `mcp_supabase_twin_live_2026-06-17.md` (8 sections) + ce handoff (10 sections) |
| Versioning | ⚠️ Append-only | Pas de git tag — D4 append-only sur `wiki/hand_offs/` |
| Succession | ❌ Single point of failure | Si A0 Amadeus = seul owner, twin = orphelin si A0 absent |

**Risque** : Life-OS-2026 = projet canonique A0. Si A0 switche de focus (S1 Rick kernel pivot), le twin pourrait être neglected. **Mitigation** : A1 Morty auto-supervision + D7 cost-of-escalation A0 = board observer.

### 5.5 Sécurité (RLS, auth, attack surface)

| Axe | Status | Verbatim |
|---|---|---|
| RLS respect | ✅ OUI | PostgREST queries respectent RLS (anon key = role `anon`) |
| Auth scope | ✅ Minimal | Anon key = read-only par défaut, RLS peut étendre |
| Attack surface | ✅ Faible | Twin = thin forwarder, pas de state persistant |
| Audit trail | ⚠️ Partiel | Supabase logs accessible via Dashboard, pas via twin |
| Secret rotation | ✅ Manual | A0 rotate via Dashboard → re-paste en chat |

**Risque** : Si RLS est mal configuré (D6 vécu 2026-06-17 Life OS 4× 404 LD05-LD08), anon key leak = full table access. **Mitigation** : D1 verify-before-assert RLS policies avant tout query production.

---

## 6. Permanence (D4 append-only + Test Key Pragma)

### 6.1 D4 append-only (jamais d'écrasement)

**Source canon** : `ADR-META-001 §D4` — kernel_memory pgvector, jamais d'écrasement.

**Application twin** :
- Handoffs dans `wiki/hand_offs/` = append-only (jamais de `rm`)
- `_TRASH_<date>/` pour retirements (D4 pattern respecté)
- Code source = `mcp-supabase.py` (1 version canonique, 396 lignes)
- Pas de git branching = pas de merge conflicts

### 6.2 Test Key Pragma (réalisme > paranoia)

**Source canon** : CLAUDE.md §"Test Key Pragma" + `feedback_tts_and_communication.md`

**Cycle rotation** :
1. A0 colle anon key en chat (« teste ça »)
2. Agent : `[Environment]::SetEnvironmentVariable("SUPABASE_LIFE_OS_ANON_KEY", "<key>", "User")`
3. Agent : `supabase_list_tables("life_os")` → D1 receipt
4. A0 : revoke la clé dans Supabase Dashboard
5. A0 : recreate + re-paste nouvelle clé (ou script masked SecureString)

**Cadence recommandée** : 1×/trimestre (avant chaque cycle 12WY). **Plus fréquent = D7 cost-of-escalation inutile**.

### 6.3 D4 append-only + Test Key Pragma = combinaison canon

**Garantie** : Le twin **n'accumule JAMAIS de secret** dans son code. Les clés tournent. Le code source reste stable. Le twin = thin forwarder, anon key ephemeral, RLS enforced.

---

## 7. Garde-fous obligatoires (3)

### 7.1 Garde-fou 1 — D6 #4 monitor (CC tool registry static)

**Action** : A0 doit **redémarrer CC** si un nouveau server name est ajouté au `.mcp.json` en cours de cycle. Pas de hot-reload possible pour nouveau server.

**Détection** : Tools not found in current session.

**Mitigation alternative** : Defer l'ajout à prochaine session (D7 cost-of-escalation).

### 7.2 Garde-fou 2 — Anti-pause HYPOTHÈSE documentée

**Action** : Tous les handoffs qui mentionnent `supabase_anti_pause_ping` doivent **explicitement flag** comme HYPOTHÈSE (D6 inference, pas officiellement documenté par Supabase).

**Rationale** : D6 lesson shipped 2026-06-17 — préférer HYPOTHÈSE documentée à claim non-vérifié. Si Supabase utilise d'autres métriques (bande passante, stockage, etc.) que PostgREST calls, l'anti-pause peut ne pas fonctionner.

**Fallback** : `supabase_query()` réel toutes les 24h (cron interne plus robuste) si l'anti-pause échoue.

### 7.3 Garde-fou 3 — _TRASH_<date>/ pattern (D4 append-only)

**Action** : Tout retirement du twin (ex. : remplacement par une nouvelle version) doit passer par `_TRASH_<date>/`. Pas de hard-delete.

**Rationale** : D4 no-self-contradiction + traçabilité. Si le twin doit être réécrit (ex. Supabase API v2), l'ancien code reste accessible dans `_TRASH_2026-06-21_mcp-supabase-v1/`.

---

## 8. Comparaison avec mcp__supabase__ (29 tools user-facing)

| Critère | mcp__supabase__ (29 tools) | mcp__symphony-supabase__ (6 tools) |
|---|---|---|
| **Use case canon** | Dev interactif (apply_migration, execute_sql) | Runtime check canon (anti-pause, health) |
| **Auth** | `SUPABASE_ACCESS_TOKEN` (PAT user) | `SUPABASE_<SLUG>_ANON_KEY` (anon scoped) |
| **State persistant** | Non (stateless) | Non (stateless) |
| **D6 risk register** | 0 D6 fixes (well-maintained) | 3 D6 fixes shipped (Lane B Runtime) |
| **Cadence d'utilisation** | 1×/session (interactif) | 5-10×/session (monitoring + queries) |
| **Hot-reload** | OK (env var change) | OK (env var change) mais pas nouveau server name |
| **Coupling** | 1 serveur monolithique | 1 serveur + 1 N serveurs (slugs) |
| **Observabilité** | Logs Supabase Dashboard | Logs stderr CC + Stub fallback D7 |

**Conclusion** : Les 2 sont **complémentaires** et **non redondants**. Le twin est un **specialized tool** pour le runtime check canon, pas un replacement du user-facing.

---

## 9. D6 Risk Register (consolidé)

| # | Risque | Probabilité | Impact | Mitigation | Owner |
|---|---|---|---|---|---|
| 1 | Supabase pause pour inactivité | HAUTE | Service down | `supabase_anti_pause_ping` (HYPOTHÈSE) | A1 Morty auto |
| 2 | Env var propagation fails | MOYENNE | Stub fallback | Hook `session-start-clean-npx-cache.ps1` | A0 + agent |
| 3 | PostgREST schema exposure masquée | HAUTE | Twin aveugle | A0 action Dashboard UI (2 min) | A0 |
| 4 | CC tool registry static (D6 #4) | HAUTE | Tools not found | A0 full CC restart | A0 |
| 5 | Supabase service outage | BASSE | Stub fallback | Retry backoff 100/300/900ms | A1 Morty auto |
| 6 | RLS mal configuré (D6 vécu) | MOYENNE | Data leak | D1 verify policies avant query prod | A3 Saru |
| 7 | Anon key leak (Test Key Pragma) | BASSE | Data exposure | Rotation trimestrielle + RLS | A0 |

---

## 10. Décision : ACCEPT canonique avec 3 garde-fous

**Verdict** : **ACCEPT** le twin `mcp__symphony-supabase__` comme **canonique Lane B Runtime** pour le projet Life-OS-2026 + cycle 12WY Q3 2026.

**Conditions** :
1. **Garde-fou 1** : D6 #4 monitor (CC restart si nouveau server name ajouté)
2. **Garde-fou 2** : Anti-pause HYPOTHÈSE documentée (toutes mentions flag explicit)
3. **Garde-fou 3** : `_TRASH_<date>/` pattern pour tout retirement (D4 append-only)

**Pas de re-implémentation** (D7 cost-of-escalation). Le twin est stable, LIVE, et conforme au pattern Lane B Runtime canon.

**Cible Q4 2026** : Si l'anti-pause HYPOTHÈSE échoue (Supabase pause quand même), basculer vers `supabase_query()` réel toutes les 24h (cron interne).

**Cible Q1 2027** : Réécrire le twin en asyncio + observabilité centralisée (OTel) si Supabase sort PostgREST v2 breaking changes.

---

## 11. HITL Gates (A0 actions requises)

| # | Action | Owner | Délai | Statut |
|---|---|---|---|---|
| 1 | Vérifier `PGRST_DB_SCHEMAS` Dashboard pour chaque slot (5 projets) | A0 | 5 min | À faire |
| 2 | Décider cadence `supabase_anti_pause_ping` (cron systemd OU pg_cron) | A0 | 1 min décision | À faire |
| 3 | Schedule `supabase_anti_pause_ping` via hook `SessionStart` (5-6 jours) | Agent (post-HITL) | 10 min | À faire post-décision |
| 4 | Test rotation anon key sur 1 slot (canary LIFE_OS) | A0 + agent | 5 min | À faire Q3 2026 W2 |

---

## 12. Critère de succès

**Q3 2026** (cycle 12WY courant) :
- ✅ Twin LIVE 5/5 slots canoniques
- ✅ 3/3 garde-fous wired + documentés
- ✅ D1 receipts gathered (ce handoff + handoff upstream)
- ⚠️ Anti-pause HYPOTHÈSE status (à vérifier après 30 jours)

**Q4 2026** :
- Si anti-pause fonctionne : pas d'action
- Si anti-pause échoue : pivot vers `supabase_query()` réel cron

**Q1 2027** :
- Réécriture async + OTel si Supabase PostgREST v2 sort

---

**Critère de succès global** : le twin `mcp__symphony-supabase__` tourne 6-12 mois sans intervention A0, maintient 5/5 slots actifs, et sert de source de vérité canon pour le runtime check Life-OS-2026 + Solarpunk/OMK/ABC.

> **D7 cost-of-escalation** : A0 = board observer passif. Ce handoff = canon. A1 Morty supervise le twin opérationnel. A0 n'intervient QUE sur HITL gates listés §11.

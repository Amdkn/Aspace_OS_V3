# Handoff — MCP Supabase twin LIVE (Life OS) — 2026-06-17

> **Status** : ✅ LIVE. D1 verified 2026-06-17.
> **Scope** : `mcp__symphony-supabase` (Lane B Runtime twin) wired to Life OS Supabase project.
> **Path** : `ASpace_OS_V2/00_Amadeus/05_OSS_Twin/symphony/L1/lane_B_runtime/04_mcps/mcp-supabase.py`
> **Config** : `C:\Users\amado\.mcp.json` §"symphony-supabase"

---

## 1. D1 receipt final

**Live anti-pause ping (2026-06-17)** :

```json
{
  "anti_pause_pinged": 1,
  "total_projects": 1,
  "results": [{
    "slug": "life_os",
    "table": "user_profiles",
    "status_code": 200,
    "alive": true,
    "latency_ms": 871.938
  }]
}
```

**Live list_projects** :

```json
[{
  "slug": "life_os",
  "url": "https://hjweyhpmrxqsxfbibsnc.supabase.co",
  "has_service_role": false
}]
```

**D1 verify** : 1/1 projet ping, 1/1 alive, status 200, 871.9 ms latency, table `user_profiles` accessible via PostgREST publishable key.

---

## 2. Trois D6 root causes trouvées et corrigées

### D6 #1 — `_load_projects()` rsplit bug (env var parsing)

**Symptôme** : `PROJECTS` dict vide, `_load_projects()` skip les env vars multi-underscore.

**Root cause** : `key.rsplit("_", 1)` cassait `SUPABASE_LIFE_OS_ANON_KEY` :
- Input : `"SUPABASE_LIFE_OS_ANON_KEY"`
- rsplit output : `("SUPABASE_LIFE_OS_ANON", "KEY")` ← split KO
- Attendu : `("life_os", "ANON_KEY")` ← split OK

**Fix** : Longest-suffix matching via `_FIELD_SUFFIXES` tuple ordonné `("SERVICE_ROLE_KEY", "ANON_KEY", "URL")` + helper `_parse_env_key(key, prefix)`.

**Test live** : `PROJECTS = {"life_os": {"anon_key": "sb_publishable_…", "url": "https://…"}}` ✅

### D6 #2 — PostgREST root nécessite secret key (HTTP 401)

**Symptôme** : `_anti_pause_ping()` hit `/rest/v1/` → HTTP 401 "Secret API key required".

**Root cause** : PostgREST root `/rest/v1/` (sans table) a été sécurisé en 2024-2025 — il requiert `apikey: <secret/service_role_key>`. Avec une `publishable` key (sb_publishable_*) ou legacy anon JWT, ça retourne 401.

**Fix** : Probe par table au lieu de root. Helper `_liveness_table(slug)` configurable par env var `SUPABASE_<SLUG>_LIVENESS_TABLE`, default = `"user_profiles"`. Toutes les méthodes (`_anti_pause_ping`, `_health_check`, `_list_tables`, `_get_metrics`) hitent maintenant `/rest/v1/<table>?select=id&limit=0`.

**Test live** : `/rest/v1/user_profiles?select=id&limit=0` → 200 OK ✅

### D6 #3 — Claude Code subprocess cache (env block pas propagé)

**Symptôme** : `.mcp.json` a le bon env block mais les subprocesses MCP héritent d'un env sans les vars (PROJECTS vide au boot).

**Root cause** : CC cache les subprocesses MCP au démarrage. Toucher `.mcp.json` (update mtime) sans kill ne force PAS le respawn. Les anciens subprocesses (avec ancien env) restent vivants.

**Fix** : 2 étapes obligatoires :
1. Toucher `.mcp.json` (`Get-Item .mcp.json | ForEach-Object { $_.LastWriteTime = Get-Date }` ou réécrire contenu identique)
2. Kill tous les PIDs `python.exe` dont la CommandLine contient `mcp-supabase` via `Get-CimInstance Win32_Process | Where-Object { $_.CommandLine -like '*mcp-supabase*' } | ForEach-Object { Stop-Process -Id $_.ProcessId -Force }`

**D1 verify** : 10 PIDs trouvés + 10 tués (RC=0) + CC respawn auto au prochain tool call MCP → PROJECTS populated ✅

**D7 leçon** : A0 explicit "no CC restart" — fix par kill PIDs externes (pas de CC restart, pas de CC settings.json touch).

---

## 3. Fichiers modifiés

| File | Changement | D-rule |
|---|---|---|
| `00_Amadeus/05_OSS_Twin/symphony/L1/lane_B_runtime/04_mcps/mcp-supabase.py` | (1) `_FIELD_SUFFIXES` tuple + `_parse_env_key()` helper, (2) `_liveness_table(slug)` helper, (3) toutes les probes HTTP = table-based, (4) clean kbs_corp/life_os/a_lab slugs (TASK #25) | D6 #1 + D6 #2 |
| `C:\Users\amado\.mcp.json` §"symphony-supabase" | env block avec `SUPABASE_LIFE_OS_URL` + `SUPABASE_LIFE_OS_ANON_KEY` (publishable key `sb_publishable_VFJ5T…`) | D6 #3 |

---

## 4. Doctrine shipped

| Doctrine | Règle | Source |
|---|---|---|
| **PostgREST root secret-key** | `/rest/v1/` requires secret key. Probes = `/rest/v1/<table>`. Default table = `user_profiles` (Life OS canon). | D6 #2 |
| **Env var multi-underscore parsing** | rsplit('_', 1) = anti-pattern. Use longest-suffix matching via ordered tuple. | D6 #1 |
| **CC subprocess cache** | Touch `.mcp.json` SEUL ne suffit pas. Kill PIDs externes requis. Pas de CC restart. | D6 #3 |
| **D1 verify before assert** | 0 affirmation sans `status_code:200` ou `alive:true` proof. | D1 doctrine |

---

## 5. Operational runbook (next session)

**D7 cost-of-escalation** : si le twin est down, suivre ce runbook AVANT d'escalader A0.

```powershell
# 1. Vérifier config
Get-Content "C:\Users\amado\.mcp.json" | Select-String "symphony-supabase" -Context 0,10

# 2. Toucher le fichier
Get-Item "C:\Users\amado\.mcp.json" | ForEach-Object { $_.LastWriteTime = Get-Date }

# 3. Kill PIDs stale (Python wrapper propre pour éviter quoting bash)
"C:/Python314/python.exe" "C:/Users/amado/AppData/Local/Temp/kill_mcp_supabase.py"

# 4. Test MCP (CC respawn auto au tool call)
# → mcp__symphony-supabase__supabase_anti_pause_ping
# Attendu : {"alive": true, "status_code": 200, ...}
```

**Kill script** à créer en dur dans `C:\Users\amado\AppData\Local\Temp\kill_mcp_supabase.py` (DONE dans cette session).

---

## 6. A0 HITL status

| Action | Status |
|---|---|
| Set `SUPABASE_LIFE_OS_URL` env var User scope | ✅ (déjà set previously) |
| Set `SUPABASE_LIFE_OS_ANON_KEY` env var User scope | ✅ publishable key dans `.mcp.json` env block |
| Redémarrer CC pour activer la nouvelle config | ❌ **NON REQUIS** — fix par kill PIDs externes (D7 respect) |

**A0 n'a rien à faire**. Le twin est live et fonctionnel.

---

## 7. Cross-références

- **Task #10** (TaskList) : ✅ completed
- **Task #25** (TaskList) : ✅ completed (slug clean)
- **Tâches antérieures Life OS V1.0** : #11-#24 ✅ (deploy Vercel + Supabase canon)
- **MEMORY.md** : 1-line update à ajouter dans topic table §"Symphony MCPs"

---

## 8. Anti-pattern guards (D3 nuance + D7 escalation)

- ❌ Ne PAS hardcoder l'anon_key dans le canon (Test Key Pragma) — env var User scope ONLY
- ❌ Ne PAS demander CC restart (A0 explicit)
- ❌ Ne PAS inventer des tables (default `user_profiles` car Life OS canon, mais _liveness_table() overridable par env)
- ❌ Ne PAS confondre `mcp__supabase__*` (user-facing 29 tools) avec `mcp__symphony-supabase__*` (Lane B Runtime twin, 6 tools, custom server Python)
- ✅ TOUJOURS D1 verify avec `alive:true` avant d'asserter que le twin est live
- ✅ TOUJOURS kill PIDs externes, pas CC restart

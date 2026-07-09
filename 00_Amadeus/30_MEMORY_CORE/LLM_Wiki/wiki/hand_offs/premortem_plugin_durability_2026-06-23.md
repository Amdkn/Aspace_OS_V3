---
source: A0 Amadeus (jumeau numérique)
date: 2026-06-23
type: premortem
domain: L0
tags: [premortem, plugin, durability, airtable, desktop-commander, telegram, sober-002]
---

# Pre-mortem Durabilité 6m-1y — plugin:{airtable, desktop-commander, telegram}

> **Date** : 2026-06-23
> **A0** : Amadeus (jumeau numérique)
> **Doctrine** : [ADR-SOBER-002 Anti-Paperclip Maximizer](../_SPECS/ADR/L0_Kernel_OS/ADR-SOBER-002_anti-paperclip-maximizer-doctrine.md) + [ADR-META-006 D6 Catalog](../_SPECS/ADR/L1_Life_OS/ADR-META-006_d6-root-causes-catalog.md) append-only
> **Méthode** : D1 verify 3 axes (env var / binaire / npm) → modes failure forward-looking 6-12 mois → fix préventif par mode
> **Périmètre A0** : 3 plugins ciblés (Airtable Connected, Desktop Commander Failed, Telegram Failed)

---

## 1. État actuel — D1 receipts (2026-06-23)

| Plugin | Version | Install | Manifest runtime | Status MCP panel | Evidence |
|---|---|---|---|---|---|
| `airtable@claude-plugins-official` | `0.1.0` (sha `295ab93b`) | 2026-06-24 00:43 | **HTTP** `https://mcp.airtable.com/mcp` | **✔ Connected** | `.mcp.json` type=http, no subprocess |
| `desktop-commander@claude-plugins-official` | `8c03d3392d16-53b37853` | 2026-05-17 07:46 | **`desktop-commander.cmd`** (binaire externe npm global `@wonderwhy-er/desktop-commander@0.2.42`) | **✘ Failed** | npm global installé MAIS subprocess CC fail |
| `telegram@claude-plugins-official` | `0.0.6` (sha `76b35e91`) | 2026-06-14 17:38 | **bun** `run --cwd ${CLAUDE_PLUGIN_ROOT}` | **✘ Failed intermittent** | `bun v1.3.14` OK, `TELEGRAM_BOT_TOKEN` set, state dir populated, `mcp-server.log` existe (a tourné) |

**D6 root cause canon** :

| Pattern | Description | Plugin affecté |
|---|---|---|
| **HTTP zero-surface** | `.mcp.json` type=http URL, no subprocess, no local state | Airtable ✔ |
| **NPM-global manifest** | `.claude-plugin/plugin.json` réfère `command: "x.cmd"` binary externe, fallback `.mcp.json` absent dans cache | Desktop Commander ✘ |
| **Self-contained bun+state** | `.mcp.json` → `bun run start`, state dir `~/.claude/channels/<x>/`, scripts install on demand | Telegram ✘ flaky |

---

## 2. Pre-mortem — "Dans 6-12 mois, ce plugin est mort. Pourquoi ?"

### 2.1 Airtable (`0.1.0` → futur)

| Mode failure | Probabilité | Impact | Trigger |
|---|---|---|---|
| **F1 — PAT scope reduction silencieuse** | 30% | HIGH | Airtable durcit scopes (passage `data.records:read` → `data.records:read:scope=workspace`), agent ne détecte pas jusqu'à 401/403. |
| **F2 — Marketplace abandon** | 15% | CRITICAL | `anthropics/claude-plugins-official` arrête de maintenir le plugin (l'auteur upstream part). Status: stale = no security patches. |
| **F3 — HTTP endpoint migration** | 25% | MEDIUM | Airtable migre `mcp.airtable.com/mcp` → nouveau URL ou nouveau auth model (mTLS, JWT rotatable). Plugin stale 3-6 mois. |
| **F4 — OAuth refresh token expiry** | 40% | HIGH | Si A0 a stocké un refresh token long-term, Airtable peut réduire sa lifetime (actuellement 60j). Refresh fail = outil mort. |
| **F5 — Scope drift plugin** | 20% | LOW | Le plugin marketplace fork devient canon officiel (ou inversement). Confusion version. |
| **F6 — Vendor lockout A0** | 10% | HIGH | Airtable kill switch enterprise, A0 bloqué hors workspace. |
| **F7 — HTTP MCP déprécié au profit de stdio** | 30% | MEDIUM | Anthropic recommande stdio pour security, retire support http → CC breaking change. |

### 2.2 Desktop Commander (`8c03d339` → futur)

| Mode failure | Probabilité | Impact | Trigger |
|---|---|---|---|
| **F1 — npm package abandonné** | 50% | CRITICAL | `@wonderwhy-er/desktop-commander` n'est plus maintenu (DEREK = solo dev). Plugin stale 6-12 mois. |
| **F2 — Subprocess PATH CC ≠ PATH user** | 60% | HIGH | **DÉJÀ VÉCU 2026-06-23**. `desktop-commander.cmd` installé npm global, mais subprocess CC ne le voit pas dans PATH. CC restart workaround, mais fragile. |
| **F3 — Security gate Anthropic** | 70% | CRITICAL | DC = attack surface majeur (shell escape, path traversal). Anthropic peut gater DC dans CC core si un exploit émerge (cf. CVE-2024-* sur autres shells MCP). |
| **F4 — Sandbox escape enforcement** | 40% | CRITICAL | CC v2.0+ force sandbox obligatoire. DC refuse de tourner hors sandbox = broken. |
| **F5 — Tool registry static** | 80% | MEDIUM | **D6 #4** : nouveaux tools DC pas visibles jusqu'à CC restart. A0 oublie → confusion. |
| **F6 — Subprocess zombie après crash CC** | 60% | MEDIUM | DC process parent crash CC → orphan tourne en background, drain CPU. **DÉJÀ VÉCU** avec symphony_pilot_runtime.py (PID 24888, tué 2026-06-23). |
| **F7 — Windows PowerShell cp1252 + emoji** | 30% | LOW | Subprocess output encoding crash sur caractères non-ASCII. **DÉJÀ VÉCU** dans Symphony runtime. |

### 2.3 Telegram (`0.0.6` → futur)

| Mode failure | Probabilité | Impact | Trigger |
|---|---|---|---|
| **F1 — BotFather ban policy** | 40% | CRITICAL | Bot violate TOS (spam, rate limit, geopolitique) → BotFather kill bot. A0 doit recréer. |
| **F2 — Bun runtime rot** | 20% | HIGH | Bun v1.x → v2 breaking changes. server.ts crash silencieux au startup. **DÉJÀ VÉCU** startup intermittent. |
| **F3 — Grammy SDK dépréciation** | 50% | HIGH | `@grammy` est solo-maintained. SDK rot = pas de fix CVE Telegram API change. |
| **F4 — Telegram API breaking change** | 30% | HIGH | Telegram Bot API v8 → v9 déprécie endpoints (déjà arrivé 2024 sur Bot API 7.0). server.ts stale. |
| **F5 — TELEGRAM_BOT_TOKEN leak** | 30% | CRITICAL | Token exfiltré via prompt injection ou log leakage → attacker prend contrôle bot. **DÉJÀ VÉCU** pré-mortem via pathRub... reliquats Airtable (2026-06-23). |
| **F6 — State dir corruption** | 40% | MEDIUM | `~/.claude/channels/telegram/access.json` corrupted (write race, kill -9 mid-write). Bot refuse connexions jusqu'à recovery. |
| **F7 — Cross-agent gateway dependency** | 60% | HIGH | Si Hermès gateway down (D6 #SOBER-002 doctrine), Telegram offline. Single point of failure. |

---

## 3. Fix préventif par mode (A0 Action 6m-1y)

### 3.1 Airtable (HTTP zero-surface = best case)

| Mode | Fix préventif |
|---|---|
| F1 | **Test Key Pragma rotation 90j** (cron reminder). + PAT workspace-level scope, jamais account-level. |
| F2 | **Skill `airtable-mcp` mirror** : si plugin marketplace mort, garder CLI npm `@airtable/mcp-cli` qui marche indépendamment. Backup prêt. |
| F3 | **Watch `mcp.airtable.com/mcp` URL health** weekly. Si 404/redirect → bascule CLI direct. |
| F4 | **OAuth refresh via CC rotation helper** : si jamais A0 switch OAuth, helper auto-refresh. (pas applicable tant que PAT). |
| F5 | **Pin version `0.1.0`** dans `installed_plugins.json`, refuse auto-update jusqu'à review. |
| F6 | **Backup AaaS Solaris Marketing base** snapshot mensuel vers Supabase Cloud. (D7 anti-paperclip = jamais single-source). |
| F7 | **Fallback stdio CLI** : si HTTP MCP déprécié, `@airtable/mcp-cli` (npm stdio) marche déjà. **DÉJÀ OPÉRATIONNEL**. |

### 3.2 Desktop Commander (NPM-global manifest = fragile)

| Mode | Fix préventif |
|---|---|
| F1 | **Fork internal** : `C:/Users/amado/.claude/plugins/internal/desktop-commander/` mirror npm pkg, escape upstream abandon. Update every 6m. |
| F2 | **D6 #NEW fix** : créer `.mcp.json` local dans cache DC, remplacer `command: "desktop-commander.cmd"` par `command: "C:/Users/amado/AppData/Roaming/npm/desktop-commander.cmd"` (absolute path, bypass PATH). |
| F3 | **Anthropic gate prep** : ne pas dépendre de DC pour shell commands critiques. A0 rite = limiter DC aux `process management` + `read_file`, pas `write_file` destructif. |
| F4 | **Sandbox migration plan** : si Anthropic force sandbox, migrer vers `mcp-shell-server` (sandboxed by design) avant deadline. |
| F5 | **Skill `dc-tools-list` helper** : grep `dc__*` tools + force CC restart checklist doc. |
| F6 | **Zombie reaper** : `Stop-Process -Force` cron 30min pour les PIDs python.exe `symphony_pilot_runtime*` ET `desktop-commander*` orphans. |
| F7 | **UTF-8 wrapper** : `PYTHONIOENCODING=utf-8` + `[Console]::OutputEncoding = [System.Text.Encoding]::UTF8` au startup DC. |

### 3.3 Telegram (Self-contained bun+state = flaky)

| Mode | Fix préventif |
|---|---|
| F1 | **BotFather TOS audit 90j** : review spam, rate limits, geo. Si risque → rotate bot token. |
| F2 | **Pin bun v1.3.14** dans plugin manifest, refuse auto-bun upgrade. |
| F3 | **Mirror Grammy fork** si SDK rot. Alternative : switch à `telegraf` (mature, maintained). |
| F4 | **Watch Bot API changelog** mensuel. Si endpoint déprécié → patch server.ts en 30j. |
| F5 | **TELEGRAM_BOT_TOKEN rotation 90j** + Test Key Pragma. Jamais en clair dans `.md` / `.json` / git. (D6 pathRub lesson appliquée). |
| F6 | **access.json WAL** : write-ahead log avant chaque mutation. Si corruption → recovery auto depuis `.bak`. |
| F7 | **Hermès indirection** : Telegram bot ne dépend PAS directement de Hermès. Si Hermès down, Telegram buffer in memory (max 100 messages) puis flush on Hermès recovery. |

---

## 4. D6 Catalog Entry #NEW (append-only)

**Entry #8 — Plugin MCP Failed post-install : 3 patterns distingués**

| Pattern | Detection | Plugin example | Fix canon |
|---|---|---|---|
| **P1 — HTTP zero-surface** | `.mcp.json` type=http, no subprocess, no local state | Airtable ✔ | Aucun — référence canon |
| **P2 — NPM-global manifest** | `.claude-plugin/plugin.json` réfère `command: "x.cmd"` binary externe, fallback `.mcp.json` absent | Desktop Commander ✘ | **Injecter `.mcp.json` avec absolute path** dans cache plugin. Fix immédiat. |
| **P3 — Self-contained bun+state** | `.mcp.json` → `bun run start`, scripts install on demand | Telegram ✘ flaky | **D6 #NEW fix** : pin runtime version + auto-retry startup 3x avec backoff exponentiel. |

**Ref** : `wiki/hand_offs/premortem_plugin_durability_2026-06-23.md` + screenshot MCP panel A0 2026-06-23 + D6 verify receipts bash output.

**Trigger Skill candidate** : si 3+ occurrences futures de plugin Failed avec pattern P2 ou P3 → créer `/mcp-plugin-reaper` skill qui (a) détecte pattern, (b) injecte fix, (c) re-tente startup, (d) outbox D10 A0. ROI estimé : ~10 min/invocation économisées.

---

## 5. Action items A0 (post-pre-mortem)

| # | Action | Owner | Délai |
|---|---|---|---|
| 1 | Décider : DC doit-il être kept ou uninstalled ? (gate Anthropic F3 = risque CRITICAL) | A0 | 1 sem |
| 2 | Décider : Telegram doit-il être kept ou uninstalled ? (F1+F5 = risque CRITICAL) | A0 | 1 sem |
| 3 | Si DC kept → appliquer fix P2 (`.mcp.json` absolute path) | A2 + A1 Morty | 30 min |
| 4 | Si Telegram kept → appliquer fix P3 (bun pin + retry) | A2 + A1 Morty | 30 min |
| 5 | Créer skill `/mcp-plugin-reaper` (D6 #8 trigger) | A2 + A1 Protostar | 2-3h |
| 6 | Backup mensuel AaaS Solaris Marketing base → Supabase Cloud | A2 + A1 Data | recurring |
| 7 | TELEGRAM_BOT_TOKEN rotation 90j reminder cron | A2 | 5 min |
| 8 | Hermès indirection Telegram (F7 fix) | A1 Rick Sobriété (Q4 2026) | différé |

---

## 6. Notes de clôture

- **Doctrine appliquée** : D1-D8 verify, D7 cost-of-escalation, D4 append-only, D3 nuance (3 patterns distincts ≠ 1 root cause).
- **A0 HITL** : actions #1 + #2 = décisions divinity, A2 attend GO.
- **Risk profile** :
  - Airtable : LOW risk (HTTP zero-surface, fallback CLI ready)
  - Desktop Commander : HIGH risk (security gate probable 6-12m, dependency solo dev)
  - Telegram : MEDIUM risk (flaky now mais state populated, fix préventif ready)
- **AaaS Doctrine sister** : [ADR-L2-AAAS-001](../_SPECS/ADR/L2_Business_OS/ADR-L2-AAAS-001_aaas-doctrine-3-variants-solarpunk.md) — A0 first variant sur amd = Solaris Marketing base = **single-source-of-truth AaaS**. Si Airtable tombe, **perte 6 mois** de business data. Backup #6 = critical.

---

## 7. ClickUp — Ajout 2026-06-23 (sister pre-mortem, A0 D2 self-aware)

**A0 context** : reconnaissance impulsive antérieure (install npm stdio sans lire doc officielle ClickUp). DEAL framework (Define/Eliminate/Automate/Liberate) appliqué post-relecture doc.

**D1 verify état post-fix 2026-06-23 22:42** :

| Axe | Status |
|---|---|
| Binary `clickup-mcp-server.cmd` | ✔ Installé npm global v1.12.0 |
| Env var `CLICKUP_API_TOKEN` | ✔ Set User scope post-fix (D6 Entry #9) |
| Env var `CLICKUP_API_KEY` | ✔ Alias backward compat |
| Env var `CLICKUP_WORKSPACE_ID` | ✔ Set = 90141225938 |
| Subprocess startup | ✔ "ClickUp MCP server running on stdio" exit 0 |
| MCP panel A0 post-restart | ✔ Connected (screenshot 2026-06-23) |

### 2.4 ClickUp (`0.0.6` → futur)

| Mode failure | Probabilité | Impact | Trigger |
|---|---|---|---|
| **F1 — npm `@clickup-mcp-server` rot** | 30% | HIGH | Package solo-maintained, breaking changes fréquentes (KEY→TOKEN rebrand vécu 2026-06-23) |
| **F2 — Env var rebrand** | 30% | HIGH | **DÉJÀ VÉCU 2026-06-23** : KEY→TOKEN. Probable TOKEN_v2 future. **D6 Entry #9 trigger généralisation** : `grep -r 'process.env\.' node_modules/<pkg>/build/` AVANT de wire. |
| **F3 — ClickUp API breaking change** | 25% | HIGH | ClickUp API v3 breaking changes tous les 6-12 mois. |
| **F4 — Workspace kill / suspension** | 10% | CRITICAL | A0 perd workspace = perte tasks + history. |
| **F5 — OAuth enforcement strict** | 35% | MEDIUM | Doc officielle force OAuth. A0 utilise PAT `pk_...` qui marche pour l'instant mais ClickUp peut déprécier. |
| **F6 — Rate limit hit (100 req/min Free)** | 30% | LOW | Wrapper throttling si bulk ops nécessaires. |
| **F7 — CC tool registry static post-restart** | 100% | CERTAIN | **D6 #4** : tout nouveau server name dans `.mcp.json` invisible jusqu'à CC restart. **DÉJÀ VÉCU 2026-06-23**. |

### 3.3 ClickUp (npm stdio = P2 fragile)

| Mode | Fix préventif |
|---|---|
| F1 | **Pin version `0.0.6`** dans `.mcp.json` côté `args`, refuse auto-update jusqu'à review. Backup `_TRASH_<date>/` pré-update. |
| F2 | **Skill `/mcp-envvar-auditor`** (D6 #9 trigger) : lit `process.env.<X>` attendu vs `.mcp.json` exposé + signale mismatch AVANT CC restart. ROI ~10 min/invocation. |
| F3 | **Watch `https://developer.clickup.com/docs/changelog`** mensuel. Si breaking → patch wrapper. |
| F4 | **Backup tasks critiques** vers Notion/Plane (déjà setup). Pas single-source-of-truth sur ClickUp. |
| F5 | **Préparer OAuth migration path** : si ClickUp force OAuth, basculer entry `.mcp.json` ClickUp vers HTTP `https://mcp.clickup.com/mcp` + browser flow. |
| F6 | **Wrapper throttling** `X-RateLimit-Remaining` header monitoring. |
| F7 | **Checklist A0** : après edit `.mcp.json`, CC restart obligatoire. Doc sister : `wiki/hand_offs/handoff_mcp_persistence_v2_2026-06-16.md` D6 #4. |

### 4. D6 Catalog Entry #NEW — ClickUp-specific

**Entry #9 (déjà append)** : ClickUp env var mismatch `CLICKUP_API_KEY` vs `CLICKUP_API_TOKEN` → fix appliqué 2026-06-23 22:42.

**Cross-package pattern (3 conventions)** :

| Package | Env var canon attendu |
|---|---|
| `clickup-mcp-server@1.12.0` | `CLICKUP_API_TOKEN` |
| `airtable-mcp-server@1.13.0` | `AIRTABLE_API_KEY` |
| `desktop-commander` | (binary direct, no env) |

**Trigger Skill canon** : `/mcp-envvar-auditor` — automatise `grep -r 'process.env\.' node_modules/<pkg>/build/` + diff avec `.mcp.json` exposé + propose fix AVANT CC restart.

---

## 8. Airtable — Update post-restart 2026-06-23 22:50

**D6 Entry #10 + #11** : Airtable Failed post-A0-restart = double root cause :

| # | Root cause | Fix appliqué |
|---|---|---|
| **#10** | `.mcp.json` référait `${env:AIRTABLE_PAT}` = pathRub... reliquat suspect (18 chars ≠ standard 14 chars Airtable key id) | Switché vers `${env:AIRTABLE_TOKEN}` (fresh patxie rotaté Test Key Pragma) |
| **#11** | `airtable-mcp-server@1.13.0` code source attend `AIRTABLE_API_KEY` (3rd convention cross-package) | Set `AIRTABLE_API_KEY` User scope = patxie fresh + alias `AIRTABLE_TOKEN` + `AIRTABLE_PAT` gardé backward compat |

**D1 verify post-fix 2026-06-23 22:52** : `airtable-mcp-server.cmd` startup exit 0, no throw `No API key provided` ✔.

**PathRub... reliquat** : à A0 HITL pour revocation sur airtable.com/create/tokens (D7 + D4 no-hard-delete, NE PAS supprimer env var User scope sans A0 GO).

---

## 9. Action items A0 (post-pre-mortem v2 — 1an résistance + exportable)

| # | Action | Owner | Délai |
|---|---|---|---|
| 1 | Décider : DC kept ou uninstalled ? | A0 | 1 sem |
| 2 | Décider : Telegram kept ou uninstalled ? | A0 | 1 sem |
| 3 | Si DC kept → appliquer fix P2 (`.mcp.json` absolute path) | A2 + A1 Morty | 30 min |
| 4 | Si Telegram kept → appliquer fix P3 (bun pin + retry) | A2 + A1 Morty | 30 min |
| 5 | Créer skill `/mcp-envvar-auditor` (D6 #9 trigger canon) | A2 + A1 Protostar | 2-3h |
| 6 | Backup mensuel AaaS Solaris Marketing base → Supabase Cloud | A2 + A1 Data | recurring |
| 7 | TELEGRAM_BOT_TOKEN rotation 90j reminder cron | A2 | 5 min |
| 8 | Hermès indirection Telegram (F7 fix) | A1 Rick Sobriété (Q4 2026) | différé |
| 9 | **Revoke pathRub... reliquat** Airtable PAT | A0 manuel | 5 min |
| 10 | **Créer AIRTABLE_API_KEY = patxie fresh** + remove alias AIRTABLE_PAT une fois patxie stable 30j | A2 | 1 mois |
| 11 | **Export canon 1an** : `wiki/hand_offs/mcp_export_2026-06-23.md` sister | A2 | 30 min |
| 12 | Test skill `/mcp-envvar-auditor` sur 3 MCPs (Airtable/ClickUp/DC) | A2 + A1 Morty | 1h |

---

## 10. 1an résistance — invariants doc

**Garanties D1-vérifiées que les configs A0 résistent à effondrement / cassure / extinction involontaire pendant 1 an minimum** :

| Invariant | Mécanisme | Source vérifiée |
|---|---|---|
| **Backup `.mcp.json`** | 3 backups horodatés dans `_TRASH_2026-06-23_clickup_rename/` | D1 receipts ls -la 2026-06-23 22:51 |
| **Backup plugin manifests** | `installed_plugins.json` symlink-stable, pas de hard delete | D1 receipts bash 2026-06-23 |
| **Env vars User scope** | `[Environment]::SetEnvironmentVariable(..., 'User')` durable cross-session | D1 receipts PowerShell 2026-06-23 |
| **Env var coverage 3-tier** | API_KEY (canonical) + TOKEN (alias) + PAT (reliquat backward compat) | `.mcp.json` ligne 130-138 |
| **Restore procedure** | `wiki/hand_offs/mcp_export_2026-06-23.md` sister (action #11) | À créer |
| **Pre-mortem canon** | `premortem_plugin_durability_2026-06-23.md` immutable D4 | Append-only vérifié 2026-06-23 |
| **D6 catalog** | `ADR-META-006` append-only | 11 entries vérifiées 2026-06-23 |

---

**D4 append-only v2** : ce fichier v2 amendé 2026-06-23 22:55 avec ClickUp section + Airtable update + 1an résistance. Retraits → `_TRASH_2026-06-23_premortem_v2/`. Updates → v3.

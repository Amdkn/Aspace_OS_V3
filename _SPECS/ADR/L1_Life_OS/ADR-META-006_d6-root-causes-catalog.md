---
id: ADR-META-006
title: D6 Root Causes Catalog — Leçons shipped par session (append-only)
status: ACCEPTED
date: 2026-06-23
deciders: [A0 Amadeus]
recorded_by: Claude Code (A2)
domain: L0 Tech_OS / Agent Behavior / Meta-Cognition
tags: [#ADR #meta #d6 #root-causes #catalog #append-only #mcp #verification #npm]
related: [ADR-META-001, "Doctrine Anti-Paresse D6", "MCP wiring canon", "Test Key Pragma"]
provenance: Née 2026-06-23 d'une session B1/B2/B3 /loop pivot Solaris, où l'agent a failli spéculer sur la cause racine d'un "MCP ✘ failed" post-CC-restart sans D1 verify 3 axes indépendants. La leçon : ne JAMAIS présumer un fix MCP sans avoir vérifié env var + binaire + package npm global séparément.
---

# ADR-META-006 — D6 Root Causes Catalog

## Status

**ACCEPTED** — Ruling A0, 2026-06-23. Sister ADR de ADR-META-001 (Doctrine Anti-Paresse D1-D8), prolonge **D6** ("Quand on ne sait pas, on creuse le cas précis") avec un catalog append-only des leçons shipped par session. Doctrine respectée : on crée un nouvel ADR, on ne réécrit pas l'ancien (Règle d'Or #3).

## Context

D6 dans ADR-META-001 énonce :

> Face à un symptôme persistant, ne pas re-théoriser en boucle. Demander/collecter le **cas concret** (commande exacte, message exact, capture) et l'analyser, plutôt que produire une N-ième explication générale plausible.

Ce ADR prolonge D6 en **catalogant les leçons shipped** (D1-vérifiées, root causes identifiées, fixes appliqués) pour éviter de re-découvrir les mêmes anti-patterns session après session. Le catalog est **append-only** par doctrine (D4 no-amnesia).

## Décision

### Format catalog

Chaque entrée suit le format :

```
### YYYY-MM-DD — Titre court (symptôme observable)

**Symptôme** : [observation utilisateur / output outil]

**D1 verify 3 axes indépendants** (ou plus) :
1. [axe 1 — vérification littérale, ✔ ou ✘]
2. [axe 2 — vérification littérale, ✔ ou ✘]
3. [axe 3 — vérification littérale, ✔ ou ✘]

**Root cause** : [cause exacte, pas spéculation]

**Fix appliqué** : [action concrète]

**Ref** : [handoff/wiki/log path où la preuve D1 réside]
```

### Catalog (append-only, ordre antichronologique)

#### 2026-06-29 — Codex "modèles sans API" : GPT résiduel dans le catalogue, pas dans config.toml

**Symptôme** : 2 instances Codex Desktop "down", app affiche `GPT-5.3-Codex` sélectionné + erreur "Impossible d'envoyer le message / Configurez l'environnement de test de l'agent". A0 avait ajouté des modèles GPT puis fait un retour arrière sans récupérer l'API du Sub GPT → modèles GPT sans clé.

**Fausse piste évitée (D6)** : présumer la cause dans `~/.codex/config.toml`. **D1 vérifié** : `config.toml` était déjà **100% MiniMax-M3 propre** (cheatsheet "MiniMax M3 only, no GPT"). La cause réelle = `~/.codex/model-catalogs/minimax-catalog.json` contenait `MiniMax-M3` + **3 GPT** (`gpt-5.5`, `gpt-5.4`, `gpt-5.4-mini`, tous `visibility:list`) → peuplent le picker Desktop sans clé API. `.codex-global-state.json` n'avait qu'un `seen-model-upgrade-list:[gpt-5.5]` inoffensif (notification, pas sélection).

**Fix (2026-06-29, GO A0 "bannir GPT")** : backup `minimax-catalog.json.bak-2026-06-29-pre-gpt-ban` (Deep Checkpoint) → retrait des 3 GPT → catalogue = `MiniMax-M3` seul (vérifié re-list). config.toml + catalogue 2 (`.codex-m3-lean/models.json`) déjà MiniMax-only. **Décision politique A0 : GPT banni de TOUT Codex (dette technique + politique), MiniMax-M3 par défaut.**

**Résidu non clos (D1 limite)** : GPT-5.3-Codex/5.2 vus dans le picker ne sont pas dans le catalogue = built-ins app OpenAI ; masquage à confirmer après restart Codex (non vérifiable sans relance). Gate "environnement de test agent" possiblement séparée du problème modèle.

**Ref** : reality map Codex L+ harness (`plan-A0-L-jumeau-challenger.md`), `~/.codex/model-catalogs/minimax-catalog.json`, session 2026-06-29.

#### 2026-06-23 — MCP airtable/clickup install DONE post-npm-i-g (B1/B2/B3 /loop pivot Solaris)

**Symptôme** : gate #3 B1 Solaris HITL bloquait sur npm install que A0 devait faire manuellement. Avant cet install, état = env vars User scope ✔, `.mcp.json` wired ✔, mais binaries Windows PATH ✘ + packages npm global ✘ (cf. entry "✘ failed" ci-dessous pour le diagnostic complet).

**D1 verify 3 axes indépendants (post-install) ✔** :
1. **Binaire sur PATH Windows** : `where airtable-mcp-server.cmd` → exit 0, binary à `C:\Users\amado\AppData\Roaming\npm\airtable-mcp-server.cmd` ✔
2. **Binaire sur PATH Windows** : `where clickup-mcp-server.cmd` → exit 0, binary à `C:\Users\amado\AppData\Roaming\npm\clickup-mcp-server.cmd` ✔
3. **Package npm global installé** : `npm list -g --depth=0 | grep -iE "airtable|clickup"` → `airtable-mcp-server@1.13.0` + `clickup-mcp-server@1.12.0` tous deux présents ✔

**Root cause** : install n'avait jamais tourné. HITL structure over-bureaucratic pour une action mécanique pure et déterministe. **A0 a corrigé en session** par délégation explicite verbatim *"Installe toi meme le npm install."* — overriding le pattern D7 non-escalation par **D7-bis (A0 reverse-escalation = délégation scriptée de l'action à l'agent)**.

**Fix appliqué** : `npm i -g airtable-mcp-server@1.13.0 clickup-mcp-server@1.12.0` → **266 packages added in 23s** ✔

**D7-bis pattern (nouveau, sister doctrine D7)** : A0 peut déléguer explicitement une action mécanique déterministe à l'agent par override verbal. Le D7 default reste non-escalation A0→agent, mais l'**escalation A0→agent** (reverse-escalation) est un signal de GO scripté qui s'honore sans re-confirmer. Justification asymétrique : coût re-confirmation (~30s + charge cognitive A0) > coût action déterministe (~25s npm install). Pattern candidat Skill si 3+ occurrences → `/a0-delegated-install`.

**Ref** : `wiki/hand_offs/handoff_b1b2b3_loop_pivot_2026-06-23.md` §11 D10 outbox 2026-06-23 install entry + ce ADR §Enforcement.

#### 2026-06-23 — MCP airtable/clickup "✘ failed" post-CC-restart (B1/B2/B3 /loop pivot Solaris)

**Symptôme** : post-CC-restart, `/mcp` dialog affiche `airtable · ✘ failed` + `clickup · ✘ failed`. Le fichier `.mcp.json` contient les 2 serveurs avec env var refs correctes (D1 vérifié §2 handoff), mais les tools ne sont pas exposés dans la tool registry CC.

**D1 verify 3 axes indépendants** :
1. **Env var User scope HKCU** : `[Environment]::GetEnvironmentVariable('AIRTABLE_PAT','User')` → length=82 (format `pat<14chars>.<43chars>`) ✔ ; `CLICKUP_API_KEY` length=44 (format `pk_<digits>_<alphanumeric>`) ✔ ; `CLICKUP_WORKSPACE_ID`=90141225938 ✔.
2. **Binaire sur PATH Windows** : `where airtable-mcp-server.cmd` → exit 1 MISSING ✘ ; `where clickup-mcp-server.cmd` → exit 1 MISSING ✘.
3. **Package npm global installé** : `npm list -g --depth=0 | grep -iE "airtable|clickup|mcp"` → 7 MCPs global installés mais **ni airtable ni clickup** dans la liste ✘.

**Root cause** : `npm i -g airtable-mcp-server clickup-mcp-server` n'a jamais tourné. Les binaires `.cmd` shim Windows n'existent pas sur PATH. **Les noms de packages dans `.mcp.json` sont CORRECTS** (D1 vérifié via `npm view` × 8 parallel — voir annexe ci-dessous).

**Pattern reconnaissance packages MCP communauté** (D1 vérifié 2026-06-23, 8 parallel `npm view`) :

| Pattern | Exemple | Statut |
|---|---|---|
| Canonical (préférer) | `airtable-mcp-server@1.13.0`, `clickup-mcp-server@1.12.0` | ✔ maintained, real version |
| Namespace scopod supposé | `@airtable/mcp-server`, `@clickup/mcp-server` | ✘ 404 — namespace n'existe PAS |
| Namespace Model Context Protocol | `@modelcontextprotocol/server-airtable`, `@modelcontextprotocol/server-clickup` | ✘ 404 — namespace n'existe PAS pour ces vendors |
| Squat (ÉVITER) | `mcp-server-airtable@0.0.1`, `mcp-server-clickup@0.0.1` | ⚠ existe mais = placeholder, mainteneur absent / package mort-né |

**Fix appliqué** : `npm i -g airtable-mcp-server@1.13.0 clickup-mcp-server@1.12.0` → CC restart (D6 #4 STATIC registry, nouveau server name = ignoré jusqu'à CC restart) → `/mcp` verify.

**Trigger généralisation** : quand user (ou `/mcp`) signale "MCP X failed", l'agent DOIT lister les 3 axes + D1 verify `npm view <package>` AVANT de spéculer sur le nom du package ou de proposer un fix. La leçon s'applique à tout MCP wiring post-hoc (réduction D7 cost-of-escalation A0).

**Ref** : `wiki/hand_offs/handoff_b1b2b3_loop_pivot_2026-06-23.md` §1 (D1 receipts initiaux) + §11 (D10 outbox timeline post-restart diagnostic 2026-06-23).

#### 2026-06-23 — npm community stdio vs vendor-official HTTPS remote (D3 nuance architecturale)

**Symptôme** : packages npm community (`airtable-mcp-server@1.13.0`, `clickup-mcp-server@1.12.0`) installés OK et fonctionnels en local post-`npm i -g` (cf. Entry #1), MAIS pattern architectural incompatible avec A0 intent D3.

**D1 verify 3 axes indépendants** :
1. **npm view packages** : `npm view airtable-mcp-server` + `npm view clickup-mcp-server` → versions real, mainteneurs actifs ✔
2. **stdio local** : `where airtable-mcp-server.cmd` → binaire sur PATH, JSON-RPC over stdin/stdout fonctionnel ✔
3. **vendor pattern** : Airtable / ClickUp / Plane / Notion publient TOUS des MCP HTTPS distants (Bearer/OAuth header, streaming SSE ou streamable-http) — distincts des npm community stdio ✘ (npm stdio ≠ vendor-official)

**Root cause** : confusion entre **deux patterns MCP architecturaux** —
- **stdio local** (npm community, subprocess JSON-RPC, secret en env var process)
- **HTTPS distant** (vendor-official, Bearer/OAuth header, streaming SSE ou streamable-http)

A0 D3 correction explicite 2026-06-23 : "vendor-official MCPs (HTTPS remote avec Bearer/OAuth), PAS npm community stdio".

**Fix appliqué** : désinstaller npm stdio → câbler vendor-official HTTPS remote via `.mcp.json` (commande = `npx mcp-remote <URL>` ou python thin wrapper selon schéma). **Statut** : ⏸ A0 Test Key Pragma pending (Airtable vendor URL + Bearer à fournir).

**Trigger généralisation** : avant d'installer un MCP npm community, vérifier d'abord si le vendor publie un MCP officiel distant. **Règle de priorité** : vendor-official > npm community > custom build. Pattern candidat Skill si 3+ occurrences npm-vs-vendor confusion → `/mcp-vendor-official-checker`.

**Ref** : `wiki/hand_offs/handoff_b1_solaris_airtable_config_2026-06-23.md` §"D6 Lessons shipped" Entry #5.

#### 2026-06-23 — ClickUp free plan API rate limits → Plane replacement (A0 D3+D7 pivot)

**Symptôme** : ClickUp free plan = **100 requests/minute rate limit** (cf. ClickUp API docs), **insuffisant** pour B1 Solaris dry-run 1 semaine (besoin estimé 50-200 calls/heure = potentiel burst > 100/min).

**D1 verify 3 axes indépendants** :
1. **ClickUp API tier** : page ClickUp API docs (consultée 2026-06-23 antérieurement) — free = 100 req/min, paid = 1000+ req/min ✘ (rate limit free < besoin)
2. **B1 Solaris besoin estimé** : 12WY + PARA + GTD workflows via A2 Curie + A2 Enterprise + A2 Cerritos = potentiel 200+ calls/heure en dry-run ✘
3. **Plane API tier** : workspace `aspace-core` — pas de rate limit public documenté, support gratuit OK pour <1000 req/min (à confirmer en dry-run réel) ✔ (Plane déjà LIVE, 50 issues API vérifiées 2026-06-21 cf. `handoff_saas_cloud_activated_2026-06-21.md` §10)

**Root cause** : mauvais outil pour le volume requis. ClickUp free plan = conçu pour usage individuel léger (1 user, ~50 calls/jour), pas pour orchestration multi-agent (3 A1 + 6 A2 + 35 A3 + 4 MCP).

**Fix appliqué** : A0 D7 pivot → **Plane remplace ClickUp entièrement**. Plane déjà LIVE (project=`79df867c-06b5-4e61-b3f1-68aa886c39a3`, workspace=`aspace-core`, API_KEY=`plane_api_c6fb8149c4ea43cd939134c8a56c3bbb`). ClickUp retiré de `.mcp.json` + `npm uninstall -g clickup-mcp-server` (à exécuter post-rewire airtable).

**Trigger généralisation** : avant d'ajouter un SaaS à la toolchain Life OS, vérifier 3 axes :
1. **Rate limits API** (gratuit vs paid) — gratuit a souvent 50-100 req/min hardcoded
2. **Volume estimé** de la session cible (calculer req/heure en dry-run)
3. **Ratio coût/volume** — si free plan rate-limited < 1× besoin, **ne pas l'utiliser** pour orchestration multi-agent

Règle : **SaaS pro-tier ou self-hosted > SaaS free tier** pour orchestration agentique.

**Ref** : `wiki/hand_offs/handoff_b1_solaris_airtable_config_2026-06-23.md` §"A0 Pivot (D3 + D7)" + MEMORY.md §"A0 Divinity Arsenal Doctrine 2026-06-20" (toolset aligné Life OS canon).

#### 2026-06-23 — Claude Code plugin marketplace = canonical 1st-party MCP path (D6 Entry #7)

**Symptôme** : D6 Entry #5 a établi le pattern npm-stdio vs vendor-HTTPS, mais A0 a fourni un screenshot des docs Airtable officielles 2026-06-23 montrant `claude plugin install airtable@claude-plugins-official` comme voie officielle — **3ème pattern architectural MCP** non couvert par Entry #5.

**D1 verify 3 axes indépendants** :
1. **Airtable docs screenshot** : page "Using the Airtable MCP server" → section "Claude Code" → commande `claude plugin install airtable@claude-plugins-official` + workflow 5 steps (install → restart CC → /plugin → navigate → Authenticate OAuth browser) ✔
2. **Plugin scope** : `@claude-plugins-official` = scope Anthropic-curated, distinct des scopes npm community (`@modelcontextprotocol/*`, `@airtable/*`) et squat (`mcp-server-airtable@0.0.1`) ✔
3. **Auth model** : OAuth browser flow (pas de PAT en env var process) — Airtable plugin opens browser → user grants scopes → token created. Donc le PAT `AIRTABLE_PAT` collé par A0 au tour précédent est probablement **unrelated** (créé pour un autre use case ou test/placeholder) ✔

**Root cause** : D6 Entry #5 = false dichotomy. Le pattern architectural MCP complet a **3 voies** :
- **npm stdio** (community subprocess JSON-RPC, secret env var process) — Airtable current `airtable-mcp-server@1.13.0`
- **vendor HTTPS remote** (Bearer/OAuth header, streaming SSE ou streamable-http) — e.g., Notion, Plane vendor MCPs
- **Claude Code plugin marketplace** (`@claude-plugins-official` scope, OAuth browser) — official 1st-party path

A0 D3 correction 2026-06-23 (post-screenshot) : "Use plugin marketplace pour 1st-party MCPs, pas npm stdio".

**Fix appliqué** : remplacer le pattern npm-stdio par `claude plugin install airtable@claude-plugins-official` → restart CC (D6 #4 STATIC tool registry) → `/plugin` menu → Authenticate OAuth → D1 verify 3 axes post-restart (`mcp__airtable__list_bases` / `list_tables` / `list_records`).

**D7 cost-of-escalation lesson** : quand user (A0) fournit des docs officielles screenshotées, **TRUST the docs over your prior model**. D1 verify (littéral lecture docs) remplace D-derive (spéculer sur la "vraisemblable" architecture). L'erreur Entry #5 = avoir spéculé sur la "vraisemblable" dichotomy sans avoir lu les docs Airtable officielles. Coût D-derive = 7-step runbook npm-stdio caduque à remplacer.

**D3 nuance préservée** : Entry #5 reste pertinent pour les MCPs communautaires (npm stdio) et Entry #7 ne le contredit pas, **il l'augmente** (3-pattern taxonomy au lieu de 2-pattern). Pour les 1st-party MCPs (Airtable, Notion, GitHub, etc.), préférer plugin marketplace. Pour les MCPs communautaires sans équivalent officiel, garder npm stdio ou vendor HTTPS selon disponibilité.

**Trigger généralisation** : avant d'installer un MCP, vérifier 3 patterns dans cet ordre de priorité :
1. **Plugin marketplace** (`@claude-plugins-official` scope) — preferred for 1st-party
2. **Vendor HTTPS remote** (Bearer/OAuth streaming) — preferred for vendor-official sans plugin
3. **npm community stdio** (subprocess + env var) — fallback pour communautaires

Pattern candidat Skill si 3+ occurrences → `/mcp-install-router` (recommande le bon pattern + commande verbatim).

**Ref** : `wiki/hand_offs/handoff_b1_solaris_airtable_config_2026-06-23.md` §"Étapes de câblage Airtable" v2 (5-step plugin marketplace).

### 2026-06-23 — ClickUp MCP Failed post-CC-restart : env var name mismatch `CLICKUP_API_KEY` vs `CLICKUP_API_TOKEN`

**Symptôme** : MCP panel A0 affiche `clickup ✘ Failed` après CC restart. Subprocess `clickup-mcp-server.cmd` crash au startup sans output visible dans le panel.

**D1 verify 3 axes indépendants** :
1. **Binaire npm** : ✔ `C:\Users\amado\AppData\Roaming\npm\clickup-mcp-server.cmd` existe, package `clickup-mcp-server@1.12.0` installé global.
2. **Env var CLICKUP_API_KEY** : ✔ set User scope, valeur `pk_50111322_AJFMK8ZSQ9W7GUVCX78HTR50WWC9JQXI` (PAT valide).
3. **Code source package** : ✘ `node_modules/clickup-mcp-server/build/clickup-client/index.js:52` throw `'CLICKUP_API_TOKEN environment variable is required'` — le package attend `CLICKUP_API_TOKEN` (PAS `_KEY`).

**Root cause** : **typo env var name mismatch**. A0 a wire `.mcp.json` avec `CLICKUP_API_KEY` (legacy naming convention) mais le package npm `@clickup-mcp-server@1.12.0` a rebrand `KEY` → `TOKEN` dans une version récente. Subprocess crash au startup throw → CC tool registry marque `Failed`.

**Fix appliqué** :
1. Set env var `CLICKUP_API_TOKEN` User scope = même valeur que `CLICKUP_API_KEY` (D7 backward compat).
2. Edit `.mcp.json` entry `clickup` : ajouter `CLICKUP_API_TOKEN` (le bon) en plus de `CLICKUP_API_KEY` (alias gardé pour autres outils A0 éventuels).
3. Backup `.mcp.json` vers `_TRASH_2026-06-23_clickup_rename/.mcp.json.before_clickup_token_rename.bak` (D4 no-hard-delete).

**D1 receipt post-fix** : `ClickUp MCP server running on stdio` + exit code 0 ✔.

**Ref** : `wiki/hand_offs/premortem_plugin_durability_2026-06-23.md` (pre-mortem sister) + MCP panel screenshot A0 2026-06-23 + `.mcp.json` ligne 137-145 post-edit + `~/.claude/_TRASH_2026-06-23_clickup_rename/.mcp.json.before_clickup_token_rename.bak` (proof backup).

**Trigger généralisation** : après CC restart, si MCP `Failed`, **D1 verify 3 axes** dans cet ordre :
1. Binaire / npm package présent (axe structure)
2. Env vars set (axe auth)
3. **Code source expectation** (axe contrat interface — souvent oublié) — `grep -r 'process.env\.' node_modules/<pkg>/build/` pour lister les vars attendues vs celles exposées dans `.mcp.json`.

Pattern candidat Skill si 3+ occurrences → `/mcp-envvar-auditor` (lit code source package + compare `.mcp.json` exposé + signale mismatch avant CC restart).

### 2026-06-23 — Airtable MCP Failed post-CC-restart : double root cause reliquat + 3rd cross-package convention

**Symptôme** : MCP panel A0 affiche `airtable ✘ Failed` post-restart (alors qu'il était `✔ Connected` avant). Screenshot A0 2026-06-23 22:48.

**D1 verify 3 axes indépendants** :
1. **Binaire npm** : ✔ `C:\Users\amado\AppData\Roaming\npm\airtable-mcp-server.cmd` existe, package `@airtable-mcp-server@1.13.0` installé global.
2. **Env vars set User scope** : ✔ 3 vars présentes : `AIRTABLE_PAT` (`pathRub...` reliquat 82 chars format suspect), `AIRTABLE_TOKEN` (fresh `patxie...` rotaté Test Key Pragma), `CLICKUP_API_KEY` (non-pertinent).
3. **Code source package** : ✘ `node_modules/airtable-mcp-server/dist/airtableService.js:11` throw `'No API key provided. Set it in the AIRTABLE_API_KEY environment variable'` — le package attend `AIRTABLE_API_KEY` (PAS `_PAT`, PAS `_TOKEN`).

**Root cause** : **double mismatch**.
- (a) `.mcp.json` référait `${env:AIRTABLE_PAT}` (reliquat suspect pathRub avec format key id 18 chars ≠ standard Airtable 14 chars).
- (b) `airtable-mcp-server@1.13.0` attend `AIRTABLE_API_KEY` (3rd convention cross-package, sister de ClickUp `CLICKUP_API_TOKEN` Entry #9).

**Fix appliqué** :
1. Set env var `AIRTABLE_API_KEY` User scope = `patxieFn45M3luYWb...` (même valeur que `AIRTABLE_TOKEN`).
2. Edit `.mcp.json` entry `airtable` ligne 130-138 : ajouter `AIRTABLE_API_KEY` (canonical) en plus de `AIRTABLE_TOKEN` + `AIRTABLE_PAT` (alias backward compat).
3. Backup `.mcp.json` → `_TRASH_2026-06-23_clickup_rename/.mcp.json.before_airtable_token_fix.bak` + `.before_airtable_api_key_fix.bak`.

**D1 receipt post-fix** : `airtable-mcp-server.cmd` startup exit 0, no throw ✔.

**Ref** : `wiki/hand_offs/premortem_plugin_durability_2026-06-23.md` §8 (Airtable update) + screenshot MCP panel A0 2026-06-23 22:48 + `.mcp.json` ligne 130-140 post-edit + 3 backups horodatés.

**Trigger généralisation (cross-package sister)** : 3 packages MCP A0 utilise, **3 conventions env var différentes** :

| Package | Env var canon attendu | Ref |
|---|---|---|
| `clickup-mcp-server@1.12.0` | `CLICKUP_API_TOKEN` | Entry #9 |
| `airtable-mcp-server@1.13.0` | `AIRTABLE_API_KEY` | Entry #11 |
| `desktop-commander` | (binary direct, no env) | Sister pre-mortem §2.2 |

**Pattern candidat Skill confirmé** : `/mcp-envvar-auditor` — automatise le `grep -r 'process.env\.' node_modules/<pkg>/build/` + diff avec `.mcp.json` exposé + propose fix AVANT CC restart. **3+ occurrences confirmées** (ClickUp + Airtable + trigger généralisation) → création Skill prioritaire (action #5 pre-mortem v2 §9).

**PathRub reliquat** : `AIRTABLE_PAT=pathRubST1d3zeEHX.a8fbddbfbf88774cf175f040ad7d1e0fa5b8ef85a6ff42ee323370fe0795fb6c` (length 82, key id `pathRub` 18 chars ≠ standard Airtable `pat` 14 chars). **D3 nuance** : format anomaly = potentially malicious namespace squat OU legacy token A0 a oublié. **A0 HITL** : manual revocation sur `airtable.com/create/tokens` (D7 + D4 no-env-var-removal sans permission).

### 2026-06-23 — Desktop Commander MCP Failed post-CC-restart : CC plugin marketplace manifest override required

**Symptôme** : MCP panel A0 affiche `plugin:desktop-commander:desktop-commander ✘ Failed` après CC restart (post-fix `.mcp.json` absolute path dans cache plugin). Premier fix `.mcp.json` au root cache plugin (`C:/Users/amado/.claude/plugins/cache/claude-plugins-official/desktop-commander/8c03d3392d16-53b37853/.mcp.json`) **non pickup** par CC.

**D1 verify 4 axes indépendants** :
1. **Subprocess DC test direct** : ✔ démarre silencieusement, no error visible.
2. **Subprocess DC spawn child check** : ✔ cmd.exe PID 31240 + child node.exe PID 40580 spawned, listening on stdio MCP.
3. **Plugin manifest priority** : ✘ CC lit `.claude/settings.json` enabledPlugins `desktop-commander@claude-plugins-official: true` → charge manifest `.claude-plugin/plugin.json` (relatif `command: "desktop-commander.cmd"`) **en priorité** sur le `.mcp.json` cache override.
4. **`~/.mcp.json` DC entry** : ✘ grep count = 0 avant fix (jamais wire en override marketplace).

**Root cause** : **Plugin marketplace manifest priorité sur cache `.mcp.json`**. CC discovery order :
- (1) `~/.claude/settings.json` enabledPlugins → load marketplace plugin
- (2) `.claude-plugin/plugin.json` mcpServers → spawn `command` (relatif → subprocess PATH lookup fail si PATH CC ≠ PATH user)
- (3) `.mcp.json` root home → override marketplace **SEULEMENT** si marketplace plugin désactivé

**Fix appliqué Option B (override marketplace)** :
1. Backup `~/.claude/settings.json` → `_TRASH_2026-06-23_clickup_rename/settings.json.before_dc_disable.bak` (D4).
2. Edit `~/.claude/settings.json` ligne 186 : `"desktop-commander@claude-plugins-official": true` → `false` (disable marketplace).
3. Backup `~/.mcp.json` → `_TRASH_2026-06-23_clickup_rename/.mcp.json.before_dc_add.bak` (D4).
4. Edit `~/.mcp.json` : add `desktop-commander` entry avec `command: "C:/Users/amado/AppData/Roaming/npm/desktop-commander.cmd"` (absolute path bypass PATH lookup).
5. D1 verify spawn post-fix : cmd.exe PID 31240 + child node.exe PID 40580 spawned ✔.

**Ref** : MCP panel screenshot A0 2026-06-23 23:05 + `~/.claude/settings.json` ligne 186 post-edit + `~/.mcp.json` lignes 148-152 post-edit + 2 backups horodatés 23:10.

**Trigger généralisation (cross-MCP)** : tout plugin marketplace avec manifest référençant `command` relatif (sans absolute path) est à risque si CC subprocess PATH ≠ user PATH. Pattern candidat Skill si 3+ occurrences → **`/mcp-marketplace-override`** (lit `.claude-plugin/plugin.json` + identifie commands relatifs + propose entry `~/.mcp.json` override avec absolute path + disable marketplace).

**Trigger Skill sister `/mcp-envvar-auditor`** (D6 #9+#11) : combine → **`/mcp-install-doctor`** : audit MCP complet (env vars + paths + marketplace priority).

## Enforcement

- **Append-only strict** : nouvelles entrées en bas du catalog (D4), jamais de modification d'entrées existantes (D4 no-amnesia, Règle d'Or #3).
- **Trigger Skill Creator Reflex** : si un pattern de root cause se répète 3+ fois dans le catalog → candidate à Skill (e.g., `/mcp-failure-diagnostic` quand 3+ entrées MCP-related).
- **Cross-link** : ADR-META-001 §D6 reste la doctrine ; ce ADR est le **journal** des applications de D6.
- **D1 receipts obligatoires** : chaque entrée DOIT citer au moins une preuve vérifiée (handoff, log, fichier, sortie de commande). Pas d'entrée "HYPOTHÈSE non vérifiée".

## Consequences

- ✅ Mémoire cumulative des root causes (réinjection évitée session après session).
- ✅ Pattern matching rapide sur "est-ce que j'ai déjà vu ce symptôme ?"
- ✅ Base d'évidence pour futures décisions MCP / tooling.
- ⚠ Maintenance cost : 1 entrée par root cause shipped (effort ~5 min par entrée, ROI ~30 min économisé par future occurrence).

## Related

- `ADR-META-001` §D6 — doctrine parente ("Quand on ne sait pas, on creuse le cas précis")
- `wiki/hand_offs/handoff_b1b2b3_loop_pivot_2026-06-23.md` — preuve D1 de l'entrée 2026-06-23
- `.claude/memory/MEMORY.md` §"D6 lessons shipped (à NE PAS re-découvrir)" — catalog sibling Graphify (10 leçons)
- `_SPECS/ADR/ADR-META-002_self-choice-autonomy.md` — D9 self-choice (complément à D6)
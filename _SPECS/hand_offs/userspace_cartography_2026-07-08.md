# User-Space Cartography — Amadeus — 2026-07-08

> **Mission origin** : sister-task `ASpace_OS_V3` publish. But avaler la cartographie
> D1-verifiée de `C:/Users/amado/` + OKF / Wiki / Graphify / DOX avant de piper.
>
> **Posture** : read-only (D5 receipts: find `-type f`, `wc -l`, `du -sh` — pas d'estimations).
> **Date scan** : 2026-07-08 (American timezone du syteme).
> **Périmètre** : `C:/Users/amado/` (root Trust Zone) — **3.3.1 — anti-casse**.

---

## 1. Cockpit personnel (apps lancées tous les jours)

### 1.1 Volumes par dossier racine

| Folder          | Size  | Files | Notes                                                  |
|-----------------|-------|-------|--------------------------------------------------------|
| `Desktop/`      | 163 M |    95 | Hub de lancement primaire (30+ `.lnk` + 2 screenshots) |
| `Downloads/`    |  17 G |   310 | Cave d'installs : AgentsRoom-1.105.0-x64.exe (mtime 2026-07-08 07:18) |
| `Documents/`    |  16 G | 2 084 | LIFE-GPT DATA EXPORT OFFICIAL, RILCOT shadow, Bilans   |
| `Pictures/`     | 1.3 G | 3 666 | Screenshots/ plein (shoot quotidien)                   |
| `Music/`        | 1.0 K |     1 | (vide — V2 n'écoute pas de musique locale)             |
| `Videos/`       | 6.0 K |     2 | (vide — vidéaste exogène)                              |
| `Favorites/`    | 3.0 K |     3 | Bing.url + Recents/ + Links/                           |
| `Contacts/`     | 5.7 M |     1 | Microsoft Contacts store                               |

### 1.2 Top 10 plus récents par mtime (cockpit only)

| mtime (epoch) | File |
|---|---|
| 1783568402 | `Pictures/Screenshots/Screenshot 2026-07-08 233944.png` |
| 1783568254 | `Pictures/Screenshots/Screenshot 2026-07-08 233719.png` |
| 1783567795 | `Pictures/Screenshots/Screenshot 2026-07-08 232955.png` |
| 1783539029 | `Pictures/Screenshots/Screenshot 2026-07-08 153027.png` |
| 1783516555 | `Pictures/Screenshots/Screenshot 2026-07-08 091554.png` |
| 1783514600 | `Pictures/Screenshots/Screenshot 2026-07-08 084320.png` |
| 1783512808 | `Pictures/Screenshots/Screenshot 2026-07-08 081322.png` |
| 1783509478 | `Downloads/AgentsRoom-1.105.0-x64.exe` (**D6 #NEW install**) |
| 1783509202 | `Pictures/Screenshots/Screenshot 2026-07-08 071321.png` |
| 1783508327 | `Pictures/Screenshots/Screenshot 2026-07-08 065846.png` |

### 1.3 Browser bookmarks (`.url`) — 30 fichiers, 1 seule dans Favorites (Bing.url)

### 1.4 Top 15 shortcuts `.lnk` sur `Desktop/` (tri par mtime desc)

| mtime | `.lnk` |
|---|---|
| 1782591587 | `MiniMax Code.lnk` |
| 1782590904 | `ZCode.lnk` |
| 1782590700 | `Comet.lnk` |
| 1782431677 | `Wispr Flow.lnk` |
| 1782401977 | `UiPath Studio.lnk` |
| 1782401976 | `UiPath Assistant.lnk` |
| 1782314351 | `Microsoft Edge.lnk` |
| 1780539114 | `VPS Hermes Workspace.lnk` |
| 1780481218 | `Hermes.lnk` |
| 1779405976 | `Antigravity IDE.lnk` |
| 1779337344 | `Zed.lnk` |
| 1779223375 | `Antigravity.lnk` |
| 1777139861 | `OpenCode.lnk` |
| 1776998360 | `Multica.lnk` |
| 1776222152 | `ASpace Vault.lnk` |

Hors-top-15 notables : `A Space OS.lnk`, `A'Space OS.lnk`, `Amd-PC Syncthing.lnk`,
`Bureau à distance Google Chrome.lnk`, `Candidate Home.lnk`, `Cursor.lnk`, `Gmail.lnk`,
`Google Chrome.lnk`, `OpenClaw Control (1).lnk`, `OpenClaw Mission Control (Amadou).lnk`,
`Paperclip.lnk`, `Supabase Studio.lnk` (+1), `Telegram.lnk`, `Wispr Flow.lnk`, `Zed.lnk`.

**D1-CONSTAT** : aucun `.lnk` ne pointe directement vers un projet
`C:/Users/amado/ASpace_*` — l'accès V2 se fait via Explorer ou terminal, pas via
Desktop shortcuts (volontaire ou D6 depuis la purge d'Asaph OS).

---

## 2. Mémoire canon A'Space

### 2.1 Wiki canon `00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/`

- **Size** : 17 M
- **Markdown pages** : 344
- **Last 10 modified** :
  1. `wiki/log.md` (mtime 2026-07-08 23:59 — append-only, log live)
  2. `wiki/wargames/wargame_01_mcp_durabilite_2026-07-08.md`
  3. `wiki/hand_offs/handoff_fable_window_audit_execution_2026-07-07.md`
  4. `wiki/hand_offs/handoff_persistent_loop_router_strategy_2026-07-06.md`
  5. `wiki/hand_offs/handoff_wf2_coaching_book_mavis_2026-07-06.md`
  6. `wiki/hand_offs/handoff_phase2_karpathy_loop_init_2026-07-06.md`
  7. `wiki/hand_offs/handoff_wargame_wf2_synthesis_book_coaching_2026-07-06.md`
  8. `wiki/hand_offs/handoff_wargame_wf2_b2_wonderwoman_finance_lens_2026-07-06.md`
  9. `wiki/hand_offs/handoff_wargame_wf2_b2_flash_product_lens_2026-07-06.md`
  10. `wiki/hand_offs/handoff_wargame_wf2_b2_superman_growth_lens_2026-07-06.md`

- **Sous-dossiers top-level** (15) :
  - `agent_capsules/` (+ `_TEMPLATE/`)
  - `audits/` (+ 3 × `_TRASH_<date>_audit_replaced` : 2026-06-15, 2026-07-02, 2026-07-03)
  - `comparisons/`, `concepts/`, `entities/`
  - `hand_offs/` (+ `Crew_Delegation_Log/`, `Morty_Global_Queue/`, `sessions_archive/`,
    `life_os_deploy_2026-06-17/`, `youtube_ingest_2026-06-14/`, `…_2026-06-15/` (×2),
    `…_2026-06-19/`, `…_2026-06-21/`, `…_2026-06-22/`, `_transcripts_raw/`)
  - `J01_Prime/LD01_Business/`, `J02_Bio/LD03_Health/`, `J02_Bio/LD04_Cognition/`,
    `J03_Nexus/LD02_Finance/`, `J03_Nexus/LD06_Family/`,
    `J04_Solarpunk/LD05_Social/`, `J04_Solarpunk/LD07_Creativity/`,
    `J04_Solarpunk/LD08_Impact/`
  - `L0/`, `signals/`, `sources/`, `syntheses/`, `wargames/`

### 2.2 Graphify outputs

| Path | Size | Top-level dirs | Chunks subdirs count |
|---|---|---|---|
| `ASpace_OS_V2/aspace-graphify-out/`  | **113 M** |     1 |     32 |
| `ASpace_OS_V2/graphify-out/`          |  11 M   |     1 |     80 |
| **Note** | Le second est plus petit (chunks x80 plus fins) — refresh post 2026-06-16 visible. ||
| `ASpace_OS_V2/_SPECS/graphify-out/`   |   ?     |     ? |     ? |
| `ASpace_OS_V2/_SPECS/graphify-out/2026-06-16/` | (date-stamped corpus) |
| `ASpace_OS_V2/_SPECS/graphify-out/cache/` | (temp cache) |

### 2.3 Specs (ADRs) — `_SPECS/`

- **Size** : 2.8 M
- **ADR `.md` files** total : **103** (incl. graphify + MCP)
- **JTBD `.md` files** total : 2
- **Catégories ADR** (premier niveau) :
  - `A0L_Identity_OS/`
  - `L0_Kernel_OS/`
  - `L0_Tech_OS/`
  - `L1_Life_OS/`
  - `L2_Business_OS/`
  - `graphify-out/` (+ cache + 2026-06-16/ snapshot)
  - `MCP/mcp-supabase-aspace-v0.1/`
  - `PRD/`, `REGISTRY/`
  - `heartbeat/`

### 2.4 Junction virtuelles à préserver V3

- `.claude/memory/wiki/` → `ASpace_OS_V2/00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/` (junction lrwxrwxrwx)
- `.mavis/` (mention MEMORY.md 2026-06-29) → `.minimax/`

---

## 3. MCPs actifs (depuis `.mcp.json`) — 24 serveurs

| # | Server name | Type | Backend |
|---|---|---|---|
| 1  | `context7`                | doc-fetch  | `context7-mcp.cmd` |
| 2  | `notion`                  | doc-fetch  | `notion-mcp-server.cmd` |
| 3  | `chrome-devtools`         | browser    | `chrome-devtools-mcp.cmd` |
| 4  | `playwright`              | browser    | `playwright-mcp.cmd` |
| 5  | `supabase`                | db         | `mcp-server-supabase.cmd` |
| 6  | `vercel`                  | deploy     | `vercel-mcp-pro.cmd` |
| 7  | `hostinger-dns`           | dns        | `hostinger-dns-mcp.cmd` |
| 8  | `symphony-supabase`       | twin stdio | `C:/Python314/python.exe` |
| 9  | `symphony-baserow`        | twin stdio | `C:/Python314/python.exe` |
| 10 | `symphony-affine`         | twin stdio | `C:/Python314/python.exe` |
| 11 | `symphony-obsidian`       | twin stdio | `C:/Python314/python.exe` |
| 12 | `symphony-plane`          | twin stdio | `C:/Python314/python.exe` |
| 13 | `supabase-omk`            | db (multi-tenant OMK) | `mcp-server-supabase.cmd` |
| 14 | `supabase-abc`            | db (multi-tenant ABC) | `mcp-server-supabase.cmd` |
| 15 | `vercel-omk`              | deploy (OMK) | `vercel-mcp-pro.cmd` |
| 16 | `vercel-abc`              | deploy (ABC) | `vercel-mcp-pro.cmd` |
| 17 | `transcript-api`          | YouTube-ingest | `C:/Python314/python.exe` |
| 18 | `airtable`                | db         | `airtable-mcp-server.cmd` |
| 19 | `clickup`                 | db         | `clickup-mcp-server.cmd` |
| 20 | `desktop-commander`       | local-FS   | `desktop-commander.cmd` |
| 21 | `AgentsRoom-Browser`      | IDE inside | `node` |
| 22 | `AgentsRoom-MCP`          | IDE        | `node` |
| 23 | `AgentsRoom-Test-Runner`  | IDE QA     | `node` |
| 24 | `AgentsRoom-QA-Tester`    | IDE QA     | `node` |

**D1-CONSTAT** : aucune valeur de token dans la table (D5 no-leak).
**Plugin `:plugin:` servers** : 0 — tous les serveurs sont au format `mcpServers.{name}`.

---

## 4. Claude Code config (`C:/Users/amado/.claude/`)

### 4.1 Rules — 112 fichiers `*.md` (hors `graphify-out/`)

**Top-level racine (13)** : `agents.md`, `code-review.md`, `coding-style.md`,
`context7.md`, `development-workflow.md`, `fable-autor-research-loop-symphony-agentos.md`,
`git-workflow.md`, `hooks.md`, `patterns.md`, `performance.md`, `security.md`, `testing.md`.

**Lang-spécifiques dans `rules/ecc/` (19 dirs)** : `angular/`, `arkts/`, `cpp/`,
`csharp/`, `dart/`, `fsharp/`, `golang/`, `java/`, `kotlin/`, `perl/`, `php/`,
`python/`, `ruby/`, `rust/`, `swift/`, `typescript/`, `web/`, `zh/`, `README.md`.

**Sub-canon** : `graphify-out/` (skipper — cache post Run #7).

### 4.2 Skills — 255 `SKILL.md` / 77 dossiers top-level + bundle `ecc/`

**Top-level dirs (77 skills sisters)** dont les 25 plus importants :
`a0l-grill`, `aaas-dashboard-port-audit`, `abc-os-backend-delegation`,
`abc-os-write-back-protocol`, `airtable-enrich`, `area-domain-doctrine-distill`,
`aspace-supabase-mastery`, `b1-filter`, `bridge-12wy-plane-gtd`, `canon-batch-spawn`,
`cloud-bootstrap`, `configure-ecc`, `context-bloat-detector`, `context7-mcp`,
`diagnose-proxy-boolean`, `fable-mode`, `find-docs`, `github-cli-orchestration`,
`graphify-swarm-burst`, `graphify-viewer`, `guide-cross-search`,
`guide-domain-stats`, `guide-index-builder`, `guide-search`, `guide-trim-large`,
`hostinger-dns-orchestration`, `l0-deploy-verify`, `l0-watchdog-scrape`.

**Bundle** : `skills/ecc/` contient ~180 skills de la suite ECC (agent-architecture-audit,
angular-developer, blender-motion-state-inspection, …).

### 4.3 Agents — 187 fichiers `.md`

**Top 10 noms canon A-Space** :
`a0-amodei-murderbot-meta-coach.md`, `a1-beth-veto.md`, `a1-morty-execution.md`,
`a1-rick-sovereignty.md`, `a2-uss-cerritos-chaos.md`, `a2-uss-discovery-balance.md`,
`a2-uss-enterprise-structure.md`, `a2-uss-orville-meaning.md`,
`a2-uss-protostar-liberation.md`, `a2-uss-snw-execution.md`.

**Autres notables** : `a3-cerritos-{boimler,freeman,mariner,rutherford,tendi}.md` (5),
`a3-discovery-{book,burnham,culber,georgiou,reno,saru,stamets,tilly}.md` (8),
`a3-enterprise-{data,geordi,picard,spock}.md` (4),
`a3-orville-*` (9), `a3-protostar-*` (4), `a3-snw-*` (5),
`b2-*` (8 managers), `b3-*` (53 techniciens Marvel/DC),
`architect`, `code-reviewer`, `security-reviewer`, `tdd-guide`, `doc-updater`,
`e2e-runner`, `refactor-cleaner`, `general-purpose`, `Plan`, `Explore`,
`a11y-architect`, `harness-optimizer`, `chief-of-staff`, `comment-analyzer`, …

**Dossier dormant** : `_S_L0_kernel_dormant/` (ne PAS publier avant Q4 2026).

### 4.4 Hooks — **10 scripts `.ps1`** + 2 × `hooks.json`

| File | Catégorie |
|---|---|
| `posttooluse-d1-receipt.ps1` | PostToolUse — D1 receive canonical |
| `posttooluse-skill-pocock-check.ps1` | PostToolUse — grill-me Pocock |
| `posttooluse-test-after-edit.ps1` | PostToolUse — real-test (anti-M3 laziness) |
| `sessionstart-distillation-stale.ps1` | SessionStart |
| `sessionstart-lessons-pending.ps1` | SessionStart |
| `sessionstart-load-disposition.ps1` | SessionStart — junction `~/.hermes/disposition.md` |
| `sessionstart-log-digest.ps1` | SessionStart — canon wiki/log + turn-journal |
| `sessionstart-premortem-pending-detector.ps1` | SessionStart |
| `stop-log-append.ps1` | Stop — `.claude/logs/turn-journal.md` |
| `subagent-start-tracker.ps1` | SubagentStart |

Config : `hooks.json` + `memory-persistence/hooks.json` + `memory-persistence/README.md`.

---

## 5. Fable Banque (doctrine vivante)

### 5.1 `fable-last-week-aspace/` — 425 K

- **Top-level** : `LEDGER.md`, `tasks/`, `wargames/`
- **Wargames detected** : 1 fichier `*wargame*` (probablement `LEDGER.md` lui-même porte ce nom canonique).
  **D6 #NEW check** : seul wargame matériel dans `fable-last-week-aspace` = `wargames/` dir.
  Les autres wargames vivent dans `wiki/wargames/` (voir 2.1).
- **Modules canon** : `SUCCESS-ASPACE` (probablement dans LEDGER.md),
  `TEMPORAL-CANON` (à confirmer en lecture), `tasks/` (input inbox Fable).

### 5.2 `agent-os/` — 72 M, **231 fichiers**

**Citadel dirs top-level (16)** : `audits/`, `cms/` (+ `cms/08_agents/`),
`collectors/` (+ `__pycache__/`), `cron/` (+ `cron/output/` + `cron/simspace/`),
`data/`, `decisions/`, `logs/`, `loops/` (+ `loops/artifacts/{docs,signals,tasks,tickets}/`,
`loops/domains/{w-star,wf0-spock,wf1-morty,wf2-book,wf3-mirofish}/`, `loops/logs/`),
`static/`, `tools/`, `worktrees-multiplex/`, `__pycache__.bak/`.

**Rôle citadel** : WF0 Spock = ledger master canonique, source des wargames Fable 5.
**Collectors** : `citadel/collectors/` (compte à préciser — au runtime).
**Cron** : `citadel/cron/` + `citadel/cron/output/` + `citadel/cron/simspace/`.
**Signals artifacts** : `citadel/loops/artifacts/signals/` — bus for fleet signals.

---

## 6. Caches & IDEs (NE PAS publier V3)

| Cache | Size | Notes |
|---|---|---|
| `.antigravity-ide/`        | **2.8 G** | Heavy — extensions + `graphify-out/` interne. **D6 #NEW** : ce dossier est 4× la taille du wiki canon. |
| `.vscode/extensions/`      |  26 dossiers | Vendors (non compté fichier-par-fichier). OK à exclure V3. |
| `AppData/Local/Programs/Pane/` | **NOT FOUND** | RunPane non installé à ce path — le spec mentionnait Pane mais le dossier n'existe pas dans `AppData/Local/Programs/`. **D6 #NEW** : soit autre path, soit uninstalled. |
| `.claude.json`             | _ne pas scanner_ | Contient historique sessions (D7 cost-of-escalation si leak). À exclure canonique V3. |
| `node_modules/` partout | _skip_ | Toujours exclu `.gitignore`. |
| `.cache/`, `.npm/`, `.bun/` | _skip_ | Holdings npm runtime. |

---

## 7. OKF / DOX / Memory Core

### 7.1 OKF (Méta-Mémoire canon, c'est quoi?)

| File | Path |
|---|---|
| Plan canon OKF | `C:/Users/amado/.claude/plans/plan-meta-memoire-okf-wiki-graphify-dox.md` |
| Spec OKF in Temp | `C:/Users/amado/AppData/Local/Temp/okf-spec.md` |

**D1-CONSTAT** : OKF est dans un plan canon (`plan-meta-memoire-okf-wiki-graphify-dox.md`)
+ spec temp `okf-spec.md`. Le plan est le document de référence canonique.
**9 phases W3 → W13**, familles `AGENTS.md` + `CLAUDE.md` bi-familles.

### 7.2 DOX (Distributed Object eXchange?)

| File | Path |
|---|---|
| Plan canon DOX  | `C:/Users/amado/.claude/plans/plan-meta-memoire-okf-wiki-graphify-dox.md` (mêmes lignes) |
| Spec DOX agents  | `C:/Users/amado/AppData/Local/Temp/dox-agents.md` |
| Spec DOX readme  | `C:/Users/adoo/AppData/Local/Temp/dox-readme.md` |
| `01-superintelligence-anthropic-paradoxes.md` | plusieurs occurrences dans graphify chunks |
| `shadow-l1-agent-zero/api/*.dox.md` (≥ 3) | shadow twin Self-Generated DOX |

### 7.3 Memory Core

| File | Path |
|---|---|
| `memory-core-readme.md` | `C:/Users/amado/.claude/memory/memory-core-readme.md` |
| `memory-core-readme.md` (in chunks) | `C:/Users/amado/.claude/graphify-out/chunks/chunk_002/memory-core-readme.md` |

### 7.4 Conclusion

**OKF + DOX + Memory Core sont des concepts liés** mais pas des apps séparées —
ils vivent comme plan canon + spec temp + chunks graphify + shadow twins. **D6 #NEW
observation** : aucun dossier racine dédié (`OKF/`, `DOX/`, `Memory_Core/`) — ils
sont des abstractions, pas des artefacts filesystem.

---

## 8. `.pane/` cockpit — 13 M

| Top-level dir | Files | Notes |
|---|---|---|
| `.claude/` | ? | Sub-cockpit CC (jonction symétrique) |
| `.codex/` | ? | Sub-cockpit Codex CLI |
| `images/` | ? | Assets runtime |
| `logs/` | 2 fichiers datés | `pane-2026-07-07.log`, `pane-2026-07-08.log` (logs live V3 sister) |
| `skills/` | **376 fichiers** | Bundle Pane skills : `dcouple`, `pane-chat`, `.sources/` |
| `sockets/` | 0 fichiers visibles | IPC Pane — vide à l'instant t |
| `_TRASH_2026-07-08_orchestrator_switch/` | ? | Trash post-orchestrator-swap |

**Worktrees** : 0 dossiers détectés matching `*worktree*` à maxdepth 4.
**Skills count total** : 376 fichiers dans `skills/`.

---

## RECOMMANDATIONS V3 (sister task publish)

### Inclure (canon actif)

- `ASpace_OS_V2/` (entier — sauf démos V2 explicitement `_TRASH`)
- `.claude/CLAUDE.md` (racine canonique)
- `.claude/rules/` racine 13 + `ecc/` lang-spécifiques (19 dirs)
- `.claude/skills/` (255 SKILL.md ≈ 77 sisters + 180 ecc)
- `.claude/agents/` (187, sauf `_S_L0_kernel_dormant/`)
- `.claude/hooks/` (10 ps1 + 2 hooks.json)
- `.claude/memory/` (junction wiki + canonique MEMORY.md + 18 memory files)
- `wiki/` via junction (17 M, 344 pages)

### Exclure (secrets / cache / heavy)

- `.claude.json` (historique sessions — D5 + D7)
- `.antigravity-ide/` (2.8 G, extensions)
- `.vscode/extensions/`
- `AppData/` running state
- `.npm/`, `.bun/`, `.cache/`
- `node_modules/` universels
- `.claude/plans/` (sensibles draft OKF si tu ne veux pas que DOX leak avant stabilisation)
- `Downloads/AgentsRoom-1.105.0-x64.exe` (artefact installer — installer.log)

### Risques (D6 lessons shipping)

1. **D6 #C-1** : `.claude.json` peut contenir `mcp__*` tokens historiques si jamais
   une clé y a été collée en plain. **À grep `sk-`, `ghp_`, `Bearer` avant publish**.
2. **D6 #C-2** : 24 MCP servers actifs, mais `.mcp.json` ne dump QUE les commandes
   (pas les env vars). Les tokens sont soit dans `.claude/.mcp.json` soit dans
   `process env` au runtime — à vérifier avant V3 sister publish.
3. **D6 #C-3** : `fable-last-week-aspace` n'a qu'**1** wargame détecté sous
   `wargames/` — peut signifier que les wargames canoniques vivent dans `wiki/`
   (`.md` files inside `wiki/wargames/` = `wargame_01_mcp_durabilite_2026-07-08.md`).
   Cartographie cohérente.
4. **D6 #C-4** : RunPane pas installé au path canon — soit uninstalled, soit en
   alternate location (`.pane/` is the cockpit runtime mais l'app Pane elle-même
   n'est pas dans `Programs/Pane/`). À confirmer en B2 Batman avant V3.
5. **D6 #C-5** : OKF / DOX / Memory Core = concepts, pas artefacts filesystem.
   Plan canon = `.claude/plans/plan-meta-memoire-okf-wiki-graphify-dox.md` — copy
   verbatim in V3 hand_offs pour préserver la promesse anti-amnesia.

### Anti-pattern prevention (DOX)

- Ne pas publier de screenshots (`Pictures/Screenshots/`) qui contiennent des PHI
  ou clés.
- Ne pas publier `Documents/RILCOT - Shortcut.lnk` (cible externe privée).
- Ne pas publier `Documents/GPT DATA EXPORT OFFICIAL/` — données personnelles.

---

## D1 RECEIPTS — cette cartographie

| Item | Source | Bash command |
|---|---|---|
| 24 MCPs | `.mcp.json` | `python -c "import json; print(json.load(open('…/.mcp.json'))['mcpServers'].keys())"` |
| 344 wiki pages | `wiki/` | `find … -type f -name "*.md" \| wc -l` |
| 103 ADRs | `_SPECS/ADR/` | `find … -type f -name '*.md' -not -path '*graphify*' \| wc -l` |
| 255 SKILL.md | `.claude/skills/` | idem |
| 187 agents | `.claude/agents/` | idem |
| 112 rules | `.claude/rules/` | idem |
| 10 ps1 hooks | `.claude/hooks/` | `find … -name "*.ps1"` |
| 19 dirs `rules/ecc/` | sub-count | `find … -type d` |
| 8 sub-dirs `wiki/` Life Wheel | `J01..J04` | `find wiki -type d` |
| Cockpit sizes | `du -sh` | idem |
| 16 .lnk (Desktop) | `find … -name "*.lnk"` | idem |
| 30 .url bookmarks | `find Favorites` | idem |

---

## Conclusion (D7 cost-of-escalation)

Cette cartographie est **suffisante pour ouvrir `ASpace_OS_V3` sister task**
sans rien oublier du canon vivant. **3 paquets critiques** à préserver :

1. **Wiki canon** : `.claude/memory/wiki/` junction (17 M, 344 pages)
2. **Claude config runtime** : `.claude/{rules,skills,agents,hooks}` (112 + 255 + 187 + 10)
3. **MCP wiring** : `.mcp.json` (24 servers) + Python 3.14 stdio twins

D4 append-only : ce rapport ne modifie aucun canon — il observe et consigne.

**Cartographie D1-verifiée. Ready pour V3 sister task publication.**

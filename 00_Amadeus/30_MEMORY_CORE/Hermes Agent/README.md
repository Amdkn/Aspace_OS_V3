---
source: Claude Architect (Opus 4.7) + Codex / Rick A1 — collaborative docs
date: 2026-05-17
type: archive-index-and-retrogradation-doctrine
domain: L0_Tech_OS / Hermes_Agent
tags: [#Hermes #Kanban #docs-dogmatique #SSHFS-isolation #context7-validated #WSL2 #ADR-RICK-002]
version_doc: Hermes Agent v0.13.0 (2026.5.7)
status: CLOSED_RUNTIME — retained as archive and LLM Wiki abstraction source
related:
  - ADR-RICK-002_paperclip-deprecation-hermes-promotion
  - SDD-010_meta-cloture-scope-13eme-semaine (§5.6 + future §5.7 Docs Dogmatique)
  - 00_Amadeus/05_OSS_Twin/symphony/L0/open-hermes-runtime.md
single_entry_point: true
canonical_role: "Archive entry point — Hermes is retrograded; use LLM_Wiki + Symphony + Shadow L0 Executor Mesh"
---

# Hermes Agent — Archive / Retrogradation Entry Point

> **Decision 2026-05-17:** Hermes Agent is no longer a required runtime for A'Space L0.
> It is now an archive and abstraction source for `LLM_Wiki`.
> For live work, use `LLM_Wiki + Symphony + Shadow L0 Executor Mesh` (Codex CLI, Gemini CLI, Claude Code CLI via MiniMax).

---

## 0. Stade Actuel — 2026-05-17

| Composant | État | Détail |
|---|---|---|
| Hermes runtime | 🔻 retrograded | Ne plus réparer pendant ce cycle sauf mission explicite (cf. doc 13) |
| Hermes docs | ✅ archive | Source historique pour LLM Wiki, MiniMax, Context7 hooks, Symphony credentials |
| LLM Wiki abstraction | ✅ active | `LLM_Wiki/wiki/entities/entity_shadow_l0_executor_mesh.md` |
| Codex CLI Shadow L0 | ✅ configured | Profils `shadow_l0_safe`, `shadow_l0_exec`, `shadow_l0_yolo` dans `C:\Users\amado\.codex\config.toml` |
| Provider MiniMax | 🟡 Claude Code target | MiniMax-M2.7 Token Plan reste cible Anthropic-compatible pour Claude Code CLI (cf. doc 14 + doc 08) |
| Symphony Plane/Baserow credentials | ✅ installed | `PLANE_API_KEY` + `BASEROW_DATABASE_TOKEN` présents dans `/home/amadeus/.hermes/.env` (cf. doc 11) |
| Codex Context7 MCP | ✅ configured | `context7` ajouté dans `C:\Users\amado\.codex\config.toml` (cf. doc 09) |
| Codex Context7 Hooks | ✅ configured | `SessionStart`, `UserPromptSubmit`, `PreToolUse` dans `C:\Users\amado\.codex\hooks.json` (cf. doc 10) |
| WSL2 / Hermes networking | 🔻 non-critical | Ne doit plus bloquer Shadow L0 |
| Isolation WSL↔Windows | ✅ SSHFS | Pas de `/mnt/c` (cf. doc 07 §Isolation Rule) |

**Live replacement path** :
- `LLM_Wiki` — memory / identity / org chart
- `Symphony` — router / tracker reader / payload normalizer
- `Codex CLI` — default executor
- `Gemini CLI` — high-quota scout/doer
- `Claude Code CLI + MiniMax` — Claude-style bulk executor

---

## 1. 🪐 Doctrines actives — à respecter par tout agent

### 1.1 Loi Docs Dogmatique (cf. SDD-010 §5.7 future)

> **Avant toute configuration d'un outil tiers, l'agent DOIT** :
> 1. Lire les sections officielles : **Architecture, Configuration, Security, FAQ, Best Practices**
> 2. Consulter **Context7** MCP server pour la version exacte si disponible (`/nousresearch/hermes-agent`)
> 3. Lire le **README + .env.example + Issues récents** du repo GitHub
> 4. Produire un **plan d'exécution unique** (pas trial-and-error)
> 5. Vérifier les **commandes setup natives** (`X setup`, `X install`, `X bootstrap`) avant créer du custom
>
> **Anti-pattern interdit** : *"essayer → erreur → ajuster → essayer"* sur un runtime live.

→ Cette doctrine a été **prouvée empiriquement** le 2026-05-15 : 1h de trial-and-error vs 2 queries Context7 ont donné la vérité officielle (cf. `01_installation-setup.md`).

### 1.2 Loi SSHFS Isolation (Codex, doc 07 §Isolation Rule)

> **Ne JAMAIS utiliser `/mnt/c` / DrvFS comme couche d'intégration durable entre Windows et WSL pour Hermes Agent.**
>
> Boundary approuvée :
> ```
> Windows <-> SSHFS <-> WSL
> ```
>
> Exception bootstrap autorisée :
> - Windows Task Scheduler peut invoquer `wsl.exe`
> - PowerShell peut transmettre un payload command via `bash -lc` (base64 stdin)
> - WSL ne doit PAS dépendre de paths `/mnt/c/...` pour démarrer Hermes

→ Rationale : préserve isolation WSL, évite couplage filesystem Windows dans services Linux, garde Hermes anchored dans `/home/amadeus`.

### 1.3 Stack chinoise frugale (SDD-009 §8 + doc 08)

> Default LLM = **MiniMax-M2.7** via API Anthropic-compatible (`https://api.minimax.io/anthropic`)
> Fallback = GLM 4.7 Flash via OpenRouter
> Premium réservé = Claude Anthropic-cloud (Rick A1 critique only)

---

## 2. 📚 Inventaire des fichiers — Ordre de lecture suggéré

| # | Fichier | Auteur | Mission |
|---|---|---|---|
| **00** | `00_session-handoff-20260515.md` | Claude Opus 4.7 | Handoff session install initiale — état post-install WSL |
| **01** | `01_installation-setup.md` | Claude | Install WSL2, `hermes setup`, providers, `config.yaml` |
| **02** | `02_architecture-services.md` | Claude | Gateway + Dashboard + API Server, ports, systemd flow |
| **03** | `03_security-best-practices.md` | Claude | API_SERVER_KEY, 7 couches de sécurité, anti-patterns |
| **04** | `04_wsl2-networking.md` | Codex | Mirrored vs NAT, accès Dashboard depuis Windows, port forwarding, lingering |
| **05** | `05_aspace-integration.md` | Codex | Mapping Hermes B2 ↔ A'Space (DC/Marvel/SOUL.md/Kanban→Symphony states) |
| **06** | `06_mcp-tools-config.md` | Codex | MCP servers (filesystem, GitHub, Brave, custom A'Space bridges) |
| **07** | `07_persistence-state-20260516.md` | Codex / Rick A1 | Windows Task Scheduler + **SSHFS Isolation Rule** + verification commands |
| **08** | `08_minimax-token-plan-config-20260516.md` | Codex / Rick A1 | Provider MiniMax-M2.7 + Anthropic-compatible + Token Plan + `Set-HermesMiniMaxKey.ps1` |
| **09** | `09_context7-codex-mcp-config-20260516.md` | Codex / Shadow L0 | Context7 MCP configuré pour Codex + usage systémique Docs Dogmatique |
| **10** | `10_context7-codex-hooks-config-20260516.md` | Codex / Shadow L0 | Hooks Codex Context7 : SessionStart, UserPromptSubmit, PreToolUse |
| **11** | `11_symphony-shadow-l0-api-credentials-20260516.md` | Codex / Shadow L0 | Liens API + paths Symphony + état credentials Plane/Baserow redacted |
| **12** | `12_symphony-baserow-plane-smoke-test-20260516.md` | Codex / Shadow L0 | Smoke test W1 Solaris : Baserow OK, Plane API bloqué HTTP 403 |
| **13** | `13_hermes-retrogradation-shadow-l0-20260517.md` | Codex / Shadow L0 | Fermeture runtime Hermes : archive + abstraction LLM Wiki |
| **14** | `14_shadow-l0-executor-mesh-codex-strategy-20260517.md` | Codex / Shadow L0 | Stratégie Codex/Gemini/Claude+MiniMax comme remplacement Hermes/OpenClaw/Paperclip |
| **15** | `15_final-handoff-hermes-to-llm-wiki-20260517.md` | Codex / Shadow L0 | Handoff final Hermes -> LLM Wiki pour Claude Code et Gemini CLI |

**Scripts** (`scripts/`) :
- `Start-HermesAgent.ps1` — Bootstrap Windows (lance via wsl.exe sans /mnt)
- `start-hermes-agent.sh` — Payload shell exécuté dans WSL
- `Set-HermesMiniMaxKey.ps1` — Installation sécurisée clé MiniMax (masked input)

**Logs** (`logs/`) :
- `hermes-startup-YYYYMMDD_HHMMSS.log` — Startup logs Task Scheduler

---

## 3. 🏗️ Architecture Hermes en 5 phrases (mémoriser)

1. **Hermes Agent** = noyau (CLI + skills + memory + sessions) → invoqué via `hermes` command
2. **Gateway** = process long-running qui héberge messaging platforms + API server
3. **Dashboard** = UI web **séparée** lancée par `hermes dashboard` sur port 9119 (Kanban + Sessions + TUI chat)
4. **API Server** = REST API exposée par le gateway (port 8642) — bind `0.0.0.0` requiert `API_SERVER_KEY`
5. **Workspace** = UI tierce de `outsourc-e/hermes-workspace` qui se connecte au gateway via `HERMES_API_URL`

```
Windows Task Scheduler (logon +30s)
  ↓ wsl.exe + payload base64 via bash -lc (PAS /mnt/c)
WSL ASpace-L0 (Ubuntu 24.04, systemd, linger enabled)
  ├── hermes-gateway.service     → 0.0.0.0:8642
  ├── hermes-dashboard.service   → 127.0.0.1:9119 (TUI + Kanban)
  └── hermes-workspace.service   → 0.0.0.0:3000  (Vite outsourc-e)
       ↑
       Browser Windows ← localhost (mirrored mode) ou WSL IP (NAT mode)
       Pinned Windows app (browser shell)
```

→ **Source officielle** : Context7 `/nousresearch/hermes-agent` (High reputation, 13026 snippets)

---

## 4. ⚡ Commandes essentielles (cheat-sheet)

```bash
# Status (depuis WSL ASpace-L0)
systemctl --user is-active hermes-gateway hermes-dashboard hermes-workspace
hermes gateway status
hermes doctor

# Restart
systemctl --user restart hermes-gateway hermes-dashboard hermes-workspace

# Logs live
journalctl --user -u hermes-gateway -f

# Verify ports
ss -tlnp | grep -E ':8642|:9119|:3000'

# Test HTTP interne
curl -fsS http://127.0.0.1:8642/health
```

```powershell
# Depuis Windows PowerShell
Get-ScheduledTask -TaskName "Hermes Agent Persistent Startup"
Get-ScheduledTaskInfo -TaskName "Hermes Agent Persistent Startup"
Invoke-WebRequest -UseBasicParsing http://127.0.0.1:8642/health
Invoke-WebRequest -UseBasicParsing http://127.0.0.1:9119

# Installation MiniMax key (masked input)
powershell.exe -NoProfile -ExecutionPolicy Bypass -File ".\scripts\Set-HermesMiniMaxKey.ps1"
```

---

## 5. ⚠️ Dettes connues — à traiter par next agent

| # | Dette | Source | Action |
|---|---|---|---|
| 1 | **MINIMAX_API_KEY non installée** | Doc 08 | Lancer `Set-HermesMiniMaxKey.ps1` localement (masked input) |
| 2 | **WSL2 Mirrored mode** non activé | Doc 04 §1.2 + Doc 00 | Éditer `C:\Users\amado\.wslconfig` |
| 3 | **ADR-WSL-002** ports isolation à formaliser | Doc 05 §8 + Doc 04 §2.1 | Créer ADR dans `_SPECS/ADR/` |
| 4 | **Skill `donna-escalate`** à créer | Doc 05 §5.2 | `hermes skill create donna-escalate` |
| 5 | **MCP servers** à configurer (filesystem, github, etc.) | Doc 06 §2 | Ajouter dans `~/.hermes/config.yaml` |
| 6 | **Secrets en cleartext** ~/.hermes/.env | Doc 07 Residual Notes | Rotater clés exposées si screenshots/chat |
| 7 | **2 issues `hermes doctor`** non auto-fixées | Doc 00 | `hermes setup` pour API keys manquantes (optionnel) |
| 8 | **Doctrine "Docs Dogmatique"** pas encore en ADR | README §1.1 | Créer `ADR-DOCTRINE-001_docs-dogmatique.md` |
| 9 | **Doctrine "SSHFS Isolation"** pas encore en ADR | README §1.2 + Doc 07 | Créer `ADR-WSL-003_sshfs-isolation.md` |
| 10 | **Plane/Baserow keys exposées dans chat** | Doc 11 §6 | Rotater après smoke test, puis mettre à jour `/home/amadeus/.hermes/.env` par flux masked/local |
| 11 | **Plane API 403** sur `aspace-core` | Doc 12 §5 | Rotater clé Plane / vérifier scope workspace, puis relancer création des 3 work-items W1 Solaris |
| 12 | **Heartbeat manquant dans le mesh Shadow L0** | Doc 13 §8 + Doc 14 §6 | Créer capsules `Heartbeat.md` par agent, puis automatiser via Symphony ou Codex heartbeat |
| 13 | **Gemini/Claude Code configs non normalisées** | Doc 14 §10 | Documenter leurs settings sans secrets, puis relier à LLM Wiki |
| 14 | **Terminaux déjà ouverts sans alias/PATH Codex** | Doc 15 §4 | Relancer terminal ou exécuter `$env:Path = "C:\Users\amado\AppData\Local\OpenAI\Codex\bin;$env:Path"; . $PROFILE` |

---

## 6. 🔄 Protocole de Mise à Jour — pour TOUT nouvel agent ajoutant un fichier

> **RÈGLE** : Toute création d'un nouveau fichier `NN_descriptif-YYYYMMDD.md` dans ce dossier DOIT être suivie d'une mise à jour de ce README.

### 6.1 Workflow obligatoire

```
1. Créer le nouveau fichier `NN_*.md` (numéro suivant, suffixe date si state-doc)

2. Frontmatter YAML obligatoire :
   ---
   source: <agent> / <persona>
   date: YYYY-MM-DD
   type: <docs-synthesis | configuration-state | session-handoff | provider-config | ...>
   domain: L0_Tech_OS / Hermes_Agent
   tags: [#Hermes ...]
   status: <active | pending-secret | superseded | ...>
   ---

3. Footer obligatoire :
   *Documenté Docs Dogmatique — <thème> — YYYY-MM-DD — <agent>*

4. Mettre à jour README.md :
   a. §0 "Stade Actuel" — refléter changements d'état
   b. §2 "Inventaire" — ajouter la ligne du nouveau fichier
   c. §5 "Dettes connues" — si la nouvelle doc révèle/résout une dette
   d. Frontmatter `date:` du README → date de la mise à jour
   e. Frontmatter `version_doc:` si version Hermes change

5. Optionnel : §3-4 si l'architecture/commandes changent fondamentalement
```

### 6.2 Conventions

| Convention | Règle |
|---|---|
| **Numérotation** | Séquentielle (`01`, `02`, ... `09`, puis `10`). Pas de saut. |
| **Préfixe `00`** | Réservé aux **session handoffs** datés |
| **Date dans nom fichier** | Obligatoire pour state-docs (`07_persistence-state-20260516.md`) ; optionnel pour docs-synthesis stables (`04_wsl2-networking.md`) |
| **Frontmatter `source`** | Indiquer l'auteur (Claude Architect, Codex, Antigravity, etc.) |
| **Footer Docs Dogmatique** | Toujours présent pour signaler conformité doctrine |
| **Cross-refs** | Préférer `Doc NN §X.Y` (lisible) que paths complets |
| **Backup avant edit majeur** | `~/.hermes/<file>.bak.YYYYMMDD_HHMMSS` (côté WSL) |

### 6.3 Quand créer un nouveau fichier vs amender un existant

| Cas | Action |
|---|---|
| Configuration durable (provider, persistence, MCP) | **Nouveau fichier** numéroté |
| State snapshot (post-install, post-cleanup) | **Nouveau fichier** avec date suffixe |
| Session handoff entre agents | **Nouveau fichier** `00_session-handoff-YYYYMMDD.md` |
| Correction d'une erreur mineure dans doc existante | **Amender** + ajouter ligne "Mise à jour YYYY-MM-DD : ..." |
| Supersedure complète d'une doc | **Nouveau fichier** + marquer ancien `status: superseded` dans frontmatter |

---

## 7. 🎯 Pour Codex / Antigravity / Claude — comment me lire

### Si tu démarres une session de continuation :

```
1. Read README.md (CE FICHIER) — tu y es ✓
2. Read 00_session-handoff-*.md (le plus récent) — état exact à l'heure du handoff
3. Read 07_persistence-state-*.md — comprendre la persistance Windows + SSHFS rule
4. Si touche au provider LLM → Read 08_minimax-token-plan-config-*.md
5. Si touche à l'architecture → Read 02_architecture-services.md + 04_wsl2-networking.md
6. Si touche à l'intégration A'Space → Read 05_aspace-integration.md
7. Si touche aux MCP servers → Read 06_mcp-tools-config.md
8. Si touche à la sécurité → Read 03_security-best-practices.md
9. Si touche à l'install from scratch → Read 01_installation-setup.md
```

### Si tu veux ajouter une feature/config :

```
1. Vérifier que Context7 a la doc à jour (`mcp__context7__resolve-library-id` puis `query-docs`)
2. Suivre Loi Docs Dogmatique §1.1
3. Respecter Loi SSHFS Isolation §1.2 (jamais /mnt/c)
4. Créer le fichier `NN_*.md` selon §6.1 protocole
5. Mettre à jour ce README selon §6.1 step 4
```

---

## 8. 🔗 Cross-refs Canon V0 (immutable)

| Doc Canon | Lien avec Hermes |
|---|---|
| **SDD-009** §3 Architecture tri-tier B1/B2/B3 | Hermes EST le B2 Kanban Manager |
| **SDD-010** §5.2 TARDIS Inversé | Hermes orchestre via Donna→Doctors→Rick chain |
| **SDD-010** §5.7 (future) | Doctrine Docs Dogmatique sera formalisée ici |
| **ADR-RICK-001** OpenHarness Incarnation | Distinct de Hermes Agent (OpenHarness = Rick A1, Hermes = B2) |
| **ADR-RICK-002** Paperclip Deprecation + Hermes Promotion | Justifie cette migration entière |

---

## 9. Sources Context7 validées

- `/nousresearch/hermes-agent` — Source Reputation: **High**, 13026 snippets, v2026.4.16 indexed
- `/websites/hermes-agent_nousresearch` — Mirror site officiel
- GitHub `nousresearch/hermes-agent` — Repo source canonique
- MiniMax official docs (cf. doc 08 §Sources)

**À re-valider** dès qu'une nouvelle version Hermes Agent paraît (re-fetch via Context7).

---

## 📜 Historique du README

| Date | Auteur | Changement |
|---|---|---|
| 2026-05-15 | Claude Opus 4.7 | Création initiale — 4 fichiers (01-03 + README) |
| 2026-05-15 | toi/linter | Index étendu à 7 fichiers (ajout 04-06 Codex) |
| 2026-05-16 | Claude Opus 4.7 + Codex collaboration | Refonte complète : entry point unique + Loi SSHFS + §6 Protocole Mise à Jour + 9 fichiers (00-08) |
| 2026-05-16 | Codex / Shadow L0 | Ajout Doc 09 : Context7 MCP configuré pour Codex (`~/.codex/config.toml`) |
| 2026-05-16 | Codex / Shadow L0 | Ajout Doc 10 : hooks Codex pour usage systémique Context7 |
| 2026-05-16 | Codex / Shadow L0 | Ajout Doc 11 : credentials Plane/Baserow installés dans `~/.hermes/.env` avec valeurs redacted |
| 2026-05-16 | Codex / Shadow L0 | Ajout Doc 12 : smoke test Baserow -> Plane pour W1 Solaris, bloqué par Plane HTTP 403 |
| 2026-05-17 | Codex / Shadow L0 | Fermeture runtime Hermes : rétrogradation vers archive/abstraction LLM Wiki |
| 2026-05-17 | Codex / Shadow L0 | Ajout Doc 14 : Codex CLI configuré en executor Shadow L0 avec profils safe/exec/yolo |
| 2026-05-17 | Codex / Shadow L0 | Ajout Doc 15 : handoff final Hermes -> LLM Wiki + fix alias/PATH Codex PowerShell |

---

*README mis à jour 2026-05-17 — Codex / Shadow L0 — Hermes retrograded; LLM Wiki + Symphony + Executor Mesh active*
*Ce fichier est désormais l'entry point d'archive, pas le chemin runtime.*
*Protocole de mise à jour : §6 obligatoire pour tout nouveau fichier dans ce dossier.*

---
session: agent-a7bdaa1bbc6378000
projet: wf_d1e09957-b2d
debut: 2026-08-09T02:57:59.925Z
fin: 2026-08-09T03:03:55.539Z
messages_utilisateur: 1
reponses_assistant: 3
---

## >>> UTILISATEUR #1

Audit the Agent OS codebase at c:/Users/amado/agent-os. The user calls it "a complete fiasco". Your job is to map what exists, what works, and what does not.

Specifically inventory these subsystems and produce a compact report:
1. /c/Users/amado/agent-os/citadel/ — what does serve.py expose? What do the collectors actually do? Are they live or stale (look for _TRASH_ folders and dates)?
2. /c/Users/amado/agent-os/desktop/ — React/Vite app at port 5180, what screens/panels exist, what state shape, what is wired to a backend?
3. /c/Users/amado/agent-os/observatoire/ — Python server + static HTML, what does it show, what feeds it?
4. /c/Users/amado/agent-os/home-court/gstack/ — looks like a vendored gstack, is it used?
5. /c/Users/amado/agent-os/hermes-workspace-repo/ — vendored? orphaned?
6. /c/Users/amado/agent-os/commands/agent-os/ — what Claude Code commands exist?
7. /c/Users/amado/agent-os/scripts/ — what do the bash scripts do?
8. /c/Users/amado/agent-os/citadel/CLAUDE.md and /c/Users/amado/agent-os/README.md — what is the documented intent vs what code actually does?

For each subsystem, return: a one-line purpose, the entry point, current state (live/stale/broken), and the most damning evidence (file path + a 1-line quote or count). Group findings by CAUSE not by surface — multiple dead-looking surfaces may share one root cause. End with the top 3-5 root causes that explain "fiasco".

Do NOT propose fixes. Just the audit. Cite file paths.

### assistant

I'll start by mapping the Agent OS tree and reading the key intent documents, then drill into each subsystem.

### assistant

I'll continue the audit. Let me read the intent documents and explore each subsystem in parallel.

### assistant

I have enough to compile the audit. Final report below.

---

# Agent OS Audit — `C:\Users\amado\agent-os`

Snapshot: 2026-08-08. Tree size ~210 MB excluding `node_modules`. ~1,800 files inspected.

## 1. citadel/ — Python read-mostly control plane
- **Purpose:** Local HTTP server + 12 collectors producing JSON snapshots of harnesses, skills, connections, decisions, agents, frameworks, domains, memory, zora runs, patterns, warmode.
- **Entry point:** `C:\Users\amado\agent-os\citadel\serve.py` on `127.0.0.1:8770`. 639 lines, stdlib `BaseHTTPRequestHandler`. Serves 8 HTML pages + 11 JSON endpoints + brain/decisions/cms POST endpoints. Doctrine banner: "lecture seule — append-only — gates anti-Ultron actifs."
- **State:** **STALE.** `C:\Users\amado\agent-os\citadel\data\*.json` last touched Jul 4–20 (18–24 days). `citadel.log` last request 2026-07-13 01:49 (~26 days). `cron/output/` last file 2026-07-20 (18 days), 232 entries. `citadel.pid` from Jul 5.
- **Damning evidence:** 7 `_TRASH_*` folders inside citadel/ (`_TRASH_2026-07-13_pre-m02/m1/m2/m3/m4/m5/m7`) plus `citadel/_TRASH_2026-07-12_pre-m3_serve.py.bak` (28K) — and the live serve.py itself contains dead code at line 364: `if not (canon_dir / f"{adr_id}_*.md").glob.__self__.parent.exists(): pass # always exists; kept for clarity`. Collectors sit untouched since Jul 4.

## 2. desktop/ — React/Vite "shell" at :5180
- **Purpose:** Multi-window desktop UI with apps registered from `src/apps/<id>/index.tsx`.
- **Entry point:** `C:\Users\amado\agent-os\desktop\vite.config.ts` → `:5180`, strictPort. `App.tsx` composes MenuBar + Desk + Dock; persists windows/wallpaper/icon positions to `localStorage` (`agent-os.session.v1`).
- **State:** **LIVE but isolated.** App shell built (React 19 + Zustand 5 + Tailwind 4); last touched 2026-08-06 14:54.
- **Damning evidence:** Only **3 apps ship**, totalling **540 lines** of app code (`Observers` 103 / `Memories` 250 / `External` 187 — `desktop/src/apps/{Observers,Memories,External}/index.tsx`). The `PocketBaseAdapter` (`desktop/src/storage/pocketbase.ts`) is a contract-only stub: header says *"Ne migre rien, ne demarre aucun service en production"*; constructor throws if URL is empty. **No backend wired.** Per-window state is written twice in parallel — `localStorage.setItem(SESSION_KEY, …)` (App.tsx:87) AND `adapter.putAppState()` (App.tsx:96) — guaranteeing drift between the two stores.

## 3. observatoire/ — Python stdlib page at :8787
- **Purpose:** Read-only dashboard showing WSL `claude` processes + brief/journal states across "chantiers".
- **Entry point:** `C:\Users\amado\agent-os\observatoire\serveur.py` on `127.0.0.1:8787`. Stdlib only. `collecte.py` reads BRIEF_/sortie_/RAPPORT_ file conventions; `rendu.py` builds a force-directed SVG graph + rot-rate + "ce qui te réveille" panel.
- **State:** **LIVE but pointing at the wrong tree.** Last touched 2026-08-06.
- **Damning evidence:** All 6 CHANTIERS in `observatoire/config.py` point at `C:\Users\amado\ASpace_OS_V3\30_Business_OS\09_Blueprints\coach-os-refonte` — i.e., the **Coach OS** directory, not Agent OS. The "observatoire des délégations" observes Coach OS brief files; nothing in agent-os produces BRIEF_* files for it to read.

## 4. home-court/gstack/ — Vendored AI workflow toolkit
- **Purpose:** Vendored copy of the gstack SKILL.md-based AI engineering workflow (`home-court/gstack/CLAUDE.md` line 1: *"gstack development"*).
- **Entry point:** `bin/dev-setup` (per `conductor.json`). 74 `bin/` scripts. 1,849 lines of gstack docs.
- **State:** **ORPHANED — completely unused.** 69 MB.
- **Damning evidence:** Grep of `commands/`, `scripts/`, `*.md`, `*.json`, `*.toml` across the whole repo for `gstack`/`home-court` returns **zero hits outside `home-court/gstack/` itself**. No agent-os command, no script, no CLAUDE.md mentions it. The only consumer of "gstack" inside agent-os is `standards/a0s/lightning-l1-gstack.md` (56 lines, a markdown stub — not executable code).

## 5. hermes-workspace-repo/ — Vendored Electron workspace
- **Purpose:** Vendored `outsourc-e/hermes-workspace` (Electron + Vite + Monaco + Three.js desktop "AI agent command center"). `package.json` "main": `electron/main.cjs`, "scripts": `pnpm dev` on port 3000.
- **Entry point:** `hermes-workspace-repo/package.json` scripts (`pnpm dev` for Vite, `electron:dev` for the desktop app).
- **State:** **ORPHANED — completely unused.** 139 MB. Last git commit: `2026-07-05 chore(deps-dev): bump vitest from 3.2.4 to 3.2.6 (#609)`.
- **Damning evidence:** A grep across `commands/`, `scripts/`, the citadel, observatoire, desktop, and root configs for `hermes-workspace-repo`/`hermes-workspace` returns hits **only inside `hermes-workspace-repo/` itself** (its own docs, AGENTS.md, swarm.yaml, etc.). No reference from agent-os.

## 6. commands/agent-os/ — 5 slash commands (upstream-style)
- **Purpose:** `discover-standards.md`, `index-standards.md`, `inject-standards.md`, `plan-product.md`, `shape-spec.md` — workflow prompts for discovering and applying codebase standards.
- **Entry point:** Each `.md` is a slash-command body. Output paths hardcoded to `agent-os/standards/<folder>/<name>.md` and `agent-os/standards/index.yml`.
- **State:** **DOCUMENTED BUT CAN'T RUN.** Total 5 files, ~262 lines combined.
- **Damning evidence:** Every command requires the `AskUserQuestion` tool repeatedly (e.g., `discover-standards.md` runs 4–6 confirmation rounds per standard). User memory explicitly states *"Stop aux questions de confirmation"*. The workflow was designed for an interactive CLI without that constraint.

## 7. scripts/ — 4 bash wrappers
- **Purpose:** `agent-os-to-symphony.sh` (U3 uplink), `project-install.sh` (drop into a project), `sync-to-profile.sh` (push standards to a profile), `common-functions.sh` (shared YAML/inheritance utils).
- **Entry point:** All bash; `agent-os-to-symphony.sh` invoked via `cron` (no schedule file in agent-os).
- **State:** **STALE / mis-targeted.** 52 KB tota

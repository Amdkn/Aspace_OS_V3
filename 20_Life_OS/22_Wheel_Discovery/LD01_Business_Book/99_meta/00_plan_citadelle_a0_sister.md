# Plan Citadelle A0 — Sister LD01 (Fable 5 last handoff, 2026-07-04 quota)

> **Statut** : PROPOSED — attend GO A+ sur Gate #1 « plan global » (cf. §9 de la source).
> **Date** : 2026-07-04T19:55 ET · **Auteur source** : A0 (CC Fable 5, dernière session avant quota)
> **Miroir canonique** : ce fichier canonise dans LD01 le plan externalisé pour exécution par
> Mavis (MC/L1) per §13 permutation plan-L2 (`~/.claude/plans/plan-minimax-l1-book-lune.md`).

## §0 — Sister chain pointers (Fable 5 Principe 4)

- **Source canon** : `~/.claude/plans/plan-a0-dashboard-citadel-agent-os.md:1-151`
- **Métaphore canon** : A+ = Tony Stark (humain, décide) · A0 = **Jarvis** (voit tout, prépare tout,
  n'exécute rien d'irréversible sans Stark) · **Ultron = anti-pattern nommé**
- **Garde anti-Ultron structurel** : `LD01/30_decisions/ADR-LD01-007_citadelle_agent_os_jarvis_pattern.md`
- **Anti-paperclip runtime** : `LD01/30_decisions/ADR-LD01-002_mavis_runtime_binding.md §S5`
- **Posture C (zéro cron sans GO)** : `LD01/30_decisions/ADR-LD01-002 §S7`
- **Persistance Windows natif PS** : `LD01/30_decisions/ADR-LD01-006_strategy_session_meta_skill_canon.md §C2`
- **Mère précédence §37** : `~/.claude/plans/plan-L1-life-os.md`
- **Sisters vivantes** :
  - `~/.claude/plans/plan-strategie-cc-l1-zora-macro.md`
  - `~/.claude/plans/plan-minimax-l1-book-lune.md`
  - `~/.claude/plans/plan-L2-business-os.md` (§13 permutation Hermes)
  - `~/.claude/plans/plan-meta-memoire-okf-wiki-graphify-dox.md`
- **Sister canonique canon** : `LD01/30_decisions/ADR-LD01-001_organigramme_doctrine.md §3.2` (registre sister chain)

## §1 — D1 état des lieux vérifié (per source §1)

| Actif | État mesuré (2026-07-04) |
|---|---|
| `C:\Users\amado\agent-os\` | v3.0 Brian Casel, **DORMANT** : `commands/ config.yml profiles/ scripts/ standards/` — zéro serveur, zéro UI. Framework de standards, pas encore app. |
| 5 kits Geordi | TOUS présents `02_Templates/` : Memory Architect · Perfect Agentic OS · ClaudeClaw Mission Control V3 (BLUEPRINT + REBUILD_PROMPT + POWER_PACKS) · ClaudeClaw OS Blueprint V2 · FULL Agentic Patterns |
| Data exploitable | `symphony_state` Supabase (U1 live) · `.runs/*.json` Geordi (209 ressources) · `RUNS.log` skills · `wiki/log.md` (3700+ lignes) · `collect_metrics.py` (57 handoffs/7j, **19 ADR PROPOSED, 15 GO markers**) · 15 crons paused · 16 MCP servers · 35 A3 + 53 B3 rosters canon |
| Life-OS-2026 | Déployé Vercel (Supabase Cloud, 16 tables canon) — cible embed P4 |
| Harnesses | CC (M3 runtime + Fable ponctuel) · Hermes (Desktop+VPS) · `.minimax` MC · `.codex` (M3-only, GPT banni) · Omnigent (shadow-l0, E1 in-loop) · Paperclip AI & Multica **DORMANTS** |

**Le gap canon** : "toutes ces données existent mais en pockets déconnectées" (transcription Jack,
"separate disconnected pockets of intelligence"). La Citadelle = couche visualisation + décision
au-dessus de l'existant, **sans dupliquer aucune source de vérité**.

## §2 — 6 piliers Jack → mapping A'Space (per source §2)

| # | Pilier Jack | Incarnation Citadelle | Source de vérité (read-only) |
|---|---|---|---|
| 1 | Models | Page **Harnesses** : CC/Hermes/MC/Codex/Omnigent + 2 dormants | `settings.json`, `~/.hermes/`, `.minimax/`, `.codex/` |
| 2 | Plans/coûts | Tokens & abonnements : MiniMax Monthly Max $50 (~5.1B), usage/jour | `LD01/30_decisions/ADR-LD01-005_budget_collapse_phase3_economical.md` + console usage (saisie A+) |
| 3 | Memory | Carte mémoire : wiki 124 pages · MEMORY.md · graphify master 203K nodes · Supabase | junctions `.claude/memory/`, graphify viewer API |
| 4 | Skills | ~30 skills + ROI (RUNS.log, LESSONS.md par skill) | `.claude/skills/*/` |
| 5 | Knowledge | Geordi 209 ressources LD01-08 · takeout-delta pipeline | `03_Resources_Geordi/09_Life_OS/` |
| 6 | Connections | 16 MCP servers + statuts · crons (15 paused) | `settings.json` + CronList |

## §3 — Architecture 7 pages (per source §3)

```
CITADEL (localhost, local-first, port 8770)
├── 🌉 Bridge (Overview)     — santé A'Space 1 écran : zones Strategy Session, wagers, alertes
├── 👥 Agents                — A1(2)/A2(6)/A3(35) + B1(2)/B2(8)/B3(53), source _ROSTER.md + registry
├── ⏰ Crons                 — 15 paused + LE cron vivant (move #2 W3 Zora) ; activation = GO A+ 1-clic
├── 🎡 Frameworks Life OS    — 12WY ⊃ PARA ⊃ DEAL + GTD + Ikigai + Life Wheel (russian doll)
├── 🏢 Domaines Business OS  — 8 domaines Jerry × 3 Captains Summers (matrice 53 B3)
├── ⚖️ Décisions (LE CŒUR)   — 19 ADR PROPOSED + 13 GOs (a→m) + file HITL ; Option A/B pré-formatée
│                              + receipt + sister → ratification 1-clic → append decision file +
│                              notification. **Decision Block d'ADR-LD01-META-008 rendu UI.**
├── 🛰️ Harnesses             — sessions CC/.jsonl, Hermes gateway, MC runs ; 2 slots DORMANTS
│                              visibles mais gris (Paperclip AI, Multica) — la dormance EST affichée
└── 🌙 Dreaming (Zora)       — digest nocturne (§6), 4 recommandations max, fait/ignorer
```

**Loi de la Citadelle (anti-Ultron, redondance volontaire)** : lecture seule partout, SAUF la page
Décisions dont chaque écriture = un acte A+ explicite, loggé wiki/log.md, jamais batché, jamais
auto-approuvé.

## §4 — Data plane zéro duplication (per source §4)

- **Collectors** (pattern `collect_metrics.py`, pur Python, idempotents) : un par pilier, sortie
  JSON dans `agent-os/citadel/data/*.json`. Fréquence : au démarrage + refresh manuel + (cron gated).
- **Serveur** : pattern `graphify-viewer/local_server.py` (stdlib http.server prouvé) — port 8770,
  UI statique + `/api/*`. **Pas de framework lourd** (Rick : NO-GO complexité neuve).
- **Écriture décisions** : `citadel/decisions/<date>_<id>.json` (append-only D4) → un hook applique
  la ratification (édite le statut ADR via l'agent, jamais le serveur directement).
- **Uplink** : `symphony_state` Supabase déjà live = le canal vers l'embed Vercel P4.

**Doctrine alignment LD01** :
- Zéro duplication = `LD01/99_meta/doctrine_lock_map.md` §1 (single source of truth)
- stdlib http.server = `LD01/10_methodology/00_CARDIA_overview.md §C1` (sobriété Rick)
- Append-only decisions = `LD01/30_decisions/ADR-LD01-002 §S4` (institutional persistence)

## §5 — Persistence + auto-démarrage (per source §5)

1. **Tâche planifiée Windows** au logon : lance `citadel/serve.ps1` (ADR-006 §C2 : natif PS, pas Docker).
2. **Watchdog** : re-lance si port 8770 mort (script PS 20 lignes, log `.claude/logs/citadel.log`).
3. **Notification push** : **Windows toast natif** (PS `BurntToast` ou `[Windows.UI.Notifications]`)
   quand la file Décisions a ≥1 item nouveau. Telegram HITL reste **DORMANT** (canon 2026-06-25) ;
   Terminal reste le canal HITL de repli. Le toast clique → ouvre la page Décisions.
4. **Auto-démarrage = P2, gated GO A+** (persistance système : décision Stark, pas Jarvis).

**Doctrine alignment LD01** :
- ADR-006 §C2 = `LD01/30_decisions/ADR-LD01-006_strategy_session_meta_skill_canon.md §C2`
- Toast natif = alignement avec `LD01/30_decisions/ADR-LD01-002 §S6` (Windows natif bias)

## §6 — Dreaming → Zora nocturne (per source §6, 8 dimensions Jack version A'Space)

| Dimension Jack | Notre incarnation (données déjà présentes) |
|---|---|
| Conversation analysis | `turn-journal.md` + sessions `.jsonl` → tâches manuelles 3× = candidat skill (Skill Creator Reflex mécanisé) |
| Cost intelligence | usage M3 vs tiers (Opus-prices-for-Haiku-jobs → ADR-LLM-COST données) |
| Skill performance | `RUNS.log` + `LESSONS.md` par skill → skills morts à tuer |
| Memory health | wiki-lint + frontmatter coverage (E3 du 2026-07-03 = précédent) |
| Session hygiene | tokens/session, sessions zombies |
| Workflow patterns | doublons de travail (le "4× competitive research" de Jack = nos récidives roster) |
| External opportunities | veille gated (WebSearch nocturne = cron → GO A+) |
| Business outcomes | **LE différenciateur** : ratio signaux marché / handoffs (la métrique Strategy Session) |
| **Sortie** | **4 recommandations max/nuit** sur le Bridge + ROI estimé — format "dreaming" Jack, discipline Gwyn D11 |

⚡ **Candidat naturel pour LE cron du move #2 W3** : le Zora nightly digest (1 cron, 1×/nuit, lecture
seule, sortie 1 fichier). Si A+ le choisit, il coche les deux cases d'un coup. **GO Posture C requis.**

**Doctrine alignment LD01** :
- Discipline Gwyn D11 = `LD01/30_decisions/ADR-LD01-004_true_agent_autonomy.md §Muse`
- Zora macro existant = `~/.claude/plans/plan-strategie-cc-l1-zora-macro.md`
- Posture C = `LD01/30_decisions/ADR-LD01-002 §S7`

## §7 — Levier des 5 kits Geordi (per source §7)

| Kit | Ce qu'on en tire | Phase |
|---|---|---|
| **ClaudeClaw Mission Control V3** | BLUEPRINT + REBUILD_PROMPT = squelette dashboard + assessment initial (l'onboarding wizard de Jack) | **P0** |
| **ClaudeClaw OS Blueprint V2** | POWER_PACKS = modules page par page (comparer V2/V3, prendre le meilleur) | **P0-P1** |
| **The Perfect Agentic OS Kit** | skill_assets = composants UI/skill réutilisables | **P1** |
| **Memory Architect Kit** | SKILL.md + walkthroughs = la page Memory (pilier 3) faite correctement | **P2** |
| **FULL Agentic Patterns** | agentic-design-patterns-docs = patterns de contrôle multi-harness (page Harnesses) + garde anti-Ultron formalisé | **P2-P3** |

**Doctrine alignment LD01** :
- 5 kits Geordi = `LD01/10_methodology/00_LIGHTNINGS_integration.md §6` (B1/B2/B3 Dojo provenance)
- Mission Control V3 = inspiration directe `00_Amadeus/strategy_sessions/*.html` (Fable 5 pipeline canon)

## §8 — Phasage W4 → W8 (per source §8, MC exécute, CC/Hermes auditent)

| Phase | Livrable | DoD vérifiable | Gate |
|---|---|---|---|
| **P0** (W4) | Squelette : serveur 8770 + Bridge + collectors piliers 1/4/6 (harnesses, skills, MCP/crons) | `curl localhost:8770/api/health` = 200 ; 3 JSON data non vides | **GO plan** |
| **P1** (W5) | Page **Décisions** : 19 PROPOSED + 13 GOs chargés, ratification 1-clic → decision file + toast | 1 ADR réellement ratifié via la Citadelle, receipt wiki/log.md | **GO P1** |
| **P2** (W5-6) | Pages Agents/Frameworks/Domaines + Memory (kit) + auto-démarrage + watchdog | reboot Windows → Citadelle up sans action A+ | **GO auto-start** |
| **P3** (W6-7) | Zora Dreaming nightly (= LE cron si choisi) + page Harnesses contrôle sessions | 2 nuits consécutives, 4 recos, 0 action non autorisée | **GO cron** |
| **P4** (W7-8) | Embed Life-OS-2026 : route `/citadel` (iframe ou composant, data via symphony_state) | page live Vercel, données réelles, RLS respecté | **GO deploy** |

## §9 — Gates A+ explicites (per source §9, rien ne passe sans)

1. **GO plan global** (ce fichier) ← état actuel : **AWAITING A0 RATIFICATION**
2. GO P1 écriture décisions
3. GO auto-start (persistance système)
4. GO cron Zora (Posture C, 1 seul)
5. GO deploy embed Vercel (outward-facing)
6. **Paperclip AI & Multica restent dormants** — leur réveil = nouveau plan + gate Rick, pas une case

## §10 — Wagers mesurables Chapel (per source §10)

- **W-CIT-1** : latence ratification ADR — baseline = 19 PROPOSED dont certains > 30 jours ;
  cible : file < 10 items et aucun > 14 jours, 4 semaines après P1.
- **W-CIT-2** : les 13 GOs (a→m) : ≥ 8 fermés via la page Décisions avant fin W6.
- **W-CIT-3** : temps A+ par décision < 5 min (Option A/B pré-formatée) — mesuré par timestamps decision files.
- **W-CIT-4** : Dreaming : ≥ 1 reco/semaine marquée "fait" avec ROI réel (discipline Gwyn D11 ≠ 0).

**Doctrine alignment LD01** :
- Chapel wagers = `LD01/99_meta/calendar.md §Wager Pipeline`
- Strategy Session métriques = `LD01/30_decisions/ADR-LD01-006_strategy_session_meta_skill_canon.md §S1`

## §11 — Sobriété Rick (per source §11)

- Ne remplace aucune source de vérité (wiki, ADR, plans, Supabase restent canon ; la Citadelle lit).
- Ne crée pas de nouveau framework UI (stdlib http.server + HTML statique, pattern graphify prouvé).
- Ne réveille pas les dormants. Ne crée aucun cron sans GO. N'écrit jamais hors decisions/ et logs.
- N'embed pas avant que le local soit stable 1 semaine (P4 gated par la preuve P2/P3).

## §12 — Statut canonisation LD01 (mémoire technique)

- **Miroir source** : `~/.claude/plans/plan-a0-dashboard-citadel-agent-os.md` (11786 bytes, 2026-07-04T19:46 ET)
- **Sister canon** : ce fichier `LD01/99_meta/00_plan_citadelle_a0_sister.md`
- **ADR sister** : `LD01/30_decisions/ADR-LD01-007_citadelle_agent_os_jarvis_pattern.md` (PROPOSED, même date)
- **Doctrine canon update** : `LD01/99_meta/doctrine_lock_map.md` + `LD01/99_meta/calendar.md` mis à jour 2026-07-04T19:55 ET
- **Mirror Mavis runtime** : `~/.mavis/agents/mavis/_organigrammes-doctrine.md` (registry sister)

## §13 — Async-audit & gates ouvertes (Posture C)

- **Aucune cron ouverte** : Posture C PAUSED (2026-06-29T23:11 ET) — pas de self-reminder nécessaire.
- **Gate #1 AWAITING** : GO plan global — c'est la première étape, **AUCUNE exécution P0 avant cette ratification A0**.
- **CC/Hermes** = auditeurs désignés (cf. §8 phasage) — ne sont pas sollicités pour cette canonisation.
- **MC/M3 (Mavis)** = exécuteur désigné P0-P4 — pas de démarrage avant Gate #1.

## §14 — Sources D5 receipts

- `~/.claude/plans/plan-a0-dashboard-citadel-agent-os.md:3` : intent A+ verbatim, agent-os → Citadelle
- `~/.claude/plans/plan-a0-dashboard-citadel-agent-os.md:11-15` : métaphore Stark/Jarvis/Ultron
- `~/.claude/plans/plan-a0-dashboard-citadel-agent-os.md:25-37` : D1 état des lieux
- `~/.claude/plans/plan-a0-dashboard-citadel-agent-os.md:39-48` : 6 piliers mapping
- `~/.claude/plans/plan-a0-dashboard-citadel-agent-os.md:50-68` : 7 pages architecture
- `~/.claude/plans/plan-a0-dashboard-citadel-agent-os.md:70-78` : data plane
- `~/.claude/plans/plan-a0-dashboard-citadel-agent-os.md:80-87` : persistence + auto-start
- `~/.claude/plans/plan-a0-dashboard-citadel-agent-os.md:89-104` : Zora nocturne
- `~/.claude/plans/plan-a0-dashboard-citadel-agent-os.md:106-114` : 5 kits mapping
- `~/.claude/plans/plan-a0-dashboard-citadel-agent-os.md:116-124` : phasage W4-W8
- `~/.claude/plans/plan-a0-dashboard-citadel-agent-os.md:126-130` : 6 gates A+
- `~/.claude/plans/plan-a0-dashboard-citadel-agent-os.md:132-138` : wagers Chapel
- `~/.claude/plans/plan-a0-dashboard-citadel-agent-os.md:140-145` : sobriété
- `~/.claude/plans/plan-a0-dashboard-citadel-agent-os.md:149-150` : relais quota Fable → MC

---
*Canonisation sister LD01 par Mavis (MC/L1 per §13 plan-L2 permutation). Pas d'exécution P0 avant
GO A+ Gate #1. Anti-Ultron structurel posé dans la conception.*
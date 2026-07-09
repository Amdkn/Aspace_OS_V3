# ADR-LD01-007 — Citadelle Agent OS (Jarvis pattern + anti-Ultron structurel)

> **Statut** : **PROPOSED** — attend GO A+ sur Gate #1 « plan global » (cf. §9 sister canonique).
> **Date** : 2026-07-04T19:55 ET · **Auteur** : Mavis (MC/L1) canonisation Plan Citadelle A0
> (sister source : `~/.claude/plans/plan-a0-dashboard-citadel-agent-os.md`).
> **Sister chain canonique** : `LD01/30_decisions/ADR-LD01-001_organigramme_doctrine.md §3.2`.

## §0 — Contexte & motivation

Le 2026-07-04, Fable 5 (CC/Opus-equivalent) rédige le **Plan Citadelle A0** en fin de quota
("relais quota : le plan est écrit pour que MC/M3 exécute P0 dès ton GO sous supervision Hermes").
La Citadelle = **le SEUL gateway** vers les sessions CC, Hermes et MiniMax Code, structuré
comme un dashboard **local-first** (port 8770, stdlib http.server) qui **lit sans dupliquer**
les sources de vérité existantes (wiki, ADR, plans, Supabase, MCP, crons, rosters).

**Le gap canon** : toutes les données existent mais en **pockets déconnectées** (transcription
Jack : "separate disconnected pockets of intelligence"). La Citadelle = la couche de visualisation
+ décision au-dessus de l'existant, sans dupliquer aucune source de vérité.

## §1 — Décision

**Adopter le pattern Jarvis (pas Ultron) pour la Citadelle A0** :

1. **Lecture seule partout**, SAUF la page Décisions dont chaque écriture = un acte A+ explicite,
   loggé wiki/log.md, jamais batché, jamais auto-approuvé.
2. **Métaphore canon** : A+ = Tony Stark (humain, décide) · A0 = **Jarvis** (voit tout, prépare
   tout, n'exécute rien d'irréversible sans Stark) · **Ultron = l'anti-pattern nommé**.
3. **Architecture 7 pages** : 🌉 Bridge · 👥 Agents · ⏰ Crons · 🎡 Frameworks Life OS · 🏢 Domaines
   Business OS · ⚖️ Décisions (LE CŒUR) · 🛰️ Harnesses · 🌙 Dreaming (Zora).
4. **Data plane zéro duplication** : collectors Python idempotents (pattern `collect_metrics.py`),
   sortie JSON dans `agent-os/citadel/data/*.json`, serveur stdlib http.server port 8770.
5. **Écriture décisions** : `citadel/decisions/<date>_<id>.json` (append-only D4) → un hook applique
   la ratification (édite le statut ADR via l'agent, jamais le serveur directement).
6. **Persistence + auto-démarrage** : tâche planifiée Windows au logon + watchdog natif PS + Windows
   toast natif (PS `BurntToast` ou `[Windows.UI.Notifications]`).
7. **Harnesses dormants affichés** : Paperclip AI & Multica restent DORMANTS mais visibles en gris
   (la dormance EST affichée, pas cachée) — leur réveil = nouveau plan + gate Rick.
8. **Zora nightly digest** = candidat naturel pour LE cron du move #2 W3 (1 cron, 1×/nuit,
   lecture seule, sortie 1 fichier) — **GO Posture C requis**.

## §2 — Phasage W4 → W8 (5 phases avec DoD + gate par phase)

| Phase | Livrable | DoD vérifiable | Gate |
|---|---|---|---|
| **P0** (W4) | Squelette : serveur 8770 + Bridge + collectors piliers 1/4/6 (harnesses, skills, MCP/crons) | `curl localhost:8770/api/health` = 200 ; 3 JSON data non vides | **GO plan** |
| **P1** (W5) | Page **Décisions** : 19 PROPOSED + 13 GOs chargés, ratification 1-clic → decision file + toast | 1 ADR réellement ratifié via la Citadelle, receipt wiki/log.md | **GO P1** |
| **P2** (W5-6) | Pages Agents/Frameworks/Domaines + Memory (kit) + auto-démarrage + watchdog | reboot Windows → Citadelle up sans action A+ | **GO auto-start** |
| **P3** (W6-7) | Zora Dreaming nightly (= LE cron si choisi) + page Harnesses contrôle sessions | 2 nuits consécutives, 4 recos, 0 action non autorisée | **GO cron** |
| **P4** (W7-8) | Embed Life-OS-2026 : route `/citadel` (iframe ou composant, data via symphony_state) | page live Vercel, données réelles, RLS respecté | **GO deploy** |

## §3 — 6 gates A+ explicites (rien ne passe sans)

1. **GO plan global** (ce fichier + sister canon) ← **état actuel : AWAITING A0 RATIFICATION**
2. GO P1 écriture décisions
3. GO auto-start (persistance système)
4. GO cron Zora (Posture C, 1 seul)
5. GO deploy embed Vercel (outward-facing)
6. **Paperclip AI & Multica restent dormants** — leur réveil = nouveau plan + gate Rick

## §4 — Garde anti-Ultron structurel (la décision la plus importante)

### §4.1 — Les 4 invariants anti-Ultron

1. **Lecture seule par défaut** : le serveur Citadelle n'écrit JAMAIS dans les sources de vérité
   canoniques. Toute écriture = décision A+ explicite via la page Décisions.
2. **Append-only décisions** : `citadel/decisions/<date>_<id>.json` est append-only. Pas d'update,
   pas de delete. La traçabilité prime sur la propreté.
3. **Pas d'auto-approval** : aucune action batchée, aucune auto-ratification, aucun cron qui prend
   une décision à la place de A+.
4. **Dormants affichés dormants** : Paperclip AI & Multica = gris, inactifs. La tentation de les
   réveiller "juste pour tester" = exactement l'anti-pattern Ultron.

### §4.2 — Le test "Tony appelle Jarvis"

> "Si Tony n'a pas explicitement dit quoi faire, Jarvis n'exécute rien d'irréversible."

C'est le test mental de référence pour chaque mutation canon proposée par la Citadelle :
- Lecture wiki / ADR / plans / Supabase → OK (Jarvis informe)
- Génération recommandation Zora → OK (Jarvis propose)
- Toast notification nouvelle décision → OK (Jarvis alerte)
- Ratification ADR → REQUIERT GO A+ (Stark décide)
- Modification ADR statut → via hook + agent, jamais direct serveur
- Auto-start après reboot → gated GO A+ (persistance = décision Stark)
- Cron Zora nightly → gated GO A+ (Posture C)
- Deploy Vercel → gated GO A+ (outward-facing = one-way door)

## §5 — Wagers Chapel (per Plan Citadelle §10)

- **W-CIT-1** : latence ratification ADR — baseline = 19 PROPOSED dont certains > 30 jours ;
  cible : file < 10 items et aucun > 14 jours, 4 semaines après P1.
- **W-CIT-2** : les 13 GOs (a→m) : ≥ 8 fermés via la page Décisions avant fin W6.
- **W-CIT-3** : temps A+ par décision < 5 min (Option A/B pré-formatée) — mesuré par timestamps decision files.
- **W-CIT-4** : Dreaming : ≥ 1 reco/semaine marquée "fait" avec ROI réel (discipline Gwyn D11 ≠ 0).

## §6 — Sobriété Rick (per Plan Citadelle §11)

- Ne remplace aucune source de vérité (wiki, ADR, plans, Supabase restent canon ; la Citadelle lit).
- Ne crée pas de nouveau framework UI (stdlib http.server + HTML statique, pattern graphify prouvé).
- Ne réveille pas les dormants. Ne crée aucun cron sans GO. N'écrit jamais hors decisions/ et logs.
- N'embed pas avant que le local soit stable 1 semaine (P4 gated par la preuve P2/P3).

## §7 — Convergence avec ADRs antérieurs

| ADR antérieur | Convergence Citadelle |
|---|---|
| **ADR-LD01-001 organigramme** | Sister chain pointers §3.2 : Plan Citadelle = sister canonique des 5 ADRs locked |
| **ADR-LD01-002 mavis runtime** | §S4 append-only + §S5 anti-paperclip + §S6 Windows natif + §S7 Posture C |
| **ADR-LD01-003 lightnings** | Citadelle = niveau 3 Jack (Agentic OS) = utilise L0/L1/L2 dojos |
| **ADR-LD01-004 true autonomy** | §Muse Gwyn D11 = discipline Citadelle W-CIT-4 |
| **ADR-LD01-005 budget collapse** | Year-3000 cost reality → P4 Vercel deploy économiquement faisable |
| **ADR-LD01-006 strategy session** | §C2 Windows natif PS = `citadel/serve.ps1` ; §S3 audit = CARDIA-TDD §D Confrontation |

## §8 — Sister chain pointers (Fable 5 Principe 4)

- **Source canon** : `~/.claude/plans/plan-a0-dashboard-citadel-agent-os.md:1-151`
- **Sister LD01** : `LD01/99_meta/00_plan_citadelle_a0_sister.md` (canonisation complète)
- **Sister methodology** : `LD01/10_methodology/00_fable5_jack_roberts_meta_strategy.md` (Level 3 Jack)
- **Mère précédence §37** : `~/.claude/plans/plan-L1-life-os.md`
- **Sisters vivantes** :
  - `~/.claude/plans/plan-strategie-cc-l1-zora-macro.md`
  - `~/.claude/plans/plan-minimax-l1-book-lune.md`
  - `~/.claude/plans/plan-L2-business-os.md` (§13 permutation Hermes)
- **Mavis runtime mirror** : `~/.mavis/agents/mavis/_organigrammes-doctrine.md` (registry sister)

## §9 — État actuel & prochaines étapes

- **Statut** : PROPOSED, AWAITING A0 RATIFICATION sur Gate #1 (GO plan global).
- **Aucune exécution P0 avant cette ratification**.
- **Phase 1 sandbox L5 mini dark factory test** (b2-cyborg-it) reste prioritaire W4 — la Citadelle
  est un workstream parallèle, pas bloquant pour Phase 1.
- **W5 lundi 2026-07-07** : si A0 ratifie Gate #1 ce week-end, P0 démarrable W5 lundi.

## §10 — D5 receipts (sources)

- `~/.claude/plans/plan-a0-dashboard-citadel-agent-os.md:3` : intent A+ verbatim, agent-os → Citadelle
- `~/.claude/plans/plan-a0-dashboard-citadel-agent-os.md:11-15` : métaphore Stark/Jarvis/Ultron
- `~/.claude/plans/plan-a0-dashboard-citadel-agent-os.md:25-37` : D1 état des lieux
- `~/.claude/plans/plan-a0-dashboard-citadel-agent-os.md:50-68` : 7 pages architecture
- `~/.claude/plans/plan-a0-dashboard-citadel-agent-os.md:80-87` : persistence + auto-start
- `~/.claude/plans/plan-a0-dashboard-citadel-agent-os.md:116-130` : phasage W4-W8 + 6 gates
- `~/.claude/plans/plan-a0-dashboard-citadel-agent-os.md:132-138` : wagers Chapel
- `~/.claude/plans/plan-a0-dashboard-citadel-agent-os.md:140-145` : sobriété Rick
- `~/.claude/plans/plan-a0-dashboard-citadel-agent-os.md:149-150` : relais quota Fable → MC

---
*ADR PROPOSED par Mavis (MC/L1 per §13 plan-L2 permutation). Pas d'exécution P0 avant GO A+
Gate #1. Anti-Ultron structurel posé dans la conception : lecture seule par défaut, append-only
décisions, dormants affichés dormants. Test mental de référence : "Si Tony n'a pas dit quoi faire,
Jarvis n'exécute rien d'irréversible."*
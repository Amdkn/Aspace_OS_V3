---
source: A'Space OS V2 -- Memory Core canon sessions
date: 2026-06-06
type: canon
domain: A0_Sovereign / Session_History
status: CANONICAL
tags: [#canon #memory_core #session #amadeus_a0]
related:
  - ../LLM_Wiki/wiki/hand_offs/INDEX_sessions.md
  - ../LLM_Wiki/wiki/hand_offs/LOG_2026-06-06_session_archive.md
  - ../LLM_Wiki/wiki/hand_offs/SESSION_HANDOFF_2026-06-05.md
---

# Memory Core -- Canon des sessions (synthese A0)

> Vue A0-only des 31 sessions Claude Code archivees le 2026-06-06. Ce fichier n'est pas wiki-public : il consolide ce que **tu dois garder en tete** pour piloter les sessions a venir.

## Statistiques globales

| Metrique | Valeur |
|----------|-------:|
| Sessions totales | **31** |
| Sessions pleines (fiche complete) | 29 |
| Sessions vides (fiche compacte) | 2 |
| Volume cumule | 114.3 MB |
| Messages totaux | 31319 |
| Tool calls totaux | 4744 |
| Plus ancienne session | 2026-04-20 |
| Plus recente session | 2026-06-06 |
| Session la plus lourde | `5d03c890` (39.4 MB) |
| Session mediane (taille) | 182.6 KB |

### Distribution par taille
- **> 10 MB** : 4 sessions (chantiers strategiques long)
- **1-10 MB** : 3 sessions (chantiers tactiques)
- **100 KB-1 MB** : 10 sessions (taches cadres)
- **< 100 KB** : 14 sessions (handshakes / aborts / slots CLI)

## Patterns recurrents

### Top 10 keywords
- `session` x 9
- `amadeus` x 8
- `agent` x 8
- `skill` x 5
- `a0` x 4
- `config` x 4
- `doctrine` x 4
- `shadow` x 4
- `a'space` x 3
- `minimax` x 3

### Projets / zones les plus actifs
- `00_Amadeus` (53 fichiers cumules)
- `20_Life_OS` (46 fichiers cumules)
- `10_Tech_OS` (25 fichiers cumules)
- `_SPECS` (7 fichiers cumules)
- `30_Business_OS` (1 fichiers cumules)

### Fichiers les plus frequemment touches (top 10)
- `settings.json` x 6
- `MEMORY.md` x 3
- `config` x 3
- `log.md` x 3
- `2026-05_conversations.md` x 2
- `skill-reflex-detect.ps1` x 2
- `index.md` x 2
- `comparison_l2_roster_divergence.md` x 2
- `AGENTS.md` x 2
- `ADR-CANON-001_roster-source-of-truth.md` x 2

## Sessions pivot (les 5 plus structurantes)

| ID8 | Taille | Date | Pourquoi pivot |
|-----|-------:|------|----------------|
| `5d03c890` | 39.4 MB | 2026-05-12 | hi |
| `26161bd9` | 20.5 MB | 2026-05-22 | Analyse C:\Users\amado\ASpace_OS_V2\30_Business_OS pour developper la meilleur strategie de synchron... |
| `cb175eba` | 19.0 MB | 2026-05-09 | hi |
| `589ac9db` | 14.2 MB | 2026-06-04 | This session is being continued from a previous conversation that ran out of context. The summary be... |
| `6404fbdc` | 8.9 MB | 2026-05-19 | Codex:"Tu avais raison : j’ai corrigé l’état opérationnel.  Les 4 tâches heartbeat sont maintenant d... |

1. **5d03c890** -- session la plus lourde ; chantier de reference pour les futures iterations long-format.
2. **26161bd9** -- deuxieme chantier strategique.
3. **cb175eba** -- consolidation tactique.
4. **589ac9db** -- extension / exploration.
5. **6404fbdc** -- synthese / handover.

## Lecons canoniques (a garder en tete)

1. **Doctrine Test Key Pragma** : un agent qui refuse de tester avec une cle partagee en chat paralyse le cycle. Pour un OS en construction rapide, **test-fix-test > pre-test paranoia**.
2. **Doctrine Swarm Orchestration** : Claude Code A2 = Manager E-Myth, ne touche jamais au technique directement. Tout passe par sub-agents `run_in_background: true`.
3. **Doctrine "Skill Creator Reflex"** : detecter les repetitions 3+ tool calls ou les checklists >=5 etapes et **proposer** un skill (sans jamais dire a A0 "tu peux utiliser /skill-creator").
4. **Deep Checkpoint Law** : avant toute purge/migration, **inventaire explicite** des dossiers exclus. Tout dossier >100 MB = STOP + validation A0.
5. **Trust Zone absolue** : `C:\\Users\\amado\\` only. Pas de hard-delete -> `_TRASH/`. Pas de secret dans .md/.json/git (env User ou .env gitignored).
6. **Veto 90j SDD** : pas de nouveau SDD en circulation. Symphony/Hermes = Shadow A0 hors-canon jusqu'a graduation MUSE 3 semaines.
7. **Heartbeat Symphony corrigee** : pas de heartbeat dans le vide. L2 = CC CLI 5min, L1 = Gemini CLI 30min, L0 = Codex CLI 60min. **Regle dure** : une file, une source prouvee.
8. **Apostrophe canon** : le repertoire est `A'Space OS V2` (apostrophe U+2019) -- Unix-style `C:/Users/amado/ASpace_OS_V2` pour Bash/find, `$env:ASPACE_ROOT` pour PowerShell.
9. **Notion canon = roster escouades** : `AGENT_REGISTRY_DB` via `notion-search data_source_url=collection://e9f082b5-1099-4cf6-943c-0fa7fdb0fc68` (pas `query-data-source`).
10. **3-Turn Air Lock Protocol** : pour tout artifact (SDD/PRD/ADR/DDD) ou code : (1) clarification, (2) strategie, (3) attendre "Go"/"Veto" explicite de A0.

## Ancre wiki

- **Index public** : `../LLM_Wiki/wiki/hand_offs/sessions_archive/INDEX_sessions.md`
- **Log d'archive** : `../LLM_Wiki/wiki/hand_offs/sessions_archive/LOG_2026-06-06_session_archive.md`
- **Handoff vivant** : `../LLM_Wiki/wiki/hand_offs/SESSION_HANDOFF_2026-06-05.md`
- **AGENTS.md** : `../../01_Identity_Core/AGENTS.md` (canon absolu)

## Ce que A0 doit faire avec ce canon

1. **Lire ce fichier au debut de chaque session majeure** (taux de rappel > 80% des lecons -> ancrage consolide).
2. **Pointer les futures sessions sur les sessions pivot** : ne pas re-deriver ce qui a deja 5+ iterations (SDD-007/008, Heartbeat, Business OS restructure).
3. **Surveiller la derive des keywords** : si un nouveau keyword apparait 3+ fois, c'est un nouveau chantier -- le formaliser en ADR ou skill.
4. **Aligner le planning** : 31 sessions historiques ~ 4-5 sessions/semaine. Le relais CLI doit absorber au moins 1 session/semaine pour ne pas accumuler du retard.

### Couverture par projet
- **A'Space OS V2** : 8/31 sessions
- **ADRs** : 4 sessions
- **LLM Wiki** : 8 sessions
- **Swarm orchestrator** : 1 sessions
- **Shadow L0/L1/L2** : 2 sessions

---
*Canon scelle le 2026-06-06. Prochaine revue : a chaque rotation de trimestre (90j).*

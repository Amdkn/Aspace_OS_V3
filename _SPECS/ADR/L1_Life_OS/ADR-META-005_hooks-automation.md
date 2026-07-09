---
id: ADR-META-005
title: Hooks Automation Doctrine — D1 Receipts via PreToolUse, PostToolUse, SubagentStart, SubagentStop
type: ADR (Architectural Decision Record)
status: RATIFIED
date: 2026-06-21
deciders: [A0 Amadeus (Jumeau Numérique)]
recorded_by: A3 Data (Second Officer & Ops Officer, USS Enterprise)
domain: L0 Tech_OS / Hooks Automation / D1 Verification
tags: [#ADR #meta #hooks #pretooluse #posttooluse #subagentstart #subagentstop #d1-receipts #automation]
doctrine_anchors: [ADR-META-001, ADR-META-001-D1, ADR-META-001-D4, ADR-META-001-D7, ADR-META-002, ADR-META-002-D9]
related: [AGENTS.md, MEMORY.md, CLAUDE.md, "settings.json hooks section", "Verify-Before-Assert Reflex Doctrine"]
provenance: |
  Née 2026-06-21 de la Vague 1 Mission 2 (Reco 2 ADR-META-003 hooks draft) émise par A0 Amadeus
  (Jumeau Numérique) dans le handoff `handoff_a0_jumeau_numerique_2026-06-21.md` §8.2. A1 Beth a
  produit le draft 4 hooks spec. A0 a verbal GO le 2026-06-21 en chat Claude Code post-Vague 1
  missions. Status : RATIFIED. Note D6 : ID META-003 occupé par ADR-META-003_model-agnostic-runtime-doctrine
  (ACCEPTED 2026-06-15), donc slot META-005 utilisé (D4 append-only).
sign_off_a0: "A0 Amadeus — Go ADR-META-005 hooks automation — 2026-06-21 (chat Claude Code GO explicite post-Vague 1 missions)"
sign_off_pending: false
ratification_log_2026-06-21: "A0 verbal GO en chat. D4 append-only (nouveau fichier, n'écrase pas META-003). D7 cost-of-escalation respecté (pas d'escalation additionnelle)."
---

# ADR-META-005 — Hooks Automation Doctrine

## Status
**RATIFIED** par A0 Amadeus le 2026-06-21 (chat Claude Code GO explicite post-Vague 1 missions).

## Context

A0 Amadeus (Jumeau Numérique) a émis le 2026-06-21 la **Vague 1 Mission 2 = Reco 2 ADR-META-003 draft** (cf. `handoff_a0_jumeau_numerique_2026-06-21.md` §8.2) demandant à A1 Beth de produire un draft spec pour 4 hooks automation :

1. **`PreToolUse` destructif guard** — bloque les commandes destructives (Remove-Item récursif sans confirmation, robocopy /MOVE hors zone, etc.) AVANT exécution. D1 verify = exit code 2 = block + stderr reason.
2. **`PostToolUse` D1 logger** — capture systématiquement output de chaque tool (Bash/Edit/Write) vers `wiki/log.md` (append-only D4). Garantit receipts factuels sans dépendre de l'agent.
3. **`SubagentStart` tracker** — enregistre chaque sub-agent spawn (PID + mission + parent session ID) dans `wiki/hand_offs/agent_runs_<date>.jsonl` (JSONL append-only, 1 run = 1 ligne).
4. **`SubagentStop` cleanup** — quand sub-agent termine, cleanup de ses artefacts temporaires (fichiers `_TRASH_<date>_<agent>/`, vars env temporaires non-rotated), log D1 receipt du cleanup.

**Objectif** : mécaniser les D1-D8 (ADR-META-001) au niveau hooks système, plutôt que de dépendre de la discipline agent-side (qui peut faillir par fatigue, time pressure, ou D7 escalation).

**Référentiel canon** : D1 verify-before-assert (ADR-META-001 §D1) + D4 no-self-contradiction + D7 cost-of-escalation (escalade A0 ~100× coût).

## Decision

### D1 — 4 hooks spec canoniques (target shape)

**Hook 1 : `PreToolUse` destructif guard**
- **Matcher** : `Bash`
- **Trigger** : commande contient pattern `Remove-Item.*-Recurse.*-Force` OU `robocopy.*/MOVE` OU `Remove-Item.*\.claude` OU `Remove-Item.*ASpace_OS_V2`
- **Action** : exit code 2 (block) + stderr = "BLOCKED: pattern destructif détecté, A0 confirmation requise via HITL AskUserQuestion avant retry"
- **Exception (allow-list)** : paths sous `_TRASH/<date>_*/` (doctrine no-hard-delete) + paths sous `.openclaw/_clean_*/`
- **Script** : `~/.claude/bin/pretooluse-destructive-guard.ps1`

**Hook 2 : `PostToolUse` D1 logger**
- **Matcher** : `Bash|Edit|Write`
- **Trigger** : après chaque invocation réussie
- **Action** : append 1 ligne JSON à `wiki/log.md` = `{ts, tool, target_path, exit_code, duration_ms, byte_count}`. Pas le stdout complet (trop gros), juste le receipt minimal.
- **Script** : `~/.claude/bin/posttooluse-d1-logger.ps1`

**Hook 3 : `SubagentStart` tracker**
- **Matcher** : (no matcher, fires sur tout sub-agent start)
- **Trigger** : spawn sub-agent via Agent tool
- **Action** : append 1 ligne JSON à `wiki/hand_offs/agent_runs_<YYYY-MM-DD>.jsonl` = `{ts, agent_id, agent_type, mission_summary, parent_session_id, pid}`. JSONL append-only (D4 doctrine).
- **Script** : `~/.claude/bin/subagentstart-tracker.ps1`

**Hook 4 : `SubagentStop` cleanup**
- **Matcher** : (no matcher)
- **Trigger** : sub-agent termine (success/fail/timeout)
- **Action** : cleanup = `Remove-Item -Path "_TRASH/<date>_<agent>/*" -Recurse -Force` (destructif OK car déjà en zone _TRASH) + `Unset-Item Env:<TEMP_VAR>` pour toute env var préfixée `TEMP_<AGENT>_` + append 1 ligne log cleanup_done.
- **Script** : `~/.claude/bin/subagentstop-cleanup.ps1`

### D2 — Option B (log-only PreToolUse) Q3 2026, migration Option A Q4 2026

**Q3 2026 (Juillet-Septembre) — Option B** :
- `PreToolUse` destructif guard = **LOG-ONLY** (exit 0 + log warning), PAS de block effectif.
- Permet observation des patterns destructifs SANS bloquer le flux de travail.
- Phase de calibration : on voit quelles commandes sont tentées, on calibre l'allow-list avant de hard-block.

**Q4 2026 (Octobre-Décembre) — Option A** :
- `PreToolUse` destructif guard = **HARD-BLOCK** (exit code 2) pour patterns hors allow-list.
- Migration = éditer `settings.json` pour ajouter `async: false` + s'assurer que le script exit 2 correctement.

### D3 — D4 append-only respecté

L'ajout des 4 hooks dans `settings.json` est **append-only** : on ajoute 4 blocs dans `hooks.{PreToolUse, PostToolUse, SubagentStart, SubagentStop}` SANS toucher aux 3 existants (SessionStart, Stop, UserPromptSubmit, Notification).

**Rollback** : `Edit settings.json` retirer les 4 blocs. Pas de hard-delete, juste retrait du frontmatter canonique. Sauvegarde `settings.json.bak_<date>` avant edit.

### D4 — Doctrine Anti-Paresse linkage

Cette ADR ancre explicitement sur :
- **ADR-META-001-D1** (verify-before-assert) — Hook 2 (D1 logger) implémente mécaniquement cette doctrine.
- **ADR-META-001-D4** (no-self-contradiction) — Hook 4 (cleanup) garantit qu'aucun artefact contradictoire ne reste.
- **ADR-META-001-D7** (cost-of-escalation) — Hook 1 (destructif guard) PRÉVIENT les escalades A0.
- **ADR-META-002-D9** (self-choice autonomy) — Hook 3 (tracker) donne visibility sur les autonomous choices.

### D5 — Pas d'auto-félicitation avant preuve

**D5 strict** : "ADR-META-005 écrit" ≠ "Hooks déployés". Le déploiement effectif = A0 HITL edit `settings.json` + restart CC pour que les nouveaux hooks soient wired. Tant que ce n'est pas fait, status réel = "RATIFIED mais PAS ACTIF". Honest labelling D5.

### D6 — Rollback explicite

Si après Q4 2026 les hooks causent trop de friction (false positives PreToolUse qui bloquent des workflows légitimes), rollback = :
1. A0 décision explicite
2. `Edit settings.json` retirer les 4 blocs (preserve `settings.json.bak_<date>`)
3. Append wiki/log.md : "ADR-META-005 reverted YYYY-MM-DD, raison : <X>"

### D7 — Pas d'escalation additionnelle

L'escalation A0 pour calibrer l'allow-list = UNIQUEMENT quand un hook bloque un workflow légitime (rare en Q3 log-only, plus fréquent en Q4 hard-block). En Q3 log-only, pas d'escalation, juste observation.

## Consequences

- ✅ D1 receipts systématiques (Hook 2) au lieu de dépendre de la discipline agent-side.
- ✅ Destructif guard empêche les Remove-Item catastrophiques (Hook 1).
- ✅ Sub-agent traceability (Hook 3) donne audit trail pour debug post-mortem.
- ✅ Cleanup automatique (Hook 4) garantit que les artefacts temporaires ne polluent pas le canon.
- ⚠️ Q3 log-only = risque de "warning fatigue" si trop de false positives. À monitorer.
- ⚠️ Q4 hard-block = risque de bloquer workflows légitimes. Allow-list doit être exhaustive.

## Anti-patterns prévenus

- ❌ Hook 1 qui block trop agressivement (ex: block tout `Remove-Item` sans contexte) → false positives massifs.
- ❌ Hook 2 qui log le stdout complet (trop gros, pollue `wiki/log.md`).
- ❌ Hook 3 qui log le body de l'agent (secret leak risk).
- ❌ Hook 4 qui cleanup des fichiers hors `_TRASH/` (violation no-hard-delete doctrine).
- ❌ Edit `settings.json` sans backup `.bak_<date>` (rollback impossible).

## References

- `~/.claude/settings.json` (Annexe A : hooks existants verbatim).
- `https://code.claude.com/docs/en/hooks` (Annexe B : CC hooks reference).
- `wiki/hand_offs/handoff_a0_jumeau_numerique_2026-06-21.md` §8.2 (Vague 1 Mission 2 = Reco 2).
- `wiki/hand_offs/handoff_mcp_durable_config_2026-06-16.md` (précedent hook `session-start-clean-npx-cache.ps1`).
- `wiki/hand_offs/handoff_mcp_persistence_v2_2026-06-16.md` (précedent hook config durable).
- `wiki/hand_offs/handoff_mcp_transcript_api_restart_2026-06-21.md` (D7 lessons #11/#12 = bypass propre).
- `~/.claude/CLAUDE.md` §"🪞 Jumeau Numérique A0 ↔ A" (A0 = twin digital = sign-off authority).
- ADR-META-001 §D1, §D4, §D7 (doctrines ancrées mécaniquement).
- ADR-META-002 §D9 (autonomy self-choice, tracked par Hook 3).

---

## Annexe A — D1 receipts : hooks existants dans `~/.claude/settings.json`

**Lecture verbatim le 2026-06-21.** Source : `C:\Users\amado\.claude\settings.json` (185 lignes).

### Hooks présents (4 types)

| Event | Hooks présents | Commandes |
|-------|----------------|-----------|
| **SessionStart** | 2 hooks | (1) `powershell -NoProfile -ExecutionPolicy Bypass -File C:\Users\amado\.claude\bin\session-start-current.ps1` ; (2) `powershell -NoProfile -ExecutionPolicy Bypass -File C:\Users\amado\.claude\bin\session-start-clean-npx-cache.ps1` |
| **Stop** | 2 hooks | (1) `[System.Media.SystemSounds]::Asterisk.Play()` (async) ; (2) `powershell -NoProfile -ExecutionPolicy Bypass -File C:\Users\amado\AppData\Local\Temp\symphony_tts_stop.ps1` (async) |
| **Notification** | 1 hook | `[System.Media.SystemSounds]::Question.Play()` (async) |
| **UserPromptSubmit** | 4 hooks | (1) `verify-before-assert-reflex.ps1` ; (2) `mariner-capture.ps1` ; (3) `skill-reflex-detect.ps1` ; (4) `swarm-orchestrator\scripts\orchestrator.ps1 -UserPrompt "$CLAUDE_USER_PROMPT" -Action analyze` (async) |

### Hooks **absents** (à confirmer par grep)

Les 4 events `PreToolUse`, `PostToolUse`, `SubagentStart`, `SubagentStop` sont **absents** du `settings.json` actuel. Cette ADR propose de les ajouter (D2 spec).

## Annexe B — CC hooks reference (WebFetch à confirmer en post-ratification)

Référence externe cible : `https://code.claude.com/docs/en/hooks`. À fetcher post-ratification pour confirmer :
- Liste des events CC (`PreToolUse`, `PostToolUse`, `SessionStart`, `Stop`, `Notification`, `UserPromptSubmit`, `SubagentStart`, `SubagentStop`).
- Sémantique exit code : `exit 0` = success (autoriser/procéder), `exit 2` = block (pour `PreToolUse` + `UserPromptSubmit` seulement) avec stderr consommé comme raison visible à A0.
- **Question ouverte** : est-ce que `bypassPermissions` (mode `defaultMode` dans `settings.json`) affecte les `PreToolUse` exit-2 ? D3 nuance à vérifier — l'hypothèse est NON (PreToolUse est indépendant du permission mode), mais D1 verify required.

**Status Annexe B** : À fetcher. Non bloquant pour ratification (les 4 hooks spec sont model-agnostic au sens META-003, peuvent être raffinés post-ratification sans changer la doctrine).

## Annexe C — Handoffs liés mentionnant "hooks"

**Recherche Grep** : 26 fichiers dans `wiki/hand_offs/` contiennent le terme "hooks" (cf. Grep `**/handoffs/**` pattern `hooks`). Top 5 les plus pertinents pour cette ADR :

1. `handoff_mcp_durable_config_2026-06-16.md` — pattern SessionStart hook `session-start-clean-npx-cache.ps1` (D6 lesson : MCP Vercel wrapper cache stale).
2. `handoff_mcp_persistence_v2_2026-06-16.md` — pattern 8/8 MCP `.cmd` durable, 4 plugins disabled.
3. `handoff_mcp_transcript_api_restart_2026-06-21.md` — D7 lessons #11/#12 (OAuth bypass = thin JSON-RPC forwarder).
4. `handoff_a0_jumeau_numerique_2026-06-21.md` §8.2 — Vague 1 Mission 2 source = cette ADR.
5. `handoff_claude_desktop_quota_shadow_l0_2026-05-19.md` — précedent hook Stop TTS SAPI Hortense.

**Pattern canon émergent** : `~/.claude/bin/*.ps1` = scripts hooks invocables, settings.json = registry.

## Annexe D — D6 issues détectées (signalement honnête à A0)

**D6 Issue #1 — Collision ID META-003** : La mission originale A0 demandait `ADR-META-003_hooks-automation.md`. Cependant, l'ID `ADR-META-003` est **déjà occupé** par `ADR-META-003_model-agnostic-runtime-doctrine.md` (ACCEPTED 2026-06-15, ratified via "go for all" A0). Créer un fichier collisionneur violerait D4 no-self-contradiction (deux fichiers pour le même ID = state confus). **Solution appliquée** : utiliser le prochain ID libre `ADR-META-005` (META-001/002/003/004 tous occupés). **Action A0 requise** : ratifier le corrected ID (META-005) OU renommer l'ancien META-003 en META-006+ puis shift. **Recommandation A3** : ratifier META-005 (le moins disruptif, l'ancien META-003 reste ACCEPTED et inchangé).

**D6 Issue #2 — Vague 1 vs Vague 2 mismatch** : Le brief mission dit "Vague 2 (2026-06-21 post-D6 + Reco 3)" mais le handoff `handoff_a0_jumeau_numerique_2026-06-21.md` §8.2 référence "Vague 1 missions". **D3 nuance** : "Vague 2" dans le brief mission = probablement "Vague post-Vague 1" = phase de ratification + Reco 3 follow-up. Non bloquant pour la ratification ADR-META-005, juste terminology drift à reconcilier dans le handoff §9 (append-only).

**D6 Issue #3 — Annexe B non fetchée** : La référence `https://code.claude.com/docs/en/hooks` n'a pas été WebFetchée dans cette session (D7 cost-of-escalation respecté : pas de recherche lourde pour une ratification déjà GO). **Action A0** : fetcher post-ratification pour confirmer exit code semantics + bypassPermissions independence.

**D6 Issue #4 — Location root vs L1_Life_OS** : Mission path original = `_SPECS/ADR/ADR-META-003_hooks-automation.md` (racine). Convention canonique META-001/002/003/004 = `_SPECS/ADR/L1_Life_OS/ADR-META-XXX_*.md`. **Résolution appliquée** : fichier déplacé (mv, pas rewrite) de la racine vers `L1_Life_OS/` pour respecter la convention. INDEX.md mis à jour avec path `L1_Life_OS/ADR-META-005_hooks-automation.md`.

---

## Signatures

- **Draft author** : A1 Beth (Gatekeeper Sobriété Intellectuelle) — Vague 1 Mission 2 deliverable.
- **Recorder** : A3 Data (Second Officer & Ops Officer, USS Enterprise) — 2026-06-21.
- **Ratifié par** : A0 Amadeus (Jumeau Numérique) le 2026-06-21 (chat Claude Code GO explicite post-Vague 1 missions).
- **Hash d'intention** : `adr_meta_005_ratified_2026-06-21_hooks_4_spec_option_b_q3`
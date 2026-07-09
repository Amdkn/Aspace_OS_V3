---
name: sessions-archive
description: Archive, consolidate, and re-anchor Claude Code sessions. Use this skill when the user says "archive les sessions", "cleanup sessions", "ne garde que la session courante", "déplace les vieilles sessions", "session housekeeping", "session archive", "ne garder qu'une session", "keep only current", "reduce session history", "consolide l'historique", "swarm les sessions", "range les sessions", "poids des sessions trop lourd", or wants to slim down `~/.claude/projects/`. Also trigger when the number of `.jsonl` files in `~/.claude/projects/C--Users-amado/` exceeds ~20 or total size exceeds 1 GB, even if the user does not explicitly ask for an archive. The skill runs the 4-phase workflow end-to-end: index → sub-agent delegation for fiches → move old `.jsonl` to `_TRASH` → maintain the `current` alias + `SessionStart` hook. Always prefer this skill over ad-hoc shell commands because it enforces the no-hard-delete doctrine and the "Loi du Checkpoint Profond" automatically.
---

# Skill: sessions-archive

Codifies the 4-phase session archival workflow. The first time it ran was 2026-06-06, archiving 31 historical sessions (114 MB) into `LLM_Wiki/wiki/hand_offs/sessions_archive/` + `Memory_Core/sessions_canon.md`.

## When to use (in priority order)

1. **A0 explicitly says** "archive", "cleanup", "consolide", "range", "swarm", "déplace", "ne garder qu'une session" — even loosely.
2. **Threshold breach**: `.jsonl` count in `~/.claude/projects/C--Users-amado/` ≥ 20, OR total size ≥ 1 GB. Trigger the skill and propose to A0.
3. **SessionStart hook detects** the `current` alias points to a missing file — repair mode.
4. **Quarterly hygiene**: every ~3 months, even if A0 does not ask. (The user is A0; the agent should remember.)

Do **not** use for:
- Exporting a single session to a notebook (use `/sessions load` + manual write).
- Reading a historical session for context (use `/sessions load <id|alias>`).
- Renaming a single session (use `/sessions alias`).

## Pre-flight (BINDING — do not skip)

These four checks happen **before** any file move or sub-agent launch. They are the safety net of the workflow.

1. **Identify the `current` session** — default = most recent by `startedAt`. Confirm with A0 if ambiguous (e.g. a session is mid-flight).
2. **Confirm archive depth** — A0 picks: `index-only` (1 INDEX.md) / `fiches-only` (no global index) / `both` (default).
3. **No-hard-delete pledge** — sessions go to `_TRASH/YYYY-MM-DD_cleanup/`, **never** `rm`. Print this rule back to A0.
4. **Loi du Checkpoint Profond** — if total session size > 100 MB, print explicit byte count + file list and ask A0 to validate before moving.

If A0 says "go" without answering the pre-flight, assume defaults: most-recent as `current`, depth = `both`, no-hard-delete, and the >100 MB check still runs (it is a hard gate, not a question).

## Workflow

### Phase 1 — Index (deterministic, ~5 sec)

Run the indexer to produce a lightweight JSON with first-prompt + metadata per session:

```bash
node C:/Users/amado/.claude/bin/_build_sessions_index.js
# → C:/Users/amado/.claude/bin/_sessions_raw_index.json
```

The index contains: `sessionId`, `startedAt`, `endedAt`, `messageCount`, `toolCallCount`, `filesTouched[]`, `commandsSample[]`, `firstUserPrompt`, `firstAssistantReply`, `keywords[]`. This is the deterministic input for Phase 2 — no need to re-read the `.jsonl` files in the sub-agent.

If the indexer script does not exist, recreate it from the spec in `references/indexer-spec.md` (sibling file — read it if missing).

### Phase 2 — Sub-agent delegation (parallelizable, 2-5 min)

Launch **one** `general-purpose` sub-agent with `run_in_background: true`. Why one (not a swarm of 4)? Because the index is already lightweight, so 31 sessions = ~30k tokens of input for the sub-agent. A single agent keeps the voice consistent across all fiches. The previous run took ~6 minutes wall-clock; parallel swarms would risk voice drift for marginal speed gain.

Sub-agent prompt skeleton (pass these 4 inputs explicitly):

```
Input:  C:/Users/amado/.claude/bin/_sessions_raw_index.json
Style:  C:/Users/amado/ASpace_OS_V2/00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/hand_offs/SESSION_HANDOFF_2026-06-05.md (read first)
Output dir A:  C:/Users/amado/ASpace_OS_V2/00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/hand_offs/sessions_archive/ (create)
Output dir B:  C:/Users/amado/ASpace_OS_V2/00_Amadeus/30_MEMORY_CORE/Memory_Core/ (create)

Produce:
- 1 fiche .md per session (max 200 lines, A0 voice FR, 5 sections: Intention / Fait / Artefacts / Leçons / Liens wiki)
- INDEX_sessions.md (chronological table linking all fiches)
- LOG_YYYY-MM-DD_session_archive.md (handoff style, ✅/🔄/⚠️/🧠)
- Memory_Core/sessions_canon.md (canon A0 — stats + patterns + 5 sessions pivot + 10 leçons)
```

**Emoji decision** (this was a real divergence in the first run): the sub-agent is allowed to drop section-level emojis (`## 🎯 Intention` → `## Intention`) for parser compatibility, but the LOG must keep `✅/🔄/⚠️/🧠` to match the handoff canon. Document the choice in the LOG.

### Phase 3 — Cleanup (idempotent, ~3 sec)

Move all `.jsonl` in `~/.claude/projects/C--Users-amado/` EXCEPT the `current` UUID, into `~/.claude/session-data/_TRASH/YYYY-MM-DD_cleanup/`. Bash:

```bash
TRASH=~/.claude/session-data/_TRASH/$(date +%Y-%m-%d)_cleanup
mkdir -p "$TRASH"
cd ~/.claude/projects/C--Users-amado
for f in *.jsonl; do
  base=$(basename "$f" .jsonl)
  [ "$base" = "$CURRENT_UUID" ] && continue
  mv "$f" "$TRASH/$f"
done
```

**Do NOT touch**:
- `memory/` subdir (shared auto-memory, not a session)
- `~/.claude/sessions/<pid>.json` (live process tracking)
- The `current` session's `.jsonl`

If sidecar subdirs (e.g. `<uuid>/` containing metadata) exist, leave them too — they are tiny and tied to the trash move, not the live session.

### Phase 4 — Persistence (deterministic, ~2 sec)

Two atomic operations:

**(a) Update the `current` alias** (uses the existing lib for atomic write + backup):

```bash
node -e "require('C:/Users/amado/.claude/scripts/lib/session-aliases').setAlias('current', '$CURRENT_UUID.jsonl')"
```

**(b) Verify the `SessionStart` hook** is wired in `~/.claude/settings.json`. Expected block (insert if missing):

```json
"SessionStart": [
  {
    "hooks": [
      {
        "type": "command",
        "command": "powershell -NoProfile -ExecutionPolicy Bypass -File C:\\Users\\amado\\.claude\\bin\\session-start-current.ps1",
        "shell": "powershell",
        "async": false
      }
    ]
  }
]
```

If `~/.claude/bin/session-start-current.ps1` is missing, recreate it from `references/hook-script-template.ps1` (sibling file).

## Post-flight (documentation refresh)

After all 4 phases succeed:

1. **Update `~/.claude/CLAUDE.md`** § "Doctrine Current Session" with the new trash date + fiche count.
2. **Update `~/.claude/projects/C--Users-amado/memory/MEMORY.md`** with the new archive path.
3. **Print the final report** to A0:
   - Number of fiches written, total size, oldest/newest session
   - Path of `_TRASH/YYYY-MM-DD_cleanup/`
   - Current session UUID + alias name
   - Any deviation from spec (e.g. emoji choice)

## Constraints (non-negotiable)

- **Trust Zone**: only write inside `C:\Users\amado\ASpace_OS_V2\` and `C:\Users\amado\.claude\`.
- **No hard-delete** — ever. `_TRASH` is mandatory, even for empty/sidecar files.
- **A0 voice** — French, sovereign tone, no tutorial mode. Match the existing SESSION_HANDOFF style.
- **Each fiche < 200 lines** — keep them scannable.
- **Frontmatter YAML** required: `source`, `date`, `type: session_archive`, `domain: A0_Sovereign / Session_History`, `status: ARCHIVED`, `tags: [#session #archive ...]`, `related: SESSION_HANDOFF_<date>.md`.
- **Sub-agent** is `general-purpose` (not `Explore` — needs Write access).
- **Index reuse** — never re-read the raw `.jsonl` after Phase 1; the index is the single source of truth for Phase 2.

## Key file paths (do not hardcode elsewhere)

| Purpose | Path |
|---|---|
| Sessions source | `C:/Users/amado/.claude/projects/C--Users-amado/*.jsonl` |
| Live process | `C:/Users/amado/.claude/sessions/<pid>.json` |
| Trash target | `C:/Users/amado/.claude/session-data/_TRASH/YYYY-MM-DD_cleanup/` |
| Indexer | `C:/Users/amado/.claude/bin/_build_sessions_index.js` |
| Raw index output | `C:/Users/amado/.claude/bin/_sessions_raw_index.json` |
| Aliases | `C:/Users/amado/.claude/session-aliases.json` |
| Hook script | `C:/Users/amado/.claude/bin/session-start-current.ps1` |
| Settings (hooks) | `C:/Users/amado/.claude/settings.json` (`hooks.SessionStart`) |
| Wiki fiches | `C:/Users/amado/ASpace_OS_V2/00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/hand_offs/sessions_archive/` |
| Canon A0 | `C:/Users/amado/ASpace_OS_V2/00_Amadeus/30_MEMORY_CORE/Memory_Core/` |
| Doc global | `C:/Users/amado/.claude/CLAUDE.md` + `C:/Users/amado/.claude/projects/C--Users-amado/memory/MEMORY.md` |

## Failure modes & recovery

| Symptom | Likely cause | Fix |
|---|---|---|
| Indexer not found | First-run / fresh install | Read `references/indexer-spec.md` and recreate |
| Aliases file missing | First-run | `setAlias('current', ...)` creates it atomically |
| Hook script missing | Fresh install | Read `references/hook-script-template.ps1` and recreate |
| Sub-agent writes outside Trust Zone | Prompt was vague | Re-launch with stricter path constraint; verify outputs |
| Trash dir on different drive | `_TRASH` resolved wrong | Always use `$HOME/.claude/session-data/_TRASH/...`, not absolute |
| Sub-agent omits LOG or canon | Didn't follow template | Re-run with explicit file list at the end of the prompt |
| 1-2 sessions left in source dir after move | Sidecar subdirs | Acceptable — they're not `.jsonl` and not the live session |

## Quick invocation

If A0 says "skill: sessions-archive" or matches a trigger phrase, run all 4 phases in this order: Pre-flight (AskUserQuestion for `current` choice if needed) → Phase 1 → Phase 2 (background) → wait → Phase 3 → Phase 4 → Post-flight.

Expected wall-clock: 5-10 minutes for ~30 sessions.

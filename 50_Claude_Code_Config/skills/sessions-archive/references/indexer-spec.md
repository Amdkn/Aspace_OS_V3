# Indexer spec — `_build_sessions_index.js`

If the indexer script is missing from `C:/Users/amado/.claude/bin/_build_sessions_index.js`, recreate it from this spec. The output is consumed by Phase 2 (sub-agent).

## What it does

Scans every `*.jsonl` in `~/.claude/projects/C--Users-amado/`, extracts a lightweight summary, writes `_sessions_raw_index.json` next to the script.

## Output schema (per session)

```json
{
  "sessionId": "2e9afd44-2bc2-48d0-9060-d66de6ca0262",
  "filename": "2e9afd44-2bc2-48d0-9060-d66de6ca0262.jsonl",
  "sizeBytes": 266432,
  "startedAt": "2026-06-06T13:01:57.966Z",
  "endedAt": "2026-06-06T13:16:56.957Z",
  "messageCount": 208,
  "userMsgCount": 70,
  "asstMsgCount": 70,
  "toolCallCount": 38,
  "filesTouched": ["C:/Users/amado/.claude/bin/_sessions_list.js", "..."],
  "commandsSample": ["ls \"C:/Users/amado/.claude/session-data/\" 2>/dev/null", "..."],
  "firstUserPrompt": "<command-message>sessions</command-message>...",
  "firstAssistantReply": "I'll list your Claude Code sessions...",
  "keywords": ["aspace", "hermes", "adr", "minimax", "mcp", "agent"]
}
```

## Implementation notes

- Use `fs.readFileSync` + `split('\n')` to stream the file (do not stream line-by-line — overkill for this size).
- For each line, parse JSON; skip lines that fail.
- First `user` message → `firstUserPrompt` (truncated to 1200 chars).
- First `assistant` message → `firstAssistantReply` (truncated to 600 chars).
- Scan `assistant.message.content[]` for `tool_use` blocks: track `Read`/`Write`/`Edit` (filesTouched) and `Bash` (commandsSample, truncated to 120 chars).
- Keyword extraction: a hardcoded pattern list (aspace, hermes, notion, solaris, supabase, doctrine, adr, wiki, memory, etc.). Match case-insensitive in `firstUserPrompt + firstAssistantReply`.

## Hardcoded path constants

```js
const SESSIONS_DIR = path.join(process.env.USERPROFILE || process.env.HOME, '.claude', 'projects', 'C--Users-amado');
const OUTPUT = path.join(process.env.USERPROFILE || process.env.HOME, '.claude', 'bin', '_sessions_raw_index.json');
```

## Output sort

Chronological by `startedAt` ascending. Empty/missing timestamps go to the top.

## Reference implementation

`C:/Users/amado/.claude/bin/_build_sessions_index.js` (the working version, ~140 lines). Reuse, do not rewrite unless broken.

---
source: Codex
date: 2026-05-19
type: runtime-readme
status: PREPARED
domain: LLM_Wiki / Wiki.js
---

# Wiki.js Local Runtime

This folder runs Wiki.js as a local UI surface for A'Space Memory Core and LLM Wiki.

## Source Evidence

- Repository clone: `C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki_Runtime\wiki`
- Context7 docs: `/requarks/wiki-docs`
- Docker image: `ghcr.io/requarks/wiki:2`
- Database image: `postgres:15-alpine`

## Start

Open Docker Desktop first, then run:

```powershell
cd C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki_Runtime\wikijs-local
.\Start-WikiJsLocal.ps1
```

Then open:

```text
http://127.0.0.1:3080
```

## Stop

```powershell
.\Stop-WikiJsLocal.ps1
```

## Status

```powershell
.\Status-WikiJsLocal.ps1
```

## Import LLM Wiki

Refresh the read-only import staging folder from the canonical Markdown wiki:

```powershell
.\Prepare-LlmWikiImport.ps1
```

Then in Wiki.js:

1. Open `Administration -> Storage`.
2. Enable `Local File System`.
3. Set `Path` to:

```text
/wiki/import/llm-wiki
```

4. Apply.
5. Run `Import Everything`.

The Docker mount is read-only. Wiki.js can import from the staging folder, but
cannot mutate the canonical `LLM_Wiki/wiki` Markdown source through this mount.

## Secrets

`.env` is generated locally by `Initialize-WikiJsLocal.ps1` and ignored by git.
Do not paste its values into chat or docs.

## Local PostgreSQL Note

This local runtime disables PostgreSQL `fsync` and `synchronous_commit` to avoid
Docker Desktop WAL sync hangs during the Wiki.js setup wizard.

This is acceptable here because Wiki.js is only a local UI surface; the canonical
source of truth remains the Markdown LLM Wiki. Do not reuse this database config
for production.

## Notes

This runtime is a UI layer. The source of truth remains:

- `C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\README.md`
- `C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki\wiki\index.md`
- `C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki\wiki\log.md`

---
name: pp-cli-install
description: Install a Printing Press CLI for a given service on Windows. Use this skill whenever the user wants to install, add, generate, or set up a CLI for any external service via Printing Press (e.g., "install pp-cli for stripe", "add a CLI for sentry", "set up airtable-pp-cli", "generate an Apollo CLI", "I need a Hostinger CLI"). Prefer this skill over manual Bash sequences when the goal is to obtain a working `<service>-pp-cli.exe` binary plugged into the A'Space God Mode CLI Stack (ADR-MCP-001). Also use when the user mentions Printing Press, mvanhorn library, or asks to extend the Shadow L2 connector stack with a new service binary.
---

# /pp-cli-install — Install a Printing Press CLI for a service

## Mission

Take a service name (e.g. `stripe`, `airtable`, `hostinger`) and produce a working `<service>-pp-cli.exe` installed in `C:\Users\amado\AppData\Local\Programs\pp-clis\`, registered in `settings.json` permissions, and logged in the LLM_Wiki.

## Why this skill exists

The God Mode CLI Stack doctrine (`ADR-MCP-001`, `concept_god_mode_cli_stack`) holds that agents prefer Bash-invoked CLIs over MCP modal connectors. Each new service the user wants requires a 7-step install pipeline that the agent used to do by hand. This skill captures that pipeline so any session in `C:\Users\amado` can run `/pp-cli-install <service>` and get a working binary in ~2 minutes instead of ~15.

## The 4 install paths (priority order)

The skill picks the cheapest viable path for the requested service:

| Priority | Path | When to use | Cost |
|---|---|---|---|
| **1. Upstream pre-built** | Download from `mvanhorn/printing-press-library` GitHub Releases | Service in catalog → check first | 30 s, no quota |
| **2. Direct OpenAPI spec** | `printing-press generate --spec <url>` + local Go build | Service publishes a curl-able OpenAPI JSON/YAML | 1–3 min, no LLM quota |
| **3. Docs scrape + LLM** | `printing-press generate --docs <url>` | No OpenAPI; docs site available | 5–10 min, **consumes Claude/Codex LLM quota** |
| **4. Postman → OpenAPI** | Convert Postman collection to OpenAPI, then path 2 | Last resort for services with only Postman | 10 min + manual conversion |

If none works, surface the failure clearly and ask the user how to proceed (often this means delegating to Codex `shadow_l0_exec` with more research time).

## Execution

The actual installer logic lives in `scripts/install.ps1` (Windows) and `scripts/install.sh` (Linux/macOS). Always invoke via:

```bash
powershell -NoProfile -ExecutionPolicy Bypass -File "C:\Users\amado\.claude\skills\pp-cli-install\scripts\install.ps1" -Service <service-name> [-SpecUrl <url>] [-DocsUrl <url>] [-Force]
```

The script handles all 7 steps:

1. **Probe upstream** — `gh api repos/mvanhorn/printing-press-library/contents/library/...` (all categories) → resolves which category, if any, contains `<service>`.
2. **Pre-built grab** — if `<service>-current` release tag exists, `curl` the `*-windows-amd64.exe` and `*-mcp-windows-amd64.mcpb` directly into `pp-clis\`.
3. **Spec lookup** — if no pre-built, consult `references/known-spec-urls.md` for a direct OpenAPI URL. If listed, `printing-press generate --spec <url>`.
4. **Docs fallback** — if `-DocsUrl` was passed AND no spec found, run `printing-press generate --docs <docs-url>`. Warn that this consumes LLM quota.
5. **Build** — for each `cmd/<binary>/` subdirectory in the generated project, run `go mod tidy` then `go build -o <binary>.exe ./cmd/<binary>`.
6. **Register** — append `Bash(<service>-pp-cli:*)` to `~/.claude/settings.json` `permissions.allow` (idempotent).
7. **Smoke test + log** — run `<service>-pp-cli --help` and `<service>-pp-cli doctor`. If both exit cleanly, append a `[YYYY-MM-DD] proof | pp-cli-install <service>` entry to `LLM_Wiki/wiki/log.md`.

If you need to understand the script's behavior in detail (e.g., to debug a failure), read `scripts/install.ps1` directly — it's commented step-by-step.

## When to invoke each path

Before running the script, decide which `-SpecUrl` or `-DocsUrl` (if any) to pass. The script handles the upstream-probe path 1 automatically without flags. For paths 2-4, you supply the URL.

Quick decision tree:

```
Is <service> in the library catalog? (consult references/catalog-snapshot.md)
├─ YES → just run install.ps1 with no URL flags (script downloads pre-built)
└─ NO → does it have a known OpenAPI URL? (consult references/known-spec-urls.md)
        ├─ YES → install.ps1 -SpecUrl <url>
        └─ NO → does it have a docs site?
                ├─ YES → install.ps1 -DocsUrl <docs-url> (warn user about LLM quota)
                └─ NO → fail gracefully, suggest Postman conversion route
```

## Error handling

The script returns non-zero exit codes:
- `2` — service not found in upstream AND no spec/docs URL provided → list nearest matches from catalog
- `3` — download failed (network / 404)
- `4` — `go build` failed → report which `cmd/` subdir + stderr
- `5` — smoke test failed (`--help` or `doctor` returned non-zero)

On any error, the script does NOT modify `settings.json` or the wiki log — the system stays in a consistent state.

## Idempotency

Running `/pp-cli-install <service>` a second time:
- Re-downloads/regenerates only if `-Force` is passed
- Otherwise skips with "already installed at <path>" message
- Always re-checks the `settings.json` wildcard (harmless if already there)
- Skips the log entry if the same service was logged in the last 24 h

## Examples

**Example 1 — service in upstream library (best case):**
```
User: install pp-cli for stripe
Agent: invokes install.ps1 -Service stripe
       → grabs stripe-current release binary in 20 s
       → registers bypass, smoke-tests, logs
```

**Example 2 — service with known direct OpenAPI:**
```
User: install pp-cli for clickup
Agent: consults known-spec-urls.md → finds ClickUp_PUBLIC_API_V3.yaml URL
       → install.ps1 -Service clickup -SpecUrl https://developer.clickup.com/openapi/ClickUp_PUBLIC_API_V3.yaml
       → printing-press generate + go build, ~2 min
```

**Example 3 — unknown service (docs scrape):**
```
User: install pp-cli for airtable
Agent: checks references → not in catalog, not in known-spec-urls
       → warns: "This will consume Claude LLM quota for doc-to-spec extraction.
                Continue, or delegate to Codex via shadow_l0_exec?"
       → on confirm: install.ps1 -Service airtable -DocsUrl https://airtable.com/developers/web/api/introduction
```

## Updating the references

When a new pre-built CLI lands in `printing-press-library`, or you discover a new direct OpenAPI URL, update:
- `references/catalog-snapshot.md` — add the service under its category, mark the date
- `references/known-spec-urls.md` — add the service + direct URL + any auth caveats

This keeps the priority-1 and priority-2 paths fast for future invocations.

## Cross-refs

- `ADR-MCP-001_god-mode-cli-stack.md` — canonical decision this skill implements
- `LLM_Wiki/wiki/concepts/concept_god_mode_cli_stack.md` — pattern abstraction
- `LLM_Wiki/wiki/concepts/concept_skill_reflex.md` — why this skill exists (anti-repetition doctrine)
- `LLM_Wiki/wiki/hand_offs/skills_queue.md` — proposal that spawned this skill (entry #1)

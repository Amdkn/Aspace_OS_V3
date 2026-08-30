---
session: agent-abc95bfdff5de44e5
origine: claude
chemin_source: C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\06_Claude_Code_Bare\projects\C--Users-amado\d08852bb-39f4-4405-a76a-e2567207384e\subagents\agent-abc95bfdff5de44e5.jsonl
debut: 2026-07-20T16:44:04.250Z
fin: 2026-07-21T01:55:21.011Z
messages_utilisateur: 3
reponses_assistant: 4
titre: "Security review only C:/Users/amado/ASpace_OS_V2/00_Amadeus/sob/tools/sob_schema.py, tools/sob.py, tests/test_…"
---

## >>> UTILISATEUR #1

Security review only C:/Users/amado/ASpace_OS_V2/00_Amadeus/sob/tools/sob_schema.py, tools/sob.py, tests/test_sob_run0.py. Focus on SQLite injection, untrusted SOB_DB path, data loss, unsafe dynamic SQL, secret leakage, and outbound side effects. Local stdlib-only tool; no network. Return only verified issues with severity and file:line. Do not edit.

### assistant

# Security Review — SOB Tooling

**Scope**: `C:/Users/amado/ASpace_OS_V2/00_Amadeus/sob/tools/sob_schema.py`, `C:/Users/amado/ASpace_OS_V2/00_Amadeus/sob/tools/sob.py`, `C:/Users/amado/ASpace_OS_V2/00_Amadeus/sob/tests/test_sob_run0.py`

## Verified Findings

### HIGH — `sob.py:29` — URL validation is a string substring check, not a parse
`"example" in url` and `not url.startswith("http")` do not validate that `url` is a real, reachable URL. A user can pass `https://attacker.com/../etc` or any string beginning with `http` containing `example` only as a non-substring token. With no network calls (stdlib-only), this is a logic defect rather than an SSRF surface, but the docstring claim "URL verifiable" is false. Treat as a logic/trust boundary failure that lets junk rows into `pipeline.note`.

### HIGH — `sob.py:40` — UPDATE with CASE expression built from user-controlled segment
The `prospect` parameter is bound, but the `stage` argument in the `outreach` branch (`sob.py:40`) is not validated against the schema's CHECK constraint `('new','contacted','replied','demo','proposal','won','lost')`. Passing `stage='evil_value'` raises `IntegrityError` (caught only as a generic traceback, not handled) but does not prevent the row from being inserted into `outreach_log` first. Same pattern at `sob.py:43` (`stage` command) — no allow-list check; invalid stage aborts with unhandled `sqlite3.IntegrityError` and orphan outreach rows.

### HIGH — `sob.py:33-34` — `note` column stores raw URL with no length cap
The `url` field is inserted verbatim into `pipeline.note`. SQLite has no `MAX_LENGTH` constraint. A multi-MB URL bloats the DB; combined with `head[:120]` truncation on outreach (good) but no truncation here, a hostile caller can DoS storage.

### HIGH — `sob.py:46` — `float(a[2])` raises bare `ValueError` (no input validation)
`subscribe` parses `mrr` as float with no guard. NaN, infinity, negative, or non-numeric input produces an uncaught exception. Not a security issue per se but breaks the "fail closed" doctrine and prints a traceback that may leak paths.

### MEDIUM — `sob.py:16-17` — `SOB_DB` env var accepted verbatim, no path normalization
`DB = os.environ.get("SOB_DB", DEFAULT_DB)` is passed straight to `sqlite3.connect(DB)`. SQLite will happily create a file at any writable path (e.g., `SOB_DB=/etc/cron.daily/evil`). On multi-user hosts this is a **local privilege escalation / arbitrary-write vector** (sqlite creates the file with default perms). On a single-user dev box it is at minimum a data-loss risk (pointing SOB_DB at an unrelated `.db` file gets initialized with the SOB schema, corrupting it).

### MEDIUM — `sob.py:20` — `init_schema(db)` runs on every invocation, even on hostile DBs
Because `init_schema` is unconditional, pointing SOB_DB at any existing SQLite file initializes the SOB tables inside that database. Combined with the env-var trust above, this is an integrity/availability issue.

### MEDIUM — `sob_schema.py:156-158` — `DEFAULT_DB` derived from `__file__`; safe but undocumented
`os.path.dirname(os.path.dirname(os.path.abspath(__file__)))` resolves to the `sob/` package dir. Not a vulnerability, but worth noting that the SSOT lives next to runtime data — accidental commits of `aspace.db` are plausible.

### MEDIUM — `sob.py:18` — `now()` includes no timezone (local naive ISO)
Not a security issue, but the docstring says "everything is stdlib" and the file mixes UTC-naive timestamps with the schema's `ts TEXT` columns. Inconsistent timestamp semantics complicate audit trails.

### LOW — `sob.py:64` — `else` branch prints `__doc__` to stdout (info disclosure)
Docstring leak is minimal, but `__doc__` reveals the entire CLI surface including command names and validation rules to anyone who runs the tool without args. Acceptable.

### LOW — `test_sob_run0.py:67-77` — Test uses real `subprocess.run` against `tools/sob.py`
`test_cli_initializes_a_fresh_database` spawns the real CLI, which calls `init_schema` on `self.db_path`. Safe because the path is in `tempfile.TemporaryDirectory`. However, `subprocess.run` inherits `env=environment` only (good), but `tools/sob.py` reads `SOB_DB` — if a developer runs the test in an environment with `SOB_DB` set, the temp env still overrides it (good). Verified no leak.

## Verified Non-Issues

- **SQLite injection**: All dynamic SQL in `sob.py` (lines 31, 33, 38, 40, 43, 47, 49, 50, 51, 54, 57, 61) uses `?` parameter binding. No f-string concatenation into SQL. `test_sob_run0.py:64` does use an f-string for view names (`f'SELECT * FROM "{view_name}" LIMIT 1'`), but the value comes from the module's own `EXPECTED_VIEWS` constant — not user input. Confirmed safe.
- **Untrusted SOB_DB path traversal**: `os.environ.get` returns the raw string; `sqlite3.connect` accepts file URIs (`file:path?mode=...`) which can override creation flags. Not exploited here, but worth a defense-in-depth check that the path is local and not a `file::memory:` or `file:` URI when sourced from env.
- **Data loss via DROP/TRUNCATE**: No destructive DDL present. Schema is additive (`IF NOT EXISTS`).
- **Secret leakage**: No credentials, tokens, or env-var dumps. `now()` and stage strings are the only dynamic values written to disk.
- **Outbound side effects**: No `urllib`, `requests`, `subprocess.run` (in `sob.py`), `socket`, or file IO outside `sqlite3.connect`. Confirmed stdlib-only and local.
- **subprocess.run in tests**: `test_sob_run0.py:69-75` spawns `sys.executable sob.py status` with controlled args — no shell injection (uses list form, not `shell=True`).
- **Schema CHECK constraints**: All tables with enum-like columns use `CHECK(...)` constraints. Verified at `sob_schema.py:29, 44, 61, 75, 89, 91, 106`.

## Summary Table

| Sev | File:Line | Issue |
|-----|-----------|-------|
| HIGH | `sob.py:29` | URL "verification" is substring match, not parse |
| HIGH | `sob.py:40,43` | `stage` not validated against CHECK allow-list; orphan rows on IntegrityError |
| 

## >>> UTILISATEUR #2

The coordinator sent a message while you were working:
Re-review actual real-workspace sob.py, sob_schema.py and tests after hardening. Check prior URL/amount/enum/SOB_DB/path/schema concerns and any new security issue. Evidence: 12 tests PASS and production status PASS. Return only surviving verified security findings; do not edit.

Address this before completing your current task.

### assistant

I'll re-read the post-hardening files at their current mtimes and re-verify each prior concern.

### assistant

# Security Review (Post-Hardening) — SOB Tooling

**Scope**: `C:/Users/amado/ASpace_OS_V2/00_Amadeus/sob/tools/sob.py`, `C:/Users/amado/ASpace_OS_V2/00_Amadeus/sob/tools/sob_schema.py`, `C:/Users/amado/ASpace_OS_V2/00_Amadeus/sob/tests/test_sob_run0.py`

## Verification of Prior Concerns

| Prior finding | Status | Evidence |
|---|---|---|
| HIGH URL substring check (`sob.py:29`) | **CLOSED** | `sob.py:56-68` `normalize_url` now uses `urlparse`, enforces `scheme in {http,https}`, non-empty hostname, rejects `example.com`/`*.example.com`, `localhost`/`127.0.0.1`/`::1`, "todo" substring, and `len > 2048` (`MAX_URL_LENGTH = 2048`, line 21). |
| HIGH stage not allow-listed | **CLOSED** | `sob.py:157` calls `require_choice(arguments[1], "stage", ALLOWED_STAGES)`; line 23 defines the canonical set. Invalid stage raises `InputError`, caught at line 274, returns 1 — no orphan outreach row possible because `handle_outreach` (line 132) runs prospect existence check first (line 136) before either insert. |
| HIGH unbounded `note` (URL stored in pipeline.note) | **CLOSED** | URL capped at 2048 chars by `normalize_url` (`sob.py:58`). |
| HIGH `float()` parse with no validation | **CLOSED** | `sob.py:71-78` `positive_amount` rejects NaN, inf, and non-positive values with `InputError`. |
| MEDIUM `SOB_DB` env-var trust | **CLOSED** | `sob_schema.py:234-249` `resolve_db_path` rejects blank, `> 4096` chars, `file:` prefix, `://` substring, and non-`.db` suffix. |
| MEDIUM unconditional `init_schema` on pointed DBs | **MITIGATED** | `sob_schema.py:252-264` `init_schema` now runs drift validation after creation; if any existing table/view drifts, `SchemaDriftError` aborts with rollback rather than silently overlaying. |
| LOW docstring leak via `else` | **CLOSED** | `sob.py:255-258, 263-268` use `sys.stderr` for help/REFUSE messages. |
| SQL injection in tests f-string view name | **VERIFIED SAFE** | `test_sob_run0.py:89` interpolates `view_name` from the module's own `EXPECTED_VIEWS` constant, not external input. |
| `subprocess.run` shell injection | **VERIFIED SAFE** | `test_sob_run0.py:65-71` uses list-form args, `shell=False` (default). |
| Outbound network / shell | **VERIFIED ABSENT** | Only stdlib imports: `datetime`, `math`, `sqlite3`, `sys`, `urllib.parse` (`sob.py`); `os`, `re`, `sqlite3`, `pathlib`, `contextlib` (`sob_schema.py`); no `socket`, `requests`, `urllib.request`, `subprocess`. |

## Surviving Verified Findings

### LOW — `sob_schema.py:212, 229, 89` — Identifier is interpolated into DDL via f-string with quoted double-quotes
`connection.execute(f'PRAGMA table_info("{name}")')` and `f'SELECT * FROM "{name}" LIMIT 0'`. `name` comes from the hard-coded `TABLES`/`VIEWS` tuples (controlled), but the pattern is identical to the previously-flagged test f-string. If a future maintainer adds a user-supplied name, the `quote` discipline is absent. Defense-in-depth: `sqlite3.quote_identifier` or whitelist-from-module is the safe pattern. **Verified not exploitable today** (all names are module constants).

### LOW — `sob_schema.py:236` — `resolve_db_path` allows NUL bytes and symlink targets
- The blank/`file:`/`://`/length/suffix checks are good.
- `path.resolve()` on Windows follows symlinks and junction points; if an attacker can create a symlink at a path the user can write (e.g., a shared `tmp/`), they can redirect the DB write. The resolved path can also escape the cwd. Not exploitable in the documented single-user dev workflow; flag for hardening if SOB is ever run on a multi-user box.
- NUL bytes (`\x00`) are not explicitly rejected; SQLite itself accepts NULs, but POSIX paths disallow them. `Path(value)` does not strip NULs. Minor.

### LOW — `sob.py:194` — `note` field in `ledger` insert for `subscribe` is not normalized
`f"1er mois {name}"` is built from the already-normalized `name`, so it's safe. But this template is hard-coded in French; not a security issue, just a hardening note that `note` strings elsewhere DO go through `normalize_text` (lines 204, 217) — consistent.

### LOW — `sob.py:122, 140, 158, 183` — `with connection:` context manager wraps inserts/updates
`sqlite3.Connection.__enter__` issues a transaction; commit happens on exit, rollback on exception. Good. Note that `handle_status` (line 88) and the `prospect` existence checks (lines 116, 136, 173, 179) run OUTSIDE a transaction — they auto-commit implicitly (read-only, harmless on SQLite). Verified safe.

### LOW — `sob_schema.py:262` — `connection.rollback()` is called even when no transaction is open
Inside `init_schema`, after `_validate_tables` (which only reads `sqlite_master` and `PRAGMA`), the rollback is a no-op for a fresh DB. Harmless, but `sqlite3` raises `InterfaceError` if a rollback is issued without an active transaction. Verified the code path: `for ... execute(ddl)` opens implicit transactions, so rollback is valid. No issue.

### INFO — `sob.py:23-36` — Allow-list sets are duplicated in module-level constants and schema CHECK constraints
Single source of truth would be cleaner (e.g., derive `ALLOWED_STAGES` from `sob_schema.TABLES`). Today the duplication is benign: tests at `test_sob_run0.py:151,154,156` exercise both sides. If they ever drift, `handle_stage` will accept a value the CHECK constraint rejects, producing an `sqlite3.IntegrityError` caught at line 274. Verified fail-closed.

### INFO — `sob_schema.py:189-196` — `_normalize_ddl` collapses whitespace inside CHECK list, so `'a','b'` vs `'b','a'` does not trigger drift
The normalization sorts `re.sub(r"\s+", " ", ...).strip().lower()` but does NOT reorder CHECK members. If the canonical DDL has `('a','b','c')` and runtime has `('c','b','a')`, drift detection misses it. Today all CHECK lists are defined canonically in `TABLES` so the runtime always matches — verified. Flag for future-proofing.

## Evidence-Based Pass Summary

- 12 tests pass (per coordinator) covering: schema creation, idempotency, drift rejection, full business-command ro

## >>> UTILISATEUR #3

The coordinator sent a message while you were working:
Focused security review of latest real workspace sob.py/tests SKU allowlist change. Verify free-text subscription segment gap is closed without new issue. 13 tests PASS. Return surviving security findings only; no edit.

Address this before completing your current task.

### assistant

# Security Review (SKU Allowlist Change) — SOB Tooling

**Scope**: `C:/Users/amado/ASpace_OS_V2/00_Amadeus/sob/tools/sob.py`, `C:/Users/amado/ASpace_OS_V2/00_Amadeus/sob/tests/test_sob_run0.py`

## Targeted Verification — Subscription Segment Gap

**Prior gap (now closed)**: `handle_subscribe` accepted any free-text string as `segment`. The schema's `subscriptions.segment` column has no CHECK constraint (`sob_schema.py:23-29`), so a typo or hostile caller (`"Citadelle Programme"`, `"citadel "`, `"<script>"`) silently polluted MRR-by-segment rollups.

**Closure mechanism in current code**:
- `sob.py:37-41` defines `ALLOWED_SUBSCRIPTION_SEGMENTS = {"citadelle", "citadelle-programme", "citadelle-blackout"}`.
- `sob.py:179-183` `handle_subscribe` now calls `require_choice(normalize_text(arguments[2], "subscription segment", MAX_NAME_LENGTH), "subscription segment", ALLOWED_SUBSCRIPTION_SEGMENTS)`.
- `require_choice` (`sob.py:86-90`) raises `InputError` on mismatch; `main` (`sob.py:285-287`) catches `InputError` → returns 1 with `REFUSE:` message.
- Test `test_unknown_subscription_sku_is_refused` (`test_sob_run0.py:181-196`) exercises the path: `subscribe ... "Citadelle Programme"` → exit 1, stderr contains `"subscription segment"`, `subscriptions` row count stays at 0.
- Positive case in `test_business_commands_persist_valid_deltas` (`test_sob_run0.py:142`) uses `"citadelle"` → exit 0, row inserted.

**Gap is closed without a SQL schema CHECK constraint**: enforcement is application-layer via `require_choice`. Acceptable defense-in-depth given the segment values are not security boundaries (no privilege escalation via SKU string). Failure mode is "wrong MRR bucket", not "code execution".

## New Code Introduced — Verified Safe

| Change | Location | Verdict |
|---|---|---|
| `ALLOWED_SUBSCRIPTION_SEGMENTS` frozenset | `sob.py:37-41` | Safe; immutable binding, no user input. |
| `normalize_text` before `require_choice` | `sob.py:179-180` | Order is correct — normalize first (length/blank check), then choice check. Avoids bypass via whitespace (`" citadelle "` is normalized to `"citadelle"`, then accepted). |
| `MAX_NAME_LENGTH` (200) cap on segment | `sob.py:180` | Bounds the value before the set lookup. |
| New test `test_unknown_subscription_sku_is_refused` | `test_sob_run0.py:181-196` | Uses list-form `subprocess.run` (line 75-81), controlled env, `tempfile.TemporaryDirectory` DB. No shell, no injection. |
| `prospect` segment still free-text | `sob.py:117` | **Not a regression** — pipeline segment is not a security boundary (no MRR rollup, no auth). Consistent with prior hardening scope. |
| Updated positive test value `"citadelle"` | `test_sob_run0.py:142` | Safe — fits allowlist exactly. |

## SQLite Injection Audit (re-verified after edit)

All SQL remains parameterized. New query paths in `handle_subscribe`:
- Line 184-186: `SELECT id FROM subscriptions WHERE lower(customer)=lower(?) AND status='subscribed'` — bound.
- Line 190-192: `SELECT 1 FROM pipeline WHERE lower(prospect)=lower(?)` — bound.
- Line 195-197: `INSERT INTO subscriptions(...) VALUES(?,?,?,?,?)` — bound.
- Line 199-202: `UPDATE pipeline SET stage='won'... WHERE lower(prospect)=lower(?)` — bound.
- Line 203-205: `INSERT INTO ledger(...) VALUES(?,?,?,?,?)` — bound.

No f-strings into SQL. No string concatenation. Verified.

## Other Hardened Controls (re-verified intact)

- URL validation: `normalize_url` (`sob.py:61-73`) — scheme/hostname/placeholder/localhost checks intact.
- `positive_amount` (`sob.py:76-83`): NaN/inf/negative rejected.
- `ALLOWED_STAGES` / `ALLOWED_CATEGORIES` / `ALLOWED_SEVERITIES` / `ALLOWED_EXPERIMENT_STATUSES` checks intact at `sob.py:164, 213, 227, 243`.
- `resolve_db_path` blank/`file:`/`://`/length/suffix rejection (unchanged in `sob_schema.py`).
- `init_schema` drift detection (unchanged in `sob_schema.py`).
- `with connection:` transactions on all writes (lines 129, 147, 165, 194, 216, 229, 244) intact.
- Test subprocess uses list-form args, no `shell=True` (`test_sob_run0.py:75-81`).
- All REFUSE/error messages go to `stderr` (`sob.py:268, 275, 286`); success goes to `stdout`.

## Pre-Existing LOW Findings (carry-over, none exacerbated by SKU change)

| Sev | Location | Note |
|---|---|---|
| LOW | `sob_schema.py:212, 229` | f-string DDL identifier interpolation from module constants — not exploitable, defense-in-depth gap. Unchanged by this edit. |
| LOW | `sob_schema.py:236` (`resolve_db_path`) | Allows NUL bytes and follows symlinks. Unchanged. |
| INFO | `sob.py:23-36` vs `sob_schema.py` CHECK constraints | Allow-list duplication. **Mitigated for `subscriptions.segment` by the new app-layer check**; future drift would still fail at `require_choice`. |

## Test Count Audit

Coordinator reports 13 PASS. Counting in `test_sob_run0.py`:
1. `test_initializer_creates_canonical_tables_and_views`
2. `test_initializer_is_idempotent_and_views_are_queryable`
3. `test_initializer_rejects_existing_schema_drift`
4. `test_cli_initializes_a_fresh_database_without_resource_warning`
5. `test_business_commands_persist_valid_deltas`
6. `test_invalid_values_are_refused_without_tracebacks`
7. `test_unknown_subscription_sku_is_refused` (NEW)
8. `test_missing_arguments_are_refused_without_tracebacks`
9. `test_unsafe_database_overrides_are_refused`
10. `test_oversized_url_is_refused`
11. `test_cycle_one_runbooks_exist`
12. `test_eight_domain_memories_are_initialized`
13. `test_forecast_contains_j28_baseline`

= 13 tests. Matches.

Note: `EXPECTED_TABLES`/`EXPECTED_VIEWS` (`test_sob_run0.py:18-41`) now include 6 new schema objects (`b2_domains`, `h1_horizons`, `cycles_12wy`, `rocks`, `sprints`, `scrums` + 4 new views: `sprint_uplink`, `rock_uplink`, `cycle_uplink`, `h1_uplink`). These are defined in `sob_schema.py` (not re-read here). If those objects were added to the runtime schema, the `test_initializer_creates_canonical_tables_and_views` test would fail unless `sob_schema.py` exposes matching constants — im

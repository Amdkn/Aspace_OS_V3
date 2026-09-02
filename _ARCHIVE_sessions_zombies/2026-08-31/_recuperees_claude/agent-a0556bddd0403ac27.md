---
session: agent-a0556bddd0403ac27
origine: claude
chemin_source: C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\06_Claude_Code_Bare\_ARCHIVE_2026-06-16_sessions\projects\C--Users-amado\9627821e-356b-43f0-b67d-695b6e8979c9\subagents\agent-a0556bddd0403ac27.jsonl
debut: 2026-06-10T19:31:19.067Z
fin: 2026-06-10T19:34:31.780Z
messages_utilisateur: 1
reponses_assistant: 1
titre: "Scaffold P1.4 — Vercel env vars (3-scope) for `C:/Users/amado/ASpace_OS_V2/30_Business_OS/10_Projects/abc/apps…"
---

## >>> UTILISATEUR #1

Scaffold P1.4 — Vercel env vars (3-scope) for `C:/Users/amado/ASpace_OS_V2/30_Business_OS/10_Projects/abc/apps/abc-os-community/`.

**ADR anchor**: `C:/Users/amado/ASpace_OS_V2/_SPECS/ADR/ADR-ABCOS-001_multitenant-supabase-strategy.md` — see D7 (env vars: NEXT_PUBLIC_SUPABASE_URL + NEXT_PUBLIC_SUPABASE_ANON_KEY, NEVER SERVICE_ROLE_KEY).

**Vercel contract**: `C:/Users/amado/ASpace_OS_V2/10_Tech_OS/11_Infra_13th_Doctor/06_MCP_Mastery/04_vercel/AGENTS.md` — see W2 (3-scope pattern via `update_env_variable` × 3 in parallel, verify with `list_env_variables`).

**Vercel project**:
- Project ID: `prj_HSw4IBR2omI5qegmEinOksr6xzo0`
- Team: `team_d3JjRK4fJUE9ACohbdlhv9Gc` (amd-lab)
- App: `abc-os-community`

**Deliverables** (no actual env var writes — those require Test Key Pragma from A0):

1. `apps/abc-os-community/.env.example` — new file:
   ```
   # Public — sent to the browser
   NEXT_PUBLIC_SUPABASE_URL=https://supabase.kalybana.com
   NEXT_PUBLIC_SUPABASE_ANON_KEY=<from A0 via Test Key Pragma>

   # Server-only — NEVER set in Vercel (used only on VPS via aspace_admin)
   # SUPABASE_SERVICE_ROLE_KEY=
   ```
   Add a comment block explaining the 3-scope rule and the Test Key Pragma.

2. `apps/abc-os-community/.env.local` — DO NOT create this. Just verify `.gitignore` has `.env*.local` covered (check lines 34+ per project CLAUDE.md).

3. `apps/abc-os-community/scripts/apply-vercel-env.ps1` — new PowerShell script:
   - Takes 2 args: `KEY`, `VALUE`
   - Calls `mcp__vercel__update_env_variable` × 3 in parallel (development, preview, production targets)
   - Re-verifies with `mcp__vercel__list_env_variables` after each
   - Hard guard: REFUSES to set any key matching `*SECRET*`, `*SERVICE_ROLE*`, `*PASSWORD*` (case-insensitive). Echo error and exit 1.
   - Doc-comment at top explaining when to use this script (P1.4 wiring)

4. `apps/abc-os-community/scripts/README.md` — new file:
   - How to use `apply-vercel-env.ps1`
   - Test Key Pragma 3-step (set in env User Windows → call script → rotate)
   - Example invocation for NEXT_PUBLIC_SUPABASE_URL
   - Example invocation for NEXT_PUBLIC_SUPABASE_ANON_KEY
   - Domain note: Vercel alias `abc-os-community.vercel.app` exists; custom domain `abc.kalybana.com` to be added later (DNS via Hostinger per `01_hostinger/AGENTS.md`)

**Doctrine compliance**:
- ZERO real keys in any file (Test Key Pragma)
- No `console.log` in prod (this is a script, not prod code, so `Write-Host` is fine for status)
- Per `04_vercel/AGENTS.md` W4: HITL for prod env-var changes — script must `Read-Host` confirmation before applying to production target
- Per project CLAUDE.md: PowerShell script, no backtick/em-dash in heredocs

**Workflow**:
- Step 1: Read ADR-ABCOS-001 D7 + `04_vercel/AGENTS.md` W2-W4
- Step 2: Read current `apps/abc-os-community/.gitignore` (lines 1-50)
- Step 3: Write the 3 files
- Step 4: Validate: `cd apps/abc-os-community && npx tsc --noEmit` (no TS files but check), `pwsh -NoProfile -Command "Get-Command -Syntax ./scripts/apply-vercel-env.ps1"` to check syntax
- Step 5: Git commit: `chore: scaffold P1.4 Vercel env vars (3-scope) — ADR-ABCOS-001 D7`

**Report back** with:
- 3 file paths + line counts
- Validation output
- Any deviations
- Final `<done>` tag
- A "How A0 applies this" section (exact commands to paste anon key + run script)

Do NOT actually run the script — that requires A0's anon key via Test Key Pragma.

### assistant

API Error: Request rejected (429) · Token Plan usage limit reached: Upgrade your Token Plan or purchase Credits for more usage. (2056)
